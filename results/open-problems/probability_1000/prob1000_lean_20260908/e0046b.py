"""Exact rationals r_k = a_k / Gamma(3/2), a_k = int sqrt(x) e^{-x} L_k(x)^2 dx, via L_k = sum_i C(k,i)(-x)^i/i! and
int x^{1/2+m} e^{-x} = Gamma(3/2) (3/2)_m.  Then look for a holonomic recurrence and a closed form."""
from fractions import Fraction as F
from math import comb
def poch32(m):
    p = F(1)
    for t in range(m): p *= F(3,2) + t
    return p
def r(k):
    s = F(0)
    for i in range(k+1):
        for j in range(k+1):
            s += F(comb(k,i)*comb(k,j)*(-1)**(i+j), 1) * poch32(i+j) / (F(1)*__import__('math').factorial(i)*__import__('math').factorial(j))
    return s
R = [r(k) for k in range(0, 16)]
print("r_k:", [str(x) for x in R[:10]])
D = [R[k]-R[k-1] for k in range(1,16)]
print("d_k = r_k - r_{k-1}:", [str(x) for x in D[:9]])
print("d_k * 4^k (numerators?):", [str(D[k-1]*4**k) for k in range(1,10)])
print("d_k * 16^k:", [str(D[k-1]*16**k) for k in range(1,10)])
# try: d_k = c * C(2k,k)^2 / 16^k * (something rational in k)?
c2 = [F(comb(2*k,k)**2, 16**k) for k in range(1,16)]
print("d_k / (C(2k,k)^2/16^k):", [str(D[k-1]/c2[k-1]) for k in range(1,12)])
# fit a linear recurrence with polynomial coefficients of degree <=2, order 2, for r_k:  (a0+a1 k+a2 k^2) r_k + (b0+..) r_{k-1} + (c0+..) r_{k-2} = 0
import sympy as sp
ks = list(range(2,16))
unk = sp.symbols('a0 a1 a2 b0 b1 b2 c0 c1 c2')
eqs = []
for k in ks:
    a = unk[0]+unk[1]*k+unk[2]*k**2; b = unk[3]+unk[4]*k+unk[5]*k**2; c = unk[6]+unk[7]*k+unk[8]*k**2
    eqs.append(sp.Rational(R[k].numerator,R[k].denominator)*a + sp.Rational(R[k-1].numerator,R[k-1].denominator)*b + sp.Rational(R[k-2].numerator,R[k-2].denominator)*c)
sol = sp.linsolve(eqs, unk)
print("order-2 degree-2 recurrence solutions:", sol)
