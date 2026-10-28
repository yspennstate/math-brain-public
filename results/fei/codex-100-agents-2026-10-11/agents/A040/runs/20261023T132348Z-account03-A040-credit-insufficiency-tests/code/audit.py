"""Independent direct-character and prime-log reconstruction; stdlib only."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;identities=0
def ck(b):
 global checks
 assert b
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime exceeded')
@lru_cache(None)
def amps(g):
 return tuple(F(sum(y*(-1 if (x&t).bit_count()%2 else 1) for x,y in enumerate(g)),len(g)) for t in range(len(g)))
def P(g):return tuple(x*x for x in amps(g))
def cut(g,i,b):return tuple(y for x,y in enumerate(g) if (x>>i)&1==b)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def lg(x):
 out={}
 for sign,n in ((1,x.numerator),(-1,x.denominator)):
  for p,k in factors(n).items():out[p]=out.get(p,F(0))+sign*k
 return {p:k for p,k in out.items() if k}
def combine(*terms):
 out={}
 for weight,v in terms:
  for p,k in v.items():out[p]=out.get(p,F(0))+weight*k
 return {p:k for p,k in out.items() if k}
def KL(p,q):
 ck(sum(p)==sum(q)==1)
 return combine(*[(x,lg(x/y)) for x,y in zip(p,q) if x])
def eq(a,b):
 global identities
 ck(a==b);identities+=1
def core(r):
 return tuple((1-2*((x>>1)&1))*(1-2*((x>>2)==0 or ((x&1) and (x>>2)==3))) for x in range(2**(r+2)))
def tensor(k,r):
 out=[]
 for x in range(2**(1+k*(r+1))):
  val=1-2*(x&1)
  for b in range(k):
   row=(x>>(1+b*(r+1)))&((1<<(r+1))-1);j=row&1;w=row>>1
   val*=1-2*(w==0 or (j and w==3))
  out.append(val)
 return tuple(out)
def gate(h,e):return tuple(e if not(x&1) else h[x>>1] for x in range(2*len(h)))
def lift(g,h,a):
 p=P(g);v=P(h);q=tuple((1-a)*x+a*(t==len(v)-1) for t,x in enumerate(v));ck(v[0]==0 and v[-1]>0)
 out=tuple(x if t<2 else x*q[t>>1]/v[t>>1] if v[t>>1] else F(0) for t,x in enumerate(p))
 ck(sum(out)==1 and all((x>0)==(y>0) for x,y in zip(p,out)))
 return out
def step(g,q,i):
 p=P(g);children=[cut(g,i,b) for b in (0,1)];cp=list(map(P,children));pp=[];qq=[]
 for t in range(len(cp[0])):
  lo=t%(1<<i)+(t>>i)*(1<<(i+1));hi=lo+(1<<i);pp.append(p[lo]+p[hi]);qq.append(q[lo]+q[hi])
 rows=[];zz=[]
 for b in (0,1):
  raw=[y*x/(2*z) if z else F(0) for z,y,x in zip(pp,qq,cp[b])];zz.append(sum(raw));rows.append(tuple(x/zz[-1] for x in raw))
 ck(sum(zz)==1 and all(z>0 for z in zz))
 return children,rows,zz,pp,qq
def fvec(m,a):return combine((1-m,lg(1/(1-a))),(m,lg(m/(a+(1-a)*m))))

rare=[]
for r in (3,4):
 for a in (F(1,6),F(1,r)):
  for e in (-1,1):
   h=core(r);g=gate(h,e);q=lift(g,h,a);gs,old,zz,pb,qb=step(g,q,1);d=F(1,2**r);m=d*d
   ck(zz==[F(1,2)-3*a/20,F(1,2)+3*a/20]);sig={}
   for b in (0,1):
    hc=cut(h,0,b);fresh=lift(gs[b],hc,a)
    sig=combine((1,sig),(F(1,2),KL(P(gs[b]),fresh)),(-F(1,2),KL(P(gs[b]),old[b])))
   kap=combine((F(1,2),lg(1/(1-F(9,100)*a*a))))
   eq(sig,combine((1,kap),(F(1,4),fvec(4*m,a)),(F(1,4),fvec(16*m,a)),(-F(1,2),fvec(10*m,a))))
   eq(KL(P(g),q),combine((F(1,2),fvec(m,a))))
   b=1-a;full=a+b*m
   eq(KL(q,P(g)),combine((full/2,lg(full/m)),(b*(1-m)/2,lg(b))))
   ck(sum((y-x)**2/x for x,y in zip(pb,qb) if x)==a*a*(1/(10*m)-1)/2)
   rare.append({'r':r,'alpha':str(a),'epsilon':e,'reference_outcomes':list(map(str,zz))})

tensor_records=[]
for k,r in ((1,3),(2,3)):
 h=tensor(k,r);ck(P(h)[-1]==F(1,2**(2*r*k)))
 for e in (-1,1):
  h=tensor(k,r) # Each sign starts from the ORIGINAL core, never a restricted loop variable.
  g=gate(h,e);q=lift(g,h,F(1,6));oldroot=lift(g,h,F(1,8));m0=P(h)[-1]
  # Both root signs have reach1/4; first-reset core identity uses complete G laws.
  first=combine((1,KL(P(g),q)),(-1,KL(P(g),oldroot)))
  eq(first,combine((F(1,2),fvec(m0,F(1,6))),(-F(1,2),fvec(m0,F(1,8)))))
  states=[(F(1,4),g,q,h)]
  for level in range(k):
   nxt=[]
   for reach,g,q,h in states:
    j=2+level*r;gs,old,zz,_,_=step(g,q,j);ck(zz==[F(19,40),F(21,40)]);sig={};m=P(h)[-1]
    for b in (0,1):
     hc=cut(h,j-1,b);fresh=lift(gs[b],hc,F(1,6));ck(P(hc)[-1]==m*(4 if b==0 else 16))
     sig=combine((1,sig),(F(1,2),KL(P(gs[b]),fresh)),(-F(1,2),KL(P(gs[b]),old[b])))
     nxt.append((reach/2,gs[b],fresh,hc))
    eq(sig,combine((F(1,2),lg(F(400,399))),(F(1,4),fvec(4*m,F(1,6))),(F(1,4),fvec(16*m,F(1,6))),(-F(1,2),fvec(10*m,F(1,6)))))
    tensor_records.append({'k':k,'r':r,'epsilon':e,'level':level,'reach':str(reach),'full_mass':str(m),'outcomes':list(map(str,zz))})
   ck(sum(x[0] for x in nxt)==F(1,4));states=nxt

# Exact endpoint and induction certificates for the analytic ALL-s owner exhaustion.
ck(400**300>2*399**300);ck(6**40<2**11*5**40)
ck(F(49,16)-F(4096,1200)==-F(421,1200))
ck(F(33,65536)<F(1,1024));ck(F(32,65536)==F(1,2048));ck(F(97,2**20)<F(1,16))
for s in (12,13,20,32):
 ck(6*s+31<2*(6*s+25));ck(2*s+11<2*(2*s+9));ck(2*s+10<2*(2*s+8))
# The scalar inequalities are affine in s with positive slack for all s>=12;
# the PROOF/REVIEW supplies that argument, rather than extrapolating these fixtures.
out={'status':'PASS','checks':checks,'exact_prime_log_equalities':identities,'runtime_seconds':time.perf_counter()-start,'rare_dense':rare,'tensor_query_nodes':tensor_records,'foreign_or_primary_helper_imports':False,'formal_verification':'not attempted'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:out[k] for k in ('status','checks','exact_prime_log_equalities','runtime_seconds')}))
