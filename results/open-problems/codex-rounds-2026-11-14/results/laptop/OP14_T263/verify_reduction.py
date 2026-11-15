"""Small deterministic analytic checks; no training, numpy, torch, or GPU.

Run: python -B verify_reduction.py
All output files are written beside this script. Python stdlib only.
"""

import os

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"

import csv
import ctypes
import json
import math
from pathlib import Path
import time

if os.name == "nt":
    kernel = ctypes.windll.kernel32
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    kernel.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    if not kernel.SetPriorityClass(kernel.GetCurrentProcess(), 0x4000):
        raise OSError("Could not set BelowNormal priority")

ROOT = Path(__file__).resolve().parent
SQRT2 = math.sqrt(2.0)
SQRT2PI = math.sqrt(2.0 * math.pi)


def tail(t):
    return 0.5 * math.erfc(t / SQRT2)


def interval_mass(lo, hi):
    # Stable even for very small positive or negative tail intervals.
    if lo >= 0:
        return max(0.0, tail(lo) - tail(hi))
    if hi <= 0:
        return max(0.0, tail(-hi) - tail(-lo))
    return 1.0 - tail(-lo) - tail(hi)


def score(x1, x2, u, v):
    # Evaluate the original four-neuron score, rather than the tail formula.
    p = u[0] * x1 + u[1] * x2
    q = v[0] * x1 + v[1] * x2
    return max(p, 0.0) - max(-p, 0.0) + max(q, 0.0) + max(-q, 0.0)


def conditional_error(z2, y, mu, cov, u, v):
    x2 = y * mu[1] + math.sqrt(cov[1][1]) * z2
    mean = y * mu[0] + cov[0][1] / cov[1][1] * (x2 - y * mu[1])
    sd = math.sqrt(cov[0][0] - cov[0][1] ** 2 / cov[1][1])
    cuts = []
    if v[0] != 0.0:
        cuts.append(-v[1] * x2 / v[0])
    for s in (-1, 1):
        a = u[0] + s * v[0]
        if a != 0.0:
            cuts.append(-(u[1] + s * v[1]) * x2 / a)
    cuts = [-math.inf] + sorted(set(cuts)) + [math.inf]
    result = 0.0
    for lo, hi in zip(cuts, cuts[1:]):
        if lo == -math.inf and hi == math.inf:
            probe = 0.0
        elif lo == -math.inf:
            probe = hi - max(1.0, abs(hi))
        elif hi == math.inf:
            probe = lo + max(1.0, abs(lo))
        else:
            probe = (lo + hi) / 2.0
        if y * score(probe, x2, u, v) < 0.0:
            result += interval_mass((lo - mean) / sd, (hi - mean) / sd)
    return result


def adaptive_simpson(fn, a, b, tol, depth=20):
    c = (a + b) / 2.0
    fa, fc, fb = fn(a), fn(c), fn(b)
    whole = (b - a) * (fa + 4 * fc + fb) / 6.0

    def rec(a, b, fa, fc, fb, whole, tol, depth):
        c = (a + b) / 2.0
        l, r = (a + c) / 2.0, (c + b) / 2.0
        fl, fr = fn(l), fn(r)
        left = (c - a) * (fa + 4 * fl + fc) / 6.0
        right = (b - c) * (fc + 4 * fr + fb) / 6.0
        delta = left + right - whole
        if abs(delta) <= 15.0 * tol:
            return left + right + delta / 15.0
        if depth == 0:
            raise ArithmeticError(f"Quadrature failed: [{a}, {b}], "
                                  f"delta={delta}, tol={tol}, f={(fa, fc, fb)}")
        return (rec(a, c, fa, fl, fc, left, tol / 2, depth - 1)
                + rec(c, b, fc, fr, fb, right, tol / 2, depth - 1))

    return rec(a, b, fa, fc, fb, whole, tol, depth)


def integrate_original(mu, cov, u, v, panels, tol):
    # Scaling by the Bayes tail keeps rare-error quadrature away from an
    # absolute-error floor. It does not use either of the predicted margins.
    det = cov[0][0] * cov[1][1] - cov[0][1] ** 2
    s2 = (cov[1][1] * mu[0] ** 2 - 2 * cov[0][1] * mu[0] * mu[1]
          + cov[0][0] * mu[1] ** 2) / det
    scale = tail(math.sqrt(max(0.0, s2)))

    def fn(z):
        p = (conditional_error(z, 1, mu, cov, u, v)
             + conditional_error(z, -1, mu, cov, u, v)) / 2.0
        return math.exp(-z * z / 2.0) / SQRT2PI * (p / scale)

    # Omitted probability <= 2 Q(40) < exp(-800), before rescaling.
    # Wide composite panels prevent missing off-centre narrow peaks.
    width = 80.0 / panels
    cuts = [-40.0 + k * width for k in range(panels + 1)]
    # The piecewise linear boundary changes topology at x2=0 for each label.
    # Split there explicitly; recursively bisecting across its cusp otherwise
    # consumes the depth budget despite a tiny total quadrature error.
    for y in (-1, 1):
        cusp = -y * mu[1] / math.sqrt(cov[1][1])
        if -40.0 < cusp < 40.0:
            cuts.append(cusp)
    cuts = sorted(set(cuts))
    total = math.fsum(adaptive_simpson(fn, a, b, tol / (len(cuts)-1))
                      for a, b in zip(cuts, cuts[1:]))
    return total * scale


