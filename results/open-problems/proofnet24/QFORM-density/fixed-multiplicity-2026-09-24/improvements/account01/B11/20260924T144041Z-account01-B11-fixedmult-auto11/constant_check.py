#!/usr/bin/env python3
"""Exact-rational certificates for account01/B11 auto11's <2547 constant.
Standard-library only. This checks arithmetic certificates; it is not a proof
of the analytic lemmas recorded in IMPROVEMENT.md.
"""
from fractions import Fraction as F
from math import factorial
import json

# Gamma(3/8): degree-6 alternating upper polynomial on [0,1], plus
a = F(3, 8)
gamma01 = sum((F((-1)**k, factorial(k)) / (a + k) for k in range(7)), F(0))
# tail <= e^-1 < 46/125, since e > sum_{k=0}^6 1/k! = 1957/720 > 125/46
e_partial = sum((F(1, factorial(k)) for k in range(7)), F(0))
assert e_partial > F(125, 46)
gamma_upper = gamma01 + F(46, 125)
assert gamma_upper < F(2477, 1000)

# Prefactor 2^(5/8) pi^(-1/4) e^(3/8) < 169/100.
assert F(1543, 1000) ** 8 > 32
# Use classical pi > 223/71 > 313/100.
assert F(223, 71) > F(313, 100)
assert F(94, 125) ** 4 * F(313, 100) > 1
x = F(3, 8)
S4 = sum((x**k / factorial(k) for k in range(5)), F(0))
t5 = x**5 / factorial(5)
exp38_upper = S4 + t5 / (1 - F(1, 16))
assert exp38_upper == F(1191929, 819200)
assert exp38_upper < F(291, 200)
prefactor_upper = F(1543, 1000) * F(94, 125) * F(291, 200)
assert prefactor_upper < F(169, 100)
Cq_upper = F(169, 100) * F(2477, 1000)
assert Cq_upper == F(418613, 100000)

# Log certificates: if a positive Taylor partial sum for exp(q) exceeds y,
# then log(y)<q.
q2 = F(1733, 2500)
exp_q2_partial = sum((q2**k / factorial(k) for k in range(7)), F(0))
assert exp_q2_partial > 2
qC = F(143179, 100000)
exp_qC_partial = sum((qC**k / factorial(k) for k in range(10)), F(0))
assert exp_qC_partial > Cq_upper

# pi < 22/7; combine all upper bounds in the scalar-pivot ledger.
bracket_upper = F(22, 7) + 4*q2 + 8 + 8*qC
normalized_density_upper = 100*bracket_upper + 10
assert normalized_density_upper == F(2228623, 875)
assert normalized_density_upper < 2547

out = {
    "status": "PASS",
    "gamma_01_upper": str(gamma01),
    "gamma_total_upper": str(gamma_upper),
    "gamma_margin_to_2477_1000": str(F(2477,1000)-gamma_upper),
    "pow2_eighth_margin": str(F(1543,1000)**8-32),
    "pi_inverse_fourth_certificate_margin": str(F(94,125)**4*F(313,100)-1),
    "exp_3_8_upper_margin_to_291_200": str(F(291,200)-exp38_upper),
    "prefactor_upper": str(prefactor_upper),
    "prefactor_margin_to_169_100": str(F(169,100)-prefactor_upper),
    "Cq_upper": str(Cq_upper),
    "log2_exp_partial_margin": str(exp_q2_partial-2),
    "logC_exp_partial_margin": str(exp_qC_partial-Cq_upper),
    "bracket_upper": str(bracket_upper),
    "normalized_density_upper": str(normalized_density_upper),
    "margin_to_2547": str(F(2547)-normalized_density_upper),
    "limitations": [
        "Arithmetic certificate only; analytic inequalities are proved in IMPROVEMENT.md.",
        "Uses the classical Archimedean bounds 223/71 < pi < 22/7."
    ]
}
print(json.dumps(out, indent=2))
