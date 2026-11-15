"""Staleness check, arXiv lane: for each list problem not yet checked through OpenAlex, query the arXiv export API
(relevance order) and score papers since 2019 by word overlap with the problem; flag abstracts that read like an answer.
Output op200_stale4.tsv in the same columns as op200_stale2.tsv (DOI column carries the arXiv id)."""
import json, re, sys, time, urllib.request, urllib.parse, os
import xml.etree.ElementTree as ET
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import op200_sheet as H
P = H.pool(); keep = [l.strip() for l in open(S + "/op200_keep.txt", encoding="utf-8") if l.strip()]
done = set()
for l in open(S + "/op200_stale2.tsv", encoding="utf-8"):
    p = l.split("\t")
    if len(p) > 2 and p[1] != "ERR":
        done.add(p[0])
extra = [a for a in sys.argv[1:]]
keep = [k for k in keep if k not in done] + [e for e in extra if e not in keep]
print("to check", len(keep), flush=True)

STOP = set("the a an of for in on and or to with by is are be as at from that this its it any every all under into than "
           "random prove show determine whether does do can must there exist exists existence law laws limit problem "
           "question conjecture case general open which when what versus via given some new".split())
ANS = re.compile(r"(conjecture[ds]? (of|by)|question (of|by|posed|raised)|open problem|we (answer|resolve|settle|disprove|"
                 r"confirm|prove the conjecture)|answering|resolving|settling|counterexample|affirmative|negative answer)", re.I)
A = "{http://www.w3.org/2005/Atom}"


def words(t):
    return {w for w in re.findall(r"[a-z][a-z\-]{2,}", t.lower()) if w not in STOP}


def get(url):
    for k in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "op200-staleness/1.0"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            time.sleep(5 * (k + 1))
    return None


def query(ws):
    q = " AND ".join("all:" + w for w in ws)
    x = get("http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "max_results": 25, "sortBy": "relevance"}))
    time.sleep(3.2)
    if x is None:
        return None
    out = []
    for e in ET.fromstring(x).iter(A + "entry"):
        t = " ".join((e.findtext(A + "title") or "").split())
        ab = " ".join((e.findtext(A + "summary") or "").split())
        y = int((e.findtext(A + "published") or "0")[:4] or 0)
        i = (e.findtext(A + "id") or "").rsplit("/abs/", 1)[-1]
        out.append((t, y, ab, i))
    return out


fo = open(S + "/op200_stale4.tsv", "w", encoding="utf-8")
for pid in keep:
    r = P[pid]
    tw0 = [w for w in re.findall(r"[a-z][a-z\-]{3,}", str(r["title"]).lower()) if w not in STOP]
    tw0 = sorted(dict.fromkeys(tw0), key=len, reverse=True)
    rows = None
    for n in (4, 3, 2):
        if len(tw0) < n and n != 2:
            continue
        rows = query(tw0[:n])
        if rows:
            break
    if rows is None:
        fo.write(pid + "\tERR\n"); fo.flush(); continue
    pw = words(str(r["title"]) + " " + str(r.get("statement", ""))[:400])
    best = []
    for t, y, ab, i in rows:
        if y < 2019:
            continue
        sc = len(pw & words(t + " " + ab[:1500])) / max(1, len(pw))
        best.append((sc, y, "ANS" if ANS.search(ab) else "", "arXiv:" + i, t))
    best.sort(reverse=True)
    if not best:
        fo.write("%s\t0.00\t0\t\t\t(no arXiv hit since 2019)\n" % pid)
    for sc, y, flag, i, t in best[:3]:
        fo.write("%s\t%.2f\t%s\t%s\t%s\t%s\n" % (pid, sc, y, flag, i, t[:150]))
    fo.flush()
fo.write("DONE\n")
fo.close()
