import urllib.request, urllib.parse, json, concurrent.futures, pathlib, datetime
ROOT=pathlib.Path.cwd()
queries={
 'source_pdf':'https://arxiv.org/pdf/1806.03755',
 'source_abs':'https://arxiv.org/abs/1806.03755',
 'arxiv':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"generalized reflected Brownian"')+'&max_results=30',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('Exponential ergodicity and convergence for generalized reflected Brownian motion')+'&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('generalized reflected Brownian motion')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1806.03755?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"generalized reflected Brownian"')}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'E0110-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  target=ROOT/(name+('.pdf' if name.endswith('pdf') else '.txt'))
  target.write_bytes(data)
  outcome=f'{name}: OK {len(data)} bytes'
 except Exception as e: outcome=f'{name}: FAILED {e}'
 return name,url,outcome
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for name,url,outcome in pool.map(fetch,queries.items()):
  print(outcome,flush=True)
  with open('LITERATURE.md','a',encoding='utf-8') as f:f.write(f'\n- 2026-10-11 {name}: {url}\n  {outcome}\n')
try:
 import pymupdf
 doc=pymupdf.open('source_pdf.pdf')
 text='\n'.join(p.get_text() for p in doc)
 pathlib.Path('source.txt').write_text(text,encoding='utf-8')
 print(text[:24000])
except Exception as e:print('PDF extraction',e)
