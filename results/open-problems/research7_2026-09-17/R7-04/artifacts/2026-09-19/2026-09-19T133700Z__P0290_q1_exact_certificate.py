#!/usr/bin/env python3
"""
Exact finite-core certificate for R7-04 / P0290 fixed Q1 recovery.

This checker proves the compact regime 0 <= c <= 3/2 for the centered
3x3 generator matrix M corresponding to the exact four-state Q1 ray.
All polynomial and tail arithmetic is exact (fractions.Fraction).

It also verifies the rational matrix inequalities used for the analytic
large-c regime c >= 3/2.  The only transcendental step there is the
elementary strict lower bound
  exp(19/8) > sum_{k=0}^5 (19/8)^k/k! > 185/18,
which is checked rationally.
"""
from fractions import Fraction as F
from math import factorial, comb

def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def mat_T(A):
    return [list(row) for row in zip(*A)]
def mat_scale(a,A):
    return [[a*x for x in row] for row in A]
def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mat_pow(A,n):
    R=eye(len(A)); B=A
    while n:
        if n&1: R=mat_mul(R,B)
        B=mat_mul(B,B); n//=2
    return R
def sym(A):
    AT=mat_T(A)
    return mat_scale(F(1,2),mat_add(A,AT))
def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def leading_principal_minors(A):
    return [A[0][0], det2([row[:2] for row in A[:2]]), det3(A)]
def poly_add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,x in enumerate(p): r[i]+=x
    for i,x in enumerate(q): r[i]+=x
    return r
def poly_neg(p):
    return [-x for x in p]
def poly_mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            r[i+j]+=x*y
    return r
def bernstein_0B(power,B):
    """Exact Bernstein coefficients on [0,B] for power coefficients."""
    n=len(power)-1
    out=[]
    for j in range(n+1):
        s=F(0)
        for k in range(j+1):
            s += power[k]*(B**k)*F(comb(j,k),comb(n,k))
        out.append(s)
    return out
def ffloat(q):
    return float(q.numerator/q.denominator)

# Centered matrix of Q1 in the orthonormal (u,v,w) basis.
M=[
    [F(-4),F(-1),F(1)],
    [F(1),F(-2),F(1)],
    [F(-1),F(1),F(-4)],
]

# ------------------------------------------------------------------
# Compact interval 0 <= c <= 3/2
# F(c)=M Psi(cM)=sum_{n>=0} c^n M^(n+1)/[n!(n+2)(n+3)].
# H(c)=Sym F(c).  We truncate at N=50 and certify h<0, tr(H-)<0,
# det(H-)>0 by exact Bernstein coefficients plus a rigorous tail.
# ------------------------------------------------------------------
N=50
h=[]; a=[]; b=[]; d=[]
for n in range(N+1):
    Mn=mat_pow(M,n+1)
    Hn=sym(Mn)
    den=F(1, factorial(n)*(n+2)*(n+3))
    h.append(Hn[0][0]*den)
    a.append(Hn[1][1]*den)
    b.append(Hn[1][2]*den)
    d.append(Hn[2][2]*den)

tr=poly_add(a,d)
det=poly_add(poly_mul(a,d),poly_neg(poly_mul(b,b)))
B=F(3,2)

Bh=bernstein_0B(h,B)
Ba=bernstein_0B(a,B)
Bb=bernstein_0B(b,B)
Bd=bernstein_0B(d,B)
Btr=bernstein_0B(tr,B)
Bdet=bernstein_0B(det,B)

# ||M||_2 <= sqrt(||M||_1 ||M||_inf) <= 6.
# On c<=3/2, c||M||<=9.
# Entrywise tail <= 6 * sum_{n>N} 9^n/n!
#                 <= 6 e^9 9^(N+1)/(N+1)!
# and e<3 gives e^9<3^9.
eps=F(6*(3**9)*(9**(N+1)), factorial(N+1))

# Compact sign margins.
h_upper=max(Bh)+eps
tr_upper=max(Btr)+2*eps
Amax=max(abs(min(Ba)),abs(max(Ba)))
Bmax=max(abs(min(Bb)),abs(max(Bb)))
Dmax=max(abs(min(Bd)),abs(max(Bd)))
det_err=eps*(Amax+Dmax+2*Bmax)+2*eps*eps
det_lower=min(Bdet)-det_err

