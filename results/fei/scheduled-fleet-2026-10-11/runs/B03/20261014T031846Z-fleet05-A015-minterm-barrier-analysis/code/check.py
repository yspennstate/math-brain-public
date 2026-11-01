from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial
import json, sys, time
BASE=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
 global COUNT
 COUNT+=1
 assert x,COUNT
def comp(n,k,positive=False):
 start=1 if positive else 0
 if k==1:
  if n>=start: yield (n,)
 else:
  for j in range(start,n-start*(k-1)+1):
   for tail in comp(n-j,k-1,positive): yield (j,)+tail
def fifth(x):
 if x==1: return F(1),F(1)
 lo=0; hi=1
 while F(hi)**5<x: hi*=2
 den=1<<64; low=0; high=hi*den
 while high-low>1:
  mid=(low+high)//2
  if F(mid,den)**5<x: low=mid
  else: high=mid
 ck(F(low,den)**5<=x<=F(high,den)**5)
 return F(low,den),F(high,den)
def ratio(sizes,occ):
 s=sum(sizes); u=sum(occ); v=F(s)**s/F(s+u)**(s+u)
 for a,b in zip(sizes,occ): v*=F(a+b)**(a+b)/F(a)**a
 return v
def occupation(sizes,u):
 lo=hi=F(0)
 maps=0
 for occ in comp(u,len(sizes)):
  m=factorial(u)
  for x in occ: m//=factorial(x)
  a,b=fifth(ratio(sizes,occ)**6)
  lo+=m*a; hi+=m*b; maps+=m
 ck(maps==len(sizes)**u)
 ck(lo**5>=F(1,len(sizes)**u))
 target=F(1); s=sum(sizes)
 for a in sizes: target*=F(a,s)**(u*a)
 ck(lo**(5*s)>=target)
 return lo,hi
def fwht(a):
 a=list(a); step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(i,i+step): a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 return a
def physical():
 for m in range(1,5):
  core=[(-1)**x.bit_count() for x in range(1<<m)]
  a=fwht(core); ck(a[-1]==1<<m); ck(all(v==0 for v in a[:-1]))
  for r in range(1,4):
   p=F(1,1<<r); n=m+r
   vals=[core[x>>r] if x&((1<<r)-1)==(1<<r)-1 else -1 for x in range(1<<n)]
   f=fwht(vals)
   ck(sum(v*v for v in f)==1<<(2*n))
   ck(F(f[0],1<<n)==p-1)
   # Nonempty data rows retain the core Fourier coefficient for every U.
   for U in range(1<<r): ck(F(f[(((1<<m)-1)<<r)|U]**2,1<<(2*n))==p*p)
   influences=[F(sum(vals[x]!=vals[x^(1<<j)] for x in range(1<<n)),1<<n) for j in range(n)]
   ck(influences==[p]*n); ck(sum(influences)==p*(m+r))
   ck(sum(F(f[S]**2,1<<(2*n)) for S in range(1<<n) if S>>r)==p)
 return 12
