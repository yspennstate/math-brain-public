from fractions import Fraction as F
from functools import lru_cache
import json,time
from pathlib import Path
start=time.monotonic(); checks=0
@lru_cache(None)
def ln(q):
 q=F(q); k=0
 while q>2: q/=2; k+=1
 while q<1: q*=2; k-=1
 z=(q-1)/(q+1); s=F(0)
 for j in range(48): s+=2*z**(2*j+1)/(2*j+1)
 tail=2*z**97/(97*(1-z*z))
 if k:
  a,b=ln(F(2)); return s+k*(a if k>=0 else b),s+tail+k*(b if k>=0 else a)
 return s,s+tail
@lru_cache(None)
def lg(q):
 a,b=ln(F(q)); c,d=ln(F(2)); return (a/d,b/c) if a>=0 else (a/c,b/d)
def expression(terms):
 a=b=F(0)
 for c,q in terms:
  if not c: continue
  l,h=lg(q); a+=c*(l if c>=0 else h); b+=c*(h if c>=0 else l)
 return a,b
def ck(x):
 global checks
 checks+=1
 assert x

def stat(t):
 n=(len(t)-1).bit_length(); w=list(t); step=1
 while step<len(w):
  for i in range(0,len(w),2*step):
   for j in range(i,i+step): a,b=w[j],w[j+step]; w[j]=a+b;w[j+step]=a-b
  step*=2
 p=[F(a*a,len(t)**2) for a in w]; ds=[F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
 pi=[sum(p[j] for j in range(len(p)) if j&s==s) for s in range(len(p))]
 U=expression([(a,pi[s]/a) for s,a in enumerate(p) if a]); H=expression([(a,1/a) for a in p if a]); return p,ds,U,H
rows=[]
for m in range(1,9):
 t=[-1]+[1]*((1<<m)-1); p,ds,U,H=stat(t); d=F(1,1<<(m-1)); ck(p[0]==(1-d)**2); ck(all(a==d*d for a in p[1:]));ck(ds==[d]*m)
 terms=[(m*d-m*d*d,F(2))]
 if d<1: terms.append((-2*(1-d)**2,1-d))
 lo,hi=expression(terms); ck(max(lo,U[0])<=min(hi,U[1])); ck(U[1]<=F(19,8)*m*d)
 for i in range(m):
  children=[[t[x] for x in range(len(t)) if (x>>i)&1==b] for b in (0,1)]
  us=[stat(c)[2] for c in children]; drift=U[1]-(us[0][0]+us[1][0])/2
  ck(drift<=F(19,8)*d)
  ids=[sum(stat(c)[1]) for c in children]; ck(sum(ds)==d+sum(ids)/2)
 ck(H[1]<=2*d*(2*m+1))
 if m>=3:
  h=expression([(-d,d),(-(1-d),1-d)]); ck(h[0]>=d*(m-1)); ck(m*h[0]/d>=m*(m-1))
 rows.append({'m':m,'I':str(m*d),'U_interval':[str(U[0]),str(U[1])],'strong_full_terminal_capital_over_I_lower':str(F(m*(m-1),m+1)) if m>=3 else None})
p,ds,U,H=stat([1,1,1,-1]);ck(p==[F(1,4)]*4);ck(ds==[F(1,2)]*2);ck(U[0]<=1<=U[1]);ck(H[0]<=2<=H[1])
out={'status':'PASS','primary_assertions':checks,'point_dimensions':list(range(1,9)),'all_coordinates_tested':36,'arithmetic':'integer FWHT/physical edges; Fraction; 48-term atanh intervals with explicit 97th-power tail','seconds':time.monotonic()-start,'rows':rows}
assert out['seconds']<55
Path(__file__).resolve().parents[1].joinpath('out/EXACT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
