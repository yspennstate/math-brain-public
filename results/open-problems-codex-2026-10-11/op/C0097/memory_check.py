"""Exact finite-memory orbit transfer matrices. No floating point or SAW extrapolation."""
import json, time
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parent
def canonical(w):
 labels={}; out=[]
 for a in w:
  k=abs(a)
  if k not in labels: labels[k]=(len(labels)+1)*(1 if a>0 else -1)
  out.append(labels[k]*(1 if a>0 else -1))
 return tuple(out)
def valid(w):
 p=[0]*(max(map(abs,w),default=0)); seen={tuple(p)}
 for a in w:
  p[abs(a)-1]+=1 if a>0 else -1
  if tuple(p) in seen:return False
  seen.add(tuple(p))
 return True
def states(tau):
 words={()}
 for _ in range(tau):
  out=set()
  for w in words:
   k=max(map(abs,w),default=0)
   for a in list(range(1,k+1))+list(range(-k,0))+[k+1]:
    if valid(w+(a,)):out.add(canonical(w+(a,)))
  words=out
 return sorted(words)
results=[]
for tau in range(1,7):
 ws=states(tau); ix={w:i for i,w in enumerate(ws)}; successors=[]; B=[]
 for w in ws:
  k=max(map(abs,w)); target=ix[canonical((w+(k+1,))[-tau:])]; successors.append(target)
  row={target:-2*k}
  for a in list(range(1,k+1))+list(range(-k,0)):
   z=(w+(a,))[-tau:]
   if valid(z):
    j=ix[canonical(z)];row[j]=row.get(j,0)+1
  B.append(row)
 destinations=[]
 for i in range(len(ws)):
  j=i
  for _ in range(tau):j=successors[j]
  destinations.append(j)
 assert len(set(destinations))==1
 fixed=destinations[0];assert successors[fixed]==fixed
 assert ws[fixed]==tuple(range(1,tau+1))
 result={'memory':tau,'states':len(ws),'fresh_reset_checked':True}
 if tau<=4:
  x,l=S.symbols('x l'); T=S.zeros(len(ws))
  for i,j in enumerate(successors):T[i,j]+=1
  for i,row in enumerate(B):
   for j,b in row.items():T[i,j]+=x*b
  poly=S.factor(T.charpoly(l).as_expr());result['characteristic_polynomial']=str(poly)
  # factor containing the branch l=1 at x=0
  factors=S.factor_list(poly)[1]
  factor=next(f for f,m in factors if f.subs({l:1,x:0})==0)
  branch=1
  for n in range(1,8):
   a=S.Symbol('a'); expr=S.expand(factor.subs(l,branch+a*x**n)).coeff(x,n)
   sol=S.solve(expr,a)[0];branch+=sol*x**n
  result['normalized_connective_constant_series']=str(branch)
  if tau==1:assert S.expand(branch-1)==0
  if tau in (2,3):assert S.expand(branch-(1-x))==0
 results.append(result);print(result,flush=True)
(P/'memory_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
# The paired-axis return class; not the connective constant.
x=S.Symbol('x'); q=0; pair=1;fall=1;paired=[]
for n in range(1,21):
 pair*=2*n-1;q+=pair*x**n*fall
 coeff=int(S.expand(q).coeff(x,n));paired.append({'order':n,'paired_axis_series_coefficient':coeff,'uncancelled_diagonal':pair})
 fall=S.expand(fall*(1-2*n*x))
(P/'paired_return_results.json').write_text(json.dumps(paired,indent=2),encoding='utf-8')
