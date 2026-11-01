# T084, agent B: negative control - S8 at its true basis-failing pair (3,7). The certificate must fail, and N must be
# negative at some (q, y): take q small and y = s * (1,..,1) small, where the basis term dominates.
from fractions import Fraction as Fr
exec(open('amgm_cert.py').read().split("if __name__")[0])
A = [0b0111, 0b1011, 0b1101, 0b1111]
cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
r = certify('S8 true bad pair', cols, 3, 7)
C = Npoly(cols, 3, 7)
for qv, s in [(sp.Rational(1, 10**4), sp.Rational(1, 100)), (sp.Rational(1, 10**6), sp.Rational(1, 1000)), (sp.Rational(1, 100), sp.Rational(1, 10))]:
    val = sum(c.subs(q, qv) * s ** sum(m) for m, c in C.items())
    print('q', qv, 'y', s, 'N =', float(val))
