from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures
ROOT=Path(__file__).parent
qs=[
('arxiv_last','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"last vertex" AND all:"random walk"')+'&max_results=30'),
('arxiv_transitive','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"vertex-transitive" AND (all:"cover time" OR all:"last")')+'&max_results=40'),
('openalex_retry','https://api.openalex.org/works?search='+urllib.parse.quote('last visited vertex random walk')+'&per_page=10'),
('openalex_source_retry','https://api.openalex.org/works?search='+urllib.parse.quote('Reversible Markov Chains Random Walks Graphs Aldous Fill')+'&per_page=5'),
('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('vertex transitive cover time')+'&limit=10&fields=title,authors,year,url'),
('crossref_exact','https://api.crossref.org/works?query='+urllib.parse.quote('Aldous Fill last vertex uniform distribution')+'&rows=10'),
]
def get(q):
 name,url=q
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0247-research/1.0'}),timeout=35) as r:data=r.read()
  (ROOT/(name+'.txt')).write_bytes(data);res='OK '+str(len(data))
 except Exception as e:res=repr(e)
 with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'\n- 2026-10-12 {name}: {url}\n  Result: {res}.\n')
 return name,res
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(get,qs):print(r,flush=True)
# If source indexed, inspect its citing works without claiming a comprehensive search.
for filename in ['openalex_source_retry.txt','openalex_source.txt']:
 if not (ROOT/filename).exists():continue
 try:
  j=json.loads((ROOT/filename).read_text())
  for w in j.get('results',[]):
   print('SOURCE CANDIDATE',w['id'],w['title'])
   if 'reversible markov chains' in w['title'].lower() and 'random walks' in w['title'].lower():
    url='https://api.openalex.org/works?filter=cites:'+w['id'].split('/')[-1]+'&per-page=100'
    print(get(('openalex_citing',url)))
 except Exception as e:print(repr(e))
