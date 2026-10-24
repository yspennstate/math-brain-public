"""Simulated annealing over integer-weight LTFs, aimed at one lemma at a time.

usage: python anneal_lemmas.py OBJ n steps seed
OBJ in {L3, L3tail, L4, L5, L6, T1, pw_c, pw_a, HI}
Weights are positive integers (sign flips of inputs do not change fhat^2);
theta is an integer, so exact ties w.x = theta (the sgn(0) convention) occur.
"""
import math, sys, time, json
import numpy as np
import ltf_ref as L

L.be_polite()
OBJ, n, steps, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rng = np.random.default_rng(seed)
WMAX = 4 * n


def score(w, t):
    tab = L.ltf_table(w, t)
    sp = L.Spec(tab)
    if sp.I < 1e-12:
        return -1.0, None
    absw = [abs(x) for x in w]
    if OBJ in ("pw_c", "pw_a"):
        r, U, N = L.ranks_and_U(absw)
        inf = sp.influences()
        best = 0.0
        arg = None
        for i in range(n):
            if inf[i] < 1e-15 or N[i] < 2:
                continue
            cs = sorted(set([c for c in [0.3, 0.6, 1.0, 1.5, 2.0, 3.0, N[i] / 3, N[i] / 2, N[i]] if 0 < c <= N[i]]))
            for (c, maxP, ra, rb, rc) in L.lemma2_pointwise(tab, absw, i, U[i], N[i], cs):
                v = rc if OBJ == "pw_c" else ra
                if v > best:
                    best, arg = v, (i, N[i], c, maxP)
        return best, arg
    out = L.lemma_checks(sp, absw)
    return float(out[OBJ]), out.get(OBJ + "_arg")


def propose(w, t):
    w = list(w)
    u = rng.random()
    j = int(rng.integers(n))
    if u < 0.3:
        w[j] = max(1, w[j] + int(rng.choice([-2, -1, 1, 2])))
    elif u < 0.45:
        w[j] = int(rng.integers(1, WMAX + 1))
    elif u < 0.55:
        k = int(rng.integers(n)); w[j] = w[k]            # create a tie
    elif u < 0.6:
        w = [2 * x + int(rng.integers(0, 2)) for x in w]  # near-ties
        t = 2 * t + int(rng.integers(-1, 2))
    elif u < 0.65:
        w = [max(1, x // 2) for x in w]; t = t // 2
    if rng.random() < 0.5:
        t = t + int(rng.choice([-3, -2, -1, 1, 2, 3]))
    S = sum(w)
    t = max(-S - 1, min(S + 1, t))
    return w, t


best_global = (-1, None, None, None)
t0 = time.time()
for restart in range(4):
    w = [int(x) for x in rng.integers(1, WMAX + 1, size=n)]
    t = int(rng.integers(-sum(w) // 2, sum(w) // 2 + 1))
    cur, arg = score(w, t)
    T = 0.05
    for s in range(steps):
        w2, t2 = propose(w, t)
        v, a2 = score(w2, t2)
        if v >= cur or rng.random() < math.exp((v - cur) / max(T, 1e-9)):
            w, t, cur, arg = w2, t2, v, a2
            if cur > best_global[0]:
                best_global = (cur, list(w), t, arg)
        T *= 0.999
    print(f"restart {restart}: cur={cur:.6f} best={best_global[0]:.6f}", flush=True)
print(f"OBJ={OBJ} n={n} steps={steps} seed={seed} time={time.time() - t0:.0f}s")
print(f"BEST {OBJ} = {best_global[0]:.9f}  w={best_global[1]} theta={best_global[2]} arg={best_global[3]}")
