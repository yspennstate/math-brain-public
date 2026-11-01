#!/usr/bin/env python3
"""
Exact self-check for the I0122 critical-pair distance-layer inequalities.

Enumeration convention:
For each n<=6, enumerate every transitively closed subset of the forward
relations i<j in the natural order. Every finite poset has some linear
extension, so after relabeling by that extension every poset on <=6 elements
appears in this enumeration (usually many times). This is a coverage check,
not an isomorphism-class census.

All arithmetic is integer/Fraction exact.
"""
from itertools import combinations, product, permutations
from fractions import Fraction
from collections import Counter

def posets_with_natural_linear_extension(n):
    pairs = list(combinations(range(n), 2))
    for bits in product((0, 1), repeat=len(pairs)):
        lt = [[False]*n for _ in range(n)]
        for (i,j), b in zip(pairs, bits):
            if b:
                lt[i][j] = True
        cl = [row[:] for row in lt]
        for k in range(n):
            for i in range(n):
                if cl[i][k]:
                    for j in range(n):
                        if cl[k][j]:
                            cl[i][j] = True
        if all(cl[i][j] == bool(b) for (i,j), b in zip(pairs, bits)):
            yield cl

def linear_extensions(lt):
    n = len(lt)
    pred = [0]*n
    for x in range(n):
        mask = 0
        for z in range(n):
            if lt[z][x]:
                mask |= 1 << z
        pred[x] = mask
    out = []
    def rec(mask, seq):
        if len(seq) == n:
            out.append(tuple(seq))
            return
        for x in range(n):
            if not ((mask >> x) & 1) and not (pred[x] & ~mask):
                rec(mask | (1 << x), seq + (x,))
    rec(0, ())
    return out

def is_incomparable(lt, x, y):
    return x != y and not lt[x][y] and not lt[y][x]

def is_critical(lt, x, y):
    # D(x) subset D(y), U(y) subset U(x)
    n = len(lt)
    if not is_incomparable(lt, x, y):
        return False
    return (
        all((not lt[z][x]) or lt[z][y] for z in range(n))
        and all((not lt[y][z]) or lt[x][z] for z in range(n))
    )

def slaves(lt, x, y):
    # Peczarski slave for ordered incomparable pair (x,y):
    # z>x and z||y, or z<y and z||x.
    n = len(lt)
    ss = []
    for z in range(n):
        if z in (x,y):
            continue
        upper = lt[x][z] and is_incomparable(lt, z, y)
        lower = lt[z][y] and is_incomparable(lt, z, x)
        if upper or lower:
            ss.append(z)
    return ss

def transitive_reduction_edges(lt):
    n = len(lt)
    ans = []
    for i in range(n):
        for j in range(n):
            if lt[i][j] and not any(
                k not in (i,j) and lt[i][k] and lt[k][j]
                for k in range(n)
            ):
                ans.append((i,j))
    return ans

def analyze(lt):
    n = len(lt)
    exts = linear_extensions(lt)
    N = len(exts)
    positions = []
    rank_sum = [0]*n
    for L in exts:
        pos = [0]*n
        for r,x in enumerate(L, start=1):
            pos[x] = r
            rank_sum[x] += r
        positions.append(pos)
    mu = [Fraction(s,N) for s in rank_sum]

    records = []
    for x,y in permutations(range(n), 2):
        if not is_critical(lt, x, y):
            continue
        A = Counter()
        B = Counter()
        for pos in positions:
            if pos[x] < pos[y]:
                A[pos[y]-pos[x]] += 1
            else:
                B[pos[x]-pos[y]] += 1

        # Critical swap injection: B_k -> A_k, and adjacency gives equality at k=1.
        assert A[1] == B[1], (n,x,y,A,B)
        for k in range(1,n):
            assert A[k] >= B[k], (n,x,y,k,A,B)

        p = Fraction(sum(A.values()), N)
        q = Fraction(sum(B.values()), N)
        d = mu[y] - mu[x]
        assert p + q == 1
        assert d >= 0

        # Exact identity and main theorem.
        signed_excess = sum(Fraction(A[k]-B[k],N) for k in range(2,n))
        signed_moment = sum(Fraction(k*(A[k]-B[k]),N) for k in range(2,n))
        assert signed_excess == p-q
        assert signed_moment == d
        assert d >= 2*(p-q)
        assert d <= (n-1)*(p-q)
        assert p <= Fraction(1,2) + d/Fraction(4,1)

        # Layer-2 refinement when d<=1 and p>2/3.
        if d <= 1 and p > Fraction(2,3):
            r2 = Fraction(A[2]-B[2], N)
            lower = 3*(2*p-1)-d
            assert r2 >= lower
            assert r2 > 0

            # Since B_2 injects into A_2, A_2>B_2 ensures a distance-2
            # majority extension outside the image. Such an extension must
            # have its unique intervening element among the slaves.
            # Verify directly that at least one distance-2 majority extension
            # has an intervening slave.
            ss = set(slaves(lt,x,y))
            found = False
            for L,pos in zip(exts,positions):
                if pos[y]-pos[x] == 2:
                    z = L[pos[x]]  # 0-index list: between positions r and r+2
                    # pos[x] is 1-based; L[pos[x]] is the unique middle item.
                    if z in ss:
                        found = True
                        break
            assert found, (n,x,y,A,B,ss)

        records.append((x,y,p,d,A,B,mu))
    return records

def fmt(f):
    return f"{f.numerator}/{f.denominator}"

def main():
    print("I0122 critical-pair layer exact check")
    print("arithmetic=exact Fraction/integer")
    global_best = None

    for n in range(2,7):
        poset_representations = 0
        critical_pairs = 0
        best = None
        best_payload = None

        for lt in posets_with_natural_linear_extension(n):
            poset_representations += 1
            records = analyze(lt)
            critical_pairs += len(records)
            for x,y,p,d,A,B,mu in records:
                if p > Fraction(2,3):
                    key = (d, p)
                    if best is None or key < best:
                        best = key
                        best_payload = (
                            x,y,p,d,A,B,mu,
                            transitive_reduction_edges(lt),
                            slaves(lt,x,y)
                        )
                    if global_best is None or key < global_best[0]:
                        global_best = (key,n,best_payload)

        print(
            f"n={n} forward_transitive_representations={poset_representations} "
            f"ordered_critical_pairs_checked={critical_pairs}"
        )
        if best_payload is None:
            print("  no critical pair with p>2/3")
        else:
            x,y,p,d,A,B,mu,covers,ss = best_payload
            print(
                "  minimum d among checked critical pairs with p>2/3: "
                f"d={fmt(d)}, p={fmt(p)}, pair=({x},{y}), slaves={ss}"
            )
            print(f"  covers={covers}")
            print(
                "  distance layers A_k="
                + str(dict(sorted(A.items())))
                + " B_k="
                + str(dict(sorted(B.items())))
            )

    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
