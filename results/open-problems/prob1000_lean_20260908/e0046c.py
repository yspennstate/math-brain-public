from fractions import Fraction as F
from math import comb
import sympy as sp
def Cbin_half(j):  # generalized binomial C(1/2, j)
    if j == 0: return F(1)
    return F((-1)**(j-1) * comb(2*j, j), 4**j * (2*j-1))
def p(m): return F((2*m+1)*comb(2*m,m), 4**m)          # (3/2)_m / m!
N = 30
r = [sum(p(m)*Cbin_half(k-m)**2 for m in range(k+1)) for k in range(N)]
print("closed form check r_0..r_4:", [str(x) for x in r[:5]])
S = []; acc = F(0)
for k in range(N): acc += r[k]; S.append(acc)          # S_n = sum_{k<n} r_k  -> S[n-1]
c = [F(comb(2*n,n)**2, 16**n) for n in range(N+1)]
print("S_n / c_n for n=1..8:", [str(S[n-1]/c[n]) for n in range(1,9)])
print("S_n / (n c_n):", [str(S[n-1]/(n*c[n])) for n in range(1,9)])
# fit S_n = (A n^2 + B n + C) c_n + (D n^2 + E n + G) c_{n-1}  ?
A,B,C,D,E,G = sp.symbols('A B C D E G')
eqs=[]
for n in range(1, 12):
    eqs.append(sp.Rational(S[n-1].numerator,S[n-1].denominator) - (A*n**2+B*n+C)*sp.Rational(c[n].numerator,c[n].denominator) - (D*n**2+E*n+G)*sp.Rational(c[n-1].numerator,c[n-1].denominator))
print("fit S_n = (An^2+Bn+C) c_n + (Dn^2+En+G) c_{n-1}:", sp.linsolve(eqs, [A,B,C,D,E,G]))
# order-2 recurrence for S_n with degree-2 coefficients
a0,a1,a2,b0,b1,b2,c0,c1,c2 = sp.symbols('a0 a1 a2 b0 b1 b2 c0 c1 c2')
eqs=[]
for n in range(3, 20):
    Sn=lambda i: sp.Rational(S[i-1].numerator,S[i-1].denominator)
    eqs.append((a0+a1*n+a2*n**2)*Sn(n) + (b0+b1*n+b2*n**2)*Sn(n-1) + (c0+c1*n+c2*n**2)*Sn(n-2))
print("order-2 deg-2 recurrence for S_n:", sp.linsolve(eqs, [a0,a1,a2,b0,b1,b2,c0,c1,c2]))
