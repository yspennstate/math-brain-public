#!/usr/bin/env python3
"""Rigorous local selector certificate around the source-valid n=18 shared-host gate.

For each of the nine source host-pairs, keep the other eight pairs fixed and
replace that pair by an arbitrary distinct pair of base-false core cells,
subject only to disjointness from the fixed sixteen cells.  This enumerates all
277875 nontrivial one-host support replacements.

Entropy is bounded above by exact rational atanh-series lower bounds for log2(r)
precomputed for every possible integer Fourier numerator r.  Influence is exact
integer arithmetic.  Candidates are grouped by their exact influence numerator;
only 13 influence levels occur, so the final comparison with C*=6.5218512 is
exact rational arithmetic.
"""
from fractions import Fraction
from itertools import combinations
import numpy as np

CSTAR = Fraction(4076157, 625000)  # 6.5218512 exactly
SCALE = 10**15
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
P0 = [(78,79),(113,121),(228,484),(170,186),(149,151),
      (338,466),(284,316),(291,295),(393,457)]


def ln_bounds(x, N=40):
    """Rational lower/upper bounds for ln(x), 1 <= x <= 2."""
    z = (x-1)/(x+1)
    s = Fraction(0,1)
    zp = z
    for k in range(N+1):
        s += 2*zp/Fraction(2*k+1,1)
        zp *= z*z
    tail = Fraction(0,1) if z == 0 else 2*zp/Fraction(2*N+3,1)/(1-z*z)
    return s, s+tail

LN2_LO, LN2_HI = ln_bounds(Fraction(2,1))


def log2_lower_integer(r):
    k = r.bit_length()-1
    m = Fraction(r, 1 << k)
    if m == 1:
        return Fraction(k,1)
    lo, _ = ln_bounds(m)
    return Fraction(k,1) + lo/LN2_HI


def entropy_upper_table():
    # coefficient = A/512, so p=A^2/2^18 and
    # -p log2 p = p (18 - 2 log2 |A|).
    out = [0]*513
    for r in range(1,513):
        p = Fraction(r*r, 1 << 18)
        term = p*(Fraction(18,1)-2*log2_lower_integer(r))
        q = term.numerator*SCALE
        out[r] = (q + term.denominator - 1)//term.denominator
    return np.array(out, dtype=np.int64)


def main():
    base = int(TOP+BOT, 16)
    core = np.array([1 if (base >> x) & 1 else 0 for x in range(512)], dtype=np.int64)
    f0 = np.where(core == 1, -1, 1).astype(np.int64)
    false_cells = [x for x in range(512) if core[x] == 0]
    assert len(false_cells) == 265
    assert all(core[x] == 0 for e in P0 for x in e)
    assert all((a^b).bit_count() == 1 for a,b in P0)

    chars = np.empty((512,512), dtype=np.int8)
    for s in range(512):
        chars[s] = [1 if ((s & x).bit_count() & 1) == 0 else -1 for x in range(512)]
    A0 = chars.astype(np.int64) @ f0
    wt = np.array([s.bit_count() for s in range(512)], dtype=np.int64)
    U = entropy_upper_table()

    original_support = set(x for e in P0 for x in e)
    level_max = {}
    maximizing_witness = {}
    alternatives = 0
    host_entropy_scaled = 9*SCALE//16  # every distinct two-point host block has H=1/16

    for j, old in enumerate(P0):
        remaining = original_support - set(old)
        A_fixed = A0 - chars[:, sorted(remaining)].sum(axis=1).astype(np.int64)
        allowed = [x for x in false_cells if x not in remaining]
        pairs = list(combinations(allowed, 2))

        for start in range(0, len(pairs), 4000):
            batch = pairs[start:start+4000]
            X = np.array(batch, dtype=np.int64)
            A = A_fixed[:,None] - chars[:,X[:,0]].astype(np.int64) - chars[:,X[:,1]].astype(np.int64)
            Hup = U[np.abs(A)].sum(axis=0) + host_entropy_scaled

            # Empty-host core influence plus eight fixed source edges and the replacement pair.
            Inum = (wt[:,None]*(A*A)).sum(axis=0)
            xor = np.bitwise_xor(X[:,0], X[:,1])
            adjacent = (xor & (xor-1)) == 0
            Inum = Inum + 8*5120 + np.where(adjacent, 5120, 5632)

            for t,(a,b) in enumerate(batch):
                if {a,b} == set(old):
                    continue
                alternatives += 1
                ii = int(Inum[t]); hh = int(Hup[t])
                if hh > level_max.get(ii, -1):
                    level_max[ii] = hh
                    maximizing_witness[ii] = (j,a,b)

    assert alternatives == 277875
    assert len(level_max) == 13

    # Exact rational upper ratio at every exact influence level.
    best = None
    for ii, hh in level_max.items():
        assert ii > (1 << 18)
        Rup = Fraction(hh, SCALE) * Fraction(1 << 18, ii-(1 << 18))
        assert Rup < CSTAR
        if best is None or Rup > best[0]:
            best = (Rup, ii, hh, maximizing_witness[ii])

    Rup, ii, hh, witness = best
    assert Rup == Fraction(1357333420684069, 209375000000000)
    assert CSTAR-Rup == Fraction(8179174315931, 209375000000000)
    assert ii == 536576

    print("PASS")
    print("alternatives_checked =", alternatives)
    print("exact_influence_levels =", len(level_max))
    print("max_nontrivial_ratio_upper =", float(Rup))
    print("max_nontrivial_ratio_upper_exact =", f"{Rup.numerator}/{Rup.denominator}")
    print("gap_to_Cstar_lower =", float(CSTAR-Rup))
    print("gap_to_Cstar_lower_exact =", f"{(CSTAR-Rup).numerator}/{(CSTAR-Rup).denominator}")
    print("maximizing_witness_replace_slot_pair =", witness)
    print("maximizing_influence_exact =", f"{ii}/{1<<18}")
    print("Cstar_exact =", f"{CSTAR.numerator}/{CSTAR.denominator}")


if __name__ == "__main__":
    main()
