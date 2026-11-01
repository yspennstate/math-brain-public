#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction
from math import factorial

TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

base = int("".join(SLICES[0]), 16)
masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
pairs = []
seen = base
for m in masks:
    assert m.bit_count() == 2
    assert (seen & m) == 0
    seen |= m
    pts = tuple(x for x in range(512) if (m >> x) & 1)
    pairs.append(pts)

T = tuple(x for e in pairs for x in e)
assert len(T) == 18 and len(set(T)) == 18
assert base.bit_count() == 247
assert all(((base >> x) & 1) == 0 for x in T)

def hd(a,b):
    return (a ^ b).bit_count()

adj = {tuple(sorted((a,b))) for i,a in enumerate(T) for b in T[i+1:] if hd(a,b) == 1}
P0 = {tuple(sorted(e)) for e in pairs}
assert adj == P0
assert len(adj) == 9

# Directly verify the one-pair Fourier formulas for all C(18,2) source-cell pairs.
for i,a in enumerate(T):
    for b in T[i+1:]:
        d = a ^ b
        valid = [s for s in range(512) if (s & d).bit_count() % 2 == 0]
        assert len(valid) == 256
        mass = Fraction(len(valid), 1 << 16)
        assert mass == Fraction(1,256)
        influence = sum(Fraction(s.bit_count()+1, 1 << 16) for s in valid)
        if hd(a,b) == 1:
            assert influence == Fraction(5,256)
        else:
            assert influence == Fraction(11,512)

pair_entropy = Fraction(1,16)
pair_influence_adj = Fraction(5,256)
pair_influence_non = Fraction(11,512)
penalty = pair_influence_non - pair_influence_adj
assert penalty == Fraction(1,512)

perfect_matchings = factorial(18) // ((2**9) * factorial(9))
assert perfect_matchings == 34459425

# Certified entropy interval imported from the completed fleet01/B12 source artifact.
getcontext().prec = 80
Hlo = Decimal("6.776605309005978082519790221891882314787235038")
Hhi = Decimal("6.776605309005978082519790221891882314787235039")
Cstar = Decimal("6.5218512")

# For k nonadjacent pairs: I=261/128+k/512 and I-1=(532+k)/512.
R0lo = Decimal(128)*Hlo/Decimal(133)
R0hi = Decimal(128)*Hhi/Decimal(133)
gap = Cstar - R0hi
assert gap > 0

# A non-original perfect matching has at least two changed/nonadjacent edges:
# symmetric difference with P0 is a union of alternating even cycles, and P0
# contains every adjacency edge on T.
Ralt_hi = Decimal(512)*Hhi/Decimal(534)
assert Ralt_hi < R0lo

print("PASS")
print("special_cells =", T)
print("source_pairs =", pairs)
print("adjacency_edges_on_special_set =", len(adj))
print("unique_all_adjacent_matching = True")
print("perfect_matchings_closed_analytically =", perfect_matchings)
print("pair_entropy =", pair_entropy)
print("adjacent_pair_influence =", pair_influence_adj)
print("nonadjacent_pair_influence =", pair_influence_non)
print("influence_penalty_per_nonadjacent_pair =", penalty)
print("source_R_upper =", R0hi)
print("stable_center =", Cstar)
print("stable_center_gap =", gap)
print("best_nonoriginal_repairing_upper =", Ralt_hi)
print("full_FEI_status = OPEN_NOT_PROVED")