def exact_risk(mu, cov, u, v):
    margins = []
    for s in (-1, 1):
        w = [u[j] + s * v[j] for j in range(2)]
        variance = math.fsum(w[i] * cov[i][j] * w[j]
                             for i in range(2) for j in range(2))
        if variance <= 0:
            raise ValueError("Degenerate branch")
        margins.append(math.fsum(w[j] * mu[j] for j in range(2))
                       / math.sqrt(variance))
    return math.fsum(tail(t) for t in margins) / 2.0, margins


def write_csv(name, rows):
    with (ROOT / name).open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    start = time.perf_counter()
    identity = [[1.0, 0.0], [0.0, 1.0]]
    cases = [
        ("orthogonal", [2.0, 0.0], identity, [1.0, 0.0], [0.0, 0.7]),
        ("correlated", [1.2, -0.4], [[1.3, 0.4], [0.4, 0.8]],
         [0.8, -0.2], [0.25, 0.5]),
        ("opposite_margin_signs", [1.0, 0.4], identity,
         [0.3, 0.2], [1.0, -0.5]),
        ("reversed_u", [1.5, 0.0], identity, [-1.0, 0.2], [0.1, 0.6]),
        ("zero_v", [2.0, 0.3], identity, [1.0, 0.1], [0.0, 0.0]),
        ("zero_signal", [0.0, 0.0], identity, [0.8, 0.2], [0.1, 0.4]),
        ("zero_u", [2.0, 0.0], identity, [0.0, 0.0], [0.5, 0.7]),
        ("parallel", [1.5, 0.0], identity, [1.0, 0.0], [0.4, 0.0]),
        ("rare_error", [8.0, 0.0], identity, [1.0, 0.0], [0.0, 0.25]),
    ]
    rows = []
    for name, mu, cov, u, v in cases:
        print("Checking " + name, flush=True)
        expected, margins = exact_risk(mu, cov, u, v)
        integral = integrate_original(mu, cov, u, v, 320, 1e-9)
        refined = integrate_original(mu, cov, u, v, 640, 2e-10)
        error = abs(integral / expected - 1.0)
        refined_error = abs(refined / expected - 1.0)
        assert max(error, refined_error) < 2e-8, (name, expected, integral, refined)
        rows.append(dict(case=name, rho_minus=margins[0], rho_plus=margins[1],
                         formula=expected, integral=integral, refined=refined,
                         relative_error=error, refined_relative_error=refined_error))
        write_csv("risk_identity_checks.csv", rows)

    grid = []
    for a in [1.0, 1.1, 2.0, 4.0, 8.0, 16.0, 32.0]:
        for b in [1.0, 1.1, 2.0, 4.0, 8.0, 16.0, 32.0]:
            if b <= a:
                log_ratio = math.log(tail(b)) - math.log(tail(a))
                gap = (a * a - b * b) / 2.0
                assert log_ratio >= gap - 1e-12
                assert log_ratio <= gap + math.log(a / b) + 1e-12
                grid.append(dict(a=a, b=b, log_ratio=log_ratio,
                                 log_lower=gap, log_upper=gap + math.log(a / b)))

    thresholds = []
    for r in [2.0, 4.0, 8.0, 16.0, 32.0]:
        for name, b in [("critical_c1", 1.0 / r),
                        ("critical_c2", 2.0 / r),
                        ("vanishing_L2_failure", 1.0 / math.sqrt(r))]:
            t = r / math.sqrt(1.0 + b * b)
            log_ratio = math.log(tail(t)) - math.log(tail(r))
            gap = r * r * b * b / (1.0 + b * b)
            thresholds.append(dict(regime=name, r=r, b=b, even_second_moment=b*b,
                                   squared_margin_gap=gap, risk=tail(t),
                                   bayes_risk=tail(r), risk_ratio=math.exp(log_ratio),
                                   ratio_lower=math.exp(gap / 2.0),
                                   ratio_upper=(r / t) * math.exp(gap / 2.0)))

    # The excluded u=v case has a half-space of zero scores, not a null tie set.
    try:
        exact_risk([1.0, 0.0], identity, [1.0, 0.0], [1.0, 0.0])
    except ValueError:
        degenerate_rejected = True
    else:
        raise AssertionError("Degeneracy was not rejected")

    write_csv("risk_identity_checks.csv", rows)
    write_csv("tail_inequality_checks.csv", grid)
    write_csv("contamination_threshold.csv", thresholds)
    result = dict(risk_cases=len(rows), tail_inequality_cases=len(grid),
                  threshold_rows=len(thresholds), degenerate_rejected=degenerate_rejected,
                  max_relative_error=max(x["relative_error"] for x in rows),
                  max_refined_relative_error=max(x["refined_relative_error"] for x in rows),
                  runtime_seconds=time.perf_counter()-start,
                  threads="one; stdlib only", priority="BelowNormal on Windows")
    (ROOT / "verification_summary.json").write_text(json.dumps(result, indent=2)+"\n",
                                                     encoding="utf-8")
    print(json.dumps(result, indent=2))
    for row in thresholds[-3:]:
        print("r={r:g} {regime}: risk_ratio={risk_ratio:.10g}".format(**row))


if __name__ == "__main__":
    main()
