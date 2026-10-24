import itertools,json,time,pathlib
import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(66); started=time.monotonic(); results=[]
def model(m):
 pairs=list(itertools.combinations_with_replacement(range(m),2)); n=len(pairs)*m
 def row_at(x,k):
  a=np.zeros(n)
  for q,(i,j) in enumerate(pairs): a[q*m+k]=x[i]*x[j]*(1 if i==j else 2)
  return a
 eq=[]; rhs=[]
 for q in range(len(pairs)):
  a=np.zeros(n);a[q*m:(q+1)*m]=1;eq.append(a);rhs.append(1.)
 ub=[];br=[]
 for bits in range(1,1<<m):
  I={i for i in range(m) if bits>>i&1}
  for k in range(m):
   a=np.zeros(n)
   for q,(i,j) in enumerate(pairs):
    if i in I and j in I:a[q*m+k]=1 if i==j else 2
   ub.append(a);br.append(len(I))
 return pairs,n,row_at,eq,rhs,np.array(ub),np.array(br)
# Hostile test: fixing a distinct-positive boundary point must force identity on its face.
for m in range(2,7):
 pairs,n,row,eq,rhs,ub,br=model(m)
 for r in range(1,m+1):
  x=np.zeros(m);x[:r]=np.arange(1,r+1);x/=x.sum()
  A=eq+[row(x,k) for k in range(m)]; b=rhs+list(x)
  for trial in range(3):
   sol=linprog(rng.normal(size=n),A_ub=ub,b_ub=br,A_eq=A,b_eq=b,bounds=(0,1),method='highs',options={'time_limit':5})
   if not sol.success:raise RuntimeError((m,r,sol.message))
   err=max(abs(sol.x[q*m+k]-((i==k)+(j==k))/2) for q,(i,j) in enumerate(pairs) if i<r and j<r for k in range(m))
   results.append({'kind':'face_rigidity','m':m,'support':r,'max_error':float(err)})
# Bounded exploratory search: repeated values in four types, cycles longer than order bound 4.
m=4;pairs,n,row,eq,rhs,ub,br=model(m)
base=[.4,.4,.15,.05]; perms=np.array(sorted(set(itertools.permutations(base))))
for period in [5,6]:
 for trial in range(24):
  if time.monotonic()-started>150:break
  ids=np.r_[0,rng.choice(np.arange(1,len(perms)),period-1,replace=False)]; cycle=perms[ids]
  A=list(eq);b=list(rhs)
  for t in range(period):
   for k in range(m):A.append(row(cycle[t],k));b.append(cycle[(t+1)%period,k])
  sol=linprog(np.zeros(n),A_ub=ub,b_ub=br,A_eq=A,b_eq=b,bounds=(0,1),method='highs',options={'time_limit':5})
  item={'kind':'repeated_cycle_search','period':period,'trial':trial,'status':int(sol.status),'message':sol.message}
  results.append(item)
  if sol.success:
   pathlib.Path('candidate_cycle.json').write_text(json.dumps({'cycle':cycle.tolist(),'coefficients':sol.x.tolist(),'pairs':pairs}),encoding='utf8')
# Exact rational sanity controls, independent of LP tolerances.
from fractions import Fraction as F
x=(F(1,2),F(1,3),F(1,6));cycle=[x,(x[2],x[0],x[1]),(x[1],x[2],x[0])]
assert len(set(cycle))==3
assert 2*F(0)*(1-F(0))==0
assert 2*F(1)*(1-F(1))==0
summary={'seconds':time.monotonic()-started,'face_tests':sum(a['kind']=='face_rigidity' for a in results),'max_face_error':max(a['max_error'] for a in results if a['kind']=='face_rigidity'),'repeated_cycle_counts':{str(s):sum(a['kind']=='repeated_cycle_search' and a['status']==s for a in results) for s in range(5)},'exact_controls':'3-cycle distinct; logistic endpoints verified'}
pathlib.Path('experiments.json').write_text(json.dumps({'summary':summary,'results':results},indent=2),encoding='utf8');print(summary)
