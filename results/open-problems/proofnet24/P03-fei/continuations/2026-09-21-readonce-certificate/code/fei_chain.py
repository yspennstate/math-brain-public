"""Exact O(n) calculator for AND/OR chains (lexicographic threshold functions)

    f = x1 op1 (x2 op2 (x3 op3 ( ... x_n ))),   op in {A, O},  +1 = true.

For f = x op g with g on the other variables (a = E[g] = ghat(empty)):
    AND: fhat(empty) = (a-1)/2, fhat({x}) = (1+a)/2, fhat(S) = fhat({x} u S) = ghat(S)/2  (S nonempty)
    OR : fhat(empty) = (a+1)/2, fhat({x}) = (1-a)/2, fhat(S) = ghat(S)/2, fhat({x} u S) = -ghat(S)/2
so every nonempty-set coefficient of g is halved and doubled in multiplicity, and (a, H, I) of f follow from
(a, H, I) of g alone:
    H(f) = phi(fhat(empty)^2) + phi(fhat({x})^2) + (H(g) - phi(a^2))/2 + (1 - a^2)
    I(f) = fhat({x})^2 + I(g)/2 + (1 - a^2)/4
with phi(p) = p log2(1/p). A constant tail c = +-1 is the state (c, 0, 0); a single variable is (0, 0, 1).

Restrictions of a chain are chains: fixing x_i to the absorbing value of op_i makes the tail from i a constant,
fixing it to the identity value deletes gate i. So the min-step and total-step statistics of the 09-20/21 work
(Delta_i H = H(f) - avg H(children)) cost O(n^2) per chain instead of 2^n.

Validated against brute force (fei_step_tribes.steps) for every pattern of length <= 9 and random ones to 12.
"""
import math, random, sys
from math import log2

def phi(p):
    return 0.0 if p <= 0.0 else -p * log2(p)

def state_var():
    return (0.0, 0.0, 1.0)

def state_const(c):
    return (float(c), 0.0, 0.0)

def gate(op, st):
    """f = x op g, with g's state st = (a, H, I)"""
    a, H, I = st
    if op == "A":
        a2 = (a - 1.0) / 2.0; w1 = ((1.0 + a) / 2.0) ** 2
    else:
        a2 = (a + 1.0) / 2.0; w1 = ((1.0 - a) / 2.0) ** 2
    H2 = phi(a2 * a2) + phi(w1) + (H - phi(a * a)) / 2.0 + (1.0 - a * a)
    I2 = w1 + I / 2.0 + (1.0 - a * a) / 4.0
    return (a2, H2, I2)

def chain_state(pattern, tail=None):
    """pattern: string over 'A'/'O' of the gates from the outside in; tail: None (a variable) or +-1 (constant)"""
    st = state_var() if tail is None else state_const(tail)
    for op in reversed(pattern):
        st = gate(op, st)
    return st

def ratio(pattern, tail=None):
    a, H, I = chain_state(pattern, tail)
    return H / I if I > 1e-15 else float("nan")

def chain_HI(pattern, tail=None):
    a, H, I = chain_state(pattern, tail)
    return H, I

def restriction_states(pattern):
    """for coordinate i (0-based; the last coordinate is the bare tail variable) return the two children states"""
    n = len(pattern) + 1
    out = []
    for i in range(n):
        if i == n - 1:  # the tail variable: children are the prefix chain with constant tails -1 and +1
            c0 = chain_state(pattern, tail=-1); c1 = chain_state(pattern, tail=+1)
        else:
            op = pattern[i]
            # absorbing value: AND & false -> tail constant false from gate i; OR & true -> constant true
            absorbing = chain_state(pattern[:i], tail=(-1 if op == "A" else +1))
            # identity value: gate i vanishes
            identity = chain_state(pattern[:i] + pattern[i + 1:], tail=None)
            c0, c1 = (absorbing, identity)
        out.append((c0, c1))
    return out

