"""Independent exact arithmetic for the two-row, two-site w448 claim."""
from fractions import Fraction as F

A = (F(7, 10), F(1, 10), F(1, 10), F(1, 10))
B = (F(1, 10), F(7, 10), F(1, 10), F(1, 10))
rows = (A, B)
a = F(11, 20)
weights = (a, 1 - a)

g = F(0)
gd = F(0)
for i, origin in enumerate(rows):
    for j, left in enumerate(rows):
        mass = weights[i] * weights[j]
        visits = 1 / (1 - origin[1] * left[0])
        g += mass * visits
        gd += mass * visits * (origin[0] - origin[1])

raw_drift = sum(weights[i] * (row[0] - row[1]) for i, row in enumerate(rows))
aux_drift = gd / g
assert raw_drift == F(3, 50), raw_drift
assert g == F(2021, 1581), g
assert gd == F(-202, 2635), gd
assert aux_drift == F(-606, 10105), aux_drift

a2 = F(9, 10)
delta = F(3, 5) * (a2 - 7 * (1 - a2)) / (a2 + 7 * (1 - a2))
assert delta == F(3, 40), delta

print(f"raw_drift={raw_drift}; E_G={g}; E_Gd={gd}; auxiliary_drift={aux_drift}; delta_9_10={delta}")
