"""Finite checks for the arbitrary-rank pair extension; not a universal proof."""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp
from scipy.special import gamma

D,k,s=sp.symbols('D k s', positive=True)
A1=2*sp.sqrt(2)
B1=20*2**sp.Rational(1,4)/sp.sqrt(D)/k**sp.Rational(1,4)/s**sp.Rational(1,4)
r=(2*A1/B1)**sp.Rational(2,3)
expected=3*400**sp.Rational(1,3)/(D**2*k*s)**sp.Rational(1,6)
assert sp.simplify(A1/r+B1*sp.sqrt(r)-expected)==0
smallball_constant=2**(3/8)*math.pi**(-1/4)*math.exp(3/8)*gamma(3/8)
elementary_bound=73/15
assert smallball_constant<elementary_bound<5
localized_constant=4*(2*math.sqrt(2)+4+math.log(625/2))
assert localized_constant<51
rng=np.random.default_rng(2026092218)
ratios=[]; rank_errors=[]
for n in [4,7,12,25]:
    for j in range(30):
        Q,_=np.linalg.qr(rng.normal(size=(n,n)))
        eig=rng.uniform(-4,4,size=n)
        A=Q@np.diag(eig)@Q.T
        B=A[:2,:2]
        if np.linalg.det(B)>=-1e-8: continue
        E=A[:2,2:]; C=A[2:,2:]
        S=C-E.T@np.linalg.solve(B,E)
        A0=A.copy(); A0[2:,2:]=E.T@np.linalg.solve(B,E)
        rank_errors.append(float(np.linalg.svd(A0,compute_uv=False)[2]))
        s3=sorted(np.abs(eig),reverse=True)[2]
        ratios.append(float(np.linalg.norm(S,ord=2)/s3))
        assert ratios[-1]>=1-1e-8
        assert rank_errors[-1]<1e-7
# Exhaustive coordinate cuts in several finite zero-diagonal examples.
cut_ratios=[]
for n in [3,4,6,8]:
    T=rng.normal(size=(n,n));T=(T+T.T)/2;np.fill_diagonal(T,0)
    best=0
    for mask in range(1,2**(n-1)):
        I=[i for i in range(n) if mask>>i&1]
        J=[i for i in range(n) if not(mask>>i&1)]
        best=max(best,float(np.linalg.norm(T[np.ix_(I,J)],ord=2)))
    cut_ratios.append(best/np.linalg.norm(T,ord=2))
    assert cut_ratios[-1]>=.5-1e-12
out={
 'status':'PASS',
 'scope':'Finite symbolic, scalar and matrix checks; not an independent or full-conjecture proof',
 'pair_optimization':'PASS',
 'quarter_smallball_exact_prefactor':smallball_constant,
 'elementary_prefactor_bound':elementary_bound,
 'full_pair_prefactor':float(3*400**(1/3)),
 'localized_full_rank_constant':localized_constant,
 'rank_two_approximation_cases':len(ratios),
 'min_schur_norm_over_third_singular_value':min(ratios),
 'max_numerical_third_singular_value_rank_two_approximation':max(rank_errors),
 'cut_norm_ratios':cut_ratios
}
Path(__file__).with_name('full_matrix_check_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
