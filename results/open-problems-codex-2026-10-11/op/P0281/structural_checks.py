from pathlib import Path
import itertools,math,json
from fractions import Fraction
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import expm_multiply

def row_patterns(top):
 if len(top)==1:yield (top,);return
 for lower in itertools.product(*(range(top[i+1],top[i]+1) for i in range(len(top)-1))):
  for pat in row_patterns(lower):yield pat+(top,)
def wt(pat):
 top=pat[-1];n=len(top);l=[a+n-i-1 for i,a in enumerate(top)];return Fraction(math.prod(l[i]-l[j] for i in range(n) for j in range(i+1,n)),math.prod(math.factorial(x) for x in l))
checks=[]
for n,M in [(2,6),(3,3),(4,2)]:
 pats=[p for s in itertools.combinations_with_replacement(range(M+1),n) for p in row_patterns(tuple(reversed(s)))];weights={tuple(x for r in p for x in r):wt(p) for p in pats};keys=list(weights);count=0
 for a,b in itertools.combinations_with_replacement(keys,2):
  lo=tuple((x+y)//2 for x,y in zip(a,b));hi=tuple((x+y+1)//2 for x,y in zip(a,b));assert lo in weights and hi in weights
  assert weights[a]*weights[b]<=weights[lo]*weights[hi],(a,b)
  count+=1
 r={'n':n,'cap':M,'arrays':len(pats),'exact_pair_checks':count};checks.append(r);print(r,flush=True)
# Independent n=3 edge distribution, summing all arrays through top lambda_1<=20.
t=.5;M=20;edge={}
for a in range(M+1):
 for b in range(a+1):
  for c in range(b+1):
   w=math.exp(-3*t)*t**(a+b+c)*(a-b+1)*(a-c+2)*(b-c+1)/(math.factorial(a+2)*math.factorial(b+1)*math.factorial(c))
   for v in range(c,b+1):
    for u in range(v,a+1):edge[u,v,c]=edge.get((u,v,c),0.)+w*(a-max(u,b)+1)
states=list(edge);idx={x:i for i,x in enumerate(states)};rows=[];cols=[];data=[]
for x,j in idx.items():
 rate=0
 for k in range(3):
  if k==0 or x[k]<x[k-1]:
   rate+=1;y=list(x);y[k]+=1
   if tuple(y) in idx:rows.append(idx[tuple(y)]);cols.append(j);data.append(1.)
 rows.append(j);cols.append(j);data.append(-rate)
Q=csc_matrix((data,(rows,cols)),shape=(len(idx),len(idx)));v=np.zeros(len(idx));v[idx[(0,0,0)]]=1;p=expm_multiply(t*Q,v)
errs=[abs(edge[x]-p[i])/p[i] for x,i in idx.items() if p[i]>1e-12 and x[0]<=6]
r={'n':3,'t':t,'array_top_cap':M,'compared_states':len(errs),'max_relative_error':max(errs),'array_total_mass':sum(edge.values())};checks.append(r);print(r,flush=True);Path('structural_checks.json').write_text(json.dumps(checks,indent=2))
