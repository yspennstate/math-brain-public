#!/usr/bin/env python3
"""Numerical consistency checks for PROB20-14 canonical recentering.

This is a certificate/checking aid, not a proof.  It uses only the Python
standard library.

We take the critical offspring law
    P(0)=0.29, P(1)=0.50, P(2)=0.20, P(10)=0.01,
whose mean is exactly 1.  For a pair (m,L), conditioning on S_m=m-L makes
all values >m-L impossible.  We:

1. truncate the one-site law to {0,...,m-L};
2. exponentially tilt the truncated law so its mean is exactly 1-L/m;
3. compute the conditional first-coordinate marginal under the original law
   and under the tilted law by exact finite convolutions;
4. verify that the two conditional marginals agree to floating precision.

The identity is exact mathematically because product weights differ only by
a factor depending on the fixed total.  The script is intended to catch
index/sign mistakes in implementations of the reduction.
"""

from math import exp

PI = {0: 0.29, 1: 0.50, 2: 0.20, 10: 0.01}
assert abs(sum(PI.values()) - 1.0) < 1e-15
assert abs(sum(k * p for k, p in PI.items()) - 1.0) < 1e-15


def convolve_n(pmf, n, max_sum):
    """Return probabilities of sums 0..max_sum for n iid pmf variables."""
    cur = [0.0] * (max_sum + 1)
    cur[0] = 1.0
    items = list(pmf.items())
    for _ in range(n):
        nxt = [0.0] * (max_sum + 1)
        for s, ps in enumerate(cur):
            if ps == 0.0:
                continue
            for x, px in items:
                if s + x <= max_sum:
                    nxt[s + x] += ps * px
        cur = nxt
    return cur


def truncated_base(total):
    z = sum(p for x, p in PI.items() if x <= total)
    return {x: p / z for x, p in PI.items() if x <= total}


def mean_of(pmf):
    return sum(x * p for x, p in pmf.items())


def tilt_to_mean(base, target_mean):
    """Bisection for theta in p_theta(x) proportional p(x)e^{theta x}."""
    xs = sorted(base)
    assert xs[0] < target_mean < xs[-1]

    def tilted(theta):
        # stabilize exponentials by subtracting the maximum exponent
        a = max(theta * x for x in xs)
        w = {x: base[x] * exp(theta * x - a) for x in xs}
        z = sum(w.values())
        return {x: wx / z for x, wx in w.items()}

    lo, hi = -1.0, 1.0
    while mean_of(tilted(lo)) >= target_mean:
        lo *= 2.0
    while mean_of(tilted(hi)) <= target_mean:
        hi *= 2.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if mean_of(tilted(mid)) < target_mean:
            lo = mid
        else:
            hi = mid
    theta = 0.5 * (lo + hi)
    return theta, tilted(theta)


def conditional_first_marginal(pmf, m, total):
    rest = convolve_n(pmf, m - 1, total)
    denom = convolve_n(pmf, m, total)[total]
    assert denom > 0.0
    out = {}
    for x, px in pmf.items():
        if x <= total:
            out[x] = px * rest[total - x] / denom
    return out


def qmoment(pmf, q):
    return sum((x ** q) * p for x, p in pmf.items())


def run_case(m, L, q=1.5):
    total = m - L
    base = truncated_base(total)
    target_mean = total / m
    theta, tilted = tilt_to_mean(base, target_mean)

    cond_original = conditional_first_marginal(PI, m, total)
    cond_tilted = conditional_first_marginal(tilted, m, total)
    keys = sorted(set(cond_original) | set(cond_tilted))
    max_err = max(abs(cond_original.get(k, 0.0) - cond_tilted.get(k, 0.0)) for k in keys)

    print(f"m={m:4d} L={L:4d} total={total:4d} theta={theta:+.8e}")
    print(f"  truncated mean = {mean_of(base):.12f}")
    print(f"  tilted mean    = {mean_of(tilted):.12f} (target {target_mean:.12f})")
    print(f"  max conditional-marginal error = {max_err:.3e}")
    print(f"  q-moment base/tilted/original = {qmoment(base,q):.12f} / "
          f"{qmoment(tilted,q):.12f} / {qmoment(PI,q):.12f}")
    assert max_err < 5e-11
    assert abs(mean_of(tilted) - target_mean) < 5e-13


if __name__ == "__main__":
    # First case removes the atom 10 exactly; later cases also test downward tilts.
    for case in [(7, 1), (11, 2), (40, 3), (100, 7), (400, 12)]:
        run_case(*case)
    print("All canonical-conditioning identity checks passed.")
