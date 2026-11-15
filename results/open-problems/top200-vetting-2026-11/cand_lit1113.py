"""arXiv check, newest first, for a batch of general-list rows.  usage: cand_lit1113.py <out> <first> <last> <query file>
Each query asks for the conjecture by name together with a word of resolution, so a hit list is short enough to read."""
import re, sys, time, urllib.parse, urllib.request

R = '(abs:proof OR abs:prove OR abs:proved OR abs:resolve OR abs:resolving OR abs:counterexample OR abs:disprove OR abs:settle)'
Q = [tuple(l.split("|", 1)) for l in open(sys.argv[4], encoding="utf-8").read().replace("RR", R).splitlines() if l.strip()]
out_path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
out = open(out_path, "w", encoding="utf-8", newline="")
for k, q in Q[a:b]:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 6})
    s = ""
    for attempt in range(3):
        try:
            s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-client/1.0"}), timeout=45).read().decode("utf-8")
            if "totalResults" in s:
                break
        except Exception as e:
            print(k, "attempt", attempt, "failed:", str(e)[:80], file=out)
        time.sleep(8)
    m = re.search(r"totalResults[^>]*>(\d+)<", s)
    print("==", k, "| total", m.group(1) if m else "?", file=out)
    for e in s.split("<entry>")[1:]:
        i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
        t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        au = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:70]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        print(i, "|", t[:130], "|", au, "\n     ", ab[:900], file=out)
    out.flush()
    time.sleep(4)
out.close()
print("queries", a, "to", min(b, len(Q)), "of", len(Q))
