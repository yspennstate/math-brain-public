from pathlib import Path
import sys,time,json,hashlib
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
source=R.parent/'20261022T221625Z-account03-A024-biased-child-stability/code/check.py'
exec(compile(source.read_text(encoding='utf-8').split("pilot='--pilot'")[0],str(source),'exec'))
checks=0;start=time.monotonic();functions=queries=restrictions=0
# Independent direct character sums, not the butterfly transform in check.py.
def spectrum(v):
 N=len(v)
 return tuple(Q(sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(N)),N) for s in range(N))
def A(v):return sum(map(abs,spectrum(v)))
for n in range(4):
 N=1<<n
 for code in range(1<<N):
  v=tuple(-1 if code>>x&1 else 1 for x in range(N));w=spectrum(v);norm=sum(map(abs,w));functions+=1
  for i in range(n):
   v0,v1=restrict(v,i,0),restrict(v,i,1)
   d=Q(sum(a!=b for a,b in zip(v0,v1)),len(v0))
   B=add(*(L(w[s],w[s^(1<<i)]) for s in range(N) if not s>>i&1))
   le(sign(add(B,const(-2*norm*d))),0)
   le(A(v0),norm);le(A(v1),norm);queries+=1;restrictions+=2
# Nonvacuous positive control: the affine phase with a point edit has B>d.
v=(-1,1,1,1);w=spectrum(v);B=add(L(w[0],w[1]),L(w[2],w[3]));eq(sign(add(B,const(-Q(1,2)))),1)
# Missing branch in the main fixed fixtures: q=1_A+1_B with independent
# codimension-two flats, so their intersection is the sole actual edit.
n=4;Aset={x for x in range(16) if x&3==0};Bset={x for x in range(16) if x&12==0}
p=(1,2,3,4,8,12)
v=tuple((-1)**((sum((x&m)==m for m in p)%2)^int(x in Aset or x in Bset)) for x in range(16))
eq(v,tuple(-1 if x in Aset&Bset else 1 for x in range(16)))
le(A(v),3)
for i in range(4):
 w=spectrum(v);v0,v1=restrict(v,i,0),restrict(v,i,1);d=Q(sum(a!=b for a,b in zip(v0,v1)),8)
 B=add(*(L(w[s],w[s^(1<<i)]) for s in range(16) if not s>>i&1))
 le(sign(add(B,const(-6*d))),0)
assert time.monotonic()-start<55
out=dict(status='PASS',functions=functions,coordinate_queries=queries,physical_children=restrictions,exact_assertions=checks,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),lane='author direct character sums; not independent human review',positive_controls=1,extra_intersection_only_fixture=True)
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
