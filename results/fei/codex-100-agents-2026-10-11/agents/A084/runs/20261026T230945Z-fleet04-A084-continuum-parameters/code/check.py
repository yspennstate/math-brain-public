from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, math, time, sys
R=Path(__file__).resolve().parents[1]
CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
def add(*es):
 out={}
 for e in es:
  for k,v in e.items():out[k]=out.get(k,Q(0))+v
 return {k:v for k,v in out.items() if v}
def sc(e,a):return {k:v*a for k,v in e.items() if v*a}
@lru_cache(None)
def factors(n):
 s=math.isqrt(n)
 if n>1 and s*s==n:return {p:2*v for p,v in factors(s).items()}
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def loge(q):return add(factors(q.numerator),sc(factors(q.denominator),-1))
def eta(q):return sc(loge(q),-q) if q else {}
def row(x,y):return add(eta(x*x),eta(y*y),sc(eta((x+y)**2),Q(-1,2)),sc(eta((x-y)**2),Q(-1,2)))
def lnseries(x,terms):
 z=(x-1)/(x+1);z2=z*z;t=z;s=Q(0)
 for j in range(terms):s+=2*t/(2*j+1);t*=z2
 return s,s+2*t/((2*terms+1)*(1-z2))
@lru_cache(None)
def logiv(q,terms=48):
 q=Q(q); k=q.numerator.bit_length()-q.denominator.bit_length();x=q/(Q(2)**k)
 if x<1:k-=1;x*=2
 ck(1<=x<2)
 a,b=lnseries(x,terms);c,d=lnseries(Q(2),terms)
 return Q(k)+a/d,Q(k)+b/c
def ev(e,terms=48):
 lo=hi=Q(0)
 for p,v in e.items():
  a,b=logiv(p,terms);u,w=sorted((v*a,v*b));lo+=u;hi+=w
 return lo,hi
def ell(b):return row(1-b,b)
def ellprime(b):
 return add(sc(loge(1-b),4*(1-b)),sc(loge(b),-4*b),sc(loge(1-2*b),-4*(1-2*b)))
def N(b):return add(sc(ellprime(b),b),sc(ell(b),-1))
def scalar(steps):
 a,b=Q(1,3),Q(7,16)
 ck(ev(N(a))[0]>0 and ev(N(b))[1]<0)
 for _ in range(steps):
  m=(a+b)/2;lo,hi=ev(N(m));ck(lo>0 or hi<0)
  if lo>0:a=m
  else:b=m
 lo=ev(ell(a))[0]/b;hi=ev(ell(b))[1]/a
 ck(lo>2 and hi<Q(9,4))
 return {'root':[str(a),str(b)],'price':[str(lo),str(hi)],'display_only':[float(lo),float(hi)],'rational_upper':'9/4','steps':steps}
def walsh(f):return [Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)),len(f)) for s in range(len(f))]
def H(f):return add(*(eta(x*x) for x in walsh(f)))
def inf(f,i):return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def restrict(f,i,b):return [f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2)]
def gate(h,a,b):return h[(a<0)+2*(b<0)]
def pivotal(h,other,j):
 return Q(sum((gate(h,1,v)!=gate(h,-1,v)) if j==0 else (gate(h,v,1)!=gate(h,v,-1)) for v in other),len(other))
def compose(h,g,k):return [gate(h,a,b) for b in k for a in g]
def correction(h,g,k):
 f=compose(h,g,k);return add(H(f),sc(H(g),-pivotal(h,k,0)),sc(H(k),-pivotal(h,g,1)))
def census(limit):
 seen=rows=0
 for hm in range(16):
  h=[1 if hm>>i&1 else -1 for i in range(4)]
  for gm in range(16):
   g=[1 if gm>>i&1 else -1 for i in range(4)]
   for km in range(4):
    k=[1 if km>>i&1 else -1 for i in range(2)]
    if seen>=limit:return {'circuits':seen,'rows':rows}
    f=compose(h,g,k);c=correction(h,g,k)
    ck(sum(x*x for x in walsh(f))==1)
    for j,core,other,offset in [(0,g,k,0),(1,k,g,2)]:
     q=pivotal(h,other,j)
     A=[Q((gate(h,1,v)+gate(h,-1,v)) if j==0 else (gate(h,v,1)+gate(h,v,-1)),2) for v in other]
     D=[Q((gate(h,1,v)-gate(h,-1,v)) if j==0 else (gate(h,v,1)-gate(h,v,-1)),2) for v in other]
     aw,dw=walsh(A),walsh(D);ck(sum(x*x for x in dw)==q)
     for i in range(len(core).bit_length()-1):
      child=[restrict(core,i,b) for b in (0,1)]
      cc=[correction(h,z,other) if j==0 else correction(h,other,z) for z in child]
      drift=add(sc(cc[0],Q(1,2)),sc(cc[1],Q(1,2)),sc(c,-1))
      w=walsh(core);mu,t=w[0],w[1<<i];d=inf(core,i)
      rhs=add(sc(row(mu,t),q),sc(add(*(row(a+mu*v,t*v) for a,v in zip(aw,dw))),-1))
      ck(drift==rhs)
      ck(inf(f,offset+i)==q*d)
      ck(abs(mu)+abs(t)<=1 and abs(t)<=d)
      ck(ev(add(sc({2:Q(9,4)*q*d},1),sc(drift,-1)))[0]>=0)
      ck(ev(add({2:Q(9,4)*d},sc(row(mu,t),-1)))[0]>=0)
      rows+=1
    seen+=1
 return {'circuits':seen,'rows':rows}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv
 root=scalar(8 if pilot else 32)
 (R/'out'/('PILOT_ROOT.json' if pilot else 'ROOT.json')).write_text(json.dumps(root,indent=2),encoding='utf-8')
 physical=census(32 if pilot else 1024)
 result={'status':'PASS','scalar':root,'physical':physical,'assertions':CHECKS,'runtime_seconds':time.perf_counter()-start,'arithmetic':'exact prime-log identities and rational directed 48-term atanh intervals'}
 (R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='scalar'}));print(json.dumps({k:v for k,v in root.items() if k!='price'}))
if __name__=='__main__':main()
