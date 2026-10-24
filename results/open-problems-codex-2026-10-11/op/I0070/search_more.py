import requests, pathlib,json,concurrent.futures
ROOT=pathlib.Path(__file__).parent
Q={
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1007/s00030-025-01090-2',
'openalex_retry':'https://api.openalex.org/works?search=critical%20time%20regularization%20Hilbert&per-page=20',
'github_retry':'https://api.github.com/search/repositories?q=%22stochastic+maximal+regularity%22',
'semantic_doi':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s00030-025-01090-2?fields=title,year,citations.title,citations.year,citations.externalIds',
'arxiv_endpoint':'http://export.arxiv.org/api/query?search_query=all:%22time+regularization%22+AND+all:%22stochastic%22&max_results=30',
'crossref_endpoint':'https://api.crossref.org/works?query=critical%20Hilbert%20time%20regularization%20stochastic&filter=from-pub-date:2025-01-01&rows=20',
}
def run(item):
 k,u=item
 try:
  r=requests.get(u,timeout=35)
  (ROOT/(k+'.json')).write_bytes(r.content)
  out={'service':k,'date':'2026-10-12','url':u,'status':r.status_code,'bytes':len(r.content)}
  if k=='openalex_doi' and r.status_code==200:
   data=r.json(); wid=data['id'].split('/')[-1]
   cu=f'https://api.openalex.org/works?filter=cites:{wid}&per-page=100'
   cr=requests.get(cu,timeout=35);(ROOT/'openalex_citations.json').write_bytes(cr.content)
   out['citation_search']={'url':cu,'status':cr.status_code,'bytes':len(cr.content)}
 except Exception as e: out={'service':k,'date':'2026-10-12','url':u,'error':str(e)}
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: res=list(ex.map(run,Q.items()))
(ROOT/'search_more_log.json').write_text(json.dumps(res,indent=2),encoding='utf8')
print(json.dumps(res,indent=2))
