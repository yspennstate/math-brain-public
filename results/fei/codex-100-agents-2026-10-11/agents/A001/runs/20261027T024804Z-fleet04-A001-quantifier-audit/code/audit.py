"""Independent finite fixed-target physical-reference audit; stdlib only."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
import json, sys, time

RUN=Path(__file__).resolve().parents[1]
SPEC=json.loads((RUN/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
START=time.monotonic(); checks=0
def ck(test):
 global checks
 checks+=1
 assert test, checks
 if checks%100==0: assert time.monotonic()-START<SPEC['max_runtime_seconds']
def fw(v):
 a=list(v); h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
@lru_cache(None)
def amp_cache(v):return tuple(F(x,len(v)) for x in fw(v))
def amp(v):return list(amp_cache(tuple(v)))
@lru_cache(None)
def law_cache(v):return tuple(x*x for x in amp_cache(v))
def law(v):return list(law_cache(tuple(v)))
def ins(t,j,b):return (t&((1<<j)-1))|((t>>j)<<(j+1))|(b<<j)
def child(v,j,b):return [v[ins(t,j,b)] for t in range(len(v)//2)]
def plus(*xs):return (sum(x[0] for x in xs),sum(x[1] for x in xs))
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def minus(a,b):return plus(a,scale(-1,b))
def lnunit(q):
 z=(q-1)/(q+1);zz=z*z;u=z;lo=F(0)
 for j in range(32):lo+=2*u/(2*j+1);u*=zz
 return lo,lo+2*u/(65*(1-zz))
LN2=lnunit(F(2))
@lru_cache(None)
def log(q):
 assert q>0
 k=q.numerator.bit_length()-q.denominator.bit_length(); q=q/F(2)**k
 if q<1:q*=2;k-=1
 lo,hi=lnunit(q);grid=1<<110
 lo=lo/LN2[1]+k;hi=hi/LN2[0]+k
 return F((lo*grid).__floor__(),grid),F((hi*grid).__ceil__(),grid)
@lru_cache(None)
def ce_cache(p,q):return plus(*[scale(-x,log(y)) for x,y in zip(p,q) if x])
def ce(p,q):return ce_cache(tuple(p),tuple(q))
def ent(p):return ce(p,p)
def div(p,q):return minus(ce(p,q),ent(p))
def same(a,b):
 # Interval overlap is diagnostic only. The report proves the identity algebraically.
 ck(max(a[0],b[0])<=min(a[1],b[1]))
def inherit(v,q,j):
 p=law(v);s=sum(q); cs=[child(v,j,b) for b in (0,1)]; ps=[law(c) for c in cs]
 a=amp(v)
 for b,c in enumerate(cs):
  ck(amp(c)==[a[ins(t,j,0)]+(-1)**b*a[ins(t,j,1)] for t in range(len(c))])
 m=[p[ins(t,j,0)]+p[ins(t,j,1)] for t in range(len(v)//2)]
 r=[q[ins(t,j,0)]+q[ins(t,j,1)] for t in range(len(v)//2)]
 ck([sum(z)/2 for z in zip(*ps)]==m)
 raw=[[r[t]*pb[t]/m[t] if m[t] else r[t] for t in range(len(m))] for pb in ps]
 z=[sum(rb) for rb in raw];ck(z[0]+z[1]==2*s);ck(min(z)>0)
 inh=[[s*x/zb for x in rb] for rb,zb in zip(raw,z)]
 for b,(pb,qb) in enumerate(zip(ps,inh)):
  ck(sum(qb)==s);ck(all(qb[t]>0 for t,x in enumerate(pb) if x))
  for t in range(len(m)):
   if pb[t]:ck(qb[t]/pb[t]==s*r[t]/(z[b]*m[t]))
 d=minus(div(p,q),scale(F(1,2),plus(*[div(pb,qb) for pb,qb in zip(ps,inh)])))
 rhs=minus(minus(div(p,q),div(m,r)),scale(F(1,2),plus(*[log(zb/s) for zb in z])))
 same(d,rhs);ck(d[1]>=0)
 return cs,ps,inh,d
def reset_ref(p,theta,s):return [s*((1-theta)*x+theta/F(len(p))) for x in p]
def one(v,q,j,theta):
 p=law(v);cs,ps,inh,d=inherit(v,q,j)
 rs=[reset_ref(pb,theta,sum(q)) for pb in ps]
 e=scale(F(1,2),plus(*[minus(ce(pb,rb),ce(pb,qb)) for pb,rb,qb in zip(ps,rs,inh)]))
 terminal=scale(F(1,2),plus(*[div(pb,rb) for pb,rb in zip(ps,rs)]))
 same(plus(ce(p,q),e),plus(ent(p),d,terminal))
 return d
def tree(v,q,order,theta):
 p=law(v)
 if not order:return (F(0),F(0)),(F(0),F(0)),div(p,q)
 j=order[0];cs,ps,inh,d=inherit(v,q,j);s=sum(q)
 rs=[reset_ref(pb,theta,s) for pb in ps]
 e=scale(F(1,2),plus(*[minus(ce(pb,rb),ce(pb,qb)) for pb,rb,qb in zip(ps,rs,inh)]))
 rest=[k-(k>j) for k in order[1:]]
 sub=[tree(c,rb,rest,theta) for c,rb in zip(cs,rs)]
 es=plus(e,scale(F(1,2),plus(*[x[0] for x in sub])))
 ds=plus(d,scale(F(1,2),plus(*[x[1] for x in sub])))
 ts=scale(F(1,2),plus(*[x[2] for x in sub]))
 same(plus(ce(p,q),es),plus(ent(p),ds,ts))
 return es,ds,ts
def witness(b):
 e=F(1,2**(b+1));N=1/e
 # Two amplitude classes of the full padded dictator; multiplicities retained.
 mult=[F(1),N-1];q=[1-2*e+2*e*e,2*e*e]
 r=[(1+3*e*e)/(1+3*e),3*e*e/(1+3*e)]
 pc=[F(1),F(0)];pe=[(1-2*e)**2,4*e*e]
 z=[sum(m*rr*p/qq for m,rr,p,qq in zip(mult,r,pb,q)) for pb in [pc,pe]]
 Z=(1+3*e*e)/((1+3*e)*(1-2*e+2*e*e))
 ck(z[0]==Z);ck(sum(z)==2);ck(0<Z<1)
 deficit=1-Z
 ck(deficit==e*(1-e)*(1-6*e)/((1+3*e)*(1-2*e+2*e*e)))
 ck(0<deficit<e);ck(z[0]*z[1]==1-deficit**2)
 delta=scale(F(-1,2),log(z[0]*z[1]));ck(delta[0]>0);ck(delta[1]<e*e)
 ck(F(3,4)/(1-e*e)<1);ck(e*e<=F(1,2**26));ck(e*e<F(18111,4096))
 # Constant source boundary: its genuine edited data law has A=1 at empty mask.
 return dict(b=b,epsilon=str(e),Zclean=str(Z),deficit=str(deficit),delta=[str(x) for x in delta],upper=str(e*e))
def main():
 pilot='--pilot' in sys.argv;maxn=1 if pilot else 3;profiles=trees=functions=0
 for n in range(maxn+1):
  for bits in range(1<<(1<<n)):
   v=[1 if bits>>x&1 else -1 for x in range(1<<n)];p=law(v);functions+=1
   ck(sum(p)==1)
   for s in [F(1),F(1,2)]:
    for initial in [F(1,4),F(1)]:
     q=reset_ref(p,initial,s)
     for j in range(n):
      for reset in [F(1,4),F(1)]:one(v,q,j,reset);profiles+=1
     if n<=2:
      for order in permutations(range(n)):
       tree(v,q,list(order),F(1,4));trees+=1
 witnesses=[witness(b) for b in ([12] if pilot else [12,13,16,24,40])]
 result=dict(status='PASS',checks=checks,labelled_functions=functions,query_reset_profiles=profiles,full_trees=trees,witnesses=witnesses,seconds=time.monotonic()-START,arithmetic='integer Walsh, exact Fraction masses, outward rational atanh log intervals; identity overlap diagnostic, algebra in DERIVATION')
 (RUN/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='witnesses'}))
if __name__=='__main__':main()
