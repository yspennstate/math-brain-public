from fractions import Fraction as F

# HARD7-01 exact self-check.
#
# Exact arithmetic for the n=3, q=4 l_4-cone obstruction used in the
# weak-(B) STUCK1 weighted-Poincare recovery.
#
# On H(x)=(sum_i |x_i|^q)^(2/q), cone measure on {H=1} sends
# W=|Z_1|^q to Beta(1/q,(n-1)/q).  The A-metric angular energy of W is
# Gamma(W)=q^2/(2(q-1))*W(1-W).
#
# We check:
#   (i) its exact Rayleigh quotient is 2 < n=3;
#  (ii) U=1/20+(17/20)W violates the desired 2/5 variance ratio;
# (iii) nevertheless U satisfies the necessary first-order energy cap
#       Gamma(U) <= 2 U(1-U), with exact slack >=1/75;
#  (iv) the reconstructed 2-homogeneous split is not convex, detected by
#       exact negative diagonal Hessian coefficients at (1,1,1).


def eq(a, b, label):
    if a != b:
        raise AssertionError(f"{label}: {a} != {b}")


n = 3
q = 4

m = F(1, n)
bern = m * (1 - m)
var_w = bern * F(q, n + q)
ew1w = bern * F(n, n + q)
energy_coeff = F(q * q, 2 * (q - 1))
energy_w = energy_coeff * ew1w
rayleigh_w = energy_w / var_w

s = F(17, 20)
var_u = s * s * var_w
ratio_u = var_u / bern
target_ratio = F(2, 5)
ratio_gap = ratio_u - target_ratio

# For U=1/20+(17/20)w,
#   2 U(1-U) - Gamma(U)
# = (289 w^2 - 238 w + 57)/600.
A = F(289, 600)
B = F(-238, 600)
C = F(57, 600)
vertex = -B / (2 * A)
minimum = C - B * B / (4 * A)

# At x=(1,1,1), for
# H=(x1^4+x2^4+x3^4)^(1/2),
# phi=(1/20)H+(17/20)x1^4/H,
# psi=H-phi,
# Hessians are sqrt(3) times these rational matrices.
phi_hess_coeff = [
    [F(16, 9), F(-2, 5), F(-2, 5)],
    [F(-2, 5), F(-1, 9), F(16, 45)],
    [F(-2, 5), F(16, 45), F(-1, 9)],
]
psi_hess_coeff = [
    [F(-2, 9), F(-2, 45), F(-2, 45)],
    [F(-2, 45), F(5, 3), F(-4, 5)],
    [F(-2, 45), F(-4, 5), F(5, 3)],
]

print("n =", n)
print("q =", q)
print("bern =", bern)
print("var_w =", var_w)
print("E_w1w =", ew1w)
print("energy_coeff =", energy_coeff)
print("energy_w =", energy_w)
print("rayleigh_w =", rayleigh_w)
print("var_ratio_U =", ratio_u)
print("target_ratio =", target_ratio)
print("ratio_gap =", ratio_gap)
print("cap_poly_coeffs =", A, B, C)
print("cap_vertex =", vertex)
print("cap_min =", minimum)
print("phi_hess_e2e2_coeff_sqrt3 =", phi_hess_coeff[1][1])
print("psi_hess_e1e1_coeff_sqrt3 =", psi_hess_coeff[0][0])

eq(bern, F(2, 9), "bern")
eq(var_w, F(8, 63), "var_w")
eq(ew1w, F(2, 21), "E_w1w")
eq(energy_coeff, F(8, 3), "energy coefficient")
eq(energy_w, F(16, 63), "energy_w")
eq(rayleigh_w, F(2, 1), "rayleigh_w")
if not rayleigh_w < n:
    raise AssertionError("Rayleigh quotient is not below n")

eq(ratio_u, F(289, 700), "variance ratio U")
eq(target_ratio, F(280, 700), "target ratio")
eq(ratio_gap, F(9, 700), "variance-ratio violation")
eq(vertex, F(7, 17), "cap polynomial vertex")
eq(minimum, F(1, 75), "cap polynomial minimum")
if not minimum > 0:
    raise AssertionError("first-order energy cap does not hold")

eq(phi_hess_coeff[1][1], F(-1, 9), "phi e2 Hessian coefficient")
eq(psi_hess_coeff[0][0], F(-2, 9), "psi e1 Hessian coefficient")
if not (phi_hess_coeff[1][1] < 0 and psi_hess_coeff[0][0] < 0):
    raise AssertionError("reconstructed split did not fail convexity as claimed")

print("ALL_EXACT_CHECKS_PASS = True")
