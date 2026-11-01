#!/usr/bin/env python3
"""Finite sanity checks for PROB20-20 2026-09-16T06-52-00Z report.

Checks four small exact-sum models:
1. marginal KL tensorization D(mu||pi) <= b/n;
2. record-envelope marginal KL lower bound;
3. Fenchel cloud-label entropy bound;
4. capped-band Bernoulli-mgf Chernoff inequality and its exact finite
   conditioning consequence n D(a||p) <= b - log P_cond(event).

These are finite bookkeeping checks, not proof of asymptotic claims.
"""
import math
from collections import defaultdict

LAWS = [
    ("lawA", [0.40, 0.25, 0.15, 0.08, 0.05, 0.04, 0.03], [(8, 15), (8, 18)]),
    ("lawB", [0.50, 0.20, 0.10, 0.07, 0.05, 0.04, 0.025, 0.015], [(8, 14), (8, 17)]),
]
L = 2
BAND_THRESHOLD = 8


def convolution(pi, n):
    d = {0: 1.0}
    for _ in range(n):
        nd = defaultdict(float)
        for s, ps in d.items():
            for k, pk in enumerate(pi):
                nd[s + k] += ps * pk
        d = dict(nd)
    return d


def conditional_marginal(pi, n, m):
    pm = convolution(pi, n).get(m, 0.0)
    prev = convolution(pi, n - 1)
    mu = [pk * prev.get(m - k, 0.0) / pm for k, pk in enumerate(pi)]
    return pm, mu


def kl(mu, pi):
    return sum(x * math.log(x / y) for x, y in zip(mu, pi) if x > 0.0)


def band_event(pi, n, m, L, U, threshold):
    d = {(0, 0): 1.0}
    for _ in range(n):
        nd = defaultdict(float)
        for (s, band_mass), ps in d.items():
            for k, pk in enumerate(pi):
                add = k if L < k <= U else 0
                nd[(s + k, band_mass + add)] += ps * pk
        d = dict(nd)
    pm = sum(ps for (s, _), ps in d.items() if s == m)
    joint = sum(ps for (s, bm), ps in d.items() if s == m and bm >= threshold)
    uncond = sum(ps for (_, bm), ps in d.items() if bm >= threshold)
    return pm, joint / pm, uncond


min_tensor_slack = float("inf")
min_record_slack = float("inf")
min_fenchel_slack = float("inf")
min_chernoff_slack = float("inf")
min_conditioning_slack = float("inf")
rows = []

for name, pi, cases in LAWS:
    nu = sum(k * pk for k, pk in enumerate(pi))
    c0 = 1.0 / (2.0 * (1.0 + nu))
    U = len(pi) - 1
    q = [k * pi[k] for k in range(len(pi))]
    rU = min(-math.log(c0 * q[k]) / k for k in range(1, U + 1) if q[k] > 0.0)
    Qbar = sum(k * pi[k] / nu for k in range(L + 1, U + 1))
    pbern = nu * Qbar / U

    for n, m in cases:
        pm, mu = conditional_marginal(pi, n, m)
        b = -math.log(pm)
        Dmu = kl(mu, pi)
        tensor_slack = b / n - Dmu

        cprof = [k * mu[k] for k in range(len(pi))]
        C = sum(cprof[k] for k in range(L + 1, U + 1))
        A = sum(mu[k] for k in range(L + 1, U + 1))
        H = -sum((cprof[k] / k) * math.log(cprof[k])
                 for k in range(L + 1, U + 1) if cprof[k] > 0.0)
        record_lower = C * rU - H - (1.0 + abs(math.log(c0))) * A
        record_slack = Dmu - record_lower

        theta = math.log(L) / L
        # Finite support is enough here; the report's universal proof uses the
        # larger infinite geometric-tail penalty.
        finite_penalty = math.exp(-1.0) * sum(
            math.exp(-theta * k) / k for k in range(L + 1, U + 1)
        )
        fenchel_upper = theta * C + finite_penalty
        fenchel_slack = fenchel_upper - H

        pm2, cond_event, uncond_event = band_event(pi, n, m, L, U, BAND_THRESHOLD)
        assert abs(pm2 - pm) < 1e-12
        c = BAND_THRESHOLD / n
        a = c / U
        pbern = nu * Qbar / U
        if not (0.0 < pbern < a < 1.0):
            raise AssertionError("test chosen outside nontrivial Bernoulli Chernoff branch")
        bern_kl = a * math.log(a / pbern) + (1.0 - a) * math.log((1.0 - a) / (1.0 - pbern))
        chernoff_upper = math.exp(-n * bern_kl)
        chernoff_slack = chernoff_upper - uncond_event
        conditioning_slack = (b - math.log(cond_event)) - n * bern_kl

        min_tensor_slack = min(min_tensor_slack, tensor_slack)
        min_record_slack = min(min_record_slack, record_slack)
        min_fenchel_slack = min(min_fenchel_slack, fenchel_slack)
        min_chernoff_slack = min(min_chernoff_slack, chernoff_slack)
        min_conditioning_slack = min(min_conditioning_slack, conditioning_slack)
        rows.append((name, n, m, cond_event, tensor_slack, record_slack,
                     fenchel_slack, chernoff_slack, conditioning_slack))

print("PROB20-20 finite band/record-entropy checker")
for row in rows:
    name, n, m, cond_event, ts, rs, fs, cs, xs = row
    print(
        f"{name} n={n} m={m}: cond_event={cond_event:.12f} "
        f"tensor_slack={ts:.12g} record_slack={rs:.12g} "
        f"fenchel_slack={fs:.12g} chernoff_slack={cs:.12g} "
        f"conditioning_slack={xs:.12g}"
    )
print(f"minimum tensor slack: {min_tensor_slack:.12g}")
print(f"minimum record-envelope slack: {min_record_slack:.12g}")
print(f"minimum Fenchel slack: {min_fenchel_slack:.12g}")
print(f"minimum Chernoff slack: {min_chernoff_slack:.12g}")
print(f"minimum conditioning-consequence slack: {min_conditioning_slack:.12g}")
assert min_tensor_slack >= -1e-12
assert min_record_slack >= -1e-12
assert min_fenchel_slack >= -1e-12
assert min_chernoff_slack >= -1e-12
assert min_conditioning_slack >= -1e-12
print("PASS")
