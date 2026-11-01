import requests,pathlib,json,pymupdf,concurrent.futures
jobs={'dimensional':'https://arxiv.org/pdf/2009.05968','height_distribution':'https://arxiv.org/pdf/1911.01762'}
def f(k,u):
 try:
  r=requests.get(u,timeout=40);pathlib.Path(k+'.pdf').write_bytes(r.content)
  if r.status_code==200:
   d=pymupdf.open(stream=r.content,filetype='pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
  return dict(service=k,url=u,status=r.status_code,date='2026-10-12',bytes=len(r.content))
 except Exception as e:return dict(service=k,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(lambda x:f(*x),jobs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
for k in jobs:
 if pathlib.Path(k+'.txt').exists():print(k,pathlib.Path(k+'.txt').read_text(encoding='utf8')[:10500])
