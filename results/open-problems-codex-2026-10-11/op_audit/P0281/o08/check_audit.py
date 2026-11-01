from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from math import factorial, prod
from collections import defaultdict
from pathlib import Path
import json
import mpmath as mp

def arrays(n,cap):
 def lower(row):
  if len(row)==1: yield (row,); return
  for small in product(*(range(row[i+1],row[i]+1) for i in range(len(row)-1))):
   for rest in lower(small):yield rest+(row,)
 for top in combinations_with_replacement(range(cap+1),n):yield from lower(tuple(reversed(top)))
def coeff(rows):
 n=len(rows); ell=[v+n-i-1 for i,v in enumerate(rows[-1])]
 return F(prod(ell[i]-ell[j] for i in range(n) for j in range(i+1,n)),prod(factorial(v) for v in ell))
def jump(rows,m,i):
 # lambda_i^m clock (zero-based): blocked by upper coordinate of shorter row.
 if i>0 and rows[m][i]==rows[m-1][i-1]:return None
 b=[list(r) for r in rows]; old=b[m][i]; b[m][i]+=1
 # Pushing follows equal lambda at the same i on successively longer rows.
 for k in range(m+1,len(rows)):
  if b[k][i]!=old:break
  b[k][i]+=1
 return tuple(tuple(r) for r in b)
out={}
for n,cap in [(1,8),(2,7),(3,4),(4,2),(5,1)]:
 aa=list(arrays(n,cap)); weights={a:coeff(a) for a in aa}
 incoming0=defaultdict(F); incoming1=defaultdict(F); exits={}
 for a in aa:
  q=0; s=sum(a[-1])
  for m in range(n):
   for i in range(m+1):
    b=jump(a,m,i)
    if b is None:continue
    q+=1
    if b in weights:
     ds=sum(b[-1])-s
     assert ds in (0,1)
     (incoming0 if ds==0 else incoming1)[b]+=weights[a]
  exits[a]=q
 for a,c in weights.items():
  assert incoming0[a]==(exits[a]-n)*c,(a,'same-degree')
  assert incoming1[a]==sum(a[-1])*c,(a,'previous-degree')
 pairs=0
 for ix,a in enumerate(aa):
  for b in aa[ix:]:
   r=tuple(tuple((x+y)//2 for x,y in zip(ar,br)) for ar,br in zip(a,b))
   s=tuple(tuple((x+y+1)//2 for x,y in zip(ar,br)) for ar,br in zip(a,b))
   assert r in weights and s in weights
   assert weights[a]*weights[b]<=weights[r]*weights[s]
   pairs+=1
 out[str(n)]={'cap':cap,'arrays':len(aa),'exact_midpoint_pairs':pairs,'generator_polynomial_identities':'all passed'}

# Independent TASEP uniformization, without using the multilevel generator.
mp.mp.dps=65
n=3; t=mp.mpf('0.5'); terms=130
v={(0,0,0):mp.mpf(1)}; probs=defaultdict(mp.mpf)
poisson=mp.exp(-n*t)
targets=[(0,0,0),(1,0,0),(1,1,0),(1,1,1),(4,2,1),(6,3,0)]
for k in range(terms+1):
 for d in targets:probs[d]+=poisson*v.get(d,0)
 if k==terms:break
 nv=defaultdict(mp.mpf)
 for d,z in v.items():
  moves=[i for i in range(n) if i==0 or d[i]<d[i-1]]
  # Bounding d1 at 26 cannot affect retained targets, since coordinates never decrease.
  nv[d]+=z*(n-len(moves))/n
  for i in moves:
   e=list(d); e[i]+=1; e=tuple(e)
   if e[0]<=26:nv[e]+=z/n
 v=nv; poisson*=n*t/(k+1)
checks=[]
for d in targets:
 # n=3: rows (a), (b,c), (u,v,w), diagonal d=(a,c,w).
 a,c,w=d; val=mp.mpf(0)
 for u in range(a,41):
  for vv in range(w,u+1):
   if not vv>=c>=w:continue
   multiplicity=max(0,u-max(vv,a,c)+1) if a>=c else 0
   # b ranges [max(v,a),u], with a>=c; no other hidden variables.
   if multiplicity:
    ell=[u+2,vv+1,w]
    val+=multiplicity*t**(u+vv+w)*prod(ell[i]-ell[j] for i in range(3) for j in range(i+1,3))/prod(mp.factorial(z) for z in ell)
 val*=mp.exp(-3*t)
 err=abs(val-probs[d])/probs[d]
 assert err<mp.mpf('1e-38'),(d,err)
 checks.append({'state':d,'probability':mp.nstr(probs[d],25),'array_relative_error':mp.nstr(err,8)})
out['representation_checks']=checks
Path('check_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
