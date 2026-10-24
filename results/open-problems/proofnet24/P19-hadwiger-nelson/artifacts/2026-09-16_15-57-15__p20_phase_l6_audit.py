from fractions import Fraction
from math import factorial

# Independent exact-arithmetic audit of P20-I0081-PHASE-L6-02.
# Peer source: proofnet24/P20-closure-log-unimodality/runs/2026-09-16/
# 2026-09-16_15-39-02__run-report.md, creation commit
# 441634a43e2e7abcafe7ae552b457353152f8548, blob
# bbc3f5de3f174cff8cf47197a214542ab6c98488.
# It uses e > sum_{n=0}^5 1/n! = 163/60 and then
# (163/60)^6 > 400 to obtain e^{-L}<1/400 for L>=6.
s = sum(Fraction(1, factorial(n)) for n in range(6))
assert s == Fraction(163, 60)
gap_num = 163**6 - 400*60**6
assert gap_num == 92969578009 and gap_num > 0
lower = Fraction(399,401)
derivative_lower = 6*lower - 1
assert derivative_lower == Fraction(1993,401) and derivative_lower > 0
print('partial_sum', s)
print('integer_gap', gap_num)
print('poisson_lower', lower)
print('derivative_lower', derivative_lower)
print('VERDICT PASS: exact arithmetic in P20-I0081-PHASE-L6-02 checks out')
