#!/usr/bin/env python3
"""P13 binary-LCS width-6 DC/BC synchronizer certificate.

Model: two independent iid uniform binary source strings. Each source-pair
letter (u,v) is one of A=(0,1), B=(1,0), C=(0,0), D=(1,1), equiprobably.
The same v is used across an entire strip column, so the true dependence is
preserved. Floating sparse linear algebra is used only to propose an integer
Bellman supersolution; every hitting-time inequality claimed below is checked
exactly over integers.
"""
from fractions import Fraction
from itertools import product
import math

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

M = 12
Q = 10_000_000
ALPH = "ABCD"
UV = {"A": (0, 1), "B": (1, 0), "C": (0, 0), "D": (1, 1)}
COMP = str.maketrans({"A": "B", "B": "A", "C": "D", "D": "C"})
PREV = Fraction(2036624461477, 5_000_000)


def comp(word):
    return word.translate(COMP)


def minimal_reset_patterns(m):
    p = {"A" * m, "B" * m}

    # Previously proved one-defect family.
    for r in range(1, m):
        for z in "BCD":
            p.add("A" * r + z + "A" * (m - r))
        for z in "ACD":
            p.add("B" * r + z + "B" * (m - r))

    add = set()
    for r in range(1, m):
        for s in range(0, m - r):
            t = m - r - s
            if t < 1:
                continue
            for z1, z2 in product("BCD", repeat=2):
                # Previous two-defect theorem: first C or second D.
                good = (z1 == "C" or z2 == "D")
                # New theorem 1: D ... C for every internal placement.
                if (z1, z2) == ("D", "C"):
                    good = True
                # New theorem 2: B ... C once at least two leading A's
                # have created a long enough zero tail.
                if (z1, z2) == ("B", "C") and r >= 2:
                    good = True
                if good:
                    add.add("A" * r + z1 + "A" * s + z2 + "A" * t)

    p |= add
    p |= {comp(w) for w in add}

    # Keep only earliest reset words.
    return sorted({w for w in p if not any(v != w and v in w for v in p)})


def prefix_automaton(patterns):
    pref = {""}
    for w in patterns:
        for k in range(1, len(w) + 1):
            pref.add(w[:k])
    pat = set(patterns)
    lens = sorted({len(w) for w in patterns})
    states = sorted(pref - pat, key=lambda s: (len(s), s))
    idx = {s: i for i, s in enumerate(states)}
    maxlen = max(map(len, states))
    trans = {}
    for s in states:
        for a in ALPH:
            z = s + a
            if any(len(z) >= L and z[-L:] in pat for L in lens):
                trans[(s, a)] = None
                continue
            for k in range(min(len(z), maxlen), -1, -1):
                u = z[-k:] if k else ""
                if u in idx:
                    trans[(s, a)] = u
                    break
    return states, idx, trans


def rational_super_solution(states, idx, trans):
    n = len(states)
    rows, cols, data = [], [], []
    rhs = np.ones(n)
    for i, s in enumerate(states):
        rows.append(i); cols.append(i); data.append(1.0)
        for a in ALPH:
            z = trans[(s, a)]
            if z is not None:
                rows.append(i); cols.append(idx[z]); data.append(-0.25)
    A = sp.csr_matrix((data, (rows, cols)), shape=(n, n))
    approx = spla.spsolve(A, rhs)

    # Candidate generation only. Exact verification follows.
    H = [int(math.ceil((Q + 3) * float(x))) for x in approx]
    min_res = None
    for i, s in enumerate(states):
        # Exact Bellman supersolution inequality
        # H(s)/Q >= 1 + (1/4) sum H(next)/Q,
        # with H=0 on absorbing transitions.
        res = 4 * H[i] - 4 * Q
        for a in ALPH:
            z = trans[(s, a)]
            if z is not None:
                res -= H[idx[z]]
        assert res >= 0
        min_res = res if min_res is None else min(min_res, res)
    return H, min_res


