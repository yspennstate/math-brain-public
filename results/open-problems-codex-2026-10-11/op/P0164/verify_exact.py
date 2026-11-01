from itertools import combinations
from collections import Counter
from fractions import Fraction
import json,math

def fn(E,x):
 k=x.bit_count()
 return 1 if k>=4 or k==3 and 31-x not in E or k==2 and x in E else -1

def spectrum(f):
 W=[0]*6
 for s in range(32):
  c=sum(f[x]*(-1)**((x&s).bit_count()) for x in range(32))
  W[s.bit_count()]+=c*c
 return tuple(W)

reps=[(),(3,),(3,5),(3,5,9),(3,5,9,17),(3,5,6)]
expected=[(0,720,0,160,0,144),(0,704,0,256,0,64),(0,720,0,288,0,16),(0,768,0,256,0,0),(0,848,0,160,0,16),(0,768,0,256,0,0)]
for E,w in zip(reps,expected):assert spectrum([fn(E,x) for x in range(32)])==w
pairs=[x for x in range(32) if x.bit_count()==2]
counts=Counter(); functions=set()
for flags in range(1<<10):
 E=[pairs[j] for j in range(10) if flags>>j&1]
 if any(a&b==0 for a,b in combinations(E,2)):continue
 f=tuple(fn(E,x) for x in range(32));assert all(f[31-x]==-f[x] for x in range(32))
 assert all(f[x]<=f[x|(1<<i)] for x in range(32) for i in range(5))
 w=spectrum(f);assert w in expected;assert sum(w)==1024
 counts[w]+=1;functions.add(f)
for i in range(5):
 f=tuple(1 if x>>i&1 else -1 for x in range(32));w=spectrum(f)
 assert w==(0,1024,0,0,0,0);counts[w]+=1;functions.add(f)
assert len(functions)==81
# Independent exhaustive truth-table enumeration over antipodal assignments.
found=set()
for m in range(1<<16):
 f=tuple(1 if m>>x&1 else -1 for x in range(16))
 f=f+tuple(-v for v in reversed(f))
 if all(f[x]<=f[x|(1<<i)] for x in range(32) for i in range(5)):found.add(f)
assert found==functions
# Partition formula versus direct DSBS probabilities for a tie-free threshold.
weights=[2,2,1,1,1];f=tuple(1 if sum(weights[i]*(1 if x>>i&1 else -1) for i in range(5))>0 else -1 for x in range(32))
W=spectrum(f)
checks=[]
for r in [Fraction(1,10),Fraction(1,2),Fraction(9,10)]:
 q=(1-r)/2
 direct=sum(Fraction(f[x]*f[y],32)*q**((x^y).bit_count())*(1-q)**(5-(x^y).bit_count()) for x in range(32) for y in range(32))
 prob=Fraction(0)
 for j in range(32):
  disagree=0
  for x in range(32):
   u=sum(weights[i]*(1 if x>>i&1 else -1) for i in range(5) if not j>>i&1)
   v=sum(weights[i]*(1 if x>>i&1 else -1) for i in range(5) if j>>i&1)
   assert abs(u)!=abs(v)
   disagree+=abs(v)>abs(u)
  prob+=q**j.bit_count()*(1-q)**(5-j.bit_count())*Fraction(disagree,32)
 fourier=sum(Fraction(W[k],1024)*r**k for k in range(6))
 assert direct==fourier==1-2*prob
 checks.append(dict(rho=str(r),stability=str(direct)))
result=dict(function_count=len(functions),spectra_counts={str(k):v for k,v in counts.items()},partition_checks=checks,all_checks='PASS')
Path=__import__('pathlib').Path
Path('exact_check.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
