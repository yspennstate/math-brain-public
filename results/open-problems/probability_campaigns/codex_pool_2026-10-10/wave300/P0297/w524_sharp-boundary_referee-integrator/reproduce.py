"""Small exact-arithmetic checks supplementing, not replacing, the written audit."""
from fractions import Fraction as F

checks = 0
for gamma in (F(1, 2), F(1), F(3, 2)):
    q = 2 / gamma + gamma / 2
    xi = F(1)
    assert q > 2
    for alpha in (F(-2), F(-1), F(0), gamma, F(2)):
        value = (2 - alpha * alpha / 2) / (xi * (q - alpha))
        deficit = (alpha - gamma) ** 2 / (2 * xi * (q - alpha))
        assert gamma / xi - value == deficit
        checks += 1

# Brownian-map anchor gamma^2=8/3 and D=4.
g2 = F(8, 3)
D = F(4)
archived = (1 + 4 / g2) * D
corrected = D
assert archived == 10 and corrected == 4

# The proposed all-dependent-set KPZ equality at gamma-thick points.
actual_euclidean = 2 - g2 / 2
false_prediction = F(2)
assert actual_euclidean == F(2, 3)
assert false_prediction - actual_euclidean == F(4, 3)

print(f"L1 exact rational checks={checks}/15")
print(f"D0049 at Brownian anchor: archived={archived}, corrected={corrected}, error {archived-D}->0")
print(f"dependent-set KPZ at anchor: actual={actual_euclidean}, false prediction={false_prediction}, gap={false_prediction-actual_euclidean}")
