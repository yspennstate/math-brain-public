"""Numerical checks of the two general lemmas behind uniform FEI+:
 Lemma A: ghat(i)^2 log2(1/ghat(i)^2) <= (2/ln2) Var[d_i g]   for every coordinate i
 Lemma B: W log2(1/W) <= 10 J,  W = sum_{|S|>=2} P(S),  J = sum_{|S|>=2} |S| P(S)
and of the reduced read-k quantity  sum_{|S|>=2} P log2(1/Q1)  / J  for the term reference.
Families: all functions on n=3 (256), n=4 (65536), random functions, random biased functions,
near-dictators (x_1 flipped on random small sets), random read-k DNFs."""
import math, itertools, numpy as np
from feicore import spectrum, popcounts, polite
from readk_nonmono import random_nonmono
polite()
LN2 = math.log(2)

def lemmas(P, n, pc):
    W = float(P[pc >= 2].sum()); J = float((P * pc)[pc >= 2].sum())
    worstA = 0.0
    I = float((P * pc).sum())
    for i in range(n):
        a = float(P[1 << i]); inf_i = float(P[((np.arange(P.size) >> i) & 1) == 1].sum())
        v = inf_i - a
        if a > 1e-15:
            lhs = a * math.log2(1 / a)
            worstA = max(worstA, lhs / v if v > 1e-15 else (float('inf') if lhs > 1e-12 else 0.0))
    lb = W * math.log2(1 / W) if W > 1e-300 else 0.0
    rB = lb / J if J > 1e-300 else (0.0 if lb < 1e-12 else float('inf'))
    return worstA, rB, W, J

def run_tt(tts, n, label):
    pc = popcounts(n); wa = 0.0; wb = 0.0; arg = None
    for tt in tts:
        P = spectrum(tt)
        a, b, W, J = lemmas(P, n, pc)
        wa = max(wa, a)
        if b > wb: wb, arg = b, (round(W, 6), round(J, 6))
    print(f"{label:40s} max LemmaA ratio={wa:.4f} (bound {2/LN2:.4f})  max LemmaB ratio={wb:.4f} at (W,J)={arg}", flush=True)

rng = np.random.default_rng(5)
# all functions on 3 and 4 variables
for n in (3, 4):
    N = 1 << n
    tts = [np.array([1 - 2 * ((m >> x) & 1) for x in range(N)], dtype=np.int8) for m in range(1, (1 << N) - 1)]
    run_tt(tts, n, f"all nonconstant functions n={n}")
# random / biased functions
for n in (6, 8, 10):
    N = 1 << n
    for q in (0.5, 0.2, 0.05, 0.01):
        tts = [np.where(rng.random(N) < q, -1, 1).astype(np.int8) for _ in range(60)]
        tts = [t for t in tts if np.any(t == -1) and np.any(t == 1)]
        run_tt(tts, n, f"random n={n} Pr[-1]={q}")
# near-dictators: x_0 flipped on a random set of measure eta, and on subcubes
for n in (8, 10, 12):
    N = 1 << n; xs = np.arange(N)
    base = np.where(xs & 1, -1, 1).astype(np.int8)
    tts = []
    for eta in (0.001, 0.004, 0.01, 0.03, 0.08):
        for _ in range(10):
            flip = rng.random(N) < eta
            tts.append(np.where(flip, -base, base).astype(np.int8))
        for w in range(2, n):
            cube = ((xs >> 1) & ((1 << w) - 1)) == ((1 << w) - 1)
            tts.append(np.where(cube, -base, base).astype(np.int8))
    run_tt(tts, n, f"near-dictators n={n}")
# random read-k DNFs
for (n, k, w) in [(10, 2, 3), (12, 3, 4), (12, 4, 3), (14, 3, 5), (12, 6, 4)]:
    N = 1 << n; xs = np.arange(N, dtype=np.int64); tts = []
    for r in range(40):
        terms = random_nonmono(n, k, [w] * 30, rng, pneg=float(rng.choice([0.0, 0.5])))
        sat = np.zeros(N, dtype=bool)
        for (mm, v) in terms: sat |= (xs & mm) == v
        tts.append(np.where(sat, -1, 1).astype(np.int8))
    run_tt(tts, n, f"read-{k} DNF n={n} w={w}")
