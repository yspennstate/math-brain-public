"""Finite supporting checks, not a proof of QFORM or an independent review."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, gamma
import sympy as sp

out = {"scope":"Finite exact algebra, quadrature, and matrix examples only; full conjecture not certified", "checks":{}}
m, a = sp.symbols('m a', positive=True)
D,k,H,s = sp.symbols('D k H s', positive=True)
r = (D*k)**sp.Rational(1,4)/sp.sqrt(H)
expr=2*sp.sqrt(2)/r + 2*sp.sqrt(2)*H*r/sp.sqrt(D*k)
assert sp.simplify(expr-4*sp.sqrt(2*H)/(D*k)**sp.Rational(1,4))==0
assert sp.simplify((4*sp.sqrt(2*H)/(D*k)**sp.Rational(1,4)).subs(H,10/sp.sqrt(s))-8*sp.sqrt(5)/(D*k*s)**sp.Rational(1,4))==0
out['checks']['optimization']='PASS'
out['checks']['explicit_pair_constant']=float(4*(2*np.sqrt(2)+2+np.log(50)))
assert out['checks']['explicit_pair_constant'] <35
# Cone shell normalization and distribution coefficient are exact identities.
delta=sp.symbols('delta', positive=True)
R=1/(2*sp.pi*delta)
assert sp.simplify(2*R*sp.pi*delta)==1
assert sp.simplify(2*R*sp.pi-1/delta)==0
out['checks']['cone_shell']='PASS: exact volume one, output density 1/delta'
# Conditional cube moment, with an independent one-dimensional quadrature.
rows=[]
for n in (2,3,4,8,16,32,64,128,1024):
    logj=(2/3)*np.log(n)+gammaln(n)+gammaln(4/3)-gammaln(n+1/3)
    moment=float(np.exp(3*logj))
    if n<=128:
        jquad=n**(2/3)*(n-1)*quad(lambda z:z**(n-2)*(1-z)**(1/3),0,1,epsabs=1e-11,epsrel=1e-11)[0]
        assert abs(jquad-np.exp(logj))<1e-8
    rows.append({'m':n,'conditional_two_thirds_moment':moment,'moment_over_m':moment/n})
assert abs(rows[0]['conditional_two_thirds_moment']-27/16)<1e-12
out['checks']['cube_moments']=rows
out['checks']['asymptotic_slope']=float(gamma(4/3)**3)
# Spectral frame / pair Schur complement checks.
rng=np.random.default_rng(20260922)
cases=0; rank_errors=[]; gap_ratios=[]
for n in (4,7,12,23):
    for _ in range(20):
        V,_=np.linalg.qr(rng.normal(size=(n,3)))
        eig=np.array([1+rng.random()*3,1+rng.random()*3,-1-rng.random()*3])
        A=V@np.diag(eig)@V.T
        B=A[:2,:2]
        if np.linalg.det(B)>=-1e-9: continue
        C=A[2:,2:]; E=A[:2,2:]
        S=C-E.T@np.linalg.solve(B,E)
        vals=np.linalg.eigvalsh(S)
        order=np.argsort(np.abs(vals)); lam=vals[order[-1]]
        err=float(np.linalg.norm(vals[order[:-1]]))
        assert err<1e-7
        assert abs(lam)+1e-8>=min(abs(eig))
        rank_errors.append(err);gap_ratios.append(float(abs(lam)/min(abs(eig))))
        cases+=1
out['checks']['schur']={'cases':cases,'max_numerical_rank_one_residual':max(rank_errors),'min_abs_schur_eigenvalue_over_spectral_gap':min(gap_ratios)}
# A fully coupled pair-zero-diagonal constructed family; Schur is exactly hh^T.
n=12;h=rng.normal(size=n);h/=np.linalg.norm(h)
B=np.array([[0.,1.],[1.,0.]])
E=rng.normal(size=(2,n))
C=E.T@B@E+np.outer(h,h)
assert np.linalg.norm(C-E.T@np.linalg.solve(B,E)-np.outer(h,h))<1e-12
out['checks']['zero_scalar_pair']='PASS: arbitrary cross couplings with rank-one Schur remainder'
out['status']='PASS'
Path(__file__).with_name('check_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
