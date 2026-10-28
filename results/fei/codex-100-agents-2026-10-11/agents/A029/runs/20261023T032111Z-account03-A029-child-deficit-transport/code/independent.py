"""Direct-character reconstruction, independent KL algebra and rational proof constants."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def add(*ds):
 out={}
 for d in ds:
  for p,v in d.items():out[p]=out.get(p,Q(0))+v
 return {p:v for p,v in out.items() if v}
def scale(d,q):return {p:v*q for p,v in d.items() if v*q}
def sub(a,b):return add(a,scale(b,-1))
@lru_cache(None)
def lg(x):
 d={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:d[p]=d.get(p,Q(0))+s;n//=p
   p+=1
  if n>1:d[n]=d.get(n,Q(0))+s
 return {p:v for p,v in d.items() if v}
def KL(p,r):
 ck(sum(p)==sum(r)==1);ck(all(not x or y>0 for x,y in zip(p,r)))
 return add(*(scale(lg(x/y),x) for x,y in zip(p,r) if x))
@lru_cache(None)
def hat(t):return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def P(t):return tuple(x*x for x in hat(t))
def child(t,i,b):return tuple(v for x,v in enumerate(t) if ((x>>i)&1)==b)
def inherit(t,r,i):
 aa=hat(t);rows=[[],[]]
 for j in range(len(t)):
  if (j>>i)&1:continue
  k=j|(1<<i);u,v=aa[j],aa[k];mass=r[j]+r[k]
  for b in (0,1):rows[b].append(mass*((u+(-1)**b*v)**2/(2*(u*u+v*v)) if u or v else Q(1,2)))
 rho=[sum(row) for row in rows];ck(sum(rho)==1 and min(rho)>0)
 return [tuple(x/rho[b] for x in rows[b]) for b in (0,1)],rho
def ln_bounds(x):
 z=(x-1)/(x+1);term=z;s=Q(0)
 for k in range(32):s+=2*term/(2*k+1);term*=z*z
 return s,s+2*term/(65*(1-z*z))
LN2=ln_bounds(Q(2))
@lru_cache(None)
def log_bound(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;lo,hi=ln_bounds(Q(p,1<<k));return k+lo/LN2[1],k+hi/LN2[0]
def interval(d):
 lo=hi=Q(0)
 for p,v in d.items():
  a,b=log_bound(p);lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
 return lo,hi
def nn(d):ck(interval(d)[0]>=0)
def enc(d):return {str(p):str(v) for p,v in d.items()}

# Key all-real-parameter proof reduces to these exact rational facts.
p0=Q(20,23);b0=Q(80,101)
ck(Q(23,32)*(p0-b0)**2/(2*b0*(1-b0))==Q(135,10304))
ck(Q(135,10304)/Q(3,4)==Q(45,2576)>Q(1,64))
ck(Q(768,1805)+Q(128,245)==Q(16768,17689))
bound=Q(45,64)*Q(1,8)**2/2*Q(3,2)*Q(16768,17689)
ck(bound==Q(17685,128*17689)<Q(1,128))
rows=[]
for m in (0,1,2,3):
 a=tuple(-1 if x in (0,1,2) else 1 for x in range(8));pa=P(a);V=1-pa[0]
 gs=[]
 for is_h in (False,True):
  vals=[]
  for x in range(1<<(m+3)):
   core=(-1 if ((x%8).bit_count()>=2 if is_h else x%8==0) else 1)
   vals.append(core*(-1 if (x>>3).bit_count()%2 else 1))
  gs.append(tuple(vals))
 refs=[tuple(Q(1,len(t)) for _ in t) for t in gs]
 inherited=[inherit(t,r,0) for t,r in zip(gs,refs)]
 g,h=[child(t,0,1) for t in gs];rg,rh=[r[0][1] for r in inherited]
 weights=(Q(5,8),Q(3,8));pg,ph=P(g),P(h)
 q=tuple(weights[0]*x+weights[1]*y for x,y in zip(pg,ph));r=tuple(weights[0]*x+weights[1]*y for x,y in zip(rg,rh))
 W=add(scale(KL(pg,rg),weights[0]),scale(KL(ph,rh),weights[1]));Z=sub(W,KL(q,r))
 M=1<<(m+2);beta=Q(40*M,55*M-36)
 ck(Z==scale(KL((p0,1-p0),(beta,1-beta)),Q(23,32)))
 ck(inherited[0][1][1]==Q(5*M-12,10*M));ck(inherited[1][1][1]==Q(1,2))
 AA=tuple(x/V for x in pa[1:]);BB=tuple(Q(7,8)*x+Q(1,56) for x in AA)
 gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g));ck(V*gamma==Q(45,64))
 C=scale(KL(AA,BB),V*gamma);nn(sub({2:Q(1,128)},C))
 f=tuple((g if y==1 else h)[x] for x in range(len(g)) for y in a);pf=P(f)
 old=[];new=[]
 for t,qt in enumerate(q):
  row=pf[t*8:(t+1)*8];ck(sum(row)==qt)
  if qt:
   old.extend(r[t]*x/qt for x in row)
   new.append(r[t]*row[0]/qt);new.extend(r[t]*sum(row[1:])/qt*x for x in BB)
  else:old.extend([r[t]]+[Q(0)]*7);new.extend([r[t]]+[Q(0)]*7)
 ck(sub(KL(pf,tuple(new)),KL(pf,tuple(old)))==C)
 posterior={}
 for t,qt in enumerate(q):
  if qt:posterior=add(posterior,scale(KL((weights[0]*pg[t]/qt,weights[1]*ph[t]/qt),(weights[0]*rg[t]/r[t],weights[1]*rh[t]/r[t])),qt))
 ck(posterior==Z)
 if m:
  nn(sub(Z,{2:Q(1,64)}));nn(sub(sub(Z,C),{2:Q(1,128)}));ck(Q(8,11)<beta<=Q(80,101)<p0)
  ck(all(len(set(child(t,0,b)))==2 for t in gs for b in (0,1)))
 else:ck(not Z);ck(interval(C)[0]>0)
 rows.append({'m':m,'Z':enc(Z),'C':enc(C),'remaining':enc(sub(Z,C))})
 if time.monotonic()-START>55:raise RuntimeError('frozen55s limit')
out={'status':'PASS','cases':4,'assertions':checks,'seconds':round(time.monotonic()-START,6),'rows':rows,'representation':'direct character sums, separate source branch normalization and posterior KL; no imports from main/helper','rational_cost_bound':str(bound),'rational_Z_lower':str(Q(45,2576))}
(RUN/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
