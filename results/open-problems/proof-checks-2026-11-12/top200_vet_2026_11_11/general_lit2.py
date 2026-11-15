"""arXiv checks for the flagged general-list rows and two statement rows; one query at a time, with retries."""
import re, time, urllib.parse, urllib.request
Q = [
 ("TO13 Atiyah", 'abs:"Atiyah conjecture" AND (abs:"torsion-free" OR abs:"L^2-Betti" OR abs:"l2-Betti" OR abs:integrality)'),
 ("AN07 Sendov", 'abs:Sendov AND abs:conjecture AND (abs:polynomial OR abs:degree)'),
 ("DG06 Caratheodory", '(abs:"Caratheodory conjecture" OR abs:"Carathéodory conjecture") AND abs:umbilic'),
 ("DG09 stable Bernstein", 'abs:"stable" AND abs:"minimal hypersurfaces" AND (abs:"Bernstein") AND (abs:"R^7" OR abs:"seven" OR abs:"R^6" OR abs:"dimension 7")'),
 ("AN01 invariant subspace", 'abs:"invariant subspace problem" AND abs:Hilbert'),
 ("CO03 Erdos-Szekeres", '(abs:"Erdos-Szekeres" OR abs:"Erdős-Szekeres") AND abs:"convex position"'),
 ("CO08 Erdos-Sos", '(abs:"Erdos-Sos" OR abs:"Erdős-Sós") AND abs:conjecture AND abs:tree'),
]
out = open("general_lit2.out", "w", encoding="utf-8", newline="")
for k, q in Q:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 7})
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
        a = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:70]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        print(i, "|", t[:120], "|", a, "\n     ", ab[:700], file=out)
    out.flush()
    time.sleep(4)
out.close()
