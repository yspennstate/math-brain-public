import mpmath as mp

mp.mp.dps = 50

# High-precision locator from the preceding certified balanced-Hessian checkpoint.
s = mp.mpf("0.5046113125617359603")

sqrt2pi = mp.sqrt(2 / mp.pi)


def f(y):
    """Standard half-normal density on y>=0."""
    return sqrt2pi * mp.e ** (-y * y / 2)


def F(y):
    """Standard half-normal CDF on y>=0."""
    return mp.erf(y / mp.sqrt(2))


def H(s):
    """
    H(s)=E[U |DABC|] in the balanced Hadamard model.

    The one-dimensional representation proved in the report is
      H(s)=6 s^2 int_0^inf y f(y)^2 [F(y)-y f(y)] F(y/s) dy.
    """
    return mp.quad(
        lambda y: 6
        * s
        * s
        * y
        * f(y) ** 2
        * (F(y) - y * f(y))
        * F(y / s),
        [0, mp.inf],
    )


Hs = H(s)
Hp = mp.diff(H, s)
ratio = s * Hp / Hs

alpha = (1 - s * s) / (s * s)
c3 = (2 * alpha**2 / mp.sqrt(3)) * (
    (2 + s * s) * Hs - (1 - s * s) * s * Hp
)

# From the analytic inequality s H'(s) <= 2 H(s), the report obtains
# c3 >= 2 sqrt(3) alpha^2 s^2 H(s) > 0.
lower = 2 * mp.sqrt(3) * alpha**2 * s * s * Hs

# S4 cubic-invariant normalization for
# h=(3,-1,-1,-1)/(2 sqrt(3)).
h1 = 3 / (2 * mp.sqrt(3))
ho = -1 / (2 * mp.sqrt(3))
I3 = h1**3 + 3 * ho**3

# A normalized transverse vector can be taken as e=(0,1,-1,0)/sqrt(2).
# For the invariant sum z_i^3,
#   T(h,e,e)/T(h,h,h) = (sum h_i e_i^2)/(sum h_i^3) = -1/2.
Te_ratio = ho / I3

print("s =", mp.nstr(s, 25))
print("lambda =", mp.nstr(s * s, 25))
print("H(s) =", mp.nstr(Hs, 25))
print("s H'(s)/H(s) =", mp.nstr(ratio, 25))
print("c3(s) =", mp.nstr(c3, 25))
print("analytic lower bound =", mp.nstr(lower, 25))
print("I3(h31) =", mp.nstr(I3, 25))
print("T(h,e,e)/T(h,h,h) =", mp.nstr(Te_ratio, 25))

assert Hs > 0
assert 1 < ratio < 2
assert c3 > lower > 0
assert abs(I3 - 1 / mp.sqrt(3)) < mp.mpf("1e-45")
assert abs(Te_ratio + mp.mpf("0.5")) < mp.mpf("1e-45")

print("ALL CHECKS PASSED")
