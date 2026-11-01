import urllib.request,pathlib,pymupdf,concurrent.futures
q={'minimal':'https://arxiv.org/pdf/2012.07129','unbalanced':'https://arxiv.org/pdf/2609.19426'}
def f(kv):
 k,u=kv
 try:
  b=urllib.request.urlopen(u,timeout=45).read();pathlib.Path(k+'.pdf').write_bytes(b);d=pymupdf.open(k+'.pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(f,q.items()));print(r)
with open('LITERATURE.md','a',encoding='utf8') as o:
 for k,u,s in r:o.write(f'- 2026-10-11 follow-up PDF {u}: {s}.\n')
