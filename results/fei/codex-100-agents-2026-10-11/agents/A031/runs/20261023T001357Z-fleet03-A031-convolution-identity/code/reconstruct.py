"""Independent truth-table/FWHT reconstruction; no imports from main checker."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1]; count=0; cache={}
def ck(b):
 global count
 assert b
 count+=1
def lg(x):
 if x in cache:return cache[x]
 k=x.numerator.bit_length()-x.denominator.bit_length(); z=x/F(2)**k
 if z<1:z*=2;k-=1
 def series(z):
  t=(z-1)/(z+1);v=t;s=F(0)
  for j in range(24):s+=v/(2*j+1);v*=t*t
  return 2*s,2*s+2*v/(49*(1-t*t))
 a,b=series(z);c,d=series(F(2));cache[x]=(k+a/d,k+b/c);return cache[x]
def logs(terms):
 lo=hi=F(0)
 for w,x in terms:
  if not w:continue
  a,b=lg(x)
  if w<0:a,b=b,a
  lo+=w*a;hi+=w*b
 return lo,hi
def add(*xs):return tuple(sum(x[j] for x in xs) for j in [0,1])
def scale(x,c):return tuple(c*z for z in (x if c>=0 else x[::-1]))
def sub(x,y):return add(x,scale(y,-1))
def zero(x):ck(x[0]<=0<=x[1])
def marginal(p,mask):
 q={}
 for s,v in p.items():q[s&~mask]=q.get(s&~mask,F(0))+v
 return q
def fair(p,i):
 q=marginal(p,1<<i);return {s|b:v/2 for s,v in q.items() for b in [0,1<<i]}
def ce(p,q):return logs([(-v,q[s]) for s,v in p.items() if v])
def H(p):return ce(p,p)
def B(p,i):
 m=marginal(p,1<<i);return logs([(v,m[s&~(1<<i)]/v) for s,v in p.items() if v])
def cmi(p,i,j):
 a=marginal(p,1<<i);b=marginal(p,1<<j);m=marginal(p,(1<<i)|(1<<j))
 return logs([(v,v*m[s&~((1<<i)|(1<<j))]/(a[s&~(1<<i)]*b[s&~(1<<j)])) for s,v in p.items() if v])
def spectrum(L,h):
 n=2*L+4;free=[i for i in range(n) if i not in h]; vals=[]
 masks=[8|1|4,(((1<<L)-1)<<4)|1|2,(((1<<L)-1)<<(L+4))|2|4]
 for z in range(1<<len(free)):
  word=sum(v<<i for i,v in h.items())|sum(((z>>j)&1)<<i for j,i in enumerate(free))
  vals.append(1 if all(word&e for e in masks) else -1)
 # Integer FWHT, in-place; this route never uses clause-union Fourier coefficients.
 step=1
 while step<len(vals):
  for start in range(0,len(vals),2*step):
   for j in range(start,start+step):u,v=vals[j],vals[j+step];vals[j],vals[j+step]=u+v,u-v
  step*=2
 amp={sum(((s>>j)&1)<<i for j,i in enumerate(free)):F(v,len(vals)) for s,v in enumerate(vals)}
 ck(sum(v*v for v in amp.values())==1)
 return amp,{s:v*v for s,v in amp.items()}
start=time.monotonic();source=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));records=[]
for L in [1,2]:
 saved=next(c for c in source['cases'] if c['L']==L)
 ar,pr=spectrum(L,{})
 # Every signed convolution at L1, without relying on normalization alone.
 if L==1:
  for U in ar:ck(sum(v*ar[s^U] for s,v in ar.items())==int(U==0))
 for s,t in product([0,1],repeat=2):
  ap,p=spectrum(L,{3:s,1:t});Q=fair(p,0);incoming=marginal(Q,16);old=ce(p,Q)
  child=[];incs=[];fresh=[];js=[]
  for u in [0,1]:
   ac,pc=spectrum(L,{3:s,1:t,4:u});q=fair(pc,2)
   for z,v in ac.items():ck(v==ap[z]+(-1)**u*ap[z|16])
   ck(sum(q.values())==sum(incoming.values())==1)
   child.append(pc);incs.append(ce(pc,incoming));fresh.append(ce(pc,q));js.append(H(marginal(pc,4)))
  avg=lambda xs:scale(add(*xs),F(1,2))
  rho=cmi(p,4,0);Ic=cmi(p,4,2)
  Jc=sub(H(marginal(p,20)),avg(js));delta=sub(avg(fresh),avg(incs))
  net=sub(add(B(p,4),avg(fresh)),old)
  zero(sub(rho,sub(old,add(B(p,4),avg(incs)))))
  zero(sub(net,sub(delta,rho)));zero(add(net,Ic,Jc));zero(sub(B(p,0),B(p,2)))
  node=next(n for n in saved['nodes'] if n['x']==s and n['b']==t)
  for key,val in [('rho_actual_conditional_KL',rho),('Delta_prescribed_reset',delta),('net_Delta_minus_rho',net),('CMI_y_c',Ic),('J_y_after_c_marginal',Jc)]:
   got=[F(z) for z in node[key]];ck(max(val[0],got[0])<=min(val[1],got[1]))
  if (L,s,t)==(2,1,0):ck(Q[16]/(Q[0]+Q[16])==F(49,218));ck(rho[0]>0)
  records.append({'L':L,'x':s,'b':t,'independently_reconstructed':True})
 ck(time.monotonic()-start<55)
out={'method':'truth-table integer FWHT; distinct 24-term rational log enclosures','checks':count,'seconds':time.monotonic()-start,'records':records}
(R/'out/RECONSTRUCT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
