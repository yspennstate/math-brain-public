from fractions import Fraction as F
from math import comb, factorial, log, pi
import mpmath as mp
def h(k): return sum(F(1, j) for j in range(1, k+1))
def B(a, b): return F(factorial(a-1)*factorial(b-1), factorial(a+b-1))
m = [F(1)]
for k in range(1, 6):
    num = k*m[k-1] + F(1, 2)*sum(comb(k, j)*m[j]*m[k-j]*B(2*j, 2*k-2*j) for j in range(1, k))
    m.append(num / h(2*k-1))
print('m_k', [str(x) for x in m[:5]])
v = m[2]-1; s3 = m[3]-3*m[2]+2; s4 = m[4]-4*m[3]+6*m[2]-3
print('QC skew', float(s3/v**1.5), 'kurt', float(s4/v**2))
mp.mp.dps = 30
H = lambda x: -x*mp.log(x)-(1-x)*mp.log(1-x)
nu = lambda x: 1/(2*x*(1-x))
J = lambda r: mp.quad(lambda x: H(x)**r*nu(x), [0, 0.5, 1])
z = mp.zeta(2); z3 = mp.zeta(3); z4 = mp.zeta(4)
print('J2', J(2), 2*z3 - z)
print('J3', J(3), 6*z4 - 3*z3 - 1.5*z)
kap = (2*z3-z)/z**2; a3 = kap/z - 2*J(3)/(3*z**3)
I3 = mp.quad(lambda x: H(x)**2*(x**2+(1-x)**2)*nu(x), [0, 0.5, 1])
a4 = mp.mpf(6)/11*(kap**2/2 + 3*a3/z + 6*kap/z**2*I3 + J(4)/z**4)
print('kappa', kap, 'a3', a3, 'a4', a4, 'skew', a3/kap**1.5, 'kurt', a4/kap**2)
