#!/usr/bin/env python3
"""Targeted exact-family checks for the B17 C-Holevo FEI route.

This is deliberately not an exhaustive Boolean sweep.  It evaluates the closed
four-sine diagonal kernel on an explicit admissible Boolean family and checks
boundary cases used in the analytic report.
"""
import math


def F(x: float) -> float:
    return 0.0 if x == 0.0 else x * x * math.log(abs(x))


def kdiag(a: float, b: float) -> float:
    return 0.25 * (F(a - b) + F(a + b) - 2.0 * F(a) - 2.0 * F(b))


def bent_one_point_row(n: int):
    assert n % 2 == 0 and n >= 2
    N = 2**n
    root = math.sqrt(N)
    n_plus = (N + root) / 2.0
    n_minus = (N - root) / 2.0
    # b_r=1/N.  The bent twist has Walsh values +/-1/sqrt(N), with
    # counts forced by h(0)=1.  Homogeneity of K gives the expression below.
    G = (n_plus * kdiag(root - 1.0, 1.0)
         + n_minus * kdiag(root + 1.0, 1.0)) / (N * N)
    min_square_bank = 1.0 / N
    influence = 2.0 * n / N
    return N, G, G / min_square_bank, influence, G / influence


def main() -> None:
    dictator_G = 2.0 * kdiag(0.5, 0.5)
    assert abs(dictator_G - math.log(2.0) / 2.0) < 1e-14
    assert kdiag(1.0, 0.0) == 0.0

    print("B17 targeted admissible-Boolean checks: C-Holevo / diagonal Gram")
    print("natural logarithms; no exhaustive Boolean sweep")
    print()
    print(f"boundary dictator: G={dictator_G:.15g}, (ln 2)/2={math.log(2)/2:.15g}")
    print(f"constant f boundary: G={kdiag(1.0, 0.0):.15g}")
    print()
    print("one-point defect f_n plus explicit quadratic bent h_n")
    print(" n      N                  G_n        N*G_n          I(f_n)        G_n/I")
    for n in range(2, 22, 2):
        N, G, ratio, influence, gi = bent_one_point_row(n)
        print(f"{n:2d} {N:8d} {G:20.12e} {ratio:14.9f} {influence:14.8e} {gi:12.9f}")

    print()
    print("For n even, sum_r min(a_r^2,b_r^2)=1/N exactly.")
    print("Thus the displayed N*G_n is the ratio against the proposed scale-free min-square bank.")
    print("Asymptotic proved from the closed kernel: N*G_n=(1/4) ln N + O(1), so the ratio diverges.")
    print(f"Predicted limiting G_n/I(f_n)=ln(2)/8={math.log(2)/8:.12f}.")


if __name__ == "__main__":
    main()
