"""Compare superbase laws of two discretizations of conformally equivalent tori, and fit exp(-c * sum|v|^2 / Im tau).

Usage: python compare.py "<glob A>" "<glob B>" m11 m12 m21 m22
The matrix sends a class (a, b) of B to the class (m11*a + m12*b, m21*a + m22*b) of A (for B's tau' = g tau).
Prints, for each superbase of A, P_A, P_B (mapped), and sum |v|^2 / Im tau in A's modulus."""
import glob
import math
import sys
from collections import Counter


def load(pattern, M=None):
    cnt, tot, tau = Counter(), 0, None
    for fn in sorted(glob.glob(pattern)):
        for line in open(fn, encoding="utf-8"):
            f = line.rstrip("\n").split("\t")
            n1, n2, sh, m, s = f if len(f) == 5 else (f[0], f[1], "0", f[2], f[3])
            tau = complex(int(sh), int(n2)) / int(n1)
            tot += 1
            if int(m) != 3:
                cnt["fig8"] += 1
                continue
            cls = [tuple(map(int, x.split(","))) for x in s.split(";")]
            if M:
                cls = [(M[0] * a + M[1] * b, M[2] * a + M[3] * b) for a, b in cls]
            norm = []
            for a, b in cls:
                if a < 0 or (a == 0 and b < 0):
                    a, b = -a, -b
                norm.append((a, b))
            cnt[tuple(sorted(norm))] += 1
    return cnt, tot, tau


A, tA, tauA = load(sys.argv[1])
B, tB, tauB = load(sys.argv[2], tuple(int(x) for x in sys.argv[3:7]) if len(sys.argv) > 6 else None)
print(f"A: {tA} samples tau {tauA:.4f}   B: {tB} samples tau {tauB:.4f}")
print(f"figure-eight  A {A['fig8'] / tA:.4f}  B {B['fig8'] / tB:.4f}")
top = A.most_common(1)[0]
q0 = None
for k, v in A.most_common(12):
    if k == "fig8":
        continue
    q = sum(abs(a + b * tauA) ** 2 for a, b in k) / tauA.imag
    q0 = q if q0 is None else q0
    pa, pb = v / tA, B[k] / tB
    se = math.sqrt(pa * (1 - pa) / tA + pb * (1 - pb) / tB)
    c = math.log(top[1] / v) / (q - q0) if q > q0 + 1e-9 else float("nan")
    print(f"{pa:.5f} {pb:.5f}  diff/se {(pa - pb) / se if se else 0:+.2f}  Q {q:7.3f}  c {c:.3f}  {k}")
