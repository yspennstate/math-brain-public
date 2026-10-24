from fractions import Fraction
from functools import lru_cache


def F(x):
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)
    r = x
    val = Fraction(0)
    wt = Fraction(1, 2)
    seen = {}
    while True:
        if r in seen:
            oval, owt = seen[r]
            q = wt / owt
            return oval + (val - oval) / (1 - q)
        seen[r] = (val, wt)
        y = 3 * r
        d = y.numerator // y.denominator
        r = y - d
        if d == 1:
            return val + wt
        if d == 2:
            val += wt
        if d not in (0, 1, 2):
            raise AssertionError
        if r == 0:
            return val
        wt /= 2


def mass(n, k):
    return F(Fraction(k + 1, 2**n)) - F(Fraction(k, 2**n))


def ceil_cantor(x):
    x = Fraction(x)
    if x <= 0:
        return Fraction(0)
    if x >= 1:
        return Fraction(1)
    r = x
    pref = Fraction(0)
    seen = set()
    j = 1
    while True:
        if r in seen:
            return x
        seen.add(r)
        y = 3 * r
        d = y.numerator // y.denominator
        r = y - d
        if d == 1:
            return pref + Fraction(2, 3**j)
        if d == 2:
            pref += Fraction(2, 3**j)
        if d not in (0, 1, 2):
            raise AssertionError
        if r == 0:
            return x
        j += 1


def intersects(n, k):
    return ceil_cantor(Fraction(k, 2**n)) <= Fraction(k + 1, 2**n)


@lru_cache(None)
def wired(n, k, radius):
    assert intersects(n, k)
    if radius == 0:
        return None
    ans = Fraction(0)
    for c in (2 * k, 2 * k + 1):
        if intersects(n + 1, c):
            C = wired(n + 1, c, radius - 1)
            ans += Fraction(1) if C is None else C / (1 + C)
    return ans


def prefix_energy(n0, k0, R):
    m0 = mass(n0, k0)
    cur = [k0]
    E = Fraction(0)
    for s in range(1, R + 1):
        n = n0 + s
        nxt = []
        level = Fraction(0)
        for p in cur:
            for c in (2 * p, 2 * p + 1):
                z = mass(n, c)
                if z:
                    nxt.append(c)
                    level += (z / m0) ** 2
        E += level
        cur = nxt
    return E


def in_cantor(x):
    x = Fraction(x)
    if x < 0 or x > 1:
        return False
    if x in (0, 1):
        return True
    r = x
    seen = set()
    while True:
        if r in seen:
            return True
        seen.add(r)
        y = 3 * r
        d = y.numerator // y.denominator
        r = y - d
        if d == 1:
            return r == 0
        if d not in (0, 2):
            return False
        if r == 0:
            return True


E8 = prefix_energy(8, 8, 8)
tail = Fraction(384) * Fraction(2, 3) ** 17
Etot = E8 + tail
GL = 1 / (1 + Etot)
CR = wired(8, 9, 6)
GR = CR / (1 + CR)
split = GL / (GL + GR)

assert mass(8, 8) == mass(8, 9) == Fraction(1, 64)
assert E8 == Fraction(955961, 524288)
assert tail == Fraction(16777216, 43046721)
assert Etot == Fraction(49947079476089, 22568879259648)
assert GL == Fraction(22568879259648, 72515958735737)
assert CR == Fraction(13703, 31620)
assert GR == Fraction(13703, 45323)
assert split == Fraction(1022889314685026304, 2016575497240830415)
assert split > Fraction(1, 2)

u0 = Fraction(52, 243)
r0 = Fraction(128, 243)
assert u0 / r0 == Fraction(13, 32)
assert (1 - u0 - r0) / r0 == Fraction(63, 128)
assert (Fraction(1, 2) - u0) / r0 == Fraction(139, 256)
assert Fraction(1, 3) < (Fraction(1, 2) - u0) / r0 < Fraction(2, 3)

checked = 0
for ell in range(1, 8):
    for j in range(1, 2**ell):
        y = (Fraction(j, 2**ell) - u0) / r0
        if 0 <= y <= 1:
            checked += 1
            assert not in_cantor(y)
assert checked == 133


def left(bits):
    return sum(Fraction(2 * b, 3 ** (i + 1)) for i, b in enumerate(bits))


suffix_cases = 0
for m in range(2, 13):
    words = [tuple((z >> (m - 1 - i)) & 1 for i in range(m)) for z in range(2**m)]
    xs = [left(w) for w in words]
    ell = Fraction(1, 3**m)
    for i, w in enumerate(words):
        if w[-2:] != (1, 1):
            continue
        suffix_cases += 1
        if i > 0:
            assert xs[i] - (xs[i - 1] + ell) == ell
        if i + 1 < len(words):
            rr = 0
            for b in reversed(w):
                if b:
                    rr += 1
                else:
                    break
            assert xs[i + 1] - (xs[i] + ell) == 3**rr * ell
            assert 3**rr * ell >= 9 * ell

print("R01_P0063_INDEPENDENT_EXACT_CHECK_PASS")
print("left_energy_prefix =", E8)
print("tail_upper =", tail)
print("left_branch_lower =", GL)
print("right_wired_descendant =", CR)
print("right_branch_upper =", GR)
print("split_lower =", split)
print("split_excess =", split - Fraction(1, 2))
print("no_tangency_boundaries =", checked)
print("suffix22_cases_checked_m2_to_m12 =", suffix_cases)
