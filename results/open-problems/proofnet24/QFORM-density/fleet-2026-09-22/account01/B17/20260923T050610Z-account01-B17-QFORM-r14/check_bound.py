from math import pi, sqrt

# Elementary envelope from the proof.
B0 = 2*pi*(1 - 1/sqrt(3) + 1/(3*sqrt(2)))
rational = 5148/1225
sharp_obstruction = 3*sqrt(2)

assert B0 < rational < sharp_obstruction
assert 5148**2 < 18 * 1225**2

# Rational ingredients used in the paper proof.
assert 3 < (7/4)**2                 # sqrt(3) < 7/4, hence 1/sqrt(3) > 4/7
assert 25**2 < 18**2 * 2            # 25 < 18 sqrt(2), hence 1/(3sqrt(2)) < 6/25

print(f"B0={B0:.15f}")
print(f"rational_certificate={rational:.15f}")
print(f"3sqrt2={sharp_obstruction:.15f}")
print(f"gap_3sqrt2_minus_B0={sharp_obstruction-B0:.15f}")
print("square_certificate:", 5148**2, "<", 18*1225**2)
print("PASS")
