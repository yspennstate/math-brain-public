from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import time,json,sys,math
START=time.monotonic();COUNTS={}; PILOT='--pilot' in sys.argv
def chk(ok,k):
 assert ok,k
 COUNTS[k]=COUNTS.get(k,0)+1
 if time.monotonic()-START>(60 if PILOT else 120):raise RuntimeError('frozen runtime exceeded')
def walsh(t):
 a=list(t);N=len(t);s=1
 while s<N:
  for k in range(0,N,2*s):
   for j in range(k,k+s):x,y=a[j],a[j+s];a[j],a[j+s]=x+y,x-y
  s*=2
 return tuple(Q(x,N) for x in a)
def child(t,b):return t[b::2]
def inf(t):return Q(sum(a!=b for a,b in zip(t[::2],t[1::2])),len(t)//2)
def add(*es):
 d={}
 for e in es:
  for p,c in e.items():d[p]=d.get(p,Q(0))+c
 return {p:c for p,c in d.items() if c}
def scale(e,c):return {p:v*c for p,v in e.items() if v*c}
@lru_cache(None)
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
@lru_cache(None)
def log(x):
 x=Q(x);return add(fac(x.numerator),scale(fac(x.denominator),-1))
def phi(x):return scale(log(1/x),x) if x else {}
def packet(a,b):return add(phi(a),phi(b),scale(phi(a+b),-1))
def paird(a,b):return add(phi(a*a),phi(b*b),scale(add(phi((a+b)**2),phi((a-b)**2)),Q(-1,2)))
def raw(w):return add(*(phi(x*x) for x in w))
@lru_cache(None)
def logint(p):
 k=p.bit_length()-1
 def s(x):
  z=(x-1)/(x+1);term=z;v=Q(0)
  for j in range(48):v+=term/Q(2*j+1);term*=z*z
  a=2*v;return a,a+2*term/(97*(1-z*z))
 a,b=s(Q(p,1<<k));c,d=s(Q(2));return a+k*c,b+k*d
@lru_cache(None)
def interval_cached(items):
 a=b=Q(0)
 for p,c in items:
  x,y=logint(p);a+=c*(x if c>=0 else y);b+=c*(y if c>=0 else x)
 return a,b
def interval(e):return interval_cached(tuple(sorted(e.items())))
def lower_nonnegative(e):return not e or interval(e)[0]>=0
def le(a,b):return lower_nonnegative(add(b,scale(a,-1)))
def pick_min(a,b):
 d=add(a,scale(b,-1))
 if not d:return a
 lo,hi=interval(d)
 if hi<=0:return a
 if lo>=0:return b
 raise AssertionError('min sign unresolved by frozen precision')
@lru_cache(None)
def physical(t):
 if len(t)==1:return {},Q(0),{}
 w=walsh(t);B=add(*(packet(w[2*i]**2,w[2*i+1]**2) for i in range(len(t)//2)))
 l,r=physical(child(t,0)),physical(child(t,1))
 return add(B,scale(add(l[0],r[0]),Q(1,2))),inf(t)+(l[1]+r[1])/2,raw(w)
@lru_cache(None)
def defect_tail(r):
 if r==0:return {}
 u=Q(1,1<<r)
 b=add(packet((1-2*u)**2,4*u*u),scale(packet(4*u*u,4*u*u),(1<<(r-1))-1))
 return add(b,scale(defect_tail(r-1),Q(1,2)))
def permute(t,order):
 return tuple(t[sum(((z>>j)&1)<<i for j,i in enumerate(order))] for z in range(len(t)))
@lru_cache(None)
def core_ledger(u,r,wgt=Q(1)):
 if len(u)==1:return {},{}, {},{}, {},Q(0),Q(0)
 p=Q(1,1<<r);m=Q(sum(u),len(u));beta=walsh(u)[1];t=beta*beta;v=1-m*m
 C=1-p+p*m
 def M(s):return add(packet(C*C,p*p*s),scale(packet((1-m)**2,s),p*(1-p)))
 mt=M(t);mv=M(v)
 cap2=add(scale(mv,t/v),scale(log(v/t),p*t)) if t else {}
 cap=pick_min(mv,cap2) if t else {}
 empty=packet(m*m,t);emptyd=paird(m,beta)
 f=tuple(1 if z>>((len(u)).bit_length()-1) else u[z&(len(u)-1)] for z in range(len(u)*(1<<r))) if r<=3 and len(u)<=8 else None
 if f is not None:
  fw=walsh(f);bi=add(*(packet(fw[2*i]**2,fw[2*i+1]**2) for i in range(len(f)//2)))
  uw=walsh(u);binner=add(*(packet(uw[2*i]**2,uw[2*i+1]**2) for i in range(len(u)//2)))
  chk(bi==add(scale(add(binner,scale(empty,-1)),p),mt),'biased_erasure_identity')
  di=add(raw(fw),scale(add(raw(walsh(child(f,0))),raw(walsh(child(f,1)))),Q(-1,2)))
  outerN=add(paird(C,p*beta),scale(paird(1-m,beta),p*(1-p)),scale(mt,-1))
  innerd=add(raw(uw),scale(add(raw(walsh(child(u,0))),raw(walsh(child(u,1)))),Q(-1,2)))
  chk(di==add(scale(add(innerd,scale(emptyd,-1)),p),mt,outerN),'biased_decrement_identity')
 chk(le(mt,cap),'certified_cap_envelope')
 chk(abs(beta)<=inf(u),'singleton_bound')
 l=core_ledger(child(u,0),r,wgt/2);rr=core_ledger(child(u,1),r,wgt/2)
 all_expr=[cap,mt,empty,emptyd,{}]
 out=[]
 for j,e in enumerate(all_expr):out.append(add(scale(e,wgt),l[j],rr[j]))
 return tuple(out)+ (wgt*inf(u)+l[5]+rr[5],wgt*t+l[6]+rr[6])


