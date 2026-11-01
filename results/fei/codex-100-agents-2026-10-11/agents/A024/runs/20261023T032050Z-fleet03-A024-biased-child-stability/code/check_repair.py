from pathlib import Path
import sys,time,json,hashlib
from functools import lru_cache
HERE=Path(__file__).resolve().parents[1]
prior=HERE.parent/'20261022T221625Z-fleet03-A024-biased-child-stability'/'code'/'check.py'
source=prior.read_text(encoding='utf-8')
exec(compile(source.split("pilot='--pilot'")[0],str(prior),'exec'))
run=HERE
start=time.monotonic()
pilot='--pilot' in sys.argv
mode='activation' if '--activation' in sys.argv else ('pilot' if pilot else 'full')
limit=180 if mode=='activation' else (60 if pilot else 600)
def deadline():
 if time.monotonic()-start>limit:raise TimeoutError('frozen runtime limit')
def truth(n,poly,point):
 return tuple((-1)**((sum((x&m)==m for m in poly)%2) ^ (point==x)) for x in range(1<<n))
def compress(m,i):return (m&((1<<i)-1))|((m>>(i+1))<<i)
def child(n,poly,point,i,b):
 terms=set()
 for m in poly:
  if m&(1<<i):
   if not b:continue
   m^=1<<i
  k=compress(m,i)
  if k in terms:terms.remove(k)
  else:terms.add(k)
 pt=None if point is None or ((point>>i)&1)!=b else compress(point,i)
 return n-1,tuple(sorted(terms)),pt
def pivot(n,poly):
 edges=[m for m in poly if m.bit_count()==2]
 return (edges[0]&-edges[0]).bit_length()-1 if edges else 0
@lru_cache(None)
def local(v,i):return split(v,i)
@lru_cache(None)
def goodtree(n,poly,point):
 v=truth(n,poly,point);a,I,H=stats(v)
 if n==0 or len(set(v))==1:return Q(0),{},Q(0)
 i=pivot(n,poly);v0,v1,d,q,B=local(v,i)
 le(sign(add(B,const(-5*d))),0)
 c0=child(n,poly,point,i,0);c1=child(n,poly,point,i,1)
 eq(truth(*c0),v0);eq(truth(*c1),v1)
 z0=goodtree(*c0);z1=goodtree(*c1)
 total=d+(z0[0]+z1[0])/2
 drop=add(H,sc(add(stats(v0)[2],stats(v1)[2]),-Q(1,2)))
 entropy=add(drop,sc(add(z0[1],z1[1]),Q(1,2)))
 eq(total,I);eq(entropy,H);le(sign(add(H,const(-8*I))),0)
 return total,entropy,Q(0)
cases=0;coordinates=0;activation_states=0;prefixes=0
if mode!='activation':
 for n in range(4 if pilot else 5):
  mons=[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)]
  for code in range(1<<len(mons)):
   poly=tuple(m for j,m in enumerate(mons) if (code>>j)&1)
   for point in [None]+list(range(1<<n)):
    v=truth(n,poly,point)
    for i in range(n):
     for b in (0,1):eq(truth(*child(n,poly,point,i,b)),restrict(v,i,b))
    if n:
     i=pivot(n,poly);v0,v1,d,q,B=local(v,i)
     le(sign(add(B,const(-5*d))),0);coordinates+=1
     if any(m.bit_count()==2 for m in poly) and n>=3:le(Q(1,4),d)
     if not any(m.bit_count()==2 for m in poly):
      for j in range(n):
       _,_,dj,_,Bj=local(v,j)
       le(sign(add(Bj,const(-5*dj*(1-dj)))),0)
       if point is not None:
        u=Q(2,1<<n)
        eq(Bj,add(const(2*u*(1-u)),L(1-u,u)))
       coordinates+=1
    goodtree(n,poly,point)
    cases+=1;deadline()
 # An independent spectral implementation on all <=3-bit nonconstant-sign polynomials.
 independent=0
 for n in range(4):
  fixtures=[tuple([1<<i for i in range(n)]),tuple([(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)])]
  for poly in fixtures:
   for pt in [None,0]:
    v=truth(n,poly,pt)
    direct=tuple(Q(sum(v[x]*((-1)**((x&s).bit_count()%2)) for x in range(1<<n)),1<<n) for s in range(1<<n))
    eq(direct,walsh(v));independent+=1
 out={'descriptions':cases,'coordinate_checks':coordinates,'independent_character_spectra':independent,'tree_states':goodtree.cache_info().currsize}
else:
 fixtures=[(0,(),None),(0,(0,),None),(1,(1,),None),(2,(3,),None),(2,(3,),0),(3,(3,4),None),(3,(3,4),0),(3,(1,2),0)]
 seen=set()
 @lru_cache(None)
 def continuation(w,h):
  global activation_states
  vw,vh=truth(*w),truth(*h);f=compose(vw,vh);a,I,H=stats(f)
  if len(set(f))==1:return Q(0),{},Q(0)
  side=0 if len(set(vw))>1 else 1
  chosen=w if side==0 else h;n,poly,point=chosen;i=pivot(n,poly)
  j=i if side==0 else w[0]+i
  f0,f1,d,q,B=local(f,j)
  le(sign(add(B,const(-14*d))),0)
  c0,c1=child(*chosen,i,0),child(*chosen,i,1)
  z0=continuation(c0,h) if side==0 else continuation(w,c0)
  z1=continuation(c1,h) if side==0 else continuation(w,c1)
  eq(f0,compose(truth(*c0),vh) if side==0 else compose(vw,truth(*c0)))
  eq(f1,compose(truth(*c1),vh) if side==0 else compose(vw,truth(*c1)))
  total=d+(z0[0]+z1[0])/2
  drop=add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)))
  entropy=add(drop,sc(add(z0[1],z1[1]),Q(1,2)))
  eq(total,I);eq(entropy,H);eq((z0[2]+z1[2])/2,Q(0))
  le(sign(add(H,const(-17*I))),0)
  activation_states+=1;deadline()
  return total,entropy,Q(0)
 for w in fixtures:
  for h in fixtures:
   continuation(w,h);cases+=1
   f=compose(truth(*w),truth(*h));a,I,H=stats(f)
   for side,chosen in enumerate((w,h)):
    for i in range(chosen[0]):
     j=i if side==0 else w[0]+i
     f0,f1,d,q,B=local(f,j)
     cs=[child(*chosen,i,b) for b in (0,1)]
     zs=[continuation(c,h) if side==0 else continuation(w,c) for c in cs]
     eq(I,d+sum(z[0] for z in zs)/2)
     eq(H,add(add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2))),sc(add(zs[0][1],zs[1][1]),Q(1,2))))
     eq(sum(z[2] for z in zs)/2,Q(0));prefixes+=1;deadline()
 out={'ordered_pairs':cases,'one_query_prefixes':prefixes,'nonconstant_continuation_states':activation_states,'memoized_states':continuation.cache_info().currsize}
out.update(status='PASS',mode=mode,exact_assertions=checks,runtime_seconds=time.monotonic()-start,prior_helper_sha256=hashlib.sha256(prior.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sign_certificates=sign_cache.cache_info().currsize)
(run/'out').mkdir(exist_ok=True)
(run/'out'/('ACTIVATION.json' if mode=='activation' else ('PILOT.json' if pilot else 'VALIDATION.json'))).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
