import urllib.request,urllib.parse,concurrent.futures,json
from pathlib import Path
qs=[('citing','https://api.openalex.org/works?filter=cites:W2172014396&per-page=100'),('oa_convex','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'entropic repulsion non Gaussian gradient field','per-page':40})),('arxiv2','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"convex" AND (all:"maximum" OR all:"extrema") AND all:"Ginzburg"','max_results':30})),('crossref2','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'pinned harmonic crystal positive origin','rows':15}))]
def f(nu):
 n,u=nu
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0073 research'}),timeout=40) as r:b=r.read()
  Path(n+('.xml' if n.startswith('arxiv') else '.json')).write_bytes(b);s='OK '+str(len(b))
 except Exception as e:s=repr(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write(f'\n- 2026-10-12 | {n} | `{u}` | {s}\n')
 print(n,s)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(f,qs))
