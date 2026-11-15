"""Scalar checks of the covariance-edge lemma; standard library only.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
     nice -n 15 python3 verify_edge.py
No matrix simulation or edge-universality inference is made here.
"""

import math
from fractions import Fraction


def edge_by_derivative(v, r, epsilon):
    ts = (v - epsilon, v + epsilon)
    lo, hi = -1.0 / max(ts) + 1e-13, -1e-13
    for _ in range(110):
        u = (lo + hi) / 2
        derivative = 1 / u**2 - r * sum(t*t/(1+t*u)**2 for t in ts) / 2
        if derivative < 0:
            lo = u
        else:
            hi = u
    u = (lo + hi) / 2
    edge = -1/u + r * sum(t/(1+t*u) for t in ts) / 2
    second = -2/u**3 + r * sum(t**3/(1+t*u)**3 for t in ts)
    return u, edge, (2/second)**(1/3)


def edge_by_minimization(v, r, epsilon):
    # Independent calculation: minimize f directly, without its derivative.
    ts = (v - epsilon, v + epsilon)
    def f(u):
        return -1/u + r * sum(t/(1+t*u) for t in ts) / 2
    lo, hi = -1/max(ts) + 1e-12, -1e-12
    ratio = (math.sqrt(5) - 1) / 2
    left, right = hi - ratio*(hi-lo), lo + ratio*(hi-lo)
    fleft, fright = f(left), f(right)
    for _ in range(110):
        if fleft < fright:
            hi, right, fright = right, left, fleft
            left = hi-ratio*(hi-lo)
            fleft = f(left)
        else:
            lo, left, fleft = left, right, fright
            right = lo+ratio*(hi-lo)
            fright = f(right)
    return min(fleft, fright)


print('Two-point populations t=v+-epsilon; trace perturbation exactly zero')
print('v r eps/v edge_shift/s2 predicted relative_error minimizer_disagreement')
max_disagreement = 0.0
for v in (0.7, 1.3):
    for r in (0.25, 0.5, 2.0, 4.0):
        coefficient = (1+math.sqrt(r))**2/(v*math.sqrt(r))
        for relative_eps in (0.1, 0.03, 0.01, 0.003):
            epsilon = v*relative_eps
            _, edge, _ = edge_by_derivative(v, r, epsilon)
            independent_edge = edge_by_minimization(v, r, epsilon)
            disagreement = abs(edge-independent_edge)
            max_disagreement = max(max_disagreement, disagreement)
            e0 = v*(1+math.sqrt(r))**2
            ratio = (edge-e0)/epsilon**2
            relative_error = abs(ratio/coefficient-1)
            assert edge >= e0-1e-12
            assert disagreement < 1e-10
            if relative_eps == 0.003:
                assert relative_error < 0.002
            print(f'{v:.1f} {r:.2f} {relative_eps:.3f} {ratio:.9f} '
                  f'{coefficient:.9f} {relative_error:.3e} {disagreement:.3e}')

print(f'max edge disagreement: {max_disagreement:.3e}')

# Exact comparison of the spherical moment from radial Gaussians and Beta moments.
for d in (2, 3, 10, 100, 1000):
    radial = Fraction(15, d*(d+2)*(d+4))
    beta = Fraction(1, d)*Fraction(3, d+2)*Fraction(5, d+4)
    assert radial == beta
print('spherical sixth-moment identities: exact agreement at d=2,3,10,100,1000')

# The quadratic coefficient is also obtained by a finite difference in t.
max_coefficient_error = 0.0
for v in (0.7, 1.3):
    for r in (0.25, 0.5, 2., 4.):
        u0 = -1/(v*(1+math.sqrt(r)))
        h = v*1e-4
        def kernel(t):
            return t/(1+t*u0)
        numeric = r*(kernel(v+h)-2*kernel(v)+kernel(v-h))/(2*h*h)
        exact = (1+math.sqrt(r))**2/(v*math.sqrt(r))
        error = abs(numeric/exact-1)
        max_coefficient_error = max(max_coefficient_error, error)
        assert error < 1e-6
print(f'coefficient finite-difference max relative error: {max_coefficient_error:.3e}')

# Check normalization by independently converting sample count and aspect ratio.
max_scale_error = 0.0
for m, n in ((200, 500), (500, 200), (317, 991), (991, 317)):
    v = 1.3
    r, b = n/m, m/n
    gamma_h = r**(1/6)/(v*(1+math.sqrt(r))**(4/3))
    gamma_k = b**(1/6)/(v*(1+math.sqrt(b))**(4/3))
    lhs = gamma_h*r*m**(2/3)
    rhs = gamma_k*n**(2/3)
    error = abs(lhs/rhs-1)
    max_scale_error = max(max_scale_error, error)
    assert error < 1e-14
print(f'transposition scale max relative error: {max_scale_error:.3e}')

c = math.exp(1.5)/2
a1 = math.exp(-0.5)-2*c*math.exp(-2)
a3 = (-math.exp(-0.5)+8*c*math.exp(-2))/math.sqrt(6)
variance = ((1-math.exp(-2))/2+c*c*(1-math.exp(-8))/2
            -c*(math.exp(-0.5)-math.exp(-4.5)))
assert abs(a1) < 1e-14 and variance >= a3*a3 > 0
print(f'activation sin(t)-exp(3/2)sin(2t)/2: a1={a1:.3e}, '
      f'a3={a3:.9f}, variance={variance:.9f}')
print('PASS: scalar checks only; the TW conclusion uses the cited theorem.')
