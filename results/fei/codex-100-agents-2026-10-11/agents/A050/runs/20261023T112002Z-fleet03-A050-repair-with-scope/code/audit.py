from pathlib import Path
src=(Path(__file__).parent/'direct.py').read_text(encoding='utf-8').split("pilot='--pilot'")[0]
exec(compile(src,str(Path(__file__).parent/'direct.py'),'exec'),globals())
def close(v):
 if not v:return
 l,h=E.bounds(v);ck(l<=0<=h and h-l<F(1,1<<70))
def ell(u):
 ans={}
 for x,w in [(1+u,(1+u)**2/2),(1-u,(1-u)**2/2),(u,-u*u)]:
  if x and w:ans=E.add(ans,E.scale(E.logvec(x),w))
 return ans
for mask in range(256):
 t=tuple(1-2*((mask>>x)&1) for x in range(8));mu=F(sum(t),8);u=abs(mu);h,i=calc(t);sg=E.add({2:4*i},E.scale(h,-1));L=ell(u)
 # Every <=3-bit core is represented, including dummy embeddings.
 ge(E.add(sg,{2:u-1}))
 for s in (1,-1):
  jt=tuple(s if not(x&1) else t[x>>1] for x in range(16));hj,ij=calc(jt)
  close(E.add(hj,E.scale(h,F(-1,2)),{2:-2},L))
  ck(ij==(1-s*mu)/2+i/2)
  sj=E.add({2:4*ij},E.scale(hj,-1));close(E.add(sj,E.scale(sg,F(-1,2)),E.scale(L,-1),{2:2*s*mu}));ge(sj)
ck(12**6*13>4*7**6*28)
res={'status':'PASS','Boolean_cores':256,'activation_children':512,'assertions':count,'primitive_assertions':E.COUNT,'runtime_seconds':time.perf_counter()-start,'scope':'Direct character sums/direct pivots; all<=3bit factors satisfy mean surplus condition; activation identity and source increasing-alpha guard checked'}
(R/'out/AUDIT.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res))
