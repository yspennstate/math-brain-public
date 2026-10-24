import urllib.request,urllib.parse,concurrent.futures,json
from pathlib import Path
q=urllib.parse.quote
u={
'arxiv_recent':'https://export.arxiv.org/api/query?search_query='+q('all:"gradient Gibbs" AND submittedDate:[20260901 TO 20261012]')+'&max_results=50&sortBy=submittedDate&sortOrder=descending',
'arxiv_minimal':'https://export.arxiv.org/api/query?search_query='+q('all:"random surfaces" AND all:"variational"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex_retry':'https://api.openalex.org/works?search='+q('"gradient Gibbs"')+'&per_page=15',
'openalex_source':'https://api.openalex.org/works?search='+q('On the rigidity of sloped height functions')+'&per_page=5',
'openalex_citing':'https://api.openalex.org/works?filter=cites:arxiv:2609.01499&per_page=20',
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01499?fields=title,year,citations.title,citations.year,citations.externalIds',
'crossref_recent':'https://api.crossref.org/works?query='+q('"gradient Gibbs" "free energy"')+'&filter=from-pub-date:2026-09-01,until-pub-date:2026-10-12&rows=20',
'github_sheffield':'https://api.github.com/search/repositories?q='+q('Sheffield random surfaces')}
def f(k,url):
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research I0008'}),timeout=35);b=r.read();Path(k+'.txt').write_bytes(b);s=f'HTTP {r.status}, {len(b)} bytes'
 except Exception as e:s=f'ERROR {e}'
 with Path('LITERATURE.md').open('a',encoding='utf-8') as out:out.write(f'\n- 2026-10-12: {k}: `{url}`. {s}\n')
 print(k,s)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(lambda kv:f(*kv),u.items()))
