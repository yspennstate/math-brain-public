"""A005 exact audit v1: symbolic prime-log identities and rational log bounds."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1]
checks=0
def ck(ok):
 global checks
 assert ok
 checks+=1
def add(*es):
 out={}
 for e in es:
  for p,v in e.items():out[p]=out.get(p,F(0))+v
 return {p:v for p,v in out.items() if v}
def mul(e,v):return {p:q*v for p,q in e.items() if q*v}
def scalar(v):return {2:F(v)} if v else {}
@lru_cache(None)
def factors(a):
 out={};p=2
 while p*p<=a:
  while a%p==0:out[p]=out.get(p,0)+1;a//=p
  p+=1
 if a>1:out[a]=out.get(a,0)+1
 return out
def elog(a):return add(mul(factors(a.numerator),1),mul(factors(a.denominator),-1))
def ent(ps):return add(*(mul(elog(p),-p) for p in ps if p))
def lnrat(x):
 z=(x-1)/(x+1); s=F(0)
 for j in range(40):s+=2*z**(2*j+1)/(2*j+1)
 return s,s+2*z**81/(81*(1-z*z))
L2=lnrat(F(2))
@lru_cache(None)
def lp(p):
 k=p.bit_length()-1; a,b=lnrat(F(p,1<<k))
 return F(k)+a/L2[1],F(k)+b/L2[0]
def interval(e):
 a=b=F(0)
 for p,v in e.items():
  l,h=lp(p);a+=v*(l if v>0 else h);b+=v*(h if v>0 else l)
 return a,b
def nonneg(e):return not e or interval(e)[0]>=0
def rank(vs):
 span={0}
 for v in vs:span|={s^v for s in tuple(span)}
 return len(span).bit_length()-1
@lru_cache(None)
def profile(f):
 N=len(f);n=N.bit_length()-1
 # Direct character sums, independent of source's butterfly transform.
 w=[sum(f[x]*(1-2*((s&x).bit_count()%2)) for x in range(N)) for s in range(N)]
 ps=[F(v*v,N*N) for v in w];ck(sum(ps)==1)
 ds=[F(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N)]
 I=sum(ds[1<<i] for i in range(n));ck(I==sum(s.bit_count()*p for s,p in enumerate(ps)))
 basis=[];a=F(0)
 for v in sorted(range(1,N),key=lambda v:(min(ds[v],1-ds[v]),v)):
  if rank(basis+[v])>len(basis):basis.append(v);a+=min(ds[v],1-ds[v])
 ck(len(basis)==n)
 return ent(ps),I,a,ps,ds,w
def child(f,i,b):
 return tuple(f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2))
def reserve_run(pilot=False):
 start=time.monotonic();cases=0;positive=zero=negative=0
 roots=[]
 for n in range(1,4):
  masks=range(min(2**(2**n),8)) if pilot else range(2**(2**n))
  roots.extend(tuple(1-2*((m>>x)&1) for x in range(1<<n)) for m in masks)
 if not pilot:
  for n in (4,5):
   roots.extend(tuple(-1 if x==p else 1 for x in range(1<<n)) for p in range(1<<n))
   roots.append(tuple(1-2*(x.bit_count()%2) for x in range(1<<n)))
   roots.append(tuple(1-2*(((x&3)==3)^((x&12)==12)) for x in range(1<<n)))
 for f in roots:
  ck(time.monotonic()-start<55)
  h,I,a,ps,ds,w=profile(f);n=len(f).bit_length()-1
  B=[];J=[];Ts=[];children=[]
  for i in range(n):
   projected=[ps[(x&((1<<i)-1))|((x>>i)<<(i+1))]+ps[(x&((1<<i)-1))|((x>>i)<<(i+1))|(1<<i)] for x in range(1<<(n-1))]
   bi=add(h,mul(ent(projected),-1));B.append(bi)
   c=[profile(child(f,i,b)) for b in (0,1)];children.append(c)
   hc=mul(add(c[0][0],c[1][0]),F(1,2));ji=add(h,mul(hc,-1),mul(bi,-1));J.append(ji)
   ck((c[0][1]+c[1][1])/2==I-ds[1<<i]);ck(nonneg(bi));ck(nonneg(ji))
   ck(interval(ji)[1]<=2*ds[1<<i]/L2[1])
   Ts.append((c[0][1]+c[1][1]-c[0][2]-c[1][2])/2)
  T=add(h,mul(add(*B),-1));ck(nonneg(T))
  for K in map(F,(0,2,F(8,3),4,10)):
   D=add(h,scalar(-K*I));ss=[];Ns={}
   for c in children:
    s=add(scalar(K*(c[0][2]+c[1][2])/2),mul(add(c[0][0],c[1][0]),-F(1,2)));ss.append(s)
    if not s:zero+=1
    elif interval(s)[0]>0:positive+=1
    else:
     ck(interval(s)[1]<0);negative+=1;Ns=add(Ns,mul(s,-1))
   residual=add(T,mul(D,n-1),add(*ss),scalar(K*sum(Ts)),mul(add(*J),-1))
   ck(not residual);ck(nonneg(add(Ns,add(*ss))))
   # The log-bound substitution is checked independently of the identity.
   ck(interval(add(*J))[1]<=2*I/L2[1]);cases+=1
 result=dict(status='PASS',cases=cases,roots=len(roots),checks=checks,positive=positive,zero=zero,negative=negative,seconds=time.monotonic()-start,arithmetic='exact prime-log identities and Fraction 40-term log enclosures',scope='finite checks; general identity and limit have analytic proof')
 (R/'out'/('PILOT.json' if pilot else 'RESERVES.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
def phase_run():
 start=time.monotonic();cases=0;f=tuple(-1 if x==0 else 1 for x in range(32));hf,_,af,_,_,_=profile(f)
 for mask in range(256):
  ck(time.monotonic()-start<55)
  vals=[(mask>>x)&1 for x in range(8)];anf=vals[:]
  for i in range(3):
   for x in range(8):
    if x>>i&1:anf[x]^=anf[x^(1<<i)]
  degree=max([s.bit_count() for s in range(8) if anf[s]]+[0]);p=tuple(1-2*vals[x&7] for x in range(32));_,_,_,_,dp,wp=profile(p)
  support=[s for s,w in enumerate(wp) if w];r=rank([s^support[0] for s in support]);z=[v for v in range(32) if dp[v] in (0,1)];ck(rank(z)==5-r)
  g=tuple(a*b for a,b in zip(f,p));hg,_,ag,_,_,_=profile(g)
  for d,K in [(3,F(10))]+([(2,F(4))] if degree<=2 else []):
   gamma=F(1,2**(d-1))-F(1,8);m=K*gamma-1;ck(gamma>=0 and m>0)
   ck(ag-af>=r*gamma);ck(nonneg(add(hf,mul(hg,-1),scalar(r))))
   ck(nonneg(add(hf,mul(hg,-1),scalar(K*(ag-af)-m*r))))
   if not r:ck(hf==hg and af==ag)
   cases+=1
 result=dict(status='PASS',cases=cases,checks=checks,seconds=time.monotonic()-start,scope='A052 analytic rigidity independently reconstructed; 384 finite phase comparisons')
 (R/'out'/'RIGIDITY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':
 if sys.argv[1]=='phase':phase_run()
 else:reserve_run(sys.argv[1]=='pilot')
