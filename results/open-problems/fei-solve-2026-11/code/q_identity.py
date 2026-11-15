"""Check of FLOW 12(bb) item 3 on functions with full spectral support.

Q(T,i) = mu(T+i)/I, pi = T-marginal of Q.  Identity:
    E_Q log2(mu(T)/mu(T+i)) = H_Q(i|T) - log2 I - D(pi || mu).
Also prints the two positive parts and L = E_Q log2(1 + mu(T)/mu(T+i)).
Exact transforms, float64.
"""
import sys

import numpy as np

from predictor import wht, f_and, f_tribes, f_pmk33, f_rand


def check(name, f, n):
    mu = wht(f) ** 2
    N = 1 << n
    idx = np.arange(N)
    pc = np.zeros(N)
    for i in range(n):
        pc += (idx >> i) & 1
    I = float((pc * mu).sum())
    signed = 0.0
    pos = 0.0
    neg = 0.0
    L = 0.0
    HiT = 0.0
    pi = np.zeros(N)
    full = True
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]
        a = mu[lo]
        b = mu[lo | (1 << i)]
        pi[lo] += b / I
        m = b > 1e-300
        if (a[m] <= 1e-300).any():
            full = False
            continue
        r = np.log2(a[m] / b[m])
        signed += float((b[m] * r).sum()) / I
        pos += float((b[m] * np.maximum(r, 0)).sum()) / I
        neg += float((b[m] * np.maximum(-r, 0)).sum()) / I
        L += float((b[m] * np.log2(1 + a[m] / b[m])).sum()) / I
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]
        b = mu[lo | (1 << i)] / I
        m = b > 1e-300
        HiT += float((b[m] * np.log2(pi[lo][m] / b[m])).sum())
    if not full:
        print("%-16s spectrum not full: signed form infinite; skipped" % name)
        return
    m = pi > 1e-300
    D = float((pi[m] * np.log2(pi[m] / mu[m])).sum())
    rhs = HiT - np.log2(I) - D
    print("%-16s n %2d  I %.5f  signed %.9f  rhs %.9f  diff %.2e   pos %.5f  neg %.5f  L %.5f  H(i|T) %.5f  D(pi||mu) %.5f"
          % (name, n, I, signed, rhs, signed - rhs, pos, neg, L, HiT, D))


def main():
    check("AND 4", f_and(4), 4)
    check("AND 8", f_and(8), 8)
    check("tribes 2x3", f_tribes(2, 3), 6)
    check("tribes 3x4", f_tribes(3, 4), 12)
    check("PM(K33)", f_pmk33(), 9)
    for n in (6, 9):
        check("random %d" % n, f_rand(n, 5), n)


if __name__ == "__main__":
    sys.exit(main())
