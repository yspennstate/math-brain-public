#!/usr/bin/env python3
"""Exact self-checks for the B9/B19/B2 sparse-defect run.

This is a self-check, not an independent audit and not a proof of the
asymptotic theorems.  It verifies the genuinely finite algebraic identities
used in the report with exact rational arithmetic:

1. local factor-table replica mismatches for one Ising edge and site fields;
2. the product-null Bernoulli-support mixture identity
      1 + chi^2 = (1 + p^2 t^2)^n;
3. the two-point heavy-tail support identity
      1 + chi^2 = 1 + eps^2((1+t^2)^n-1),
   equal to the exact pair-interface exponential moment.
"""

from fractions import Fraction
from itertools import product


def mean(values):
    values = list(values)
    return sum(values, Fraction(0, 1)) / len(values)


def subsets(n):
    return product([0, 1], repeat=n)


def check_local_tables():
    a = Fraction(1, 5)
    t = Fraction(1, 7)
    states = list(product([-1, 1], repeat=2))

    ev1 = mean(a * xi for xi, xj in states)
    ev2 = mean(2 * a * xi + a * a for xi, xj in states)
    eu = mean(t * xi * xj for xi, xj in states)
    euv1 = mean((t * xi * xj) * (a * xi) for xi, xj in states)
    euv2 = mean((t * xi * xj) * (2 * a * xi + a * a) for xi, xj in states)

    delta1 = ev2 - 2 * ev1
    delta2 = (euv2 - eu * ev2) - 2 * (euv1 - eu * ev1)
    bridge3 = mean((a * xi) * (t * xi * xj) * (a * xj) for xi, xj in states)

    assert delta1 == a * a
    assert delta2 == 0
    assert bridge3 == a * a * t
    return delta1, delta2, bridge3


def check_bernoulli_support(n=4, p=Fraction(1, 3), t=Fraction(1, 5)):
    xs = list(product([-1, 1], repeat=n))
    ss = list(subsets(n))

    def prob_s(s):
        k = sum(s)
        return p ** k * (1 - p) ** (n - k)

    def l_s(x, s):
        out = Fraction(1, 1)
        for i, bit in enumerate(s):
            if bit:
                out *= 1 + t * x[i]
        return out

    e_l2 = Fraction(0, 1)
    for x in xs:
        l_mix = sum((prob_s(s) * l_s(x, s) for s in ss), Fraction(0, 1))
        e_l2 += l_mix * l_mix
    e_l2 /= len(xs)

    closed = (1 + p * p * t * t) ** n
    pair_interface_mgf = closed  # |S cap T| ~ Bin(n,p^2)
    assert e_l2 == closed == pair_interface_mgf
    return e_l2


def check_heavy_tail_support(n=5, eps=Fraction(1, 3), t=Fraction(1, 5)):
    xs = list(product([-1, 1], repeat=n))

    def l_full(x):
        out = Fraction(1, 1)
        for xi in x:
            out *= 1 + t * xi
        return out

    e_l2 = Fraction(0, 1)
    for x in xs:
        l_mix = (1 - eps) + eps * l_full(x)
        e_l2 += l_mix * l_mix
    e_l2 /= len(xs)

    closed = 1 + eps * eps * ((1 + t * t) ** n - 1)
    # Pair interface is V iff both latent supports are V, probability eps^2.
    pair_interface_mgf = (1 - eps * eps) + eps * eps * (1 + t * t) ** n
    assert e_l2 == closed == pair_interface_mgf
    return e_l2


def main():
    d1, d2, d3 = check_local_tables()
    sparse = check_bernoulli_support()
    heavy = check_heavy_tail_support()
    print("ALL_EXACT_CHECKS_PASS")
    print(f"local_delta1={d1}")
    print(f"local_delta2={d2}")
    print(f"local_bridge3={d3}")
    print(f"bernoulli_support_1_plus_chi2={sparse}")
    print(f"heavy_tail_1_plus_chi2={heavy}")


if __name__ == "__main__":
    main()
