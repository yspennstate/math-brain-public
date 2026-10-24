import requests,concurrent.futures,json
q={
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/19-PS339',
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2995486210&per-page=100',
'arxiv_https':'https://export.arxiv.org/api/query?search_query=ti:%22activated%20random%20walks%22&max_results=60',
'crossref_diffusive':'https://api.crossref.org/works?query.title=Diffusive%20bounds%20for%20the%20critical%20density%20of%20activated%20random%20walks&rows=3',
'crossref_active':'https://api.crossref.org/works?query.title=activated%20random%20walks%20small%20sleeping%20rate&rows=15'}
def f(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=60);open(k+'.response','w',encoding='utf8').write(r.text)
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps({'date':'2026-10-12','service':k,'url':u,'http_status':r.status_code})+'\n')
  print(k,r.status_code,r.text[:200],flush=True)
 except Exception as e:print(k,e,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(f,q.items()))
