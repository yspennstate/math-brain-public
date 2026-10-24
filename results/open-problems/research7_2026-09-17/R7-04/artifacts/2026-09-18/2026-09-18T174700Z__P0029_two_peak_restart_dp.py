#!/usr/bin/env python3
"""Exact subset DP for R7-04 / P0029 (Burdzy Problem 9).

A labeling is represented by its descending-label vertex order.  A vertex is a
peak iff, when revealed, it has no neighbor among the previously revealed
vertices.  Thus exactly-two-peak labelings are exactly orders with two births.

The program uses Python arbitrary-precision integers.  It prints the exact
number of two-peak labelings, exact distance sum, exact normalized expectation,
and (optionally) the distance distribution.  For small graphs it can also
brute-force every permutation as an independent check.

No randomness or floating-point arithmetic enters the certificate itself.
"""

from __future__ import annotations

import argparse
import itertools
from fractions import Fraction


def grid_graph(rows: int, cols: int):
    nverts = rows * cols
    neigh = [0] * nverts
    coords = []
    for i in range(rows):
        for j in range(cols):
            v = i * cols + j
            coords.append((i, j))
            mask = 0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < rows and 0 <= jj < cols:
                    mask |= 1 << (ii * cols + jj)
            neigh[v] = mask

    dist = [[0] * nverts for _ in range(nverts)]
    for u, (i, j) in enumerate(coords):
        for v, (ii, jj) in enumerate(coords):
            dist[u][v] = abs(i - ii) + abs(j - jj)
    return neigh, dist, coords


def exact_two_peak_dp(rows: int, cols: int, keep_distribution: bool = True):
    """Return (count, distance_sum, distance_distribution).

    one[mask] is a dict root -> number of reveal orders of mask with exactly
    one birth, whose root/first birth is root.

    two[mask] counts reveal orders of mask with exactly two births.
    dsum[mask] sums the distance between the two births over those orders.
    """

    neigh, dist, _ = grid_graph(rows, cols)
    nverts = rows * cols
    nstates = 1 << nverts
    full = nstates - 1

    one = [None] * nstates
    two = [0] * nstates
    dsum = [0] * nstates

    maxdist = (rows - 1) + (cols - 1)
    by_distance = (
        [[0] * (maxdist + 1) for _ in range(nstates)]
        if keep_distribution
        else None
    )

    for root in range(nverts):
        mask = 1 << root
        if one[mask] is None:
            one[mask] = {}
        one[mask][root] = 1

    # Adding a bit strictly increases the integer mask, so ascending masks is
    # a valid topological order for every transition.
    for mask in range(1, nstates):
        roots = one[mask]
        if roots:
            for root, count in tuple(roots.items()):
                remaining = full ^ mask
                x = remaining
                while x:
                    bit = x & -x
                    v = bit.bit_length() - 1
                    newmask = mask | bit
                    if neigh[v] & mask:
                        if one[newmask] is None:
                            one[newmask] = {}
                        one[newmask][root] = one[newmask].get(root, 0) + count
                    else:
                        # Second birth / second peak.
                        d = dist[root][v]
                        two[newmask] += count
                        dsum[newmask] += count * d
                        if by_distance is not None:
                            by_distance[newmask][d] += count
                    x -= bit

        if two[mask]:
            remaining = full ^ mask
            x = remaining
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                if neigh[v] & mask:
                    newmask = mask | bit
                    two[newmask] += two[mask]
                    dsum[newmask] += dsum[mask]
                    if by_distance is not None:
                        src = by_distance[mask]
                        dst = by_distance[newmask]
                        for d, count in enumerate(src):
                            dst[d] += count
                # If v has no neighbor in mask it would create a third peak,
                # so that transition is intentionally discarded.
                x -= bit

    return two[full], dsum[full], (by_distance[full] if by_distance else None)


def brute_force(rows: int, cols: int):
    """Independent exact enumeration; intended only for very small grids."""
    neigh, _, coords = grid_graph(rows, cols)
    nverts = rows * cols
    count = 0
    dsum = 0
    for order in itertools.permutations(range(nverts)):
        earlier = 0
        peaks = []
        for v in order:
            if not (neigh[v] & earlier):
                peaks.append(v)
                if len(peaks) > 2:
                    break
            earlier |= 1 << v
        if len(peaks) == 2:
            count += 1
            i, j = coords[peaks[0]]
            ii, jj = coords[peaks[1]]
            dsum += abs(i - ii) + abs(j - jj)
    return count, dsum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", type=int)
    parser.add_argument("cols", type=int)
    parser.add_argument(
        "--bruteforce",
        action="store_true",
        help="independently enumerate all permutations (small grids only)",
    )
    args = parser.parse_args()

    count, dsum, distribution = exact_two_peak_dp(args.rows, args.cols, True)
    print(f"grid={args.rows}x{args.cols}")
    print(f"two_peak_labelings={count}")
    print(f"distance_sum={dsum}")
    print(f"mean_distance={Fraction(dsum, count)}")
    if args.rows == args.cols:
        print(f"normalized_mean={Fraction(dsum, count * args.rows)}")
    print("distance_distribution=")
    for d, c in enumerate(distribution):
        if c:
            print(f"  {d}: {c}")

    if args.bruteforce:
        brute_count, brute_dsum = brute_force(args.rows, args.cols)
        print(f"bruteforce_two_peak_labelings={brute_count}")
        print(f"bruteforce_distance_sum={brute_dsum}")
        assert brute_count == count
        assert brute_dsum == dsum
        print("BRUTE_FORCE_MATCH=YES")


if __name__ == "__main__":
    main()
