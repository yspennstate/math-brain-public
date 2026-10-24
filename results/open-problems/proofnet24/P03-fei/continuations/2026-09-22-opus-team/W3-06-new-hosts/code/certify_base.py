"""Exact check (independent audit checker, arb balls) of the decomposition  g = B + nine free coins:
B = 'PM(K33) or cross' on 9 variables (crosses TRUE, crosses minus the centre edge FALSE) is balanced with
I(B) = I(g) = 261/128, and every coin site of g is a boundary edge of B with s(a) + s(b) = m + 1 = 10.
Also the 4-variable tie-coin function T (H = 3, I = 3/2, ratio 6)."""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'audit'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'F2-new-gates', 'code'))
import fei_audit
import flint
from fractions import Fraction


def has_pm(x):
    return any(all((x >> (3 * r + s[r])) & 1 for r in range(3)) for s in itertools.permutations(range(3)))


def cross(p):
    r, c = divmod(p, 3)
    return sum(1 << (3 * r + j) for j in range(3)) | sum(1 << (3 * i + c) for i in range(3))


def build_B(cross_true=True):
    t = np.ones(512, dtype=np.int64)
    for x in range(512):
        if has_pm(x):
            t[x] = -1
    for p in range(9):
        X = cross(p)
        if cross_true:
            t[X] = -1; t[X ^ (1 << p)] = 1
        else:
            t[X] = 1; t[X ^ (1 << p)] = -1
    return t


def sens(t, x, m=9):
    return sum(1 for i in range(m) if t[x ^ (1 << i)] != t[x])


if __name__ == '__main__':
    for ct in (True, False):
        B = build_B(ct)
        p, I, H = fei_audit.table_quantities(B)
        R = H / (flint.arb(I.numerator) / I.denominator - 1)
        ss = [(sens(B, cross(q)), sens(B, cross(q) ^ (1 << q))) for q in range(9)]
        print(f"B (crosses {'TRUE' if ct else 'FALSE'}): Pr[true]={p} I={I} H={H.str(25, radius=True)} "
              f"H/(I-1)={R.str(22, radius=True)} site sensitivities={ss}")
    g = np.load(os.path.join(HERE, '..', '..', 'inputs', 'numaro18_pm1_table.npy')).astype(np.int64)
    pg, Ig, Hg = fei_audit.table_quantities(g)
    B = build_B(True)
    pB, IB, HB = fei_audit.table_quantities(B)
    print(f"g: I={Ig} H={Hg.str(25, radius=True)};  I(g) - I(B) = {Ig - IB};  H(g) - H(B) = {(Hg - HB).str(22, radius=True)}")
    # tie-coin function on 4 variables: x1=x2=1 -> TRUE, x1=x2=0 -> FALSE, (1,0) -> y1, (0,1) -> y2
    T = np.empty(16, dtype=np.int64)
    for idx in range(16):
        x1, x2, y1, y2 = [(idx >> i) & 1 for i in range(4)]
        if x1 and x2: v = 1
        elif not x1 and not x2: v = 0
        elif x1: v = y1
        else: v = y2
        T[idx] = -1 if v else 1
    pT, IT, HT = fei_audit.table_quantities(T)
    print(f"tie-coin T (n=4): Pr={pT} I={IT} H={HT.str(20, radius=True)} H/(I-1)={(HT / (flint.arb(IT.numerator)/IT.denominator - 1)).str(20, radius=True)}")
