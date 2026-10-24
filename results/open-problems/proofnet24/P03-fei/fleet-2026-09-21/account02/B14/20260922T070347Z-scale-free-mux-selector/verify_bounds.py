from fractions import Fraction as F

# Exact rational bookkeeping for REPORT.md, Sections 5--7.
invln2 = F(10_000_000, 6_931_471)
G1 = F(16137, 1250)                 # 12.9096
a = F(33_525_607, 125_000_000)     # 0.268204856

# Selector-local derivative envelope in (5.2).
dx = invln2 / 231
derivative_envelope = G1 + 31*dx + 31*invln2 + a/F(232, 1)
assert derivative_envelope < 58

# Final adverse ledger in (7.4).
potential_cost = F(58,464) + F(160,224*464)
entropy_cost = F(35,107648) + F(26,224*464) + F(1601,100*464*464)
margin = F(13,100) - potential_cost - entropy_cost
assert margin == F(423629,150707200)
assert margin > F(1,400)

print("selector_derivative_envelope", float(derivative_envelope), derivative_envelope)
print("potential_cost", float(potential_cost), potential_cost)
print("entropy_cost", float(entropy_cost), entropy_cost)
print("remaining_margin", float(margin), margin)
print("margin_minus_1_over_400", float(margin-F(1,400)), margin-F(1,400))
print("PASS")
