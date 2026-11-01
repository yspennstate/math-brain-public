#!/usr/bin/env python3
"""Deterministic arithmetic checks for B15 Gibbs-KL prime-tube report.

This checker verifies only the displayed numerical inequalities.  The Gibbs-KL
factorization, packet/price sufficiency, and five-bit entropy perturbation bound
are analytic statements proved in REPORT.md.  The strict central gap is sourced
from fleet01/B17 and fleet03/B18; we deliberately use the weaker floor
0.0049065 below.
"""
from decimal import Decimal, getcontext

getcontext().prec = 50

eps = Decimal("0.0000044")
delta5 = Decimal("0.0049065")
qmax = Decimal(144) * eps * eps
zmax = Decimal(4) * eps * eps
cost = Decimal(1106) * eps + Decimal(6480) * eps * eps
gap = delta5 - cost
out_min = Decimal(1) / Decimal(32) - Decimal(5) * eps

# e < 3.  These inequalities imply
# log_2(e/qmax) < 31 and log_2(e/zmax) < 36.
assert (Decimal(2) ** 31) * qmax > 3
assert (Decimal(2) ** 36) * zmax > 3
assert out_min > Decimal(1) / Decimal(64)
assert cost < delta5

print("PASS")
print("epsilon", eps)
print("delta5_floor", delta5)
print("qmax", qmax)
print("zmax", zmax)
print("q_log_condition_2^31_q_gt_3", (Decimal(2) ** 31) * qmax)
print("z_log_condition_2^36_z_gt_3", (Decimal(2) ** 36) * zmax)
print("cost_bound", cost)
print("residual_gap", gap)
print("output_min_smaller_rep", out_min)
print("one_over_64", Decimal(1) / Decimal(64))
