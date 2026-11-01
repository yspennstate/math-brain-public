"""Recursive read-once systems and their limiting entropy/influence ratio.

A system is a list of symbols T_0..T_{r-1}. Symbol j is a gate G_j on k_j inputs; every input slot is wired to
  ('x',)          a fresh uniform variable            state (p, I, H) = (1/2, 1, 0)
  ('T', i, 'prev') a fresh copy of symbol i at the previous level
  ('T', i, 'cur')  a fresh copy of symbol i at the current level (an inner self-consistent limit, Hod's 'limit of limits')
All copies are on disjoint variables, so the level-(m+1) state follows from Hod's Lemma 3.1 (O'Donnell-Tan Prop 3.2)
with a vector bias:
    p_j  = Pr[G_j = true] with input i true w.p. p_in(i)
    I_j  = sum_i It_i[G_j] I+[in_i],     H_j = sum_i It_i[G_j] H+[in_i] + Ht[G_j]
where It_i, Ht are the biased spectral influence of coordinate i and the biased spectral entropy of G_j at the input
biases, I+ = I/V, H+ = (H - h(V))/V, V = 4p(1-p); a fresh variable has I+ = 1, H+ = 0.
Every level-m function is an explicit Boolean function, so every ratio H_m/I_m is a rigorous lower bound on the
FEI constant; the limit is what we report.

Validation targets (Hod 2017): the chain T = x OR (y AND T) converges to l<2/3> = (2/3, 4/3, 2 log2 3);
T <- NAND(T_prev, T_prev) from a variable gives 6.44539 and from l<2/3> gives 6.453111 (his afterthought);
F <- dual(AND(F_prev, F_cur)) from a variable gives beta(1/2) = 6.4547837 (his Theorem 4.4).
"""
import sys, math, itertools, random, time, json
import numpy as np
from math import log2

def h2(v):
    if v <= 0 or v >= 1:
        return 0.0
    return -v * log2(v) - (1 - v) * log2(1 - v)

FRESH = (0.5, 1.0, 0.0)
L23 = (2 / 3, 4 / 3, 2 * log2(3))

def tt_values(tt, k):
    """values in {+1 (false), -1 (true)}; index bit i = input i, bit 1 = true"""
    bits = (tt >> np.arange(1 << k)) & 1
    return 1 - 2 * bits

def biased_stats(vals, k, ps):
    """vals: +-1 array of length 2^k; ps: per-input true-probabilities. Returns (p_out, It per input, Ht)."""
    a = np.asarray(vals, dtype=float).reshape([2] * k)
    for j in range(k):
        p = ps[k - 1 - j]   # axis j of the C-order reshape is input k-1-j
        eta = 1.0 - 2.0 * p
        sig = math.sqrt(max(1e-300, 1.0 - eta * eta))
        M = np.array([[1.0 - p, p], [(1.0 - p) * (1.0 - eta) / sig, p * (-1.0 - eta) / sig]])
        a = np.tensordot(M, a, axes=([1], [j]))
        a = np.moveaxis(a, 0, j)
    coef = a.reshape(-1)
    pS = coef * coef
    nz = pS > 1e-18
    Ht = float(-(pS[nz] * np.log2(pS[nz])).sum())
    idx = np.arange(1 << k)
    It = np.array([float(pS[(idx >> i) & 1 == 1].sum()) for i in range(k)])
    p_out = (1.0 - coef[0]) / 2.0   # E[f] = coef[empty] = Pr[false] - Pr[true] = 1 - 2 p_out
    return p_out, It, Ht

def plus(state):
    p, I, H = state
    V = 4 * p * (1 - p)
    if V < 1e-12:
        return None
    return I / V, (H - h2(V)) / V

def evaluate(system, starts=None, levels=400, inner=200, tol=1e-11, trace=False):
    """system: list of (tt, k, wiring). Returns dict with ratio per symbol (limit), states, converged flag."""
    r = len(system)
    prev = [tuple(starts[j]) if starts else FRESH for j in range(r)]
    ratios_hist = []
    for m in range(levels):
        cur = list(prev)
        # inner loop for 'cur' references
        for it in range(inner):
            new = []
            for j, (tt, k, wiring) in enumerate(system):
                ins = []
                for w in wiring:
                    if w[0] == "x":
                        ins.append(FRESH)
                    elif w[2] == "prev":
                        ins.append(prev[w[1]])
                    else:
                        ins.append(cur[w[1]])
                ps = [s[0] for s in ins]
                p_out, It, Ht = biased_stats(tt_values(tt, k), k, ps)
                I = 0.0; H = Ht
                for s, iti in zip(ins, It):
                    pl = plus(s)
                    if pl is None:
                        return dict(ok=False, why="degenerate input")
                    I += iti * pl[0]; H += iti * pl[1]
                new.append((p_out, I, H))
            delta = max(abs(a[0] - b[0]) + abs(a[1] - b[1]) / (1 + abs(b[1])) + abs(a[2] - b[2]) / (1 + abs(b[2])) for a, b in zip(new, cur))
            cur = new
            if not any(w[0] == "T" and w[2] == "cur" for (_, _, wiring) in system for w in wiring):
                break
            if delta < tol:
                break
        else:
            return dict(ok=False, why="inner did not converge")
        prev = cur
        rat = [s[2] / s[1] if s[1] > 1e-300 else float("nan") for s in prev]
        ratios_hist.append(rat)
        if any(not math.isfinite(x) for x in rat) or any(s[1] > 1e250 for s in prev):
            break
        if m > 5 and max(abs(ratios_hist[-1][j] - ratios_hist[-2][j]) for j in range(r)) < tol:
            return dict(ok=True, ratio=rat, states=prev, levels=m + 1, hist=ratios_hist if trace else None)
    return dict(ok=True, ratio=ratios_hist[-1] if ratios_hist else [float("nan")] * r, states=prev, levels=levels, hist=ratios_hist if trace else None, note="not converged")

