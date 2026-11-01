from itertools import combinations
from fractions import Fraction
from collections import defaultdict

# Exact finite self-check supporting the displayed-range Gram-perturbation
# reducibility certificates described in the first SMALL6 immutable report.
# A nonzero coefficient-preserving symmetric perturbation on the displayed
# square coordinates is a sound reducibility certificate; kernel_dim=0 is
# only a search screen and is NOT used as an irreducibility certificate.

SOURCE_E1 = [
    (1,1),(1,2),(2,3),(2,4),(3,1),(3,3),(3,5),(4,2),
    (4,4),(4,5),(5,2),(5,3),(5,6),(6,1),(6,4),(6,6),
]
SOURCE_E2 = [
    ((1,4),(6,5)),((1,5),(2,2)),((3,6),(6,2)),((2,6),(4,3)),
    ((1,6),(2,5)),((3,4),(5,1)),((1,3),(4,1)),((5,5),(6,3)),
]
SOURCE_HOLES = [(2,1),(3,2),(4,6),(5,4)]

NEAR_E1 = [
    (1,1),(1,2),(1,3),(2,1),(2,4),(2,5),(3,2),(3,4),
    (3,6),(4,3),(4,5),(4,6),(5,1),(5,6),(6,2),(6,5),
]
NEAR_E2 = [
    ((1,4),(4,1)),((1,5),(5,5)),((1,6),(2,2)),((2,3),(3,1)),
    ((3,3),(6,6)),((3,5),(6,1)),((4,2),(5,3)),((4,4),(6,4)),
    ((5,2),(5,4)),
]

def rank_q(rows, ncols):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r

def displayed_range_kernel_dim(e1, e2):
    # Each displayed square is one coordinate.  An E1 square has one cell;
    # an E2 square has its two halves represented by the same coordinate.
    edges = [(p,) for p in e1] + [tuple(pair) for pair in e2]
    N = len(edges)
    variables = list(combinations(range(N), 2))
    vid = {ab: i for i, ab in enumerate(variables)}

    # Group off-diagonal Gram entries by the biquadratic monomial they
    # produce.  The homogeneous coefficient-preservation equations say
    # that the sum in every group is zero.
    coeff = defaultdict(lambda: defaultdict(int))
    for a, b in variables:
        for p in edges[a]:
            for q in edges[b]:
                key = (tuple(sorted((p[0], q[0]))),
                       tuple(sorted((p[1], q[1]))))
                coeff[key][vid[(a, b)]] += 1

    rows = []
    for d in coeff.values():
        row = [0] * len(variables)
        for j, v in d.items():
            row[j] = v
        rows.append(row)

    rank = rank_q(rows, len(variables))
    return N, len(variables), rank, len(variables) - rank

def main():
    source = displayed_range_kernel_dim(SOURCE_E1, SOURCE_E2)
    assert source == (24, 276, 276, 0)
    print("SOURCE_N24 N=%d vars=%d rank=%d kernel_dim=%d" % source)

    ext = []
    for a, b in combinations(SOURCE_HOLES, 2):
        t = displayed_range_kernel_dim(SOURCE_E1, SOURCE_E2 + [(a, b)])
        ext.append((a, b, t[-1]))
    assert [x[-1] for x in ext] == [1, 3, 0, 0, 2, 0]
    print("SOURCE_N24_ONE_EDGE_EXTENSION_DISPLAYED_RANGE_KERNELS")
    for a, b, d in ext:
        print("  extension=%s--%s kernel_dim=%d reducible_certificate=%s" %
              (a, b, d, d > 0))

    near = displayed_range_kernel_dim(NEAR_E1, NEAR_E2)
    assert near == (25, 300, 296, 4)
    print("NEAR_N25 N=%d vars=%d rank=%d kernel_dim=%d reducible_certificate=True" % near)
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