assert max(Bh) < 0 and h_upper < 0
assert max(Btr) < 0 and tr_upper < 0
assert min(Bdet) > 0 and det_lower > 0

# ------------------------------------------------------------------
# Analytic tail c >= 3/2
# Closed form:
# c^2 F(c)= M^-1 + (2/c)M^-2
#          + e^{cM}(M^-1-(2/c)M^-2).
# Hence scaled H is L(c)+Sym(E(c)).
# Verify exact inverse, positivity of Sym(M^-2), the Loewner margin
# L(c) <= -(3/25)I, and the dissipative semigroup estimate.
# ------------------------------------------------------------------
Minv=[
    [F(-7,32),F(3,32),F(-1,32)],
    [F(-3,32),F(-17,32),F(-5,32)],
    [F(1,32),F(-5,32),F(-9,32)],
]
assert mat_mul(M,Minv)==eye(3) and mat_mul(Minv,M)==eye(3)
Minv2=mat_mul(Minv,Minv)
S1=sym(Minv)
S2=sym(Minv2)

# S2 is positive definite, so L(c)=S1+(2/c)S2 is Loewner-decreasing.
assert all(x>0 for x in leading_principal_minors(S2))

L15=mat_add(S1,mat_scale(F(4,3),S2))
margin=F(3,25)
T=mat_scale(F(-1),mat_add(L15,mat_scale(margin,eye(3))))
assert all(x>0 for x in leading_principal_minors(T))

# Dissipation: Sym(M) <= -(19/12) I.
SM=sym(M)
diss=mat_scale(F(-1),mat_add(SM,mat_scale(F(19,12),eye(3))))
assert all(x>0 for x in leading_principal_minors(diss))

# Frobenius-norm upper bounds imply operator-norm bounds:
# ||M^-1||_2 < 7/10, ||M^-2||_2 < 2/5.
fro1sq=sum(x*x for row in Minv for x in row)
fro2sq=sum(x*x for row in Minv2 for x in row)
assert fro1sq < F(49,100)
assert fro2sq < F(4,25)

# For c>=3/2:
# ||E(c)|| <= exp(-19c/12)*(7/10 + (2/c)*(2/5))
#          <= exp(-19/8)*(37/30).
# Prove exp(19/8) > 185/18 by a degree-5 Taylor lower bound.
x=F(19,8)
exp_lower=sum((x**k)/factorial(k) for k in range(6))
assert exp_lower > F(185,18)
# Hence exp(-19/8) < 18/185 and the perturbation is strictly below 3/25.
tail_large_bound=F(37,30)*F(18,185)
assert tail_large_bound == margin  # strict in reality because exp inequality is strict.

print("P0290 Q1 exact compact-and-tail certificate")
print("N =",N)
print("compact interval = [0, 3/2]")
print("eps <=", eps, "~", ffloat(eps))
print("max Bernstein h_N =", max(Bh), "~", ffloat(max(Bh)))
print("certified h upper =", h_upper, "~", ffloat(h_upper))
print("max Bernstein tr_N =", max(Btr), "~", ffloat(max(Btr)))
print("certified trace upper =", tr_upper, "~", ffloat(tr_upper))
print("min Bernstein det_N =", min(Bdet), "~", ffloat(min(Bdet)))
print("certified determinant lower =", det_lower, "~", ffloat(det_lower))
print("S2 leading principal minors =", leading_principal_minors(S2))
print("-(L(3/2)+3/25 I) leading principal minors =", leading_principal_minors(T))
print("-(Sym(M)+19/12 I) leading principal minors =", leading_principal_minors(diss))
print("||M^-1||_F^2 =", fro1sq, "< 49/100")
print("||M^-2||_F^2 =", fro2sq, "< 4/25")
print("Taylor_5(exp(19/8)) =", exp_lower, "> 185/18")
print("(37/30)*(18/185) =", tail_large_bound, "= 3/25; strict exponential bound gives <")
print("CONCLUSION: H_Q1(c) is strictly negative definite on the centered space for every c>0.")
print("ALL_EXACT_CHECKS_PASS")
