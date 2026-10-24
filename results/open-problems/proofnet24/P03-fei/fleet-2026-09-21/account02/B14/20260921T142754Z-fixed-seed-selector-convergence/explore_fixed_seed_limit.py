"""Exploratory high-precision continuation of account02/B14 Numaro selector recursion.

Not a directed-rounding certificate.  The analytic convergence theorem is in REPORT.md;
this script only reproduces the displayed exploratory depth-6+ values and two-class DP.
"""
from collections import Counter
import hashlib
import numpy as np
import mpmath as mp

mp.mp.dps = 80
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def fwht(a):
    out = np.array(a, dtype=np.int64, copy=True)
    h = 1
    while h < len(out):
        v = out.reshape(-1, 2*h)
        L, R = v[:, :h].copy(), v[:, h:].copy()
        v[:, :h], v[:, h:] = L+R, L-R
        h *= 2
    return out

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    hosts = [[x for x in range(512) if (mask >> x) & 1] for mask in masks]
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    table = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert table.sum() == 0
    return table

def phi(x):
    return mp.mpf('0') if x == 0 else -x*mp.log(x, 2)

def h2(x):
    return mp.mpf('0') if x == 0 or x == 1 else -x*mp.log(x,2)-(1-x)*mp.log(1-x,2)

def entropy_walsh(W, N):
    c = Counter(int(z)*int(z) for z in W if z)
    den = mp.mpf(N)**2
    return sum(mult*phi(mp.mpf(sq)/den) for sq, mult in c.items())

def child(values, n, i, bit):
    idx = np.arange(1 << n)
    return values[((idx >> i) & 1) == bit]

def pair_counter(W, i):
    bit = 1 << i
    c = Counter()
    for K in range(len(W)):
        if K & bit:
            continue
        c[(int(W[K]), int(W[K|bit]))] += 1
    return c

table = reconstruct()
N = len(table)
W = fwht(table)
H = entropy_walsh(W, N)
aC, aA = mp.mpf(57)/256, mp.mpf(1)/256
pc = {"C": pair_counter(W,0), "A": pair_counter(W,9)}
a = {"C": aC, "A": aA}
rep = {"C": 0, "A": 9}

def biased_H(label, q, sign):
    total = mp.mpf('0')
    for (Ai, Bi), mult in pc[label].items():
        A, B = mp.mpf(Ai)/N, mp.mpf(Bi)/N
        u = (A + sign*q*B)**2
        v = (1-q*q)*B*B
        total += mult*(phi(u)+phi(v))
    return total

def K(label, q):
    return H - (biased_H(label,q,1)+biased_H(label,q,-1))/2 + a[label]*h2(q*q)

def base_ratio(label):
    i = rep[label]
    H0 = entropy_walsh(fwht(child(table,18,i,0)), N//2)
    H1 = entropy_walsh(fwht(child(table,18,i,1)), N//2)
    return (H-(H0+H1)/2)/a[label]

base = {label: base_ratio(label) for label in ("C","A")}
print("truth_table_sha256", EXPECTED_SHA)
print("base_C", mp.nstr(base['C'], 45))
print("base_A", mp.nstr(base['A'], 45))

R, q = base['C'], aC
for r in range(2,9):
    R += K('C',q)/(aC*q)
    q *= aC
    if r >= 5:
        print(f"all_core_r{r}", mp.nstr(R,45))

dp = {(1,1):(base['C'],'C'), (1,0):(base['A'],'A')}
for r in range(1,16):
    candidates = [(value, c, word) for (rr,c),(value,word) in dp.items() if rr == r]
    value, c, word = min(candidates, key=lambda z: z[0])
    print(f"min_r{r}", mp.nstr(value,45), word)
    if r == 15:
        break
    for c0 in range(r+1):
        key=(r,c0)
        if key not in dp:
            continue
        value0, word0 = dp[key]
        q0 = aC**c0 * aA**(r-c0)
        for label in ('C','A'):
            c1 = c0 + (label == 'C')
            value1 = value0 + K(label,q0)/(a[label]*q0)
            key1=(r+1,c1)
            if key1 not in dp or value1 < dp[key1][0]:
                dp[key1] = (value1, label+word0)