def lift_fixture(support,owned,parent,u):
 n=len(support); roots=[i for i,v in enumerate(parent) if v is None]
 which=[]
 for i in range(n):
  v=i
  while parent[v] is not None: v=parent[v]
  which.append(v)
 total=0; maps=0; root_below=0
 for alpha in product(range(n),repeat=u):
  ua={a:sum(which[v]==a for v in alpha) for a in roots}
  for a in roots:
   expected=1 if len(roots)==1 else ua[a]*prod_int(u+j for j in range(1,len(roots)-1))
   counts=0
   others=[b for b in roots if b!=a]
   # Enumerate gate-level added parents, allowing owners below old roots.
   for attaches in product(range(u),repeat=len(others)):
    newparent=list(parent)
    for b,j in zip(others,attaches): newparent[b]=alpha[j]
    valid=True
    for v in range(n):
     seen=set()
     while newparent[v] is not None:
      if v in seen: valid=False; break
      seen.add(v); v=newparent[v]
     if not valid or v!=a: valid=False; break
    if not valid: continue
    buckets={j:[] for j in range(u)}
    for b,j in zip(others,attaches): buckets[j].append(b)
    for seqs in product(*(list(permutations(buckets[j])) for j in range(u))):
     # Reconstruct the actual queue; old data edges precede/follow core
     # groups according to globally fixed core-first coordinate order.
     oldchildren={v:[] for v in range(n)}
     for b,v in enumerate(parent):
      if v is not None: oldchildren[v].append(b)
     queue=[a]; seen=[]
     while queue:
      v=queue.pop(0); seen.append(v)
      for j in range(u):
       if alpha[j]==v: queue.extend(seqs[j])
      queue.extend(oldchildren[v])
     ck(len(seen)==n and len(set(seen))==n)
     # Deleting precisely fresh-coordinate edges recovers the base forest.
     recovered=list(newparent)
     for b in others: recovered[b]=None
     ck(recovered==parent)
     counts+=1
   ck(counts==expected)
   if expected and a not in alpha: root_below+=1
   total+=counts
  maps+=1
 ck(maps==n**u)
 return {'gates':n,'components':len(roots),'u':u,'maps':maps,'added_events':total,'root_not_owner_cases':root_below}
def prod_int(xs):
 v=1
 for x in xs: v*=x
 return v
def fixtures():
 data=[([{0},{1},{2}],[{0},{1},{2}],[None,None,None]),([{0,1},{0,2}],[{1},{0}],[1,None]),([{0,1},{0,2},{3}],[{1},{0},{3}],[1,None,None])]
 rows=[]
 for sup,own,par in data:
  # All fixtures are minimal monotone primes of their actual union.
  n=max(max(b) for b in sup)+1
  truth=[1 if any(all(x>>j&1 for j in b) for b in sup) else -1 for x in range(1<<n)]
  a=fwht(truth); ck(sum(t*t for t in a)==1<<(2*n))
  ck(a[sum(1<<j for b in own for j in b)]!=0)
  for b in sup:
   for j in b:
    ck(any(truth[x]<0 and all(x>>k&1 for k in b-{j}) for x in range(1<<n)))
  for u in [1,2,3]: rows.append(lift_fixture(sup,own,par,u))
 ck(any(r['root_not_owner_cases'] for r in rows))
 return rows
def main():
 spec=json.loads((BASE/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
 allsizes=[ss for s in range(1,9) for k in range(1,min(4,s)+1) for ss in comp(s,k,True)]
 if '--spec' in sys.argv:
  spec['case_count']['occupation']=len(allsizes)*4
  spec['case_count']['pilot_occupation']=sum(sum(ss)<=4 for ss in allsizes)*4
  (BASE/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8'); print(json.dumps(spec['case_count'])); return
 pilot='--pilot' in sys.argv; begin=time.perf_counter(); rows=[]
 for sizes in allsizes:
  if pilot and sum(sizes)>4: continue
  for u in [1,2,3,4]:
   lo,hi=occupation(sizes,u)
   rows.append({'sizes':sizes,'u':u,'Z_interval':[str(lo),str(hi)]})
 # For equal parts, stronger termwise rational R>=k^-u certifies sharpness.
 for k in [2,3,4]:
  for L in [1,2,4,8,16]:
   for u in [1,2,3,4]:
    for occ in comp(u,k): ck(ratio((L,)*k,occ)>=F(1,k**u))
 fixture=fixtures(); nphysical=physical()
 result={'mode':'pilot' if pilot else 'full','status':'PASS','occupation_cases':len(rows),'assertions':COUNT,'runtime_seconds':time.perf_counter()-begin,'physical_activations':nphysical,'lift_fixtures':fixture,'intervals':rows}
 (BASE/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:result[k] for k in ['mode','status','occupation_cases','assertions','runtime_seconds']}))
if __name__=='__main__': main()
