from fractions import Fraction
from collections import Counter, defaultdict
from itertools import permutations, product
import math
import time
import numpy as np
import networkx as nx

# Frozen unresolved graph H = K_{5,5} \ C_10, v(H)=10, e(H)=15.
V_H = 10
E_H = 15


def pair_list(n):
    # Lower-triangular order. For n=8 the first 21 bits are exactly the n=7 edges,
    # then the seven edges incident with the new vertex 7.
    return [(i, j) for j in range(1, n) for i in range(j)]

PAIRS = {n: pair_list(n) for n in range(1, 9)}


def graph_code(G, n=None):
    if n is None:
        n = G.number_of_nodes()
    G = nx.convert_node_labels_to_integers(G, ordering="sorted")
    c = 0
    for k, (i, j) in enumerate(PAIRS[n]):
        if G.has_edge(i, j):
            c |= 1 << k
    return c


def neighbor_masks(code, n):
    nb = [0] * n
    for k, (i, j) in enumerate(PAIRS[n]):
        if (code >> k) & 1:
            nb[i] |= 1 << j
            nb[j] |= 1 << i
    return nb


def stable_colors(code, n):
    """Canonical 1-WL color refinement, starting from degrees.

    Color IDs are assigned by sorting exact signatures, so the color labels themselves
    are isomorphism-invariant, not dependent on vertex order.
    """
    nb = neighbor_masks(code, n)
    colors = [nb[i].bit_count() for i in range(n)]
    while True:
        signatures = []
        for i in range(n):
            cnt = Counter(colors[j] for j in range(n) if (nb[i] >> j) & 1)
            signatures.append((colors[i], tuple(sorted(cnt.items()))))
        palette = {sig: k for k, sig in enumerate(sorted(set(signatures)))}
        new_colors = [palette[sig] for sig in signatures]
        if new_colors == colors:
            return colors, nb
        colors = new_colors


def canonical_code(code, n):
    """Exact canonical adjacency code.

    Stable color classes are ordered canonically. Every permutation inside each
    color class is then enumerated, so no isomorphism-preserving relabeling is lost.
    Equal outputs imply isomorphism because the output is an adjacency code of an
    actual relabeling of the input graph.
    """
    colors, nb = stable_colors(code, n)
    classes = defaultdict(list)
    for v, c in enumerate(colors):
        classes[c].append(v)
    ordered_classes = [classes[c] for c in sorted(classes)]
    class_perms = [list(permutations(cls)) for cls in ordered_classes]

    best = None
    for pieces in product(*class_perms):
        order = tuple(v for piece in pieces for v in piece)
        out = 0
        bit = 0
        for b in range(1, n):
            ob = order[b]
            for a in range(b):
                if (nb[ob] >> order[a]) & 1:
                    out |= 1 << bit
                bit += 1
        if best is None or out < best:
            best = out
    return best


def burnside_unlabeled_count(n):
    """Exact number of unlabeled simple graphs on n vertices via Burnside."""
    pairs = PAIRS[n]
    pindex = {e: k for k, e in enumerate(pairs)}
    total = 0
    for perm in permutations(range(n)):
        seen = set()
        orbits = 0
        for idx in range(len(pairs)):
            if idx in seen:
                continue
            orbits += 1
            cur = idx
            while cur not in seen:
                seen.add(cur)
                i, j = pairs[cur]
                a, b = perm[i], perm[j]
                if a > b:
                    a, b = b, a
                cur = pindex[(a, b)]
        total += 1 << orbits
    assert total % math.factorial(n) == 0
    return total // math.factorial(n)


