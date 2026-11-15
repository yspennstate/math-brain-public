#!/usr/bin/env python3
"""Exact polynomial, cut-locus and sample-moment checks for PROOF.md.

Run with OMP_NUM_THREADS=1, nice -n 15, python3 -B. No files are written.
"""
import os
import sys
import resource
import time
from fractions import Fraction as F
from itertools import product


def main():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise SystemExit("REFUSED: actual niceness must be at least 15")
    resource.setrlimit(resource.RLIMIT_CPU, (60, 65))
    start = time.monotonic()

    # Two-variable polynomials, with rational coefficients.
    def tidy(p):
        return {k: F(v) for k, v in p.items() if v}

    def add(*polys):
        out = {}
        for p in polys:
            for k, v in p.items():
                out[k] = out.get(k, F(0)) + v
        return tidy(out)

    def scale(p, a):
        return tidy({k: v * a for k, v in p.items()})

    def mul(p, q):
        out = {}
        for (i, j), a in p.items():
            for (k, ell), b in q.items():
                key = (i + k, j + ell)
                out[key] = out.get(key, F(0)) + a * b
        return tidy(out)

    def deriv(p, axis):
        out = {}
        for ij, a in p.items():
            if ij[axis]:
                key = list(ij)
                key[axis] -= 1
                out[tuple(key)] = a * ij[axis]
        return tidy(out)

    def integral(p):
        return sum((a / ((i + 1) * (j + 1)) for (i, j), a in p.items()), F(0))

    def face(p, axis, value):
        out = {}
        for ij, a in p.items():
            key = ij[1 - axis]
            out[key] = out.get(key, F(0)) + a * value**ij[axis]
        return {k: v for k, v in out.items() if v}

    def evaluate(p, x):
        return sum((a * x[0]**i * x[1]**j for (i, j), a in p.items()), F(0))

    one = {(0, 0): F(1)}
    ax = {(2, 0): F(1), (3, 0): F(-2), (4, 0): F(1)}
    ay = {(0, 2): F(1), (0, 3): F(-2), (0, 4): F(1)}
    raw = scale(mul(ax, ay), F(1, 10000))
    f = add(raw, scale(one, -integral(raw)))
    assert integral(f) == 0
    v = [deriv(f, i) for i in range(2)]
    h = [[deriv(v[i], j) for j in range(2)] for i in range(2)]
    assert h[0][1] == h[1][0]
    cofactor = [[h[1][1], scale(h[0][1], -1)],
                [scale(h[1][0], -1), h[0][0]]]
    det = add(mul(h[0][0], h[1][1]), scale(mul(h[0][1], h[1][0]), -1))
    trace = add(h[0][0], h[1][1])
    q = add(one, scale(trace, -1))
    jac = add(mul(add(one, scale(h[0][0], -1)),
                  add(one, scale(h[1][1], -1))),
              scale(mul(h[0][1], h[1][0]), -1))
    assert jac == add(q, det)
    r = [scale(add(*(mul(cofactor[i][j], v[j]) for j in range(2))), F(1, 2))
         for i in range(2)]
    assert add(*(deriv(r[i], i) for i in range(2))) == det
    trace_h2 = add(*(mul(h[i][j], h[j][i]) for i in range(2) for j in range(2)))
    assert scale(add(mul(trace, trace), scale(trace_h2, -1)), F(1, 2)) == det

    # A second expression for 2R, independent of cofactor differentiation.
    energy_poly = add(*(mul(w, w) for w in v))
    for i in range(2):
        assert scale(r[i], 2) == add(mul(trace, v[i]),
                                    scale(deriv(energy_poly, i), -F(1, 2)))
        for endpoint in (F(0), F(1)):
            assert not face(v[i], i, endpoint)
            assert not face(h[i][1 - i], i, endpoint)
            assert not face(r[i], i, endpoint)

    energy = integral(energy_poly)
    vr = integral(add(*(mul(v[i], r[i]) for i in range(2))))
    assert integral(det) == 0
    assert integral(q) == integral(jac) == 1
    assert integral(mul(f, q)) == energy
    assert integral(mul(f, jac)) == energy - vr
    # Coefficient sums bound each entry on Q; maximum absolute row sum
    # bounds the operator norm of a symmetric matrix.
    gamma_bound = max(sum(sum(abs(a) for a in h[i][j].values()) for j in range(2))
                      for i in range(2))
    assert gamma_bound < F(1, 8)

    points = [(F(a), F(b)) for a, b in (
        (F(1, 100), F(1, 100)), (F(99, 100), F(99, 100)),
        (F(1, 4), F(1, 4)), (F(3, 4), F(3, 4)),
        (F(1, 5), F(4, 5)), (F(4, 5), F(1, 5)))]
    for x, y in product(points, repeat=2):
        vx = tuple(evaluate(w, x) for w in v)
        fdiff = evaluate(f, y) - evaluate(f, x)
        v2 = sum(a*a for a in vx)
        base_square = sum((y[i]-x[i])**2 for i in range(2))
        moved_square = sum((y[i]-x[i]+vx[i])**2 for i in range(2))
        assert abs(moved_square-base_square-2*fdiff-v2) <= gamma_bound*base_square
        lifts = [tuple(y[i]-x[i]+k[i] for i in range(2))
                 for k in product((-1, 0, 1), repeat=2)]
        base_torus = min(sum(a*a for a in z) for z in lifts)
        moved_torus = min(sum((z[i]+vx[i])**2 for i in range(2)) for z in lifts)
        assert abs(moved_torus-base_torus-2*fdiff-v2) <= gamma_bound*base_torus

    # Exact sample enumeration on a four-state probability space.
    # The three zero-mean basis vectors are orthonormal for uniform mass.
    basis = [(1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1)]
    eigenvalues = (F(2), F(5), F(9))
    multipliers = (F(1, 2), F(1, 3), F(1, 5))
    for a, b in product(range(3), repeat=2):
        assert sum(basis[a][s]*basis[b][s] for s in range(4)) == (4 if a == b else 0)
    spectral_target = sum((2*u-u*u)/lam for u, lam in zip(multipliers, eigenvalues))
    for n in (1, 2, 3):
        total = F(0)
        for sites in product(range(4), repeat=n):
            coeffs = [F(sum(vec[s] for s in sites), n) for vec in basis]
            nu_f = sum(u*a*a/lam for u, a, lam in zip(multipliers, coeffs, eigenvalues))
            e_f = sum(u*u*a*a/lam for u, a, lam in zip(multipliers, coeffs, eigenvalues))
            total += 2*nu_f - e_f
        assert n*total/F(4**n) == spectral_target

    # Independent exponent balance, without importing the preceding script.
    r_power = -F(1, 6)/5
    assert r_power == -F(1, 30)
    assert r_power/2 == -F(1, 60)
    assert F(1, 5)/2 + 1 == F(11, 10)
    assert -(1-F(5, 6))/2 == -F(1, 12)
    assert F(1, 2) + 1 == F(3, 2)

    print(f"niceness={priority}; exact rational arithmetic; one thread")
    print("Hessian operator-norm upper bound for test polynomial:", gamma_bound)
    print("PASS: Jacobian = 1-Delta f+det Hess f; divergence factor 1/2; independent trace identity.")
    print("PASS: Neumann condition, mixed face derivatives, normal flux, and Jacobian mass 1.")
    print("PASS: both integration-by-parts identities, including the sign of the source correction.")
    print(f"PASS: square and torus pointwise inequalities for {len(points)**2} ordered pairs each.")
    print("      Pairs include seam crossings and cut-locus ties.")
    print("Enumerated spectral target 2F-F_2 =", spectral_target)
    print("PASS: exhaustive sample expectations for n=1,2,3 agree with the spectral identity.")
    print("PASS: previous repair rate (-1/60,11/10); new reduction rate (-1/12,3/2).")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = rss if sys.platform == "darwin" else rss*1024
    assert rss < 1_000_000_000
    print(f"Peak resident memory: {rss} bytes")
    print(f"Elapsed time: {time.monotonic()-start:.3f} seconds")


if __name__ == "__main__":
    main()
