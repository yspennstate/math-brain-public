import urllib.request,urllib.parse,json,concurrent.futures
from pathlib import Path
q=urllib.parse.quote
urls={
'source_abs':'https://arxiv.org/abs/2609.01499','source_pdf':'https://arxiv.org/pdf/2609.01499',
'arxiv':'http://export.arxiv.org/api/query?search_query='+q('all:"gradient Gibbs" AND all:"free energy"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search='+q('gradient Gibbs measures minimal free energy')+'&per-page=20',
'crossref':'https://api.crossref.org/works?query='+q('gradient Gibbs measures Sheffield minimal')+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('gradient Gibbs measures minimal free energy')+'&limit=20&fields=title,authors,year,url,externalIds',
'github':'https://api.github.com/search/repositories?q='+q('gradient Gibbs measures'),
'sheffield_pdf':'https://arxiv.org/pdf/math/0304049'}
def fetch(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45); b=r.read(); Path(k+('.pdf' if b[:4]==b'%PDF' else '.txt')).write_bytes(b); msg=f'{k}: HTTP {r.status}, {len(b)} bytes'
 except Exception as e: msg=f'{k}: ERROR {e}'
 with Path('LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'\n- 2026-10-12: {k}, URL/query `{u}`. {msg}\n')
 return msg
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for s in ex.map(lambda kv:fetch(*kv),urls.items()):print(s)
