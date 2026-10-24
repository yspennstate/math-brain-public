import urllib.request, pathlib,concurrent.futures,json,xml.etree.ElementTree as E
q={
'arxiv_matching':'https://export.arxiv.org/api/query?search_query=ti:matching%20AND%20(all:Poisson%20OR%20au:Holroyd)&max_results=80',
'arxiv_noncross':'https://export.arxiv.org/api/query?search_query=all:%22non-crossing%22%20AND%20all:Poisson&max_results=40',
'geometric':'https://arxiv.org/pdf/0909.0575',
'openalex_retry':'https://api.openalex.org/works?search=non-crossing%20Poisson%20matching&per_page=20',
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP185',
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867?fields=title,citations.title,citations.year,citations.externalIds',
'crossref_minimal':'https://api.crossref.org/works?query.title=minimal%20matchings%20point%20processes&rows=15',
'github_broad':'https://api.github.com/search/repositories?q=noncrossing+matching'}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read()
  suffix='.pdf' if k=='geometric' else '.xml' if k.startswith('arxiv') else '.json';pathlib.Path(k+suffix).write_bytes(b)
  if suffix=='.pdf':
   import pymupdf
   d=pymupdf.open(k+suffix);pathlib.Path(k+'.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  s=f'OK ({len(b)} bytes)'
 except Exception as e:s=str(e)
 return k,u,s
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=8).map(get,q.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for k,u,s in results:f.write(f'- 2026-10-11 {k}: {u} — {s}.\n')
print(results)
