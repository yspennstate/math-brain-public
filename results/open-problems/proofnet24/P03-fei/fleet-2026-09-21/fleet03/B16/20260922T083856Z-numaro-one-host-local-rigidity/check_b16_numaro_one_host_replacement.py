#!/usr/bin/env python3
"""
Exact/fixed-point certificate for the fleet03/B16 one-host-pair deformation theorem.

Source family: the exact 18-input Numaro seed reconstructed by the fleet02/B16
composition-prime checker.  The 9-bit core has nine disjoint two-point hosts.
We replace exactly one host pair by ANY other pair of positive core cells,
disjoint from the eight retained host pairs.  The new pair need not be an edge.

All sign decisions use:
  * exact integer Walsh transforms,
  * exact integer influence numerators,
  * rigorous rational lower/upper bounds on log2(integer),
  * conservative 1e-7 fixed-point outward rounding.
Floating-point values are diagnostics only.
"""
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import math
import numpy as np

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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
N = 512
DEN = 1 << 18
SCALE = 10_000_000  # rigorous fixed-point log scale
C0 = Fraction(64548, 10000)  # 6.4548

def sha_table(table):
    return hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()

def reconstruct_source():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2
        assert not (seen & mask)
        seen |= mask
        hosts.append(tuple(x for x in range(N) if (mask >> x) & 1))
    core = [-1 if (base >> x) & 1 else 1 for x in range(N)]
    parent = []
    for y in range(N):
        row = core.copy()
        for j, cells in enumerate(hosts):
            if (y >> j) & 1:
                for x in cells:
                    row[x] = -1
        parent.extend(row)
    assert sha_table(parent) == EXPECTED_PARENT_SHA
    assert sum(core) == 18
    assert all(core[x] == 1 for e in hosts for x in e)
    assert len({x for e in hosts for x in e}) == 18
    return core, hosts

def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def ln_q_interval(num, den, terms=40):
    # q=num/den in [1,2); atanh expansion with rigorous positive tail.
    y = Fraction(num-den, num+den)
    s = Fraction(0)
    yp = y
    for r in range(terms):
        s += Fraction(2, 2*r+1) * yp
        yp *= y*y
    tail = Fraction(2) * yp / (Fraction(2*terms+1) * (1-y*y))
    return s, s + tail

LN2_LO, LN2_HI = ln_q_interval(2, 1)

def log2_interval_integer(t):
    assert 1 <= t <= 512
    if t == 1:
        return Fraction(0), Fraction(0)
    k = t.bit_length()-1
    qden = 1 << k
    lo, hi = ln_q_interval(t, qden)
    return Fraction(k) + lo/LN2_HI, Fraction(k) + hi/LN2_LO

def outward_log_tables():
    lo = np.zeros(513, dtype=np.int64)
    hi = np.zeros(513, dtype=np.int64)
    for t in range(1, 513):
        a, b = log2_interval_integer(t)
        lo[t] = (a.numerator*SCALE)//a.denominator
        hi[t] = (b.numerator*SCALE + b.denominator - 1)//b.denominator
        assert Fraction(int(lo[t]), SCALE) <= a <= b <= Fraction(int(hi[t]), SCALE)
    return lo, hi

LOG_LO, LOG_HI = outward_log_tables()
POPCOUNT = np.array([s.bit_count() for s in range(N)], dtype=np.int64)

# H[S,x] = chi_S(x), exact.
HAD = np.empty((N,N), dtype=np.int16)
for S in range(N):
    for x in range(N):
        HAD[S,x] = -1 if ((S & x).bit_count() & 1) else 1

def g_walsh(core, edges):
    zeros = {x for e in edges for x in e}
    assert len(zeros) == 18
    g = [0 if x in zeros else core[x] for x in range(N)]
    assert sum(g) == 0  # the full 18-bit function is balanced.
    return np.array(fwht_int(g), dtype=np.int16)

