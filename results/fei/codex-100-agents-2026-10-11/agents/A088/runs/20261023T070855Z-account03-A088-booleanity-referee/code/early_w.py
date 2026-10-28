from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];START=time.perf_counter();checks=0
def ck(v,s):
 global checks
 checks+=1
 if not v:raise AssertionError(s)
 if time.perf_counter()-START>55:raise TimeoutError(s)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def scale(a,k):return a[0]*k,a[1]*k
@lru_cache(None)
def ln(x):
 z=(x-1)/(x+1);assert 0<=z<=F(1,3)
 v=2*sum((z**(2*j+1)/(2*j+1) for j in range(30)),F())
 return v,v+2*z**61/(61*(1-z*z))
@lru_cache(None)
def log(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln(x);c,d=ln(F(2));den=1<<90;lo=k+a/d;hi=k+b/c
 return F(lo.numerator*den//lo.denominator,den),F(-((-hi.numerator*den)//hi.denominator),den)
def law(v):
 a=list(v);s=1
 while s<len(a):
  for start in range(0,len(a),2*s):
   for i in range(start,start+s):a[i],a[i+s]=a[i]+a[i+s],a[i]-a[i+s]
  s*=2
 return [F(x*x,len(a)**2) for x in a]
def ce(p,q):
 a=(F(),F())
 for x,y in zip(p,q):
  if x:a=add(a,scale(log(1/y),x))
 return a
def enc(a):return {'lo':str(a[0]),'hi':str(a[1]),'approx':float((a[0]+a[1])/2)}
rows=[]
for m in range(2,6):
 mask=1<<(2*m);d=F(1,mask)
 v=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))-2*(x==0) for x in range(2*mask)]
 p=law(v);a,b=v[:mask],v[mask:];pa,pb=law(a),law(b);q=[p[s]+p[s+mask] for s in range(mask)]
 ck(all(x in (-1,1) for x in v+a+b),'actual Boolean functions')
 ck(all((x+y)/2==z for x,y,z in zip(pa,pb,q)),'both actual child spectral bills')
 I=F(sum(v[x]!=v[x^mask] for x in range(2*mask)),2*mask);ck(I==d,'actual physical w influence')
 L=add(ce(p,p),neg(scale(add(ce(pa,q),ce(pb,q)),F(1,2))))
 e=add(L,(-3*d,-3*d));ck(e[0]>0,'early w violates nonpositive rate3 CE sign')
 ck(e[0]>d*(2*m-4),'analytic all-m lower bound')
 rows.append({'m':m,'influence':str(I),'complete_CE_drop':enc(L),'rate3_debit':enc(e)})
out={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-START,'cases':rows,'scope':'Positive early-w debit, not a failure of fixed original source funding or FEI'}
(R/'out'/'EARLY_W.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'PASS','checks':checks,'runtime_seconds':out['runtime_seconds'],'debits':[r['rate3_debit']['approx'] for r in rows]}))
