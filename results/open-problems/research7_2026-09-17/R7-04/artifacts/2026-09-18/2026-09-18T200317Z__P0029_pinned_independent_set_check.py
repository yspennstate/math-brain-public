#!/usr/bin/env python3
r"""
Exact certificate for R7-04 / P0029.

Implements the root-pinned independent-set expansion specialized from the
successive-ordering inclusion-exclusion mechanism:

  b(empty)=1,
  b(I)=|N[I]|^{-1} sum_{x in I} b(I\{x}) for independent I.

For a fixed first peak r and a non-neighbour v,

  W(r,v)/(N-1)! =
    sum_{I independent, I subset V\N[r], v in I}
      (-1)^{|I|-1} b(I),

where W(r,v) counts full labelings with exactly two peaks, first r and second v.

For the rank-2 completion count,

  F({r,v})/(N-2)! =
    sum_{I independent, I disjoint from N[r] union N[v]}
      (-1)^{|I|} b(I).

All arithmetic is exact Python Fraction / arbitrary-precision integer.
For n <= 4 we independently compute W by the older subset prefix/completion DP
and assert equality pair-by-pair. Then we extend the full exactly-two-peak
distribution to the 5x5 square.
"""

from fractions import Fraction
from math import factorial
from collections import Counter


def grid_graph(n):
    N = n*n
    neigh = []
    closed = []
    for r in range(n):
        for c in range(n):
            m = 0
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                rr, cc = r+dr, c+dc
                if 0 <= rr < n and 0 <= cc < n:
                    m |= 1 << (rr*n+cc)
            neigh.append(m)
            closed.append(m | (1 << (r*n+c)))
    return N, neigh, closed


def independent_masks_grid(n):
    row_patterns = [p for p in range(1 << n) if (p & (p << 1)) == 0]
    out = []
    def rec(row, prev, mask):
        if row == n:
            out.append(mask)
            return
        for p in row_patterns:
            if (p & prev) == 0:
                rec(row+1, p, mask | (p << (row*n)))
    rec(0, 0, 0)
    return out


def b_weights_grid(n):
    N, neigh, closed = grid_graph(n)
    ims = independent_masks_grid(n)
    ims.sort(key=int.bit_count)
    b = {0: Fraction(1,1)}
    for mask in ims[1:]:
        m = mask
        closed_union = 0
        numerator = Fraction(0,1)
        while m:
            bit = m & -m
            i = bit.bit_length()-1
            closed_union |= closed[i]
            numerator += b[mask ^ bit]
            m ^= bit
        b[mask] = numerator / closed_union.bit_count()
    return N, neigh, closed, ims, b


def exact_pair_weights_independent_sets(n):
    N, neigh, closed, ims, b = b_weights_grid(n)

    # Exact W(r,v): first peak r; unique additional peak v.
    accum = [[Fraction(0,1) for _ in range(N)] for __ in range(N)]
    for r in range(N):
        forbidden = closed[r]
        for I in ims:
            if I == 0 or (I & forbidden):
                continue
            coeff = b[I] if ((I.bit_count()-1) % 2 == 0) else -b[I]
            m = I
            while m:
                bit = m & -m
                v = bit.bit_length()-1
                accum[r][v] += coeff
                m ^= bit

    W = {}
    factW = factorial(N-1)
    for r in range(N):
        for v in range(N):
            if v == r or ((neigh[r] >> v) & 1):
                continue
            z = accum[r][v] * factW
            assert z.denominator == 1
            W[(r,v)] = int(z)

    # Exact rank-2 F({r,v}), unordered pair.
    signed = []
    for I in ims:
        signed.append((I, b[I] if I.bit_count() % 2 == 0 else -b[I]))
    F = {}
    factF = factorial(N-2)
    for r in range(N):
        for v in range(r+1, N):
            if (neigh[r] >> v) & 1:
                continue
            forbidden = closed[r] | closed[v]
            p = Fraction(0,1)
            for I, coeff in signed:
                if (I & forbidden) == 0:
                    p += coeff
            z = p * factF
            assert z.denominator == 1
            F[(r,v)] = int(z)

    return W, F, len(ims)


