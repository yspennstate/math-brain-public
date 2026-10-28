from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys
run=Path(__file__).resolve().parents[1];(run/'out').mkdir(exist_ok=True)
start=time.monotonic();checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def le(a,b):
 global checks
 assert a<=b,(a,b);checks+=1
def add(*vecs):
 out={}
 for v in vecs:
  for k,x in v.items():out[k]=out.get(k,Q(0))+x
 return {k:x for k,x in out.items() if x}
def sc(v,c):return {k:x*c for k,x in v.items() if x*c}
@lru_cache(None)
def fac(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logq(q):
 return add({p:Q(k) for p,k in fac(q.numerator).items()},{p:Q(-k) for p,k in fac(q.denominator).items()})
def e(q):return {} if not q else sc(logq(q),-q)
def L(a,b):return add(e(a*a),e(b*b),sc(e(a*a+b*b),-1))
@lru_cache(None)
def ln_small(x,N):
 z=(x-1)/(x+1);v=Q(0)
 for j in range(N):v+=2*z**(2*j+1)/(2*j+1)
 tail=2*z**(2*N+1)/((2*N+1)*(1-z*z))
 return v,v+tail
@lru_cache(None)
def logint(p,N):
 k=p.bit_length()-1;x=Q(p,2**k)
 lo,hi=ln_small(x,N);l2,h2=ln_small(Q(2),N)
 return Q(k)+lo/h2,Q(k)+hi/l2
def bounds(v,N=24):
 lo=hi=Q(0)
 for p,c in v.items():
  l,h=logint(p,N)
  lo+=c*(l if c>0 else h);hi+=c*(h if c>0 else l)
 return lo,hi
@lru_cache(None)
def sign_cache(v):
 if not v:return 0
 for N in [24,48,96]:
  lo,hi=bounds(dict(v),N)
  if lo>0:return 1
  if hi<0:return -1
 raise AssertionError(('unresolved sign',v))
def sign(v):return sign_cache(tuple(sorted(v.items())))
def const(c):return {2:Q(c)} if c else {}
def walsh(v):
 a=list(v);step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
  step*=2
 return tuple(Q(x,len(a)) for x in a)
def restrict(v,i,b):
 return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
@lru_cache(None)
def stats(v):
 n=(len(v)-1).bit_length();a=walsh(v)
 I=sum(Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n))
 return a[0],I,add(*(e(x*x) for x in a))
def split(v,i):
 v0,v1=restrict(v,i,0),restrict(v,i,1)
 a,b=walsh(v0),walsh(v1)
 B=add(*(L((x+y)/2,(x-y)/2) for x,y in zip(a,b)))
 d=Q(sum(x!=y for x,y in zip(v0,v1)),len(v0))
 q=stats(tuple(x*y for x,y in zip(v0,v1)))[1]/2
 return v0,v1,d,q,B
