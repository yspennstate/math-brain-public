"""Independent representation: formal rational prime-log vectors and 32-term logs.
No imports of the Fourier, interval or transport implementation. Finite vectors
check exact algebra; all-dimensional extension is the concavity/Bellman proof.
"""
import json,time
from math import isqrt
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def ck(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55-second watchdog')
def add(a,b):
 d=dict(a)
 for p,c in b.items():d[p]=d.get(p,F(0))+c
 return {p:c for p,c in d.items() if c}
def scale(a,c):return {p:v*c for p,v in a.items() if v*c}
def factors(n):
 root=isqrt(n)
 if n>1 and root*root==n:return scale(factors(root),2)
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1 if p==2 else 2
 if n>1:out[n]=out.get(n,0)+1
 return out
def logvec(q):return add(factors(q.numerator),scale(factors(q.denominator),-1))
def atom(q):return scale(logvec(q),-q) if q else {}
def Hvec(k):
 e=F(1,2**k);return add(atom((1-2*e)**2),scale(atom(4*e*e),2**k-1))
def const(q):return {2:F(q)} if q else {}
def logbounds(q):
 shift=0
 while q<1:q*=2;shift-=1
 while q>=2:q/=2;shift+=1
 def natural(q):
  t=(q-1)/(q+1)
  lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
  return lo,lo+2*t**65/(65*(1-t*t))
 a,b=natural(q);c,d=natural(F(2))
 return F(shift)+a/d,F(shift)+b/c
def bounds(vec):
 lo=hi=F(0)
 for p,c in vec.items():
  a,b=logbounds(F(p));lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def positive(v):return max(F(0),v[0]),max(F(0),v[1])
def plus(*vs):return sum((v[0] for v in vs),F(0)),sum((v[1] for v in vs),F(0))
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def times(v,c):return (v[0]*c,v[1]*c) if c>=0 else (v[1]*c,v[0]*c)
def intersect(a,b):return a[0]<=b[1] and b[0]<=a[1]
def exact(q):return F(q),F(q)
def recorded(v):return tuple(F(x) for x in v)
S={};Q={1:{},2:{}};HH={};rows=[]
for k in range(1,33):
 e=F(1,2**k);HH[k]=Hvec(k);S[k]=add(const(8*k*e),scale(HH[k],-1))
 if k>=2:
  delta=add(scale(S[k-1],F(1,2)),scale(S[k],-1))
  q=2*e
  closed=add(const(8*(k-3)*e*e),add(atom((1-q)**2),scale(atom((1-2*q)**2),F(-1,2))))
  ck(delta==closed,'EXACT formal prime-log local deficit identity')
  if k==2:ck(delta=={},'exact boundary delta2 zero')
  else:
   ck(bounds(delta)[0]>0,'independent rigorous positive sign k>=3')
   Q[k]=add(delta,scale(Q[k-1],F(1,2)))
 target=add(HH[k],const(-8*(k-1)*e))
 ck(Q[k]==target,'EXACT prime-log Bellman telescope, not interval overlap')
 rows.append({'k':k,'Q_symbolic_terms':{str(p):str(c) for p,c in Q[k].items()}})
C=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
ss={k:bounds(S[k]) for k in [2,3,4]}
def T(k):
 e=F(1,2**(k-1));hv=add(atom(e),atom(1-e))
 return bounds(add(scale(hv,k),scale(HH[k],-1)))
for row in C['histories']:
 policy=row['policy'];s0=plus(exact(3),times(ss[4],F(1,4)))
 if policy==1:s1=plus(exact(2),times(ss[4],F(1,4)));s2=plus(exact(2),times(ss[3],F(1,8)))
 else:
  s1=plus(exact(3),times(ss[3],F(1,8)))
  s2=plus(exact(2),times(ss[3],F(1,8))) if policy==2 else plus(exact(F(5,2) if policy==3 else 3),times(ss[2],F(1,16)))
 b0=times(T(4),F(1,4));b1=exact(0) if policy==1 else times(T(3),F(1,8))
 u1=positive(minus(s1,s0));u2=positive(minus(s2,s1))
 for name,value in [('S0',s0),('S1',s1),('S2',s2),('B0_retained',b0),('B1_retained',b1),('U1_retained',u1),('U2_after_second_reset',u2)]:
  ck(intersect(recorded(row[name]),value),'independent physical sector formula '+name)
 ck(intersect(recorded(row['L0']),recorded(row['A'])),'prefix source booking readback')
 debt=plus(recorded(row['A']),u1,u2,b0,b1,exact(F(11,32)))
 ck(minus(s2,debt)[0]>F(1,128),'independently reconstructed remaining owner')
 if policy==0:ck(u1[0]>0 and u2[0]>0 and b1[0]>0,'genuine post-second-reset positive charge')
 if policy==1:ck(u2[0]>positive(minus(s2,s0))[1],'net cannot replace cumulative debit')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'independence':'rational prime-log vectors and independent 32-term logarithms, direct physical sector formulas; no shared helper import; author validation not external review','symbolic_rows':rows}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
