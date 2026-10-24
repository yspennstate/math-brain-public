from fractions import Fraction as F

def psi(s):
    c = F(1,3)  # worst hard-strip c=1-lambda at lambda=2/3
    return s/(s-c)

def G(p, lam, x):
    return (lam+1)*x*x + (lam*lam-1+p*lam)*x - p*lam

def dG_dlambda(p, lam, x):
    return x*x + (2*lam+p)*x - p

def c1_type_lower(p, x):
    A = psi(2*x)
    B = psi(x+1)
    C = psi(F(2))
    return F(1,2)*((1-p)**2*A + 2*p*(1-p)*B + p*p*C), (A,B,C)

def hard_margin_from_X(X):
    return 2*(1-X)/(1+X+F(2,3))**2

def support_free_slack(p, A):
    return 1-A-2*p*A*A

def support_free_margin(p, A):
    s = support_free_slack(p,A)
    return 2*(1-p)*s/((1-A)*(1+A)**2)

# Main all-D theorem
p0 = F(20119,50000)          # 0.40238
lam0 = F(65487,100000)       # 0.65487
x0 = F(50267,100000)         # 0.50267
target0 = F(1,176000)

g0 = G(p0,lam0,x0)
dg0 = dG_dlambda(p0,lam0,x0)
C0,(A0,B0,D0) = c1_type_lower(p0,x0)
X0 = p0/((1-p0)*C0)
hm0 = hard_margin_from_X(X0)
sf0 = support_free_slack(p0,lam0)
sfm0 = support_free_margin(p0,lam0)

assert g0 > 0
assert dg0 > 0
assert A0 > B0 > D0
assert X0 < 1
assert hm0 > target0
assert sf0 > 0
assert sfm0 > target0

# Finite-D extension beyond the all-D p-cap
p1 = F(40239,100000)         # 0.40239
lam1 = F(13097,20000)        # 0.65485
x1 = F(100537,200000)        # 0.502685
Dmax = 50000
target1 = F(1,400000)

g1 = G(p1,lam1,x1)
dg1 = dG_dlambda(p1,lam1,x1)
C1,(A1,B1,D1) = c1_type_lower(p1,x1)
XD = F(Dmax-1)*p1/(F(Dmax)*(1-p1)*C1+p1)
hm1 = hard_margin_from_X(XD)
sf1 = support_free_slack(p1,lam1)
sfm1 = support_free_margin(p1,lam1)

assert g1 > 0
assert dg1 > 0
assert A1 > B1 > D1
assert XD < 1
assert hm1 > target1
assert sf1 > 0
assert sfm1 > target1

# Exact obstruction for trying to make p=0.40239 uniform in all D
# within the present architecture:
# support-free patch + one-child Jensen cap + type-conditioned c1 Jensen
# + pathwise c_D<=1/D + discard a_D.
lam_bar = F(654869,1000000)
x_low = F(502672,1000000)
h_bar = support_free_slack(p1,lam_bar)
g_bar = G(p1,lam_bar,x_low)
dg_at_zero = x_low*x_low + p1*x_low - p1
Copt,_ = c1_type_lower(p1,x_low)
asym_gap = (1-p1)*Copt - p1

assert h_bar < 0
assert dg_at_zero > 0
assert g_bar < 0
assert asym_gap < 0

print("ALL_EXACT_CHECKS_PASS")
print("MAIN p0 =", p0, float(p0))
print("MAIN lambda0 =", lam0, float(lam0))
print("MAIN x0 =", x0, float(x0))
print("MAIN Gcorner =", g0, float(g0))
print("MAIN dG/dlambda corner =", dg0, float(dg0))
print("MAIN psi-values A>B>C =", A0, B0, D0)
print("MAIN Cstar =", C0, float(C0))
print("MAIN Xstar =", X0, float(X0))
print("MAIN hard margin =", hm0, float(hm0))
print("MAIN support-free slack =", sf0, float(sf0))
print("MAIN support-free margin =", sfm0, float(sfm0))
print("MAIN target =", target0, float(target0))
print("GAIN over previous p =", p0-F(792847,2000000), float(p0-F(792847,2000000)))
print("FINITE p1 =", p1, float(p1), "Dmax =", Dmax)
print("FINITE lambda1 =", lam1, float(lam1), "x1 =", x1, float(x1))
print("FINITE Gcorner =", g1, float(g1))
print("FINITE Cstar =", C1, float(C1))
print("FINITE X_Dmax =", XD, float(XD))
print("FINITE hard margin =", hm1, float(hm1))
print("FINITE support-free slack =", sf1, float(sf1))
print("FINITE support-free margin =", sfm1, float(sfm1))
print("FINITE target =", target1, float(target1))
print("OBSTRUCTION h(lam_bar) =", h_bar, float(h_bar))
print("OBSTRUCTION G(lam_bar,x_low) =", g_bar, float(g_bar))
print("OBSTRUCTION dG/dlambda at lambda=0,x_low =", dg_at_zero, float(dg_at_zero))
print("OBSTRUCTION (1-p)Copt-p =", asym_gap, float(asym_gap))
