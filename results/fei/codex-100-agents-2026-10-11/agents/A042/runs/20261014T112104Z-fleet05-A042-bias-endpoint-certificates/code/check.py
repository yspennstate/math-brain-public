from fractions import Fraction as Q
from math import comb
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
@lru_cache(None)
def ln(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(x):
  z=(x-1)/(x+1);a=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
  return a,a+2*z**49/(49*(1-z*z))
 a,b=series(x);l,u=series(Q(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def h(x):
 if not x:return Q(0),Q(0)
 a,b=ln(1/(x*x));return x*x*a,x*x*b
def add(terms):return tuple(sum((a*b[i] for a,b in terms),Q(0)) for i in (0,1))
def outward(x):
 scale=10**12
 return [str(Q((x[0]*scale).__floor__(),scale)),str(Q((x[1]*scale).__ceil__(),scale))]
families=[]
for r in range(1,9):
 n=16*r*r;M=n//2
 def g(k):return 1 if k<=M-r or k>=M+r else -1
 weights=[Q(comb(n,k),2**n) for k in range(n+1)]
 mu=sum((weights[k]*g(k) for k in range(n+1)),Q(0))
 top=sum((weights[k]*g(k)*(-1)**k for k in range(n+1)),Q(0))
 b=Q(comb(n-1,M-r),2**(n-1));central=Q(comb(n-1,M-1),2**(n-1))
 a=2*(2*r-1)*b/(n-1)
 ck(central>=Q(1,12*r));ck(b>=Q(1,16*r));ck(Q(1,8*(n-1))<=a<=Q(2,n-1))
 rat=Q(1)
 for j in range(1,r):rat*=Q(M-j,M+j)
 ck(b==central*rat);ck(rat>=Q(3,4))
 w2=[Q(comb(n-2,k),2**(n-2)) for k in range(n-1)]
 zg=[Q(g(k+2)-2*g(k+1)+g(k),2) for k in range(n-1)]
 ck(all(z.denominator==1 for z in zg))
 ck(sum((w*z for w,z in zip(w2,zg)),Q(0))==2*a)
 zg2=sum((w*z*z for w,z in zip(w2,zg)),Q(0))
 Ig=n*sum((Q(comb(n-1,k),2**(n-1))*Q(g(k+1)-g(k),2)**2 for k in range(n)),Q(0))
 ck(Ig==2*n*b)
 # Independent physical selector disagreement count.
 disagreement=sum((weights[k] for k in range(n+1) if g(k)!=(-1)**k),Q(0));ck(disagreement==(1-top)/2)
 for eps in (Q(1,2),Q(1,8),Q(1,64)):
  ck(time.monotonic()-start<55)
  m=2*eps*a;V=4*(1-eps)+eps*zg2-m*m
  W=V/4;paircount=Q(n*(n-1),2)
  packets=((1-eps)+eps*top)**2+eps*(1-eps)*(top-1)**2
  ck(packets==(1-eps)+eps*top*top);ck(W>=packets>=1-eps)
  I=(1-eps)*n+eps*Ig+4*eps*(1-eps)*disagreement
  D=I-1+eps*eps*mu*mu
  ck((1-eps)*n-1<=D<=n+1)
  la,ua=ln(1/m);kap=(2*m*la/(1-m),2*m*ua/(1-m))
  bill=(paircount*W*kap[0],paircount*W*kap[1])
  exact=tuple(paircount*x/4 for x in h(m))
  larg,uarg=ln(Q(n-1)/(4*eps))
  ck(bill[0]>=n*eps*(1-eps)*larg/4)
  ck(bill[0]/D>=eps*(1-eps)*larg/6)
  ck(exact[1]/D<=10*eps*eps*larg/n)
  ck(max(bill[0]/exact[1],V/(m*(1-m)))<=min(bill[1]/exact[0],V/(m*(1-m))))
  if eps==Q(1,2):
   ck(bill[0]>=Q(n,16)*ln(Q(n-1,2))[0]);ck(bill[0]/D>=ln(Q(n-1,2))[0]/24)
  families.append({'r':r,'n':n,'epsilon':str(eps),'mu':str(mu),'top':str(top),'a':str(a),'delta':str(D),'bill_over_delta':outward((bill[0]/D,bill[1]/D)),'exact_residual_over_delta':outward((exact[0]/D,exact[1]/D)),'variance_price_over_exact':str(V/(m*(1-m)))})
  (root/'out/FAMILY.json').write_text(json.dumps(families,indent=2)+'\n',encoding='utf-8')

def truth(mask,n):return {x:Q(1 if mask>>sum(v<<i for i,v in enumerate(x))&1 else -1) for x in product((0,1),repeat=n)}
def direct(T,p):
 n=len(p);P={};W={}
 for s in range(1<<n):
  den=Q(1);w=Q(1);moment=Q(0)
  for i in range(n):
   if s>>i&1:den*=p[i]*(1-p[i]);w*=4*p[i]*(1-p[i])
  for x,f in T.items():
   a=f
   for i in range(n):
    a*=p[i] if x[i] else 1-p[i]
    if s>>i&1:a*=x[i]-p[i]
   moment+=a
  P[s]=moment*moment/den;W[s]=w
 ck(sum(P.values())==1)
 return P,W
unit_count=0
domains=[(n,mask,eps) for n in (1,2) for mask in range(2**(2**n)) for eps in (Q(1,8),Q(1,32))]+[(3,mask,Q(1,64)) for mask in (0,128,105,150)]
for n,mask,eps in domains:
 G=truth(mask,n);full=(1<<n)-1
 gh={s:sum((val*(-1)**sum(x[i] for i in range(n) if s>>i&1) for x,val in G.items()),Q(0))/2**n for s in range(1<<n)}
 mu=gh[0];t=gh[full];Ig=sum(s.bit_count()*a*a for s,a in gh.items())
 FT={x+(z,):(G[x] if z else Q((-1)**sum(x))) for x in G for z in (0,1)}
 P,W=direct(FT,[Q(1,2)]*n+[eps])
 # Centered 0/1 moments have reflected character signs; masses are invariant.
 for s in range(1<<n):
  target=((1-eps if s==full else 0)+eps*gh[s])**2
  ck(P[s]==target)
  ck(P[s|(1<<n)]==eps*(1-eps)*(gh[s]-(s==full))**2)
 D=sum((s.bit_count()-1)*v for s,v in P.items() if s)
 ck(D==n-1+eps*(Ig-n+2-2*t)-eps*eps*(2-2*t-mu*mu))
 Z=sum(a*a for s,a in gh.items() if s and s!=full);ck(Z==1-t*t-mu*mu)
 J=add([(4,h((a-(s==full))/2)) for s,a in gh.items()])
 exact=add([(1,h(1+eps*(t-1)))]+[(1,h(eps*a)) for s,a in gh.items() if s and s!=full]+[(eps*(1-eps),J)])
 actual=add([(p,ln(W[s]/p)) for s,p in P.items() if s and p])
 ck(max(exact[0],actual[0])<=min(exact[1],actual[1]))
 if n==1 and t==1:ck(D==0 and actual==(0,0))
 if abs(mu)==1:ck(Z==0)
 unit_count+=1
out={'helper_version':'A042-rare-profile-v1','assertions_passed':checks,'family_cases':len(families),'unit_atom_direct_cases':unit_count,'largest_compressed_n':1024,'runtime_seconds':time.monotonic()-start,'continuum_proof':'PROOF.md; growing diagonal is proved analytically, not computed'}
(root/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
