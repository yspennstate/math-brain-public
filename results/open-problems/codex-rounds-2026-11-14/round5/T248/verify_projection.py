"""Independent projection and scalar-edge checks; standard library only.

No simulation of Tracy-Widom fluctuations. Run with the one-thread nice
command in LOG.md. All matrices below have size at most eight.
"""

import os
import sys

priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    print("NOT RUN: effective nice value below 15")
    sys.exit(77)

import math
import resource
import time
from fractions import Fraction as F

started = time.monotonic()
print(f"Effective nice value: {priority}")


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def frob2(a):
    return sum(x*x for row in a for x in row)


# Exact projection checks on covariance-like perturbations. This calculation
# uses ambient P matrices and row sums, not a chosen orthonormal basis Q.
for n in range(2, 9):
    p = [[F(i == j)-F(1, n) for j in range(n)] for i in range(n)]
    assert mm(p, p) == p
    assert all(sum(row) == 0 for row in p)
    dmat = [[F(0) if i == j else F((i+j+2)**2, 10*n*n)
             for j in range(n)] for i in range(n)]
    a = mm(mm(p, dmat), p)
    ede = sum(map(sum, dmat))/n
    de2 = sum(sum(row)**2 for row in dmat)/n
    assert trace(a) == -ede
    assert frob2(a) == frob2(dmat)-2*de2+ede**2
    assert frob2(a) <= frob2(dmat)
    for q in (F(0), F(2, 7), F(3, 4)):
        dim, v = n+1, F(2)
        sigma = [[(v-q/dim)*F(i == j)+q/dim
                  for j in range(n)] for i in range(n)]
        compressed = mm(mm(p, sigma), p)
        expected = [[(v-q/dim)*x for x in row] for row in p]
        assert compressed == expected
        defect = [[compressed[i][j]-v*p[i][j]
                   for j in range(n)] for i in range(n)]
        assert trace(defect) == -q*F(n-1, dim)
        assert frob2(defect) == q*q*F(n-1, dim*dim)
print("Exact rational P^2=P, trace, Frobenius identity, and spike removal:")
print("  N=2,...,8 and q=0,2/7,3/4 all passed")

# Independent check of the predecessor's d=2 pair/star/cycle constants:
# trapezoidal integration is exact for these finite Fourier polynomials.
angles = [2*math.pi*k/32 for k in range(32)]
pair = sum((math.cos(t)**2-0.5)**4 for t in angles)/len(angles)
second = sum((math.cos(t)**2-0.5)**2 for t in angles)/len(angles)
# Fix vertex 0 by rotation, integrate the remaining three vertices.
cycle = sum((math.cos(a)**2-0.5)
            *(math.cos(a-b)**2-0.5)
            *(math.cos(b-c)**2-0.5)
            *(math.cos(c)**2-0.5)
            for a in angles for b in angles for c in angles)/len(angles)**3
assert abs(pair-3/128) < 1e-14
assert abs(second**2-1/64) < 1e-14
assert abs(cycle-1/128) < 1e-14
print(f"Independent Fourier integrations at d=2: "
      f"pair={pair:.12f}, star={second**2:.12f}, cycle={cycle:.12f}")

# A bounded Lipschitz example: sigma(t)=cos(t)-exp(-1/2).
# The covariance can be calculated either from the joint characteristic
# function or from its even Hermite series.
q = math.exp(-1)/2
v = (1-math.exp(-1))**2/2
hermite_error = 0.0
for rho in (-1., -0.8, -0.3, 0., 0.3, 0.8, 1.):
    exact = math.exp(-1)*(math.cosh(rho)-1)
    series = math.exp(-1)*sum(rho**(2*k)/math.factorial(2*k)
                             for k in range(1, 14))
    hermite_error = max(hermite_error, abs(exact-series))
    assert abs(exact-series) < 1e-15
    remainder = exact-q*rho*rho
    assert abs(remainder) <= v*abs(rho)**3+1e-15
assert abs(math.exp(-1)*(math.cosh(1)-1)-v) < 1e-15
print(f"Cosine covariance: characteristic-function / Hermite max error "
      f"{hermite_error:.3e}")
for alpha, b in ((1., 0.25), (v/q, 1.), (4., 4.)):
    # The middle algebra check uses b=1 only to evaluate the threshold;
    # the proved universality theorem still excludes that aspect ratio.
    spike_strength = q*alpha*math.sqrt(b)/v
    print(f"  quadratic spike ratio q*alpha*sqrt(b)/v={spike_strength:.9f}; "
          "projection identity independent of ratio")


