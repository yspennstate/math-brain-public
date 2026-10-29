"""Control for kappa.py: the same support inversion applied to the raw q-coefficients of N (no division by
(1-q)^2). N itself has coefficients of both signs, so this must show negative kappa; if it did not, the
positivity in kappa.py would say nothing about D3. python kappa_control.py adj|dis NMAX"""
import sys
from math import comb
import rec
kind, NMAX = sys.argv[1], int(sys.argv[2])
V0 = 3 if kind == 'adj' else 4
C = {}
for n in range(V0, NMAX + 1):
    d = {}
    for k, x in enumerate(rec.Npoly(n, kind)):
        for i, c in enumerate(int(c) for c in x.coeffs()):
            if c:
                for s in range(k + 1):
                    d[(i, s - (2 * n - i))] = d.get((i, s - (2 * n - i)), 0) + c * comb(k, s) * (-1) ** s
    C[n] = d
keys = set().union(*C.values())
neg = pos = 0
for key in keys:
    for r in range(NMAX - V0 + 1):
        kap = sum((-1) ** (r - m) * comb(r, m) * C[m + V0].get(key, 0) for m in range(r + 1))
        neg += kap < 0
        pos += kap > 0
print(kind, 'raw-N kappa: positive', pos, 'negative', neg)