def exact_W_subset_dp(n):
    """Independent older prefix/completion DP, used only for n<=4."""
    N, neigh, _ = grid_graph(n)
    M = 1 << N
    full = M-1

    neigh_union = [0]*M
    buckets = [[] for _ in range(N+1)]
    for m in range(1, M):
        bit = m & -m
        i = bit.bit_length()-1
        neigh_union[m] = neigh_union[m ^ bit] | neigh[i]
        buckets[m.bit_count()].append(m)

    F = [0]*M
    F[full] = 1
    for sz in range(N-1, 0, -1):
        for S in buckets[sz]:
            frontier = neigh_union[S] & ~S & full
            t = 0
            m = frontier
            while m:
                bit = m & -m
                t += F[S | bit]
                m ^= bit
            F[S] = t

    W = {}
    for r in range(N):
        A = [0]*M
        A[1 << r] = 1
        for sz in range(2, N):
            for S in buckets[sz]:
                if ((S >> r) & 1) == 0:
                    continue
                total = 0
                m = S & ~(1 << r)
                while m:
                    bit = m & -m
                    i = bit.bit_length()-1
                    prev = S ^ bit
                    if neigh[i] & prev:
                        total += A[prev]
                    m ^= bit
                A[S] = total

        for v in range(N):
            if v == r or ((neigh[r] >> v) & 1):
                continue
            forbidden = (1 << v) | neigh[v]
            total = 0
            for sz in range(1, N):
                for S in buckets[sz]:
                    if ((S >> r) & 1) == 0 or (S & forbidden):
                        continue
                    if A[S]:
                        total += A[S] * F[S | (1 << v)]
            W[(r,v)] = total
    return W


def dist(n, a, b):
    ar, ac = divmod(a,n)
    br, bc = divmod(b,n)
    return abs(ar-br)+abs(ac-bc)


def report(n, W, F, indep_count):
    total = sum(W.values())
    dcount = Counter()
    for (r,v), w in W.items():
        dcount[dist(n,r,v)] += w
    num = sum(d*w for d,w in dcount.items())
    norm_mean = Fraction(num, total*n)

    ratios = []
    for (r,v), f in F.items():
        H = W[(r,v)] + W[(v,r)]
        ratios.append((Fraction(H,2*f), r, v, H, f))
    lo = min(ratios)
    hi = max(ratios)

    print(f"=== {n}x{n} ===")
    print(f"independent_sets={indep_count}")
    print(f"exactly_two_peak_labelings={total}")
    print(f"E[rho_n/n | exactly two peaks]={norm_mean} ~= {float(norm_mean):.15f}")
    print("distance_distribution_counts:")
    for d in sorted(dcount):
        print(f"  d={d}: {dcount[d]} ; prob={Fraction(dcount[d],total)}")
    print(f"unordered_promotion_tilt_min={lo[0]} ~= {float(lo[0]):.15f}"
          f" pair={divmod(lo[1],n)}--{divmod(lo[2],n)}")
    print(f"unordered_promotion_tilt_max={hi[0]} ~= {float(hi[0]):.15f}"
          f" pair={divmod(hi[1],n)}--{divmod(hi[2],n)}")
    print()


def main():
    expected_totals = {
        2: 8,
        3: 143808,
        4: 779299174080,
    }
    expected_means = {
        2: Fraction(1,1),
        3: Fraction(666,749),
        4: Fraction(377754599,463868556),
    }

    for n in (2,3,4):
        W, F, cnt = exact_pair_weights_independent_sets(n)
        W2 = exact_W_subset_dp(n)
        assert W == W2
        total = sum(W.values())
        assert total == expected_totals[n]
        num = sum(dist(n,r,v)*w for (r,v),w in W.items())
        mean = Fraction(num,total*n)
        assert mean == expected_means[n]
        print(f"crosscheck_{n}x{n}=PASS")
        report(n,W,F,cnt)

    W5, F5, cnt5 = exact_pair_weights_independent_sets(5)
    total5 = sum(W5.values())
    assert total5 == 7063261481362958280000
    num5 = sum(dist(5,r,v)*w for (r,v),w in W5.items())
    mean5 = Fraction(num5,total5*5)
    assert mean5 == Fraction(5689414559220285956,7357564043086414875)
    print("5x5_independent_set_certificate=PASS")
    report(5,W5,F5,cnt5)

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
