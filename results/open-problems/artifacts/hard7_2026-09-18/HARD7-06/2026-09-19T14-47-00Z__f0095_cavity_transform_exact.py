from fractions import Fraction as F
import sympy as sp

# HARD7-06 self-check for the q=3 ACG cavity reparameterization.
# Symbolic identities are exact. Root signs use exact Fraction Taylor bounds;
# printed decimals are presentation only.

lam, mu, r, s = sp.symbols("lam mu r s")
alpha = (1 - 2*lam)/(1 + lam)
A = (2 + alpha)/3
B = (1 + 2*alpha)/3
assert sp.simplify(A - 1/(1 + lam)) == 0
assert sp.simplify(B - (1 - lam)/(1 + lam)) == 0

alpha_mu = (1 - 2*mu)/(1 + mu)
R = 1 - (1 - alpha)*(1 - alpha_mu)/3
Q = (1 + lam + mu - 2*lam*mu)/((1 + lam)*(1 + mu))
assert sp.simplify(R - Q) == 0

T = (1 - 2*r + s)/(2 - r)
Tout = (3*r - 2*s)/(3 - 3*r + s)
assert sp.simplify((1 - 2*T)/(1 + T) - Tout) == 0

lnew = sp.symbols("lnew")
rnew = r*(1 - lnew)
snew = s*(1 - 2*lnew)
delta = 1 - 2*r + s
delta_new = 1 - 2*rnew + snew
assert sp.simplify(delta_new - delta - 2*lnew*(r - s)) == 0

# Current rigorous ACG endpoint from the preceding HARD7-06 checkpoint.
d = F(46865076662, 10_000_000_000)

# Exact enclosure of exp(x), x>=0.  The lower bound is the positive Taylor
# partial sum.  The tail is bounded by a geometric series once N+2>x.
def exp_pos_bounds(x, N=80):
    assert x >= 0
    term = F(1)
    total = F(1)
    for k in range(1, N + 1):
        term = term*x/k
        total += term
    nxt = term*x/(N + 1)
    ratio = x/(N + 2)
    assert ratio < 1
    return total, total + nxt/(1 - ratio)

def exp_neg_bounds(x, N=80):
    lo, hi = exp_pos_bounds(x, N)
    return 1/hi, 1/lo

def fixed_point_F_bounds(q):
    # F(q)=1-exp(-d q)(1+d q)-q.
    x = d*q
    elo, ehi = exp_neg_bounds(x)
    c = 1 + x
    return 1 - ehi*c - q, 1 - elo*c - q

brackets = [
    (F(1388, 10000), -1),
    (F(1389, 10000), +1),
    (F(9319, 10000), +1),
    (F(9320, 10000), -1),
]
rows = []
for q, sign in brackets:
    lo, hi = fixed_point_F_bounds(q)
    if sign < 0:
        assert hi < 0
    else:
        assert lo > 0
    rows.append((q, lo, hi, sign))

print("SYMBOLIC_TRANSFORM_IDENTITIES_PASS = True")
print("DELTA_RECURRENCE_PASS = True")
for q, lo, hi, sign in rows:
    print(
        f"q={float(q):.4f} "
        f"F_interval=[{float(lo):.18e},{float(hi):.18e}] "
        f"sign={'+' if sign > 0 else '-'} exact_sign=True"
    )
print("NONZERO_ROOT_BRACKETS_q = (0.1388,0.1389), (0.9319,0.9320)")
print("BOUNDARY_ATOM_BRACKETS_p0 = (0.8611,0.8612), (0.0680,0.0681)")
print("ALL_EXACT_CHECKS_PASS = True")
