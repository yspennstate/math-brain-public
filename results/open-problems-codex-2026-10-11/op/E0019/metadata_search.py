from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures
jobs={
'one_dim_2025':'https://arxiv.org/pdf/2506.02274',
'linear2024_metadata':'https://api.crossref.org/works/10.1137/24M1696172',
'feller2023_metadata':'https://api.crossref.org/works/10.1007/s00440-024-01307-y',
'singular2020_metadata':'https://api.crossref.org/works/10.1137/20M1364345',
'torus2017_metadata':'https://api.crossref.org/works/10.1088/1361-6544/aaa04f',
'source_metadata':'https://api.crossref.org/works/10.5802/afst.1468'}
def run(z):
 k,u=z
 try:
  with urllib.request.urlopen(u,timeout=40) as f:b=f.read()
  Path(k+('.pdf' if '/pdf/' in u else '.json')).write_bytes(b)
  if '/pdf/' in u:
   import pymupdf
   d=pymupdf.open(k+'.pdf');Path(k+'.txt').write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
   print(k,d[0].get_text()[:2200])
  else:
   x=json.loads(b)['message'];print(k,x.get('title'),x.get('container-title'),x.get('volume'),x.get('issue'),x.get('page'),x.get('article-number'),x.get('published'))
  return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(run,jobs.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for k,u,s,n in r:f.write(f'\n- 2026-10-12 {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(r,indent=2))
