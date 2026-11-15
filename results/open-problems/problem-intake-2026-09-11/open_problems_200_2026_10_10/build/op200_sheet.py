"""Sheet of the picked problems: id|tier|source|locator|statement, plus source metadata, for writing the 200 list."""
import json, re, glob, csv, subprocess, sys, os
S = os.path.dirname(os.path.abspath(__file__))
B = "~/brain-repo/06_math_research"
def picks():
    ids = []
    for l in open(S + "/op200_picks.txt", encoding="utf-8"):
        if not l.startswith("#"):
            ids += re.findall(r"\b[A-Z]\d{4}\b", l.split("#")[0])
    out = []
    [out.append(i) for i in ids if i not in out]
    return out
def pool():
    return {json.loads(l)["problem_id"]: json.loads(l) for l in open(S + "/op200_pool.jsonl", encoding="utf-8")}
def sources():
    src = {}
    for f in glob.glob(B + "/probability_1000_intake_*/sources.jsonl"):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                r = json.loads(l); src[r["source_id"]] = r
    txt = subprocess.run(["git", "-C", "~/open-problems-repo", "show",
                          "origin/master:probability_campaign_2026_09/codex_20h_20260906/sources.jsonl"],
                         capture_output=True, encoding="utf-8", errors="replace").stdout
    for l in txt.splitlines():
        if l.strip():
            try:
                r = json.loads(l); src.setdefault(r["source_id"], r)
            except Exception:
                pass
    return src
def tiers():
    t = {}
    with open(B + "/probability_1000_intake_agent/RANKING_2026-09-07.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            t[r.get("id") or r.get("problem_id")] = r
    return t
if __name__ == "__main__":
    P, SRC, T = pool(), sources(), tiers()
    ids = picks()
    if sys.argv[1:2] == ["keys"]:
        print(list(next(iter(SRC.values())).keys())); print(list(next(iter(T.values())).keys())); sys.exit()
    a, b = int(sys.argv[1]), int(sys.argv[2])
    for i in ids[a:b]:
        r = P[i]; t = T.get(i, {})
        st = re.sub(r"\s+", " ", str(r.get("statement")))[:175]
        print("%s|t%s|%s|%s|%s" % (i, t.get("tier", "-"), r["source_id"][:26], re.sub(r"\s+", " ", str(r.get("locator")))[:22], st))
