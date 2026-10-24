#!/usr/bin/env python3
"""Exact verifier for B17 block-OR softmax counterexample and D-dichotomy calibration."""
from fractions import Fraction
from collections import Counter, defaultdict
import hashlib, json, struct

POS = {2, 8, 10, 11, 14}
BLOCKS = 4
K = 4
N = 1 << (BLOCKS * K)
D = N * N
M = 24

def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def gate(x):
    return 1 if x in POS else -1

def F(x):
    for b in range(BLOCKS):
        if gate((x >> (K*b)) & 15) == 1:
            return 1
    return -1

def floor_log2_frac(x):
    n, d = x.numerator, x.denominator
    k = n.bit_length() - d.bit_length()
    def ge_pow2(j):
        return n >= d*(1 << j) if j >= 0 else n*(1 << (-j)) >= d
    while not ge_pow2(k):
        k -= 1
    while ge_pow2(k+1):
        k += 1
    return k

def ln_y_bounds(y, terms=M):
    assert Fraction(1) <= y < Fraction(2)
    z = (y - 1) / (y + 1)
    z2 = z*z
    s = Fraction(0)
    zp = z
    for j in range(terms):
        s += zp / (2*j + 1)
        zp *= z2
    lo = 2*s
    hi = lo if z == 0 else lo + 2*zp / ((2*terms + 1)*(1-z2))
    return lo, hi

def ln2_bounds(terms=M):
    z = Fraction(1,3)
    z2 = z*z
    s = Fraction(0)
    zp = z
    for j in range(terms):
        s += zp / (2*j + 1)
        zp *= z2
    lo = 2*s
    hi = lo + 2*zp / ((2*terms + 1)*(1-z2))
    return lo, hi

def log2_bounds(x, terms=M):
    assert x >= 1
    k = floor_log2_frac(x)
    y = x / (1 << k) if k >= 0 else x * (1 << (-k))
    lylo, lyhi = ln_y_bounds(y, terms)
    l2lo, l2hi = ln2_bounds(terms)
    return Fraction(k) + lylo/l2hi, Fraction(k) + lyhi/l2lo

truth = [F(x) for x in range(N)]
H = fwht(truth)
assert sum(h*h for h in H) == D

inner = [gate(x) for x in range(16)]
Hinner = fwht(inner)
EXPECTED_INNER = [-6, 6, -6, -2, 6, 2, -2, 2, -6, -2, 2, -2, -2, 2, -2, -6]
assert Hinner == EXPECTED_INNER

truth_hash = hashlib.sha256(bytes(1 if v > 0 else 0 for v in truth)).hexdigest()
walsh_hash = hashlib.sha256(b"".join(struct.pack("<q", h) for h in H)).hexdigest()

def pair_counter(i):
    c = Counter()
    for t in range(N):
        if (t >> i) & 1:
            continue
        a2 = H[t]*H[t]
        b2 = H[t | (1 << i)]*H[t | (1 << i)]
        c[(min(a2,b2), max(a2,b2))] += 1
    return c

pc0 = pair_counter(0)
assert all(pair_counter(i) == pc0 for i in range(16))

inf_nums = []
for i in range(16):
    inf_nums.append(sum(H[s]*H[s] for s in range(N) if (s >> i) & 1))
q = [min(Fraction(x,D), 1-Fraction(x,D)) for x in inf_nums]
assert all(x == Fraction(3993,32768) for x in q)
J = sum(q, Fraction(0))
assert J == Fraction(3993,2048)

ratio_weight = defaultdict(int)
for (lo, hi), count in pc0.items():
    assert lo > 0
    ratio_weight[Fraction(lo+hi, 2*lo)] += count*lo

EXPECTED_WEIGHTS = {
    Fraction(1,1): 65421312,
    Fraction(5,1): 87228416,
    Fraction(65,9): 132487740,
    Fraction(172266089,15944049): 63776196,
}
assert dict(ratio_weight) == EXPECTED_WEIGHTS

assert 5**25 > 2**58
assert 65**20 > (2**57) * (9**20)
assert 172266089**100 > (2**343) * (15944049**100)
short_lb = (
    Fraction(87228416, 2*D) * Fraction(58,25)
    + Fraction(132487740, 2*D) * Fraction(57,20)
    + Fraction(63776196, 2*D) * Fraction(343,100)
)
target = Fraction(3,4) * q[0]
assert short_lb - target == Fraction(34141481,21474836480)
assert short_lb > target

Wlo = Fraction(0)
Whi = Fraction(0)
for ratio, weight in ratio_weight.items():
    if ratio == 1:
        continue
    lo, hi = log2_bounds(ratio)
    coeff = Fraction(weight, 2*D)
    Wlo += coeff*lo
    Whi += coeff*hi
assert Wlo > target

Tcoeff = defaultdict(Fraction)
Hcoeff = defaultdict(Fraction)
for s, hsigned in enumerate(H):
    h = abs(hsigned)
    if h == 0:
        continue
    h2 = h*h
    neigh = sum(H[s ^ (1 << i)]**2 for i in range(16))
    Hcoeff[h] += Fraction(h2, D)
    Tcoeff[h] += Fraction(h2 * (D - h2 - neigh), D*D)

Tlo = Thi = Fraction(0)
Hlo = Hhi = Fraction(0)
for h, coeff in Hcoeff.items():
    llo, lhi = log2_bounds(Fraction(D, h*h))
    Hlo += coeff*llo
    Hhi += coeff*lhi
    Tlo += Tcoeff[h]*llo
    Thi += Tcoeff[h]*lhi

assert Thi < 4*J

def dec(x, digits=18):
    return f"{float(x):.{digits}f}"

out = {
    "status": "PASS",
    "construction": {
        "inner_positive_indices_little_endian": sorted(POS),
        "blocks": BLOCKS,
        "variables": 16,
        "truth_sha256": truth_hash,
        "integer_walsh_sha256": walsh_hash,
        "inner_integer_walsh": Hinner,
    },
    "folded_influence": {
        "q_i": str(q[0]),
        "J": str(J),
        "all_16_coordinates_equal": True,
    },
    "softmax_counterexample": {
        "pair_ratio_weight_exact": {str(k): v for k,v in sorted(ratio_weight.items(), key=lambda z: float(z[0]))},
        "short_exact_lower_bound_W_i": str(short_lb),
        "three_quarters_q_i": str(target),
        "exact_positive_margin_lower_bound": str(short_lb-target),
        "W_i_interval": [dec(Wlo), dec(Whi)],
        "W_over_J_interval": [dec(Wlo/q[0]), dec(Whi/q[0])],
        "refutes_W_le_3J_over_4": True,
    },
    "replacement_calibration": {
        "T2_over_J_interval": [dec(Tlo/J), dec(Thi/J)],
        "T2_lt_4J_certified": True,
        "H_over_J_interval": [dec(Hlo/J), dec(Hhi/J)],
    },
    "log_certificate": {
        "method": "exact rational atanh-series bounds after power-of-two normalization",
        "terms": M,
    },
}
print(json.dumps(out, indent=2, sort_keys=True))
