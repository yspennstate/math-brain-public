from fractions import Fraction

# Arithmetic-only sanity check for the analytic three-dimensional MUX tube.
# This does not replace the proof of the source-potential derivative bounds or
# the Fannes-Audenaert continuity estimate in REPORT.md.

eps = Fraction(1, 2**14)
l1_bound = 7 * eps + 16 * eps * eps
tv_bound = l1_bound / 2
assert tv_bound < 4 * eps
assert 4 * eps == Fraction(1, 4096)
assert 15 * 4096 < 2**16

# REPORT.md derives a total perturbation loss < 238 eps from the exact MUX
# formula, the h96 source slope bound, and entropy continuity.
loss = 238 * eps
line_reserve = Fraction(1, 64)
margin = line_reserve - loss
assert margin == Fraction(9, 8192)
assert margin > Fraction(1, 1000)

print(f"eps={eps} = {float(eps):.12g}")
print(f"l1_bound={l1_bound} = {float(l1_bound):.12g}")
print(f"tv_bound={tv_bound} < 4eps={4*eps}")
print(f"fannes_log_check: 15*4096={15*4096} < 2^16={2**16}")
print(f"loss_bound=238eps={loss} = {float(loss):.12g}")
print(f"line_reserve=1/64={float(line_reserve):.12g}")
print(f"certified_margin={margin} = {float(margin):.12g}")
print("PASS")
