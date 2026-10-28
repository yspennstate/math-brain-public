from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parents[1]
old=A/'runs/20261023T124031Z-account03-A078-coding-and-padding/code';sys.path.insert(0,str(old))
from exact import add,logvec,nonneg,scalar
spec=dict(helper_version='A078-direct-walsh-event-review-v1',family='all minority events d1..3, W_A plus Boolean event e; three fixed majority-parity families',domain=dict(event_dimensions=[1,2,3],family_r=[0,1,2]),case_count=dict(events=174,family_roots=3),symmetry='none',arithmetic='independent direct integer Walsh sums and physical edges; exact rational prime-log vectors; outward log signs',memory_estimate_MB=30,max_runtime_seconds=55)
(O/'FROZEN_INDEPENDENT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8');start=time.monotonic();checks=events=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<55
def walsh(v):return tuple(Q(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(v)),len(v)) for s in range(len(v)))
def phi(q):return add((-q,logvec(q))) if q else {}
def H(v):return add(*[(1,phi(a*a)) for a in walsh(v)])
def U(v):
 p=[a*a for a in walsh(v)]
 return add(*[(a,logvec(sum((b for t,b in enumerate(p) if (t&s)==s),Q(0))/a)) for s,a in enumerate(p) if a])
def inf(v,j):return Q(sum(a!=v[x^(1<<j)] for x,a in enumerate(v)),len(v))
def child(v,j,b):return tuple(a for x,a in enumerate(v) if ((x>>j)&1)==b)
for d in (1,2,3):
 size=1<<d
 for mask in range(1,1<<size):
  if mask.bit_count()>size//2:continue
  events+=1;p=Q(mask.bit_count(),size);a=tuple((mask>>x)&1 for x in range(size));e=tuple(1-2*t for t in a);W=tuple(1 for _ in e)+e
  aa=walsh(a);He=H(e);Hw=H(W)
  ck(Hw==add((1,phi((1-p)**2)),(1,phi(p*p)),*[(2,phi(q*q)) for q in aa[1:]]))
  ck(He==add((1,phi((1-2*p)**2)),*[(4,phi(q*q)) for q in aa[1:]],(-1,scalar(8*p*(1-p)))))
  ie=sum((inf(e,j) for j in range(d)),Q(0));J=sum((inf(W,j) for j in range(d)),Q(0))
  ck(J==ie/2);ck(inf(W,d)==p);ck(J+p<=ie);ck(nonneg(add((2,Hw),(-1,He))))
ck(events==174)
for r in (0,1,2):
 n=2*r+1;N=n+1;c=Q(comb(2*r,r),4**r)
 M=tuple(1 if 2*x.bit_count()<n else -1 for x in range(1<<n));g=tuple(1 if not(x&1) else M[x>>1] for x in range(1<<N));f=tuple(t*(-1 if x.bit_count()%2 else 1) for x,t in enumerate(g));F=f+tuple(f[x^((1<<N)-1)] for x in range(1<<N))
 af=walsh(f);ck(af[-1]**2==Q(1,4))
 for j in range(1,N):ck(af[((1<<N)-1)^(1<<j)]**2==c*c/4)
 ck(af[((1<<N)-1)^1]**2==Q(1,4));ck(H(F)==H(f));ck(H(f)==add((1,scalar(2)),(Q(1,2),H(M))))
 ck(inf(F,N)==Q(1,2));ck(sum((inf(F,j) for j in range(N+1)),Q(0))==n+1-n*c/2)
 # Both actual padding terminals have the full original U, including mean rows.
 uf=U(f);uF=U(F)
 ck(U(child(F,N,0))==uf);ck(U(child(F,N,1))==uf)
 lower=add((1,scalar(Q(1,4))),(n*c*c/4,logvec(1+1/(c*c))))
 ck(nonneg(add((1,uf),(-1,uF),(-1,lower))))
result=dict(status='PASS',exact_assertions=checks,events=events,direct_family_roots=3,runtime_seconds=time.monotonic()-start,review='A077@1 PROOF equations7-9 HOLDS at stated scope; whole transfer theorem not independently accepted here',checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(O/'INDEPENDENT_REVIEW.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
