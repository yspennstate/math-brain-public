#!/usr/bin/env python3
"""Exact regression checks for the POS3 deletion cut-charge identity and clean-fork collapse."""
from collections import defaultdict, Counter


def closure(n, covers):
    R = [[False] * n for _ in range(n)]
    for a, b in covers:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    return R


def extensions(n, covers):
    R = closure(n, covers)
    pred = [{u for u in range(n) if R[u][v]} for v in range(n)]
    out = []

    def rec(word, rem):
        if not rem:
            out.append(tuple(word))
            return
        used = set(word)
        for v in sorted(rem):
            if pred[v] <= used:
                rec(word + [v], rem - {v})

    rec([], set(range(n)))
    return out, R


def pair_signed(exts, u, v):
    a = sum(L.index(u) < L.index(v) for L in exts)
    return 2 * a - len(exts), a


def verify_cut_charge():
    covers = [
        (0, 2), (0, 3), (0, 4), (1, 4), (1, 5), (2, 5),
        (3, 6), (3, 7), (4, 7), (4, 8), (5, 8), (6, 8),
    ]
    ext, _ = extensions(9, covers)
    assert len(ext) == 349
    C = (2, 5, 8)
    Q = (0, 1, 3, 4, 6, 7)

    # Verify the integer cut-charge identity for every ordered retained pair.
    for x in Q:
        for y in Q:
            if x == y:
                continue
            rq = rp = 0
            for L in ext:
                qword = [v for v in L if v in Q]
                rq += qword.index(y) - qword.index(x)
                rp += L.index(y) - L.index(x)
            lhs = 0
            for c in C:
                bx, _ = pair_signed(ext, x, c)
                by, _ = pair_signed(ext, y, c)
                lhs += bx - by
            assert lhs == 2 * (rp - rq), (x, y, lhs, rp, rq)

    selected = {}
    for x, y in ((0, 1), (1, 3), (4, 6), (6, 7)):
        rq = rp = 0
        pieces = []
        for L in ext:
            qword = [v for v in L if v in Q]
            rq += qword.index(y) - qword.index(x)
            rp += L.index(y) - L.index(x)
        for c in C:
            bx, _ = pair_signed(ext, x, c)
            by, _ = pair_signed(ext, y, c)
            pieces.append((c, bx, by, bx - by))
        selected[(x, y)] = (rq, rp, pieces)

    # The two known cross-interface rescuing pairs are exact.
    assert pair_signed(ext, 3, 2)[1] == 193  # P(2<3)=156/349.
    assert pair_signed(ext, 6, 5)[1] == 193  # P(5<6)=156/349.
    return selected


def deletion_channels_equal_pred():
    covers = [
        (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 2), (1, 5), (2, 5), (4, 5), (4, 6),
    ]
    ext, R = extensions(7, covers)
    assert len(ext) == 79
    a, b = 4, 3

    def pred(v):
        return {u for u in range(7) if R[u][v]}

    assert pred(a) == pred(b) == {0}
    assert pair_signed(ext, a, b)[1] == 56

    fibers = defaultdict(list)
    for L in ext:
        tau = tuple(v for v in L if v not in (a, b))
        fibers[tau].append(L)

    pos_channels = Counter()
    neg_channels = Counter()
    defect_total = 0
    for tau in fibers:
        n = len(tau)

        def interval(v):
            lo = max([tau.index(q) + 1 for q in tau if R[q][v]] + [0])
            hi = min([tau.index(q) for q in tau if R[v][q]] + [n])
            return lo, hi

        la, ua = interval(a)
        lb, ub = interval(b)
        assert la == lb
        r = ua - la + 1
        s = ub - lb + 1
        defect = min(r, s) * (s - r)
        defect_total += defect
        if defect > 0:
            pos_channels[tau[ua]] += defect
        elif defect < 0:
            neg_channels[tau[ub]] += -defect

    assert defect_total == 33
    assert dict(pos_channels) == {5: 10, 6: 23}
    assert not neg_channels
    # The first clean fork terminates at unequal predecessor sets.
    assert pred(6) == {0, 4}
    assert pred(5) == {0, 1, 2, 4}
    # The known balanced escape remains present.
    assert pair_signed(ext, 2, 3)[1] == 42
    return dict(pos_channels), pred(6), pred(5)


if __name__ == "__main__":
    selected = verify_cut_charge()
    channels, p6, p5 = deletion_channels_equal_pred()
    print("CUT_CHARGE_ALL_ORDERED_Q_PAIRS=PASS")
    for pair, (rq, rp, pieces) in selected.items():
        print(
            "BOUNDARY", pair, "Q_RANK_NUM", rq, "P_RANK_NUM", rp,
            "CHARGE_PIECES", pieces, "TOTAL", sum(p[3] for p in pieces),
        )
    print("SEVEN_POINT_CHANNELS", channels)
    print("SEVEN_POINT_PRED6", sorted(p6), "PRED5", sorted(p5))
    print("POS3_B19_CUT_CHARGE_FORK_COLLAPSE_CHECK_PASS")
