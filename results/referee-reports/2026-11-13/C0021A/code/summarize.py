#!/usr/bin/env python3
"""Recompute bound conversions, fits, and restriction-state counts."""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
import json
import math
from pathlib import Path

getcontext().prec = 55


def sigma_for_base(base):
    x = Decimal(base.numerator)/Decimal(base.denominator)
    return str((Decimal(3)/x).ln()/Decimal(3).ln())


def main():
    rows = json.loads(Path("data/exact_results.json").read_text())["results"]
    finite = []
    for row in rows[1:]:
        k = row["k"]
        c = Q(row["cost"])
        delta = c/3**k
        decimal_delta = Decimal(delta.numerator)/Decimal(delta.denominator)
        sigma = -decimal_delta.ln()/Decimal(3).ln()/k
        assert abs(float(sigma)-row["effective_sigma"]) < 1e-14
        finite.append(dict(k=k, cost=str(c), delta=str(delta), sigma=str(sigma)))
    # Least-squares slope with a free intercept for three equally spaced k's.
    fit = (Decimal(finite[2]["sigma"])*3-Decimal(finite[0]["sigma"]))/2
    state_counts = [3]
    for _ in range(4):
        old = state_counts[-1]
        state_counts.append(math.comb(old+2, 3)-2*old+2)
    lam = Q(246003, 100000)
    # Rational isolation of the positive root in the simple MNS recurrence.
    polynomial = lambda x: 32*x**3-47*x**2-78*x-2
    left, right = Q(24670436373266, 10**13), Q(24670436373268, 10**13)
    assert polynomial(left) < 0 < polynomial(right)
    result = dict(
        certified_lambda=str(lam), sigma_lower=sigma_for_base(lam),
        sigma_upper=sigma_for_base(Q(9, 4)),
        directional_sigma=sigma_for_base(Q(5, 2)),
        osss_sigma_upper=sigma_for_base(Q(2)),
        schramm_steif_sufficient_noise_exponent=str(Decimal(sigma_for_base(lam))/2),
        finite=finite, descriptive_three_point_fit_sigma=str(fit),
        fixed_tree_state_counts=state_counts,
        simple_interleaving_root_interval=[str(left), str(right)],
        simple_interleaving_sigma_interval=[sigma_for_base(right), sigma_for_base(left)],
    )
    # Two independent influence computations: direct truth-table flips and
    # the chain/Russo formula (3/2)**k.
    influence_checks = []
    for k in (1, 2):
        n = 3**k
        def f(x):
            a = [(x >> i) & 1 for i in range(n)]
            while len(a) > 1:
                a = [int(sum(a[i:i+3]) >= 2) for i in range(0, len(a), 3)]
            return a[0]
        table = [f(x) for x in range(1 << n)]
        influences = [Q(sum(table[x] != table[x ^ (1 << i)] for x in range(1 << n)),
                          1 << n) for i in range(n)]
        assert influences == [Q(1, 2**k)]*n
        assert sum(influences) == Q(3, 2)**k
        influence_checks.append(dict(k=k, each=str(influences[0]), total=str(sum(influences))))
    result["influence_truth_table_checks"] = influence_checks
    Path("data/summary.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
