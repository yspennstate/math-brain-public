from fractions import Fraction
from collections import defaultdict


def conv_power(pmf, n):
    dist = {0: Fraction(1, 1)}
    for _ in range(n):
        nxt = defaultdict(Fraction)
        for s, ps in dist.items():
            for k, pk in pmf.items():
                nxt[s + k] += ps * pk
        dist = dict(nxt)
    return dist


laws = [
    {0: Fraction(2, 5), 1: Fraction(1, 5), 3: Fraction(1, 5), 8: Fraction(1, 5)},
    {0: Fraction(1, 2), 2: Fraction(1, 5), 5: Fraction(1, 5), 11: Fraction(1, 10)},
    {0: Fraction(3, 10), 1: Fraction(1, 10), 4: Fraction(3, 10), 9: Fraction(1, 5), 15: Fraction(1, 10)},
]

print("PROB20-20 forced-atom exact decomposition checker")
print("All arithmetic below is exact Fraction arithmetic.")

total_checks = 0
for law_id, pmf in enumerate(laws, 1):
    nu = sum(Fraction(k) * p for k, p in pmf.items())
    forced_k = max(pmf)
    max_n = 24
    dists = [None] + [conv_power(pmf, n) for n in range(1, max_n + 1)]

    checks = 0
    max_center_ratio = Fraction(0)
    for n in range(8, max_n + 1):
        for m, p_nm in dists[n].items():
            # A toy compact-supercritical window.
            if Fraction(m, n) <= nu + Fraction(1, 5):
                continue

            denom = Fraction(forced_k) - nu
            if denom <= 0:
                continue

            target = (Fraction(m) - nu * n) / denom
            r = max(0, int(target + Fraction(1, 2)))
            if r > n // 3:
                continue

            residual_n = n - r
            residual_m = m - r * forced_k
            if residual_m < 0:
                continue

            # Nearest-integer centering identity used in Theorem 4.1.
            centering_error = abs(Fraction(residual_m) - nu * residual_n)
            assert centering_error <= denom / 2
            if denom:
                max_center_ratio = max(max_center_ratio, centering_error / (denom / 2))

            # Exact subset contribution: requiring the first r variables to
            # equal forced_k gives a disjoint contribution to P(S_n=m).
            rhs = (pmf[forced_k] ** r) * dists[residual_n].get(residual_m, Fraction(0))
            assert p_nm >= rhs
            checks += 1

    total_checks += checks
    print(
        f"law={law_id} mean={float(nu):.6g} forced_k={forced_k} "
        f"checks={checks} max_center_ratio={float(max_center_ratio):.12g} PASS"
    )

# Check the near-inverse cutoff algebra used in Section 7 of the report.
# A=min(1/Psi,n), K=A/log(e+A) has K*Psi -> 0 in both branches.
# Here we check the simpler deterministic inequalities on a finite grid.
import math

cutoff_checks = 0
for n in [10**3, 10**4, 10**5, 10**6]:
    for psi in [1/n**2, 1/n, 1/math.sqrt(n), 1/math.log(n)]:
        a = min(1/psi, n)
        k = a / math.log(math.e + a)
        if a == n:
            assert k * psi <= 1 / math.log(math.e + n) + 1e-15
        else:
            assert k * psi <= 1 / math.log(math.e + a) + 1e-15
        cutoff_checks += 1

print(f"total_exact_forced_atom_checks={total_checks}")
print(f"near_inverse_cutoff_checks={cutoff_checks} PASS")
print("ALL CHECKS PASSED")