def bounds_batch(W, replacement_distances):
    """
    For 9-host functions, return:
      H_lo_num, H_hi_num over common denominator DEN*SCALE,
      I_num over denominator DEN.

    Eight retained source hosts are adjacent.
    A replacement host pair contributes entropy 1/16 exactly.
    Its influence is 5/256 when adjacent and 11/512 otherwise.
    """
    W = np.asarray(W, dtype=np.int64)
    sq = W*W
    aw = np.abs(W)
    # core spectral entropy
    Hhi_core = (sq*(18*SCALE - 2*LOG_LO[aw])).sum(axis=1, dtype=np.int64)
    Hlo_core = (sq*(18*SCALE - 2*LOG_HI[aw])).sum(axis=1, dtype=np.int64)
    # nine host terms: each contributes entropy 1/16
    host_H_num = 147456*SCALE  # (9/16)*DEN*SCALE
    Hlo = Hlo_core + host_H_num
    Hhi = Hhi_core + host_H_num

    Icore = (sq*POPCOUNT).sum(axis=1, dtype=np.int64)
    d = np.asarray(replacement_distances, dtype=np.int64)
    # 8 retained adjacent hosts give 80/512; replacement gives 10/512 if
    # adjacent, 11/512 otherwise. Convert /512 to /DEN by *512.
    host512 = np.where(d == 1, 90, 91).astype(np.int64)
    Inum = Icore + host512*512
    return Hlo, Hhi, Inum

