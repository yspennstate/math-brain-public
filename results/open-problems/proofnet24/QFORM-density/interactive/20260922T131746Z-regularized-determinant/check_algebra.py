"""Finite checks for the QFORM regularized-determinant supporting argument.

These checks verify scalar algebra, matrix identities, and Gaussian/uniform
examples. They are not a verification of the universal analytic theorem.
Requires Python 3.10+, numpy, scipy, sympy.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
from typing import Any
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import gammaln

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(22131746)
results: dict[str, Any] = {"scope": "finite algebra and example checks; not a universal proof", "checks": {}}

c, q = sp.symbols("c q", positive=True)
p = 2/(1+c)
r = 1/c
# log(C_p^2/C_r), using p'=2/(1-c) and r'=1/(1-c).
young_log = sp.log(2/(1+c))*(1+c)/2-sp.log(2/(1-c))*(1-c)/2 \
    +c*sp.log(c)/2-(1-c)*sp.log(1-c)/2
young_target = c*sp.log(2)+c*sp.log(c)/2-(1+c)*sp.log(1+c)/2
# Identity checked after expanding logs on the mathematical domain 0<c<1.
young_res = sp.simplify(sp.expand_log(young_log-young_target, force=True))
assert young_res == 0
hy_log = c*sp.log(2*sp.pi)+(q-c)*sp.log(q/(q-c))/2-c*sp.log(q/c)/2
hy_target = c*sp.log(2*sp.pi)+(q/2-c)*sp.log(q)-(q-c)*sp.log(q-c)/2+c*sp.log(c)/2
assert sp.simplify(sp.expand_log(hy_log-hy_target, force=True)) == 0
log_g = c*sp.log(2)-(1+c)*sp.log(1+c)/2
log_h = (q/2-c)*sp.log(q)-(q-c)*sp.log(q-c)/2
assert sp.simplify(sp.diff(log_g,c,2)+1/(2*(1+c))) == 0
assert sp.simplify(sp.diff(log_h,c,2)+1/(2*(q-c))) == 0
assert sp.simplify(sp.diff(log_g,c).subs(c,1)-(sp.log(2)-1)/2) == 0
assert sp.simplify(sp.diff(log_h,c).subs(c,0)-(1-sp.log(q))/2) == 0
alpha_log = 2*sp.log(sp.pi)+2+sp.log(2/q)
assert sp.simplify(sp.expand_log(sp.log(2*sp.pi)+(1-sp.log(2*q)/2)-alpha_log/2, force=True)) == 0
results["checks"]["symbolic_identities"] = "PASS: Young, Hausdorff-Young, tangent derivatives, constant cancellation"

max_frame_error = 0.0
matrix_cases = 0
max_gaussian_ratio = 0.0
for m,k in [(1,1),(3,5),(5,3),(8,11),(12,7)]:
    for scale in [0.0, 0.01, 1.0, 10.0, 1000.0]:
        B = rng.normal(size=(m,k))
        alpha=(math.pi*math.e)**2
        M=alpha*np.eye(m)+scale**2*B@B.T
        inv=np.linalg.inv(M)
        vals,vecs=np.linalg.eigh(M)
        invhalf=(vecs*(1/np.sqrt(vals)))@vecs.T
        V=math.sqrt(alpha)*invhalf
        W=scale*invhalf@B
        err=np.linalg.norm(V@V.T+W@W.T-np.eye(m),ord=2)
        max_frame_error=max(max_frame_error,float(err))
        ci=np.sum(V*V,axis=0)
        dj=np.sum(W*W,axis=0)
        assert np.min(ci)>0 and np.max(ci)<=1+1e-8
        assert np.min(dj)>=-1e-10 and np.max(dj)<=1+1e-8
        assert abs(np.sum(1-ci)-np.sum(dj))<1e-6
        singular=np.linalg.svd(B,compute_uv=False)
        graph_log=-0.5*np.log1p((scale*singular/(math.pi*math.e))**2).sum()
        # f(x)=exp(-pi*x*x), D variance=1/pi, q=2.
        gaussian_log=-0.5*np.log1p((scale*singular/math.pi)**2).sum()
        ratio=math.exp(float(gaussian_log-graph_log))
        max_gaussian_ratio=max(max_gaussian_ratio,ratio)
        assert ratio<=1+1e-12
        matrix_cases+=1
results["checks"]["graph_frame"]={"cases":matrix_cases,"max_operator_identity_error":max_frame_error}
results["checks"]["gaussian_graph_examples"]={"cases":matrix_cases,"max_exact_integral_over_bound":max_gaussian_ratio}

uniform_cases=[]
for qv in [1.0,4/3,1.5,2.0]:
    L=math.pi*math.e*math.sqrt(2/qv)
    for a in [0.0,0.1,1.0,5.0,10.0,30.0,100.0]:
        d=a*a/(L*L+a*a)
        if d>qv/2+1e-12:
            continue  # scalar Fourier exponent outside the claimed domain
        integrand=lambda x: 2*(1-x)*abs(np.sinc(a*x/(2*math.pi)))**qv
        # Break at Fourier zeros to avoid cusp quadrature artifacts.
        zeros=[2*math.pi*j/a for j in range(1,int(a/(2*math.pi))+1)] if a else []
        edges=[0.0]+[x for x in zeros if 0<x<1]+[1.0]
        val=sum(quad(integrand,lo,hi,epsabs=2e-10,epsrel=2e-10,limit=100)[0] for lo,hi in zip(edges,edges[1:]))
        bound=(1+a*a/(L*L))**(-0.5)
        assert val<=bound+1e-8
        uniform_cases.append({"q":qv,"a":a,"integral":val,"bound":bound})
results["checks"]["uniform_difference_graph_examples"]=uniform_cases

quad_cases=0
worst_quad_ratio=0.0
for n in [3,6,10,18]:
    for _ in range(8):
        M=rng.normal(size=(n,n))
        A=(M+M.T)/2
        # Include arbitrary self blocks, not only pure bilinear forms.
        cut=n//2
        B=A[:cut,cut:]
        singular=np.linalg.svd(B,compute_uv=False)
        eig=np.linalg.eigvalsh(A)
        for t in [0.0,0.2,1.0,20.0]:
            exact_log=-0.25*np.log1p((t*eig/math.pi)**2).sum()
            bound_log=-0.125*np.log1p((2*t*singular/(math.pi*math.e))**2).sum()
            ratio=math.exp(float(exact_log-bound_log))
            assert ratio<=1+1e-10
            worst_quad_ratio=max(worst_quad_ratio,ratio)
            quad_cases+=1
results["checks"]["gaussian_full_quadratic_examples"]={"cases":quad_cases,"max_exact_characteristic_modulus_over_bound":worst_quad_ratio}

# Gamma integral and the simpler min-envelope constants.
constants=[]
for qv,rv in [(2.,5),(2.,6),(1.,3),(4/3,3)]:
    nu=rv/(4*qv)
    exact=math.e/(2*math.sqrt(2*qv))*math.sqrt(math.pi)*math.exp(gammaln(nu-0.5)-gammaln(nu))
    simple=math.e/math.sqrt(2*qv)*rv/(rv-2*qv)
    assert exact<=simple+1e-12
    constants.append({"q":qv,"large_cross_singular_values":rv,"sigma":1,"gamma_bound":exact,"simple_bound":simple})
results["checks"]["density_constants"]=constants

# Extra small singular values only improve the regularized upper envelope.
for eps in [1e-12,1e-8,1e-4,0.1,1.0]:
    singular=np.array([1.,1.,1.,1.,1.,eps,eps**2])
    for t in [0.01,1.,100.,1e6]:
        all_log=-0.125*np.log1p((2*t*singular/(math.pi*math.e))**2).sum()
        five_log=-5/8*math.log1p((2*t/(math.pi*math.e))**2)
        assert all_log<=five_log+1e-12
results["checks"]["small_extra_singular_values"]="PASS in listed finite examples; monotonicity is proved in the report"
results["status"]="PASS"
(ROOT/"check_results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":results["status"],"matrix_cases":matrix_cases,"uniform_cases":len(uniform_cases),"gaussian_quadratic_cases":quad_cases,"density_constants":constants},indent=2))