def influences(pattern):
    """Inf_i = P(children differ) = (1/4) E[(f0 - f1)^2] ... computed as weight of sets containing i:
    for chain coordinate i, Inf_i = P(all gates before i take their identity value) * P(gate i pivotal)."""
    n = len(pattern) + 1
    infs = []
    for i in range(n):
        c0, c1 = restriction_states(pattern)[i] if False else (None, None)
    # cheaper and exact: Inf_i = (1 - E[f0 f1]) / 2 needs cross terms; use the pivotality product instead
    p_alive = 1.0
    for i in range(n):
        if i == n - 1:
            infs.append(p_alive)  # the tail variable is pivotal whenever alive
        else:
            # gate i = x_i op_i T_{i+1}: pivotal iff T_{i+1} takes the identity value of op_i:
            #   AND: T = true, prob (1 + a_T)/2 ; OR: T = false, prob (1 - a_T)/2
            aT = chain_state(pattern[i + 1:])[0]
            piv = (1.0 + aT) / 2.0 if pattern[i] == "A" else (1.0 - aT) / 2.0
            infs.append(p_alive * piv)
            p_alive *= 0.5  # x_i must take its identity value for later gates to matter
    return infs

def steps(pattern):
    """returns (H/I, min-step, total-step, argmin coordinate, H, I)"""
    a, H, I = chain_state(pattern)
    infs = influences(pattern)
    kids = restriction_states(pattern)
    d = [H - (k0[1] + k1[1]) / 2.0 for (k0, k1) in kids]
    ratios = [d[i] / infs[i] if infs[i] > 1e-15 else float("inf") for i in range(len(d))]
    amin = min(range(len(ratios)), key=lambda i: ratios[i])
    return H / I, ratios[amin], sum(d) / I, amin, H, I

# ------------------------------------------------------------------ validation against brute force
def validate():
    import itertools, numpy as np
    sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
    from fei_step_tribes import steps as bf_steps
    from fei_lex import chain_tt
    worst = 0.0; count = 0
    pats = ["".join(p) for L in range(1, 9) for p in itertools.product("AO", repeat=L)]
    rng = random.Random(3)
    pats += ["".join(rng.choice("AO") for _ in range(L)) for L in (9, 10, 11) for _ in range(6)]
    for pat in pats:
        n = len(pat) + 1
        f = chain_tt(pat, n)
        rho0, tau, ratios, Hb, Ib = bf_steps(f, n)
        hi, r0, tt, amin, H, I = steps(pat)
        err = max(abs(H - Hb), abs(I - Ib), abs(r0 - rho0), abs(tt - tau))
        worst = max(worst, err); count += 1
    print("validation: %d patterns, worst abs error %.2e -> %s" % (count, worst, "OK" if worst < 1e-9 else "MISMATCH"))
    return worst < 1e-9

# ------------------------------------------------------------------ search
def anneal(n, objective, iters=20000, seed=0, init=None, T0=0.05):
    rng = random.Random(seed)
    pat = list(init) if init else [rng.choice("AO") for _ in range(n - 1)]
    cur = objective("".join(pat)); best = (cur, "".join(pat))
    for it in range(iters):
        T = T0 * (1 - it / iters) + 1e-4
        j = rng.randrange(n - 1)
        old = pat[j]; pat[j] = "O" if old == "A" else "A"
        if rng.random() < 0.15:  # occasionally flip a block
            k = rng.randrange(n - 1); pat[k] = "O" if pat[k] == "A" else "A"
        else:
            k = None
        val = objective("".join(pat))
        if val >= cur or rng.random() < math.exp((val - cur) / T):
            cur = val
            if val > best[0]:
                best = (val, "".join(pat))
        else:
            pat[j] = old
            if k is not None:
                pat[k] = "O" if pat[k] == "A" else "A"
    return best

if __name__ == "__main__":
    ok = validate()
    print("known patterns: AO chain %.4f, all-A %.4f, tribes-like (AAO)* %.4f  (n = 40)" % (ratio(("AO" * 40)[:39]), ratio("A" * 39), ratio(("AAO" * 40)[:39])))
    print("max H/I over chains by annealing (objective H/I):")
    for n in (12, 20, 30, 45, 60, 90):
        best = max((anneal(n, ratio, iters=6000 if n <= 30 else 12000, seed=s) for s in range(4)), key=lambda b: b[0])
        print("  n=%3d  H/I %.5f  pattern %s" % (n, best[0], best[1][:70] + ("..." if n > 71 else "")))
    print("max min-step over chains by annealing (objective min-step):")
    for n in (12, 20, 30, 45):
        obj = lambda p: steps(p)[1]
        best = max((anneal(n, obj, iters=3000, seed=s) for s in range(3)), key=lambda b: b[0])
        hi, r0, tt, amin, H, I = steps(best[1])
        print("  n=%3d  min-step %.5f  total-step %.5f  H/I %.4f  argmin %d  pattern %s" % (n, r0, tt, hi, amin, best[1][:60]))
