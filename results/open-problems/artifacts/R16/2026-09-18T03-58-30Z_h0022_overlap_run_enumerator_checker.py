from itertools import product
from math import comb


def predicted(L):
    out = {(0, 0, 0): 1, (L, 0, 1): 1}
    for j in range(1, L):
        for r in range(1, min(j, L - j) + 1):
            out[(j, r, 0)] = (L * comb(j - 1, r - 1) * comb(L - j - 1, r - 1)) // r
    return out


def exact(L):
    out = {}
    for bits in product((0, 1), repeat=L):
        j = sum(bits)
        z = int(j == L)
        if j in (0, L):
            r = 0
        else:
            r = sum(bits[i] == 1 and bits[(i - 1) % L] == 0 for i in range(L))
        key = (j, r, z)
        out[key] = out.get(key, 0) + 1
    return out


for L in range(3, 13):
    p = predicted(L)
    e = exact(L)
    assert p == e, (L, p, e)
    assert sum(p.values()) == 2**L
    print(f"L={L}: subsets={2**L} exact_run_enumerator=PASS")

print("ALL_EXACT_CHECKS_PASS")
