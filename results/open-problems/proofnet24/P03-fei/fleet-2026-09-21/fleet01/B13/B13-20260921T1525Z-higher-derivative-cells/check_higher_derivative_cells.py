from fractions import Fraction
import math
import json


def check_cluster(n: int, L: int):
    # Abstract law from the previous B13 report:
    # (1-1/L) delta_empty + (1/L) Unif{|S|=L}.
    # For a fixed pair A, p_A=(L-1)/(n(n-1)); conditional on A subset X,
    # |X\A|=L-2 deterministically.
    k = 2
    p = Fraction(L - 1, n * (n - 1))
    effective = 4 * p  # 4^(k-1) p_A
    required = 0.5 * math.log(1 / float(effective))
    actual = L - k
    return {
        "n": n,
        "L": L,
        "p_pair_exact": f"{p.numerator}/{p.denominator}",
        "effective_4p": float(effective),
        "actual_outside_mean": actual,
        "required_outside_mean": required,
        "violation_gap": required - actual,
        "violates": actual + 1e-12 < required,
    }


main = check_cluster(4096, 7)
assert main["p_pair_exact"] == "1/2795520"
assert main["violates"]

family = []
for r in range(2, 21):
    n = 2 ** (2 * r)
    L = r + 1
    row = check_cluster(n, L)
    assert row["violates"], row
    family.append({"r": r, "n": n, "L": L, "gap": row["violation_gap"]})

print(json.dumps({"status": "PASS", "main": main, "dyadic_family": family}, indent=2, sort_keys=True))
