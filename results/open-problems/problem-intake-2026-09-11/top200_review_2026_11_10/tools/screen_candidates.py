"""Screen replacement candidates against the rows already on the lists.

usage: python -I -X utf8 screen_candidates.py list.jsonl candidates.tsv out.tsv [LISTNAME ...]
For each candidate, every listed or retired row whose title or statement matches one of its keywords is recorded.
Prints one short line per candidate: FREE, or the ids it overlaps.
"""
import csv, json, re, sys

rows = [json.loads(x) for x in open(sys.argv[1], encoding="utf-8") if x.strip()]
cands = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
only = set(sys.argv[4:])


def text(r):
    return " ".join(str(r.get(k, "")) for k in ("title", "statement", "summary"))


def lname(r):
    return r.get("list") or r.get("list_name") or ""


out = []
for c in cands:
    pat = re.compile(c["keywords"], re.I)
    hits_t, hits_s = [], []
    for r in rows:
        if only and lname(r) not in only:
            continue
        rid = r.get("id") or r.get("problem_id") or ""
        if pat.search(str(r.get("title", ""))):
            hits_t.append(rid)
        elif pat.search(text(r)):
            hits_s.append(rid)
    out.append([c["key"], c["title"], ",".join(hits_t), ",".join(hits_s)])
    print("%s | %s | title: %s | text: %s" % (c["key"], c["title"][:58], ",".join(hits_t) or "-", ",".join(hits_s[:8]) or "-"))
with open(sys.argv[3], "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["key", "title", "title_hits", "text_hits"])
    w.writerows(out)
