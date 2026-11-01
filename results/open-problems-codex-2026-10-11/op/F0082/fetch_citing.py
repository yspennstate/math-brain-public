import pathlib,urllib.request,concurrent.futures,pymupdf
q={'p_cyclic':'https://arxiv.org/pdf/2311.17687','cyclic':'https://arxiv.org/pdf/2109.13590','optimal_factor':'https://arxiv.org/pdf/2106.04524'}
def f(kv):
 k,u=kv
 try:
  b=urllib.request.urlopen(u,timeout=40).read();pathlib.Path(k+'.pdf').write_bytes(b);d=pymupdf.open(k+'.pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,q.items()));print(r)
with open('LITERATURE.md','a',encoding='utf8') as o:
 for k,u,s in r:o.write(f'- 2026-10-11 citation follow-up {u}: {s}.\n')
for k in q:
 p=pathlib.Path(k+'.txt')
 if p.exists():
  s=p.read_text(encoding='utf8');print(k,s[:6500])
