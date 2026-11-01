#!/usr/bin/env python3
"""Exact finite core for HARD7-06: cycle-code/cut-coset duality on K_5^(3).

All algebra is exact integer/Fraction arithmetic.  The script verifies:
(1) the factor-graph cut/cycle dimensions;
(2) the exact cut-coset one-hot representation of NAE solution counts;
(3) the exact cycle-code Fourier formula for all gauge sectors;
(4) Parseval over the gauge quotient;
(5) the d=6,k=3 nonbacktracking two-step branching factor 10 and x^2*10=10/9.
"""
from itertools import combinations, product
from fractions import Fraction
from collections import Counter

V = tuple(range(5))
clauses = tuple(combinations(V, 3))
M = len(clauses)
edges = tuple((v, a) for a, C in enumerate(clauses) for v in C)
E = len(edges)
edge_index = {e:i for i,e in enumerate(edges)}


def parity(x: int) -> int:
    return x.bit_count() & 1


def gf2_rref_basis(vecs):
    """Reduced row-space basis as integer bitmasks."""
    piv = {}
    for x in vecs:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p] = y
                for q in tuple(piv):
                    if q != p and ((piv[q] >> p) & 1):
                        piv[q] ^= y
                break
    return tuple(piv[p] for p in sorted(piv))


def gf2_nullspace(rowmasks, ncols):
    rows = list(rowmasks)
    r = 0
    pivcols = []
    for c in range(ncols):
        pivot = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        pivcols.append(c)
        r += 1
        if r == len(rows):
            break
    free = [c for c in range(ncols) if c not in pivcols]
    basis = []
    for f in free:
        x = 1 << f
        for i, p in enumerate(pivcols):
            if (rows[i] >> f) & 1:
                x |= 1 << p
        basis.append(x)
    return tuple(basis), tuple(pivcols)


incidence_rows = []
for v in V:
    mask = 0
    for a, C in enumerate(clauses):
        if v in C:
            mask ^= 1 << edge_index[(v, a)]
    incidence_rows.append(mask)
for a, C in enumerate(clauses):
    mask = 0
    for v in C:
        mask ^= 1 << edge_index[(v, a)]
    incidence_rows.append(mask)

cut_basis = gf2_rref_basis(incidence_rows)
cycle_basis, _ = gf2_nullspace(incidence_rows, E)
rank_cut = len(cut_basis)
beta = len(cycle_basis)
assert rank_cut == 14
assert beta == E - rank_cut == 16
assert all(parity(c & d) == 0 for c in cycle_basis for d in cut_basis)


def syndrome(mask: int) -> int:
    """Gauge/cut-coset coordinate: characters against the chosen cycle basis."""
    s = 0
    for i, b in enumerate(cycle_basis):
        if parity(mask & b):
            s |= 1 << i
    return s


factor_edge_ids = tuple(tuple(edge_index[(v, a)] for v in C) for a, C in enumerate(clauses))
sector_onehot_counts = [0] * (1 << beta)
for choice in product(range(3), repeat=M):
    y = 0
    for a, j in enumerate(choice):
        y |= 1 << factor_edge_ids[a][j]
    sector_onehot_counts[syndrome(y)] += 1
assert sum(sector_onehot_counts) == 3**M

ell = 0
for a, C in enumerate(clauses):
    ell |= 1 << edge_index[(min(C), a)]
q_signed = syndrome(ell)


def nae_solution_count(literal_mask: int) -> int:
    z = 0
    for bits in product((0,1), repeat=len(V)):
        ok = True
        for a, C in enumerate(clauses):
            vals = []
            for v in C:
                lit = (literal_mask >> edge_index[(v,a)]) & 1
                vals.append(bits[v] ^ lit)
            if vals[0] == vals[1] == vals[2]:
                ok = False
                break
        z += int(ok)
    return z

z_unsigned = nae_solution_count(0)
z_signed = nae_solution_count(ell)
assert z_unsigned == 2 * sector_onehot_counts[0]
assert z_signed == 2 * sector_onehot_counts[q_signed]
assert z_unsigned == 0
assert z_signed == 6

cycle_masks = []
for coord in range(1 << beta):
    b = 0
    for i, gen in enumerate(cycle_basis):
        if (coord >> i) & 1:
            b ^= gen
    cycle_masks.append(b)
    assert b.bit_count() % 2 == 0

D = 3**M
coeff_num = []
for b in cycle_masks:
    e = b.bit_count() // 2
    coeff_num.append(((-1)**e) * 3**(M-e))

fw = coeff_num[:]
h = 1
while h < len(fw):
    for i in range(0, len(fw), 2*h):
        for j in range(i, i+h):
            x, y = fw[j], fw[j+h]
            fw[j], fw[j+h] = x+y, x-y
    h *= 2


def z_from_fourier(q: int) -> Fraction:
    Fq = Fraction(fw[q], D)
    return Fraction(2**len(V), 1) * Fraction(3,4)**M * Fq

assert z_from_fourier(0) == z_unsigned
assert z_from_fourier(q_signed) == z_signed
for q in range(1 << beta):
    assert z_from_fourier(q) == 2 * sector_onehot_counts[q]

mean_F = sum(Fraction(x, D) for x in fw) / (1 << beta)
mean_F2 = sum(Fraction(x, D)**2 for x in fw) / (1 << beta)
cycle_l2 = sum(Fraction(1, 3**b.bit_count()) for b in cycle_masks)
assert mean_F == 1
assert mean_F2 == cycle_l2

hist = Counter(sector_onehot_counts)
occupied = sum(1 for c in sector_onehot_counts if c)
assert occupied == 41141
assert hist == Counter({0:24395, 1:25749, 2:13080, 3:2120, 4:180, 5:12})
assert q_signed == 65280
assert sector_onehot_counts[q_signed] == 3

d, k = 6, 3
branch2 = (d-1)*(k-1)
x = Fraction(1,3)
instability = branch2 * x*x
assert branch2 == 10
assert instability == Fraction(10,9)

print(f"factor_graph_vertices = {len(V)+M}")
print(f"factor_graph_edges = {E}")
print(f"rank_cut_space = {rank_cut}")
print(f"beta_1 = {beta}")
print(f"cycle_words = {1<<beta}")
print(f"onehot_vectors = {3**M}")
print(f"occupied_gauge_sectors = {occupied}/{1<<beta}")
print("sector_occupancy_histogram = " + repr(dict(sorted(hist.items()))))
print(f"unsigned_onehot_count = {sector_onehot_counts[0]}")
print(f"signed_character_index = {q_signed}")
print(f"signed_onehot_count = {sector_onehot_counts[q_signed]}")
print(f"unsigned_solution_count_direct = {z_unsigned}")
print(f"signed_solution_count_direct = {z_signed}")
print(f"unsigned_solution_count_dual = {z_from_fourier(0)}")
print(f"signed_solution_count_dual = {z_from_fourier(q_signed)}")
print(f"sector_mean_F = {mean_F}")
print(f"sector_mean_F2 = {mean_F2}")
print(f"cycle_parseval_rhs = {cycle_l2}")
print(f"cycle_parseval_rhs_decimal = {float(cycle_l2):.16f}")
print(f"nonbacktracking_two_step_branching = {branch2}")
print(f"x_squared_branching = {instability}")
print("ALL_EXACT_CHECKS_PASS = True")