def triple_common_neighbor_tensor(code, n):
    nb = neighbor_masks(code, n)
    C = np.empty((n, n, n), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            ab = nb[a] & nb[b]
            for c in range(n):
                C[a, b, c] = (ab & nb[c]).bit_count()
    return C


def hom_trace(code, n):
    """Exact hom(H,G) as trace(T^5), T_(a,b),(b,c)=C(a,b,c)."""
    C = triple_common_neighbor_tensor(code, n)
    T = np.zeros((n * n, n * n), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            row = a * n + b
            for c in range(n):
                T[row, b * n + c] = C[a, b, c]
    T2 = T @ T
    T4 = T2 @ T2
    T5 = T4 @ T
    h = int(np.trace(T5))
    assert 0 <= h <= n ** V_H
    return h


def hom_contraction(code, n):
    """Previous five-tensor formula, used here as an independent computational cross-check."""
    C = triple_common_neighbor_tensor(code, n)
    h = int(np.einsum("cde,dea,eab,abc,bcd->", C, C, C, C, C, optimize=True))
    assert 0 <= h <= n ** V_H
    return h


def exact_defect(code, n):
    m = code.bit_count()
    h = hom_trace(code, n)
    return h, h * n ** 20 - (2 * m) ** 15


start = time.time()
print("C30 Sidorenko exact n=8 certificate")
print("H=K_{5,5}\\C_10; v(H)=10; e(H)=15")

# Recover the complete n=7 unlabeled base set from NetworkX's atlas, but certify its
# completeness independently by Burnside count and exact canonical-code uniqueness.
atlas7 = [nx.convert_node_labels_to_integers(G, ordering="sorted")
          for G in nx.graph_atlas_g() if G.number_of_nodes() == 7]
U7 = burnside_unlabeled_count(7)
assert U7 == 1044
assert len(atlas7) == U7
codes7 = [canonical_code(graph_code(G, 7), 7) for G in atlas7]
assert len(set(codes7)) == U7
print(f"n=7_base: atlas={len(atlas7)} burnside={U7} canonical_unique=PASS")

# New trace(T^5) formula must match the previous exact tensor contraction on every
# n=7 isomorphism class, rather than merely on a few examples.
for code in codes7:
    assert hom_trace(code, 7) == hom_contraction(code, 7)
print("trace_vs_previous_contraction_all_n7=PASS")

# Complete canonical augmentation from order 7 to order 8.
# Any 8-vertex graph loses one vertex to a 7-vertex graph; after relabeling that
# deletion graph to one of atlas7, the deleted vertex has one of 2^7 neighborhoods.
# Hence these 1044*128 extensions hit every 8-vertex isomorphism class.
canon8 = set()
extensions = 0
for base in codes7:
    for mask in range(1 << 7):
        extensions += 1
        # By lower-triangular bit order, bits 0..20 are edges among vertices 0..6,
        # and bits 21..27 are edges from vertex 7 to vertices 0..6.
        raw8 = base | (mask << 21)
        canon8.add(canonical_code(raw8, 8))

assert extensions == 1044 * 128 == 133632
U8 = burnside_unlabeled_count(8)
assert U8 == 12346
assert len(canon8) == U8
print(f"n=8_generation: extensions={extensions} distinct_canonical={len(canon8)} burnside={U8} COMPLETE=PASS")

violations = []
min_ratio = None
min_record = None
for code in sorted(canon8):
    h, D = exact_defect(code, 8)
    m = code.bit_count()
    if D < 0:
        violations.append((code, m, h, D))
    if m > 0:
        ratio = Fraction(h * 8 ** 20, (2 * m) ** 15)
        if min_ratio is None or ratio < min_ratio:
            min_ratio = ratio
            min_record = (code, m, h, D)

assert not violations
assert min_ratio is not None
code, m, h, D = min_record
assert code == (1 << 28) - 1  # K_8
assert m == 28
assert h == 147104216
assert min_ratio == Fraction(688615849984, 678223072849)

print("n=8_violations=0")
print(f"n=8_min_nonempty_ratio={min_ratio} ~= {float(min_ratio):.15f}")
print(f"n=8_minimizer_canonical_code={code} edge_count={m} hom={h} defect={D}")
print("n=8_minimizer=K_8")
print("largest_completely_checked_host_order=8")
print(f"elapsed_seconds={time.time()-start:.3f}")
print("ALL_EXACT_CHECKS_PASS")
