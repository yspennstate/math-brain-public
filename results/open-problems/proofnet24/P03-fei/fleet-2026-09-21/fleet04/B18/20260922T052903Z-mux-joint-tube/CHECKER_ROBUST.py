from fractions import Fraction as F

# Addendum arithmetic only: the analytic inequalities are proved in the text.
loss = F(259, 524288)
assert loss < F(1, 2000)
reserve_gap = F(89, 4096) - F(1, 2000) - F(1, 48)
assert reserve_gap == F(607, 1536000)
assert reserve_gap > 0
print("PASS")
print("robust_loss_bound", f"{loss.numerator}/{loss.denominator}", float(loss))
print("robust_loss_target", "1/2000", float(F(1, 2000)))
print("reserve_gap_over_1_48", f"{reserve_gap.numerator}/{reserve_gap.denominator}", float(reserve_gap))
