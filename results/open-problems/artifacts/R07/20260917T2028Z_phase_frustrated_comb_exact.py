from fractions import Fraction as F

# Exact finite core for R07 / I0077 T29.
# Canonical alternating combs at geometric times 4^k:
#   D_- = union_j [12j-2-eta, 12j-2+eta]
#   D_+ = union_j [12j+2-eta, 12j+2+eta]
# Sampled OU correlation is r=1/2.

L = F(12)
c_minus, c_plus = F(-2), F(2)
r = F(1, 2)
eta0 = F(1, 10)
eta_relax = F(1, 5)
s2 = F(1) - r*r


def dist_to_lattice(x, shift):
    # For the two parity representatives below, this finite range contains
    # every nearest lattice point; all arithmetic is exact.
    return min(abs(x - (shift + j*L)) for j in range(-4, 5))


sep_minus_to_plus = []
sep_plus_to_minus = []
for parity in (0, 1):
    mu_mp = r * (parity*L + c_minus)
    mu_pm = r * (parity*L + c_plus)
    sep_minus_to_plus.append(dist_to_lattice(mu_mp, c_plus))
    sep_plus_to_minus.append(dist_to_lattice(mu_pm, c_minus))

Delta = min(sep_minus_to_plus + sep_plus_to_minus)
d = Delta - (F(1) + r) * eta_relax
chernoff_exponent = d*d / (F(2)*s2)
exp4_taylor_lower = F(1) + F(4) + F(4**2, 2) + F(4**3, 6)

# A wide disconnected example for the source-side existence regime.
wide_eta = F(7, 2)
common_central_halfwidth = wide_eta - F(2)

print("sep minus->plus parities =", sep_minus_to_plus)
print("sep plus->minus parities =", sep_plus_to_minus)
print("Delta =", Delta)
print("relaxed distance d =", d)
print("s^2 =", s2)
print("Chernoff exponent =", chernoff_exponent)
print("exp(4) Taylor lower bound through cubic =", exp4_taylor_lower)
print("wide eta =", wide_eta)
print("common central halfwidth =", common_central_halfwidth)

assert sep_minus_to_plus == [F(3), F(3)]
assert sep_plus_to_minus == [F(3), F(3)]
assert Delta == F(3)
assert d == F(27, 10)
assert s2 == F(3, 4)
assert chernoff_exponent == F(243, 50)
assert chernoff_exponent > 4
assert exp4_taylor_lower == F(71, 3)
assert exp4_taylor_lower > 16
# Therefore 2 exp(-243/50) < 2 exp(-4) < 1/8.
# Since 1/8 = 4^(-3/2), the geometric-time persistence exponent is > 1.
assert F(3, 2) > 1
assert wide_eta < L/2
assert common_central_halfwidth == F(3, 2)
assert common_central_halfwidth > 1

print("PASS")
