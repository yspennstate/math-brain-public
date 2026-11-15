"""Independent sanity checks for the analytic statements, not their proofs."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,math
from pathlib import Path
import numpy as np,networkx as nx,sympy as sp
from search import gap
ROOT=Path(__file__).resolve().parents[1]
cycle_checks=0
for n in range(4,65,2):
 a=nx.to_numpy_array(nx.cycle_graph(n));base=1-math.cos(2*math.pi/n)
 for j in range(2,n//2+1):
  value=gap(a,[(0,j)])
  if j==n//2:assert abs(value-base)<1e-12
  else:assert value<base-1e-12
  cycle_checks+=1
 ant=[(i,i+n//2) for i in range(n//2)]
 assert abs(gap(a,ant)-(2-2*math.cos(4*math.pi/n))/3)<1e-12
for m in [4,6,8]:
 g=nx.complete_bipartite_graph(m,m);a=nx.to_numpy_array(g);extra=[(i,i+1) for i in range(0,2*m,2)];assert abs(gap(a,extra)-m/(m+1))<1e-12
for n in [4,6,8,10]:
 a=nx.to_numpy_array(nx.complete_graph(n));extra=[(i,i+1) for i in range(0,n,2)]
 for i,j in extra:a[i,j]=a[j,i]=0
 assert abs(gap(a)-1)<1e-12;assert abs(gap(a,extra)-n/(n-1))<1e-12
# Exact arithmetic re-derivation of the K_3,3 quotient and remaining subspaces.
x=sp.symbols('x');Q=sp.Matrix([[sp.Rational(1,4),0,sp.Rational(3,4)],[0,0,1],[sp.Rational(2,3),sp.Rational(1,3),0]])
assert sp.factor(Q.charpoly(x).as_expr())==(x-1)*(12*x*x+9*x-1)/12
assert abs(gap(nx.to_numpy_array(nx.complete_bipartite_graph(3,3)),[(0,1)])-(33-math.sqrt(129))/24)<1e-12
# Check first and second derivatives against increasingly local finite differences.
r=next(z for z in map(json.loads,(ROOT/'data/search_d3_n10.jsonl').open()) if z['id']==9);a=nx.to_numpy_array(nx.from_graph6_bytes(r['g6'].encode()));d=3;L=d*np.eye(10)-a;w,v=np.linalg.eigh(L);mu=w[1]/d;f=v[:,1];u,z=0,2;b=np.eye(10)[:,u]-np.eye(10)[:,z];B=np.outer(b,b);C=np.diag([int(i in [u,z]) for i in range(10)]);W=np.einsum('ij,jk,kl->il',v.T,B-mu*C,v,optimize=False)/d
first=W[1,1];second=2*sum(W[j,1]**2/(mu-w[j]/d) for j in range(10) if j!=1)-2*first*sum(f[i]**2 for i in [u,z])/d
errs=[]
for h in [0.01,0.005,0.0025]:
 def val(t):
  deg=d+t*np.diag(C);return np.linalg.eigvalsh((L+t*B)/np.sqrt(deg[:,None]*deg[None,:]))[1]
 p,m=val(h),val(-h);errs.append([h,abs((p-m)/(2*h)-first),abs((p-2*mu+m)/(h*h)-second)])
assert errs[-1][1]<errs[0][1]/8 and errs[-1][2]<errs[0][2]/8
out={'cycle_chord_checks':cycle_checks,'cycle_antipodal_matching_sizes_checked':31,'matching_bound_equality_examples':7,'K33_exact_quotient':'(x-1)*(12*x*x+9*x-1)/12','derivative_first':float(first),'derivative_second':float(second),'finite_difference_errors':errs}
(ROOT/'data/proof_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
