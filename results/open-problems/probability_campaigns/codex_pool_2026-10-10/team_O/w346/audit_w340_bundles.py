"""Read-only content and edge audit of w340's two staged bundles."""

import json
import re
import sqlite3
from pathlib import Path

root = Path("~/brain_workers/w340")
rows = [json.loads(x) for x in (root / "results.jsonl").read_text(encoding="utf-8-sig").splitlines() if x.strip()]
by_key = {r["entry_key"]: r for r in rows if "entry_key" in r}
db = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True)
cache = {}


def bodies(logical):
    if logical not in cache:
        cache[logical] = db.execute(
            "SELECT id,body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?", (logical,)
        ).fetchall()
    return cache[logical]


results = []
for name in ("bundle_001.json", "bundle_002.json"):
    bundle = json.loads((root / name).read_text(encoding="utf-8-sig"))
    entries = {e["key"]: e for e in bundle["entries"]}
    errors = []
    for key, entry in entries.items():
        if key not in by_key or not entry["statement"].endswith(by_key[key]["statement"]):
            errors.append((key, "entry/result statement mismatch"))
    dependencies = {key: [] for key in entries}
    for relation in bundle["relations"]:
        frm = relation["from_key"]
        quotes = re.findall(r'"([^"]*)"', relation["rationale"])
        if len(quotes) < 2 or frm not in entries:
            errors.append((frm, "missing FROM or quote pair"))
            continue
        from_quote, to_quote = quotes[:2]
        if from_quote not in entries[frm]["statement"]:
            errors.append((frm, "FROM quote mismatch"))
        if "to_key" in relation:
            key = relation["to_key"]
            if key not in entries or to_quote not in entries[key]["statement"]:
                errors.append((frm, "internal TO quote mismatch", key))
            if relation["kind"] == "depends_on":
                dependencies[frm].append(key)
        else:
            logical = relation["to_existing_logical"]
            if not any(to_quote in body for _, body in bodies(logical)):
                errors.append((frm, "external TO quote mismatch", logical))
    seen = set()
    active = set()

    def visit(key):
        if key in active:
            errors.append((key, "dependency cycle"))
            return
        if key in seen:
            return
        active.add(key)
        for nxt in dependencies[key]:
            visit(nxt)
        active.remove(key)
        seen.add(key)

    for key in entries:
        visit(key)
    results.append({"bundle": name, "entries": len(entries), "relations": len(bundle["relations"]),
                    "endpoint_quotes": 2 * len(bundle["relations"]),
                    "pending_audit_prefixes": sum("independent audit pending" in e["statement"] for e in entries.values()),
                    "errors": errors})

out = Path("~/brain_workers/w346/w340_bundle_validation.json")
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(results, ensure_ascii=False))
