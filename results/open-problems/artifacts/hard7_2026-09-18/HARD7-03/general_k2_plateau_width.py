from fractions import Fraction as F
import sympy as sp

print("HARD7-03 exact general-K2 plateau / binary-width certificate")

# Coupling identity: W~Exp(a), U=B E with p=1-r/a, E~Exp(r).
# Then Z=W+U has Exp(r) Laplace transform.
r, a, s = sp.symbols("r a s", positive=True)
p = 1 - r/a
lap_W = a/(a+s)
lap_U = (1-p) + p*r/(r+s)
lap_diff = sp.factor(sp.simplify(lap_W*lap_U - r/(r+s)))
print("coupling_laplace_difference =", lap_diff)
assert lap_diff == 0

# Mean bonus identity.
mean_U = sp.simplify(p/r)
mean_target = sp.simplify(1/r - 1/a)
print("mean_bonus_difference =", sp.simplify(mean_U-mean_target))
assert sp.simplify(mean_U-mean_target) == 0

# Exact convex-boundary secant algebra.
G0, Gv, v = sp.symbols("G0 Gv v", positive=True)
sv = v/Gv
gv = (1-v)/Gv
g0 = 1/G0
secant = sp.factor(sp.simplify((gv-g0)/sv - ((G0-Gv)/(G0*v)-1)))
print("secant_identity_difference =", secant)
assert secant == 0

# Frozen binary law Q=1/2 delta_{1/2}+1/2 delta_1.
r_bin = F(1,2)
E_inv_alpha = F(1,2)*F(2,1) + F(1,2)*F(1,1)
mu = F(1,1)/r_bin - E_inv_alpha
r_mu = r_bin*mu
print("binary_E_inv_alpha =", E_inv_alpha)
print("binary_mu =", mu)
print("binary_r_mu =", r_mu)
assert E_inv_alpha == F(3,2)
assert mu == F(1,2)
assert r_mu == F(1,4)

# Optimized path-count Chernoff certificate.
# h(a)=a-1-log(3a). For a>1, h is strictly increasing.
# It is enough to prove exp(a_hi-1)>3*a_hi.
a_hi = F(6578563,2000000)
x = a_hi - 1

# Since x>0, any finite Taylor partial sum is strictly below exp(x).
taylor = F(0)
term = F(1)
for k in range(15):  # k=0,...,14
    if k == 0:
        term = F(1)
    elif k > 0:
        term = term*x/k
    taylor += term

rhs = 3*a_hi
gap = taylor-rhs
print("a_hi =", a_hi)
print("a_hi_float =", float(a_hi))
print("x =", x)
print("taylor_0_14 =", taylor)
print("3a_hi =", rhs)
print("taylor_minus_3a_hi =", gap)
print("taylor_minus_3a_hi_float =", float(gap))
assert a_hi > 1
assert gap > 0

# Hence a_*<a_hi, G_1(0)<=a_*<a_hi, and for the binary law
# Delta_2(Q) >= (r*mu)/a_hi = 1/(4*a_hi).
L = r_mu/a_hi
print("L =", L)
print("L_float =", float(L))
print("L_minus_1_over_16 =", L-F(1,16))
print("L_minus_19_over_250 =", L-F(19,250))
assert L == F(500000,6578563)
assert L > F(1,16)
assert L > F(19,250)

print("ALL_EXACT_CHECKS_PASS = True")
