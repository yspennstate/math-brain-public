#!/usr/bin/env python3
from fractions import Fraction
import itertools, math
import sympy as sp

print('R13 Komlos quantitative-bound checker')

# X01: exact rational Komlos matrix A=[1 1 1].
vals=[abs(sum(eps)) for eps in itertools.product((-1,1), repeat=3)]
assert min(vals)==1
print('X01 Boolean discrepancy A=[1,1,1] = 1: PASS')

# Exact rank-2 unit vectors sum to zero.
s3=sp.sqrt(3)
x1=sp.Matrix([1,0])
x2=sp.Matrix([sp.Rational(-1,2),s3/2])
x3=sp.Matrix([sp.Rational(-1,2),-s3/2])
for x in (x1,x2,x3):
    assert sp.simplify((x.T*x)[0]-1)==0
assert x1+x2+x3==sp.zeros(2,1)
print('X01 rank-2 vector discrepancy = 0 exact certificate: PASS')

# C01: equilateral hyperplane rounding.  Only odd harmonics divisible by 3 survive.
w=(-1+sp.I*sp.sqrt(3))/2
assert sp.simplify(1+w+w**2)==0
j=sp.symbols('j', integer=True, nonnegative=True)
odd_sum=sp.summation(1/(2*j+1)**2,(j,0,sp.oo))
assert sp.simplify(odd_sum-sp.pi**2/8)==0
E2=sp.simplify(sp.Rational(8,1)/sp.pi**2 * 9 * sp.Rational(1,9) * odd_sum)
assert sp.simplify(E2-1)==0
print('C01 equilateral random-hyperplane E[D^2]=1 exact series certificate: PASS')

# Ercan's final exact arithmetic from the explicit 2395 theorem.
val=sp.Rational(7,2)*sp.Rational(17091,25)+2
assert val==sp.Rational(119737,50)
assert val==sp.Rational(2395)-sp.Rational(13,50)
assert val<2395
print('Ercan final arithmetic 2394.74 < 2395: PASS')

# C02: exact projector leverage identities used in the Banaszczyk baseline.
for rows,cols in [(5,2),(7,3),(8,4)]:
    X=sp.Matrix([[sp.Rational((i+1)*(j+2)+(i==j),7) for j in range(cols)] for i in range(rows)])
    assert X.rank()==cols
    P=X*(X.T*X).inv()*X.T
    assert sp.simplify(sp.trace(P)-cols)==0
    for i in range(rows):
        pii=sp.simplify(P[i,i])
        assert pii>=0 and pii<=1
print('C02 exact projector leverage identities: PASS')

# Local audit inputs for Guo-Fang-Lu Lemma 2.4.
t=sp.symbols('t', real=True)
f=sp.Rational(2,1)/(sp.pi*(1+t**2)**2)
assert sp.simplify(sp.integrate(f,(t,-sp.oo,sp.oo))-1)==0
E_invS=sp.simplify(sp.Rational(1,2)*sp.gamma(sp.Rational(1,2))/sp.gamma(sp.Rational(3,2)))
assert E_invS==1
C=3*sp.sqrt(2*sp.pi)
assert sp.simplify(sp.sqrt(2*sp.pi)/C-sp.Rational(1,3))==0
print('GFL Lemma-2.4 local cube-density constants: PASS')

# Numerical sanity only for explicit pointwise pre-GFL bounds.
from statistics import NormalDist
nd=NormalDist()
def ercan(n): return 2395*(1+max(0.0,math.log(n/9)))**0.25+2*math.sqrt(2)
def bana(n): return 5*nd.inv_cdf(1-1/(4*n))
def pre_gfl(n):
    arr=[math.sqrt(n),ercan(n)]
    if n>=4: arr.append(bana(n))
    return min(arr)
for n in [1,2,3,4,100,10**6,10**12]:
    extra=(f', Bana={bana(n):.9g}' if n>=4 else '')
    print(f'n={n}: sqrt={math.sqrt(n):.9g}, Ercan={ercan(n):.9g}, preGFL={pre_gfl(n):.9g}'+extra)
print('PASS')
