"""Print the rows of Tables 1-3 of the paper from the closed form and the result files.
The lower bounds on F/(tau_2 Delta) in Table 3 are rounded down to three decimals."""
import csv
import math
from fractions import Fraction


def V3(s):
    return Fraction((s + 2) * (5 * s**3 + 19 * s**2 + 13 * s + 8), (s + 3) * (s + 4) * (s * s + s + 1))


def rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


print("% Table 1, closed-form columns (the linear-program column comes from sanity_checks.py)")
for s in [2, 3, 4, 5, 7, 37, 41, 49]:
    tau = (s + 2) / (s + 2 - math.sqrt(s))
    v = V3(s)
    print(f"{s} & {2 * (s * s + s + 1) + 1} & ${v.numerator}/{v.denominator}$ & {tau:.6f} & {float(v) / (2 * tau):.4f}\\\\")

print("% Table 2")
for r in rows("rr_lp_results.csv"):
    print(f"{r['d']} & {r['n']} & {float(r['mu2']):.4f} & {float(r['tau2']):.4f} & {r['diam_H']} & "
          f"{float(r['best_certificate']):.4f} & {r['r']} & {float(r['F_LP']):.4f} & {float(r['hub_bound']):.4f} & "
          f"{float(r['F_over_tau2_Delta']):.3f} & {float(r['d_plus_1_minus_mu2']):.3f}\\\\")

print("% Table 3")
for r in rows("rr_dual_large_results.csv"):
    print(f"random & {r['n']} & {r['d']} & {float(r['mu2']):.4f} & {float(r['tau2']):.4f} & {r['diam_H']} & "
          f"{float(r['best_certificate']):.4f} & {r['r']} & {float(r['hub_bound']):.4f} & "
          f"{math.floor(float(r['ratio_lower_bound']) * 1000) / 1000:.3f} & {float(r['d_plus_1_minus_mu2']):.3f}\\\\")
for r in rows("lps_results.csv"):
    print(f"$X^{{{r['p']},{r['q']}}}$ & {r['n']} & {r['d']} & {float(r['mu2']):.4f} & {float(r['tau2']):.4f} & {r['diam_H']} & "
          f"{float(r['best_certificate']):.4f} & {r['r']} & {float(r['hub_bound']):.4f} & "
          f"{math.floor(float(r['ratio_lower_bound']) * 1000) / 1000:.3f} & {float(r['d_plus_1_minus_mu2']):.3f}\\\\")
