from fractions import Fraction
from functools import lru_cache


def qco_rect(h, w):
    cells = [(i, j) for i in range(h) for j in range(w)]
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
    def q(mask):
        if mask == 0:
            return Fraction(1, 1)
        den = 2 * mask.bit_count() + ecount(mask)
        s = Fraction(0, 1)
        m = mask
        while m:
            bit = m & -m
            m ^= bit
            s += q(mask ^ bit)
        return Fraction(2, den) * s

    return q((1 << (h * w)) - 1), len(edges)


budget = Fraction(1, 64)
best = {}
for area in range(1, 17):
    for h in range(1, area + 1):
        if area % h:
            continue
        w = area // h
        if h > w:
            continue
        q, e = qco_rect(h, w)
        if area not in best or q < best[area][3]:
            best[area] = (h, w, e, q)

print("BEST_RECTANGULAR_ALL_CO_POISON_BY_AREA")
for area in range(1, 17):
    h, w, e, q = best[area]
    print(area, f"{h}x{w}", "edges", e, "qCO", q, "below_1_over_64", q < budget)

assert all(best[a][3] >= budget for a in range(1, 15))
assert best[15][0:2] == (3, 5)
assert best[15][3] < budget
assert best[16][0:2] == (4, 4)
assert best[16][3] < budget

print("FIRST_RECTANGULAR_AREA_BELOW_1_OVER_64 = 15")
print("FIRST_RECTANGULAR_SHAPE_BELOW_1_OVER_64 = 3x5")
print("PASS exact rectangular all-CO obstruction threshold")
