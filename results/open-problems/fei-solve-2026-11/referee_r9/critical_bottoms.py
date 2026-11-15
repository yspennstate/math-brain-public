"""Near-critical M towers: (1) is the pinned limit independent of the bottom word? (2) which bottom words (depth <= 5 over
M, D, P, Pd, Q2) land their mean nearest M's fixed point, and what does word + M^k (+ a cap) reach in double precision?"""
import itertools, json
from scipy.optimize import brentq
from tower_recompute import PM, T, dual, G, compose, LEAF
gates = {"M": G(PM(3)), "D": G(dual(PM(3))), "P": G(PM(4)), "Pd": G(dual(PM(4))), "Q2": G(dual(T(2, 2)))}
caps = {"": None, "T26": G(T(2, 6)), "T35": G(T(3, 5)), "dT43": G(dual(T(4, 3)))}
M = gates["M"]
def phi(p):
    tot = 0.0
    for x in range(512):
        bits = [(x >> k) & 1 for k in range(9)]
        if any(all(bits[r * 3 + s[r]] for r in range(3)) for s in itertools.permutations(range(3))):
            tot += p ** sum(bits) * (1 - p) ** (9 - sum(bits))
    return tot
mfix = 1 - 2 * brentq(lambda p: phi(p) - p, 0.3, 0.95, xtol=1e-15)
def pinned(st, n=40):
    st = (mfix, mfix ** 2) + tuple(st[2:])
    for _ in range(n):
        st, r = compose(st, *M)
        st = (mfix, mfix ** 2) + tuple(st[2:])
    return r
print("pinned limit from LEAF", f"{pinned(LEAF):.10f}", flush=True)
for b in gates:
    st, _ = compose(LEAF, *gates[b])
    print(f"pinned limit from {b}: {pinned(st):.10f}", flush=True)
words = {}
def dfs(word, st, depth):
    if word:
        words[",".join(word)] = st
    if depth == 5:
        return
    for name, g in gates.items():
        try:
            nst, _ = compose(st, *g)
        except AssertionError:
            continue
        if abs(nst[0]) < 0.999:
            dfs(word + [name], nst, depth + 1)
dfs([], LEAF, 0)
ranked = sorted(words, key=lambda w: abs(words[w][0] - mfix))[:25]
best = (0, "")
rows = []
for w in ranked:
    st = words[w]
    peak = (0, "")
    for k in range(1, 40):
        try:
            st, r = compose(st, *M)
        except AssertionError:
            break
        if abs(st[0]) > 0.9999:
            break
        for c, g in caps.items():
            rr = r
            if g is not None:
                try:
                    _, rr = compose(st, *g)
                except AssertionError:
                    continue
            if rr > peak[0]:
                peak = (rr, f"{w},M^{k}" + (f",{c}" if c else ""))
    rows.append((abs(words[w][0] - mfix), peak[0], peak[1]))
    print(f"dev {abs(words[w][0]-mfix):.3e}  peak {peak[0]:.12f}  {peak[1]}", flush=True)
    best = max(best, peak)
json.dump({"mfix": mfix, "best": best, "rows": rows}, open("critical_bottoms.json", "w"), indent=1)
print("BEST", best)
