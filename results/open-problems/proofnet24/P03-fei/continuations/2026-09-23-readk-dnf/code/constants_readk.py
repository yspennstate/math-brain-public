from fractions import Fraction
import math
def tau(m, beta):
    # Pr[Bin(m-1,1/2) < m/beta - 1], exact rational
    s = Fraction(0)
    for j in range(m):
        if j < Fraction(m, 1)/beta - 1:
            s += math.comb(m-1, j)
    return s / 2**(m-1)
def Cbeta(beta, M=4000):
    best = (0, 0)
    for m in range(1, M):
        v = m*tau(m, beta)
        if v > best[0]: best = (float(v), m)
    return best
for beta in [Fraction(5,2), Fraction(3), Fraction(7,2), Fraction(4), Fraction(9,2), Fraction(5), Fraction(6), Fraction(8)]:
    cb, marg = Cbeta(beta, 600)
    for k in (1,2,3,4,10):
        pass
    print(f"beta={float(beta):4.1f}  C_beta={cb:.4f} (at m={marg})  beta+C_beta={float(beta)+cb:.4f}  "
          + "  ".join(f"C_{k}={2.885+11.542+k*(k+1)*(float(beta)+cb):.1f}" for k in (1,2,3,5)))
