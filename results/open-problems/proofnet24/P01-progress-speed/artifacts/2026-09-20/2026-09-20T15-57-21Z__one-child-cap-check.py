from fractions import Fraction as F

p = F(792847, 2000000)
A = F(8217203, 12500000)
x0 = F(24995699, 50000000)
L = F(2, 3)
target = F(1, 15000000)

def G(x, p, lam):
    return (lam + 1)*x*x + (lam*lam - 1 + p*lam)*x - p*lam

u = (1-p)*x0 + p
G_corner = G(x0, p, A)
dG_dlam_corner = x0*x0 + (2*A + p)*x0 - p

# Raw common-mean ratio is increasing in mu on D>=3 if this D=3 worst-case slack is positive.
ratio_mu_slack = 3*(1-L) - L - 2*u*u + 1

K = (L + 2*u - 1)/u
X = p*K/(1-p)
hard_margin = 2*(1-X)/(1+X+L)**2

support_slack = 1 - A - 2*p*A*A
lower_margin = 2*(1-p)*support_slack/((1-A)*(1+A)**2)

# D=2 is handled separately.
d2_margin = F(63, 256)

def frontier_poly(z):
    return (46818*z**6 - 113508*z**5 + 112815*z**4
            - 58105*z**3 + 16065*z**2 - 2193*z + 108)

p_lo = F(792847, 2000000)   # 0.3964235
p_hi = F(991059, 2500000)   # 0.3964236
P_lo = frontier_poly(p_lo)
P_hi = frontier_poly(p_hi)

assert G_corner > 0
assert dG_dlam_corner > 0
assert x0 < 1
assert ratio_mu_slack > 0
assert X < 1
assert hard_margin > target
assert support_slack > 0
assert lower_margin > target
assert d2_margin > target
assert P_lo > 0
assert P_hi < 0

print("ALL_EXACT_CHECKS_PASS")
for name, value in [
    ("p_star", p),
    ("lambda_split", A),
    ("mu1_cap", x0),
    ("mu_cap", u),
    ("G_corner", G_corner),
    ("dG_dlambda_corner", dG_dlam_corner),
    ("ratio_mu_slack", ratio_mu_slack),
    ("K", K),
    ("X", X),
    ("one_minus_X", 1-X),
    ("hard_margin", hard_margin),
    ("support_free_slack", support_slack),
    ("lower_margin", lower_margin),
    ("D2_margin", d2_margin),
    ("frontier_P_lo", P_lo),
    ("frontier_P_hi", P_hi),
]:
    print(f"{name}={value} ~= {float(value):.16g}")
