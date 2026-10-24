# Evidence only (float64): min_i B_i/I_i and H/I on the composed family
#   f = -1  iff  AND_a(x_1..x_a)  and  Tribes_{c,d}(y)   (Tribes_{c,1} = OR_c; c = 0 means AND_a alone)
# plus the exact linear form of the certified n = 5 value (AND_3 and OR_2).
import sys, os, json, itertools
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from certlog import add_mlogm, enclose_form, sign_form
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'out')

def wht(f):
    W = f.astype(np.float64).copy(); h = 1; N = len(W)
    while h < N:
        W = W.reshape(-1, 2, h); W = np.stack([W[:, 0] + W[:, 1], W[:, 0] - W[:, 1]], 1).reshape(N); h *= 2
    return W

def stats(f, n):
    N = 1 << n; W = wht(f); q = W * W / (N * N)
    def xl(v): return np.where(v > 0, -v * np.log2(np.where(v > 0, v, 1)), 0.0)
    H = xl(q).sum(); pc = np.array([bin(s).count('1') for s in range(N)]); I = (q * pc).sum()
    R = np.inf; per = []
    for i in range(n):
        Q = q.reshape(-1, 2, 1 << i); a = Q[:, 0]; b = Q[:, 1]
        Ii = b.sum(); Bi = (xl(a) + xl(b) - xl(a + b)).sum()
        if Ii > 1e-15:
            per.append(Bi / Ii); R = min(R, Bi / Ii)
    return R, H / I, per

def table(a, c, d):
    n = a + c * d; N = 1 << n; x = np.arange(N)
    andp = np.ones(N, bool)
    for j in range(a): andp &= (x >> j) & 1 == 1
    if c == 0:
        trib = np.ones(N, bool)
    else:
        trib = np.zeros(N, bool)
        for t in range(c):
            blk = np.ones(N, bool)
            for j in range(d): blk &= (x >> (a + t * d + j)) & 1 == 1
            trib |= blk
    return np.where(andp & trib, -1, 1), n

rows = []
for a in range(1, 8):
    for c in range(0, 7):
        for d in (1, 2, 3):
            if c == 0 and d > 1: continue
            f, n = table(a, c, d)
            if n > 16 or n < 1: continue
            R, HI, per = stats(f, n)
            rows.append({'a': a, 'c': c, 'd': d, 'n': n, 'min_B_ratio': round(float(R), 6), 'H_over_I': round(float(HI), 6)})
rows.sort(key=lambda r: -r['min_B_ratio'])
# exact form of the certified n=5 value: f = -1 on {5,12,13}
n = 5; N = 32; f = np.ones(N, int); f[[5, 12, 13]] = -1
W = [sum(int(f[x]) * (-1) ** bin(x & S).count('1') for x in range(N)) for S in range(N)]
q = [w * w for w in W]; forms = {}
for i in (1, 0):
    bit = 1 << i; form = {}; D = 0
    for T in range(N):
        if T & bit: continue
        A, B = q[T], q[T | bit]; D += B
        add_mlogm(form, A + B, 1); add_mlogm(form, A, -1); add_mlogm(form, B, -1)
    lo, hi = enclose_form(form)
    forms['coord%d' % i] = {'N2_I_i': D, 'ratio_as_coeff_times_log2_p': {str(p): str(Fr(v, D)) for p, v in sorted(form.items()) if v},
                            'ratio_lo': str(float(lo / D)), 'ratio_hi': str(float(hi / D))}
res = {'family_top15': rows[:15], 'family_count': len(rows), 'n5_exact_forms': forms}
with open(os.path.join(OUT, 'family_scan.json'), 'w', encoding='utf-8') as fh: json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
