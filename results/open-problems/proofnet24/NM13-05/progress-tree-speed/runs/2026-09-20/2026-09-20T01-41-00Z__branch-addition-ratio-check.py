from fractions import Fraction as F


def a(lam):
    """a(lambda)=1/Q-1/V from the two-support escape derivative bridge."""
    Q = (F(2)-lam) * (F(2)-lam/F(2))
    V = F(3) - lam/F(3)
    return F(1)/Q - F(1)/V


def rho_small(p):
    # Exact tail bound when p <= 1/2, using 3/4 <= c3/c2 <= 1.
    return p * (F(1)-p)


def rho_large(p):
    # Exact tail bound when p >= 4/7, with F_p(t) decreasing for t >= 3/4.
    return F(12) * p * (F(1)-p) / (F(4)-p)**2


def numerator(lam, rho):
    # -ell'(lambda) >= [4-2 lambda a(lambda) rho]/(3+lambda)^2.
    return F(4) - F(2)*lam*a(lam)*rho


def margin(lam, rho):
    return numerator(lam, rho) / (F(3)+lam)**2


def large_gap(p, lam):
    # Equivalent positivity test for the exact large-p bound.
    return (F(4)-p)**2 - F(6)*lam*a(lam)*p*(F(1)-p)


print("a(1) =", a(F(1)))

p_small = F(1,8)
p_large = F(9,10)
L19 = F(19,10)
print("small-tail rho at p=1/8 =", rho_small(p_small))
print("small-tail numerator at p=1/8, lambda=19/10 =",
      numerator(L19, rho_small(p_small)))
print("small-tail derivative margin at p=1/8, lambda=19/10 =",
      margin(L19, rho_small(p_small)))
print("large-tail rho at p=9/10 =", rho_large(p_large))
print("large-tail numerator at p=9/10, lambda=19/10 =",
      numerator(L19, rho_large(p_large)))
print("large-tail derivative margin at p=9/10, lambda=19/10 =",
      margin(L19, rho_large(p_large)))

L1966 = F(983,500)
p_old_small = F(1,30)
p_old_large = F(35,36)
print("small old-tail numerator at p=1/30, lambda=983/500 =",
      numerator(L1966, rho_small(p_old_small)))
print("small old-tail derivative margin at p=1/30, lambda=983/500 =",
      margin(L1966, rho_small(p_old_small)))
print("large old-tail rho at p=35/36 =", rho_large(p_old_large))
print("large old-tail gap at p=35/36, lambda=983/500 =",
      large_gap(p_old_large, L1966))
print("large old-tail numerator at p=35/36, lambda=983/500 =",
      numerator(L1966, rho_large(p_old_large)))
print("large old-tail derivative margin at p=35/36, lambda=983/500 =",
      margin(L1966, rho_large(p_old_large)))

U1967 = F(1967,1000)
print("large old-tail gap at p=35/36, lambda=1967/1000 =",
      large_gap(p_old_large, U1967))

assert a(F(1)) == F(7,24)
assert numerator(L19, rho_small(p_small)) == F(1481,6816)
assert margin(L19, rho_small(p_small)) == F(37025,4091304)
assert rho_large(p_large) == F(108,961)
assert numerator(L19, rho_large(p_large)) == F(54092,477617)
assert margin(L19, rho_large(p_large)) == F(5409200,1146758417)
assert numerator(L1966, rho_small(p_old_small)) == F(10669196969,27362435850)
assert margin(L1966, rho_small(p_old_small)) == F(53345984845000,3373946495184213)
assert rho_large(p_old_large) == F(420,11881)
assert large_gap(p_old_large, L1966) == F(2373902221,26267938416)
assert numerator(L1966, rho_large(p_old_large)) == F(9495608884,240809703951)
assert margin(L1966, rho_large(p_old_large)) == F(2373902221000000,1484661418862356839)
assert large_gap(p_old_large, U1967) == F(-4489281919,22648172976)

print("ALL_EXACT_CHECKS_PASS")
