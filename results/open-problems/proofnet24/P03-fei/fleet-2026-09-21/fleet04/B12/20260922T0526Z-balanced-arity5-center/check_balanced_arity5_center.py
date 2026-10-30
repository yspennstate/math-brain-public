#!/usr/bin/env python3
"""
Rigorous finite certificate for the balanced arity-five center.

The theorem certified is:

  For every balanced Boolean f : {0,1}^5 -> {-1,+1},
      H(f) <= 6 (I(f)-1).

Here H is Fourier-Shannon entropy in bits and I is total influence.

Proof split:
  (A) If the minimum Hamming distance d_* from f to a signed dictator is
      <= 10, cube automorphisms reduce to a fixed dictator.  Balance forces
      exactly d_*/2 flips in each dictator half.  We exhaust all such defect
      sets for d=2,4,6,8,10 and verify H <= 6(I-1) with a rigorous
      rational upper bound for every logarithm.

  (B) If d_* >= 12, every singleton Fourier coefficient has magnitude <=1/4.
      Balanced 5-bit Fourier coefficients are integer multiples of 1/8.
      Parseval therefore reduces the remaining claim to a 31-atom integer
      spectral relaxation.  A dynamic program checks this larger relaxation
      and in fact proves H <= (11/2)(I-1).

No Booleanity constraints are used in (B), so it is a genuine relaxation.
"""
from fractions import Fraction
import itertools
import math
import numpy as np

N = 32
SCALE = 10**12

def ln_bounds_integer(x: int, terms: int = 60):
    """Exact rational lower/upper bounds for ln(x), x positive integer."""
    if x <= 0:
        raise ValueError("x must be positive")
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    power = y
    s = Fraction(0, 1)
    for r in range(terms):
        s += Fraction(2, 2*r + 1) * power
        power *= y2
    # Positive atanh tail, using 1/(2r+1) <= 1/(2N+1).
    tail = Fraction(2, 2*terms + 1) * power / (1 - y2)
    return s, s + tail

LN2_LO, LN2_HI = ln_bounds_integer(2)

def log2_lower_integer(k: int):
    """Rigorous lower bound for log_2(k)."""
    if k in (1, 2, 4, 8):
        return Fraction({1:0, 2:1, 4:2, 8:3}[k], 1)
    lo, _ = ln_bounds_integer(k)
    return lo / LN2_HI

def ceil_scaled(fr: Fraction):
    num = fr.numerator * SCALE
    den = fr.denominator
    return (num + den - 1) // den

# For a balanced 5-bit Boolean function, every nonempty Fourier coefficient
# equals m/8 for an integer m.  If u=m^2, its entropy contribution is
# (u/64) log_2(64/u) = (u/64)(6 - 2 log_2 |m|).
# E_BY_M is a SAFE CEILING of this contribution times SCALE.
E_BY_M = [0]
for m in range(1, 9):
    u = m*m
    h_upper = Fraction(u, 64) * (Fraction(6, 1) - 2*log2_lower_integer(m))
    E_BY_M.append(ceil_scaled(h_upper))
E_LUT = np.array(E_BY_M, dtype=np.int64)

def walsh_matrix():
    W = np.empty((N, N), dtype=np.int16)
    for S in range(N):
        for x in range(N):
            W[S, x] = -1 if ((S & x).bit_count() & 1) else 1
    return W

W = walsh_matrix()
DEG = np.array([S.bit_count() for S in range(N)], dtype=np.int16)
COST_WEIGHT = DEG - 1

# Fixed dictator chi_{1}; coordinate 0 is its physical bit.
BASE = np.array([1 if ((x >> 0) & 1) == 0 else -1 for x in range(N)],
                dtype=np.int16)
POS = [x for x in range(N) if BASE[x] == 1]
NEG = [x for x in range(N) if BASE[x] == -1]
BASE_COEFF = (W @ BASE).astype(np.int16)

