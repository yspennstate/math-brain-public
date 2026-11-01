"""Frozen exhaustive isospectral-edge census; rational integer-product signs."""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
import json,time,hashlib
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); count=0
def ck(x):
 global count
 count+=1
 assert x,count
 assert time.perf_counter()-start<55
def law(t):
 return tuple(F(sum(v*(-1)**((s&z).bit_count()%2) for z,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
def child(t,j,y):return tuple(v for z,v in enumerate(t) if (z>>j)&1==y)
def ref(p,a,S):
 q=[(1-a)*x for x in p];q[0]+=a*p[0];q[S]+=a*(1-p[0]);return q
def sign(p,old,new):
 # D(p||new)-D(p||old)=sum p log(old/new). No approximate logarithms.
 den=lcm(*(x.denominator for x in p));num=div=1
 for x,a,b in zip(p,old,new):
  if x:
   rat=a/b;e=int(x*den);num*=rat.numerator**e;div*=rat.denominator**e
 return (num>div)-(num<div)
rows=[];edges=0;neg=zero=collision=0
for n in range(1,4):
 for table in range(1<<(1<<n)):
  t=tuple(1-2*((table>>z)&1) for z in range(1<<n));p=law(t)
  for j in range(n):
   s=law(child(t,j,0))
   if s!=law(child(t,j,1)):continue
   edges+=1;u=s[0];v=p[0];ck(v in (F(0),u))
   for S in range(1,1<<n):
    if not p[S]:continue
    T=(S&((1<<j)-1))|((S>>(j+1))<<j)
    for a in (F(1,8),F(1,6),F(1,2)):
     q=ref(p,a,S);old=[q[z]+q[z|(1<<j)] for z in range(1<<n) if not ((z>>j)&1)]
     expected=[(1-a)*x for x in s];expected[0]+=a*v;expected[T]+=a*(1-v)
     ck(old==expected);new=ref(s,a,T) if T else list(s)
     ck(sum(new)==sum(old)==1);ck(all(y>0 for x,y in zip(s,old) if x))
     actual=sign(s,old,new);predicted=(-1 if (u>v if T else u<1) else 0)
     ck(actual==predicted);ck(actual<=0)
     neg+=actual<0;zero+=actual==0;collision+=not T
     rows.append({'n':n,'table':table,'j':j,'S':S,'T':T,'alpha':str(a),'parent_empty':str(v),'child_empty':str(u),'sign':actual})
out={'status':'PASS','arithmetic':'Fraction and exact integer powers; no floating signs','functions':276,'isospectral_edges':edges,'transactions':len(rows),'strictly_negative':neg,'zero':zero,'retired_witness_transactions':collision,'assertions':count,'seconds':time.perf_counter()-start,'rows':rows}
(R/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
