from fractions import Fraction
from functools import lru_cache


def rect_cells(h, w):
    return {(i, j) for i in range(h) for j in range(w)}


def poison(cells):
    cells = sorted(cells)
    n = len(cells)
    idx = {v: i for i, v in enumerate(cells)}
    edges = []
    for (x, y), i in idx.items():
        for dx, dy in ((1, 0), (0, 1)):
            z = (x + dx, y + dy)
            if z in idx:
                edges.append((i, idx[z]))

    @lru_cache(None)
    def ecount(mask):
        return sum(1 for a, b in edges if ((mask >> a) & 1) and ((mask >> b) & 1))

    @lru_cache(None)
    def qco(mask):
        if mask == 0:
            return Fraction(1, 1)
        k = mask.bit_count()
        den = 2 * k + ecount(mask)
        s = Fraction(0, 1)
        m = mask
        while m:
            bit = m & -m
            s += qco(mask ^ bit)
            m ^= bit
        return Fraction(2, den) * s

    @lru_cache(None)
    def qo(mask):
        if mask == 0:
            return Fraction(1, 1)
        if mask.bit_count() & 1:
            return Fraction(0, 1)
        k = mask.bit_count()
        den = 2 * k + ecount(mask)
        s = Fraction(0, 1)
        for a, b in edges:
            bits = (1 << a) | (1 << b)
            if (mask & bits) == bits:
                s += qo(mask ^ bits)
        return s / Fraction(den, 1)

    full = (1 << n) - 1
    return qco(full), qo(full), len(edges)


budget = Fraction(1, 64)
rows = []
for area in range(1, 17):
    for h in range(1, area + 1):
        if area % h:
            continue
        w = area // h
        if h > w:
            continue
        qco, qo, e = poison(rect_cells(h, w))
        rows.append((area, h, w, e, qco, qo, qco + qo))

print("DIRECT_MONOCHROMATIC_POISON_RECTANGLES")
for area, h, w, e, qco, qo, total in rows:
    if (h, w) in {(2, 7), (3, 4), (3, 5), (2, 8), (4, 4)}:
        print(f"{h}x{w} area={area} edges={e}")
        print(" qCO =", qco)
        print(" qO  =", qo)
        print(" sum =", total)
        print(" sum<1/64 =", total < budget)

best_by_area = {}
for r in rows:
    area = r[0]
    if area not in best_by_area or r[-1] < best_by_area[area][-1]:
        best_by_area[area] = r

assert all(best_by_area[a][-1] >= budget for a in range(1, 15))
assert best_by_area[15][1:3] == (3, 5)
assert best_by_area[15][-1] < budget
assert best_by_area[16][1:3] == (4, 4)
assert best_by_area[16][-1] < budget

q35 = next(r[-1] for r in rows if r[1:3] == (3, 5))
q28 = next(r[-1] for r in rows if r[1:3] == (2, 8))
q44 = next(r[-1] for r in rows if r[1:3] == (4, 4))
assert q28 < q35
assert q44 < q28

qco_c, qo_c, e_c = poison(rect_cells(4, 4) - {(0, 0)})
assert qo_c == 0
assert q35 < qco_c

print("FIRST_RECTANGLE_AREA_WITH_SUM_BELOW_1_OVER_64 = 15")
print("BEST_AREA15 = 3x5")
print("3x5_sum =", q35)
print("3x5_margin_to_1/64 =", budget - q35)
print("2x8_sum =", q28)
print("4x4_sum =", q44)
print("4x4_minus_corner_qCO =", qco_c)
print("3x5_beats_4x4_minus_corner =", q35 < qco_c)
print("PASS")