def main():
    core, source_edges = reconstruct_source()
    assert all((a^b).bit_count() == 1 for a,b in source_edges)

    W0 = g_walsh(core, source_edges)
    H0lo, H0hi, I0num = bounds_batch(W0[None,:], np.array([1], dtype=np.int64))
    assert int(I0num[0]) * 128 == 261 * DEN  # I=261/128=2.0390625

    # Rigorous source ratio lower bound > 6.52184.
    src_num, src_den = 163046, 25000
    src_cmp = src_den*int(H0lo[0]) - src_num*SCALE*(int(I0num[0])-DEN)
    assert src_cmp > 0

    positive = [x for x,v in enumerate(core) if v == 1]
    source_sets = [set(e) for e in source_edges]
    W0i = W0.astype(np.int16)

    total = 0
    adjacent_replacements = 0
    nonadjacent_replacements = 0
    # Prove every replacement ratio < 6.48279.
    thr_num, thr_den = 648279, 100000
    min_positive_slack = None
    max_certified_upper = -1.0
    max_diag = None
    max_float = -1.0
    max_float_diag = None

    for j, old in enumerate(source_edges):
        occupied = set().union(*(source_sets[k] for k in range(9) if k != j))
        available = [x for x in positive if x not in occupied]
        pairs = [e for e in combinations(available,2) if e != old]
        oldvec = HAD[:,old[0]] + HAD[:,old[1]]

        for b0 in range(0, len(pairs), 1800):
            batch = pairs[b0:b0+1800]
            aa = np.array([a for a,b in batch], dtype=np.int64)
            bb = np.array([b for a,b in batch], dtype=np.int64)
            # Restoring the old pair and zeroing the new pair changes g-hat
            # by chi(old endpoints)-chi(new endpoints).
            W = (W0i[:,None] + oldvec[:,None] - HAD[:,aa] - HAD[:,bb]).T.astype(np.int64)
            distances = np.array([(a^b).bit_count() for a,b in batch], dtype=np.int64)
            Hlo, Hhi, Inum = bounds_batch(W, distances)

            # Avoid int64 overflow: these magnitudes stay below 1.9e18 at SCALE=1e7.
            lhs = thr_den * Hhi
            rhs = thr_num * SCALE * (Inum-DEN)
            assert int(lhs.max()) < (1<<63)-1
            assert int(rhs.max()) < (1<<63)-1
            slacks = rhs-lhs
            assert np.all(slacks > 0)

            idx = int(slacks.argmin())
            sval = int(slacks[idx])
            if min_positive_slack is None or sval < min_positive_slack:
                min_positive_slack = sval

            # Diagnostic certified-upper ratio (not used for a sign decision).
            rupper = (Hhi.astype(np.float64)/(DEN*SCALE))/((Inum-DEN).astype(np.float64)/DEN)
            im = int(rupper.argmax())
            if float(rupper[im]) > max_certified_upper:
                max_certified_upper = float(rupper[im])
                max_diag = {
                    "replaced_host_index": j,
                    "old_pair": list(old),
                    "new_pair": list(batch[im]),
                    "new_pair_hamming_distance": int(distances[im]),
                    "H_upper_over_Iminus1": float(rupper[im]),
                    "I_exact": f"{int(Inum[im])}/{DEN}",
                }

            # A separate ordinary-float diagnostic using midpoint-ish log values.
            sq = W*W
            aw = np.abs(W)
            Hfloat_core = np.zeros(len(batch), dtype=np.float64)
            for row in range(len(batch)):
                vals = aw[row]
                nz = vals > 0
                masses = (vals[nz].astype(np.float64)**2)/DEN
                Hfloat_core[row] = np.sum(masses*(18 - 2*np.log2(vals[nz].astype(np.float64))))
            Hfloat = Hfloat_core + 9/16
            Ifloat = Inum.astype(np.float64)/DEN
            rfloat = Hfloat/(Ifloat-1)
            imf = int(rfloat.argmax())
            if float(rfloat[imf]) > max_float:
                max_float = float(rfloat[imf])
                max_float_diag = {
                    "replaced_host_index": j,
                    "old_pair": list(old),
                    "new_pair": list(batch[imf]),
                    "new_pair_hamming_distance": int(distances[imf]),
                    "H": float(Hfloat[imf]),
                    "I": float(Ifloat[imf]),
                    "ratio": float(rfloat[imf]),
                }

            total += len(batch)
            adjacent_replacements += int(np.count_nonzero(distances == 1))
            nonadjacent_replacements += int(np.count_nonzero(distances != 1))

    assert total == 277875
    assert adjacent_replacements + nonadjacent_replacements == total

    # Consequences in the balanced uniform gate margin units:
    # c_G = 4(H/(I-1)-C0).
    replacement_c_upper = Fraction(4) * (Fraction(thr_num,thr_den)-C0)
    source_c_lower = Fraction(4) * (Fraction(src_num,src_den)-C0)
    gap_lower = Fraction(src_num,src_den)-Fraction(thr_num,thr_den)
    assert replacement_c_upper == Fraction(2799,25000)  # 0.11196
    assert source_c_lower == Fraction(838,3125)         # 0.26816

    out = {
        "status": "PASS",
        "source_parent_sha256": EXPECTED_PARENT_SHA,
        "source_hosts": [list(e) for e in source_edges],
        "positive_core_cells": len(positive),
        "family_definition": "replace exactly one of the nine source host pairs by any distinct pair of positive core cells disjoint from the other eight retained hosts",
        "replacements_checked": total,
        "adjacent_replacements": adjacent_replacements,
        "nonadjacent_replacements": nonadjacent_replacements,
        "source_ratio_rigorous_lower": f"{src_num}/{src_den}",
        "replacement_ratio_rigorous_upper": f"{thr_num}/{thr_den}",
        "certified_ratio_gap_lower": f"{gap_lower.numerator}/{gap_lower.denominator}",
        "replacement_base_margin_upper": f"{replacement_c_upper.numerator}/{replacement_c_upper.denominator}",
        "source_base_margin_lower": f"{source_c_lower.numerator}/{source_c_lower.denominator}",
        "max_certified_upper_diagnostic": max_certified_upper,
        "max_certified_upper_witness": max_diag,
        "max_plain_float_diagnostic": max_float,
        "max_plain_float_witness": max_float_diag,
        "min_integer_certificate_slack": min_positive_slack,
        "log_scale": SCALE,
        "log_interval_terms": 40,
        "full_FEI": "OPEN_NOT_PROVED"
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
