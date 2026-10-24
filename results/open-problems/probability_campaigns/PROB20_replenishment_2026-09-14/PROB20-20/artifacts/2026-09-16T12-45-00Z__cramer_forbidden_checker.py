#!/usr/bin/env python3
"""Finite algebra checker for the PROB20-20 Cramer-forbidden-zone report.

This is a bookkeeping/sanity check only.  It does not verify the asymptotic
universal theorem.
"""
import math
import numpy as np


def normalize(raw):
    raw = np.asarray(raw, dtype=float)
    return raw / raw.sum()


def F(pi, cap, t):
    k = np.arange(len(pi))
    m = k <= cap
    return float(np.sum(pi[m] * np.exp(t * k[m])))


def dF(pi, cap, t):
    k = np.arange(len(pi))
    m = k <= cap
    return float(np.sum(k[m] * pi[m] * np.exp(t * k[m])))


def mean_t(pi, cap, t):
    return dF(pi, cap, t) / F(pi, cap, t)


def saddle(pi, cap, lam):
    if mean_t(pi, cap, 0.0) >= lam:
        return 0.0
    hi = 1e-5
    while mean_t(pi, cap, hi) < lam:
        hi *= 2.0
        if hi > 10.0:
            raise RuntimeError("failed to bracket saddle")
    lo = 0.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if mean_t(pi, cap, mid) < lam:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def rate(pi, cap, lam):
    s = saddle(pi, cap, lam)
    return s, lam * s - math.log(F(pi, cap, s))


def tilted_law(pi, cap, s):
    k = np.arange(len(pi))
    out = np.zeros_like(pi)
    m = k <= cap
    out[m] = pi[m] * np.exp(s * k[m]) / F(pi, cap, s)
    return out


def kl(p, q):
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / q[m])))


def truncated_mgf(pi, cap, t):
    k = np.arange(len(pi))
    m = k <= cap
    return float(np.sum(pi[m] * np.exp(t * k[m])) + np.sum(pi[~m]))


def truncated_rate(pi, cap, mu):
    k = np.arange(len(pi))
    m = k <= cap

    def log_derivative(t):
        num = float(np.sum(k[m] * pi[m] * np.exp(t * k[m])))
        return num / truncated_mgf(pi, cap, t)

    if mu <= log_derivative(0.0):
        return 0.0, 0.0
    hi = 1e-5
    while log_derivative(hi) < mu:
        hi *= 2.0
        if hi > 10.0:
            raise RuntimeError("failed to bracket truncated saddle")
    lo = 0.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if log_derivative(mid) < mu:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2.0
    return t, mu * t - math.log(truncated_mgf(pi, cap, t))


def run_case(name, pi, lam, L, K, U):
    kvals = np.arange(len(pi))
    nu = float(np.dot(kvals, pi))
    sU, IU = rate(pi, U, lam)
    sK, IK = rate(pi, K, lam)
    pU = tilted_law(pi, U, sU)
    pK = tilted_law(pi, K, sK)

    pyth_err = (IK - IU) - kl(pK, pU)

    band = (kvals > L) & (kvals <= K)
    D = float(np.sum(kvals[band] * pi[band] * np.exp(sU * kvals[band])))
    a = max(0.0, math.log(8.0 * lam / D))
    test_t = sU + a / L
    mean_slack = mean_t(pi, K, test_t) - lam
    saddle_slack = a / L - (sK - sU)

    rate_upper = lam * a / L + math.log(F(pi, U, sU) / F(pi, K, sU))
    rate_slack = rate_upper - (IK - IU)

    mu = nu + 0.15 * (lam - nu)
    Js = [truncated_rate(pi, cap, mu)[1] for cap in (L, K, U)]
    mono_slack = min(Js[0] - Js[1], Js[1] - Js[2])

    tol = 1e-10
    assert abs(pyth_err) < tol
    assert mean_slack > -tol
    assert saddle_slack > -tol
    assert rate_slack > -tol
    assert mono_slack > -tol

    print(f"CASE {name}")
    print(f"  nu={nu:.12g} lambda={lam:.12g}")
    print(f"  sU={sU:.12g} sK={sK:.12g} IU={IU:.12g} IK={IK:.12g}")
    print(f"  D(L,K;sU)={D:.12g}")
    print(f"  Pythagorean error={pyth_err:.3e}")
    print(f"  test-cap mean slack={mean_slack:.12g}")
    print(f"  saddle upper-bound slack={saddle_slack:.12g}")
    print(f"  rate upper-bound slack={rate_slack:.12g}")
    print(f"  truncated J(L),J(K),J(U)={Js}")
    print(f"  truncated-rate monotonicity slack={mono_slack:.12g}")
    return pyth_err, mean_slack, saddle_slack, rate_slack, mono_slack


k = np.arange(501)
examples = []
examples.append((
    "dense_sqrt",
    normalize(np.exp(-0.45 * np.sqrt(k + 1))),
    60.0, 80, 160, 400,
))

raw = np.zeros(501)
raw[0] = 1.0
raw[1] = 0.4
for kk, ww in [(8, 0.22), (20, 0.16), (50, 0.12), (100, 0.09),
               (180, 0.07), (300, 0.055), (450, 0.045)]:
    raw[kk] = ww
examples.append(("sparse_scales", normalize(raw), 45.0, 50, 180, 450))

raw = np.exp(-0.03 * k) / (k + 1) ** 1.2
raw *= np.where((k // 25) % 2 == 0, 1.0, 0.15)
examples.append(("staircase", normalize(raw), 12.0, 40, 120, 350))

stats = [run_case(*case) for case in examples]
print("SUMMARY")
print(f"  max |Pythagorean error|={max(abs(x[0]) for x in stats):.3e}")
print(f"  min mean slack={min(x[1] for x in stats):.12g}")
print(f"  min saddle slack={min(x[2] for x in stats):.12g}")
print(f"  min rate slack={min(x[3] for x in stats):.12g}")
print(f"  min truncated monotonicity slack={min(x[4] for x in stats):.12g}")
print("PASS")
