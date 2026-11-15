"""Exact checks for RESULT.md. Run with OMP_NUM_THREADS=1 python3 exact_audit.py.
No floating-point arithmetic is used. Sympy is needed for symbolic identities.
"""
import os
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import random
import time
from fractions import Fraction as F
import sympy as s

start = time.monotonic()
def check_zero(expr):
    assert s.factor(expr) == 0, s.factor(expr)

g,p,z,d,u=s.symbols('g p z d u', real=True)
check_zero(d*u*z-(u-z)**2 + (u-(1+d/2)*z)**2-d*(1+d/4)*z**2)
P=(2+g)/(20*g)
check_zero(7+16*g-(200*g-70)*P-5-(3*g-2)*(4*g-7)/(2*g))
check_zero(120*g-(200*g-70)*(3+5*P)/4-5*(14+51*g-68*g**2)/(8*g))
print('PROVED: moment completion and n=5 coefficient identities verified symbolically.')

# Check the moment bound independently by rational zero-sum vectors, without square roots.
rng=random.Random(20261113)
for k in range(3000):
    x=[F(rng.randrange(-100,101),rng.randrange(1,15)) for _ in range(4)]
    x.append(-sum(x)); R=sum(t*t for t in x)
    if not R: continue
    p0=max(-x[i]*x[j] for i in range(5) for j in range(i))
    P3=sum(t**3 for t in x); P4=sum(t**4 for t in x)
    assert 4*P4*R**2 <= 4*p0*R**3+(3*R+5*p0)*P3**2
print('PROVED: moment bound holds on 3000 exact rational checks (corroboration only).')

a,b,lam,beta=s.symbols('a b lam beta',positive=True)
n=a+b+1; c=2*n/(n-2)
Aa=2-c*(1/a-1/n); Ab=2-c*(1/b-1/n)
ha=lam*a/n; hb=lam*b/n
ell_a=lam*(2-2/n-2/a); ell_b=lam*(2-2/n-2/b)
da=ell_a-Aa*ha; db=ell_b-Ab*hb
K=4*((n-1)/(n-2)-1/a-1/b)
check_zero(da-2*lam*(b-1)*((n-1)*a-n)/(n*a*(n-2)))
check_zero(da/hb+db/ha-K+2*(n-3)/(a*b*(n-2)))
check_zero(Aa/b+Ab/a-2*(n**2-4*n+1)/(a*b*(n-2)))
check_zero((da+lam*Aa/(n*(n-2)))/hb+(db+lam*Ab/(n*(n-2)))/ha-K-2*(n-5)/(a*b*(n-2)**2))
print('PROVED: equitable singleton-case coefficient identities verified symbolically.')

# Explicit equitable counterexample to the stronger inequality.
W=s.zeros(5)
for i in range(1,5): W[0,i]=W[i,0]=s.Rational(1,8)
for i,j in [(1,3),(2,4)]: W[i,j]=W[j,i]=s.Rational(49,200)
for i,j in [(1,4),(2,3)]: W[i,j]=W[j,i]=s.Rational(1,200)
assert sum(W)==2
L=s.diag(*list(W*s.ones(5,1)))-W
H=s.eye(5)-s.ones(5)/5
lam=s.Rational(5,8); G=lam*H-L
Pi=s.diag(1,s.Rational(1,2),s.Rational(1,2),s.Rational(1,2),s.Rational(1,2))
Pi[1,2]=Pi[2,1]=Pi[3,4]=Pi[4,3]=s.Rational(1,2)
Pi-=s.ones(5)/5
assert Pi*Pi==Pi and Pi*G==s.zeros(5) and s.trace(Pi)==2
assert L.eigenvals()=={0:1,s.Rational(27,200):1,s.Rational(123,200):1,lam:2}
M=Pi.multiply_elementwise(G)
X1=2*s.trace(L*G); X2=s.Rational(10,3)*s.trace(G*M)
X3=(1-lam)/3*(2*s.trace(G)-s.Rational(10,3)*s.trace(M))
Y=0
for i in range(5):
    for j in range(i):
        Y+=2*W[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j])
assert X1+X2-Y == -s.Rational(143,10000)
assert X1+X2+X3-Y == s.Rational(241,5000)
print('PROVED: explicit q=3 equitable example has spectrum',L.eigenvals())
print('X1 =',X1,'X2 =',X2,'X3 =',X3,'2S5 =',Y)
print('X1+X2-2S5 =',X1+X2-Y,'T =',X1+X2+X3-Y)
print('All exact audits passed; seconds = %.3f'%(time.monotonic()-start))
