"""Control: on grid N=6 compare envelope.py's fusion rows with a direct all-orientation Fraction calculation."""
import os, itertools
os.environ["T067_N"] = os.environ.get("CTRL_N", "6")
from fractions import Fraction
import envelope as E
assert E.N == int(os.environ.get("CTRL_N", "6"))
def direct(K, H):
    k = E.ORB[K]; out = {}
    hs = E.PERMS[H]
    for h in hs:
        tot = sum(a*b for a, b in zip(k, h))
        if tot == 0: continue
        mass = Fraction(3*tot, len(hs)*E.N**2)
        q = [Fraction(E.N*a*b, tot) for a, b in zip(k, h)]
        f = [x.numerator // x.denominator for x in q]; r = [x - fi for x, fi in zip(q, f)]
        s = sum(r)
        if s == 0: verts = [(f, Fraction(1))]
        elif s == 1: verts = [([fi + (j == i) for i, fi in enumerate(f)], r[j]) for j in range(3) if r[j]]
        else: verts = [([fi + (i != j) for i, fi in enumerate(f)], 1 - r[j]) for j in range(3) if r[j] != 1]
        # barycentre check
        assert [sum(w*v[i] for v, w in verts) for i in range(3)] == q
        for v, w in verts:
            d = E.canon(v); out[d] = out.get(d, 0) + mass*w
    return out
key, h, num = E.fusion_tensor()
tab = {}
for kk, hh, nn in zip(key, h, num):
    K, d = divmod(int(kk), E.NO); tab.setdefault((K, int(hh)), {})[d] = Fraction(int(nn), E.D)
bad = 0
for K in range(E.NO):
    for H in range(E.NO):
        a = direct(K, H); b = tab.get((K, H), {})
        if a != b: bad += 1
        bs = direct(H, K)
        if sum(a.values()) != 1: bad += 1
        if a != bs: bad += 1   # symmetry of orbit-pair fusion
print("N=%d orbits" % E.N, E.NO, "pairs", E.NO**2, "mismatches", bad)
