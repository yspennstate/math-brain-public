"""X032: deterministic algebra and independent atom-Hessian checks.

The proof and the rational logarithmic certificates are in agents/X032.md.
Numerical values below are verification, not the argument for the theorem.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

import numpy as np

I = np.eye(3)


def frame(b):
    a = .5-b
    return np.array([[2**-.5, 0, np.sqrt(b)],
                     [-2**-.5, 0, np.sqrt(b)],
                     [0, 2**-.5, -np.sqrt(a)],
                     [0, -2**-.5, -np.sqrt(a)]], complex)


def adj(a):
    h = np.trace(a)
    return a@a-h*a+(h*h-np.trace(a@a))/2*I


def basis():
    out = []
    for i in range(3):
        a = np.zeros((3, 3), complex)
        a[i, i] = 1
        out.append(a)
    for i, j in combinations(range(3), 2):
        a = np.zeros((3, 3), complex)
        a[i, j] = a[j, i] = 2**-.5
        out.append(a)
        a = np.zeros((3, 3), complex)
        a[i, j] = 1j*2**-.5
        a[j, i] = -1j*2**-.5
        out.append(a)
    return out


BASIS = basis()


def qmat(f):
    diag = np.array([f(a) for a in BASIS])
    out = np.diag(diag)
    for i, j in combinations(range(9), 2):
        out[i, j] = out[j, i] = (f(BASIS[i]+BASIS[j])-diag[i]-diag[j])/2
    return out


def geometry(v):
    u = [np.outer(z.conj(), z) for z in v]
    t = np.array([np.trace(z).real for z in u])
    effects, weights = {}, {}
    for i, j in combinations(range(4), 2):
        z = np.cross(v[i], v[j])
        effects[i, j] = np.outer(z, z.conj())
        weights[i, j] = np.vdot(z, z).real
    r = {s: abs(np.linalg.det(v[list(s)]))**2
         for s in combinations(range(4), 3)}
    w = sum(np.log(t[i]*t[j]/weights[i, j])*effects[i, j]
            for i, j in effects)
    e1 = -sum(t*np.log(t))
    e2 = -sum(x*np.log(x) for x in weights.values())
    e3 = -sum(x*np.log(x) for x in r.values())
    fv = lambda a: sum(np.trace(p@a).real**2/z for p, z in zip(u, t))
    fw = lambda a: sum(np.trace(effects[s]@a).real**2/weights[s]
                       for s in effects)
    return t, weights, r, w, e1-e2+e3, fv, fw


def inclusion_derivatives(k, direction, subset):
    """Differentiate a determinant by its multilinearity in columns."""
    n = len(subset)
    if not n:
        return 0., 0.
    base = k[np.ix_(subset, subset)]
    change = direction[np.ix_(subset, subset)]
    coefficients = []
    for order in (1, 2):
        value = 0.
        for columns in combinations(range(n), order):
            z = base.copy()
            z[:, columns] = change[:, columns]
            value += np.linalg.det(z).real
        coefficients.append(value*(2 if order == 2 else 1))
    return coefficients


def independent(v, s, a, data):
    t, weights, r, *_ = data
    q = 1-s
    subsets = [()] + [(i,) for i in range(4)] + list(weights) + list(r)
    k, d = s*v@v.conj().T, v@a@v.conj().T
    deriv = {z: inclusion_derivatives(k, d, z) for z in subsets}
    p = {(): q**3}
    p.update({(i,): s*q*q*t[i] for i in range(4)})
    p.update({z: s*s*q*x for z, x in weights.items()})
    p.update({z: s**3*x for z, x in r.items()})
    fi, acceleration = 0., 0.
    for z in subsets:
        dp, ddp = np.sum([(-1)**(len(top)-len(z))*np.array(deriv[top])
                          for top in subsets if set(z) <= set(top)], axis=0)
        fi += dp*dp/p[z]
        acceleration += ddp*np.log(p[z])
    return fi, fi+acceleration


def check(b):
    v = frame(b)
    assert np.linalg.norm(v.conj().T@v-I) < 1e-14
    data = geometry(v)
    t, weights, r, w, tau, fv, fw = data
    ca = np.log((.5+b)**2/(2*b))
    cb = np.log((1-b)**2/(1-2*b))
    cc = np.log(2*(.5+b)*(1-b))
    expected = np.diag([(1-2*b)*cb+2*b*cc,
                        2*b*ca+(1-2*b)*cc, cc])
    expected_tau = -2*(.5+b)*np.log(.5+b)-2*(1-b)*np.log(1-b)-np.log(2)
    assert np.linalg.norm(w-expected) < 2e-14
    assert abs(tau-expected_tau) < 2e-14
    ab = np.diag([3*b, -1+2*b, 1])
    fv_exact = 25*b*b/(1+2*b)
    qw_exact = 6*b*b*ca-(1-2*b)*((1-2*b)*cb+2*b*cc)
    assert abs(fv(ab)-fv_exact) < 2e-15
    assert abs(np.trace(w@adj(ab)).real-qw_exact) < 2e-15
    assert qw_exact-fv_exact > b*b/2
    rows = []
    test_a = np.array([[.4, .2-.1j, .07j],
                       [.2+.1j, -.15, .11], [-.07j, .11, .31]])
    for s in (.1, .5, .9):
        tt = w+s*tau*I
        negative_hessian = qmat(lambda a: independent(v, s, a, data)[1])
        expected_hessian = qmat(lambda a: fv(a)/s+fw(a)/(1-s)
                                -2*np.trace(tt@adj(a)).real)
        error = np.max(abs(negative_hessian-expected_hessian))
        assert error < 2e-11
        eigenvalues = np.linalg.eigvalsh(negative_hessian)
        assert eigenvalues[0] >= b*b-2e-12
        adaptive_gap = qmat(lambda a: fw(a)/7-np.trace(tt@adj(a)).real)
        assert np.linalg.eigvalsh(adaptive_gap)[0] >= -2e-13
        x = test_a[0, 0].real
        y = (test_a[1, 1]+test_a[2, 2]).real
        z = (test_a[1, 1]-test_a[2, 2]).real
        explicit_fw = ((1-2*b)*x*x+b/2*(y+z)**2
                       +2*(b*x+(1-b)*y/2-b*z/2)**2)
        assert abs(fw(np.diag(np.diag(test_a)))-explicit_fw) < 2e-15
        rows.append(dict(s=s, independent_identity_error=error,
                         negative_hessian_min_eigenvalue=eigenvalues[0],
                         adaptive_gap_min_eigenvalue=np.linalg.eigvalsh(adaptive_gap)[0]))
    return dict(b=b, W_diagonal=np.diag(w).real.tolist(), tau=tau,
                first_comparison_counterdirection=np.diag(ab).tolist(),
                QW_minus_Fv=qw_exact-fv_exact,
                proven_countergap_lower_bound=b*b/2,
                nearparallel_row_term=(.5+b)*ca, scalar_checks=rows)


if __name__ == '__main__':
    assert Fraction(1924, 405) > Fraction(19, 4)
    # Positive exponential partial sums certify both upper logarithmic bounds.
    from math import factorial
    assert sum(Fraction(5)**k/factorial(k) for k in range(8)) > 125
    assert sum(Fraction(7, 10)**k/factorial(k) for k in range(5)) > 2
    results = [check(b) for b in (.001, .0001)]
    out = Path(__file__).with_name('results.json')
    out.write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps(results, indent=2))
