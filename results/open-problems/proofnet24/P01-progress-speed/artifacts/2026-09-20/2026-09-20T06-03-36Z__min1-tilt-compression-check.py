from fractions import Fraction as F


def threshold(R):
    return R / (2 * R - 1)


def h(R, L):
    return (R - (2 * R - 1) * L) / (1 - L)


def derivative_margin(R, L):
    return 2 * h(R, L) / (R + L) ** 2


# Case A: minimum offspring 1, mean <= 3/2, L=7/10.
R = F(3, 2)
L = F(7, 10)
assert threshold(R) == F(3, 4)
assert h(R, L) == F(1, 3)
assert derivative_margin(R, L) == F(50, 363)
print("A mean<=3/2: threshold=", threshold(R), "h=", h(R, L),
      "margin=", derivative_margin(R, L))

# Case B: minimum offspring 1, branching probability p=P(nu>=2)<=1/100.
p = F(1, 100)
Rp = (1 + p) / (1 - p)
L = F(49, 50)
assert Rp == F(101, 99)
assert threshold(Rp) == F(101, 103)
assert h(Rp, L) == F(1, 33)
assert derivative_margin(Rp, L) == F(1485000, 98029801)
print("B p<=1/100: R=", Rp, "threshold=", threshold(Rp), "h=", h(Rp, L),
      "margin=", derivative_margin(Rp, L))

# Case C: exact law P(nu=1)=9/10, P(nu=10)=1/10.
p1 = F(9, 10)
p10 = F(1, 10)
mean = p1 + 10 * p10
A = p10 * F(9, 10)  # E[(nu-1)/nu]
B = p1 * F(1, 2) + p10 * F(1, 11)  # E[1/(nu+1)]
Rshape = 1 + A / B
Rp2 = (1 + p10) / (1 - p10)
Rmin = min(mean, Rp2, Rshape)
L = F(6, 7)
assert mean == F(19, 10)
assert Rp2 == F(11, 9)
assert Rshape == F(604, 505)
assert Rmin == Rshape
assert threshold(Rmin) == F(604, 703)
assert h(Rmin, L) == F(2, 101)
assert derivative_margin(Rmin, L) == F(123725, 13169641)
print("C {1,10} 9/10-1/10: mean=", mean, "Rp=", Rp2, "Rshape=", Rshape,
      "threshold=", threshold(Rmin), "h=", h(Rmin, L),
      "margin=", derivative_margin(Rmin, L))

print("ALL_EXACT_CHECKS_PASS")
