#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

# Exact/symbolic self-check for R09 / G0013, 2026-09-17T2031Z.
# This certifies the finite algebra and the 18432-cell rational upper sum used
# in the written proof. It is a SELF-CHECK, not an independent audit.

u = sp.symbols("u")
K = u*(3-u)**2 / ((u-1)**2*(4-u))
Kp = sp.factor(sp.diff(K, u))
assert sp.simplify(Kp - 12*(u-3)/((u-4)**2*(u-1)**3)) == 0

u0 = F(17,12)
k = F(6137,775)
c = 1+k
r = k/c
m0 = F(19,48)

def Kq(x):
    return x*(3-x)**2/((x-1)**2*(4-x))
def Gq(x):
    return (x*x-k*(x-1)**3/(3-x))/3

assert Kq(u0) == k
assert Gq(u0) == F(17,31)
assert (3-u0)/4 == m0
assert c == F(6912,775)
assert r == F(6137,6912)

# At the transition the one-sided ramp and two-sided clipped-affine branch meet.
L0 = F(19,24)
def aval(m,L):
    return 6*m*(1-m)-L*L/2
assert L0 == 2*m0
assert aval(m0,L0)*L0 == r

# Tail objective and derivative. The analytic report proves:
#  - concavity in L on 0<=L<=2m,
#  - the unique maximizer solves aval(m,L)*L=r,
#  - the resulting envelope is increasing in m.
def Ft(m,L):
    a = aval(m,L)
    return c*a*a/F(12) - k*m*(1-m) + k*L/F(6)

def Fp(m,L):
    return (k-c*aval(m,L)*L)/F(6)

def root_bracket_and_tangent_cap(m, steps=42):
    lo, hi = F(0), 2*m
    # g(L)=a(L)L-r; derivative of F has the opposite sign.
    def g(L):
        return aval(m,L)*L-r
    assert g(lo) < 0
    assert g(hi) >= 0
    for _ in range(steps):
        mid=(lo+hi)/2
        if g(mid) <= 0:
            lo=mid
        else:
            hi=mid
    assert Fp(m,lo) >= 0
    assert Fp(m,hi) <= 0
    # Concavity: F(L*) <= F(lo)+F'(lo)(hi-lo).
    cap = Ft(m,lo)+Fp(m,lo)*(hi-lo)
    return cap,lo,hi

# Exact right-Riemann upper sum on [m0,1/2].
N = 18432
width = (F(1,2)-m0)/N
assert width == F(5,884736)

small_integral = F(17,31)*m0**3/F(3)
tail_sum = F(0)
max_bracket_width = F(0)
for j in range(1,N+1):
    m = m0+j*width
    cap,lo,hi = root_bracket_and_tangent_cap(m)
    tail_sum += cap
    max_bracket_width=max(max_bracket_width,hi-lo)

B_upper = 2*(small_integral + width*tail_sum)
B_cap = F(4442834905081,10**14)
assert B_upper < B_cap

# Combine S <= 2B + cH with S <= 1/9-(4/3)H.
H0 = (F(1,9)-2*B_cap)/(c+F(4,3))
U_new = 2*B_cap+c*H0
assert U_new == F(1289727882057511,11918000000000000)

U_old = F(580249,5337500)
assert U_new < U_old
assert U_new > F(1,10)

# B20 nesting identity: on the tail, implicit differentiation of
# L(6m(1-m)-L^2/2)=r gives
# L'=-6(1-2m)L/D, D=6m(1-m)-3L^2/2.
# The condition L'>=-2 is equivalent to
# L^2+2(1-2m)L-4m(1-m)<=0, whose positive root is exactly 2m.
m,L=sp.symbols("m L", positive=True)
poly = L**2 + 2*(1-2*m)*L - 4*m*(1-m)
assert sp.factor(poly.subs(L,2*m)) == 0
assert sp.simplify(poly-(L-2*m)*(L+2-2*m)) == 0

# B14 D4 covariance algebra is linear; record the exact cost/rho conversion.
# If d=rho_XU+rho_YV, then W2^2=1/3-d/6, so d=2-6S.
direct_rho_lower = 2-6*U_new

print("R09 G0013 OPTIMIZED-PENALTY / NESTING SELF-CHECK")
print("K'(u) = 12(u-3)/((u-4)^2 (u-1)^3) [symbolically verified]")
print("u0 =", u0, "; k=K(u0) =", k, "; G_k(u0) =", Gq(u0))
print("m0 =", m0, "; c=1+k =", c, "; r=k/c =", r)
print("tail cells =", N, "; width =", width)
print("max root-bracket width <=", max_bracket_width, "=", float(max_bracket_width))
print("B_upper exact =", B_upper)
print("B_upper decimal =", float(B_upper))
print("B_cap =", B_cap, "=", float(B_cap))
print("B_cap-B_upper =", B_cap-B_upper, "=", float(B_cap-B_upper))
print("intersection H0 =", H0, "=", float(H0))
print("U_new =", U_new, "=", float(U_new))
print("U_old =", U_old, "=", float(U_old))
print("strict improvement =", U_old-U_new, "=", float(U_old-U_new))
print("remaining gap U_new-1/10 =", U_new-F(1,10), "=", float(U_new-F(1,10)))
print("direct Spearman-sum lower bound 2-6U_new =", direct_rho_lower, "=", float(direct_rho_lower))
print("tail nesting factorization: L^2+2(1-2m)L-4m(1-m)=(L-2m)(L+2-2m)")
print("SELF_CHECK_ONLY / PASS")
