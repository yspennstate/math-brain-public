"""One line per top-400 row: list, id, title, ledger status, literature state, our moves, posted/solved signals.
usage: python -I -X utf8 rows_status.py <list.jsonl> <frontier rows dir> <memory dir> <out.tsv>
"""
import json, os, re, sys, glob
lst, rowsdir, memdir, out = sys.argv[1:5]
rows = [json.loads(l) for l in open(lst, encoding="utf-8") if l.strip()]
mem = {}
for f in os.listdir(memdir):
    m = re.findall(r"(?<![a-z0-9])t(\d{3})(?![0-9])", f.lower())
    for x in m:
        mem.setdefault("T" + x, []).append(f)
def jl(p):
    o = []
    if os.path.exists(p):
        for l in open(p, encoding="utf-8", errors="replace"):
            l = l.strip()
            if l:
                try: o.append(json.loads(l))
                except Exception: pass
    return o
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("list\trank\tid\tdomain\ttitle\tledger_status\tretired_reason\tlit\tmoves\tmove_kinds\tlast_move\tdossier\tmemories\n")
    for r in rows:
        rid = r["problem_id"]; d = os.path.join(rowsdir, rid)
        lit = ""
        p = os.path.join(d, "lit.json")
        if os.path.exists(p):
            try:
                j = json.load(open(p, encoding="utf-8"))
                lit = (str(j.get("status", "")) + " " + str(j.get("verdict", "")) + " " + str(j.get("note", ""))[:160]).strip()
            except Exception as e:
                lit = "unreadable"
        mv = jl(os.path.join(d, "moves.jsonl"))
        kinds = ",".join(sorted(set(str(m.get("kind")) for m in mv)))
        last = (mv[-1].get("at", "")[:10] + " " + str(mv[-1].get("what", mv[-1].get("why", "")))[:140]) if mv else ""
        fh.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in (
            r["list"], r["rank"], rid, r["domain"], r["title"], r.get("ledger_status", ""), r.get("retired_reason", "")[:200],
            lit, len(mv), kinds, last, "yes" if os.path.exists(os.path.join(d, "DOSSIER.md")) else "", ";".join(mem.get(rid, []))[:300])) + "\n")
print("rows", len(rows), "->", out)
