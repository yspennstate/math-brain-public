"""Full abstracts for two follow-up questions (Cartan-Hadamard in all dimensions; zero divisors over F_2)."""
import re, time, urllib.parse, urllib.request
U = [("id 2610.37817 2610.17662 2607.15632", {"id_list": "2610.37817,2610.17662,2607.15632"}),
     ("zero divisors torsion-free", {"search_query": 'abs:"zero divisors" AND abs:"torsion-free" AND (abs:"group algebra" OR abs:"group ring") AND abs:counterexample', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 6}),
     ("Kaplansky zero-divisor F_2", {"search_query": 'abs:Kaplansky AND abs:"zero-divisor conjecture" AND (abs:"finitely presented" OR abs:"characteristic 2" OR abs:"F_2")', "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 6})]
out = open("general_lit5.out", "w", encoding="utf-8", newline="")
for k, p in U:
    s = urllib.request.urlopen(urllib.request.Request("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(p), headers={"User-Agent": "research-client/1.0"}), timeout=45).read().decode("utf-8")
    print("==", k, file=out)
    for e in s.split("<entry>")[1:]:
        i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
        t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        au = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:90]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        print(i, "|", t[:130], "|", au, "\n     ", ab[:1700], file=out)
    time.sleep(4)
out.close()
