"""Independent FWHT representation: audit exact iff fresh==inherited."""
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0;cases=0;balanced=0;unbalanced=0
def ck(x):
 global C
 assert x;C+=1
 assert time.perf_counter()-start<55
def walsh(t):
 a=list(t);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [F(v,len(t)) for v in a]
def qref(p,alpha):
 q=[(1-alpha)*v for v in p];q[0]+=alpha*p[0];q[-1]+=alpha*(1-p[0]);return q
for bits in range(256):
 t=[(-1 if bits>>x&1 else 1) for x in range(8)];w=walsh(t);p=[a*a for a in w]
 for i in range(3):
  childs=[[t[x] for x in range(8) if x>>i&1==b] for b in (0,1)]
  wc=[walsh(z) for z in childs];pc=[[a*a for a in z] for z in wc]
  essential=lambda z:all(any(z[x]!=z[x^(1<<j)] for x in range(len(z))) for j in range(2))
  if not (wc[0][0]==wc[1][0] and pc[0][-1]>0 and pc[1][-1]>0 and p[-1]>0 and all(essential(z) for z in childs)):continue
  t0,t1=pc[0][-1],pc[1][-1]
  for alpha in (F(1,8),F(1,7),F(1,6),F(1,2)):
   q=qref(p,alpha);pe=[F(0)]*4;qe=[F(0)]*4
   for s in range(8):
    u=(s&((1<<i)-1))|((s>>(i+1))<<i);pe[u]+=p[s];qe[u]+=q[s]
   eq=True;rs=[]
   for b in (0,1):
    joint=[qe[s]*pc[b][s]/(2*pe[s]) if pe[s] else F(0) for s in range(4)]
    r=sum(joint);rs.append(r);inherited=[v/r for v in joint];fresh=qref(pc[b],alpha)
    eq &= inherited==fresh
   ck(eq==(t0==t1));ck((rs==[F(1,2),F(1,2)])==(t0==t1))
   if t0==t1:balanced+=1
   else:unbalanced+=1
   cases+=1
ck(cases>0 and balanced>0)
# On <=3 bits the equal-mean occupied-full regime need not contain unequal energies;
# A047 r4..6 source witnesses independently exercise that missing branch in CHECK.json.
out={'status':'PASS','eligible_profiles':cases,'balanced':balanced,'unbalanced':unbalanced,'assertions':C,'runtime_seconds':time.perf_counter()-start,'arithmetic':'independent FWHT exact fractions','scope':'all256 three-bit signs, all3 coordinates,4 tilts; no symmetry'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