def step(state, a):
    x, g = state
    u, v = UV[a]
    m = len(x)
    d = [0] * (m + 1)
    for i in range(1, m + 1):
        d[i] = (1 - g[i - 1]) * int(bool(d[i - 1] or x[i - 1] == v))
    xp = x[1:] + (u,)
    gp = [g[i + 1] + d[i + 2] - d[i + 1] for i in range(m - 1)]
    gp.append((1 - d[m]) * int(u == v))
    assert all(z in (0, 1) for z in gp)
    return xp, tuple(gp)


def apply(state, word):
    for a in word:
        state = step(state, a)
    return state


def sync(m, word):
    out = None
    for bits in product((0, 1), repeat=2 * m):
        s = (tuple(bits[:m]), tuple(bits[m:]))
        z = apply(s, word)
        if out is None:
            out = z
        elif z != out:
            return False
    return True


def finite_sanity():
    # Exhaustively verify the two new analytic families and complements
    # on every formal state through m=6.
    dc_count = 0
    bc_count = 0
    for m in range(2, 7):
        for r in range(1, m):
            for s in range(0, m - r):
                t = m - r - s
                if t < 1:
                    continue
                wdc = "A" * r + "D" + "A" * s + "C" + "A" * t
                assert sync(m, wdc)
                assert sync(m, comp(wdc))
                dc_count += 2
                if r >= 2:
                    wbc = "A" * r + "B" + "A" * s + "C" + "A" * t
                    assert sync(m, wbc)
                    assert sync(m, comp(wbc))
                    bc_count += 2

    # The r>=2 condition is substantive, not cosmetic.
    bad = "ABACA"  # m=3, r=s=t=1
    s0 = ((0, 0, 0), (0, 0, 0))
    s1 = ((0, 0, 0), (0, 0, 1))
    o0, o1 = apply(s0, bad), apply(s1, bad)
    assert o0 == ((0, 0, 0), (0, 0, 0))
    assert o1 == ((0, 0, 0), (1, 0, 0))
    assert o0 != o1
    return dc_count, bc_count, bad, o0, o1


def main():
    patterns = minimal_reset_patterns(M)
    states, idx, trans = prefix_automaton(patterns)
    assert len(patterns) == 970
    assert len(states) == 4291

    H, min_res = rational_super_solution(states, idx, trans)
    h0 = H[idx[""]]
    new = Fraction(h0, Q)
    assert min_res == 9
    assert h0 == 3281245172836
    assert new == Fraction(820311293209, 2500000)
    assert new < 328125
    assert new < PREV

    dc_count, bc_count, bad, o0, o1 = finite_sanity()

    print("model=true iid binary source pairs; shared Y-bit column dependence retained")
    print("m=12 w=6")
    print("minimal_reset_patterns=", len(patterns))
    print("nonabsorbing_prefix_states=", len(states))
    print("certificate_denominator_Q=", Q)
    print("minimum_exact_Bellman_residual_numerator=", min_res)
    print("H_empty=", h0)
    print("E_tau_upper=", new)
    print("E_tau_upper_decimal=", float(new))
    print("strict_simple_bound: E_tau < 328125")
    print("previous_constant=", PREV)
    print("previous_decimal=", float(PREV))
    print("improvement_exact=", PREV - new)
    print("improvement_decimal=", float(PREV - new))
    print("improvement_factor_previous_over_new=", float(PREV / new))
    print("fractional_reduction=", float((PREV - new) / PREV))
    print("new_DC_family_formal_state_checks=", dc_count)
    print("new_BC_r_ge_2_family_formal_state_checks=", bc_count)
    print("sharpness_counterexample_word=", bad)
    print("sharpness_output_s0=", o0)
    print("sharpness_output_s1=", o1)
    print("finite_synchronizer_sanity_m<=6=PASS")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
