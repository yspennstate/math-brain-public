"""Small deterministic checks of PROOF.md; no random graph simulation."""

import json
import math
import os
import resource
import time
from pathlib import Path

# One thread. The loops have fixed small bounds; record actual peak RSS below.
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()
ELL = math.log(2)
R = math.sqrt(2)
C = math.log(ELL) + 1
A, B = 0.25, 0.75


def f(n):
    return 2 * math.log2(n) - 2 * math.log2(math.log2(n)) + 2 * math.log2(math.e / 2) + 1


def log_inverse(t):
    lo, hi = 1.00000001, max(10.0, t + 10)
    for _ in range(100):
        mid = (lo + hi) / 2
        value = 2 / ELL * (mid - math.log(mid) + C) - 1
        if value < t:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def inverse_count(n):
    total = 0
    for j in range(math.floor(f(16)), math.floor(f(n)) + 1):
        left, right = math.exp(log_inverse(j + A)), math.exp(log_inverse(j + B))
        # These finite checks avoid nearly integer endpoints.
        assert min(abs(left - round(left)), abs(right - round(right))) > 1e-6
        total += max(0, min(n, math.floor(right)) - max(16, math.ceil(left)) + 1)
    return total


counts = []
direct = 0
for n in range(16, 200001):
    phase = f(n) % 1
    direct += A <= phase <= B
    if n in (1000, 10000, 100000, 200000):
        inverse = inverse_count(n)
        assert direct == inverse
        counts.append({"N": n, "direct_count": direct, "inverse_count": inverse})

# A separate endpoint recurrence: if L and U are limiting proportions at
# entry and exit, U=1-(1-L)/s and L=U/s, where s=r**(1/2).
s = 2**0.25
lower_recurrence = 1 / (1 + s)
upper_recurrence = s / (1 + s)
lower_geometric = (R**(B-A) - 1) / (R - 1)
upper_geometric = R * (1 - R**(A-B)) / (R - 1)
assert abs(lower_recurrence - lower_geometric) < 1e-14
assert abs(upper_recurrence - upper_geometric) < 1e-14

# Floating-point quadrature via exact real-band lengths, scaled by X(m+u).
# No claim of certified intervals is made for this asymptotic diagnostic.
cycles = []
for m in (40, 160, 640, 2560):
    row = {"cycle": m}
    for label, u, expected in (("entry", A, lower_recurrence), ("exit", B, upper_recurrence)):
        cutoff = log_inverse(m + u)
        terms = []
        for j in range(6, m + 1):
            if j + A > m + u:
                continue
            left = log_inverse(j + A)
            right = log_inverse(min(j + B, m + u))
            terms.append(math.exp(right-cutoff) - math.exp(left-cutoff))
        ratio = math.fsum(terms)
        row[label] = ratio
        row[label + "_error"] = ratio - expected
    cycles.append(row)

# Check the bracket identity (16) independently from its expanded terms.
identity_error = 0.0
theta_checks = []
for exponent in (10, 20, 40, 80, 160):
    n = 2**exponent
    L = math.log(n)
    k = math.floor(f(n))
    t = f(n) - k
    left = L - ELL / 2 * (k - 1) - math.log(k) + 1
    right = math.log((2 / ELL) * L / k) + ELL / 2 * t
    identity_error = max(identity_error, abs(left - right))
    # Product formula, not subtracting two large log-factorials in n.
    log_mu = math.fsum(math.log(n-i) for i in range(k)) - math.lgamma(k+1) - ELL*k*(k-1)/2
    theta_checks.append({"log2_n": exponent, "phase": t, "theta": log_mu/L})
assert identity_error < 1e-12
assert abs(cycles[-1]["entry_error"]) < abs(cycles[0]["entry_error"])
assert abs(cycles[-1]["exit_error"]) < abs(cycles[0]["exit_error"])

result = {
    "nice": os.getpriority(os.PRIO_PROCESS, 0),
    "constants": {"lower": lower_recurrence, "upper": upper_recurrence, "log_density": 0.5},
    "integer_counts": counts,
    "finite_cycle_diagnostic": cycles,
    "bracket_identity_max_error": identity_error,
    "theta_checks": theta_checks,
    "elapsed_seconds": round(time.monotonic()-started, 3),
    "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "status": "all checks passed",
}
Path("verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
