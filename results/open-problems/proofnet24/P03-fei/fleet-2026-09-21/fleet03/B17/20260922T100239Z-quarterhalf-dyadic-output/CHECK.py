from decimal import Decimal, getcontext
from itertools import combinations, permutations
from math import comb

getcontext().prec = 80
D = Decimal
C0 = D("6.4548")
LN2 = D(2).ln()
DEN = 4096


def log2d(x):
    return D(x).ln() / LN2


def phi_num(n):
    if n == 0:
        return D(0)
    p = D(n) / D(DEN)
    return p * log2d(D(DEN) / D(n))


PHI = {n: phi_num(n) for n in range(0, DEN + 1)}
W = [[1 if ((T & x).bit_count() & 1) == 0 else -1 for x in range(16)] for T in range(16)]
WT = [T.bit_count() for T in range(16)]


def walsh(mask):
    f = [1 if (mask >> x) & 1 else -1 for x in range(16)]
    return tuple(sum(W[T][x] * f[x] for x in range(16)) for T in range(16))


AUTOS = []
for perm in permutations(range(4)):
    for flip in range(16):
        mp = []
        for x in range(16):
            y = 0
            for i in range(4):
                bit = ((x >> i) & 1) ^ ((flip >> i) & 1)
                if bit:
                    y |= 1 << perm[i]
            mp.append(y)
        AUTOS.append(tuple(mp))
assert len(AUTOS) == 384


def transform(mask, mp):
    z = 0
    for x, y in enumerate(mp):
        if (mask >> x) & 1:
            z |= 1 << y
    return z


def canon(mask):
    return min(transform(mask, mp) for mp in AUTOS)


def masks_weight(k):
    out = []
    for cs in combinations(range(16), k):
        m = 0
        for i in cs:
            m |= 1 << i
        out.append(m)
    return out


MASKS = {k: masks_weight(k) for k in range(17)}
ORBITS = {}
for k in range(6):
    ORBITS[k] = sorted({canon(m) for m in MASKS[k]})

WCACHE = {}
for k in range(17):
    for m in MASKS[k]:
        WCACHE[m] = walsh(m)


def and_gamma(m):
    p = D(1) / (D(2) ** m)
    const = (D(1) - D(2) * p) ** 2
    w = D(4) * p * p
    H = D(0)
    if const:
        H -= const * log2d(const)
    if w:
        H -= D((1 << m) - 1) * w * log2d(w)
    I = D(m) * (D(2) ** (m - 1)) * w
    return C0 * I - H


G4 = and_gamma(2)
HQ = -(D(3) / D(4)) * log2d(D(3) / D(4)) - (D(1) / D(4)) * log2d(D(1) / D(4))


def feasible(num):
    return [(k0, num - 3 * k0) for k0 in range(17) if 0 <= num - 3 * k0 <= 16]


def is_subcube(m0, m1):
    pts = []
    for y, m in ((0, m0), (1, m1)):
        for x in range(16):
            if (m >> x) & 1:
                pts.append((y,) + tuple((x >> j) & 1 for j in range(4)))
    if not pts:
        return False
    free = 0
    for j in range(5):
        vals = {p[j] for p in pts}
        if len(vals) == 2:
            free += 1
        elif len(vals) != 1:
            return False
    return len(pts) == (1 << free)


def evaluate(m0, m1, pout, gout):
    a = WCACHE[m0]
    b = WCACHE[m1]
    n0 = [(3 * a[t] + b[t]) ** 2 for t in range(16)]
    n1 = [3 * (b[t] - a[t]) ** 2 for t in range(16)]
    H = sum((PHI[n] for n in n0), D(0)) + sum((PHI[n] for n in n1), D(0))
    ity_num = sum(n1)
    b_num = sum(WT[t] * (n0[t] + n1[t]) for t in range(16))
    Ity = D(ity_num) / D(DEN)
    A = D(4) * Ity / D(3)
    B = D(b_num) / D(DEN)
    I = Ity + B
    defect = B * C0 + A * (G4 + HQ) - (gout + H)
    currency = I / D(4) - pout * (D(1) - pout)
    c = None if abs(currency) < D("1e-70") else -defect / currency
    return defect, currency, c


summary = []
total_raw = 0
total_orbit = 0
for num in (1, 2, 4, 8, 16):
    pout = D(num) / D(64)
    m = {1: 6, 2: 5, 4: 4, 8: 3, 16: 2}[num]
    gout = and_gamma(m)
    raw = sum(comb(16, k0) * comb(16, k1) for k0, k1 in feasible(num))
    orbit = sum(len(ORBITS[k0]) * comb(16, k1) for k0, k1 in feasible(num))
    total_raw += raw
    total_orbit += orbit
    min_positive = None
    max_c = None
    max_c_arg = None
    zero_count = 0
    zero_all_subcube = True
    positive_currency_count = 0
    for k0, k1 in feasible(num):
        for m0 in ORBITS[k0]:
            for m1 in MASKS[k1]:
                defect, currency, c = evaluate(m0, m1, pout, gout)
                if currency <= D("1e-60"):
                    continue
                positive_currency_count += 1
                if abs(defect) <= D("1e-55"):
                    zero_count += 1
                    zero_all_subcube = zero_all_subcube and is_subcube(m0, m1)
                else:
                    assert defect > D("1e-40"), (num, k0, k1, m0, m1, defect)
                    if min_positive is None or defect < min_positive[0]:
                        min_positive = (defect, (k0, k1, m0, m1, c))
                if c is not None and (max_c is None or c > max_c):
                    max_c = c
                    max_c_arg = (k0, k1, m0, m1)
    summary.append({
        "num": num,
        "pout": str(pout),
        "raw": raw,
        "orbit": orbit,
        "positive_currency": positive_currency_count,
        "zero_count": zero_count,
        "zero_all_subcube": zero_all_subcube,
        "min_positive_defect": None if min_positive is None else str(min_positive[0]),
        "max_c": None if max_c is None else str(max_c),
        "max_c_arg": max_c_arg,
        "max_nonsubcube_c": None if min_positive is None else str(min_positive[1][4]),
        "max_nonsubcube_arg": None if min_positive is None else min_positive[1][:4],
    })

print("PASS")
print("C0", C0)
print("GAMMA quarter", G4)
print("raw_total", total_raw)
print("orbit_total", total_orbit)
for row in summary:
    print(row)