def scalar_edge(v, r, mean, eps, method):
    ts = (v+mean-eps, v+mean+eps)
    assert min(ts) > 0

    def f(u):
        return -1/u+r*sum(t/(1+t*u) for t in ts)/2

    lo, hi = -1/max(ts)+1e-12, -1e-12
    if method == "derivative":
        for _ in range(130):
            u = (lo+hi)/2
            fp = 1/u**2-r*sum(t*t/(1+t*u)**2 for t in ts)/2
            if fp < 0:
                lo = u
            else:
                hi = u
        return f((lo+hi)/2)
    # Independent minimization of f without evaluating its derivative.
    ratio = (math.sqrt(5)-1)/2
    left, right = hi-ratio*(hi-lo), lo+ratio*(hi-lo)
    for _ in range(130):
        if f(left) < f(right):
            hi, right = right, left
            left = hi-ratio*(hi-lo)
        else:
            lo, left = left, right
            right = lo+ratio*(hi-lo)
    return min(f(left), f(right))


max_solver_error = 0.0
max_expansion_error = 0.0
for r in (0.25, 0.5, 2., 4.):
    v = 1.3
    # Both signs of the mean defect must be retained. Mean=0 recovers
    # the predecessor's scalar perturbation check.
    for sign in (-1, 0, 1):
        for n in (1000, 10000, 100000, 1000000):
            mean, eps = sign*0.4/n, 0.6/math.sqrt(n)
            edge = scalar_edge(v, r, mean, eps, "derivative")
            other = scalar_edge(v, r, mean, eps, "minimization")
            max_solver_error = max(max_solver_error, abs(edge-other))
            assert abs(edge-other) < 1e-11
            e0 = v*(1+math.sqrt(r))**2
            # Independent second-order expansion in population eigenvalues.
            leading = (1+math.sqrt(r))**2*mean
            leading += (1+math.sqrt(r))**2/(v*math.sqrt(r))*eps**2
            if n == 1000000:
                error = abs((edge-e0)-leading)/(abs(leading)+1e-15)
                max_expansion_error = max(max_expansion_error, error)
                assert error < 0.001
            assert abs(edge-e0) < 100/n
print(f"Nonzero-trace edge lemma: max solver disagreement {max_solver_error:.3e}")
print(f"  linear-mean / quadratic-variance expansion max relative error "
      f"{max_expansion_error:.3e}")

max_scale_error = 0.0
max_center_error = 0.0
for m, n in ((200, 500), (500, 200), (317, 991), (991, 317)):
    v = 1.3
    dim = n-1
    b, c, r = m/n, dim/n, dim/m
    gamma = r**(1/6)/(v*(1+math.sqrt(r))**(4/3))
    converted = gamma*m**(2/3)*n/m
    gtilde = (b*c)**(1/6)/(v*(math.sqrt(b)+math.sqrt(c))**(4/3))
    direct = gtilde*n**(2/3)
    max_scale_error = max(max_scale_error, abs(converted/direct-1))
    # Independent Wishart singular-value fluctuation formula.
    johnstone = n/(v*(math.sqrt(m)+math.sqrt(dim))
                  *(1/math.sqrt(m)+1/math.sqrt(dim))**(1/3))
    assert abs(converted/johnstone-1) < 1e-14
    assert abs(converted/direct-1) < 1e-14
    e1 = b*v*(1+math.sqrt(r))**2
    e2 = v*(math.sqrt(b)+math.sqrt(c))**2
    e3 = v*(math.sqrt(m)+math.sqrt(dim))**2/n
    max_center_error = max(max_center_error, abs(e1-e2), abs(e2-e3))
    assert max(abs(e1-e2), abs(e2-e3)) < 1e-14
print(f"Projected N-1 normalization in both orientations: "
      f"scale error {max_scale_error:.3e}, center error {max_center_error:.3e}")

# The constant projected population shift is negative. It must not be
# discarded by pretending the compressed trace is zero.
for n in (100, 1000, 10000):
    q, v, b = 0.3, 1.3, 2.
    dim, d = n-1, n
    c = dim/n
    reference = v*(math.sqrt(b)+math.sqrt(c))**2
    shifted = (v-q/d)*(math.sqrt(b)+math.sqrt(c))**2
    coefficient = -q*(math.sqrt(b)+1)**2
    assert shifted < reference
    if n == 10000:
        assert abs(n*(shifted-reference)/coefficient-1) < 0.001
        print(f"Trace-defect sign: n*(shifted-reference)={n*(shifted-reference):.9f}; "
              f"limit coefficient={coefficient:.9f}")

# Interlacing alone leaves an order-one gap, even with a separated spike.
# K_P=diag(4,3,2), a=(10,0,0) gives K=diag(104,3,2).
assert 104 > 4 > 3
print("Interlacing failure example: lambda1(K)=104, lambda1(K_P)=4, lambda2(K)=3")
print("  The projected top cannot be identified with the original second by interlacing.")

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_mb = rss/(1024**2) if sys.platform == "darwin" else rss/1024
assert rss_mb < 1024
assert time.monotonic()-started < 60
print(f"PASS: algebra checks only; elapsed {time.monotonic()-started:.3f}s; "
      f"peak RSS {rss_mb:.1f} MiB")
