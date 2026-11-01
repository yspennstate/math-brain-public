from fractions import Fraction

# Independent exact audit of P20-D0010-CANONICAL-LAYER-FAILURE-04.
# F_* = (5/6) U[0,3/5] + (1/6) U[0,1].

w1 = Fraction(5, 6)
w2 = Fraction(1, 6)
L1 = Fraction(3, 5)
L2 = Fraction(1, 1)

# Density on [0,3/5] and on (3/5,1].
f_left = w1 / L1 + w2 / L2
f_right = w2 / L2
assert f_left == Fraction(14, 9)
assert f_right == Fraction(1, 6)
assert f_left > f_right

# Mean is the tight n=3 lower moderate-mean boundary 1/3.
mean = w1 * L1 / 2 + w2 * L2 / 2
assert mean == Fraction(1, 3)

# Canonical anchored labels have only lengths 3/5 and 1.
# A common-center triple at sum 1 would need total length 2.
possible_sums = []
for k in range(4):
    s = (3-k) * L1 + k * L2
    possible_sums.append(s)
    assert s != 2

assert possible_sums == [Fraction(9,5), Fraction(11,5), Fraction(13,5), Fraction(3,1)]

print("P11 independent audit of P20-D0010-CANONICAL-LAYER-FAILURE-04: PASS")
print("density_left=14/9 density_right=1/6 mean=1/3")
print("possible canonical triple length sums:", ", ".join(str(x) for x in possible_sums))
print("none equals 2, so no canonical supported tuple has common center 1")
print("External dependency checked separately: Wang-Wang 2011 monotone-density + moderate-mean complete-mixability theorem.")
