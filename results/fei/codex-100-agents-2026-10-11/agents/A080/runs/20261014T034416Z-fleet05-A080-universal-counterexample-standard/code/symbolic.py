from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def multiply(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def from_counts(counts,n):
 out=[F(0)]*(n+1)
 for k,c in enumerate(counts):
  for j in range(n-k+1):out[k+j]+=c*comb(n-k,j)*(-1)**j
 return out
def at(poly,p):
 out=F(0)
 for z in poly[::-1]:out=out*p+z
 return out
N={0,1,2,4,8,16,32,6,17,40};h=[-1 if x in N else 1 for x in range(64)];J=[-h[x^1] for x in range(64)]
record=[]
for name,t in [('h',h),('J',J)]:
 counts=[sum(t[x]<0 and x.bit_count()==k for x in range(64)) for k in range(7)]
 alpha=from_counts(counts,6);piv=[]
 for j in range(6):
  cs=[0]*6
  for x in range(64):
   if not x&(1<<j) and t[x]!=t[x|(1<<j)]:cs[x.bit_count()]+=1
  piv.append(from_counts(cs,5))
 if name=='h':
  ck(counts==[1,6,3,0,0,0,0]);ck(alpha==multiply([1,-4,6,-4,1],[1,4,-2]))
  ck(all(q==[0,4,-14,18,-10,2] for q in piv))
  Q=[6*x for x in piv[0]];ck(at(Q,F(1,16))==F(313875,262144));ck(at(Q,1-F(7,32))==F(1003275,8388608))
 else:
  ck(counts==[0,4,10,18,15,6,1]);ck(alpha==[0,4,-10,18,-19,10,-2]);ck(sum(q[0] for q in piv)==4)
  ck([q[0] for q in piv]==[0,1,1,1,0,1]);ck(at(alpha,F(1,16))<F(1,4))
 for q in piv:ck(len(q)==6 and all(z.denominator==1 for z in q))
 record.append({'gate':name,'negative_counts':counts,'negative_probability_polynomial':list(map(str,alpha)),'pivotal_polynomials':[[str(x) for x in q] for q in piv]})
ck(time.perf_counter()-start<60)
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'global_gate_polynomials':record}
(R/'out/SYMBOLIC.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='global_gate_polynomials'},indent=2))
