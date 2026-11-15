"""Second literature pass for STATEMENT_PASS rows T418, T382, T391, T243: one arXiv query at a time, with retries."""
import re, time, urllib.parse, urllib.request
Q = [
 ("T418 data thinning", 'au:Takeno AND ti:"Data Thinning"'),
 ("T418 Iwazaki", 'au:Iwazaki AND abs:"GP-UCB"'),
 ("T418 Lattimore", 'au:Lattimore AND abs:kernel AND abs:"adaptive"'),
 ("T382 a", 'abs:realizability AND abs:planning AND abs:"reinforcement learning" AND abs:"lower bound" AND abs:linear'),
 ("T382 b", 'abs:"realizable" AND abs:"optimal action-value" AND abs:linear'),
 ("T391 a", 'abs:"diffusion models" AND abs:"intrinsic dimension" AND abs:minimax'),
 ("T391 b", 'abs:diffusion AND abs:"low-dimensional" AND abs:"iteration complexity"'),
 ("T243 a", 'ti:quantitative AND abs:"deep neural networks" AND abs:Gaussian AND abs:"central limit"'),
 ("T243 b", 'abs:"wide neural networks" AND abs:"Gaussian process" AND abs:"Wasserstein" AND abs:"rate"'),
]
out = open("stmt_lit2.out", "w", encoding="utf-8", newline="")
for k, q in Q:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 6})
    s = ""
    for attempt in range(3):
        try:
            s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-client/1.0"}), timeout=45).read().decode("utf-8")
            if "<entry>" in s or "totalResults" in s:
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
