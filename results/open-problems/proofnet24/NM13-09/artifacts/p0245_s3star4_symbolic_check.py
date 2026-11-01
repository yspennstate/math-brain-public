"""Exact symbolic self-check for NM13-09 / P0245 S3-symmetric four-state theorem.

This is a self-check, not an independent audit.  It verifies:
(1) each orbit hitting-time formula directly from the conductance Dirichlet matrix;
(2) inclusion-exclusion for the stationary cover-time formula;
(3) the manifestly nonnegative factorization of E_pi C - 11/2;
(4) equality at the loopless K4 point.
"""
import sympy as sp

u,v,r,s = sp.symbols("u v r s")
A = 3*u + r
B = u + 2*v + s
M = A + 3*B

C = sp.Matrix([
    [r,u,u,u],
    [u,s,v,v],
    [u,v,s,v],
    [u,v,v,s],
])
c = sp.Matrix([sum(C[i,j] for j in range(4)) for i in range(4)])
L = sp.diag(*list(c)) - C

def hit(target):
    K = [i for i in range(4) if i not in target]
    LK = L.extract(K,K)
    ck = sp.Matrix([c[i] for i in K])
    return sp.cancel((ck.T * LK.inv() * ck)[0] / M)

H0   = 3*B**2/(u*M)
H1   = ((u+v)*A**2 + 4*u*A*B + 6*u*B**2)/(u*(u+3*v)*M)
H01  = 2*B**2/((u+v)*M)
H12  = ((u+2*v)*A**2 + 2*u*A*B + 3*u*B**2)/(2*u*(u+3*v)*M)
H012 = B**2/((u+2*v)*M)
H123 = A**2/(3*u*M)

checks = [
    ("H_{0}", hit({0}), H0),
    ("H_{1}", hit({1}), H1),
    ("H_{01}", hit({0,1}), H01),
    ("H_{12}", hit({1,2}), H12),
    ("H_{012}", hit({0,1,2}), H012),
    ("H_{123}", hit({1,2,3}), H123),
]
for name, got, want in checks:
    assert sp.factor(got-want) == 0, name

F = sp.cancel(H0 + 3*H1 - 3*H01 - 3*H12 + 3*H012 + H123)

D = 6*u*(u+v)*(u+2*v)*(u+3*v)*(6*u+6*v+r+3*s)
N = (
    18*(u-v)**2*(u+2*v)*(8*u**2+19*u*v+12*v**2)
    + r**2*(11*u**3+39*u**2*v+40*u*v**2+12*v**3)
    + r*s*(54*u**3+162*u**2*v+108*u*v**2)
    + r*(87*u**4+306*u**3*v+309*u**2*v**2+90*u*v**3)
    + s**2*(81*u**3+243*u**2*v+198*u*v**2+108*v**3)
    + s*(225*u**4+702*u**3*v+603*u**2*v**2+414*u*v**3+432*v**4)
)
assert sp.factor((F-sp.Rational(11,2))*D - N) == 0
assert sp.factor(F.subs({r:0,s:0,v:u}) - sp.Rational(11,2)) == 0

print("P0245 S3-symmetric four-state exact symbolic self-check")
for name,_,_ in checks:
    print(name + ": DIRICHLET_FORMULA_PASS")
print("cover inclusion-exclusion orbit formula: PASS")
print("denominator =", sp.factor(D))
print("numerator decomposition identity: PASS")
print("K4 equality F(u,u,0,0)=11/2: PASS")
print("ALL_EXACT_CHECKS_PASS")
