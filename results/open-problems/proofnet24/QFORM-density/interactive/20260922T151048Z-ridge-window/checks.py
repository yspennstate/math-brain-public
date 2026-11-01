"""Finite algebra/example checks; NOT verification of the universal proof.

Run: python checks.py
Requires numpy, scipy, sympy.  No network, random inputs use fixed seed.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import hadamard, qr
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(20260922)
results: dict[str, object] = {"scope": "finite algebra and examples only; not a universal proof", "checks": {}}
checks = results["checks"]
assert isinstance(checks, dict)

# The elementary determinant inequality used for the simpler bound.
x = sp.symbols("x", positive=True)
assert sp.simplify(sp.diff(sp.log(1+x)-x/(1+x), x)-x/(1+x)**2)==0
sigma, gamma = sp.symbols("sigma gamma", positive=True)
objective = 3*sigma**2/(gamma*(sigma**2-2*gamma**2))
assert sp.simplify(sp.diff(objective, gamma).subs(gamma, sigma/sp.sqrt(6))) == 0
assert sp.simplify(objective.subs(gamma, sigma/sp.sqrt(6))-9*sp.sqrt(6)/(2*sigma))==0
eta=sp.Rational(1,64)
delta=sp.Rational(7,32)
sig=delta-eta
assert sig == sp.Rational(13,64)
gam=sig/sp.sqrt(6)
ridge_bound=(1/sp.sqrt(7)+eta/gam)**2
constant=288*sp.sqrt(3*sp.E)/13
assert float(ridge_bound)<0.5
assert float(constant)<64
assert sp.simplify(3*sig**2/(sig**2+gam**2))==sp.Rational(18,7)
checks["symbolic"]={"status":"PASS", "sigma":str(sig),"gamma":str(gam),"ridge_diagonal_upper_bound":float(ridge_bound),"theta_lower_bound":"18/7", "constant_expression":str(constant),"constant":float(constant)}

# Check the exact integral of a power envelope, not just its asymptotic exponent.
integral_cases=[]
for q in (1., 4/3, 2.):
    theta=2*q+0.7
    Lq=math.pi*math.e*math.sqrt(2/q)
    gamma0=.3
    logdet=2.7*theta
    power=theta/(2*q)
    crossover=Lq/(2*gamma0)*math.exp(-logdet/(2*theta))
    left=quad(lambda t: 1. if t<=crossover else (crossover/t)**power,0,crossover)[0]
    tail=quad(lambda t: (crossover/t)**power,crossover,np.inf,epsabs=1e-9)[0]
    exact=2*crossover*theta/(theta-2*q)
    err=abs(2*(left+tail)-exact)
    assert err<1e-7
    integral_cases.append({"q":q,"theta":theta,"absolute_error":err})
checks["envelope_integrals"]=integral_cases

# Arbitrary-alpha graph estimates for Gaussian input densities of maximum 1.
# Such f has variance 1/(2pi); D=f*tilde(f) has variance 1/pi.
graph_cases=0
max_ratio=0.
max_frame_error=0.
for m,k in ((2,3),(3,7),(5,9),(6,4)):
    for q in (1.,4/3,2.):
        R=rng.normal(size=(m,k))/math.sqrt(k)
        for a in (.1,1.,8.):
            # Increase alpha until the required Fourier exponents are admissible.
            alpha=.1
            for _ in range(40):
                M=alpha*np.eye(m)+a*a*(R@R.T)
                Mi=np.linalg.inv(M)
                d=a*a*np.einsum('ij,ij->j',R,Mi@R)
                if d.max()<=q/2+1e-12:
                    break
                alpha*=1.7
            else:
                raise AssertionError("failed to produce admissible graph parameters")
            ev,V=np.linalg.eigh(M)
            Mih=(V/np.sqrt(ev))@V.T
            frame=alpha*(Mih@Mih)+a*a*Mih@R@R.T@Mih
            err=float(np.linalg.norm(frame-np.eye(m),2))
            max_frame_error=max(max_frame_error,err)
            assert err<1e-8
            theta=float(d.sum())
            Lq=math.pi*math.e*math.sqrt(2/q)
            _,ldet=np.linalg.slogdet(np.eye(m)+a*a*R@R.T/alpha)
            log_bound=-.5*ldet+theta*math.log(Lq/math.sqrt(alpha))
            _,lexact=np.linalg.slogdet(np.eye(m)+q*a*a*R@R.T/math.pi**2)
            log_exact=-.5*lexact
            ratio=math.exp(log_exact-log_bound)
            assert ratio<=1+1e-8
            max_ratio=max(max_ratio,ratio)
            graph_cases+=1
checks["free_alpha_gaussian_graph"]={"cases":graph_cases,"max_exact_over_bound":max_ratio,"max_frame_identity_error":max_frame_error}

# Genuine full-rank indefinite forms: flat large eigenspace plus dense,
# nonseparable perturbations in its orthogonal complement.
full_rank_cases=[]
n=128
H=hadamard(n).astype(float)/math.sqrt(n)
for r in (3,4):
    U=H[:,1:r+1]
    Vbase=np.delete(H,np.arange(1,r+1),axis=1)
    for tailscale in (1/128,1/4096,1e-7):
        rotation,_=qr(rng.normal(size=(n-r,n-r)),mode='economic')
        V=Vbase@rotation
        signs=rng.choice((-1.,1.),size=n-r)
        tailvals=signs*tailscale*rng.uniform(.3,.9,size=n-r)
        mainvals=np.array([1.,1.,-1.]+([.1] if r==4 else []))
        E=(V*tailvals)@V.T
        A=(U*mainvals)@U.T+E
        I=np.arange(n//2); J=np.arange(n//2,n)
        B=A[np.ix_(I,J)]
        B0=((U*mainvals)@U.T)[np.ix_(I,J)]
        sv=np.linalg.svd(B,compute_uv=False)
        assert sv[2]>=float(sig)-1e-10
        Rridge=(B@B.T)@np.linalg.inv(float(gam)**2*np.eye(len(I))+B@B.T)
        Rridge=(Rridge+Rridge.T)/2
        maxdiag=float(np.diag(Rridge).max())
        theta=float(np.trace(Rridge))
        assert maxdiag<=float(ridge_bound)+1e-9
        assert theta>=18/7-1e-9
        assert np.linalg.matrix_rank(A,tol=1e-10)==n
        assert np.linalg.matrix_rank(B,tol=1e-10)==len(I)
        _,logD=np.linalg.slogdet(np.eye(len(I))+B@B.T/float(gam)**2)
        exact_cert=math.e/(math.sqrt(2)*float(gam))*theta/(theta-2)*math.exp(-logD/(2*theta))
        assert exact_cert<=float(constant)+1e-8
        # Gaussian characteristic functions are checked against the claimed envelope.
        for t in (.01,1.,20.,100.,10000.):
            evals=np.linalg.eigvalsh(A)
            logactual=-.25*np.log1p(t*t*evals*evals/math.pi**2).sum()
            logenv=min(0.,-logD/4+theta/2*math.log(math.pi*math.e*math.sqrt(2)/(2*float(gam)*t)))
            assert logactual<=logenv+1e-8
        full_rank_cases.append({"n":n,"large_window_rank":r,"tail_norm":float(np.max(abs(tailvals))),"full_rank":n,"cross_rank":len(I),"max_window_leverage":float(np.max(np.sum(U*U,axis=1))),"third_cross_singular_value":float(sv[2]),"max_ridge_diagonal":maxdiag,"effective_dimension":theta,"ridge_density_certificate":exact_cert,"tail_offdiagonal_frobenius_norm":float(np.linalg.norm(E-np.diag(np.diag(E))))})
checks["full_rank_nonseparable_examples"]=full_rank_cases
results["status"]="PASS"
(ROOT/'check_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({"status":results["status"],"graph_cases":graph_cases,"full_rank_cases":len(full_rank_cases),"constant":float(constant),"ridge_upper_bound":float(ridge_bound)},indent=2))
