"""arXiv checks for the flagged general-list rows and two statement rows; one query at a time, with retries."""
import re, time, urllib.parse, urllib.request
Q = [
 ("CO12 unit distance", 'abs:"unit distance" AND (abs:Erdos OR abs:"Erdős") AND (abs:conjecture OR abs:disprove OR abs:construction)'),
 ("AG10 cubic fourfold", 'abs:"cubic fourfold" AND (abs:irrational OR abs:irrationality OR abs:"not rational")'),
 ("PD08 Leray-Hopf", 'abs:"Leray-Hopf" AND (abs:nonuniqueness OR abs:"non-uniqueness") AND abs:"Navier-Stokes"'),
 ("GE07 sofa", 'abs:"moving sofa"'),
 ("PD14 defocusing blow-up", 'abs:defocusing AND abs:supercritical AND abs:"blow-up" AND (abs:wave OR abs:"Schrödinger")'),
 ("T382 linear qstar", 'abs:"reinforcement learning" AND abs:realizability AND abs:"optimal value function" AND abs:linear'),
 ("T382 TensorPlan", 'all:TensorPlan'),
 ("T243 wide nets", 'abs:"neural networks" AND abs:"infinite-width" AND abs:"quantitative" AND (abs:Wasserstein OR abs:"total variation")'),
]
out = open("general_lit.out", "w", encoding="utf-8", newline="")
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
