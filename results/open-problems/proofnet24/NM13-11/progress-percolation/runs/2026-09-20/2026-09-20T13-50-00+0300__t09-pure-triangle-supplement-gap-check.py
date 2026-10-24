from fractions import Fraction


def muC(p):
    return 2 * (p + p * p - p * p * p)


def fracstr(x):
    return f"{x.numerator}/{x.denominator}"


# Rational square-root upper bounds used below.
assert Fraction(49, 20) ** 2 > 6
assert Fraction(99, 70) ** 2 > 2

# Concrete b=1, N=4: degree 9.
p_c_test = Fraction(3, 20)
crit_margin = 3 * muC(p_c_test) - 1
assert crit_margin == Fraction(59, 4000) and crit_margin > 0
z = Fraction(125, 23)
assert z * z > 8
a_upper = Fraction(69, 10)  # 2 + 2 sqrt(6)
nb_margin = z + Fraction(8, 1) / z - a_upper
assert nb_margin == Fraction(39, 5750) and nb_margin > 0
gap = Fraction(23, 125) - p_c_test
assert gap == Fraction(17, 500)

# Exceptional supplement endpoint b=2, N=4: degree 10.
z = Fraction(1000, 153)
assert z * z > 9
a_upper = Fraction(79, 10)  # 3 + 2 sqrt(6)
nb_margin_b2 = z + Fraction(9, 1) / z - a_upper
assert nb_margin_b2 == Fraction(1981, 153000) and nb_margin_b2 > 0
gap_b2 = Fraction(153, 1000) - p_c_test
assert gap_b2 == Fraction(3, 1000)

# Exceptional supplement endpoint b=3, N=5: degree 13.
p_c_test_b3 = Fraction(23, 200)
crit_margin_b3 = 4 * muC(p_c_test_b3) - 1
assert crit_margin_b3 == Fraction(13633, 1000000) and crit_margin_b3 > 0
z = Fraction(25, 3)
assert z * z > 12
a_upper_b3 = Fraction(338, 35)  # 4 + 4 sqrt(2)
nb_margin_b3 = z + Fraction(12, 1) / z - a_upper_b3
assert nb_margin_b3 == Fraction(61, 525) and nb_margin_b3 > 0
gap_b3 = Fraction(3, 25) - p_c_test_b3
assert gap_b3 == Fraction(1, 200)

# General critical pivot: for m=N-1 and p=1/(2m),
# m*mu_C(p)-1 = (2m-1)/(4m^2)>0.
for m in range(1, 100):
    p = Fraction(1, 2 * m)
    lhs = m * muC(p) - 1
    rhs = Fraction(2 * m - 1, 4 * m * m)
    assert lhs == rhs and lhs > 0

# Endpoint N=b+2 for b>=4:
# h(z)-a = b+5/2 - 2 sqrt(2b+2), z=2b+2.
# Squaring positivity reduces to 4b^2-12b-7>0.
for b in range(4, 100):
    poly = 4 * b * b - 12 * b - 7
    assert poly > 0
    z = 2 * b + 2
    Q = 3 * b + 3
    assert z * z > Q

# Range N>=b+3:
# h(z)-a > N+1 - 2 sqrt(2N-2), and
# (N+1)^2 - 4(2N-2) = (N-3)^2 >0.
for b in range(1, 50):
    for N in range(b + 3, 100):
        assert (N + 1) * (N + 1) - 4 * (2 * N - 2) == (N - 3) * (N - 3)
        assert (N - 3) * (N - 3) > 0
        z = 2 * N - 2
        Q = b + 2 * N - 1
        assert z * z > Q

print("PURE_TRIANGLE_CHECK")
print("b=1,N=4 critical_margin =", fracstr(crit_margin))
print("b=1,N=4 nonbacktracking_margin =", fracstr(Fraction(39, 5750)))
print("b=1,N=4 certified_gap =", fracstr(gap), "=", float(gap))
print("b=2,N=4 nonbacktracking_margin =", fracstr(nb_margin_b2))
print("b=2,N=4 certified_gap =", fracstr(gap_b2), "=", float(gap_b2))
print("b=3,N=5 critical_margin =", fracstr(crit_margin_b3))
print("b=3,N=5 nonbacktracking_margin =", fracstr(nb_margin_b3))
print("b=3,N=5 certified_gap =", fracstr(gap_b3), "=", float(gap_b3))
print("general critical pivot identity verified for m=1..99")
print("general endpoint polynomial verified for b=4..99")
print("general N>=b+3 inequalities verified for sampled b,N ranges")
print("ALL_EXACT_CHECKS_PASS")
