import urllib.request,urllib.parse,json,concurrent.futures
from pathlib import Path
jobs={
'openalex_final.json':'https://api.openalex.org/works?search=circular%20Riesz%20gas&per-page=5',
'crossref_analytic.json':'https://api.crossref.org/works?query.bibliographic=Riesz%20gas%20free%20energy%20analyticity&rows=15',
'lead_2408.04437.pdf':'https://arxiv.org/pdf/2408.04437',
'arxiv_analytic.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Riesz" AND all:"free energy"')+'&max_results=40',
'openalex_citing.json':'https://api.openalex.org/works?filter=cites:553252f8121d409b67c20553a02f3f4f39fa019a&per-page=50'}
def f(it):
 name,url=it
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0324 research'}),timeout=30) as r:b=r.read()
  Path(name).write_bytes(b)
  if name.endswith('.pdf'):
   import pymupdf
   d=pymupdf.open(name);Path(name[:-4]+'.txt').write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text().replace('\x00','') for i,p in enumerate(d)),encoding='utf-8')
  res='OK '+str(len(b))
 except Exception as e:res=str(e)
 return dict(date='2026-10-12',service_file=name,url=url,result=res)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(f,jobs.items()))
p=Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+out,indent=2),encoding='utf-8')
for x in out:print(x['service_file'],x['result'])
