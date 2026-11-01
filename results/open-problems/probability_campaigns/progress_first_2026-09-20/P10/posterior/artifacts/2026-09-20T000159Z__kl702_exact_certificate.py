from fractions import Fraction

# Exact-arithmetic certificate for the only transcendental sign checks in the
# binary-tree q=3 KL-contraction lemma at lambda = 351/500.
# Logarithms are enclosed by rational atanh-series bounds.

LAM = Fraction(351, 500)
ONE = Fraction(1, 1)
THIRD = Fraction(1, 3)


def ln_bounds(x: Fraction, n: int = 100):
    assert x > 0
    if x == 1:
        return Fraction(0), Fraction(0)
    if x < 1:
        lo, hi = ln_bounds(1 / x, n)
        return -hi, -lo
    t = (x - 1) / (x + 1)
    t2 = t * t
    s = Fraction(0)
    power = t
    for k in range(n):
        s += power / (2 * k + 1)
        power *= t2
    s *= 2
    # The omitted positive tail is bounded geometrically, since all later
    # denominators are >= 2n+1.
    rem = 2 * power / ((2 * n + 1) * (1 - t2))
    return s, s + rem


def mul_ln_bounds(c: Fraction, x: Fraction):
    assert c >= 0 and x > 0
    if c == 0:
        return Fraction(0), Fraction(0)
    lo, hi = ln_bounds(x)
    return c * lo, c * hi


def d_bounds(x: Fraction):
    # d(x)=x log(3x)+(1-x)log(3(1-x)/2), with 0 log 0 := 0.
    if x == 0:
        a = (Fraction(0), Fraction(0))
    else:
        a = mul_ln_bounds(x, 3 * x)
    y = 1 - x
    if y == 0:
        b = (Fraction(0), Fraction(0))
    else:
        b = mul_ln_bounds(y, Fraction(3, 2) * y)
    return a[0] + b[0], a[1] + b[1]


def affine(x: Fraction):
    return THIRD + LAM * (x - THIRD)


def g_bounds(x: Fraction):
    # G(x)=d(x)-2d(1/3+lambda(x-1/3)).
    dlo, dhi = d_bounds(x)
    elo, ehi = d_bounds(affine(x))
    return dlo - 2 * ehi, dhi - 2 * elo


def dprime_bounds(x: Fraction):
    return ln_bounds(2 * x / (1 - x))


def gprime_bounds(x: Fraction):
    lo1, hi1 = dprime_bounds(x)
    lo2, hi2 = dprime_bounds(affine(x))
    return lo1 - 2 * LAM * hi2, hi1 - 2 * LAM * lo2


def q_second_numerator(x: Fraction):
    # Sign of G'' is sign of this quadratic Q(x).
    return (
        LAM * LAM * x * x
        + LAM * (1 - 4 * LAM) * x / 3
        + (2 - LAM - LAM * LAM) / 9
    )


# Q is upward-opening. These exact rational signs force one root in
# (1/3,0.4) and the other in (0.4,0.49), hence G''>0 on [0.49,1].
assert q_second_numerator(THIRD) > 0
assert q_second_numerator(Fraction(2, 5)) < 0
assert q_second_numerator(Fraction(49, 100)) > 0

# The unique post-0.49 stationary point of G is bracketed exactly.
L = Fraction(507896, 1_000_000)
U = Fraction(507897, 1_000_000)
gpL = gprime_bounds(L)
gpU = gprime_bounds(U)
assert gpL[1] < 0
assert gpU[0] > 0

# Since G''>0 on this bracket, |G'| is maximized at an endpoint there.
# A rational Lipschitz lower bound then certifies the local minimum is >0.
gL = g_bounds(L)
M = max(-gpL[0], gpU[1])
min_lower = gL[0] - M * (U - L)
assert min_lower > 0

# Endpoint is also strictly positive; G(1/3)=0 exactly by definition.
g1 = g_bounds(ONE)
assert g1[0] > 0

print("PASS")
print("lambda =", float(LAM))
print("Q(1/3), Q(0.4), Q(0.49) =", *(float(q_second_numerator(x)) for x in (THIRD, Fraction(2,5), Fraction(49,100))))
print("G'(L) upper =", float(gpL[1]))
print("G'(U) lower =", float(gpU[0]))
print("certified G(local minimum) lower >", float(min_lower))
print("G(1) lower =", float(g1[0]))
