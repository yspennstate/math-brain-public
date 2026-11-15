"""arXiv title/abstract searches for the eight NEW_DL_CANDIDATES rows; prints the newest hits for each."""
import re, sys, time, urllib.parse, urllib.request
Q = {
 "T418a": 'abs:"GP-UCB" AND abs:regret AND (abs:Matern OR abs:"Mat00e9rn" OR abs:optimal)',
 "T418b": 'au:Lattimore AND abs:"adaptive covariates"',
 "T382": '(abs:"q*-realizability" OR abs:"q*-realizable" OR abs:"linear q*") AND abs:reinforcement',
 "T391": 'abs:"diffusion models" AND abs:"intrinsic dimension" AND (abs:minimax OR abs:"iteration complexity" OR abs:"convergence")',
 "T243": 'abs:"deep neural networks" AND abs:"quantitative" AND abs:"central limit" AND abs:Gaussian',
}
QOLD = {
 "N01": 'abs:"ReLU" AND abs:"hidden layers" AND (abs:"maximum of" OR abs:"piecewise linear") AND abs:depth',
 "N02": 'ti:"sharpness-aware" AND (abs:"implicit bias" OR abs:"implicit regularization")',
 "N03": 'abs:"chain of thought" AND abs:transformer AND (abs:"sample complexity" OR abs:"provably") AND abs:"gradient"',
 "N04": 'ti:"rectified flow" AND (abs:straight OR abs:straightness)',
 "N05": 'abs:"real log canonical threshold" AND (abs:"deep" OR abs:"ReLU")',
 "N06": 'abs:"neural feature ansatz" OR abs:"average gradient outer product"',
 "N07": 'abs:transformers AND (abs:"TC^0" OR abs:"TC0") AND (abs:"log-precision" OR abs:"logarithmic precision" OR abs:"uniform")',
 "N08": 'ti:Adam AND abs:"implicit bias" AND (abs:homogeneous OR abs:margin)',
}
out = open("stmt_lit.out", "w", encoding="utf-8")
for k, q in Q.items():
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 5})
    try:
        s = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-client/1.0"}), timeout=60).read().decode("utf-8")
    except Exception as e:
        s = ""; print(k, "FETCH FAILED", e, file=out)
    print("==", k, file=out)
    for e in s.split("<entry>")[1:]:
        i = re.search(r"<id>(.*?)</id>", e, re.S).group(1).split("/abs/")[-1]
        t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        a = ", ".join(re.findall(r"<name>(.*?)</name>", e))[:60]
        ab = " ".join(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1).split())
        print(i, "|", t[:110], "|", a, "\n     ", ab[:230], file=out)
    time.sleep(3.2)
out.close()
