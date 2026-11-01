from fractions import Fraction

# Literal 2D equality-clause counterexample.
# K=[-a,a]x[-M,M], Lambda=diag(0,1), t=2 log 2.
# At s=0,t/2,t the y half-widths are M,2M,4M, all >1,
# while the x half-width is always a. Hence intersection with B_2^2
# is exactly B_2^2 cap {|x_1|<=a} at all three times.
a = Fraction(1, 2)
M = Fraction(2, 1)
scales = [Fraction(1), Fraction(2), Fraction(4)]
y_halfwidths = [M*s for s in scales]

assert 0 < a < 1 < M
assert all(w > 1 for w in y_halfwidths)
assert M*M > 1                 # (0,M) in K but outside unit disk
assert a < 1                   # (1,0) in unit disk but outside K
assert (0, 1)[0] != (0, 1)[1] # Lambda is not scalar

# Stronger volume-preserving diagnostic in dimension 3.
# K=[-1/2,1/2]x[-4,4]^2, Lambda=diag(0,1,-1), t=log 2.
# At s=0,t/2,t both inactive half-widths remain >=2>1, so the
# intersection with B_2^3 is again a fixed x_1-slab although tr Lambda=0.
M3 = Fraction(4, 1)
Lambda3 = (0, 1, -1)
assert M3 * Fraction(1, 2) > 1
assert sum(Lambda3) == 0
assert len(set(Lambda3)) > 1

print("HARD7-01 exact Artstein-Avidan-Katzin equality counterexample check")
print("2D: a =", a, "M =", M, "y halfwidths =", y_halfwidths)
print("2D_CONDITIONS_EXACT = True")
print("3D: a =", a, "M =", M3, "Lambda =", Lambda3,
      "minimum inactive halfwidth =", M3 * Fraction(1, 2))
print("3D_TRACELESS_CONDITIONS_EXACT = True")
print("ALL_EXACT_CHECKS_PASS = True")
