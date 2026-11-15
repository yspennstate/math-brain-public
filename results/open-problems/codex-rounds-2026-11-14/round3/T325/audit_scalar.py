"""Independent finite-n arithmetic audit; no training or third-party modules.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
     nice -n 15 python3 audit_scalar.py
"""

import math
import os
import resource
from fractions import Fraction as Q

# A stricter-than-requested 512 MiB address-space cap, before doing any work.
# Some macOS builds do not implement RLIMIT_AS; RSS is also reported below.
try:
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
    cap = "512 MiB address-space cap set"
except (ValueError, OSError) as exc:
    cap = f"RLIMIT_AS unavailable: {exc}"


def gaussian_sum_moments(n):
    """Expand (sum x_i^2)^k using independence and Gaussian IBP.

    Coefficients of the exponential generating series E exp(t x^2)
    are obtained from E[x^(2j)] = (2j-1) E[x^(2j-2)]. Multiply n
    truncated series, rather than invoking chi-square moments.
    """
    one = [Q(1)]
    even = 1
    for j in range(1, 5):
        even *= 2 * j - 1
        one.append(Q(even, math.factorial(j)))
    total = [Q(1)] + [Q(0)] * 4
    for _ in range(n):
        total = [sum((total[i] * one[k-i] for i in range(k+1)), Q(0))
                 for k in range(5)]
    return [total[k] * Q(math.factorial(k), n**k) for k in range(5)]


def closed_moments(n):
    moments = [Q(1)]
    for k in range(4):
        moments.append(moments[-1] * Q(n + 2*k, n))
    return moments


def poly_mul(left, right):
    result = [Q(0)] * (len(left)+len(right)-1)
    for i, u in enumerate(left):
        for j, v in enumerate(right):
            result[i+j] += u*v
    return result


def expect(poly, moments):
    return sum((c*m for c, m in zip(poly, moments)), Q(0))


def direct(a, b, m):
    # Multiply the two residual factors and their square before expectation.
    residual = poly_mul([1, -a], [1, -b])
    value = expect(poly_mul(residual, residual), m)
    da = -2 * expect(poly_mul([0, 1], poly_mul([1, -a],
                                      poly_mul([1, -b], [1, -b]))), m)
    db = -2 * expect(poly_mul([0, 1], poly_mul([1, -b],
                                      poly_mul([1, -a], [1, -a]))), m)
    return value, da, db


def token_prediction(xs, w, xq, a, b):
    # Directly apply scalar label-row attention updates, no S residual formula.
    n = len(xs)
    top = xs + [xq]
    labels = [w*x for x in xs] + [Q(0)]
    for step in [a, b]:
        weighted = sum((labels[i]*xs[i] for i in range(n)), Q(0))
        labels = [labels[j] - step*weighted*top[j]/n for j in range(n+1)]
    return -labels[-1]


def run():
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    print(f"Process nice: {priority}")
    assert priority >= 15
    print(cap)
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    ns = [1, 2, 3, 5, 10, 100, 1000]
    pairs = [(Q(-7), Q(3)), (Q(0), Q(0)), (Q(1, 2), Q(2, 3)),
             (Q(100), Q(-100)), (Q(2), Q(2))]
    for n in ns:
        m = gaussian_sum_moments(n)
        assert m == closed_moments(n)
        m0, m1, m2, m3, m4 = m
        det = m2*m4-m3*m3
        assert det == Q(2*(n+2)**2*(n+4), n**4) > 0
        # Solve the normal equations from the independent moments.
        p = (m4*m1-m3*m2)/det
        q = (m3*m1-m2*m2)/det
        assert p == Q(2*n, n+2)
        assert q == Q(n*n, (n+2)*(n+4))
        assert p*p-4*q == Q(8*n*n, (n+2)**2*(n+4)) > 0
        residual = [Q(1), -p, q]
        risk = expect(poly_mul(residual, residual), m)
        assert risk == Q(8, (n+2)*(n+4))
        # Independent normal-equation orthogonality of residual to S,S^2.
        assert expect([0]+residual, m) == 0
        assert expect([0, 0]+residual, m) == 0
        for a, b in pairs:
            p0, q0 = a+b, a*b
            fp = -2+2*m2*p0-2*m3*q0
            fq = 2*m2-2*m3*p0+2*m4*q0
            value, da, db = direct(a, b, m)
            assert da == fp+b*fq and db == fp+a*fq
            assert -da+db == (a-b)*fq
            gap = m2*(p0-p)**2-2*m3*(p0-p)*(q0-q)+m4*(q0-q)**2
            assert value == risk+gap
        # Direct integration of the loss after using only normal equations.
        assert risk == 1-p+m2*q
        print(f"n={n}: moments agree; min risk={risk}; "
              f"n^2 risk={float(n*n*risk):.9f}")

    xs = [Q(1, 3), Q(-2), Q(5, 4)]
    w, xq = Q(-4, 5), Q(7, 3)
    s = sum((x*x for x in xs), Q(0))/len(xs)
    for a, b in pairs:
        prediction = token_prediction(xs, w, xq, a, b)
        assert prediction == w*xq*(1-(1-a*s)*(1-b*s))
        assert prediction == token_prediction(xs, w, xq, b, a)
    print("Exact token-update, gradient, gap and difference-equation checks passed.")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # On macOS ru_maxrss is bytes; on Linux it is KiB.
    import sys
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    print(f"Peak RSS: {rss_bytes/1024**2:.2f} MiB")
    assert rss_bytes < 1024**3


if __name__ == "__main__":
    run()
