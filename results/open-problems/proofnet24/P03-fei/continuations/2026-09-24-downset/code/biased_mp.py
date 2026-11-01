# High-precision (mpmath, 60 digits) evaluation of the biased strengthened ratio for a monotone function given by its
# truth-table mask, at given biases; used to check whether float values above 2 + 4 log2 e are rounding.
import sys, mpmath as mp
mp.mp.dps = 60
def ratio_mp(mask, m, q):
    q = [mp.mpf(v) for v in q]
    N = 1 << m
    vals = [mp.mpf(-1) if (mask >> x) & 1 else mp.mpf(1) for x in range(N)]
    a = vals[:]
    for j in range(m):
        nu = 2 * q[j] - 1; s = mp.sqrt(1 - nu * nu); ph1 = (1 - nu) / s; ph0 = (-1 - nu) / s
        b = a[:]
        for idx in range(N):
            if (idx >> j) & 1 == 0:
                x0 = a[idx]; x1 = a[idx | (1 << j)]
                b[idx] = (1 - q[j]) * x0 + q[j] * x1
                b[idx | (1 << j)] = (1 - q[j]) * ph0 * x0 + q[j] * ph1 * x1
        a = b
    L = mp.mpf(0); I = mp.mpf(0); V = mp.mpf(0)
    for A in range(1, N):
        P = a[A] ** 2
        k = bin(A).count('1')
        sig2 = mp.mpf(1)
        for j in range(m):
            if (A >> j) & 1: sig2 *= 1 - (2 * q[j] - 1) ** 2
        if P > 0: L += P * mp.log(sig2 / P, 2)
        I += k * P; V += P
    return L / (I - V)
if __name__ == '__main__':
    C = 2 + 4 / mp.log(2)
    cases = [(0xe, 2, [1.8e-06, 1e-07]), (0xfe, 3, [1e-07, 1e-07, 1.2e-06]), (0xffaa, 4, [2.5e-06, 1e-07, 1e-07, 1e-07]), (0xffccffcc, 5, [1e-07, 1e-07, 1e-07, 2.6e-06, 1e-07])]
    for mask, m, q in cases:
        r = ratio_mp(mask, m, q)
        print('mask %s biases %s: ratio %s ; minus (2 + 4 log2 e) = %s' % (hex(mask), q, mp.nstr(r, 12), mp.nstr(r - C, 6)))
