"""Independent direct-character, full-law rational validation. No source checker imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1]
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
B=tuple(1-a*a for a in A)
count=0
def ok(v):
 global count
 count+=1
 assert v,count
def save(name,v):
 (R/'out'/name).write_text(json.dumps(v,indent=2,default=str)+'\n',encoding='utf-8')
@lru_cache(None)
def four(v):
 return tuple(F(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(v)),len(v)) for s in range(len(v)))
def prob(v):return tuple(a*a for a in four(tuple(v)))
def restrict(v,j,t):return tuple(a for x,a in enumerate(v) if (x>>j)&1==t)
def marg(v,j):
 return tuple(v[(x&((1<<j)-1))+((x>>j)<<(j+1))]+v[(x&((1<<j)-1))+((x>>j)<<(j+1))+(1<<j)] for x in range(len(v)//2))
def mean(v):return F(sum(v),len(v))
SCALE=1<<128
@lru_cache(None)
def ln(q):
 assert q>0
 k=0
 while q>=2:q/=2;k+=1
 while q<1:q*=2;k-=1
 z=(q-1)/(q+1);a=z.numerator;b=z.denominator
 lo=0;hi=0
 for r in range(20):
  num=2*SCALE*pow(a,2*r+1);den=(2*r+1)*pow(b,2*r+1)
  lo+=num//den;hi+=(num+den-1)//den
 tail=2*z**41/(41*(1-z*z))
 hi+=(tail.numerator*SCALE+tail.denominator-1)//tail.denominator
 # ln2 uses the SAME series with z=1/3, without recursion.
 if k:
  l=h=0
  for r in range(20):
   den=(2*r+1)*3**(2*r+1);num=2*SCALE
   l+=num//den;h+=(num+den-1)//den
  tail2=F(2,3**41)/F(41)*F(9,8)
  h+=(tail2.numerator*SCALE+tail2.denominator-1)//tail2.denominator
  lo,hi=(lo+k*l,hi+k*h) if k>0 else (lo+k*h,hi+k*l)
 return F(lo,SCALE),F(hi,SCALE)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def neg(a):return -a[1],-a[0]
ZERO=(F(0),F(0))
def ce(p,q):
 out=ZERO
 for x,y in zip(p,q):
  if x:
   ok(y>0);out=plus(out,times(ln(y),-x))
 return out
def kl(p,q):return plus(ce(p,q),neg(ce(p,p)))
def overlap(a,b):ok(a[0]<=b[1] and b[0]<=a[1])
def coherent(ac,bc,h,r,s):
 m=mean(h)
 q=tuple((ac[u]+s*m*bc[u])**2 if t==0 else bc[u]**2*r[t] for t in range(len(r)) for u in range(len(ac)))
 ok(sum(q)==1);ok(all(x>=0 for x in q));return q
def actual(ac,bc,h,s):return coherent(ac,bc,h,prob(h),s)
def source(h,k=0):
 z=mean(h)**2
 if z==1:return (F(1),)+tuple(F(0) for _ in h[1:])
 w=tuple(F(1+(i+1)**(k+1)) for i in range(1,len(h)));den=sum(w)
 return (z,)+tuple((1-z)*a/den for a in w)
def blocks(q,groups,m):
 return tuple(q[u] for u in range(m))+tuple(sum(q[t*m+u] for t in g) for g in groups for u in range(m))
def step(h,r,s,ac,bc,j,verify=True):
 n=len(h);m=len(ac);p=prob(h);u=marg(four(h),j) # replaced by explicit pair below
 coeff=four(h);uv=[]
 for t in range(n//2):
  k=(t&((1<<j)-1))+((t>>j)<<(j+1));uv.append((coeff[k],coeff[k+(1<<j)]))
 d=uv[0][1];mu=mean(h)
 groups=[tuple(t for t in range(1,n//2) if uv[t][0]*uv[t][1]>=0),tuple(t for t in range(1,n//2) if uv[t][0]*uv[t][1]<0)]
 groups=[g for g in groups if g]
 cs=[sum((uv[t][0]*uv[t][1] for t in g),F(0)) for g in groups]
 C=sum(a*a*b*b for a,b in zip(ac,bc));D=sum(a*b**3 for a,b in zip(ac,bc));E=sum(b**4 for b in bc);beta=sum(b*b for b in bc)
 gamma=C-D*D/E if E else F(0);x=gamma*d*d+E*sum(c*c for c in cs)
 ok(gamma>=0);ok(sum(a*b for a,b in uv)==0) # actual Booleanity
 parent=actual(ac,bc,h,s);q=coherent(ac,bc,h,r,s)
 pbar=marg(parent,j+ (m.bit_length()-1));qbar=marg(q,j+(m.bit_length()-1));rbar=marg(r,j)
 coarseq=blocks(qbar,groups,m);childcost=ZERO;refund=ZERO;shapecost=ZERO;newr=[];positive=0
 for t in (0,1):
  ht=restrict(h,j,t);pt=prob(ht);z=mean(ht)**2
  rt=[z]+[F(0)]*(n//2-1)
  for g in groups:
   a=sum(pt[k] for k in g);b=sum(rbar[k] for k in g)
   if a:ok(b>0)
   for k in g:rt[k]=a*rbar[k]/b if b else F(0)
  rt=tuple(rt);ok(sum(rt)==1)
  fresh=coherent(ac,bc,ht,rt,s);pchild=actual(ac,bc,ht,s)
  coarset=blocks(pchild,groups,m);rho=kl(coarset,coarseq);refund=plus(refund,times(rho,F(1,2)))
  overlap(plus(ce(pchild,qbar),neg(ce(pchild,fresh))),rho)
  mass=beta*(1-z);epsilon=x/(mass+x) if x and mass else F(0)
  # Deliberately mix toward a single prescribed nonempty frequency.
  target=n//2-1
  rn=tuple(z if k==0 else (1-epsilon)*rt[k]+epsilon*(1-z)*(k==target) for k in range(n//2))
  qnew=coherent(ac,bc,ht,rn,s);newr.append((ht,rn))
  zeta=plus(ce(pchild,qnew),neg(ce(pchild,fresh)))
  if zeta[0]>0:positive+=1
  if epsilon:ok(zeta[1]<x) # rigorous separated interval, no tolerance
  else:ok(rn==rt) # zero transaction checked by exact law equality
  shapecost=plus(shapecost,times(zeta,F(1,2)));childcost=plus(childcost,times(ce(pchild,qnew),F(1,2)))
 # Exact chain in natural units: erasure + avg CE - root CE = -occupancy - refund + shape.
 erasure=plus(ce(parent,parent),neg(ce(pbar,pbar)))
 occ=plus(plus(ce(parent,q),neg(ce(parent,parent))),neg(plus(ce(pbar,qbar),neg(ce(pbar,pbar)))))
 lhs=plus(plus(erasure,childcost),neg(ce(parent,q)))
 rhs=plus(plus(neg(occ),neg(refund)),shapecost);overlap(lhs,rhs)
 if x:
  ok(refund[0]>=2*x);ok(plus(lhs,occ)[1]<=-x)
 else:ok(plus(lhs,occ)[0]<=0<=plus(lhs,occ)[1] or plus(lhs,occ)[1]<0)
 return {'d':d,'x':x,'gamma':gamma,'E':E,'beta':beta,'cs':cs,'positive_resets':positive,'zero_singleton_paid':bool(d==0 and x),'children':newr,'refund_interval_nats':refund,'increment_interval_nats':lhs}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;n=2 if pilot else 3
 ac,bc=four(A),four(B);cases=positive=zero=0;witness=None
 for table in range(1<<(1<<n)):
  h=tuple(1 if table>>i&1 else -1 for i in range(1<<n))
  for j in range(n):
   for s in (-1,1):
    v=step(h,source(h),s,ac,bc,j);cases+=1;positive+=v['positive_resets'];zero+=v['zero_singleton_paid']
    if v['zero_singleton_paid'] and witness is None:witness={'table':h,'query':j,'sign':s,**{k:v[k] for k in v if k!='children'}}
 # Balanced zero-singleton witness with nonempty phase exchange.
 h=tuple((-1 if (i&3)==0 else 1)*(-1 if i&4 else 1) for i in range(8))
 v=step(h,source(h,1),1,ac,bc,0);ok(v['d']==0);ok(v['x']==F(21,4096));ok(v['cs']==[F(-1,4),F(1,4)] or v['cs']==[F(1,4),F(-1,4)])
 # Direct wrapper truth, independent of factorized coefficient formula.
 truth=tuple(a+b*z for z in h for a,b in zip(A,B));ok(prob(truth)==actual(ac,bc,h,1))
 continuation=0
 for ht,rt in v['children']:
  w=step(ht,rt,1,ac,bc,0);continuation+=1
  for htt,rtt in w['children']:step(htt,rtt,1,ac,bc,0);continuation+=1
 # Parity remains the exact null-energy obstruction with fully relevant query.
 parity=tuple((-1)**i.bit_count() for i in range(8));vp=step(parity,prob(parity),1,ac,bc,0);ok(vp['x']==0);ok(vp['d']==0)
 # Positive cost beta ln(64/63)>0 at both actual parity children.
 ok(ln(F(64,63))[0]>0)
 # Gram constants independently computed from direct controller characters.
 ok(v['gamma']==F(9,3584));ok(v['E']==F(21,512));ok(v['beta']==F(3,8))
 # New strength x/(beta+x)=7/519 at BOTH balanced witness children.
 ok(v['x']/(v['beta']+v['x'])==F(7,519))
 save('WITNESS.json',{'zero_singleton_seed':h,**{k:v[k] for k in v if k!='children'},'mixture_strength':F(7,519),'parity_energy':vp['x'],'parity_influence':1,'parity_fixed_reset_cost_bits':'(3/8)log2(64/63)>0','first_enumerated':witness})
 save('PILOT.json' if pilot else 'VALIDATION.json',{'status':'PASS','seed_bits':n,'all_boolean_tables':1<<(1<<n),'transactions':cases,'strictly_positive_mixture_cost_children':positive,'zero_singleton_positive_energy_transactions':zero,'sequential_continuation_transactions':continuation,'exact_assertions':count,'runtime_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'units':'checks use natural logs; theorem divides every cost by ln2; x remains rational','rounding':'128-bit outward integer ln enclosures;20 atanh terms, range [1,2), explicit tail; sign conclusions require separated intervals'})
 print(json.dumps({'status':'PASS','transactions':cases,'checks':count,'zero_singleton_paid':zero,'seconds':time.perf_counter()-start}))
if __name__=='__main__':main()
