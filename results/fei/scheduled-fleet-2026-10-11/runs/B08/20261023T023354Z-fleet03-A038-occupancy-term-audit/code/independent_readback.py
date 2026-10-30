"""Separate root CE lane and rational payment readback; no checker imports."""
import json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0;GRID=2**100
def check(b,label):
 global count
 count+=1
 assert b,label
 if time.monotonic()-start>55:raise RuntimeError('55 second watchdog')
def floor(v):return F((v*GRID).__floor__(),GRID)
def ceil(v):return F((v*GRID).__ceil__(),GRID)
def ln(q):
 t=(q-1)/(q+1)
 a=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 return a,a+2*t**65/(65*(1-t*t))
ln2=ln(F(2))
def lg(q):
 shift=0
 while q<1:q*=2;shift-=1
 while q>=2:q/=2;shift+=1
 lo,hi=ln(q)
 return floor(shift+lo/ln2[1]),ceil(shift+hi/ln2[0])
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):
 z=[a[0]*c,a[1]*c];return min(z),max(z)
def log_interval(a):return lg(a[0])[0],lg(a[1])[1]
def entropy(p):
 out=(F(0),F(0))
 for q in p:
  if q:out=add(out,scale(lg(q),-q))
 return out
def intersect(a,b):return a[0]<=b[1] and b[0]<=a[1]
def interval(row):return tuple(map(F,row))
C=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
lo,hi=interval(C['canonical_root_bracket']);v=F(15,16)
d=[F(1,2),F(1,2),F(1,4),F(1,16),F(1,16),F(1,16),F(1,4)]
ce=scale(lg(1-v),-(1-v))
ce=add(ce,scale(log_interval((v/hi,v/lo)),-v))
for x in d:
 r=x/v
 ce=add(ce,scale(log_interval((lo*r,hi*r)),-x))
 ce=add(ce,scale(log_interval((1-hi*r,1-lo*r)),-(v-x)))
Hp=entropy([F(9,16)]+[F(1,16)]*7)
Hroot=add((F(3),F(3)),scale(Hp,F(1,4)))
A=add(ce,scale(Hroot,F(-1)))
check(intersect(A,interval(C['source_A'])),'independent affine cross-entropy vs atomwise KL')
check(1<A[0] and A[1]<F(39,32),'canonical source magnitude independently bounded')
scalar=[]
for k in range(9):
 if k==0:T=(F(0),F(0))
 else:
  eps=F(1,2**k);p=[(1-2*eps)**2]+[4*eps*eps]*(2**k-1)
  T=add(scale(entropy([2*eps,1-2*eps]),k),scale(entropy(p),-1))
 check(T[1]<=F(7,8),'independent reset KL limit')
 scalar.append({'k':k,'T':[str(x) for x in T]})
histories=C['histories'][:]
if (R/'out/DIRECT_PREFIX.json').exists():
 histories+=json.loads((R/'out/DIRECT_PREFIX.json').read_text(encoding='utf-8'))['histories']
for row in histories:
 S=interval(row['S']);L=interval(row['L']);B=interval(row['B'])
 residual=(S[0]-L[1]-F(11,32)-B[1],S[1]-L[0]-F(11,32)-B[0])
 check(residual[0]>F(7,32),'independent exact endpoint payment')
 check(intersect(residual,interval(row['remaining'])),'saved residual agrees with independent endpoint arithmetic')
 check(B[1]<=F(7,32),'retained reset budget')
 check(sum(F(t['weight']) for t in row['terminals'])==1,'all complementary terminal weights retained')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'independent_root_A':[str(x) for x in A],'scalar_rows':scalar,'method':'32-term rational atanh; affine matched-moment root CE, distinct from direct atomwise 24-term checker KL; artifact endpoints rechecked as Fractions'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
