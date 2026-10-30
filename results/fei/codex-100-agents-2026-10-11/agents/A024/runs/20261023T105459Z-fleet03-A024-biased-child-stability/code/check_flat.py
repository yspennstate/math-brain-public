from pathlib import Path
from functools import lru_cache
from collections import Counter
import time,sys,json,hashlib
HERE=Path(__file__).resolve().parents[1]
prior=HERE.parent/'20261022T221625Z-fleet03-A024-biased-child-stability'/'code/check.py'
exec(compile(prior.read_text(encoding='utf-8').split("pilot='--pilot'")[0],str(prior),'exec'))
run=HERE;(run/'out').mkdir(exist_ok=True);start=time.monotonic();checks=0
pilot='--pilot' in sys.argv;activation='--activation' in sys.argv
cap=60 if pilot else (180 if activation else 600)
def deadline():
 if time.monotonic()-start>cap:raise TimeoutError('frozen runtime cap')
def save(name,data):
 with (run/'out'/name).open('w',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2)
@lru_cache(maxsize=4096)
def fwht(v):
 a=list(v);step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
  step*=2
 return tuple(a)
@lru_cache(maxsize=4096)
def ent_hist(N,hist):return add(*(sc(e(Q(s,N*N)),c) for s,c in hist if s))
@lru_cache(maxsize=4096)
def stats(v):
 w=fwht(v);N=len(v)
 return Q(w[0],N),Q(sum(s*s*i.bit_count() for i,s in enumerate(w)),N*N),ent_hist(N,tuple(sorted(Counter(s*s for s in w).items())))
@lru_cache(maxsize=4096)
def fiber_hist(N,hist):return add(*(sc(L(Q(a,N),Q(b,N)),c) for (a,b),c in hist))
def erasure(v,i):
 w=fwht(v);N=len(v);hist=Counter(tuple(sorted((abs(w[s]),abs(w[s^(1<<i)])))) for s in range(N) if not s&(1<<i))
 return fiber_hist(N,tuple(sorted(hist.items())))
def split(v,i):
 v0,v1=restrict(v,i,0),restrict(v,i,1)
 d=Q(sum(a!=b for a,b in zip(v0,v1)),len(v0))
 q=stats(tuple(a*b for a,b in zip(v0,v1)))[1]/2
 return v0,v1,d,q,erasure(v,i)
@lru_cache(maxsize=8)
def flats(n):
 N=1<<n;spaces={frozenset([0])};pending=list(spaces)
 while pending:
  W=pending.pop()
  for v in range(N):
   if v in W:continue
   U=W|frozenset(x^v for x in W)
   if U not in spaces:spaces.add(U);pending.append(U)
 out={0}
 for W in spaces:
  for a in range(N):out.add(sum(1<<(x^a) for x in W))
 return tuple(sorted(out,key=lambda x:(x.bit_count(),x)))
def truth(n,poly,E):
 return tuple((-1)**((sum((x&m)==m for m in poly)%2)^((E>>x)&1)) for x in range(1<<n))
