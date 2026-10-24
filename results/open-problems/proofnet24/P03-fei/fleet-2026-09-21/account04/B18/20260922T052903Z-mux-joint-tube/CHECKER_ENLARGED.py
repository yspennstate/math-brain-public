from fractions import Fraction as F

loss = F(117, 8192)
base = F(89, 4096)
remaining = base - loss
assert remaining == F(61, 8192)
assert remaining > F(1, 135)
gap = remaining - F(1, 135)
assert gap == F(43, 1105920)

a = F(33525607, 125000000)  # 0.268204856
margin_upper = a - F(16, 1215)
assert margin_upper < a

print("PASS")
print("loss_bound", f"{loss.numerator}/{loss.denominator}", float(loss))
print("remaining_reserve", f"{remaining.numerator}/{remaining.denominator}", float(remaining))
print("gap_over_1_135", f"{gap.numerator}/{gap.denominator}", float(gap))
print("margin_upper_exact", f"{margin_upper.numerator}/{margin_upper.denominator}")
print("margin_upper_decimal", float(margin_upper))
