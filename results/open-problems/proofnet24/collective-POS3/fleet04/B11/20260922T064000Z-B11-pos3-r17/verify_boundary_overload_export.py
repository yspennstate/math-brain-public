from itertools import combinations
from collections import defaultdict


def closure_from_mask(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    succ = [0] * n
    for bit, (i, j) in enumerate(pairs):
        if (mask >> bit) & 1:
            succ[i] |= 1 << j
    changed = True
    while changed:
        changed = False
        for i in range(n - 1, -1, -1):
            old = succ[i]
            new = old
            x = old
            while x:
                b = x & -x
                j = b.bit_length() - 1
                new |= succ[j]
                x -= b
            if new != old:
                succ[i] = new
                changed = True
    return tuple(succ)


def pred_from_succ(succ, n):
    pred = [0] * n
    for i, s in enumerate(succ):
        x = s
        while x:
            b = x & -x
            j = b.bit_length() - 1
            pred[j] |= 1 << i
            x -= b
    return tuple(pred)


def incomparable(succ, a, b):
    return a != b and not ((succ[a] >> b) & 1) and not ((succ[b] >> a) & 1)


def width(succ, n):
    best = 0
    for mask in range(1 << n):
        vs = [i for i in range(n) if (mask >> i) & 1]
        if all(incomparable(succ, a, b) for a, b in combinations(vs, 2)):
            best = max(best, len(vs))
    return best


def covers(succ, a, b, n):
    if not ((succ[a] >> b) & 1):
        return False
    return not any(
        c not in (a, b)
        and ((succ[a] >> c) & 1)
        and ((succ[c] >> b) & 1)
        for c in range(n)
    )


def linear_extensions(succ, n):
    pred = pred_from_succ(succ, n)
    out = []

    def rec(order, used):
        if len(order) == n:
            out.append(tuple(order))
            return
        for v in range(n):
            if not ((used >> v) & 1) and (pred[v] & ~used) == 0:
                rec(order + [v], used | (1 << v))

    rec([], 0)
    return out


def main():
    stats = defaultdict(int)
    width3_posets = {}

    for n in range(3, 7):
        closures = {}
        for mask in range(1 << (n * (n - 1) // 2)):
            s = closure_from_mask(n, mask)
            closures[s] = None

        width3_posets[n] = sum(width(s, n) <= 3 for s in closures)

        for succ in closures:
            if width(succ, n) > 3:
                continue
            pred = pred_from_succ(succ, n)
            exts = None

            for x in range(n):
                for y in range(n):
                    if x == y or not incomparable(succ, x, y):
                        continue
                    px = {i for i in range(n) if (pred[x] >> i) & 1}
                    py = {i for i in range(n) if (pred[y] >> i) & 1}
                    sy = {i for i in range(n) if (succ[y] >> i) & 1}
                    sx = {i for i in range(n) if (succ[x] >> i) & 1}
                    if not px.issubset(py) or not sy.issubset(sx):
                        continue
                    D = py - px
                    U = sx - sy
                    if len(D) != 1 or len(U) != 1:
                        continue
                    d = next(iter(D))
                    u = next(iter(U))
                    if len({d, x, y, u}) != 4:
                        continue

                    if exts is None:
                        exts = linear_extensions(succ, n)
                    extset = set(exts)
                    words = {
                        (d, y, x, u): "A",
                        (d, x, y, u): "C",
                        (d, x, u, y): "X",
                        (x, d, y, u): "Y",
                        (x, d, u, y): "Z",
                        (x, u, d, y): "W",
                    }
                    cls = defaultdict(list)
                    for L in exts:
                        rel = tuple(sorted((d, x, y, u), key=L.index))
                        assert rel in words
                        cls[words[rel]].append(L)

                    # Exact current-state relabel injections Y -> A and W -> A.
                    imY = set()
                    for L in cls["Y"]:
                        T = list(L)
                        pos = {v: T.index(v) for v in (x, d, y)}
                        T[pos[x]], T[pos[d]], T[pos[y]] = d, y, x
                        T = tuple(T)
                        assert T in extset
                        assert tuple(sorted((d, x, y, u), key=T.index)) == (d, y, x, u)
                        imY.add(T)
                    assert len(imY) == len(cls["Y"])

                    imW = set()
                    for L in cls["W"]:
                        T = list(L)
                        pos = {v: T.index(v) for v in (x, u, d, y)}
                        T[pos[x]], T[pos[u]], T[pos[d]], T[pos[y]] = d, y, x, u
                        T = tuple(T)
                        assert T in extset
                        assert tuple(sorted((d, x, y, u), key=T.index)) == (d, y, x, u)
                        imW.add(T)
                    assert len(imW) == len(cls["W"])

                    unmatched = [L for L in cls["A"] if L not in (imY | imW)]
                    delta = len(cls["A"]) - len(cls["Y"]) - len(cls["W"])
                    assert len(unmatched) >= delta

                    G1 = [
                        r for r in range(n)
                        if r not in (d, x) and covers(succ, r, x, n) and incomparable(succ, r, d)
                    ]
                    G2 = [
                        r for r in range(n)
                        if r not in (d, x) and covers(succ, d, r, n) and incomparable(succ, r, x)
                    ]
                    assert len(G1) <= 2 and len(G2) <= 2

                    # If an A-extension is outside both injection images, the inverse
                    # Y relabel is invalid and a canonical G1/G2 Hasse blocker exists.
                    for L in unmatched:
                        T = list(L)
                        pos = {v: T.index(v) for v in (d, y, x)}
                        T[pos[d]], T[pos[y]], T[pos[x]] = x, d, y
                        assert tuple(T) not in extset

                        pd, py = L.index(d), L.index(y)
                        witnessed = any(pd < L.index(r) < py for r in G1)
                        witnessed |= any(pd < L.index(r) < py for r in G2)
                        assert witnessed

                    stats["states"] += 1
                    stats["extensions_examined"] += len(exts)
                    stats["positive_delta_states"] += int(delta > 0)
                    stats["total_positive_delta"] += max(delta, 0)
                    stats["unmatched_total"] += len(unmatched)

    print("POS3_BOUNDARY_OVERLOAD_EXPORT_CHECK_PASS")
    for n in range(3, 7):
        print(f"width_at_most_3_n{n}", width3_posets[n])
    for key in (
        "states",
        "extensions_examined",
        "positive_delta_states",
        "total_positive_delta",
        "unmatched_total",
    ):
        print(key, stats[key])


if __name__ == "__main__":
    main()
