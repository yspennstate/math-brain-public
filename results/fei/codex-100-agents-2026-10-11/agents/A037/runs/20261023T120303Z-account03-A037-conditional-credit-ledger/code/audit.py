"""Standalone literal-Walsh / exact prime-log audit; no main imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(x,msg=''):
 global C
 C+=1;assert x,(C,msg);assert time.perf_counter()-start<55
@lru_cache(None)
def law(t):
 return tuple(F(sum(v*(-1)**((s&z).bit_count()%2) for z,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
def restrict(t,j,y):return tuple(v for z,v in enumerate(t) if (z>>j)&1==y)
@lru_cache(None)
def factorize(k):
 out={};d=2
 while d*d<=k:
  while k%d==0:out[d]=out.get(d,0)+1;k//=d
  d+=1
 if k>1:out[k]=out.get(k,0)+1
 return out
def plus(a,b,c=F(1)):
 out=a.copy()
 for p,v in b.items():out[p]=out.get(p,F(0))+c*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def logs(x):return plus({p:F(v) for p,v in factorize(x.numerator).items()},{p:F(v) for p,v in factorize(x.denominator).items()},-1)
def kl(p,q):
 out={}
 for x,y in zip(p,q):
  if x:out=plus(out,logs(x/y),x)
 return out
def positive(a):
 den=1
 for v in a.values():den=lcm(den,v.denominator)
 num=1;div=1
 for p,v in a.items():
  e=int(v*den)
  if e>0:num*=p**e
  else:div*=p**(-e)
 return num>div
def tensor(a,b):return tuple(x*y for y in b for x in a)
def core(k,r):
 t=(1,-1)
 for i in range(k):t=tensor(t,tuple(-1 if w==0 or (j and w==3) else 1 for w in range(1<<r) for j in [0,1]))
 return t
def lifted(pg,alpha=F(1,6)):
 p=[F(1,4)]*2+[F(0)]*(2*len(pg)-2);q=p[:]
 for s in range(1,len(pg)):
  p[2*s]=p[2*s+1]=pg[s]/4;q[2*s]=q[2*s+1]=((1-alpha)*pg[s]+(alpha if s==len(pg)-1 else 0))/4
 ck(sum(p)==sum(q)==1);return p,q
def f(m):return kl([m,1-m],[F(1,6)+F(5,6)*m,F(5,6)*(1-m)])
kap={p:v/2 for p,v in logs(F(400,399)).items()};rows=[]
for k,r in [(1,3),(1,4),(2,3)]:
 g=core(k,r);pg=law(g);d=F(1,2**r);ck(pg[0]==0 and pg[-1]==d**(2*k));gg=tuple(1 if z%2==0 else g[z//2] for z in range(2*len(g)));P,Q=lifted(pg);ck(tuple(P)==law(gg));coords=list(range(len(g).bit_length()-1));active=[(F(1),g,coords,[])];case=[];total={}
 for gen in range(k):
  nxt=[];reach=F(0)
  for weight,t,coords,hist in active:
   reach+=weight;j=coords.index(1+gen*(r+1));pp=law(t);m=pp[-1];P,Q=lifted(pp);bit=j+1;pb=[P[z]+P[z|(1<<bit)] for z in range(len(P)) if not (z>>bit)&1];qb=[Q[z]+Q[z|(1<<bit)] for z in range(len(Q)) if not (z>>bit)&1];kids=[restrict(t,j,y) for y in [0,1]];childs=[lifted(law(c)) for c in kids];joints=[[qb[z]*childs[y][0][z]/(2*pb[z]) if pb[z] else qb[z]/2 for z in range(len(pb))] for y in [0,1]];out=[sum(v) for v in joints];ck(out==[F(19,40),F(21,40)]);sigma={}
   for y in [0,1]:
    pc,qc=childs[y];old=[v/out[y] for v in joints[y]];ck(sum(old)==1);sigma=plus(sigma,plus(kl(pc,qc),kl(pc,old),-1),F(1,2));ck(law(kids[y])[-1]==[4*m,16*m][y]);nxt.append((weight/2,kids[y],[v for v in coords if v!=1+gen*(r+1)],hist+[y]))
   convex=plus(plus(f(4*m),f(16*m)),f(10*m),-2);expected=plus(kap,convex,F(1,4));ck(sigma==expected,'exact normalized identity');ck(positive(convex),'strict Jensen gap');ck(positive(plus(sigma,kap,-1)));total=plus(total,sigma,weight);case.append({'history':hist,'full_mass':str(m),'outcomes':list(map(str,out)),'prime_log_sigma':{str(p):str(v) for p,v in sigma.items()}})
  ck(reach==1,'complete generation, no artificial2^-generation factor');active=nxt
 ck(positive(plus(total,kap,-k)));rows.append({'k':k,'r':r,'transactions':case,'final_physical_probability':str(sum(w for w,_,_,_ in active))})
ck(400**300>2*399**300);k=4096;s=12;r=32;ck(k==2**s and r==2*s+8);ck(F(49,16)-F(k,1200)==-F(421,1200));ck(F(k*(3*r+1),2**r)<F(1,16));ck(F(16*k*(r+1),2**r)<F(1,1024))
o={'status':'PASS','cases':len(rows),'assertions':C,'seconds':time.perf_counter()-start,'rows':rows,'standalone_large_certificate':{'k':k,'r':r,'wrapper_bits':1+k*(r+1)+3,'same_owner_residual_upper':'-421/1200','old_quarter_still_owed':True}};(R/'out/AUDIT.json').write_text(json.dumps(o,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in o.items() if k!='rows'}))
