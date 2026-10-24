# Shifting (compression) S_ij replaces f(x_i=1,x_j=0,y), f(x_i=0,x_j=1,y) by their max and min.  For monotone f it never
# increases total influence and ends at a regular function; if it also never lowered entropy by more than C times the
# influence it removes, FEI for regular functions would give FEI for all monotone functions.  This checks one step on
# f = x_i x_j OR x_i y_1 OR x_j y_2 (variables 0=x_i, 1=x_j, 2=y_1, 3=y_2).
import numpy as np
from mono_enum import walsh, phi
def table(fun, n):
    m = 0
    for x in range(1 << n):
        if fun([(x >> k) & 1 for k in range(n)]): m |= 1 << x
    return np.array([m], dtype=np.uint64)
def HI(mask, n):
    G = walsh(mask, n)[0]; P = G * G
    sizes = np.array([bin(s).count('1') for s in range(1 << n)])
    return float(phi(P).sum()), float((P * sizes).sum()), P
f  = lambda v: (v[0] and v[1]) or (v[0] and v[2]) or (v[1] and v[3])
fs = lambda v: (v[0] and v[1]) or (v[0] and (v[2] or v[3])) or (v[1] and v[2] and v[3])
def shift(fun, i, j, n):          # the compression, computed from the truth table itself
    def g(v):
        if v[i] == v[j]: return fun(v)
        a = list(v); a[i], a[j] = 1, 0
        b = list(v); b[i], b[j] = 0, 1
        hi, lo = max(bool(fun(a)), bool(fun(b))), min(bool(fun(a)), bool(fun(b)))
        return hi if v[i] == 1 else lo
    return g
n = 4
H0, I0, P0 = HI(table(f, n), n)
H1, I1, P1 = HI(table(fs, n), n)
H2, I2, _ = HI(table(shift(f, 0, 1, n), n), n)
print('f            : H = %.6f bits, I = %.6f' % (H0, I0))
print('S_ij f (hand): H = %.6f bits, I = %.6f' % (H1, I1))
print('S_ij f (code): H = %.6f bits, I = %.6f   (hand formula matches: %s)' % (H2, I2, abs(H1 - H2) < 1e-12 and abs(I1 - I2) < 1e-12))
print('entropy drop %.6f bits with influence drop %.2e' % (H0 - H1, I0 - I1))