# gates: truth table conventions, index bit i = input i, value bit 1 = true
def gate_from_fn(fn, k):
    tt = 0
    for i in range(1 << k):
        x = [bool((i >> j) & 1) for j in range(k)]
        if fn(*x):
            tt |= 1 << i
    return tt

AND2 = gate_from_fn(lambda a, b: a and b, 2)
OR2 = gate_from_fn(lambda a, b: a or b, 2)
NAND2 = gate_from_fn(lambda a, b: not (a and b), 2)
CHAIN23 = gate_from_fn(lambda x, y, t: x or (y and t), 3)   # T = x OR (y AND T) -> l<2/3>
DUAL_AND2 = gate_from_fn(lambda a, b: not ((not a) and (not b)), 2)  # dual(AND)(a,b) = NOT(AND(NOT a, NOT b)) = OR(a,b)

def validate():
    ok = True
    res = evaluate([(CHAIN23, 3, [("x",), ("x",), ("T", 0, "prev")])])
    p, I, H = res["states"][0]
    print("chain x OR (y AND T): p %.6f I %.6f H %.6f  (2/3, 4/3, %.6f)" % (p, I, H, 2 * log2(3)))
    ok &= abs(p - 2 / 3) < 1e-8 and abs(I - 4 / 3) < 1e-8 and abs(H - 2 * log2(3)) < 1e-8
    res = evaluate([(NAND2, 2, [("T", 0, "prev"), ("T", 0, "prev")])])
    print("T <- NAND(T,T) from a variable: ratio %.6f (Hod 6.44539), levels %d" % (res["ratio"][0], res["levels"]))
    ok &= abs(res["ratio"][0] - 6.44539) < 2e-5
    res = evaluate([(NAND2, 2, [("T", 0, "prev"), ("T", 0, "prev")])], starts=[L23])
    print("T <- NAND(T,T) from l<2/3>: ratio %.6f (Hod 6.453111)" % res["ratio"][0])
    ok &= abs(res["ratio"][0] - 6.453111) < 2e-5
    # F_{m+1} = (F_m AND F_{m+1})^dual : dual(AND)(a,b) = OR(a,b) applied to duals of the inputs; the dual of a symbol
    # has the same (I, H) and measure 1-p, so emulate with explicit input negation: G(a,b) = OR(NOT a, NOT b) = NAND(a,b)
    # on the ORIGINAL inputs.  So F <- NAND(F_prev, F_cur).
    res = evaluate([(NAND2, 2, [("T", 0, "prev"), ("T", 0, "cur")])])
    print("F <- NAND(F_prev, F_cur) from a variable: ratio %.7f (Hod beta(1/2) = 6.4547837), levels %d" % (res["ratio"][0], res["levels"]))
    ok &= abs(res["ratio"][0] - 6.4547837) < 2e-6
    res = evaluate([(NAND2, 2, [("T", 0, "prev"), ("T", 0, "cur")])], starts=[L23])
    print("F <- NAND(F_prev, F_cur) from l<2/3>: ratio %.7f" % res["ratio"][0])
    return ok

def all_wirings(k, r, allow_cur=True):
    opts = [("x",)]
    for i in range(r):
        opts.append(("T", i, "prev"))
        if allow_cur:
            opts.append(("T", i, "cur"))
    return list(itertools.product(opts, repeat=k))

def nondegenerate(tt, k):
    v = tt_values(tt, k)
    if v.min() == v.max():
        return False
    idx = np.arange(1 << k)
    for i in range(k):  # every input must matter
        if np.array_equal(v[(idx >> i) & 1 == 0], v[(idx >> i) & 1 == 1]):
            return False
    return True

def search_r1(k, starts_list, top=8):
    best = []
    t0 = time.time(); n = 0
    for tt in range(1 << (1 << k)):
        if not nondegenerate(tt, k):
            continue
        for wiring in all_wirings(k, 1):
            if not any(w[0] == "T" for w in wiring):
                continue
            for sname, st in starts_list:
                res = evaluate([(tt, k, list(wiring))], starts=[st], levels=250, inner=120)
                n += 1
                if res.get("ok") and math.isfinite(res["ratio"][0]) and res["ratio"][0] < 100:
                    best.append((res["ratio"][0], tt, wiring, sname, res.get("note", "")))
    best.sort(key=lambda b: -b[0])
    print("r=1 k=%d: %d systems in %.0f s; top:" % (k, n, time.time() - t0))
    for b in best[:top]:
        print("   %.7f  tt=%d wiring=%s start=%s %s" % b)
    return best

if __name__ == "__main__":
    print("validation:", "OK" if validate() else "MISMATCH")
    starts = [("var", FRESH), ("l23", L23)]
    search_r1(2, starts)
    search_r1(3, starts, top=12)
