from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures
jobs={
'lead_2609.28503.pdf':'https://arxiv.org/pdf/2609.28503',
'lead_2509.08659.pdf':'https://arxiv.org/pdf/2509.08659',
'lead_2411.01355.pdf':'https://arxiv.org/pdf/2411.01355',
'lead_2309.08951.pdf':'https://arxiv.org/pdf/2309.08951',
'openalex_retry.json':'https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=Riesz&per_page=10',
'openalex_source_retry.json':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2209.00396',
'crossref_retry.json':'https://api.crossref.org/works?query.title=Decay%20of%20correlations%20and%20thermodynamic%20limit%20for%20circular%20Riesz%20gas&rows=5',
'arxiv_recent.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Riesz gas"')+'&sortBy=submittedDate&sortOrder=descending&max_results=60'}
def f(it):
 name,url=it
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r: b=r.read()
  Path(name).write_bytes(b)
  if name.endswith('.pdf'):
   import pymupdf
   d=pymupdf.open(name);Path(name[:-4]+'.txt').write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
  result='OK '+str(len(b))
 except Exception as e: result=str(e)
 return {'date':'2026-10-12','service_file':name,'url':url,'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: out=list(ex.map(f,jobs.items()))
p=Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+out,indent=2),encoding='utf-8')
for x in out:print(x['service_file'],x['result'])
