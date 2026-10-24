from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def closure(n, covers):
    lt = [[False] * n for _ in range(n)]
    for a, b in covers:
        lt[a][b] = True
    for k in range(n):
        for i in range(n):
            if lt[i][k]:
                for j in range(n):
                    if lt[k][j]:
                        lt[i][j] = True
    return lt


def incomparable(lt, a, b):
    return a != b and not lt[a][b] and not lt[b][a]


def width(n, lt):
    best = 1 if n else 0
    for r in range(2, n + 1):
        for S in combinations(range(n), r):
            if all(incomparable(lt, a, b) for a, b in combinations(S, 2)):
                best = r
    return best


def extensions(n, lt):
    pred = [sum((1 << i) for i in range(n) if lt[i][v]) for v in range(n)]

    @lru_cache(None)
    def rec(mask):
        if mask == (1 << n) - 1:
            return ((),)
        out = []
        for v in range(n):
            bit = 1 << v
            if mask & bit:
                continue
            if pred[v] & ~mask:
                continue
            for tail in rec(mask | bit):
                out.append((v,) + tail)
        return tuple(out)

    return rec(0)


def swap_is_extension(ext, x, y, lt):
    e = list(ext)
    ix, iy = e.index(x), e.index(y)
    e[ix], e[iy] = e[iy], e[ix]
    pos = {v: i for i, v in enumerate(e)}
    n = len(e)
    return all(not lt[a][b] or pos[a] < pos[b] for a in range(n) for b in range(n))


def canonical_positive_blockers(n, lt, x, y):
    pred = [z for z in range(n) if lt[z][y] and incomparable(lt, z, x)]
    succ = [z for z in range(n) if lt[x][z] and incomparable(lt, z, y)]
    max_pred = [z for z in pred if not any(lt[z][w] for w in pred)]
    min_succ = [z for z in succ if not any(lt[w][z] for w in succ)]
    return max_pred, min_succ


def check_pair(n, lt, exts, x, y):
    assert incomparable(lt, x, y)
    A, B, Abad, Bbad = [], [], [], []
    max_pred, min_succ = canonical_positive_blockers(n, lt, x, y)
    for e in exts:
        pos = {v: i for i, v in enumerate(e)}
        if pos[x] < pos[y]:
            A.append(e)
            if not swap_is_extension(e, x, y, lt):
                Abad.append(e)
            blockers = any(pos[x] < pos[z] < pos[y] for z in max_pred + min_succ)
            assert blockers == (not swap_is_extension(e, x, y, lt))
        else:
            B.append(e)
            if not swap_is_extension(e, x, y, lt):
                Bbad.append(e)
    assert len(A) - len(B) == len(Abad) - len(Bbad)
    if width(n, lt) <= 3:
        assert len(max_pred) <= 2 and len(min_succ) <= 2
    return {
        "E": len(exts),
        "A": len(A),
        "B": len(B),
        "Abad": len(Abad),
        "Bbad": len(Bbad),
        "max_pred_blockers": max_pred,
        "min_succ_blockers": min_succ,
        "p_xy": Fraction(len(A), len(exts)),
    }


def main():
    # Bare N-poset: m<y, x<s, with x||y, x||m, s||y.
    n = 4
    lt = closure(n, [(1, 3), (0, 2)])
    exts = extensions(n, lt)
    n_case = check_pair(n, lt, exts, 0, 3)
    assert n_case["p_xy"] == Fraction(4, 5)

    # Six-element exact adversary to a stronger local shortcut.
    n6 = 6
    covers6 = [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (1, 5), (3, 4), (5, 2)]
    lt6 = closure(n6, covers6)
    assert width(n6, lt6) == 3
    e6 = extensions(n6, lt6)
    assert len(e6) == 22
    six = check_pair(n6, lt6, e6, 0, 3)
    assert six["p_xy"] == Fraction(15, 22)
    pos01 = sum(e.index(0) < e.index(1) for e in e6)
    pos23 = sum(e.index(2) < e.index(3) for e in e6)
    assert Fraction(pos01, len(e6)) == Fraction(3, 11)
    assert Fraction(pos23, len(e6)) == Fraction(3, 22)
    assert any(
        incomparable(lt6, x, y)
        and Fraction(sum(e.index(x) < e.index(y) for e in e6), len(e6)) == Fraction(1, 2)
        for x, y in combinations(range(n6), 2)
    )

    # Inherited account03/B19 exact certificate: 420 linear extensions, width three.
    n9 = 9
    covers9 = [(0, 2), (0, 3), (0, 4), (1, 4), (2, 5), (3, 6), (4, 7), (4, 8), (5, 8), (6, 8)]
    lt9 = closure(n9, covers9)
    assert width(n9, lt9) == 3
    e9 = extensions(n9, lt9)
    assert len(e9) == 420
    for x, y in combinations(range(n9), 2):
        if incomparable(lt9, x, y):
            check_pair(n9, lt9, e9, x, y)

    print("POS3_SWAP_DEFECT_CHECK_PASS")
    print("N_CASE", n_case)
    print("SIX_POINT_ADVERSARY", six)
    print("NINE_POINT_EXTENSIONS", len(e9))


if __name__ == "__main__":
    main()
