from pathlib import Path
from fractions import Fraction as F
import json,time
from arithmetic import *
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0

def ck(x):
 global checks
 assert x;checks+=1
 if time.perf_counter()-t0>55:raise RuntimeError('frozen55s')
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def h2(x):return add(entterm(x),entterm(1-x))
def erasure(f):
 P=law(f);B=Z
 for x in range(0,len(P),2):B=add(B,sub(add(entterm(P[x]),entterm(P[x+1])),entterm(P[x]+P[x+1])))
 return B
cores=[tuple(-1 if m>>x&1 else 1 for x in range(4)) for m in range(16)]
cores +=[(-1,-1,-1,1,1,1,1,1),(-1,1)]+[tuple([-1]+[1]*(2**n-1)) for n in [3,4,5,6]]
physical=[]
for g in cores:
 f=family(g);a=1-spectrum(g)[0];d=F(5,16)*a;B=erasure(f);P=law(f)
 ck(infl(f,0)==d);q0=P[0]+P[1];qstar=1-q0
 ck(P[0]==(1-F(7,16)*a)**2);ck(P[1]==d*d);ck(qstar==F(7,8)*a-F(37,128)*a*a)
 if d:ck(B[1]<F(157,40)*d)
 else:ck(B==Z)
 physical.append({'core':list(g),'dimension':len(f).bit_length()-1,'a':str(a),'d':str(d),'B':fmt(B)})
# Control indicator amplitudes from an independently materialized16-entry table.
AV=tuple(F(bool((x>>1&1)*(x>>2&1)*(x>>3&1) or (x&1)*((x>>2&1) or (x>>3&1)))) for x in range(16))
AH=spectrum(AV);pi=F(7,16);ck(AH[0]==pi);ck(sum(v*v for v in AH)==pi);LA=entropy([v*v for v in AH]);cases=[]
for n in list(range(2,25))+[32,48,64]:
 a=F(1,2**(n-1));I=a*(F(7,16)*n+F(3,4));M=scale(h2(pi*a),n)
 for c in [F(5,16),F(1,16),F(3,16),F(3,16)]:M=add(M,h2(c*a))
 ck(M[0]>(n-1)*I)
 H=add(entterm((1-pi*a)**2),scale(LA,2*a));H=add(H,scale(log(1/a),4*pi*a));H=sub(H,entterm((pi*a)**2))
 if n<=6:
  g=tuple([-1]+[1]*(2**n-1));f=family(g);ck(influence(f)==I)
  directM=Z
  for i in range(n+4):directM=add(directM,h2(infl(f,i)))
  overlap(M,directM);overlap(H,entropy(law(f)))
 if n>=6:ck(M[0]>4*I)
 cases.append({'n':n,'I':str(I),'M':fmt(M),'H':fmt(H),'M_over_I':fmt(scale(M,1/I)),'H_over_I':fmt(scale(H,1/I))})
# Exact scalar constants used by the all-a proof.
ck(L2[0]>F(2,3));ck(F(1)/L2[0]<F(3,2));ck(F(3,2)<F(74,25));ck(F(14,5)+F(9,8)==F(157,40));ck(F(157,40)<4)
out={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-t0,'physical_cases':len(physical),'grouped_cases':len(cases),'physical':physical,'grouped':cases}
(R/'out/SINGLETON.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print({k:v for k,v in out.items() if k not in ['physical','grouped']})
