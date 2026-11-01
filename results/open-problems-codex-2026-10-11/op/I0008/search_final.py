import urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
q=urllib.parse.quote
urls={
'arxiv_broad':'https://export.arxiv.org/api/query?search_query='+q('all:gradient AND all:Gibbs')+'&max_results=50&sortBy=submittedDate&sortOrder=descending',
'arxiv_conjectures':'https://export.arxiv.org/api/query?search_query='+q('all:"10.3.1" OR all:"10.3.2"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex_resolve':'https://api.openalex.org/works?search='+q('2609.01499')+'&per_page=5',
'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01499/citations?fields=title,year,externalIds&limit=100',
'github_exact':'https://api.github.com/search/repositories?q='+q('2609.01499'),
'crossref_source':'https://api.crossref.org/works?query.title='+q('On the rigidity of sloped height functions in d 3 and non-crossing surfaces')+'&rows=5'}
def f(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'I0008 research'}),timeout=30);b=r.read();Path(k+'.txt').write_bytes(b);msg=f'HTTP {r.status}; {len(b)} bytes'
 except Exception as e:msg=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'\n- 2026-10-12 {k}: `{u}`. {msg}\n')
 print(k,msg)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda kv:f(*kv),urls.items()))