def sphere_certificate(d: int, batch_a: int):
    """Exhaust balanced defect sphere at distance d from BASE."""
    k = d // 2
    As = list(itertools.combinations(POS, k))
    Bs = list(itertools.combinations(NEG, k))

    # Flipping x changes the Walsh vector by -2 BASE[x] W[:,x].
    Avec = np.array(
        [-2*np.sum(W[:, A], axis=1) for A in As], dtype=np.int16
    )
    Bvec = np.array(
        [ 2*np.sum(W[:, B], axis=1) for B in Bs], dtype=np.int16
    )

    total = 0
    min_slack = None
    max_ratio_upper = 0.0

    for a0 in range(0, len(As), batch_a):
        coeff = (BASE_COEFF[None, None, :]
                 + Avec[a0:a0+batch_a, None, :]
                 + Bvec[None, :, :])

        if np.any(coeff[:, :, 0] != 0):
            raise AssertionError("balanced sphere produced nonzero mean")
        if np.any(coeff % 4):
            raise AssertionError("balanced coefficient not multiple of 4/32")

        m = np.abs(coeff) // 4
        if np.any(m > 8):
            raise AssertionError("Fourier coefficient exceeds Parseval range")
        u = m.astype(np.int64)**2

        # H <= hnum/SCALE, rigorously.
        hnum = E_LUT[m].sum(axis=2)

        # I-1 = cost/64 because p_S=u_S/64 and mean coefficient is zero.
        cost = (u * COST_WEIGHT[None, None, :]).sum(axis=2)
        if np.any(cost <= 0):
            raise AssertionError("non-dictator balanced defect has I<=1")

        # Exact integer comparison proving H <= 6(I-1).
        # hnum/SCALE <= 6 cost/64 iff 64 hnum <= 6 cost SCALE.
        slack = 6*cost*SCALE - 64*hnum
        if np.any(slack < 0):
            idx = np.argwhere(slack < 0)[0]
            raise AssertionError(
                f"sphere d={d} violation at local indices {tuple(idx)}"
            )
        local_min = int(slack.min())
        min_slack = local_min if min_slack is None else min(min_slack, local_min)

        ratio_upper = 64.0*hnum/(cost*SCALE)
        max_ratio_upper = max(max_ratio_upper, float(ratio_upper.max()))
        total += coeff.shape[0] * coeff.shape[1]

    expected = math.comb(16, k)**2
    if total != expected:
        raise AssertionError((d, total, expected))
    return total, min_slack, max_ratio_upper

def far_spectral_relaxation():
    """
    Certify d_* >= 12 branch.

    If every signed-dictator distance is >=12 then all five singleton Fourier
    coefficients have |hat f({i})| <= 1/4, hence singleton m_i^2 in {0,1,4}.
    For every other Fourier atom allow ANY square m^2 with m=0,...,8.
    Enforce only Parseval sum m_S^2=64 and maximize a rigorous entropy ceiling
    at each (total weight, influence-excess cost) state.
    """
    squares = [m*m for m in range(9)]
    singleton = [0, 1, 4]
    e_by_u = {m*m: E_BY_M[m] for m in range(9)}

    specs = []
    specs += [(1, singleton)] * 5
    specs += [(2, squares)] * 10
    specs += [(3, squares)] * 10
    specs += [(4, squares)] * 5
    specs += [(5, squares)] * 1

    # (Parseval weight, cost units) -> maximum safe entropy numerator
    dp = {(0, 0): 0}
    for deg, opts in specs:
        nxt = {}
        for (w, c), hnum in dp.items():
            for u in opts:
                nw = w + u
                if nw > 64:
                    continue
                nc = c + (deg - 1)*u
                nh = hnum + e_by_u[u]
                key = (nw, nc)
                if nh > nxt.get(key, -1):
                    nxt[key] = nh
        dp = nxt

    relevant = 0
    min_slack = None
    max_ratio_upper = 0.0
    for (w, cost), hnum in dp.items():
        if w != 64 or cost <= 0:
            continue
        relevant += 1
        # Prove H <= (11/2)(I-1):
        # hnum/SCALE <= 11 cost/128 iff 128 hnum <= 11 cost SCALE.
        slack = 11*cost*SCALE - 128*hnum
        if slack < 0:
            raise AssertionError(("far relaxation violation", w, cost, hnum))
        min_slack = slack if min_slack is None else min(min_slack, slack)
        max_ratio_upper = max(max_ratio_upper, 64.0*hnum/(cost*SCALE))

    if relevant == 0:
        raise AssertionError("no Parseval states in far relaxation")
    return len(dp), relevant, min_slack, max_ratio_upper

def main():
    sphere_specs = [(2, 64), (4, 64), (6, 64), (8, 32), (10, 8)]
    total = 0
    results = []
    for d, batch in sphere_specs:
        out = sphere_certificate(d, batch)
        total += out[0]
        results.append((d,) + out)

    dp_states, dp_relevant, dp_min_slack, dp_ratio = far_spectral_relaxation()

    print("PASS")
    print("theorem balanced_arity5_H_le_6_times_I_minus_1")
    for d, count, min_slack, ratio in results:
        print(
            f"sphere_d{d} count {count} "
            f"min_integer_slack {min_slack} "
            f"max_ratio_upper {ratio:.12f}"
        )
    print("sphere_total", total)
    print("far_relaxation_live_states", dp_states)
    print("far_relaxation_parseval_states", dp_relevant)
    print("far_relaxation_min_integer_slack", dp_min_slack)
    print("far_relaxation_max_ratio_upper", f"{dp_ratio:.12f}")
    print("far_relaxation_certified_ratio_bound", "11/2")
    print("entropy_scale", SCALE)

if __name__ == "__main__":
    main()
