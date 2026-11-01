#!/usr/bin/env python3
"""P13 binary-LCS width-6 two-defect synchronizer certificate.

Floating sparse linear algebra is used ONLY to propose a rational Bellman
super-solution. Every claimed hitting-time inequality is then checked exactly
over integers. The formal-state tests are sanity checks, not substitutes for
the general proofs in the report.
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
UV = {"A":(0,1), "B":(1,0), "C":(0,0), "D":(1,1)}
COMP = str.maketrans({"A":"B","B":"A","C":"D","D":"C"})

OLD_NUM = 365464514289599436188349306847299150185967435856
OLD_DEN = 142953501131693084676406151816850886136787

def comp(w):
    return w.translate(COMP)

def minimal_reset_patterns(m):
    p = {"A"*m, "B"*m}
    # Previously proved one-defect family.
    for r in range(1,m):
        for z in "BCD":
            p.add("A"*r + z + "A"*(m-r))
        for z in "ACD":
            p.add("B"*r + z + "B"*(m-r))

    # New two-defect family for A:
    # first defect C OR second defect D. Both defects are internal here;
    # edge placements already contain a shorter one-defect reset word.
    add = set()
    for i in range(1,m+1):
        for j in range(i+1,m+1):
            for z1,z2 in product("BCD", repeat=2):
                if z1 == "C" or z2 == "D":
                    w = ["A"]*(m+2)
                    w[i], w[j] = z1, z2
                    add.add("".join(w))
    p |= add
    p |= {comp(w) for w in add}

    # Keep the minimal language; hitting any longer word containing one of
    # these is already accounted for at the earlier end time.
    return sorted({w for w in p if not any(v != w and v in w for v in p)})

def prefix_automaton(patterns):
    pref = {""}
    for w in patterns:
        for k in range(1,len(w)+1):
            pref.add(w[:k])
    pat = set(patterns)
    lens = sorted({len(w) for w in patterns})
    states = sorted(pref-pat, key=lambda s:(len(s),s))
    idx = {s:i for i,s in enumerate(states)}
    maxlen = max(map(len,states))
    trans = {}
    for s in states:
        for a in ALPH:
            t = s+a
            if any(len(t) >= L and t[-L:] in pat for L in lens):
                trans[(s,a)] = None
                continue
            for k in range(min(len(t),maxlen),-1,-1):
                u = t[-k:] if k else ""
                if u in idx:
                    trans[(s,a)] = u
                    break
    return states,idx,trans

def rational_super_solution(states,idx,trans):
    n = len(states)
    rows,cols,data = [],[],[]
    b = np.ones(n)
    for i,s in enumerate(states):
        rows.append(i); cols.append(i); data.append(1.0)
        for a in ALPH:
            t = trans[(s,a)]
            if t is not None:
                rows.append(i); cols.append(idx[t]); data.append(-0.25)
    A = sp.csr_matrix((data,(rows,cols)),shape=(n,n))
    # Heuristic only: approximate exact expected hitting time.
    e = spla.spsolve(A,b)

    # Inflate by 1+3/Q, round upward, then verify exactly.
    H = [int(math.ceil((Q+3)*float(x))) for x in e]
    min_res = None
    for i,s in enumerate(states):
        # Exact form of h(s) >= 1 + (1/4) sum h(next),
        # with h=0 after absorption.
        r = 4*H[i] - 4*Q
        for a in ALPH:
            t = trans[(s,a)]
            if t is not None:
                r -= H[idx[t]]
        min_res = r if min_res is None else min(min_res,r)
        assert r >= 0
    return H, min_res

def step(state,a):
    x,g = state
    u,v = UV[a]
    m = len(x)
    d = [0]*(m+1)
    for i in range(1,m+1):
        d[i] = (1-g[i-1])*int(bool(d[i-1] or x[i-1] == v))
    xp = x[1:] + (u,)
    gp = [g[i+1] + d[i+2] - d[i+1] for i in range(m-1)]
    gp.append((1-d[m])*int(u == v))
    assert all(z in (0,1) for z in gp)
    return xp,tuple(gp)

def apply(state,w):
    for a in w:
        state = step(state,a)
    return state

def sync(m,w):
    out = None
    for bits in product((0,1),repeat=2*m):
        s = (tuple(bits[:m]),tuple(bits[m:]))
        t = apply(s,w)
        if out is None:
            out = t
        elif t != out:
            return False
    return True

def finite_sanity():
    # Exhaustive checks of both new analytic families and their complements
    # for small widths.
    for m in range(2,5):
        for r in range(m+1):
            for s in range(m-r+1):
                t = m-r-s
                for z in ALPH:
                    w1 = "A"*r + "C" + "A"*s + z + "A"*t
                    w2 = "A"*r + z + "A"*s + "D" + "A"*t
                    assert sync(m,w1)
                    assert sync(m,w2)
                    assert sync(m,comp(w1))
                    assert sync(m,comp(w2))

def main():
    patterns = minimal_reset_patterns(M)
    states,idx,trans = prefix_automaton(patterns)
    assert len(patterns) == 728
    assert len(states) == 3279

    H,min_res = rational_super_solution(states,idx,trans)
    h0 = H[idx[""]]
    new = Fraction(h0,Q)
    old = Fraction(OLD_NUM,OLD_DEN)

    assert min_res == 9
    assert h0 == 4073248922954
    assert new < 407325
    assert new < old
    assert 6*new < old

    finite_sanity()

    print("model=true iid binary source pairs; shared Y-bit column dependence retained")
    print("m=12 w=6")
    print("minimal_reset_patterns=",len(patterns))
    print("nonabsorbing_prefix_states=",len(states))
    print("certificate_denominator_Q=",Q)
    print("minimum_exact_Bellman_residual_numerator=",min_res)
    print("H_empty=",h0)
    print("E_tau_upper=H_empty/Q=",new)
    print("E_tau_upper_decimal=",float(new))
    print("strict_simple_bound: E_tau < 407325")
    print("previous_constant=",old)
    print("previous_decimal=",float(old))
    print("improvement_decimal=",float(old-new))
    print("improvement_factor_previous_over_new=",float(old/new))
    print("finite_synchronizer_sanity_m<=4=PASS")
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
