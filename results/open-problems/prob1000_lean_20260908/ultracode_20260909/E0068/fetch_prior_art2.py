import urllib.request, time, json
def get(url, tries=3):
    err=""
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "prob1000-e0068/0.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8","replace")
        except Exception as e:
            err=str(e); time.sleep(8+8*t)
    return "ERROR "+err
qs = {
 "zb_ultper": "https://api.zbmath.org/v1/document/_search?search_string=ultimately%20periodic%20evolution%20operator&results_per_page=40",
 "zb_varro": "https://api.zbmath.org/v1/document/_search?search_string=au%3AVarro%20evolution%20operator&results_per_page=40",
 "zb_quadauto": "https://api.zbmath.org/v1/document/_search?search_string=quadratic%20stochastic%20operator%20automorphism%20simplex%20periodic&results_per_page=40",
 "arxiv_ultper": "http://export.arxiv.org/api/query?search_query=abs:%22evolution%20operator%22%20AND%20abs:%22ultimately%20periodic%22&max_results=20",
 "arxiv_survey2011": "http://export.arxiv.org/api/query?search_query=ti:%22quadratic%20stochastic%20operators%20and%20processes%22&max_results=10",
}
out={}
for k,u in qs.items():
    out[k]=get(u); print("==",k,len(out[k]),out[k][:100].replace("\n"," ")); time.sleep(6)
json.dump(out,open("prior_art_raw2.json","w",encoding="utf-8"))
import re
for k in ["zb_ultper","zb_varro","zb_quadauto"]:
    if out[k].startswith("ERROR"): continue
    j=json.loads(out[k]); print("=====",k,j["status"]["nr_total_results"])
    for r in j["result"]:
        t=r.get("title",{}).get("title"); au=", ".join(a.get("name","") for a in r.get("contributors",{}).get("authors",[]))
        summ=(r.get("editorial_contributions") or [{}])[0].get("text","")
        print(f"- [{r.get('year')}] {t} -- {au} -- {r.get('source',{}).get('source','')}\n    {summ[:500]}")
for k in ["arxiv_ultper","arxiv_survey2011"]:
    if out[k].startswith("ERROR"): print(k,out[k]); continue
    for m in re.finditer(r"<title>(.*?)</title>.*?<id>(.*?)</id>.*?<published>(\d{4})", out[k], re.S):
        print(k, m.group(3), m.group(2), m.group(1)[:120].replace("\n"," "))
