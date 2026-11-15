#!/usr/bin/env python3
"""Deterministic checks of PROOF.md; standard library, one process.

Run: env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
     VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_level_stability.py
No files are written. Quadrature is a numerical audit, not a proof.
"""

import ctypes
import math
import os
import resource
import sys
import time


def enforce_budget():
    # getpriority can validly return -1, so check errno separately.
    libc = ctypes.CDLL(None, use_errno=True)
    libc.getpriority.argtypes = (ctypes.c_int, ctypes.c_uint)
    libc.getpriority.restype = ctypes.c_int
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)  # PRIO_PROCESS, current process
    error = ctypes.get_errno()
    if error or priority < 15:
        raise SystemExit(f"Budget guard: niceness={priority}, errno={error}; stopping")
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise SystemExit("Budget guard: OMP_NUM_THREADS must equal 1")
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    print(f"niceness={priority}; OMP_NUM_THREADS=1; CPU cap=60 seconds")


PI = math.pi
SQRTPI = math.sqrt(PI)


def phi(t):
    return math.exp(-t*t/2) / math.sqrt(2*PI)


def alpha(t):
    return phi(t) * (t*t - 1 + 2*math.exp(-t*t)) / (4*PI)


def beta(t):
    return (phi(t)*math.exp(-t*t)/(2*PI)
            + t*phi(t)*math.erf(t)/(2*SQRTPI))


def I(d):
    return (math.erf(math.sqrt(1.5)*d)/math.sqrt(3)-d*phi(d))/(4*PI)


def J(d):
    return (math.sqrt(3)/(4*PI)*math.erf(math.sqrt(1.5)*d)
            - phi(d)*math.erf(d)/(2*SQRTPI))


def K(d):
    return math.erf(d/math.sqrt(2))/2


def simpson(fun, a, b, n=6000):
    if a == b:
        return 0.0
    assert n % 2 == 0
    h = (b-a)/n
    # fsum limits summation error; generators keep memory constant.
    total = math.fsum((fun(a), fun(b),
                      4*math.fsum(fun(a+h*j) for j in range(1, n, 2)),
                      2*math.fsum(fun(a+h*j) for j in range(2, n, 2))))
    return total*h/3


def close(actual, expected, tol=5e-10):
    assert abs(actual-expected) <= tol, (actual, expected, tol)


def main():
    enforce_budget()
    start = time.monotonic()

    # Independent spectral-angle derivation of the derivative covariances.
    spectral = [simpson(fun, 0, 2*PI)/(2*PI) for fun in (
        lambda t: math.cos(t)**2,
        lambda t: math.cos(t)**4,
        lambda t: math.cos(t)**2*math.sin(t)**2)]
    for got, want in zip(spectral, (1/2, 3/8, 1/8)):
        close(got, want)
    print("spectral moments:", " ".join(f"{x:.12f}" for x in spectral))

    max_det_error = max_edge_error = 0.0
    for t in (-4., -2., -1., -.1, 0., .1, 1., 2., 4.):
        a = t*t/4
        # Integrate |a-z| against Exp(rate=4), splitting at the kink.
        direct_det = (simpson(lambda z: (a-z)*4*math.exp(-4*z), 0, a)
                      + simpson(lambda z: (z-a)*4*math.exp(-4*z), a, 16))
        det_formula = (t*t-1+2*math.exp(-t*t))/4
        close(direct_det, det_formula)
        max_det_error = max(max_det_error, abs(direct_det-det_formula))

        sigma = math.sqrt(1/8)
        pivot = t/(2*sigma)
        # E|sigma Z-t/2| with Z standard normal, split at its zero.
        direct_edge = (
            simpson(lambda z: (t/2-sigma*z)*phi(z), -12, pivot)
            + simpson(lambda z: (sigma*z-t/2)*phi(z), pivot, 12))
        edge_formula = math.exp(-t*t)/(2*SQRTPI)+t*math.erf(t)/2
        close(direct_edge, edge_formula)
        max_edge_error = max(max_edge_error, abs(direct_edge-edge_formula))
    print(f"conditional determinant max error={max_det_error:.3e}")
    print(f"conditional edge absolute-normal max error={max_edge_error:.3e}")

    max_I_error = max_J_error = 0.0
    for d in (1e-6, .001, .1, .5, 1., 2., 4.):
        qi = simpson(alpha, 0, d)
        qj = simpson(beta, 0, d)
        close(qi, I(d))
        close(qj, J(d))
        close(simpson(phi, 0, d), K(d))
        max_I_error = max(max_I_error, abs(qi-I(d)))
        max_J_error = max(max_J_error, abs(qj-J(d)))
        for t in (d, -d):
            close(alpha(t), alpha(d))
            close(beta(t), beta(d))
    print(f"I quadrature max error={max_I_error:.3e}")
    print(f"J quadrature max error={max_J_error:.3e}")

    interior_total = simpson(alpha, -12, 12, n=12000)
    saddle_total = simpson(lambda t: phi(t)*math.exp(-t*t)/(4*PI),
                           -12, 12, n=12000)
    edge_total = simpson(beta, -12, 12, n=12000)
    close(interior_total, 1/(2*PI*math.sqrt(3)))
    close(saddle_total, interior_total/2)
    close(edge_total, math.sqrt(3)/(2*PI))
    print(f"interior total={interior_total:.12f}; saddle total={saddle_total:.12f}")
    print(f"edge total={edge_total:.12f}")
    print(f"alpha(0)={alpha(0):.12f}; beta(0)={beta(0):.12f}; phi(0)={phi(0):.12f}")

    print("square exact bounds with u=R^(-3):")
    for R in (10, 100, 1000):
        d = R**(-3)
        bound = R*R*I(d)+4*R*J(d)+4*K(d)
        leading = phi(0)*(R*R/(4*PI)+2*R/PI+4)*d
        assert bound > 0
        close(bound, leading, tol=max(1e-15, leading*d*d*2))
        print(f"  R={R:4d} u={d:.1e} bound={bound:.12g} leading={leading:.12g}")

    # Very small rectangles: corners dominate, preventing an area-only bound.
    R, d = .01, .001
    components = (R*R*I(d), 4*R*J(d), 4*K(d))
    assert components[2] > components[0]+components[1]
    print("small-square area/edge/corner bound contributions:",
          " ".join(f"{x:.12g}" for x in components))

    # Audit the additional elementary bound (2a), including small rectangles
    # where omitting the edge or corner term would be unsafe.
    for L, H in ((.01, .02), (1., 1.), (100., 1.), (1000., 1000.)):
        area, perimeter = L*H, 2*(L+H)
        for d in (1e-6, .001, .1, .5, 1.):
            exact = area*I(d)+perimeter*J(d)+4*K(d)
            simple = phi(0)*d*(area/(4*PI)
                                + perimeter/(2*PI)*(1+d*d/3)+4)
            assert exact <= simple*(1+2e-14)
    print("elementary bound (2a): 20 aspect-ratio/level checks passed")

    elapsed = time.monotonic()-start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = rss/(1024**2) if sys.platform == "darwin" else rss/1024
    assert rss_mib < 1024
    assert elapsed < 60
    print(f"PASS; elapsed={elapsed:.3f}s; peak RSS={rss_mib:.2f} MiB")


if __name__ == "__main__":
    main()
