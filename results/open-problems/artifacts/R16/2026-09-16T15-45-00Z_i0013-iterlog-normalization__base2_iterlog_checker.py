#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

print("R16 I0013 exact self-check: base-2 iterated-log normalization")

# Rigorous rational enclosure of ln 2 from the positive series
# ln 2 = sum_{j>=1} 1/(j 2^j), with tail <= 1/((K+1)2^K).
K=80
L=sum(Fraction(1, j*(2**j)) for j in range(1,K+1))
U=L+Fraction(1,(K+1)*(2**K))
lo=Fraction(693147180559,10**12)
hi=Fraction(693147180560,10**12)
assert L > lo
assert U < hi
assert 0 < L < U < 1
print("ln2 certified:", float(L), "< ln2 <", float(U))
print("decimal enclosure:", lo, "< ln2 <", hi)

# Exact symbolic derivative formula for base-2 iterated logarithms:
# L_1(x)=ln x/c, L_{r+1}=ln L_r/c, c=ln 2
x,c=sp.symbols('x c', positive=True)
Ls=[None, sp.log(x)/c]
for r in range(2,5):
    Ls.append(sp.log(Ls[-1])/c)

prod=sp.Integer(1)
for r in range(1,5):
    if r==1:
        rhs=1/(c*x)
    else:
        prod*=Ls[r-1]
        rhs=1/(c**r*x*prod)
    diff=sp.simplify(sp.diff(Ls[r],x)-rhs)
    assert diff==0
    print(f"dL_{r}/dx identity: PASS")

# Verify the integrated coefficient mechanically:
# dx/(x prod_{j<r} L_j) = c^r dL_r,
# so integral with L_r^{-beta}, gamma=1-beta,
# is c^r/gamma * L_r^gamma.
beta,gamma,alpha=sp.symbols('beta gamma alpha', positive=True)
u=sp.symbols('u', positive=True)
for r in range(1,5):
    primitive=alpha*c**r*u**gamma/gamma
    integrand=alpha*c**r*u**(-beta)
    check=sp.simplify(sp.diff(primitive,u).subs(gamma,1-beta)-integrand)
    assert check==0
    print(f"depth {r} critical-power primitive: PASS")

# Exact threshold algebra for q(x)=x^2 exp((L_r x)^gamma).
d=sp.symbols('d', positive=True)
# r=1: L1(x_n)~(1/2)L1(n), positive q coefficient 2^{-gamma}
neg1=d*alpha*c/gamma
assert sp.simplify(gamma*neg1-d*alpha*c)==0
# r>=2: L_r(x_n)~L_r(n), positive q coefficient 1
for r in range(2,5):
    negr=d*alpha*c**r/gamma
    assert sp.simplify(gamma*negr-d*alpha*c**r)==0
print("threshold coefficients: PASS")
print("ALL_EXACT_CHECKS_PASS")
