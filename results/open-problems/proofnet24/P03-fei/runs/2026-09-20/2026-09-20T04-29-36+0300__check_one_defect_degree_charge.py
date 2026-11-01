import math
import json
from fractions import Fraction


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def one_defect_values(n):
    return [-1] + [1] * ((1 << n) - 1)


def spectral_probs(n):
    vals = one_defect_values(n)
    nums = fwht(vals)
    den = 1 << n
    return [Fraction(z * z, den * den) for z in nums]


def brute_influence(n, i):
    vals = one_defect_values(n)
    N = 1 << n
    return Fraction(sum(vals[x] != vals[x ^ (1 << i)] for x in range(N)), N)


def brute_B(n, i):
    probs = spectral_probs(n)
    bit = 1 << i
    total = 0.0
    for t in range(1 << n):
        if t & bit:
            continue
        a = float(probs[t])
        b = float(probs[t | bit])
        mass = a + b
        if mass:
            total += mass * h2(b / mass)
    return total


def p_m(m):
    return Fraction(1, 1 << (m - 1))


def B_formula(m):
    p = 2.0 ** (1 - m)
    A = (1.0 - p) ** 2
    q = p * p
    mass = A + q
    return 2.0 * p * (1.0 - p) + (mass * h2(q / mass) if mass else 0.0)


def total_influence(n):
    return Fraction(n, 1 << (n - 1))


def degree_charge(n):
    if n <= 1:
        return Fraction(0, 1)
    return Fraction(n * (n - 1), 2) * Fraction(1, 1 << (n - 1))


def R_formula(n):
    return sum(2.0 ** (-(n - m)) * B_formula(m) for m in range(1, n + 1))


max_influence_error = 0.0
max_B_error = 0.0
max_B_le_4p_violation = -1e100
rows = []

for n in range(1, 9):
    probs = spectral_probs(n)
    p = float(p_m(n))
    expected0 = Fraction((2 ** n - 2) ** 2, 2 ** (2 * n))
    expected_nonzero = Fraction(4, 2 ** (2 * n))
    assert probs[0] == expected0
    assert all(probs[s] == expected_nonzero for s in range(1, 1 << n))

    for i in range(n):
        max_influence_error = max(
            max_influence_error, abs(float(brute_influence(n, i) - p_m(n)))
        )
        max_B_error = max(max_B_error, abs(brute_B(n, i) - B_formula(n)))

    if n >= 2:
        max_B_le_4p_violation = max(
            max_B_le_4p_violation, B_formula(n) / (4.0 * p) - 1.0
        )

    I = float(total_influence(n))
    D = float(degree_charge(n))
    R = R_formula(n)
    rows.append({
        "n": n,
        "I": I,
        "D_degree_over_I": D / I,
        "expected_D_ratio": (n - 1) / 2.0,
        "R_over_I": R / I,
        "B_over_influence_at_root": B_formula(n) / p,
    })

large_n = {}
for n in [16, 32, 64, 128, 256, 512, 1024]:
    large_n[str(n)] = {
        "D_degree_over_I": float(degree_charge(n) / total_influence(n)),
        "R_over_I": R_formula(n) / float(total_influence(n)),
    }

assert max_influence_error == 0.0
assert max_B_error < 1e-12
assert max_B_le_4p_violation <= 1e-12
assert all(abs(r["D_degree_over_I"] - r["expected_D_ratio"]) < 1e-15 for r in rows)
assert all(r["R_over_I"] < 4.0 for r in rows)

out = {
    "status": "PASS",
    "family": "one-defect / OR-type f_n(0)=-1, f_n(x)=+1 otherwise",
    "exhaustive_bruteforce_dimensions": "1..8",
    "max_influence_formula_error": max_influence_error,
    "max_B_formula_error": max_B_error,
    "max_violation_B_le_4p": max_B_le_4p_violation,
    "rows": rows,
    "large_n": large_n,
    "identities_checked": [
        "Fourier squared law: p_empty=(1-2^(1-n))^2 and p_S=4^(1-n) for S!=empty",
        "Inf_i=2^(1-n)",
        "B_i exact pair formula",
        "D_degree/I=(n-1)/2 for every full adaptive tree",
        "R/I<4 from exact formula",
    ],
}

print(json.dumps(out, indent=2, sort_keys=True))
