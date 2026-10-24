from fractions import Fraction

# P26 independent exact finite-core check for R07/I0077 theorem T14.
# This script certifies only the rational arithmetic and interval relations
# in the canonical disconnected-fan example. Analytic OU/FBM facts are
# proved or cited in the P26 run report.

A = Fraction(5, 1)
ou_potential_lower = A * A / Fraction(8, 1) - Fraction(1, 4)
critical = Fraction(1, 1)
gap = ou_potential_lower - critical

assert ou_potential_lower == Fraction(23, 8)
assert gap == Fraction(15, 8)
assert ou_potential_lower > critical

left = (Fraction(-6), Fraction(-5))
right = (Fraction(5), Fraction(6))
assert left[1] < right[0]
assert right[0] == A
assert min(abs(left[0]), abs(left[1])) == A

hull = (Fraction(-6), Fraction(6))
critical_interval = (Fraction(-1), Fraction(1))
assert hull[0] < critical_interval[0] < critical_interval[1] < hull[1]

# Asymmetric stress test used in the audit diagnosis:
# [-2,2] strictly contains [-1,1] (source strict monotonicity then gives
# lambda_0(-2,2)<1), whereas [5,6] has the exact lower bound 23/8>1.
wide = (Fraction(-2), Fraction(2))
assert wide[0] < critical_interval[0] < critical_interval[1] < wide[1]
assert right[0] > wide[1]

print("P26-I0077-T14-INDEPENDENT-EXACT-AUDIT: PASS")
print(f"far_component_OU_lower_bound={ou_potential_lower}")
print(f"gap_above_critical_1={gap}")
print(f"canonical_gap={right[0] - left[1]}")
print("convex_hull_strictly_contains_critical_interval=True")
print("asymmetric_stress_test_exact_geometry=True")
print("NOTE: checker certifies finite rational arithmetic/interval relations only;")
print("      OU continuity/strict monotonicity and FBM Theorem 4.3 are analytic source facts.")
print("END P26-I0077-T14-INDEPENDENT-EXACT-AUDIT")
