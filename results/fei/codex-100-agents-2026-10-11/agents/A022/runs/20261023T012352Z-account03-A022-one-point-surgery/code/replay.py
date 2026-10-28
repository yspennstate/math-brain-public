"""Independent direct-character reconstruction; imports no production helper."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
root=Path(__file__).resolve().parents[1]; count=0
def ck(v):
 global count
 count+=1; assert v,count
def add(*es):
 d={}
 for e in es:
  for p,c in e.items(): d[p]=d.get(p,F(0))+c
 return {p:c for p,c in d.items() if c}
def scale(e,a): return {p:c*a for p,c in e.items() if c*a}
@lru_cache(None)
def log(x):
 x=F(x); out={}
 for n,sign in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p<=n:
   while n%p==0: out[p]=out.get(p,0)+sign; n//=p
   p+=1
 return {p:F(c) for p,c in out.items() if c}
def C(P,Q): return add(*(scale(log(q),-p) for p,q in zip(P,Q) if p))
def H(P): return C(P,P)
def spec(f):
 n=len(f)
 return [F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(f))**2,n*n) for s in range(n)]
def edge(f,i): return F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def dataref(labels,fixed):
 out=[]
 for s in range(1<<len(labels)):
  q=F(1)
  for start in [0,3]:
   remain=[i for i in labels if start<=i<start+3]
   freq=sum(((s>>labels.index(i))&1)<<j for j,i in enumerate(remain))
   vals=[fixed[i] for i in fixed if start<=i<start+3]
   if len(vals)==0: q*=F(9 if freq==0 else 1,16)
   if len(vals)==1: q*=F(1,4) if vals[0]==0 else F(13 if freq==0 else 1,16)
   if len(vals)==2:
    main=int(all(v==0 for v in vals)); q*=F(15 if freq==main else 1,16)
  out.append(q)
 ck(sum(out)==1)
 return out
start=time.perf_counter(); cases=0
for v in [0,1,3,63]:
 for A in [(0,1),(1,1)]:
  b=[(-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1) for x in range(64)]
  f=[b[x]*(1-2*int(x==v and A[z])) for z in range(2) for x in range(64)]
  P0=spec(f); R=[sum(P0[:64]),sum(P0[64:])]
  L=scale(H(spec([1-2*a for a in A])),F(1,64)); U=F(1,32)
  levels=[]; pivs=[]; nodes=[(f,{})]; labels=list(range(6))
  for d in range(7):
   ce={}; ent={}; idata=F(0); rm=[F(0),F(0)]
   for ff,fixed in nodes:
    M=1<<len(labels); P=spec(ff); q=dataref(labels,fixed)
    ref=[q[s]*R[z] for z in range(2) for s in range(M)]
    ck(sum(ref)==1); ck(all(not p or r>0 for p,r in zip(P,ref)))
    ce=add(ce,scale(C(P,ref),F(1,len(nodes))))
    ent=add(ent,scale(H(P),F(1,len(nodes))))
    idata+=sum((edge(ff,i) for i in range(len(labels))),F(0))/len(nodes)
    for z in range(2): rm[z]+=sum(P[z*M:(z+1)*M])/len(nodes)
   ck(rm==R)
   B=add({2:4*idata-U},L,scale(ce,-1)); D=add(ce,scale(ent,-1))
   levels.append((ce,ent,idata,B,D))
   if d:
    old=levels[d-1]; drop=add(old[0],scale(ce,-1)); loss=add({2:4*pivs[-1]},scale(drop,-1))
    ck(B==add(old[3],scale(loss,-1)))
    ck(add(old[1],scale(ent,-1))==add(drop,D,scale(old[4],-1)))
    ck(old[2]-idata==pivs[-1])
   if d==6: break
   pivs.append(sum((edge(ff,0) for ff,_ in nodes),F(0))/len(nodes))
   new=[]
   for ff,fixed in nodes:
    for val in [0,1]: new.append(([a for x,a in enumerate(ff) if x%2==val],dict(fixed,**{str(d):val})))
   nodes=[(ff,{int(k):v for k,v in fixed.items()}) for ff,fixed in new]; labels=labels[1:]
  E=add(*(add({2:4*pivs[d]},scale(levels[d][1],-1),levels[d+1][1]) for d in range(6)))
  ck(add(levels[-1][3],levels[-1][4],E)==add(levels[0][3],levels[0][4]))
  ck(levels[-1][1]==L); ck(levels[-1][0]==H(R))
  ck(levels[-1][3]==add(L,scale(H(R),-1),{2:-U}))
  cases+=1
obj={'status':'PASS','cases':cases,'assertions':count,'seconds':time.perf_counter()-start,
     'method':'direct character sums and physical edges, independent complete joint reference assembly; no production imports'}
(root/'out/replay.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline=''); print(json.dumps(obj))
