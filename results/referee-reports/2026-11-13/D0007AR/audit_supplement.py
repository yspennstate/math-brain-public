"""Refinements and exact positive controls for the independent referee run."""
import json
import math
import resource
import time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from independent_checks import Law, rearrange
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, eye, hstack, vstack

start=time.monotonic()
quad=Law('quadratic',[],[],.5,.1,.5)
rows=[]
for B in (80,160):
    # Exhaustive sorted triples, exploiting the four possible integer sums.
    target=1.5*B
    row_index=[]; col_index=[]; entries=[]; k=0
    for i in range(B):
        for j in range(i,B):
            lower=max(j,math.ceil(target-3-i-j))
            upper=min(B-1,math.floor(target-i-j))
            for t in range(lower,upper+1):
                row_index.extend((i,j,t));col_index.extend((k,k,k));entries.extend((1/3,)*3)
                k+=1
    C=coo_matrix((entries,(row_index,col_index)),shape=(B,k)).tocsc()
    A=vstack((hstack((C,eye(B),-eye(B))),
              hstack((coo_matrix(np.ones((1,k))),coo_matrix((1,2*B)))))).tocsc()
    p=quad.cells(B)[2]
    rhs=np.r_[p,1]
    fit=linprog(np.r_[np.zeros(k),np.ones(2*B)],A_eq=A,b_eq=rhs,bounds=(0,None),
                method='highs-ipm',options={'threads':1,'time_limit':60.,'primal_feasibility_tolerance':1e-9,
                                           'dual_feasibility_tolerance':1e-9})
    assert fit.success
    dual_lower=float(rhs@fit.eqlin.marginals)
    residual=float(np.max(abs(A@fit.x-rhs)))
    assert abs(dual_lower-fit.fun)<1e-7 and residual<1e-7
    record={'law':quad.name,'n':3,'B':B,'columns':k,'lp':'excluded',
            'lp_l1':float(fit.fun),'lp_lower':dual_lower,'primal_residual':residual,
            'pricing':'all admissible sorted triples enumerated'}
    rows.append(record)
    print(json.dumps(record),flush=True)

controls=[]
for n,a,b in [(20,0.,1.),(40,0.,1.),(20,.9,1.)]:
    M=4000; group=M//n; A=np.zeros((M,n))
    low=a+(b-a)*(np.arange(group)+.5)/(2*group)
    for j in range(n):
        A[j*group:(j+1)*group,j]=low
        A[j*group:(j+1)*group,(j+1)%n]=a+b-low
    expected=np.r_[np.zeros(M-2*group),a+(b-a)*(np.arange(2*group)+.5)/(2*group)]
    error=float(np.max(np.abs(A.sum(axis=1)-(a+b))))
    marginal_error=max(float(np.max(abs(np.sort(A[:,j])-expected))) for j in range(n))
    assert error<1e-14 and marginal_error<1e-14
    controls.append({'n':n,'positive_uniform':[a,b],'rows':M,
                     'max_sum_error':error,'max_quantile_marginal_error':marginal_error})

# Exact pair splitting in Lemma 8, on F=(delta_0+2delta_1+delta_2)/4.
p={0:Q(1,4),1:Q(1,2),2:Q(1,4)}
conv={s:sum((p[u]*p[v] for u in p for v in p if u+v==s),Q(0)) for s in range(5)}
recovered=[{u:Q(0) for u in p} for _ in range(4)]
for s,prob in conv.items():
    for u,v in __import__('itertools').product(p,repeat=2):
        if u+v!=s:continue
        for w,z in __import__('itertools').product(p,repeat=2):
            if w+z!=4-s:continue
            weight=prob*(p[u]*p[v]/conv[s])*(p[w]*p[z]/conv[4-s])
            assert u+v+w+z==4
            for j,x in enumerate((u,v,w,z)):recovered[j][x]+=weight
assert all(m==p for m in recovered)

edge_cases=[]
for law,n,M in [(Law('atom_uniform_01',[(0,.9)],[(0,1,.1)],.05,.1,.5),131,4000),
                (Law('atom_uniform_007',[(0,.93)],[(0,1,.07)],.035,.07,.5),186,4000),
                (Law('far_uniform',[(0,.9)],[(.9,1,.1)],.095,.1,.05),1211,1000)]:
    edge_cases.append({'law':law.name,'n':n,'theorem2_N':law.bound,
                       **rearrange(law,n,M=M,sweeps=12,restarts=1)})

exact={'quadratic_middle_mass':str(Q(1,10)*Q(1,2)+Q(27,10)*Q(1,24)),
       'quadratic3_min_L1_from_middle_obstruction':str(2*(Q(1,3)-Q(13,80))),
       'yin_N_for_alpha1_half':math.ceil(776*math.pi*math.sqrt(3)),
       'pair_disintegration_four_marginals_exact':'passed'}
assert exact['quadratic_middle_mass']=='13/80'
out={'lp_refinements':rows,'structured_quantile_controls':controls,'edge_rearrangements':edge_cases,'exact':exact,
     'seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('supplement_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out),flush=True)
