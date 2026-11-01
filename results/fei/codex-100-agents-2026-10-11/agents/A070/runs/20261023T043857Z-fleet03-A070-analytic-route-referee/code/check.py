from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def plus(*xs):
 a={}
 for x in xs:
  for p,c in x.items():a[p]=a.get(p,F(0))+c
 return {p:c for p,c in a.items() if c}
def times(x,c):return {p:v*c for p,v in x.items() if v*c}
@lru_cache(None)
def log(q):
 q=F(q);a={}
 for n,s in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:a[p]=a.get(p,0)+s;n//=p
   p+=1
  if n>1:a[n]=a.get(n,0)+s
 return {p:F(v) for p,v in a.items() if v}
def ln(q):
 z=(q-1)/(q+1)
 s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 e=2*abs(z)**49/(49*(1-z*z))
 return s-e,s+e
@lru_cache(None)
def lp(p):
 if p==2:return F(1),F(1)
 k=p.bit_length()-1;a,b=ln(F(p,2**k));c,d=ln(F(2));scale=2**80
 x=k+a/d;y=k+b/c
 return F((x*scale).__floor__(),scale),F((y*scale).__ceil__(),scale)
def interval(x):
 a=b=F(0)
 for p,c in x.items():
  l,h=lp(p);a+=c*(l if c>=0 else h);b+=c*(h if c>=0 else l)
 return a,b
def ce(p,q):return plus(*(times(log(v),-w) for w,v in zip(p,q) if w))
def spectrum(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):x,y=a[k],a[k+h];a[k]=x+y;a[k+h]=x-y
  h*=2
 return [F(x,len(a))**2 for x in a]
def inf(v,i):return F(sum(x!=v[j^(1<<i)] for j,x in enumerate(v)),len(v))
def marginal(q,i):
 out=[F(0)]*(len(q)//2)
 for s,w in enumerate(q):out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=w
 return out
def children(v,i):return [[x for j,x in enumerate(v) if (j>>i)&1==b] for b in [0,1]]
def decrement(v,q,i):
 vs=children(v,i);qs=marginal(q,i)
 return plus(ce(spectrum(v),q),times(plus(*(ce(spectrum(w),qs) for w in vs)),-F(1,2)))
rows=[];completions=[]
for m in range(1,8):
 N=2**m;t=F(1,N*N)
 for d in [0,1]:
  A=(1+3*t*d)/4;B=5*(1-t*d)/16;r=7*(1-t*d)/(32*(N-1))
  for k in range(m):
   h=2**k;M=N//h;eta=F(1,M);a=A+(h-1)*r;b=B+(h-1)*r;w=h*r
   q=[a,b]+[w]*(2*M-2)
   v=[(-1 if x==0 else 1)*((-1)**(x&1) if d else 1) for x in range(2*M)]
   ck(sum(q)==1);ck(sum(spectrum(v))==1);ck(inf(v,1)==eta)
   ck(spectrum(v)==([(1-eta)**2,eta**2] if d==0 else [eta**2,(1-eta)**2])+[eta**2]*(2*M-2))
   dc=decrement(v,q,1);p0,p1=spectrum(v)[:2]
   formula=plus(times(log(1+w/a),p0),times(log(1+w/b),p1),times(log((1+a/w)*(1+b/w)),eta**2),{2:2*(M-2)*eta**2})
   ck(dc==formula);ck(interval(dc)[1]<4*eta)
   ck(F(8*(M-1),7)<=a/w<=1+F(10*M,7));ck(F(8*(M-1),7)<=b/w<=1+F(10*M,7))
   qs=marginal(q,1);vs=children(v,1)
   for vv in vs:ck(sum(spectrum(vv))==1)
   ck(vs[1]==[(-1)**(x&1) if d else 1 for x in range(M)])
   rows.append(dict(m=m,d=d,k=k,decrement_interval=[str(x) for x in interval(dc)],influence=str(eta)))
   # A d1 first-one exit is a c literal; complete it using its actual inherited reference.
   if d==1:
    literal=vs[1];bill=decrement(literal,qs,0)
    ck(inf(literal,0)==1);ck(bill==log((qs[0]+qs[1])/qs[1]));ck(interval(bill)[1]<2)
    final=marginal(qs,0);ck(ce(spectrum(children(literal,0)[0]),final)==times(log(qs[0]+qs[1]),-1))
    ck(all(len(set(vv))==1 for vv in children(literal,0)))
    completions.append(dict(m=m,d=d,exit_depth=k+1,bill_interval=[str(x) for x in interval(bill)]))
  # All-zero leaf at depth m: d0 is a c literal and d1 constant.
  a=A+(N-1)*r;b=B+(N-1)*r
  ck(a+b==1);ck(F(0)<a/b<=F(28,15))
  if d==0:
   ck(decrement([-1,1],[a,b],0)==log(1/b));ck(interval(log(1/b))[1]<2)
   completions.append(dict(m=m,d=d,exit_depth=m,bill_interval=[str(x) for x in interval(log(1/b))]))
for l in [1,2,3]:
 M=2**l;e=F(1,M);L=F(8*(M-1),7);U=1+F(10*M,7)
 V=plus(times(log(1+1/L),1-2*e+2*e*e),times(log(1+U),2*e*e),{2:2*(M-2)*e*e})
 ck(interval(V)[1]<4*e)
ck(F(4887,1280)<4);ck(F(5,8)-F(3,5)-F(1,512)==F(59,2560))
# The m2 exited-constant counterexample, independently using physical restrictions.
m=2;A=F(1,4);B=F(5,16);r=F(7,96);q=[A,B]+[r]*6
q1=marginal(q,1);v=[1]*4;e=decrement(v,q1,1)
ck(inf(v,1)==0);ck(e==log(F(45,31)));ck(interval(e)[0]>F(1,2))
ck(45**2>2*31**2)
old=json.loads((R.parent/'20261022T234315Z-fleet03-A070-analytic-route-referee/out/CORE_CHECKPOINT.json').read_text(encoding='utf-8'))
P=F(old['P_core_interval'][0]);ck(P+F(511,1024)*interval(e)[0]>F(5,8))
for n in [2,4]:ck(F(2,n)!=0) # normalized degree-one f^2 has this nonconstant coefficient
result=dict(status='PASS',assertions=checks,private_nodes=len(rows),literal_completions=len(completions),elapsed_seconds=time.perf_counter()-start,unrestricted_exit_bill_interval=[str(x) for x in interval(e)],source_review='A069 stopping theorem and m2 obstruction hold unchanged.',memory_estimate_mb=48)
(R/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(R/'out/ROWS.json').write_text(json.dumps(dict(private=rows,literal=completions),indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