def compress(m,i):return (m&((1<<i)-1))|((m>>(i+1))<<i)
def child(n,poly,E,i,b):
 terms=set()
 for m in poly:
  if m&(1<<i):
   if not b:continue
   m^=1<<i
  k=compress(m,i)
  if k in terms:terms.remove(k)
  else:terms.add(k)
 EE=0
 for x in range(1<<(n-1)):
  old=(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
  if (E>>old)&1:EE|=1<<x
 return n-1,tuple(sorted(terms)),EE
def anf(v):
 a=[int(x==-1) for x in v];n=(len(v)-1).bit_length()
 for i in range(n):
  for x in range(len(v)):
   if x&(1<<i):a[x]^=a[x^(1<<i)]
 return tuple(x for x,c in enumerate(a) if c)
def codim(n,E):return None if not E else n-(E.bit_count().bit_length()-1)
def pivot(n,poly,E):
 k=codim(n,E)
 if k is not None and k<=2:
  poly=anf(truth(n,poly,E));assert all(m.bit_count()<=2 for m in poly)
 edges=[m for m in poly if m.bit_count()==2]
 return (edges[0]&-edges[0]).bit_length()-1 if edges else 0
@lru_cache(maxsize=4096)
def annihilator(n,E):
 pts=[x for x in range(1<<n) if E>>x&1];a=pts[0]
 return frozenset(s for s in range(1<<n) if all(((s&(x^a)).bit_count()%2)==0 for x in pts))
def tensor(a,b):return tuple(x*y for y in b for x in a)
def component(C):
 v=(1,)
 for s in C:v=tensor(v,truth(*s))
 return v
def component_n(C):return sum(s[0] for s in C)
def component_pivot(C):
 offset=0
 for j,s in enumerate(C):
  if len(set(truth(*s)))>1:return j,pivot(*s),offset+pivot(*s)
  offset+=s[0]
 raise AssertionError('constant component')
def component_child(C,j,i,b):
 out=list(C);out[j]=child(*C[j],i,b);return tuple(out)
fixtures=[((0,(),0),),((0,(0,),0),),((1,(1,),0),),((2,(3,),0),),
 ((3,(3,4),sum(1<<x for x in [0,3,5,6])),),
 ((4,(3,12),(1<<0)|(1<<15)),),
 ((4,(1,4),sum(1<<x for x in [0,3,12,15])),),
 ((2,(3,),1),(1,(1,),0))]
cases=0;coords=0;affine_fibers=0;closure=0;dense=0;independent=0
if not activation:
 expected=[2,4,12,52,308]
 for n in range(4 if pilot else 5):
  fs=flats(n);eq(len(fs),expected[n]);child_fs=set(flats(n-1)) if n else set()
  mons=[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)]
  for code in range(1<<len(mons)):
   poly=tuple(m for j,m in enumerate(mons) if code>>j&1)
   nonlinear=any(m.bit_count()==2 for m in poly)
   for E in fs:
    v=truth(n,poly,E);k=codim(n,E)
    if k is not None and k<=2:
     eq(all(m.bit_count()<=2 for m in anf(v)),True);dense+=1
    if n:
     i=pivot(n,poly,E);_,_,d,q,B=split(v,i)
     le(sign(add(B,const(-4*d))),0);coords+=1
     ws=fwht(v);eq(d,Q(sum(ws[s]**2 for s in range(len(v)) if s>>i&1),len(v)**2))
     if k is not None and k>=3 and nonlinear:le(Q(1,4),d)
     for j in range(n):
      for bit in (0,1):
       c=child(n,poly,E,j,bit);eq(c[2] in child_fs,True);eq(truth(*c),restrict(v,j,bit));closure+=1
     if not nonlinear:
      W=annihilator(n,E) if E else frozenset([0])
      for j in range(n):
       Bj=erasure(v,j)
       if E and k and (1<<j) in W:
        u=Q(2,1<<k);eq(Bj,add(const(2*u*(1-u)),L(1-u,u)))
       else:eq(Bj,{})
       affine_fibers+=1
    _,I,H=stats(v);le(sign(add(H,const(-7*I))),0)
    cases+=1
    if cases%128==0:deadline()
  save('CHECKPOINT.json',{'completed_dimension':n,'descriptions':cases,'exact_assertions':checks,'runtime_seconds':time.monotonic()-start})
 # Direct O(4^n) character sums, independent of the butterfly implementation.
 for C in fixtures:
  v=component(C);N=len(v)
  direct=tuple(sum(v[x]*((-1)**((x&s).bit_count()%2)) for x in range(N)) for s in range(N))
  eq(direct,fwht(v));independent+=1
 scalar_L=scalar_R=0
 for aa in range(-8,9):
  for bb in range(-8,9):
   a,b=Q(aa,8),Q(bb,8);le(sign(add(L(a,b),const(-2*abs(a*b)))),0);scalar_L+=1
 for aa in range(-8,9):
  a=Q(aa,8)
  for bb in range(9-abs(aa)):
   beta=Q(bb,8)
   for rr in range(17):
    r=Q(rr,16);le(sign(add(rem(r,a,beta),const(-6*r*abs(beta)))),0);scalar_R+=1
 eq(sign(add(L(Q(1),Q(1)),const(-Q(19,10)))),1)
 eq(sign(rem(Q(1,2),Q(0),Q(1))),1)
 out={'descriptions':cases,'coordinate_checks':coords,'affine_fiber_checks':affine_fibers,'physical_restrictions':closure,'dense_absorptions':dense,'independent_spectra':independent,'scalar_L_pairs':scalar_L,'scalar_R_triples':scalar_R,'positive_controls':2}
else:
 @lru_cache(maxsize=1024)
 def repair(w,h):
  vw,vh=component(w),component(h);f=compose(vw,vh);_,I,H=stats(f)
  if len(set(f))==1:return Q(0),{},Q(0)
  side=0 if len(set(vw))>1 else 1;chosen=w if side==0 else h
  j,i,pos=component_pivot(chosen);idx=pos if side==0 else component_n(w)+pos
  f0,f1,d,q,B=split(f,idx);le(sign(add(B,const(-10*d))),0)
  zs=[]
  for bit in (0,1):
   cc=component_child(chosen,j,i,bit)
   actual=compose(component(cc),vh) if side==0 else compose(vw,component(cc))
   eq(actual,(f0,f1)[bit]);zs.append(repair(cc,h) if side==0 else repair(w,cc))
  It=d+sum(z[0] for z in zs)/2
  Ht=add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)),sc(add(zs[0][1],zs[1][1]),Q(1,2)))
  eq(It,I);eq(Ht,H);eq(sum(z[2] for z in zs),Q(0));le(sign(add(H,const(-13*I))),0)
  deadline();return It,Ht,Q(0)
 prefixes=0
 for w in fixtures[:4 if pilot else 8]:
  for h in fixtures[:4 if pilot else 8]:
   repair(w,h);cases+=1;f=compose(component(w),component(h));_,I,H=stats(f)
   for side,C in enumerate((w,h)):
    offset=0
    for j,s in enumerate(C):
     for i in range(s[0]):
      pos=offset+i;idx=pos if side==0 else component_n(w)+pos
      f0,f1,d,q,B=split(f,idx);zs=[]
      for bit in (0,1):
       cc=component_child(C,j,i,bit)
       actual=compose(component(cc),component(h)) if side==0 else compose(component(w),component(cc))
       eq(actual,(f0,f1)[bit]);zs.append(repair(cc,h) if side==0 else repair(w,cc))
      eq(I,d+sum(z[0] for z in zs)/2)
      eq(H,add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)),sc(add(zs[0][1],zs[1][1]),Q(1,2))))
      eq(sum(z[2] for z in zs),Q(0));prefixes+=1;deadline()
     offset+=s[0]
 out={'ordered_pairs':cases,'one_query_prefixes':prefixes,'cached_continuation_states':repair.cache_info().currsize}
out.update(status='PASS',mode=('activation_' if activation else '')+('pilot' if pilot else 'full'),exact_assertions=checks,runtime_seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(prior.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sign_certificates=sign_cache.cache_info().currsize)
save(('ACTIVATION_PILOT' if pilot else 'ACTIVATION')+'.json' if activation else ('PILOT.json' if pilot else 'VALIDATION.json'),out)
print(json.dumps(out))
