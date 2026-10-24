"""Count-splitting cost of Numaro's g (n = 18) along the optimal hit-only tree, then leaf-swap local search."""
import time, json
import numpy as np
import wlib as W, countsplit as CS
W.set_polite()
rng = np.random.default_rng(29)
g = W.load_numaro(); n = 18
p = W.spectrum(g); H = W.H_of(p); I = W.I_of(p, n)
hit, t0 = W.tree_markov_H(p, n)
c0 = CS.cs_cost(p, n, t0)
print(f"g18: H={H:.6f} I={I:.6f} H/I={H/I:.5f}  HITopt={hit:.6f} ({hit/I:.5f})  CS(hit-opt tree)={c0:.6f} ({c0/I:.5f}) loss={c0-H:.5f} bits", flush=True)

def relabel(t, m):
    if isinstance(t, (int, np.integer)):
        return m[int(t)]
    return tuple(relabel(c, m) for c in t)

best_t, best_c = t0, c0
tstart = time.time()
it = 0
while time.time() - tstart < 240:
    it += 1
    i, j = rng.choice(n, size=2, replace=False)
    m = list(range(n)); m[i], m[j] = j, i
    t2 = relabel(best_t, m)
    c2 = CS.cs_cost(p, n, t2)
    if c2 < best_c - 1e-12:
        best_t, best_c = t2, c2
        print(f"  it {it}: CS={best_c:.6f} ({best_c/I:.5f}) loss={best_c-H:.5f} bits", flush=True)
print(f"final after {it} swaps: CS={best_c:.6f} CS/I={best_c/I:.5f} loss={best_c-H:.5f} bits ({(best_c-H)/I:.5f} I)")
print("tree:", best_t)
json.dump({"H": H, "I": I, "HITopt": hit, "CS_hit_tree": c0, "CS_best": best_c, "tree": str(best_t)}, open("../logs/g18_cs.json", "w"))
