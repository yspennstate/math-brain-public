import requests, pathlib, concurrent.futures, datetime
p=pathlib.Path('.')
queries={
'source': 'https://arxiv.org/pdf/0902.4207',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22bistochastic%22+AND+all:%22quadratic%22&max_results=50',
'openalex':'https://api.openalex.org/works?search=quadratic%20bistochastic%20operators&per-page=30',
'crossref':'https://api.crossref.org/works?query=quadratic%20bistochastic%20operators&rows=30',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=quadratic%20bistochastic%20operators&limit=30&fields=title,year,authors,url,externalIds,abstract',
'github':'https://api.github.com/search/repositories?q=quadratic+bistochastic+operators'}
def f(k,u):
 try:
  r=requests.get(u,timeout=50); name=k+('.pdf' if k=='source' else '.json' if k not in ['arxiv'] else '.xml'); p.joinpath(name).write_bytes(r.content); return k,r.status_code,len(r.content),u
 except Exception as e: return k,str(e),u
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(lambda kv:f(*kv),queries.items()))
p.joinpath('search_log.json').write_text(__import__('json').dumps({'date':'2026-10-12','results':results},indent=2),encoding='utf8')
for r in results: print(r)
try:
 import pymupdf
 d=pymupdf.open('source.pdf'); p.joinpath('source.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+page.get_text() for i,page in enumerate(d)),encoding='utf8')
except Exception as e: print('PDF',e)
