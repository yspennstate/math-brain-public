import urllib.request,urllib.parse,concurrent.futures,pathlib,json
Q=urllib.parse.quote
urls={
'arxiv_https':'https://export.arxiv.org/api/query?search_query='+Q('all:"generalized reflected Brownian"')+'&max_results=50',
'arxiv_rate':'https://export.arxiv.org/api/query?search_query='+Q('all:"Brownian" AND all:"Tang" AND all:"ergodicity"')+'&max_results=30',
'openalex_retry':'https://api.openalex.org/works?filter=title.search:'+Q('generalized reflected Brownian')+'&per_page=50',
'crossref_retry':'https://api.crossref.org/works?query.title='+Q('Exponential ergodicity and convergence for generalized reflected Brownian motion')+'&rows=10',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+Q('generalized reflected Brownian')+'&limit=30&fields=title,year,authors,externalIds',
'github_retry':'https://api.github.com/search/repositories?q='+Q('Brownian ergodicity')}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:b=r.read()
  pathlib.Path(k+'.txt').write_bytes(b);s=f'OK {len(b)} bytes';print(k,s,flush=True)
 except Exception as e:s=str(e);print(k,s,flush=True)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as p:
 for k,u,s in p.map(get,urls.items()):
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: {u}\n  {s}\n')
