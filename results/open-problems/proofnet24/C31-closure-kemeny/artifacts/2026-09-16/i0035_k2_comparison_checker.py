#!/usr/bin/env python3
import sympy as sp

# Exact symbolic counterexample/extremizer check for the Aldous-Fill 14.31 source chain
# on K2, and for the Hartarsky-Martinelli-Toninelli CBSEP normalization.

theta, lam = sp.symbols('theta lambda', positive=True)
p = sp.factor(theta/(1+theta))

# States: 10, 01, 11. Source BAB rates: 10->11 theta, 01->11 theta,
# 11->10 1, 11->01 1.
Q_bab = sp.Matrix([
    [-theta, 0, theta],
    [0, -theta, theta],
    [1, 1, -2],
])
char_bab = sp.factor(Q_bab.charpoly(lam).as_expr())
assert char_bab == lam*(lam+theta)*(lam+theta+2)

# On K2 the single CBSEP edge is always nonempty and is resampled at rate one
# from Bernoulli(p)^2 conditioned on being nonempty.
weights = [
    sp.factor(p*(1-p)/(p*(2-p))),
    sp.factor(p*(1-p)/(p*(2-p))),
    sp.factor(p*p/(p*(2-p))),
]
assert weights == [1/(theta+2), 1/(theta+2), theta/(theta+2)]
Q_cb = sp.Matrix([
    [weights[j] if i != j else -(1-weights[i]) for j in range(3)]
    for i in range(3)
])
char_cb = sp.factor(Q_cb.charpoly(lam).as_expr())
assert char_cb == lam*(lam+1)**2

print('source_BAB_charpoly =', char_bab)
print('CBSEP_charpoly =', char_cb)
print('source_BAB_gap = theta')
print('CBSEP_gap = 1')
print('tau_BAB/tau_CBSEP = 1/theta')
print('therefore any universal B in tau_BAB <= (B/theta) tau_CBSEP satisfies B >= 1')
print('ALL_EXACT_CHECKS_PASS')
