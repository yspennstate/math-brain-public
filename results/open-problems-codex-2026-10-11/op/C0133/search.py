import urllib.request,urllib.parse,json,concurrent.futures,time
from pathlib import Path
p=Path('.')
queries={
'arxiv_velocity':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"excited random walk" AND (all:velocity OR all:"law of large numbers")')+'&max_results=40',
'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('Excited random walks results methods open problems')+'&per-page=5',
'openalex_velocity':'https://api.openalex.org/works?search='+urllib.parse.quote('excited random walks zero velocity non transient')+'&per-page=30',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('excited random walks law large numbers zero velocity')+'&rows=30',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('excited random walks velocity')+'&limit=30&fields=title,authors,year,externalIds,abstract,url',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('excited random walks')+'&per_page=30'}
def get(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'C0133-mathematics-literature-audit'}),timeout=35); b=r.read();p.joinpath(k+'.json' if not k.startswith('arxiv') else k+'.xml').write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(lambda kv:get(*kv),queries.items()))
p.joinpath('search_log.json').write_text(json.dumps({'date':'2026-10-12','queries':queries,'results':results},indent=2),encoding='utf8')
for x in results:print(x)
