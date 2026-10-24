import urllib.request,urllib.parse,json,concurrent.futures,time
from pathlib import Path
jobs={
'source.pdf':'https://arxiv.org/pdf/2209.00396',
'arxiv.xml':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Riesz" AND (all:"analyticity" OR all:"Boursier")')+'&max_results=40',
'openalex.json':'https://api.openalex.org/works?search='+urllib.parse.quote('Decay of correlations and thermodynamic limit for circular Riesz gas')+'&per-page=10',
'openalex_analytic.json':'https://api.openalex.org/works?search='+urllib.parse.quote('Riesz gas free energy analyticity')+'&per-page=25',
'crossref.json':'https://api.crossref.org/works?query='+urllib.parse.quote('Riesz gas free energy analyticity')+'&rows=25',
'semantic.json':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2209.00396?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
'github.json':'https://api.github.com/search/repositories?q='+urllib.parse.quote('Riesz gas')}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0324-mathematical-literature-check/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  Path(name).write_bytes(data)
  result=f'{name}: OK {len(data)} bytes'
 except Exception as e: result=f'{name}: ERROR {e}'
 return {'date':'2026-10-12','service_file':name,'url':url,'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: out=list(ex.map(fetch,jobs.items()))
Path('search_log.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for x in out: print(x['result'])
try:
 import pymupdf
 d=pymupdf.open('source.pdf'); Path('source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
 print('PDF extracted',len(d))
except Exception as e: print('PDF extraction:',e)
