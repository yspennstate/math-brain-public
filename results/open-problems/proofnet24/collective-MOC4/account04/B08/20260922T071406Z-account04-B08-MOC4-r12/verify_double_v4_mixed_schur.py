from fractions import Fraction
from itertools import permutations
import sympy as sp

# Part I: exact V4 two-point lift combinatorics on the standard channel.
S3 = list(permutations(range(3)))
EVEN_SIGNS = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
v = (1,-1,-1)

def sign_mul(s,t):
    return tuple(a*b for a,b in zip(s,t))

assert set(sign_mul(s,v) for s in EVEN_SIGNS) == set(EVEN_SIGNS)
for eps in (-1,1):
    block = [s for s in EVEN_SIGNS if s[0] == eps]
    assert len(block) == 2
    assert sign_mul(block[0],v) == block[1]
    assert sign_mul(block[1],v) == block[0]
    assert all(sum(s[j] for s in block) == 0 for j in (1,2))

lams = [Fraction(k,21) for k in (1,2,3,4,5,6)]
assert sum(lams) == 1
m = [Fraction(-1,2), Fraction(1,3), Fraction(2,5)]

R = [[Fraction(0) for _ in range(3)] for _ in range(3)]
for lam,rho in zip(lams,S3):
    for j in range(3):
        R[rho[j]][j] += lam

Dtarget = [[Fraction(0) for _ in range(3)] for _ in range(3)]
for alpha in range(3):
    Dtarget[alpha][0] = R[alpha][0] * m[alpha]

mu = {}
for lam,rho in zip(lams,S3):
    alpha = rho[0]
    for s in EVEN_SIGNS:
        eps = s[0]
        w = lam * (1 + eps*m[alpha]) / 4
        assert w >= 0
        mu[(rho,s)] = w
assert sum(mu.values()) == 1

Rmu = [[Fraction(0) for _ in range(3)] for _ in range(3)]
Dmu = [[Fraction(0) for _ in range(3)] for _ in range(3)]
for (rho,s),w in mu.items():
    for j in range(3):
        alpha = rho[j]
        Rmu[alpha][j] += w
        Dmu[alpha][j] += w*s[j]
assert Rmu == R
assert Dmu == Dtarget
for (rho,s),w in mu.items():
    assert mu[(rho,sign_mul(s,v))] == w

# Part II: exact local Spin(4) mixed-Schur identities.
ra, rb, s2, c33 = sp.symbols('ra rb s2 c33', positive=True, real=True)
c1,c2,d1,d2 = sp.symbols('c1 c2 d1 d2', real=True)
u1,u2,v1,v2,t = sp.symbols('u1 u2 v1 v2 t', real=True)
A = ra**2
B = rb**2
U2 = u1**2+u2**2
V2 = v1**2+v2**2
x3 = sp.sqrt(1-4*t**2*U2)
y3 = sp.sqrt(1-4*t**2*V2)
p3 = A/2-c33
q3 = B/2-c33
N11 = ra*rb/2
N22 = s2/4

F = (
    -2*t*(c1*u1+c2*u2) + p3*x3
    -2*t*(d1*v1+d2*v2) + q3*y3
    +4*t**2*(N11*u1*v1+N22*u2*v2)
    +2*t*(c1*u1+c2*u2)*y3
    +2*t*x3*(d1*v1+d2*v2)
    +c33*x3*y3
)
series = sp.series(F,t,0,5).removeO().expand()
P2 = sp.factor(series.coeff(t,2))
P3 = sp.factor(series.coeff(t,3))
P4 = sp.factor(series.coeff(t,4))
P2_expected = -A*U2-B*V2+2*ra*rb*u1*v1+s2*u2*v2
P3_expected = -4*((c1*u1+c2*u2)*V2+(d1*v1+d2*v2)*U2)
P4_expected = -A*U2**2-B*V2**2+4*c33*U2*V2
assert sp.simplify(P2-P2_expected) == 0
assert sp.simplify(P3-P3_expected) == 0
assert sp.simplify(P4-P4_expected) == 0

zsub = {u1:rb,u2:0,v1:ra,v2:0}
J3_poly = 6*P3_expected
J4_poly = 24*P4_expected
J3z = sp.factor(J3_poly.subs(zsub))
assert sp.simplify(J3z + 24*ra*rb*(ra*c1+rb*d1)) == 0

d1ker = -ra*c1/rb
ell = [sp.simplify(sp.diff(J3_poly,z).subs(zsub)/3) for z in (u1,u2,v1,v2)]
ell = [sp.factor(e.subs(d1,d1ker)) for e in ell]
ell_expected = [8*A*c1, -8*A*c2, -8*ra*rb*c1, -8*B*d2]
assert all(sp.simplify(x-y)==0 for x,y in zip(ell,ell_expected))

J4z = sp.factor(J4_poly.subs(zsub))
delta = A+B-4*c33
assert sp.simplify(J4z + 24*A*B*delta) == 0

D = 4*A*B-s2**2
lu1,lu2,lv1,lv2 = ell
reserve = ((ra*lu1-rb*lv1)**2/(2*(A+B)**2)
           +(2*B*lu2**2+2*s2*lu2*lv2+2*A*lv2**2)/D)
reserve_target = (32*A*c1**2
                  +128*A*B*(A*c2**2+s2*c2*d2+B*d2**2)/D)
assert sp.simplify(reserve-reserve_target) == 0
phi = 4*c1**2/B + 16*(A*c2**2+s2*c2*d2+B*d2**2)/D
assert sp.simplify(J4z+3*reserve + 24*A*B*(delta-phi)) == 0

print('PASS MOC4-DOUBLE-V4-MIXED-SCHUR-BRIDGE-v1')
print('two_point_lift_mass =', sum(mu.values()))
print('two_point_lift_R_match =', Rmu == R)
print('two_point_lift_D_match =', Dmu == Dtarget)
print('two_point_lift_v_invariant = True')
print('J3_kernel_factor =', J3z)
print('ell_kernel =', ell)
print('J4_kernel =', J4z)
print('reserve =', sp.factor(reserve_target))
print('LS_equivalence: J4+3R = -24*a*b*(delta-phi)')
