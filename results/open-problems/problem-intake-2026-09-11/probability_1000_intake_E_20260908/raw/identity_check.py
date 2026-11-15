import json, sys
from pathlib import Path
OUT = Path.home()/"Downloads"/"Probability_1000_intake_E_20260908"/"sources"
HERE = Path(__file__).resolve().parent
srcs = {json.loads(l)["source_id"]: json.loads(l) for l in (HERE.parent/"sources.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
res = {}
for sid, row in sorted(srcs.items()):
    p = OUT/sid/"text.txt"
    t = p.read_text(encoding="utf-8", errors="replace")
    head = " ".join(t.split())[:220]
    res[sid] = {"declared_title": row["title"], "url": row["url"], "first_220_chars": head,
                "chars": row.get("extracted_characters"), "pages": row.get("page_count")}
    print("=== "+sid+" ===")
    print("  declared: "+row["title"].encode("ascii","replace").decode())
    print("  text[:220]: "+head.encode("ascii","replace").decode())
(HERE/"source_identity_check_20260908.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print("\nwrote", len(res), "identity records")
