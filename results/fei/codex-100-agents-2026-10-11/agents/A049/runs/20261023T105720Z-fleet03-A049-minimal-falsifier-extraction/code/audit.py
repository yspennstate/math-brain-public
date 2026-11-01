"""Separate small-cube classification and derivative-factor arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import itertools,json
RUN=Path(__file__).resolve().parents[1]
def fwht(t):
 a=list(t);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for j in range(base,base+step):
    x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
  step*=2
 return a
def child(t,j,b):
 n=(len(t).bit_length()-1)
 return tuple(t[sum(((x>>k)&1)<<(k+(k>=j)) for k in range(n-1))+(b<<j)] for x in range(1<<(n-1)))
rows=[];essential_queries=0
for n in range(3):
 for t in itertools.product((-1,1),repeat=1<<n):
  a=fwht(t);kind='exact_character' if sum(x!=0 for x in a)==1 else 'point_defect'
  if kind=='point_defect':assert n==2 and min(t.count(1),t.count(-1))==1
  for j in range(n):
   if child(t,j,0)==child(t,j,1):continue
   essential_queries+=1
   if kind=='point_defect':
    for b in (0,1):assert sum(x!=0 for x in fwht(child(t,j,b)))==1
  rows.append({'n':n,'truth_table':t,'classification':kind})
g=(1,-1,-1,1,-1,1,1,1)
assert fwht(g)==[2,-2,-2,2,-2,2,2,6]
assert set(fwht(child(g,0,0)))=={0,4}
assert all(abs(x)==2 for x in fwht(child(g,0,1)))
# Integer polynomial operations independently verify the first-four-term
# derivative numerator. Coefficients are ordered from constant upward.
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
denoms=[[2,1],[1,2],[26,-1],[10,-1]];weights=[10,-4,-13,-5]
N=[0]*4
for j,w in enumerate(weights):
 p=[w]
 for k,d in enumerate(denoms):
  if k!=j:p=mul(p,d)
 for k,v in enumerate(p):N[k]+=v
# Equivalently a[(11-2a)(26-a)(10-a)
#                 - (18-a)(2+a)(1+2a)].
rhs1=mul(mul([11,-2],[26,-1]),[10,-1])
rhs2=mul(mul([18,-1],[2,1]),[1,2])
rhs=[0]+[x-y for x,y in zip(rhs1,rhs2)]
while rhs and rhs[-1]==0:rhs.pop()
nn=N.copy()
while nn and nn[-1]==0:nn.pop()
assert nn==rhs
# Universal bounds used in the proof are exact factor identities.
assert mul([1,-1],[9,2])==[9,-7,-2]
assert F(1,2)*(F(1,25)+F(1,9))==F(17,225)
assert 1-F(17,225)==F(208,225)
assert F(208,225)/64==F(13,900)
out={'status':'PASS','all_truth_tables_n_le_2':len(rows),'essential_queries':essential_queries,'classification':rows,'derivative_numerator':N,'all_alpha_minimality':'Any nonexact core on <=2 bits restricts to exact spectra at every essential query; fresh activation children are therefore exact too. Exact-parent cases transport exactly. No positive reset is possible for any0<alpha<1.','independence':'Different implementation by same agent; not external review.'}
(RUN/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','all_truth_tables_n_le_2','essential_queries','derivative_numerator']}))
