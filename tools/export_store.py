"""Dump the population store to versionable JSONL. Read-only on the store.

The store itself lives under local/, which .gitignore excludes, so until now the
math brain's CONTENT existed on one laptop and nowhere else - only its code was
deployed. This writes a deterministic text export that git can carry: one JSONL
file per table, rows sorted by primary key, keys sorted inside each row, so a
diff between two exports is a diff between two states of the brain rather than
a churn of binary blobs.

    python tools/export_store.py                 # write export/population/
    python tools/export_store.py --check         # exit 1 if the export is stale

Round-trips through import_store.py.

Committed artifacts carry no absolute local path and no username (AGENTS.md), but
the store's own text does: provenance rows name memory files and scratch copies
under the home directory, and some digested rows (node metadata, bundle
manifests) carry the same paths. Every string value is therefore written with
the home replaced by a token - {HOME} before a path separator, {HOME_KEY} for
the project key tools derive from it (C:\\Users\\name -> C--Users-name) - and
import_store.py puts the home back. Private repository names the store cites
are replaced the same way from local/export_private_names.json. A restore on
the exporting machine, or with --home naming its home and --private-names a
copy of that file, reproduces the store byte for byte, digests included. A
value that would not come back exactly, or that still names the home or a
private name after the substitution, makes the export refuse instead of
writing it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path

BUILD = Path(__file__).resolve().parent.parent
STORE = BUILD / "local" / "population" / "brain.sqlite3"
OUT = BUILD / "export" / "population"

# Primary key to sort each table by, so the export is byte-stable across runs.
TABLES = {
    "nodes": ("id",),
    "claims": ("id",),
    "edges": ("id",),
    "evidence": ("id",),
    "evidence_attestations": ("evidence_id",),
    "evidence_receipts": ("evidence_id",),
    "mistakes": ("id",),
    "reflexes": ("id",),
    "reflex_sources": ("reflex_id", "mistake_id"),
    "verification_events": ("id",),
    "verification_event_evidence": ("event_id", "evidence_id"),
    "bundle_manifests": ("id",),
    "bundle_members": ("bundle_id", "entry_key"),
    "schema_meta": ("version",),
    # the evidence-class layer of 2026-08-22 (claim_provenance.py): one row per claim that carries
    # a source or a measurement; the export refused on schema drift until it was listed here
    "claim_provenance": ("claim_id",),
    # edges retracted as wrong (store.retract_edge, 2026-10-07): the edge stays in edges.jsonl and a reader
    # of this export must drop every edge_id listed here, as the store's own readers do
    "edge_retractions": ("edge_id",),
}


HOME_TOKEN = "{HOME}"
HOME_KEY_TOKEN = "{HOME_KEY}"
# Private repository names the store cites (proof records typed from them), kept out of the
# export the same way: {name: token}, in a file under the gitignored local/. A restore on
# another machine needs a copy of it; without one those values keep their tokens and the
# digested rows among them stop verifying, which the restore reports.
PRIVATE_NAMES = BUILD / "local" / "export_private_names.json"
PRIVATE_TOKEN_PREFIX = "{PRIVATE_"


def private_names(path: Path | None = None) -> dict[str, str]:
    p = path or PRIVATE_NAMES
    if not p.exists():
        return {}
    names = json.loads(p.read_text(encoding="utf-8"))
    for name, token in names.items():
        if not name or not (token.startswith(PRIVATE_TOKEN_PREFIX) and token.endswith("}")):
            raise SystemExit(f"{p}: {name!r} -> {token!r}; a token must look like {{PRIVATE_...}}")
    return names


def home_spellings(home: str | Path | None = None,
                   private: dict[str, str] | None = None) -> list[tuple[str, str]]:
    """(literal, token) pairs in the order they are applied, in both directions.

    The home appears in the store four ways: as a Windows path inside JSON text
    (backslashes doubled), as a plain Windows path, as a slash path (file:///
    locators included), and as a project key. The first three are replaced only
    before a separator, so the separator that follows the token says which
    spelling to put back. The private names follow (``private`` None reads the
    local file; pass {} for none).
    """
    h = str(home if home is not None else Path.home())
    bs = h.replace("/", "\\").rstrip("\\")
    fs = bs.replace("\\", "/")
    esc = bs.replace("\\", "\\\\")
    key = re.sub(r"[^A-Za-z0-9]", "-", bs)
    names = private_names() if private is None else private
    return [
        (esc + "\\\\", HOME_TOKEN + "\\\\"),
        (bs + "\\", HOME_TOKEN + "\\"),
        (fs + "/", HOME_TOKEN + "/"),
        (key, HOME_KEY_TOKEN),
    ] + sorted(names.items(), key=lambda kv: -len(kv[0]))


def tokenise(value, spellings: list[tuple[str, str]]):
    """Replace the home and the private names in one exported value; refuse a value that would not come back."""
    if not isinstance(value, str):
        return value
    if "{HOME" in value or PRIVATE_TOKEN_PREFIX in value:
        raise SystemExit(f"a stored value already contains a token: {value[:120]!r}")
    out = value
    for literal, token in spellings:
        out = out.replace(literal, token)
    low = out.lower()
    for literal, _ in spellings:
        stem = literal.rstrip("\\/").lower()
        if stem in low:
            raise SystemExit(f"a stored value still names the home or a private name after tokenising: {out[:160]!r}")
    if detokenise(out, spellings) != value:
        raise SystemExit(f"a stored value does not survive tokenising: {value[:160]!r}")
    return out


def detokenise(value, spellings: list[tuple[str, str]]):
    """Put the home and the private names back into one exported value."""
    if not isinstance(value, str) or "{" not in value:
        return value
    for literal, token in spellings:
        value = value.replace(token, literal)
    return value


def dump_table(conn: sqlite3.Connection, table: str, keys: tuple[str, ...],
               spellings: list[tuple[str, str]] | None = None) -> str:
    """Return the JSONL text for one table, deterministically ordered.

    With ``spellings`` every string value is tokenised (the committed form);
    without it the rows are dumped as stored.
    """
    order = ", ".join(f'"{k}"' for k in keys)
    rows = conn.execute(f'SELECT * FROM "{table}" ORDER BY {order}').fetchall()
    if spellings is None:
        return "".join(
            json.dumps(dict(row), sort_keys=True, ensure_ascii=False) + "\n" for row in rows
        )
    return "".join(
        json.dumps({k: tokenise(v, spellings) for k, v in dict(row).items()},
                   sort_keys=True, ensure_ascii=False) + "\n"
        for row in rows
    )


def build() -> tuple[dict[str, str], dict[str, int]]:
    if not STORE.exists():
        raise SystemExit(f"no store at {STORE}")
    conn = sqlite3.connect(f"file:{STORE}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        present = {
            r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
        missing = sorted(set(TABLES) - present)
        extra = sorted(present - set(TABLES))
        if missing or extra:
            # Schema drift is the failure this repo has hit before; refuse rather
            # than silently export a partial brain.
            raise SystemExit(
                f"schema drift - missing tables {missing}, unknown tables {extra}; "
                "update TABLES in this file before exporting"
            )
        spellings = home_spellings()
        texts = {t: dump_table(conn, t, keys, spellings) for t, keys in sorted(TABLES.items())}
    finally:
        conn.close()
    counts = {t: text.count("\n") for t, text in texts.items()}
    return texts, counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="compare against the export on disk and exit 1 if it is stale",
    )
    args = ap.parse_args()

    texts, counts = build()
    manifest = {
        "source": STORE.relative_to(BUILD).as_posix(),
        "path_tokens": {
            HOME_TOKEN: "the exporting machine's home directory, before a path separator",
            HOME_KEY_TOKEN: "that home as a project key (C--Users-name)",
            **{
                token: "a private repository name, kept in local/export_private_names.json"
                for token in sorted(private_names().values())
            },
        },
        "counts": counts,
        "digests": {
            t: hashlib.sha256(text.encode("utf-8")).hexdigest()
            for t, text in sorted(texts.items())
        },
    }
    manifest_text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"

    if args.check:
        stale = []
        for table, text in texts.items():
            path = OUT / f"{table}.jsonl"
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(table)
        if (OUT / "MANIFEST.json").exists():
            if (OUT / "MANIFEST.json").read_text(encoding="utf-8") != manifest_text:
                stale.append("MANIFEST.json")
        else:
            stale.append("MANIFEST.json")
        if stale:
            print("STALE: " + ", ".join(sorted(stale)))
            return 1
        print(f"current: {sum(counts.values())} rows across {len(counts)} tables")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    for table, text in texts.items():
        (OUT / f"{table}.jsonl").write_text(text, encoding="utf-8", newline="\n")
    (OUT / "MANIFEST.json").write_text(manifest_text, encoding="utf-8", newline="\n")
    print(f"wrote {sum(counts.values())} rows across {len(counts)} tables to {OUT}")
    for table in sorted(counts):
        if counts[table]:
            print(f"  {table:32s} {counts[table]:6d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
