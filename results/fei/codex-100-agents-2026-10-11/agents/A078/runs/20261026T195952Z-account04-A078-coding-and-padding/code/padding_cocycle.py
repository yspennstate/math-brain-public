"""Frozen exact pilot: signed upper-set correction at uncovered physical queries."""
from pathlib import Path
from fractions import Fraction as Q
import sys, json, hashlib, time
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
OLD=A/'runs/20261023T124031Z-account03-A078-coding-and-padding/code'
sys.path.insert(0,str(OLD))
from exact import fwht,restrict,infl,add,logvec,scalar,interval,nonneg
O=R/'out'; O.mkdir(exist_ok=True)
spec=dict(helper_version='A078-cocycle-v1', family='Every Boolean seed on n=1,2,3; every nonzero one-column systematic parity padding; every uncovered coordinate',domain=[1,2,3],case_count=2336,symmetry='none',arithmetic='Fraction Walsh/edges and exact prime-log vectors; rational outward log intervals for strict signs',memory_estimate_MB=40,max_runtime_seconds=55,helper_sha256=hashlib.sha256((OLD/'exact.py').read_bytes()).hexdigest(),target='Exact drift correction; disprove or retain supermartingale assumption, not FEI')
(O/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic(); checks=cases=0; witnesses={}; extrema={}
def ck(b):
 global checks
 checks+=1
 assert b,checks
 if time.monotonic()-start>55: raise TimeoutError('frozen 55-second pilot')
def U(v):
 p=[a*a for a in fwht(v)]; pi=p[:]; n=len(v).bit_length()-1
 for j in range(n):
  for s in range(len(pi)):
   if not (s>>j)&1: pi[s]+=pi[s|(1<<j)]
 return add(*[(a,logvec(pi[s]/a)) for s,a in enumerate(p) if a])
def lift(v,P):
 n=len(v).bit_length()-1
 return tuple(v[(x%len(v))^(P if (x>>n)&1 else 0)] for x in range(2*len(v)))
def drift(v,i):
 return add((1,U(v)),(-Q(1,2),U(restrict(v,i,0))),(-Q(1,2),U(restrict(v,i,1))))
def remove_bit(P,i): return (P&((1<<i)-1))|((P>>(i+1))<<i)
def serial(v):return {str(p):str(a) for p,a in v.items()}
for n in (1,2,3):
 for mask in range(1<<(1<<n)):
  v=tuple(1-2*((mask>>x)&1) for x in range(1<<n)); uv=U(v)
  for P in range(1,1<<n):
   F=lift(v,P); d=add((1,uv),(-1,U(F)))
   ck(nonneg(d))
   for i in range(n):
    if (P>>i)&1:continue
    cases+=1; pc=remove_bit(P,i)
    children=[restrict(v,i,b) for b in (0,1)]
    lifted=[restrict(F,i,b) for b in (0,1)]
    for b in (0,1):ck(lifted[b]==lift(children[b],pc))
    dc=[add((1,U(children[b])),(-1,U(lifted[b]))) for b in (0,1)]
    correction=add((-1,d),(Q(1,2),dc[0]),(Q(1,2),dc[1]))
    ck(drift(F,i)==add((1,drift(v,i)),(1,correction)))
    ck(infl(F,i)==infl(v,i))
    lo,hi=interval(correction)
    sign='positive' if lo>0 else ('negative' if hi<0 else 'zero' if not correction else 'undecided')
    coeff=fwht(v)
    erasure_overlap=any(coeff[s] and coeff[s|(1<<i)] for s in range(len(coeff)) if not (s>>i)&1)
    if sign == 'positive' and erasure_overlap: sign='positive_nonzero_erasure'
    if sign not in witnesses:
     witnesses[sign]=dict(n=n,mask=mask,column=P,coordinate=i,seed=list(v),lift=list(F),delta_root=serial(d),delta_children=[serial(x) for x in dc],signed_correction=serial(correction),base_drift=serial(drift(v,i)),lift_drift=serial(drift(F,i)),physical_influence=str(infl(F,i)),interval=[str(lo),str(hi)])
ck(cases==2336)
result=dict(status='PASS',cases=cases,exact_assertions=checks,runtime_seconds=time.monotonic()-start,signs=list(witnesses),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(O/'WITNESSES.json').write_text(json.dumps(witnesses,indent=2),encoding='utf-8')
(O/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))

