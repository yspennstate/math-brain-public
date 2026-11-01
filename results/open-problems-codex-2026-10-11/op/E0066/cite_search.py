import requests,pathlib,concurrent.futures,json
qs={'citing_source':'https://api.openalex.org/works?filter=cites:W1544252356&per-page=100','citing_survey':'https://api.openalex.org/works?filter=cites:W2081343974&search=bistochastic&per-page=100','crossref_dynamics':'https://api.crossref.org/works?query=trajectories%20doubly%20stochastic%20quadratic%20operators&rows=20','arxiv_dynamics':'http://export.arxiv.org/api/query?search_query=all:%22doubly+stochastic%22+AND+all:%22quadratic%22&max_results=30','semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2001.10444?fields=title,authors,year,abstract,citations.title,citations.year'}
def f(k,u):
 try:
  r=requests.get(u,timeout=40); pathlib.Path(k+'.txt').write_text(r.text,encoding='utf8'); return {'service':k,'url':u,'date':'2026-10-12','status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'service':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(lambda kv:f(*kv),qs.items()))
pathlib.Path('followup_log.json').write_text(json.dumps(out,indent=2),encoding='utf8'); print(out)
