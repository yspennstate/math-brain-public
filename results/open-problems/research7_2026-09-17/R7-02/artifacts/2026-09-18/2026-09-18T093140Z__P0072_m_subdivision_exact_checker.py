#!/usr/bin/env python3
import sympy as sp

L,A,B,R,m = sp.symbols("L A B R m", nonnegative=True)
eps,k,alpha,beta,kA,kB = sp.symbols("eps k alpha beta kA kB", positive=True)
t = L+A+B+R+2
u = 1+L+A
v = 1+L+B
w = 1+A+B
d = 1+R+B
e = 1+R+A
g = u/m
Z = g*v*w + g*v*d + g*v*e + g*w*e + g*d*e + v*w*d + v*d*e + w*d*e
qL = sp.cancel(g*v*(w+d+e)/Z)
qA = sp.cancel(g*w*e/Z)
qB = sp.cancel(v*w*d/Z)
qR = sp.cancel(d*e*(g+v+w)/Z)

assert sp.factor(qL+qA+qB+qR-1) == 0

Delta = sp.cancel(qR - (R+sp.Rational(1,2))/t)
N = sp.expand(sp.cancel(Delta * (2*m*t*Z)))
assert not sp.denom(N).has(L,A,B,R,m)

N2 = sp.expand(N.subs(m,2))
Q0 = (
    2*A**3 + 6*A**2*B + 4*A**2*L + 2*A**2*R + 9*A**2
    + 4*A*B**2 + 6*A*B*L + 4*A*B*R + 15*A*B
    + 2*A*L**2 + 2*A*L*R + 10*A*L + 5*A*R + 12*A
    + 2*B**2*R + 3*B**2 + 4*B*L*R + 5*B*L + 6*B*R + 8*B
    + 2*L**2*R + 2*L**2 + 5*L*R + 6*L + 4*R + 5
)
assert sp.expand(N - (N2 + (m-2)*(B+R+1)*Q0)) == 0

def positive_coeffs(poly, gens):
    P = sp.Poly(sp.expand(poly), *gens)
    return all(c.is_Integer and c > 0 for _,c in P.terms())

assert positive_coeffs(N2, (L,A,B,R))
assert positive_coeffs(Q0, (L,A,B,R))

# Homogeneous degree-four part and its R=0 factor.
PN = sp.Poly(N, L,A,B,R)
N4 = sp.expand(sum(c*L**a[0]*A**a[1]*B**a[2]*R**a[3]
                   for a,c in PN.terms() if sum(a)==4))
fac_R0 = sp.factor(N4.subs(R,0))
expected_R0 = A*B*(A+B+L)*(2*(m+1)*A + 4*m*B + 2*(m+1)*L)
assert sp.expand(fac_R0-expected_R0) == 0

# Three projective boundary charts for q_R/rho.
def qR_hom(l,a,b,r):
    gg=(l+a)/m
    vv=l+b
    ww=a+b
    dd=r+b
    ee=r+a
    ZZ=gg*vv*ww+gg*vv*dd+gg*vv*ee+gg*ww*ee+gg*dd*ee+vv*ww*dd+vv*dd*ee+ww*dd*ee
    return sp.cancel(dd*ee*(gg+vv+ww)/ZZ)

face_beta0 = sp.factor(sp.limit(
    qR_hom(1-alpha-(k+1)*eps, alpha, k*eps, eps)/eps, eps, 0, dir="+"))
face_alpha0 = sp.factor(sp.limit(
    qR_hom(1-beta-(k+1)*eps, k*eps, beta, eps)/eps, eps, 0, dir="+"))
pure_L = sp.factor(sp.limit(
    qR_hom(1-(kA+kB+1)*eps, kA*eps, kB*eps, eps)/eps, eps, 0, dir="+"))

assert sp.factor(face_beta0 - (m+1)*(k+1)/(2-alpha)) == 0
assert sp.factor(face_alpha0 - (k+1)*(beta*(m-1)+m+1)/(beta*(m-2)+2)) == 0
assert sp.factor(pure_L - (m+1)*(kA+1)*(kB+1)/(2*(kA+kB+1))) == 0

print("PATH_PROBABILITIES_SUM_TO_ONE")
print("DELTA_IDENTITY_EXACT")
print("N_m = N_2 + (m-2)(B+R+1)Q_0")
print("N_2_ALL_COEFFICIENTS_POSITIVE")
print("Q_0_ALL_COEFFICIENTS_POSITIVE")
print("R0_LEADING_FACTOR_EXACT:", fac_R0)
print("FACE_BETA0:", face_beta0)
print("FACE_ALPHA0:", face_alpha0)
print("PURE_L:", pure_L)
print("ALL_EXACT_CHECKS_PASS")
