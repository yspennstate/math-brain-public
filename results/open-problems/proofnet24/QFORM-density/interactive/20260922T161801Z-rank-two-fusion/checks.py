"""Finite checks of the rank-two fractional-trace argument.
These verify identities and examples, not the universal analytic theorem.
No network calls. Requires numpy, scipy and sympy.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
import scipy.integrate as si
import sympy as sp


def bathtub_exact(a: float) -> float:
    """Sup over probability densities <=1 of integral |x*x-a|^-1/2 f(x)."""
    if a == 0.0:
        return math.inf
    if a < 0:
        return 2 * math.asinh(0.5 / math.sqrt(-a))
    if a <= 0.125:
        return math.pi + 2 * math.acosh(0.5 / math.sqrt(a))
    tau = math.sqrt(a / 4 - 1 / 64)
    r = tau / a
    # Stable version of pi-2 asin(sqrt(1-r)) + 2 acosh(sqrt(1+r)).
    return 2 * math.asin(math.sqrt(r)) + 2 * math.asinh(math.sqrt(r))


def psi(a: float) -> float:
    a = abs(a)
    if a == 0:
        return math.inf
    return 1 + math.log(1 / a) if a <= 1 else a ** -0.25


def run() -> dict:
    out = {'scope': 'finite identities and examples only; not a universal or independent proof', 'checks': {}}
    grid = np.logspace(-12, 12, 1201)
    ratios = [bathtub_exact(float(a)) / (8 * psi(float(a))) for a in np.r_[grid, -grid]]
    out['checks']['bathtub_envelope'] = {'cases': len(ratios), 'max_exact_over_bound': max(ratios)}
    assert max(ratios) < 1
    weak_constant = 64 * math.exp(-1.5)
    assert weak_constant < 15
    out['checks']['weak_L2_squared_constant'] = {'exact_max': weak_constant, 'bound': 15}
    a,b,c,d,e,f,h = sp.symbols('a b c d e f h', nonzero=True, real=True)
    L = sp.Matrix([[a,b,c],[b,d,e],[c,e,f]])
    D = L[1:,1:] - sp.Matrix([b,c]) * sp.Matrix([[b,c]]) / a
    assert sp.simplify(D.det() - L.det()/a) == 0
    out['checks']['symbolic_schur_determinant'] = 'PASS'
    # Kernel scaling cancellation independent of the nonzero Rayleigh coefficient.
    beta, delta, K = sp.symbols('beta delta K', positive=True)
    expr = K/sp.sqrt(beta) * (K**2*delta/beta**2)**(-sp.Rational(1,4))
    assert sp.simplify(expr - sp.sqrt(K)*delta**(-sp.Rational(1,4))) == 0
    out['checks']['rayleigh_cancellation'] = 'PASS'
    rng = np.random.default_rng(20260922)
    examples = []
    for n in (3,4,7,16,32,64):
        for _ in range(8):
            U,_ = np.linalg.qr(rng.normal(size=(n,3)))
            lam = np.array([1.0,2.0,-3.0])
            A = (U * lam) @ U.T
            i = int(np.argmax(np.abs(np.diag(A))))
            ai = A[i,i]
            ui = U[i,:]
            leverage = float(ui @ ui)
            keep = np.arange(n) != i
            C = A[np.ix_(keep,keep)]
            bv = A[keep,i]
            S = C - np.outer(bv,bv)/ai
            # Right singular vectors give an orthonormal basis of ui-perp.
            _,_,vh = np.linalg.svd(ui.reshape(1,3),full_matrices=True)
            T = vh[1:,:].T
            W = U[keep,:] @ T
            H = np.diag(lam) - np.outer(lam*ui,lam*ui)/ai
            D2 = T.T @ H @ T
            err_frame = np.linalg.norm(W.T@W-np.eye(2))
            err_rebuild = np.linalg.norm(S-W@D2@W.T)
            rel_det = abs(np.linalg.det(D2)-leverage*np.prod(lam)/ai) / max(1,abs(np.linalg.det(D2)))
            assert err_frame < 1e-10 and err_rebuild < 1e-9 and rel_det < 1e-10
            examples.append((err_frame,err_rebuild,rel_det))
    out['checks']['physical_pivot_frame'] = {'cases': len(examples), 'max_frame_error': max(x[0] for x in examples), 'max_reconstruction_error': max(x[1] for x in examples), 'max_relative_determinant_error': max(x[2] for x in examples)}
    spectral = []
    for det in (1e-12, 1e-3, 1.0, 1e3, 1e12):
        kk = math.e*math.pi/math.sqrt(det)
        # After t=kk*u, the integral is sqrt(kk)*integral u^-1/2 min(1,1/u).
        lo = si.quad(lambda u: u**-0.5, 0, 1)[0]
        hi = si.quad(lambda u: u**-1.5, 1, np.inf)[0]
        got = 2*math.sqrt(kk)*(lo+hi)/math.sqrt(2*math.pi)
        expected = 4*math.sqrt(2*math.e)*det**-0.25
        assert math.isclose(got, expected, rel_tol=1e-9)
        spectral.append({'absolute_determinant': det, 'relative_error': abs(got/expected-1)})
    out['checks']['diffuse_Riesz_integral'] = spectral
    out['constants'] = {'rank_two_half_Riesz': 16*math.sqrt(30), 'diffuse_half_Riesz': 4*math.sqrt(2*math.e), 'cap_one_shear_constant':16*math.sqrt(15)}
    out['status'] = 'PASS'
    return out

if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_name('check_results.json')
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
