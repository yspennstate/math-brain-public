"""Exact symbolic self-check for the finite algebra in the HARD7-02
Campbell--O'Rourke Q1.9 Pareto-envelope run.

This is a self-check only, not an independent proof audit.
"""
import sympy as sp

alpha, p, delta, rho = sp.symbols("alpha p delta rho", positive=True)
beta = alpha / 2
q = p / 2

C_beta = 2 + 2**beta + 2**beta / (1 - beta)
D_alpha = sp.simplify(C_beta + 1 + C_beta / (1 - beta))
B_alpha = sp.simplify(D_alpha / alpha)

checks = {}
checks["q_over_beta_minus_q"] = sp.simplify(
    q / (beta - q) - p / (alpha - p)
)
checks["two_one_minus_beta"] = sp.simplify(
    2 * (1 - beta) - (2 - alpha)
)

c_delta = sp.sqrt(delta) * sp.exp(-2 * alpha - sp.Rational(1, 2))
P_delta = rho * c_delta**alpha / 2
P_delta_expected = (
    rho
    * delta ** (alpha / 2)
    * sp.exp(-2 * alpha**2 - alpha / 2)
    / 2
)
checks["sector_potential_constant"] = sp.simplify(
    P_delta / P_delta_expected - 1
)

M_bound = 1 + q * C_beta / (beta - q)
M_bound_expected = 1 + p * C_beta / (alpha - p)
checks["moment_bound_identity"] = sp.simplify(M_bound - M_bound_expected)

for name, value in checks.items():
    print(f"{name} = {value}")
print("C_beta =", C_beta)
print("D_alpha =", D_alpha)
print("B_alpha =", B_alpha)
print("P_delta =", P_delta_expected)
print("ALL_EXACT_CHECKS_PASS =", all(value == 0 for value in checks.values()))
