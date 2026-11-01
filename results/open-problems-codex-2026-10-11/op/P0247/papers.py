from pathlib import Path
import urllib.request,concurrent.futures,re
import pymupdf
ROOT=Path(__file__).parent
qs=[('directed_paper','https://www.dmlett.com/archive/v11/DML23_v11_pp96-98.pdf'),('bht_cover','https://arxiv.org/pdf/2202.02255'),('wired_planar','https://arxiv.org/pdf/2602.21277'),('bht_hitting','https://arxiv.org/pdf/2601.03864')]
def get(q):
 name,url=q
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0247-research'}),timeout=40) as r:data=r.read()
  (ROOT/(name+'.pdf')).write_bytes(data)
  doc=pymupdf.open(stream=data,filetype='pdf');texts=[p.get_text() for p in doc]
  (ROOT/(name+'_full.txt')).write_text('\n'.join(texts),encoding='utf-8')
  res='OK '+str(len(data))
  print(name,'FIRST PAGE',texts[0][:4000],flush=True)
  for i,t in enumerate(texts):
   if re.search(r'7\.10|last (?:new |visited )?(?:vertex|state)|visited last',t,re.I):print(name,'PAGE',i+1,t[:9000],flush=True)
 except Exception as e:res=repr(e)
 with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'\n- 2026-10-12 primary paper fetch: {url}; {res}.\n')
 print(name,res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(get,qs))
