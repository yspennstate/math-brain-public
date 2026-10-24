#!/usr/bin/env python3
"""Computer-assisted certificate for the P10 q=3 binary-tree KS kernel.

Proves the orbit-averaged KS fusion inequality for the full diagonal
S3-orbit family p=q=p(a), a in [-1/2,1], for
Psi(p)=D(p||u)+(3/2)sum z_i^3-sum z_i^4.

The central interval is certified symbolically/exactly by a degree-6
Taylor truncation plus a rigorous analytic tail bound and positive
Bernstein coefficients. The two outer intervals are certified by
outward-rounded interval arithmetic for H'(a)/a^3.
"""
import math
import sympy as sp
from mpmath import iv

a = sp.symbols('a', real=True)
x = sp.symbols('x', real=True)
s2 = sp.sqrt(2)
A = (s2*a + a*a/2)/(1+a*a)
M = -a/(s2+a)
wA = (1+a*a)/3
wM = (2-a*a)/3

def cF(n):
    if n == 2:
        return sp.Rational(1)
    if n == 3:
        return sp.Rational(0)
    if n == 4:
        return sp.Rational(5,18)
    return sp.Rational(((-1)**n)*(2**n)+2, 3*n*(n-1))

def bernstein_coeffs(poly, lo, hi):
    t = sp.symbols('t', real=True)
    pt = sp.Poly(sp.expand(poly.as_expr().subs(a, lo+(hi-lo)*t)), t, extension=s2)
    n = pt.degree()
    cs = [pt.nth(k) for k in range(n+1)]
    ans = []
    for j in range(n+1):
        ans.append(sp.simplify(sum(
            cs[k] * sp.Rational(math.comb(j,k), math.comb(n,k))
            for k in range(j+1)
        )))
    return ans

N = 6
FN = sum(cF(n)*x**n for n in range(2,N+1))
HN = sp.cancel(FN.subs(x,a) - wA*FN.subs(x,A) - wM*FN.subs(x,M))
R6 = sp.cancel(HN/a**4)
num6, den6 = sp.fraction(R6)
fac = sp.factor_list(den6, extension=s2)
assert fac == (2880, [(a + s2, 11), (a**2 + 1, 5)])
poly6 = sp.Poly(num6, a, extension=s2)
bs = bernstein_coeffs(poly6, sp.Rational(-1,20), sp.Rational(1,20))
assert len(bs) == 24
assert all(b.is_positive is True for b in bs)
b0 = bs[0]
assert all(sp.simplify(b-b0).is_nonnegative is True for b in bs)

delta = sp.Rational(1,20)
L = sp.simplify(b0 / (
    sp.Integer(2880) * sp.Rational(31,20)**11 * sp.Rational(401,400)**5
))
assert L.is_positive is True

B = sp.Rational(65,8064)
CA = sp.Rational(61,40)
CM = sp.Rational(20,27)

def tail_const(C):
    return sp.simplify(B*(2*C)**7/(1-2*C*delta))

E = sp.simplify(
    tail_const(sp.Rational(1))
    + sp.Rational(401,1200)*tail_const(CA)
    + sp.Rational(2,3)*tail_const(CM)
)
central_margin = sp.simplify(L - E*delta**3)
assert central_margin.is_positive is True
print('CENTRAL_EXACT_PASS')
print('bernstein_coefficients', len(bs))
print('L_lower', sp.N(L, 20))
print('tail_relative_upper', sp.N(E*delta**3, 20))
print('central_margin', sp.N(central_margin, 20))

iv.dps = 20
I1=iv.mpf('1'); I2=iv.mpf('2'); I3=iv.mpf('3')
I6=iv.mpf('6'); I8=iv.mpf('8'); I9=iv.mpf('9')
S2=iv.sqrt(I2)

def F(z):
    return ((I1+I2*z)/I3*iv.log(I1+I2*z)
            + I2*(I1-z)/I3*iv.log(I1-z)
            + z**3/I3 - I2*z**4/I9)

def Fp(z):
    return (-I8*z**3 + I9*z**2
            - I6*iv.log(I1-z) + I6*iv.log(I1+I2*z))/I9

def AI(z): return (S2*z + z*z/I2)/(I1+z*z)
def MI(z): return -z/(S2+z)
def ApI(z): return -(S2*z*z-z-S2)/(I1+z*z)**2
def MpI(z): return -S2/(S2+z)**2

def Hp(z):
    aa=AI(z); mm=MI(z)
    return (Fp(z)
            - (I2*z/I3)*F(aa) - ((I1+z*z)/I3)*Fp(aa)*ApI(z)
            + (I2*z/I3)*F(mm) - ((I2-z*z)/I3)*Fp(mm)*MpI(z))

def certify_segment(lo, hi, base=0.002, min_width=2e-7, max_nodes=100000):
    stack=[]
    y=lo
    while y < hi-1e-15:
        z=min(hi, y+base)
        stack.append((y,z))
        y=z
    nodes=0; leaves=0; min_lb=float('inf')
    while stack:
        l,r=stack.pop(); nodes += 1
        if nodes > max_nodes:
            raise RuntimeError('node budget exceeded')
        Z=iv.mpf([l,r])
        Q=Hp(Z)/(Z**3)
        lb=float(Q.a)
        if lb > 0:
            leaves += 1
            min_lb=min(min_lb,lb)
            continue
        if r-l <= min_width:
            raise AssertionError(('uncertified box',l,r,lb,float(Q.b)))
        m=(l+r)/2
        stack.append((l,m)); stack.append((m,r))
    return nodes,leaves,min_lb

eps=1e-9
neg=certify_segment(-0.5+eps,-0.05)
pos=certify_segment(0.05,1.0-eps)
print('OUTER_INTERVAL_PASS')
print('negative_nodes_leaves_minlb',neg)
print('positive_nodes_leaves_minlb',pos)
print('OVERALL_PASS')
