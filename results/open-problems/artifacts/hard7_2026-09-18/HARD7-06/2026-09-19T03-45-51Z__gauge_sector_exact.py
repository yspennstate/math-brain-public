#!/usr/bin/env python3
"""Exact finite core for HARD7-06 run 8.

Gauge-sector calculation for NAE literals on the factor graph of K_5^(3),
the complete 3-uniform hypergraph on five vertices.  K_5^(3) is a simple
6-regular 3-uniform hypergraph.

The script certifies:
  * the F_2 gauge-map rank and first Betti number;
  * the exact size/probability of the unsigned gauge sector;
  * an explicit odd cycle-flux signing;
  * zero-literal K_5^(3) is UNSAT, while that signed formula is SAT.

All finite claims use exhaustive enumeration / exact integer arithmetic.
"""

from fractions import Fraction
from itertools import combinations, product

V = tuple(range(5))
F = tuple(combinations(V, 3))
n = len(V)
m = len(F)
incidences = tuple((v, a) for a, edge in enumerate(F) for v in edge)
E = len(incidences)

degrees = tuple(sum(v in edge for edge in F) for v in V)
assert degrees == (6, 6, 6, 6, 6)
assert (n, m, E) == (5, 10, 30)

# Rows of the coboundary/gauge map delta:
# delta(a,b)_(v,A) = a_v + b_A mod 2.
rows = []
for v, a in incidences:
    rows.append((1 << v) | (1 << (n + a)))

def gf2_rank(bitrows, ncols):
    rows = list(bitrows)
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(rows))
                      if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank

rank = gf2_rank(rows, n + m)
c = 1  # K_5^(3) incidence factor graph is connected.
beta1 = E - rank

assert rank == n + m - c == 14
assert beta1 == E - n - m + c == 16

# Exhaustively enumerate every gauge parameter (a,b) and its literal vector.
orbit = set()
for mask in range(1 << (n + m)):
    ell = 0
    for i, (v, a) in enumerate(incidences):
        bit = ((mask >> v) & 1) ^ ((mask >> (n + a)) & 1)
        if bit:
            ell |= 1 << i
    orbit.add(ell)

gauge_parameter_count = 1 << (n + m)
orbit_size = len(orbit)
class_count = (1 << E) // orbit_size
unsigned_sector_probability = Fraction(orbit_size, 1 << E)

assert gauge_parameter_count == 32768
assert orbit_size == 1 << rank == 16384
assert class_count == 1 << beta1 == 65536
assert unsigned_sector_probability == Fraction(1, 65536)

# A concrete nontrivial signing: in each triple, negate the incidence of
# its smallest vertex and no other incidence.
lit = {}
for a, edge in enumerate(F):
    mn = min(edge)
    for v in edge:
        lit[(v, a)] = int(v == mn)

# Exhibit an odd 4-cycle flux:
# v=1 -- clause (0,1,2) -- v=2 -- clause (1,2,3) -- v=1.
a0 = F.index((0, 1, 2))
a1 = F.index((1, 2, 3))
cycle_flux = (lit[(1, a0)] ^ lit[(2, a0)] ^
              lit[(2, a1)] ^ lit[(1, a1)])
assert cycle_flux == 1

def solution_count(literals):
    count = 0
    for x in product((0, 1), repeat=n):
        ok = True
        for a, edge in enumerate(F):
            vals = tuple(x[v] ^ literals[(v, a)] for v in edge)
            if vals == (0, 0, 0) or vals == (1, 1, 1):
                ok = False
                break
        count += int(ok)
    return count

zero_lit = {ia: 0 for ia in incidences}
zero_count = solution_count(zero_lit)
signed_count = solution_count(lit)

assert zero_count == 0
assert signed_count == 6

# General d=6,k=3 regular incidence-factor-graph identity:
# |E|=6n and |F|=6n/3=2n, hence beta_1=|E|-|V|-|F|+c=3n+c.
for N in range(1, 25):
    for C in range(1, min(N, 4) + 1):
        assert 6*N - N - 2*N + C == 3*N + C

print("K5^(3): n =", n)
print("K5^(3): m =", m)
print("K5^(3): factor incidences E =", E)
print("vertex degrees =", degrees)
print("connected components c =", c)
print("GF2 gauge-map rank =", rank)
print("beta1 =", beta1)
print("gauge parameter count =", gauge_parameter_count)
print("distinct all-zero gauge-orbit elements =", orbit_size)
print("gauge classes =", class_count)
print("iid-literal probability of unsigned gauge sector =", unsigned_sector_probability)
print("explicit 4-cycle flux =", cycle_flux)
print("zero-literal NAE solution count =", zero_count)
print("signed NAE solution count =", signed_count)
print("general (d,k)=(6,3) identity: beta1 = 3*n + c")
print("ALL_EXACT_CHECKS_PASS = True")
