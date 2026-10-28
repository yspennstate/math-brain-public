from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,time,json
R=Path(__file__).resolve().parents[1];checks=0;started=time.perf_counter()
def ck(x):
 global checks
 checks+=1
 assert x,checks
def trees(C,d):
 yield None
 if d:
  for i in C:
   sub=list(trees(tuple(j for j in C if j!=i),d-1))
   for a in sub:
    for b in sub:yield(i,a,b)
@lru_cache(None)
def good(f,K=1):
 N=len(f);n=(N-1).bit_length()
 inf=Q(sum(f[x]!=f[x^(1<<j)] for j in range(n) for x in range(N)),N)
 a=N*N*(2*n-K*inf);ck(a.denominator==1);a=int(a)
 product=1
 for s in range(N):
  w=sum(f[x]*(1 if (x&s).bit_count()%2==0 else -1) for x in range(N))
  if w:product*=pow(w*w,w*w)
 return pow(2,a)<=product if a>=0 else True
@lru_cache(None)
def closed(f):
 n=(len(f)-1).bit_length()
 for pattern in itertools.product((-1,0,1),repeat=n):
  row=tuple(v for x,v in enumerate(f) if all(b==-1 or ((x>>i)&1)==b for i,b in enumerate(pattern)))
  if not good(row):return False
 return True
policies=list(trees(tuple(range(4)),2));seed=tuple((-1 if x&3==0 else 1)*(-1 if x>>2==0 else 1) for x in range(16))
eligible=cases=0
for edit in (None,*range(16)):
 E=set() if edit is None else {edit};G=tuple(-v if x in E else v for x,v in enumerate(seed));D=len(E)
 for tree in policies:
  total=0;q=[0,0];a=[0,0];e=[0,0];leaves={}
  for x in range(16):
   node=tree;touched=set();known={}
   while node:
    i,lo,hi=node;j=i//2;pit=int(G[x]!=G[x^(1<<i)])
    total+=pit
    if j not in touched:q[j]+=pit;a[j]+=1;e[j]+=int(x in E)
    touched.add(j);known[i]=(x>>i)&1;node=hi if (x>>i)&1 else lo
   key=tuple(sorted(known.items()));leaves.setdefault(key,[]).append(x)
  ok=all(closed(tuple(G[x] for x in row)) for row in leaves.values());eligible+=ok;cases+=1
  for j in range(2):
   ck(2*q[j]>=a[j]-4*e[j]);ck(0<=e[j]<=D)
   if ok:ck(4*(D-e[j])>=16-a[j]);ck(2*q[j]>=16-4*D)
  ck(total>=sum(q))
  if ok:ck(total>=16-4*D)

def rank(vs):
 basis={}
 for v in vs:
  while v:
   b=v.bit_length()-1
   if b in basis:v^=basis[b]
   else:basis[b]=v;break
 return len(basis)
def amin(f):
 N=len(f);cost={v:min(sum(f[x]!=f[x^v] for x in range(N)),sum(f[x]==f[x^v] for x in range(N))) for v in range(1,N)}
 chosen=[];answer=0
 for v in sorted(cost,key=lambda v:(cost[v],v)):
  if rank(chosen+[v])>len(chosen):chosen.append(v);answer+=cost[v]
 ck(len(chosen)==(N-1).bit_length())
 return Q(answer,N),cost
tensor=0
for mask1 in range(16):
 f=tuple(1-2*((mask1>>x)&1) for x in range(4));af,cf=amin(f)
 for mask2 in range(16):
  g=tuple(1-2*((mask2>>x)&1) for x in range(4));ag,cg=amin(g)
  F=tuple(f[x&3]*g[x>>2] for x in range(16));aF,cF=amin(F)
  ck(aF==af+ag)
  for v,c in cF.items():
   ck(Q(c,16)>=max(Q(cf.get(v&3,0),4),Q(cg.get(v>>2,0),4)))
  tensor+=1
out=dict(status='PASS',checks=checks,tree_cases=cases,eligible=eligible,all_tensor_pairs=tensor,
 wall_seconds=time.perf_counter()-started,method='all-input path integration plus independent direct Walsh; no primary helper imported')
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
