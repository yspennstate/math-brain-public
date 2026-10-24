from fractions import Fraction
import itertools

N = 32

def monotone_masks(n):
    fs = [0, 1]
    width = 1
    for _ in range(n):
        out = []
        full = (1 << width) - 1
        for a in fs:
            for b in fs:
                if a & (~b & full) == 0:
                    out.append(a | (b << width))
        fs = out
        width *= 2
    return fs

def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a

def essential(mask, i):
    for x in range(N):
        if ((x >> i) & 1) == 0 and (((mask >> x) & 1) != ((mask >> (x | (1 << i))) & 1)):
            return True
    return False

def ln_bounds_rational(x, terms=48):
    y = (x - 1) / (x + 1)
    s = Fraction(0)
    yp = y
    for k in range(terms):
        s += yp / Fraction(2 * k + 1)
        yp *= y * y
    lo = 2 * s
    rem = 2 * yp / Fraction(2 * terms + 1) / (1 - y * y)
    return lo, lo + rem

LN2_LO, LN2_HI = ln_bounds_rational(Fraction(2))

def log2_bounds_int(m):
    if m & (m - 1) == 0:
        q = Fraction(m.bit_length() - 1)
        return q, q
    k = m.bit_length() - 1
    r = Fraction(m, 1 << k)
    lo, hi = ln_bounds_rational(r)
    return Fraction(k) + lo / LN2_HI, Fraction(k) + hi / LN2_LO

L3_LO, L3_HI = log2_bounds_int(3)
RSTAR_LO = Fraction(44, 5) - Fraction(9, 5) * L3_HI
RSTAR_HI = Fraction(44, 5) - Fraction(9, 5) * L3_LO

fs = monotone_masks(5)
assert len(fs) == 7581
balanced = 0
essential_balanced = 0
equality = []
strict_min = None
strict_mask = None
ref_hist = {16: 12, 64: 4, 144: 4}
for mask in fs:
    if mask.bit_count() != 16:
        continue
    balanced += 1
    if not all(essential(mask, i) for i in range(5)):
        continue
    essential_balanced += 1
    A = fwht([1 if (mask >> x) & 1 else -1 for x in range(N)])
    hist = {}
    H_UP = Fraction(0)
    I = Fraction(0)
    for s, z in enumerate(A):
        if not z:
            continue
        m = z * z
        hist[m] = hist.get(m, 0) + 1
        q = Fraction(m, 1024)
        loglo, _ = log2_bounds_int(m)
        H_UP += q * (10 - loglo)
        I += q * s.bit_count()
    if I == Fraction(13, 8) and hist == ref_hist:
        equality.append(mask)
        continue
    slack = RSTAR_LO * (I - 1) - H_UP
    assert slack > 0, (hex(mask), float(slack), I, float(H_UP))
    if strict_min is None or slack < strict_min:
        strict_min = slack
        strict_mask = mask

rep = 0xEEE0EAC0
orbit = set()
for p in itertools.permutations(range(5)):
    m = 0
    for x in range(N):
        if (rep >> x) & 1:
            y = 0
            for i in range(5):
                if (x >> i) & 1:
                    y |= 1 << p[i]
            m |= 1 << y
    orbit.add(m)
assert set(equality) == orbit
assert len(equality) == 30

print("PASS")
print("monotone_total", len(fs))
print("balanced_monotone", balanced)
print("essential_balanced_monotone", essential_balanced)
print("maximizer_count", len(equality))
print("maximizer_permutation_orbit_size", len(orbit))
print("representative_mask", hex(rep))
print("Rstar_interval", float(RSTAR_LO), float(RSTAR_HI))
print("Rstar_exact", "44/5 - (9/5) log2(3)")
print("Hstar_exact", "11/2 - (9/8) log2(3)")
print("Istar_exact", "13/8")
print("strict_nonmax_gap_lower", float(strict_min), "mask", hex(strict_mask))
print("consequence", "every essential balanced unate 5-input gate has H/(I-1) <= Rstar < 6")
