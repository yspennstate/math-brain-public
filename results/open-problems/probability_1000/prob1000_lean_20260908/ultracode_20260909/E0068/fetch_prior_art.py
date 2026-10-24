# Prior-art fetches for E0068 (arXiv API, zbMATH open API). Plain HTTP, no search API.
import urllib.request, urllib.parse, time, json, re, sys
out = {}
def get(url, tries=3):
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "prob1000-e0068/0.1 (research; contact yitz)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            err = str(e); time.sleep(4 + 4*t)
    return "ERROR " + err
queries = {
 "arxiv_survey2011": "http://export.arxiv.org/api/query?search_query=ti:%22quadratic%20stochastic%20operators%20and%20processes%22&max_results=10",
 "arxiv_bernstein_qso": "http://export.arxiv.org/api/query?search_query=abs:%22quadratic%20stochastic%22%20AND%20abs:Bernstein&max_results=50",
 "arxiv_bernstein_algebra": "http://export.arxiv.org/api/query?search_query=all:%22Bernstein%20algebras%22&max_results=50",
 "zb_plenary": "https://api.zbmath.org/v1/document/_search?search_string=ti%3Aplenary%20train&results_per_page=40",
 "zb_rozikov_bernstein": "https://api.zbmath.org/v1/document/_search?search_string=quadratic%20stochastic%20operator%20Bernstein%20idempotent&results_per_page=40",
 "zb_periodic": "https://api.zbmath.org/v1/document/_search?search_string=Bernstein%20algebra%20periodic%20plenary&results_per_page=40",
}
for k, u in queries.items():
    txt = get(u)
    out[k] = txt
    print("==", k, len(txt), txt[:120].replace("\n"," "))
    time.sleep(3.5)
json.dump(out, open("prior_art_raw.json","w",encoding="utf-8"))
