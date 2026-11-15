"""Independent scalar-law and small-ball calculations; no author code is imported.

Run: OPENBLAS_NUM_THREADS=1 python3 referee_numerics.py
The common envelope f(k) <= (k+120)/20 certifies the omitted series tails.
"""
import json
import math
import signal
import time
from pathlib import Path
import mpmath as mp

signal.alarm(240)
mp.mp.dps = 80
START = time.monotonic()
EPS = mp.mpf(1) / 20
A = 120


def weights(name, k):
    if name == "sqrt":
        return mp.sqrt(k + 1)
    if name == "log":
        return mp.log(k + 2)
    if name == "osc":
        return mp.sqrt(k + 1) + mp.mpf("0.4") * (-1) ** k
    if name == "two":
        return mp.mpf(1 if k == 0 else 2)
    return mp.mpf(1)


def solve(name, m):
    fv = [weights(name, k) for k in range(30000)]

    def series(d, details=False):
        prod, total = mp.mpf(1), mp.mpf(0)
        deriv, dprod = mp.mpf(0), mp.mpf(0)
        for k, f in enumerate(fv):
            fac = m * f / (d + m * f)
            if details:
                dprod = fac * dprod - prod * fac / (d + m * f)
            prod *= fac
            total += prod
            if details:
                deriv += dprod
            if prod < mp.mpf("1e-68"):
                if details:
                    b = d / (m * EPS)
                    assert b > 1
                    bound = prod * (k + 1 + A) / (b - 1)
                    return total, deriv, k + 1, bound
                return total
        raise RuntimeError("increase the saved weight table")

    # Find a cheap bracket before high precision, avoiding a long small-d tail.
    fdouble = [float(f) for f in fv]
    def float_M(d):
        total, r = 0.0, 1.0
        for f in fdouble:
            r *= m * f / (d + m * f)
            total += r
            if r < 1e-26:
                break
        return total
    low, high = 0.1, 8.0
    for _ in range(55):
        middle = (low + high) / 2
        if float_M(middle) > m:
            low = middle
        else:
            high = middle
    seed = mp.mpf((low + high) / 2)
    c = mp.findroot(lambda d: series(d) - m, (seed * mp.mpf("0.99"), seed * mp.mpf("1.01")),
                    tol=mp.mpf("1e-65"))
    value, derivative, K, tail = series(c, True)
    R = mp.mpf(1)
    p = []
    for f in fv[:K]:
        p.append(R * c / (c + m * f))
        R *= m * f / (c + m * f)
    mass = mp.fsum(p)
    mean = mp.fsum(k * pk for k, pk in enumerate(p))
    s = mp.fsum(f * pk for f, pk in zip(fv, p))
    # These are three exact induced tree shapes in the limit, after integrating
    # the degree processes of all unconstrained boundary vertices.
    lam = m / c
    a, b, d = fv[:3]
    aa, bb, dd = lam * a, lam * b, lam * d
    base = a / (c * (1 + aa))
    L0 = 1 + aa + m * bb
    L1 = 1 + aa + (m - 1) * bb + dd
    H0 = base ** m / L0
    H1 = m * base ** (m - 1) * lam * a * b / (c * (1 + aa)) * (
        1 / ((1 + bb) * L1) + 1 / (L0 * L1)
    )
    # Distinct scalar brackets, with certified truncation error much smaller
    # than either endpoint residual. Roundoff is checked again at 100 digits.
    delta = mp.mpf("1e-24")
    lowres, highres = series(c - delta) - m, series(c + delta) - m
    assert lowres > 0 > highres
    with mp.workdps(100):
        fv100 = [weights(name, k) for k in range(K)]
        r100, M100 = mp.mpf(1), mp.mpf(0)
        for f in fv100:
            r100 *= m * f / (c + m * f)
            M100 += r100
        precision_difference = abs(M100 - value)
    recerr = max(abs(c * p[k] - m * fv[k - 1] * p[k - 1] + m * fv[k] * p[k])
                 for k in range(1, min(K, 100)))
    fmt = lambda v: mp.nstr(v, 30)
    result = {
        "name": name, "m": m, "c": fmt(c), "p0_to_p10": [fmt(x) for x in p[:11]],
        "series_terms": K, "M_minus_m": fmt(value - m), "series_tail_bound": fmt(tail),
        "derivative": fmt(derivative), "mass": fmt(mass), "mean": fmt(mean),
        "s_minus_c": fmt(s - c), "recurrence_max_residual": fmt(recerr),
        "omitted_mass": fmt(R), "omitted_mean_bound": fmt(K * R + tail),
        "bracket_low": fmt(c - delta), "bracket_high": fmt(c + delta),
        "bracket_residual_low": fmt(lowres), "bracket_residual_high": fmt(highres),
        "80_vs_100_digit_series_difference": fmt(precision_difference),
        "ball_star0": fmt(p[0]), "ball_H0": fmt(H0), "ball_H1": fmt(H1),
    }
    print(f"{name} m={m} c={mp.nstr(c, 24)} p={','.join(mp.nstr(v, 12) for v in p[:4])} "
          f"K={K} tail<={mp.nstr(tail, 3)} H0={mp.nstr(H0, 12)} H1={mp.nstr(H1, 12)}", flush=True)
    return result


def main():
    results = []
    for name in ("sqrt", "log", "osc", "two", "uniform"):
        for m in (2, 3):
            results.append(solve(name, m))
            Path("referee_theory.json").write_text(json.dumps(results, indent=2) + "\n")
    print(f"elapsed_seconds={time.monotonic() - START:.3f}")


if __name__ == "__main__":
    main()
