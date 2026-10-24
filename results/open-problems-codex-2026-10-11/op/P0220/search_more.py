import urllib.request,urllib.parse,concurrent.futures,json
from pathlib import Path
q=[('openalex_retry','https://api.openalex.org/works?search='+urllib.parse.quote('Longest increasing subsequences from patience sorting to the Baik Deift Johansson theorem')+'&per-page=5'),('openalex_drift','https://api.openalex.org/works?search='+urllib.parse.quote('Hammersley drift')+'&per-page=10'),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Hammersley stationary')+'&limit=10&fields=title,authors,year,url,externalIds'),('crossref_focused','https://api.crossref.org/works?query.title='+urllib.parse.quote('Hammersley stationary')+'&rows=20'),('arxiv_focused','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Hammersley" AND (all:"drift" OR all:"Plancherel" OR all:"leftmost")')+'&max_results=30'),('github_drift','https://api.github.com/search/repositories?q='+urllib.parse.quote('"drift-jump" Hammersley'))]
def f(pair):
 n,u=pair
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0220-research/1.0'}),timeout=30).read();Path(n+'.raw').write_bytes(data);s='OK '+str(len(data))
 except Exception as e:s=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write('\n- 2026-10-11 '+n+': '+u+'\n  Result: '+s+'\n')
 return n,s
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(f,q):print(r)
