from math import comb
from fractions import Fraction


def tree_count(s):
    if s == 0:
        return 1
    if s == 1:
        return 1
    return s ** (s - 2)


def edge_tree(k):
    # labelled tree on k+2 vertices containing one specified edge
    if k == 0:
        return 1
    s = k + 2
    return 2 * (s ** (s - 3))


def pair_same_tree(k):
    # labelled tree on k+2 vertices in which two distinguished vertices are in the same tree
    # here the component itself is a tree on all k+2 vertices
    s = k + 2
    return s ** (s - 2)


def two_disjoint_edges_tree(k):
    # labelled tree on k+4 vertices containing two specified disjoint edges
    s = k + 4
    return 4 * (s ** (s - 4))


NMAX = 100
F = [0] * (NMAX + 1)
F[0] = 1
for n in range(1, NMAX + 1):
    F[n] = sum(comb(n - 1, s - 1) * tree_count(s) * F[n - s] for s in range(1, n + 1))


def ze(n):
    return sum(comb(n-2, k) * edge_tree(k) * F[n-2-k] for k in range(n-1))


def zef_disjoint(n):
    same = sum(comb(n-4, k) * two_disjoint_edges_tree(k) * F[n-4-k] for k in range(n-3))
    sep = 0
    ordinary = n - 4
    for k in range(ordinary + 1):
        for l in range(ordinary - k + 1):
            r = ordinary - k - l
            multinomial = comb(ordinary, k) * comb(ordinary-k, l)
            sep += multinomial * edge_tree(k) * edge_tree(l) * F[r]
    return same + sep


def q_disjoint(n):
    # Overlap H in K_n-{e,f}: H+e and H+f individually acyclic,
    # H+e+f cyclic. For disjoint e=12,f=34, H has exactly two
    # relevant components pairing endpoints crosswise: 1~3,2~4 or 1~4,2~3.
    ordinary = n - 4
    q = 0
    for k in range(ordinary + 1):
        for l in range(ordinary-k + 1):
            r = ordinary-k-l
            multinomial = comb(ordinary, k) * comb(ordinary-k, l)
            q += 2 * multinomial * pair_same_tree(k) * pair_same_tree(l) * F[r]
    return q


def row(n):
    Z = F[n]
    Ze = ze(n)
    Zef = zef_disjoint(n)
    q = q_disjoint(n)

    # Activity-weighted spanning-tree cells with edge order e<f<others.
    D = 4 * Zef
    B = 2 * Ze - D
    C = 2 * Ze - q - D
    A = Z - B - C - D
    B0 = B - 2*q
    C0 = C - q

    Delta = Ze*Ze - Z*Zef
    lhs_resid = (B0 + 2*q) * (C0 + 2*q) - D * (A - q)
    assert lhs_resid == 4 * Delta
    assert all(x >= 0 for x in (A, B, C, D, B0, C0, q))
    assert Delta > 0

    denom = (B0 + 2*q) * (C0 + 2*q)
    R = Fraction(D * (A-q), denom)
    gap = 1 - R
    gap_alt = Fraction(4*Delta, denom)
    assert gap == gap_alt
    # By symmetry denom=4(Ze-2Zef)^2, hence 1-R = Delta/(Ze-2Zef)^2.
    assert gap == Fraction(Delta, (Ze - 2*Zef)**2)
    return Z, Ze, Zef, q, A, B0, C0, D, gap


for n in range(4, NMAX+1):
    row(n)

for n in (4, 5, 6, 7, 8, 10):
    Z, Ze, Zef, q, A, B0, C0, D, gap = row(n)
    print(f"n={n} Z={Z} Ze={Ze} Zef={Zef} q={q} A={A} B0={B0} C0={C0} D={D}")
    print(f"  one_minus_R={float(gap):.15g} n2_gap={float(gap*n*n):.15g}")

for n in (20, 50, 100):
    *_, gap = row(n)
    print(f"n={n} one_minus_R={float(gap):.15g} n2_gap={float(gap*n*n):.15g}")

print("IDENTITY_CHECKS_N4_TO_N100=PASS")
print("DELTA_POSITIVE_N4_TO_N100=PASS")
print("ACTIVITY_RESIDUAL_RATIO_APPROACHES_ONE_NUMERICALLY=YES")
