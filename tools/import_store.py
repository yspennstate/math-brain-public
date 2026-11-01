"""Rebuild a population store from the JSONL export. Never writes the live store.

An export you cannot restore from is not a backup, so this is the other half of
export_store.py and the two are tested against each other:

    python tools/import_store.py --out local/population/restored.sqlite3
    python tools/import_store.py --roundtrip     # rebuild to a temp db and
                                                 # re-export it; digests must match

The target path must not be the live store; pass --force only if you genuinely
mean to overwrite an existing file that is not it.

The export writes the home directory as a token (see export_store.py); the home
put back is this machine's unless --home names another. Rows whose digests
cover a path verify only when the home put back is the exporting machine's.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import tempfile
from pathlib import Path

BUILD = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BUILD / "tools"))

from export_store import (  # noqa: E402
    OUT,
    PRIVATE_TOKEN_PREFIX,
    STORE,
    TABLES,
    build,
    detokenise,
    dump_table,
    home_spellings,
    private_names,
)

# Insert order respects the foreign keys declared in the schema.
ORDER = [
    "schema_meta",
    "nodes",
    "claims",
    "edges",
    "evidence",
    "evidence_attestations",
    "evidence_receipts",
    "mistakes",
    "reflexes",
    "reflex_sources",
    "verification_events",
    "verification_event_evidence",
    "bundle_manifests",
    "bundle_members",
    # added to TABLES on 2026-08-22 but not here, so no restore carried the provenance layer
    # and --roundtrip failed on it; the check below keeps the two lists together
    "claim_provenance",
    # after edges: each row names an edge (2026-10-07)
    "edge_retractions",
]


def read_export(home: str | None = None, private: dict[str, str] | None = None) -> dict[str, list[dict]]:
    if sorted(ORDER) != sorted(TABLES):
        raise SystemExit(
            f"ORDER and export_store.TABLES disagree: only in TABLES {sorted(set(TABLES) - set(ORDER))}, "
            f"only in ORDER {sorted(set(ORDER) - set(TABLES))}"
        )
    missing = [t for t in TABLES if not (OUT / f"{t}.jsonl").exists()]
    if missing:
        raise SystemExit(f"export incomplete - missing {missing}; run export_store.py")
    spellings = home_spellings(home, private)
    rows = {}
    left = 0
    for table in TABLES:
        text = (OUT / f"{table}.jsonl").read_text(encoding="utf-8")
        rows[table] = [
            {k: detokenise(v, spellings) for k, v in json.loads(line).items()}
            for line in text.splitlines()
            if line.strip()
        ]
        left += sum(
            1 for r in rows[table] for v in r.values() if isinstance(v, str) and PRIVATE_TOKEN_PREFIX in v
        )
    if left:
        print(f"  {left} values keep a private-name token: no --private-names file covers them")
    return rows


def schema_ddl() -> list[str]:
    """The live store's DDL; on a machine without one, the schema the code creates.

    Reading the live store alone meant a restore failed anywhere the store did not
    already exist, which is the case a restore is for (2026-10-13). The code's schema
    is SCHEMA_SQL plus the two tables other modules create on first use.
    """
    if STORE.exists():
        src = sqlite3.connect(f"file:{STORE}?mode=ro", uri=True)
    else:
        if str(BUILD / "src") not in sys.path:
            sys.path.insert(0, str(BUILD / "src"))
        from math_brain.provenance import INDEX as PROVENANCE_INDEX
        from math_brain.provenance import SCHEMA as PROVENANCE_SCHEMA
        from math_brain.store import EDGE_RETRACTIONS_SQL, SCHEMA_SQL

        src = sqlite3.connect(":memory:")
        src.executescript(
            ";\n".join([SCHEMA_SQL, EDGE_RETRACTIONS_SQL, PROVENANCE_SCHEMA, PROVENANCE_INDEX]) + ";"
        )
    try:
        return [
            r[0]
            for r in src.execute(
                "SELECT sql FROM sqlite_master WHERE sql IS NOT NULL ORDER BY type DESC"
            )
        ]
    finally:
        src.close()


def build_db(path: Path, rows: dict[str, list[dict]]) -> None:
    """Create the schema (see schema_ddl), then replay the export."""
    ddl = schema_ddl()

    conn = sqlite3.connect(path)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        for stmt in ddl:
            conn.execute(stmt)
        for table in ORDER:
            payload = rows.get(table) or []
            if not payload:
                continue
            cols = list(payload[0])
            placeholders = ", ".join("?" for _ in cols)
            names = ", ".join(f'"{c}"' for c in cols)
            conn.executemany(
                f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})',
                [tuple(r[c] for c in cols) for r in payload],
            )
        conn.commit()
        broken = conn.execute("PRAGMA foreign_key_check").fetchall()
        if broken:
            raise SystemExit(f"foreign key check failed on {len(broken)} rows")
    finally:
        conn.close()


def digest_failures(path: Path) -> tuple[set[str], set[str]]:
    """Node ids and bundle manifest ids whose stored digest their row does not reproduce.

    The live store carries some of these already (the reader refuses them: 34 node rows
    on 2026-09-25, 25 of them the orphan 'b2 replacement' rows of 2026-08-10); a restore
    must not add any, and one with the wrong home put back adds exactly the digested
    rows that name a path.
    """
    if str(BUILD / "src") not in sys.path:
        sys.path.insert(0, str(BUILD / "src"))
    from math_brain.models import GraphNode, NodeKind, content_hash

    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        nodes = {
            r["id"]
            for r in conn.execute("SELECT * FROM nodes")
            if GraphNode(
                id=r["id"],
                kind=NodeKind(r["kind"]),
                title=r["title"],
                body=r["body"],
                metadata=json.loads(r["metadata_json"]),
                created_at=r["created_at"],
            ).digest()
            != r["digest"]
        }
        manifests = {
            r["id"]
            for r in conn.execute("SELECT id, digest, payload_json FROM bundle_manifests")
            if content_hash(json.loads(r["payload_json"])) != r["digest"]
        }
    finally:
        conn.close()
    return nodes, manifests


def roundtrip() -> int:
    """Export -> import -> re-export. Byte equality is the pass condition.

    Two comparisons. The rebuilt store, exported again, must reproduce the files
    on disk. And when the export is current, the rebuilt store dumped as stored
    must equal the live store dumped as stored - the second does not go through
    the tokenising at all, so a substitution that lost or mangled a value cannot
    pass it.
    """
    rows = read_export()
    spellings = home_spellings()
    live_texts, _ = build()
    # per table: a file that is not the live store's current export (stale, or edited) cannot
    # be compared with the live store, and is named rather than passed over
    stale = sorted(
        t for t, text in live_texts.items() if (OUT / f"{t}.jsonl").read_text(encoding="utf-8") != text
    )
    live_nodes_bad, live_manifests_bad = digest_failures(STORE)
    with tempfile.TemporaryDirectory() as tmp:
        db = Path(tmp) / "roundtrip.sqlite3"
        build_db(db, rows)
        conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        live = sqlite3.connect(f"file:{STORE}?mode=ro", uri=True)
        live.row_factory = sqlite3.Row
        try:
            bad, raw_bad = [], []
            for table, keys in sorted(TABLES.items()):
                got = dump_table(conn, table, keys, spellings)
                want = (OUT / f"{table}.jsonl").read_text(encoding="utf-8")
                if got != want:
                    bad.append(table)
                if table not in stale and dump_table(conn, table, keys) != dump_table(live, table, keys):
                    raw_bad.append(table)
        finally:
            conn.close()
            live.close()
        nodes_bad, manifests_bad = digest_failures(db)
    added = sorted(nodes_bad - live_nodes_bad) + sorted(manifests_bad - live_manifests_bad)
    if bad or raw_bad or added:
        if bad:
            print("ROUNDTRIP FAILED on: " + ", ".join(bad))
        if raw_bad:
            print("REBUILT STORE DIFFERS FROM THE LIVE STORE on: " + ", ".join(raw_bad))
        if added:
            print(f"THE RESTORE BREAKS {len(added)} DIGESTS the live store keeps, e.g. {added[:3]}")
        return 1
    total = sum(len(v) for v in rows.values())
    print(f"roundtrip OK - {total} rows across {len(TABLES)} tables reproduce byte-for-byte")
    compared = len(TABLES) - len(stale)
    print(f"  the rebuilt store equals the live store, values as stored, on {compared} of {len(TABLES)} tables")
    if stale:
        print("  not compared (the files are not the live store's current export): " + ", ".join(stale))
    print(
        f"  digests: {len(nodes_bad)} node rows and {len(manifests_bad)} bundle manifests fail their stored "
        f"digest in the rebuilt store, the same ones the live store carries"
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="path for the rebuilt store")
    ap.add_argument("--roundtrip", action="store_true", help="verify export/import agree")
    ap.add_argument("--force", action="store_true", help="overwrite an existing --out file")
    ap.add_argument("--home", help="the home directory to put back for the path tokens "
                    "(default: this machine's; name the exporting machine's to reproduce its digests)")
    ap.add_argument("--private-names", type=Path, help="a copy of local/export_private_names.json "
                    "(default: this checkout's)")
    args = ap.parse_args()

    if args.roundtrip:
        return roundtrip()
    if not args.out:
        ap.error("pass --out PATH or --roundtrip")
    out = args.out.resolve()
    if out == STORE.resolve() and STORE.exists():
        raise SystemExit("refusing to overwrite the live store")
    if out.exists() and not args.force:
        raise SystemExit(f"{out} exists; pass --force to overwrite")
    if out.exists():
        out.unlink()
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = read_export(args.home, private_names(args.private_names) if args.private_names else None)
    build_db(out, rows)
    print(f"rebuilt {sum(len(v) for v in rows.values())} rows into {out}")
    nodes_bad, manifests_bad = digest_failures(out)
    print(
        f"  {len(nodes_bad)} node rows and {len(manifests_bad)} bundle manifests fail their stored digest"
        " (the store of 2026-09-25 carried 34 and 0; more means the home put back is not the exporting"
        " machine's, or the private names file is missing)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
