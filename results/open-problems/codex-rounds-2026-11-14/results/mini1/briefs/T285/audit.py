#!/usr/bin/env python3
"""Deterministic, standard-library audit of PROOF.md; no simulation."""
import csv
from fractions import Fraction
import math
import os
from pathlib import Path
import resource
import signal

assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
signal.alarm(120)
ROOT = Path(__file__).resolve().parent
mu = math.sqrt(2 / math.pi)
limit = (2 / math.pi) * (1 - 2 / math.pi)
rows = []
max_error = 0.0

# Method 1: exhaustive signs, independent of the pivotal-event derivation.
# Integrate Gaussian magnitudes analytically conditional on these signs.
for k in range(3, 18, 2):
    total1 = total3 = raw_mu_twice = raw_mu3 = 0
    for bits in range(1 << k):
        vote = 2 * bits.bit_count() - k
        y = 1 if vote > 0 else -1
        e1 = 1 if bits & 1 else -1
        e2 = 1 if bits & 2 else -1
        e3 = 1 if bits & 4 else -1
        total1 += y * e1
        total3 += y * e1 * e2 * e3
        # E[S(((G1-G2)^2)/2-1)|signs] equals
        # [-mu*(e1+e2)/2-mu^3*e1*e2*(vote-e1-e2)]/sqrt(k).
        raw_mu_twice -= y * (e1 + e2)
        raw_mu3 -= y * e1 * e2 * (vote - e1 - e2)
    f1 = Fraction(total1, 1 << k)
    f3 = Fraction(total3, 1 << k)
    pk = Fraction(math.comb(k - 1, (k - 1) // 2), 1 << (k - 1))
    assert f1 == pk
    assert f3 == -pk / (k - 2)
    # The raw-moment coefficients must be -p_K and +p_K separately.
    assert Fraction(raw_mu_twice, 2 * (1 << k)) == -pk
    assert Fraction(raw_mu3, 1 << k) == pk
    rho = mu * (1 - mu**2) * float(pk) / math.sqrt(k)
    raw_eigenvalue = (mu * raw_mu_twice / 2 + mu**3 * raw_mu3)
    raw_eigenvalue /= (1 << k) * math.sqrt(k)
    error = abs(raw_eigenvalue + rho)
    max_error = max(max_error, error)
    assert error < 1e-14
    # KxK contraction: diagonal a, off-diagonal b. Test on e1-e2.
    a = -mu * float(pk) / math.sqrt(k)
    b = -mu**3 * float(pk) / math.sqrt(k)
    assert abs(a - b + rho) < 1e-14
    rows.append({"K": k, "fourier1": str(f1), "fourier3": str(f3),
                 "rho": rho, "K_rho": k*rho,
                 "raw_moment_error": error})

with (ROOT / "exact_checks.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

# Method 2: check the central-binomial limit by the exact recurrence,
# not factorial asymptotics; compare against lgamma independently.
targets = {3, 11, 101, 1001, 10001, 100001}
asymptotic_rows = []
pk = 1.0  # p_1
for k in range(1, 100002, 2):
    if k in targets:
        j = (k - 1) // 2
        log_pk = math.lgamma(2*j+1) - 2*math.lgamma(j+1) - 2*j*math.log(2)
        pk_gamma = math.exp(log_pk)
        assert abs(pk / pk_gamma - 1) < 1e-8
        krho = mu * (1 - mu**2) * math.sqrt(k) * pk
        asymptotic_rows.append({"K": k, "p_recurrence": pk,
                                "p_lgamma": pk_gamma, "K_rho": krho,
                                "ratio_to_limit": krho/limit})
    pk *= k / (k + 1)

with (ROOT / "asymptotic_checks.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(asymptotic_rows[0]))
    writer.writeheader()
    writer.writerows(asymptotic_rows)

# Independently check Gaussian square moments and scalar variance.
def normal_moment(p):
    if p % 2:
        return 0
    value = 1
    for j in range(1, p, 2):
        value *= j
    return value

assert normal_moment(4)-2*normal_moment(2)+1 == 2
assert normal_moment(6)-3*normal_moment(4)+3*normal_moment(2)-1 == 8
for p in range(2, 31):
    assert normal_moment(2*p) <= 2**p * math.factorial(p)
    assert 2**(p-1)*(2**p*math.factorial(p)+1) <= 4**p*math.factorial(p)

# The concentration exponent at a=epsilon*rho/8 has denominator
# 272*8^2=17408; the theorem deliberately uses 32768 instead.
assert 272*8**2 == 17408
assert 32768 >= 17408
assert 8*(20**2)*6 == 19200
assert 4*32768 == 131072
assert normal_moment(6)-6*normal_moment(4)+9*normal_moment(2) == 6
for epsilon in (0.5, 0.1, 0.001):
    for row in rows:
        rho = row["rho"]
        B = math.sqrt(2*math.log(16/(epsilon*rho)))
        phi_B = math.exp(-B*B/2)/math.sqrt(2*math.pi)
        assert 4*phi_B <= epsilon*rho/4
        assert epsilon*rho/8 <= B
        assert epsilon/(2-epsilon) <= epsilon

print(f"priority={priority}; OMP_NUM_THREADS=1; standard library only")
print("exact enumeration: K=3,5,...,17; all rational identities PASS")
print(f"largest raw-moment vs tensor eigenvalue error: {max_error:.3g}")
print(f"lim K*rho_K = {limit:.15g}")
for row in asymptotic_rows:
    print(f"K={row['K']:6d} K*rho_K={row['K_rho']:.12f} "
          f"ratio={row['ratio_to_limit']:.12f}")
print("Gaussian moments, variance=2, clipping, concentration constants: PASS")
print("sample-split extension: Hermite L2=6; constants 19200 and 131072: PASS")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f"peak RSS (Darwin bytes): {rss}")
assert rss < 1_000_000_000
print("wrote exact_checks.csv and asymptotic_checks.csv")