def compose(w,h):return tuple(1-(1-x)*(1-y)//2 for y in h for x in w)
def rem(r,a,b):return add(L(1-r+r*a,r*b),sc(L(1-a,b),r*(1-r)),sc(L(a,b),-r))
def nodes(w):
 out=[]
 def rec(v,p):
  if len(v)==1:return
  v0,v1,d,q,B=split(v,0);a=stats(v)[0];beta=(stats(v0)[0]-stats(v1)[0])/2
  out.append((p,a,beta,d,q,B));rec(v0,p/2);rec(v1,p/2)
 rec(w,Q(1));return out
def mask(ns,r,K):
 out=[]
 for p,a,b,d,q,B in ns:
  R=rem(r,a,b);bf=add(sc(B,r),R)
  le(sign(add(R,const(-9*r*abs(b)))),0)
  out.append(sign(add(bf,const(-K*r*d)))>0)
 return tuple(out)
def accounts(ns,E):
 return sum(p*q for (p,a,b,d,q,B),v in zip(ns,E) if v),sum(p*d for (p,a,b,d,q,B),v in zip(ns,E) if v)
def serialize(v):return {str(p):str(c) for p,c in v.items()}
pilot='--pilot' in sys.argv
b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
controllers=[]
for point in [0,3]:
 c=list(b);c[point]*=-1
 # Selector is the least significant physical coordinate.
 w=tuple((b[x//2] if x%2==0 else c[x//2]) for x in range(32))
 controllers.extend([w,tuple(-x for x in w)])
rows=[];cases=0;migrations=0;negative_migrations=0;positive_migrations=0
for wi,w in enumerate(controllers):
 ns=nodes(w);wm,Iw,Hw=stats(w);t=(1-wm)/2
 cached={}
 def getmask(r,K):
  key=(r,K)
  if key not in cached:cached[key]=mask(ns,r,K)
  return cached[key]
 E0=tuple(sign(add(B,const(-4*d)))>0 for p,a,b,d,q,B in ns)
 Q0,P0=accounts(ns,E0)
 for code in range(8 if pilot else 256):
  h=tuple(1 if code>>x&1 else -1 for x in range(8));hm,J,Hh=stats(h);r=(1-hm)/2
  f=compose(w,h);fm,If,Hf=stats(f);eq(If,r*Iw+t*J)
  E=getmask(r,4);Qw,Pw=accounts(ns,E);Cold=r*Qw+J*Pw/2
  # One root controller query checked by full physical spectra, no transport shortcut.
  _,_,df,qf,Bf=split(f,0);_,_,dw,qw,Bw=split(w,0)
  a=wm;beta=(stats(restrict(w,0,0))[0]-stats(restrict(w,0,1))[0])/2
  eq(df,r*dw);eq(qf,r*qw+J*dw/2);eq(Bf,add(sc(Bw,r),rem(r,a,beta)))
  for i in range(3):
   h0,h1,d,q,Bh=split(h,i);children=[stats(h0),stats(h1)]
   rs=[(1-s[0])/2 for s in children];Js=[s[1] for s in children]
   eq(sum(rs)/2,r);eq(sum(Js)/2,J-d)
   Eb=[getmask(s,4) for s in rs]
   M=Q(0);child_bill=Q(0)
   for j in range(2):
    Qc,Pc=accounts(ns,Eb[j]);child_bill+=(rs[j]*Qc+Js[j]*Pc/2)/2
    for (p,a,b,dv,qv,Bv),old,new in zip(ns,E,Eb[j]):
     M+=p*(int(new)-int(old))*(rs[j]*qv+Js[j]*dv/2)/2
   eq(child_bill,Cold-d*Pw/2+M)
   if M:migrations+=1;positive_migrations+=int(M>0);negative_migrations+=int(M<0)
   f0,f1,df,qf,Bf=split(f,5+i)
   eq(f0,compose(w,h0));eq(f1,compose(w,h1));eq(df,t*d);eq(qf,t*q+Iw*d/2)
   a=hm;beta=(children[0][0]-children[1][0])/2
   eq(Bf,add(sc(Bh,t),rem(t,a,beta)))
   eps=int(sign(add(Bf,const(-4*df)))>0)
   eq(eps*qf+child_bill,Cold+eps*(t*q+Iw*d/2)-d*Pw/2+M)
   # The whole unfiltered prefix is invariant after accounting for both terminals.
   controller_all=r*sum(p*qv for p,a,b,dv,qv,Bv in ns)+J*Iw/2
   controller_children=sum(rs[j]*sum(p*qv for p,a,b,dv,qv,Bv in ns)+Js[j]*Iw/2 for j in range(2))/2
   eq(qf+controller_children,controller_all+t*q)
   eq(df+r*Iw+t*sum(Js)/2,If)
   terminalH=sc(add(children[0][2],children[1][2]),t/2)
   eq(terminalH,add(sc(children[0][2],t/2),sc(children[1][2],t/2)))
   for j in range(2):
    high=getmask(rs[j],13)
    for old,new in zip(E0,high):le(int(new),int(old))
    Qc,Pc=accounts(ns,high);le(rs[j]*Qc+Js[j]*Pc/2,rs[j]*Q0+Js[j]*P0/2)
   fixed_child=sum(rs[j]*Q0+Js[j]*P0/2 for j in range(2))/2
   eq(fixed_child,r*Q0+J*P0/2-d*P0/2)
   cases+=1
   if len(rows)<12:rows.append({'controller':wi,'core_code':code,'coordinate':i,'r':str(r),'r_children':list(map(str,rs)),'old_bill':str(Cold),'new_prefix_bill':str(child_bill),'migration':str(M),'current_bad':eps,'terminal_entropy':serialize(terminalH)})
   if time.monotonic()-start>(60 if pilot else 300):raise TimeoutError('frozen runtime cap')
out={'status':'PASS','mode':'pilot' if pilot else 'full','cases':cases,'exact_assertions':checks,'nonzero_migrations':migrations,'positive_migrations':positive_migrations,'negative_migrations':negative_migrations,'distinct_sign_certificates':sign_cache.cache_info().currsize,'runtime_seconds':time.monotonic()-start,'example_rows':rows}
(run/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='example_rows'}))
