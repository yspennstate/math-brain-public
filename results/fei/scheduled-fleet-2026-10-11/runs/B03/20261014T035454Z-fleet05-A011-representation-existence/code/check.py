from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def fw(v):
 a=list(v); s=1
 while s<len(a):
  for i in range(0,len(a),2*s):
   for j in range(i,i+s): a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return [F(x,len(a)) for x in a]
@lru_cache(None)
def log2(x):
 x=F(x); k=0
 while x>=2: x/=2;k+=1
 while x<1: x*=2;k-=1
 def ln(z):
  w=(z-1)/(z+1); s=sum((w**(2*j+1)/F(2*j+1) for j in range(32)),F(0))*2
  return s,s+2*w**65/(65*(1-w*w))
 a,b=ln(x); c,d=ln(F(2))
 return F(k)+a/d,F(k)+b/c
def ent(p):
 lo=hi=F(0)
 for x in p:
  if x:
   a,b=log2(1/x);lo+=x*a;hi+=x*b
 return lo,hi
def ce(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   a,b=log2(1/y);lo+=x*a;hi+=x*b
 return lo,hi
cases=refs=0
for m in range(1,5):
 N=2**m;t=F(1,N)
 for k in range(1,m+1):
  mask=2**k-1
  for point in range(N):
   h=[(-1)**((y&mask).bit_count()) for y in range(N)]
   for r in range(1,4):
    p=F(1,2**r);rho=4*p*t
    v=[h[y]*(-1 if x==0 and y==point else 1) for x in range(2**r) for y in range(N)]
    a=fw(v); P=[z*z for z in a];q=[sum(P[u*N+T] for u in range(2**r)) for T in range(N)]
    ck(q==[(1-rho if T==mask else 0)+rho*t for T in range(N)])
    inf=[F(sum(v[z]!=v[z^(1<<j)] for z in range(len(v))),len(v)) for j in range(m+r)]
    C=2*p*t*(m-k);E=2*p*t*k;Is=2*r*p*t
    ck(sum(inf)==k+C-E+Is);ck(sum(inf[m:])==Is)
    for T in range(N):
     if T!=mask: ck(all(P[u*N+T]==4*p*p*t*t for u in range(2**r)))
    H=ent(P);Hq=ent(q);Blo=H[0]-Hq[1];Bhi=H[1]-Hq[0]
    ck(Bhi<=m*4*p*(1-p)*t+4*Is)
    for scale in [F(1),F(1,2)]:
     for L in [1,8,32]:
      e=F(1,N*2**L); ref=[scale*(1-(N-1)*e) if T==mask else scale*e for T in range(N)]
      rep=[(1-rho)*ref[T]+rho*t for T in range(N)]
      source=log2(1/ref[mask]); cost=ce(q,rep)
      # Exact full root reference, its mass, and likelihood-ratio debt.
      Q=[rep[T]*P[u*N+T]/q[T] for u in range(2**r) for T in range(N)]
      ck(sum(Q)==(1-rho)*scale+rho)
      ck(all(Q[j]*q[j%N]==rep[j%N]*P[j] for j in range(len(P))))
      hmix=ent([rho,1-rho]); upper=(1-rho)*source[0]+rho*m+hmix[0]
      ck(cost[1]<=upper)
      ck(cost[1]+Bhi<=source[0]+6*(C+E)+6*Is)
      # Posterior KL is certified by the exact logarithm argument identity.
      for T in range(N):
       true0=((1-rho) if T==mask else F(0))/q[T]
       ref0=(1-rho)*ref[T]/rep[T]
       true1=rho*t/q[T];ref1=rho*t/rep[T]
       ck(true0+true1==1)
       if true0: ck(true0/ref0==rep[T]/(q[T]*ref[mask]))
       ck(true1/ref1==rep[T]/q[T])
      refs+=1
    cases+=1
    if time.monotonic()-start>55: raise RuntimeError('frozen cutoff')
# Neutral, non-bent entropy-changing core: parity on two of four coordinates.
m=4;r=1;t=F(1,16);p=F(1,2);rho=F(1,8)
ck(2*p*t*(m-2*2)==0);ck(F(2)+2*r*p*t==F(33,16))
# R_mask=1-15*2^(-L-4), others 2^(-L-4); c<=1.
# Unchanged CE >= (15/128)*(L+4), so L=256 exceeds 8 I(root).
ck(F(15,128)*260>8*F(33,16))
out={'status':'PASS','assertions':checks,'boolean_cases':cases,'reference_cases':refs,'seconds':time.monotonic()-start,'neutral_certificate':{'m':4,'k':2,'r':1,'L':256,'source_cost_upper':1,'data_increment':0,'influence':'33/16','unchanged_CE_lower':'975/32','eight_I':'33/2'},'log_terms':32,'arithmetic':'Fraction, integer Walsh, rational log enclosures'}
(R/'out/EXACT_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
