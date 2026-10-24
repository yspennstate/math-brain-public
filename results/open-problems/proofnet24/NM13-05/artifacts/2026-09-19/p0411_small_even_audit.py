#!/usr/bin/env python3
"""Exact-arithmetic audit aid for NM13-05 / P0411.

Purpose:
  * independently reconstruct Maclaurin coefficients of
        F_d(u) = exp(-(d-1)u) / H_d(u)
    from the Proposition 5.1 radial integral, not from the d=2
    arctangent closed form;
  * certify the sign of the computed coefficients using a rigorous
    Machin-formula rational enclosure for pi;
  * record the first negative coefficient for d=2,4,6,8.

This is a self-check / finite audit aid, not an independent audit and
not movement of the frozen density threshold d_bad.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def scale(c, x): return (c * x[0], c * x[1])


# Pair convention for J: a + b*pi.
@lru_cache(None)
def J(m, p):
    """Integral_0^1 s^(2m)/(1+s^2)^p ds = a+b*pi."""
    if p <= 0:
        q = -p
        return (
            sum(Fraction(comb(q, j), 2 * (m + j) + 1) for j in range(q + 1)),
            Fraction(0),
        )
    if m == 0:
        if p == 1:
            return (Fraction(0), Fraction(1, 4))
        return add(
            (Fraction(1, 2 * (p - 1) * (2 ** (p - 1))), Fraction(0)),
            scale(Fraction(2 * p - 3, 2 * (p - 1)), J(0, p - 1)),
        )
    # s^(2m) = s^(2m-2)(1+s^2) - s^(2m-2)
    return sub(J(m - 1, p - 1), J(m - 1, p))


def falling_half(alpha_num2, r):
    """(alpha)_r for alpha=alpha_num2/2, falling factorial."""
    ans = Fraction(1)
    for j in range(r):
        ans *= Fraction(alpha_num2 - 2 * j, 2)
    return ans


def radial_integral_I(n, k):
    r"""Exact integral after z=(1+t)/(1-t), t=s^2.

    For odd n=d-1 and k>=1:
      I = int_0^1 2 s^(n-1)(1-s^2)^(n+k-1)
                    [n+(n-2k)s^2]/(1+s^2)^(2n) ds.
    Returns A+B*pi.
    """
    assert n % 2 == 1 and k >= 1
    m0 = (n - 1) // 2
    N = n + k - 1
    ans = (Fraction(0), Fraction(0))
    for j in range(N + 1):
        c = (-1) ** j * comb(N, j)
        ans = add(ans, scale(Fraction(2 * n * c), J(m0 + j, 2 * n)))
        ans = add(
            ans,
            scale(Fraction(2 * (n - 2 * k) * c), J(m0 + j + 1, 2 * n)),
        )
    return ans


# Pair convention for G derivatives and F coefficients: a + b/pi.
def G_derivative(n, k):
    """G_n^(k)(1), where F_d(u)=G_n(e^(2u)), n=d-1 odd."""
    if k == 0:
        return (Fraction(1), Fraction(0))
    r = (n - 1) // 2
    # Gamma(n)/Gamma(n/2)^2 = kappa/pi for n=2r+1.
    kappa = Fraction((16 ** r) * (factorial(r) ** 2), factorial(2 * r))
    fall = falling_half(n - 2, k - 1)
    two_power = Fraction(2) ** (n - k - 1)
    A, B = radial_integral_I(n, k)
    pref = kappa * fall * two_power
    # pref*(A+B*pi)/pi = pref*B + pref*A/pi.
    return (pref * B, pref * A)


@lru_cache(None)
def stirling2(j, k):
    if j == k == 0:
        return 1
    if j == 0 or k == 0 or k > j:
        return 0
    return stirling2(j - 1, k - 1) + k * stirling2(j - 1, k)


def maclaurin_coeff(n, j):
    r"""[u^j] G_n(e^(2u)) as a+b/pi.

    Uses
      (e^(2u)-1)^k = k! sum_{j>=k} S(j,k) 2^j u^j/j!.
    """
    a = Fraction(0)
    b = Fraction(0)
    for k in range(j + 1):
        x, y = G_derivative(n, k)
        w = Fraction(stirling2(j, k))
        a += w * x
        b += w * y
    f = Fraction(2 ** j, factorial(j))
    return f * a, f * b


def atan_bounds_inverse(q, N):
    """Alternating-series bounds for atan(1/q), using S_N and S_(N+1)."""
    def partial(M):
        return sum(
            Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
            for k in range(M + 1)
        )
    x = partial(N)
    y = partial(N + 1)
    return min(x, y), max(x, y)


def pi_bounds():
    """Rigorous rational enclosure from Machin: pi=16 atan(1/5)-4 atan(1/239)."""
    l5, u5 = atan_bounds_inverse(5, 12)
    l239, u239 = atan_bounds_inverse(239, 4)
    return 16 * l5 - 4 * u239, 16 * u5 - 4 * l239


PI_LO, PI_HI = pi_bounds()


def sign_a_plus_b_over_pi(a, b):
    """Certified sign of a+b/pi, using pi>0 and PI_LO < pi < PI_HI."""
    # sign(a+b/pi) = sign(a*pi+b).
    x = a * PI_LO + b
    y = a * PI_HI + b
    lo = min(x, y)
    hi = max(x, y)
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    if lo == hi == 0:
        return 0
    raise AssertionError("pi enclosure too coarse for sign certification")


def fmt_fraction(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fmt_pair(a, b):
    return f"({fmt_fraction(a)}) + ({fmt_fraction(b)})/pi"


print("P0411 exact small-even audit")
print("pi enclosure width =", fmt_fraction(PI_HI - PI_LO))
print("pi lower =", fmt_fraction(PI_LO))
print("pi upper =", fmt_fraction(PI_HI))
print()

expected_first_negative = {2: 6, 4: 17, 6: 28, 8: 40}

for d, target in expected_first_negative.items():
    n = d - 1
    signs = []
    for j in range(target + 1):
        a, b = maclaurin_coeff(n, j)
        signs.append(sign_a_plus_b_over_pi(a, b))
    assert all(s > 0 for s in signs[:target])
    assert signs[target] < 0
    prev = maclaurin_coeff(n, target - 1)
    neg = maclaurin_coeff(n, target)
    print(f"d={d}: coefficients 0..{target-1} CERTIFIED POSITIVE; coefficient {target} CERTIFIED NEGATIVE")
    print(f"  c_{target-1} = {fmt_pair(*prev)}")
    print(f"  c_{target} = {fmt_pair(*neg)}")

# Exact d=2 cross-check against archived closed-form coefficient:
c6 = maclaurin_coeff(1, 6)
expected_c6 = (Fraction(61, 240), Fraction(-4, 5))
assert c6 == expected_c6
print()
print("d=2 radial-integral reconstruction:")
print("  c_6 =", fmt_pair(*c6))
print("  = (61*pi - 192)/(240*pi)")
print("  MATCHES archived closed-form coefficient EXACTLY")
print("ALL_EXACT_CHECKS_PASS")
