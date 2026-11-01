#!/usr/bin/env python3
"""Finite bookkeeping checks for PROB20-20 canonical-smoothing report.

This is a sanity checker only.  The toy laws are finite truncations and do not
verify the universal asymptotic theorem.
"""

import math


def normalize(xs):
    s = sum(xs)
    return [x / s for x in xs]


def power_law(K, p):
    return normalize([(k + 1.0) ** (-p) for k in range(K + 1)])


def mean(pi):
    return sum(k * pk for k, pk in enumerate(pi))


def canonical_saddle(pi, U, lam):
    def stats(t):
        raw = [pi[k] * math.exp(t * k) for k in range(U + 1)]
        F = sum(raw)
        mu = sum(k * raw[k] for k in range(U + 1)) / F
        var = sum((k - mu) ** 2 * raw[k] for k in range(U + 1)) / F
        return F, mu, var, [x / F for x in raw]

    lo, hi = 0.0, 1.0
    while stats(hi)[1] < lam:
        hi *= 2.0
        if hi > 50.0:
            raise RuntimeError("failed to bracket saddle")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if stats(mid)[1] < lam:
            lo = mid
        else:
            hi = mid
    s = 0.5 * (lo + hi)
    F, mu, var, pcan = stats(s)
    I = lam * s - math.log(F)
    return s, F, I, var, pcan


def exact_sum_probability(p, n, m):
    arr = [0.0] * (m + 1)
    arr[0] = 1.0
    support = [(k, pk) for k, pk in enumerate(p[: m + 1]) if pk > 0.0]
    for _ in range(n):
        nxt = [0.0] * (m + 1)
        for subtotal, mass in enumerate(arr):
            if mass == 0.0:
                continue
            for k, pk in support:
                if subtotal + k <= m:
                    nxt[subtotal + k] += mass * pk
        arr = nxt
    return arr[m]


def run_case(power, K, n, m, U):
    pi = power_law(K, power)
    nu = mean(pi)
    lam = m / n
    if not (nu < lam < U):
        raise AssertionError("toy parameters not supercritical/capped")

    s, F, I, var, pcan = canonical_saddle(pi, U, lam)
    p_orig = exact_sum_probability(pi, n, m)
    p_cap = exact_sum_probability(pi[: U + 1], n, m)
    p_local = exact_sum_probability(pcan, n, m)

    b = -math.log(p_orig)
    eta = p_cap / p_orig
    ell = -math.log(p_local)

    # Exact exponential-change-of-measure identity:
    identity_error = abs(n * I - (b - math.log(eta) + math.log(p_local)))

    # Finite diagnostic for the theorem's local-loss form.  No universal
    # constant is inferred from these toy values.
    half_log = 0.5 * math.log(n)
    excess_local = ell - half_log
    normalized_excess = excess_local / (1.0 + var)

    return {
        "power": power,
        "nu": nu,
        "lambda": lam,
        "n": n,
        "m": m,
        "U": U,
        "s": s,
        "variance": var,
        "b": b,
        "eta": eta,
        "ell": ell,
        "half_log": half_log,
        "excess_local": excess_local,
        "normalized_excess": normalized_excess,
        "identity_error": identity_error,
    }


def main():
    cases = [
        (3.0, 120, 40, 32, 20),
        (2.8, 160, 50, 45, 25),
        (3.2, 120, 60, 42, 18),
    ]
    max_identity_error = 0.0
    min_excess = float("inf")
    max_normalized_excess = 0.0

    for args in cases:
        out = run_case(*args)
        max_identity_error = max(max_identity_error, out["identity_error"])
        min_excess = min(min_excess, out["excess_local"])
        max_normalized_excess = max(max_normalized_excess, out["normalized_excess"])
        print(
            "CASE",
            f"p={out['power']:.1f}",
            f"n={out['n']}",
            f"m={out['m']}",
            f"U={out['U']}",
            f"nu={out['nu']:.12f}",
            f"s={out['s']:.12f}",
            f"var={out['variance']:.12f}",
            f"b={out['b']:.12f}",
            f"eta={out['eta']:.12f}",
            f"ell={out['ell']:.12f}",
            f"ell-half_log={out['excess_local']:.12f}",
            f"normalized_excess={out['normalized_excess']:.12f}",
            f"identity_error={out['identity_error']:.3e}",
        )

    print(f"MAX_IDENTITY_ERROR {max_identity_error:.3e}")
    print(f"MIN_ELL_MINUS_HALF_LOG {min_excess:.12f}")
    print(f"MAX_NORMALIZED_LOCAL_EXCESS {max_normalized_excess:.12f}")
    if max_identity_error < 1e-10 and min_excess > 0.0:
        print("PASS")
    else:
        print("FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
