from pathlib import Path
import json,itertools,time
import numpy as np
from scipy.optimize import linprog
prefix=Path('experiments.py').read_text(encoding='utf-8-sig').split('# Hostile test:')[0];exec(prefix)
rng=np.random.default_rng(6606);records=[]
for m in range(3,7):
 pairs,n,row,eq,rhs,ub,br=model(m)
 x=np.arange(1,m+1,dtype=float);x[:2]=2.;x/=x.sum();c=np.ones(m)/m;d=x-c
 for trial in range(12):
  y=x[rng.permutation(m)]
  sol=linprog(rng.normal(size=n),A_ub=ub,b_ub=br,A_eq=eq+[row(x,k) for k in range(m)],b_eq=rhs+list(y),bounds=(0,1),method='highs',options={'time_limit':3})
  assert sol.success,sol.message
  coeff=np.zeros((m,m,m))
  for z,(i,j) in enumerate(pairs):coeff[i,j,:]=coeff[j,i,:]=sol.x[z*m:(z+1)*m]
  B=2/m*coeff.sum(axis=1).T-np.ones((m,m))/m
  Q=np.einsum('ijk,i,j->k',coeff,d,d)
  records.append({'m':m,'trial':trial,'Q_norm':float(np.linalg.norm(Q)),'Bx_error':float(np.max(np.abs(B@x-y))),'B_min':float(B.min()),'row_error':float(np.max(np.abs(B.sum(axis=1)-1))),'column_error':float(np.max(np.abs(B.sum(axis=0)-1)))})
# Exact symbolic boundary control and an interior repeated-coordinate 2-cycle.
import sympy as s
z=s.symbols('z');f=lambda t:2*t*(1-t)
assert s.expand(f(s.Rational(1,2)+z)-s.Rational(1,2))==-2*z*z
D=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0,0],[s.Rational(1,2),s.Rational(1,2),0,0],[0,0,0,1],[0,0,1,0]])
x=s.Matrix([s.Rational(3,10),s.Rational(3,10),s.Rational(1,10),s.Rational(3,10)])
assert D*D*x==x and D*x!=x
# Floating boundary exploration of the residual gap, bounded samples only.
m=4;pairs,n,row,eq,rhs,ub,br=model(m);vs=np.array(sorted(set(itertools.permutations([.4,.4,.2,0.]))));boundary=[]
for period in [5,6,7]:
 for trial in range(80):
  ids=np.r_[0,rng.choice(np.arange(1,len(vs)),period-1,replace=False)];cyc=vs[ids];A=list(eq);b=list(rhs)
  for t in range(period):
   for k in range(m):A.append(row(cyc[t],k));b.append(cyc[(t+1)%period,k])
  sol=linprog(np.zeros(n),A_ub=ub,b_ub=br,A_eq=A,b_eq=b,bounds=(0,1),method='highs',options={'time_limit':3})
  boundary.append({'period':period,'trial':trial,'status':int(sol.status)})
  if sol.success:Path('residual_candidate.json').write_text(json.dumps({'cycle':cyc.tolist(),'pairs':pairs,'coefficients':sol.x.tolist()}),encoding='utf8')
summary={'interior_tests':len(records),'max_Q_norm':max(r['Q_norm'] for r in records),'max_Bx_error':max(r['Bx_error'] for r in records),'min_B_entry':min(r['B_min'] for r in records),'max_stochastic_error':max(max(r['row_error'],r['column_error']) for r in records),'residual_cases':len(boundary),'residual_statuses':{str(st):sum(b['status']==st for b in boundary) for st in range(5)}}
Path('radial_followup_checks.json').write_text(json.dumps({'summary':summary,'interior':records,'boundary':boundary},indent=2),encoding='utf8');print(summary)
