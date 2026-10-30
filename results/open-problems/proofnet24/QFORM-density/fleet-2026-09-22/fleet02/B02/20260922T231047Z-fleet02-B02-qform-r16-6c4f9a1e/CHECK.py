#!/usr/bin/env python3
import math
import random

try:
    import numpy as np
except Exception:
    np = None

SEED = 20260922
random.seed(SEED)


def H(q, c):
    if c == 0.0:
        return 1.0
    return q ** (q / 2.0 - c) * (q - c) ** (-(q - c) / 2.0)


def coarse_constant(k, q):
    assert k > 2 * q
    return math.e / math.sqrt(q) * k / (k - 2 * q)


def generate_capped_simplex(k, q, m, tries=200000):
    cap = q / 2.0
    out = []
    for _ in range(tries):
        xs = [random.random() for _ in range(m)]
        s = sum(xs)
        xs = [k * x / s for x in xs]
        if max(xs) <= cap + 1e-14:
            out.append(xs)
            if len(out) >= 200:
                break
    return out


def tangent_checks():
    worst = -1e300
    tested = 0
    cases = [(3, 1.0, 8), (3, 1.2, 8), (3, 1.48, 10), (5, 2.0, 9)]
    for k, q, m in cases:
        samples = generate_capped_simplex(k, q, m)
        if not samples:
            raise AssertionError((k, q, m, "no samples"))
        rhs = 0.5 * k * (1.0 - math.log(q))
        for a in samples:
            lhs = sum(math.log(H(q, c)) for c in a if c > 0)
            worst = max(worst, lhs - rhs)
            tested += 1
            if lhs > rhs + 1e-11:
                raise AssertionError((k, q, lhs, rhs, max(a)))
    return tested, worst


def transverse_exterior_checks():
    if np is None:
        return 0, None
    rng = np.random.default_rng(SEED)
    worst = 0.0
    for _ in range(100):
        m, n = 5, 6
        L, _ = np.linalg.qr(rng.normal(size=(m, 2)))
        R, _ = np.linalg.qr(rng.normal(size=(n, 2)))
        s = np.exp(rng.normal(size=2))
        B = L @ np.diag(s) @ R.T
        beta = rng.normal(size=n)
        eta = np.linalg.norm(beta - R @ (R.T @ beta))
        M = np.vstack([beta, B])
        sv = np.linalg.svd(M, compute_uv=False)
        z3 = 0.0
        for i in range(len(sv)):
            for j in range(i + 1, len(sv)):
                for l in range(j + 1, len(sv)):
                    z3 += (sv[i] * sv[j] * sv[l]) ** 2
        rhs = (s[0] * s[1]) ** 2 * eta ** 2
        err = abs(z3 - rhs) / max(1.0, abs(rhs))
        worst = max(worst, err)
        if err > 1e-10:
            raise AssertionError((z3, rhs, err))
    return 100, worst


def main():
    tested, tangent_worst = tangent_checks()
    ext_n, ext_worst = transverse_exterior_checks()
    c_d = coarse_constant(3, 1.0)
    c_d5 = coarse_constant(5, 2.0)
    if abs(c_d - 3 * math.e) > 1e-13:
        raise AssertionError(c_d)
    if abs(c_d5 - 5 * math.e / math.sqrt(2.0)) > 1e-13:
        raise AssertionError(c_d5)
    print("STATUS=PASS")
    print(f"seed={SEED}")
    print(f"sharp_D_constant={c_d:.15f}")
    print(f"sharp_D5_constant={c_d5:.15f}")
    print(f"tangent_samples={tested}")
    print(f"max_tangent_log_excess={tangent_worst:.3e}")
    if np is None:
        print("transverse_exterior_checks=SKIPPED_NO_NUMPY")
    else:
        print(f"transverse_exterior_checks={ext_n}")
        print(f"max_transverse_exterior_scaled_error={ext_worst:.3e}")


if __name__ == "__main__":
    main()
