from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json
jobs={
'fast2022':'https://arxiv.org/pdf/2212.03632',
'feller2023':'https://arxiv.org/pdf/2310.17543',
'arxiv_targeted':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(ti:"random switching" OR ti:"randomly switched" OR ti:"piecewise deterministic") AND (all:"smoothness" OR all:"regularity")')+'&max_results=60&sortBy=submittedDate&sortOrder=descending',
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.5802/afst.1463',
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2095592930&per_page=50',
'openalex_search_alt':'https://api.openalex.org/works?search='+urllib.parse.quote('Some simple but challenging Markov processes')+'&per_page=5&select=id,title,doi,publication_year'}
def run(z):
 k,u=z
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'E0019 research'}),timeout=40) as f:b=f.read()
  Path(k+('.pdf' if '/pdf/' in u else '.json')).write_bytes(b)
  if '/pdf/' in u:
   import pymupdf
   d=pymupdf.open(k+'.pdf');Path(k+'.txt').write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(run,jobs.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for k,u,s,n in r:f.write(f'\n- 2026-10-12 {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(r,indent=2))
