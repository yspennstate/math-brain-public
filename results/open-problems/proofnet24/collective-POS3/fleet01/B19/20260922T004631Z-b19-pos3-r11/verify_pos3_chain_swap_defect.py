#!/usr/bin/env python3
"""Deterministic regression checks for the POS3 arbitrary-chain swap-defect theorem.

No external packages. The proof is in REPORT.md; this script checks:
(1) the local interval reflection/defect formula exhaustively for m <= 8;
(2) the dual chain-prefix recurrence against direct full-extension enumeration
    for all small antichain remainder profiles with m,n <= 3;
(3) the source-valid width-two family with one adjacent swap having defect m.
"""

from itertools import permutations, product


def local_counts(A, B):
    a0, a1 = A
    b0, b1 = B
    uv = sum(1 for a in range(a0, a1 + 1)
             for b in range(b0, b1 + 1) if a <= b)
    vu = sum(1 for b in range(b0, b1 + 1)
             for a in range(a0, a1 + 1) if b <= a)
    return uv, vu


def short_gap_defect(A, B):
    a0, a1 = A
    b0, b1 = B
    delta = (b0 + b1) - (a0 + a1)
    assert delta >= 0
    return sum(1 for a in range(a0, a1 + 1)
               for b in range(b0, b1 + 1)
               if 0 <= b - a < delta)


def verify_local_interval_theorem():
    checked = 0
    for m in range(9):
        intervals = [(lo, hi) for lo in range(m + 1)
                     for hi in range(lo, m + 1)]
        for Iu in intervals:
            for Iv in intervals:
                if not (Iu[0] <= Iv[0] and Iu[1] <= Iv[1]):
                    continue
                for L in range(m + 1):
                    for U in range(L, m + 1):
                        A = (max(Iu[0], L), min(Iu[1], U))
                        B = (max(Iv[0], L), min(Iv[1], U))
                        if A[0] > A[1] or B[0] > B[1]:
                            continue
                        uv, vu = local_counts(A, B)
                        assert uv >= vu
                        assert uv - vu == short_gap_defect(A, B)
                        checked += 1
    return checked


def transitive_closure(rel):
    rel = set(rel)
    changed = True
    while changed:
        changed = False
        old = list(rel)
        for a, b in old:
            for c, d in old:
                if b == c and a != d and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    return rel


def poset_from_intervals(m, intervals):
    elems = [f"c{j+1}" for j in range(m)] + [
        f"q{i}" for i in range(len(intervals))
    ]
    rel = set()
    for i in range(m):
        for j in range(i + 1, m):
            rel.add((f"c{i+1}", f"c{j+1}"))
    for i, (lo, hi) in enumerate(intervals):
        q = f"q{i}"
        for j in range(1, lo + 1):
            rel.add((f"c{j}", q))
        for j in range(hi + 1, m + 1):
            rel.add((q, f"c{j}"))
    return elems, transitive_closure(rel)


def is_linear_extension(order, rel):
    pos = {x: i for i, x in enumerate(order)}
    return all(pos[a] < pos[b] for a, b in rel)


def dual_weight(tau, intervals, m):
    qidx = {f"q{i}": i for i in range(len(intervals))}
    ints = [intervals[qidx[q]] for q in tau]
    if not ints:
        return 1
    dp = {t: 1 for t in range(ints[0][0], ints[0][1] + 1)}
    for lo, hi in ints[1:]:
        new = {}
        prefix = 0
        for t in range(m + 1):
            prefix += dp.get(t, 0)
            if lo <= t <= hi:
                new[t] = prefix
        dp = new
    return sum(dp.values())


def verify_dual_fiber_recurrence():
    checked = 0
    for m in range(1, 4):
        all_intervals = [(lo, hi) for lo in range(m + 1)
                         for hi in range(lo, m + 1)]
        for n in range(1, 4):
            for intervals in product(all_intervals, repeat=n):
                # Pairwise overlap makes the q_i an antichain in the generated
                # source poset, so every q-permutation is a Q-linear extension.
                if any(max(intervals[i][0], intervals[j][0])
                       > min(intervals[i][1], intervals[j][1])
                       for i in range(n) for j in range(i)):
                    continue
                elems, rel = poset_from_intervals(m, intervals)
                full = [p for p in permutations(elems)
                        if is_linear_extension(p, rel)]
                q_elems = [f"q{i}" for i in range(n)]
                for tau in permutations(q_elems):
                    actual = sum(
                        1 for L in full
                        if tuple(x for x in L if x.startswith("q")) == tau
                    )
                    predicted = dual_weight(tau, intervals, m)
                    assert actual == predicted
                    checked += 1
    return checked


def verify_unbounded_single_swap_family():
    rows = []
    for m in range(1, 9):
        # C=c1<...<cm, u incomparable with C and v, and cm<v.
        # I(u)=[0,m], I(v)=[m,m].
        uv, vu = local_counts((0, m), (m, m))
        assert uv == m + 1
        assert vu == 1
        assert uv - vu == m
        rows.append((m, uv, vu, uv - vu))
    return rows


def main():
    local = verify_local_interval_theorem()
    dual = verify_dual_fiber_recurrence()
    rows = verify_unbounded_single_swap_family()
    print(f"local_interval_cases={local}")
    print(f"dual_fiber_cases={dual}")
    for m, uv, vu, defect in rows:
        print(f"single_swap_family m={m} W_uv={uv} W_vu={vu} defect={defect}")
    print("POS3_CHAIN_SWAP_DEFECT_CHECK_PASS")


if __name__ == "__main__":
    main()
