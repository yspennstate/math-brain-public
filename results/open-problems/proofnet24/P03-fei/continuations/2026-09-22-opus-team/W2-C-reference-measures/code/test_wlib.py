"""Sanity tests for wlib: tree DP vs brute force over all binary trees, identities on known functions."""
import itertools, math, sys
import numpy as np
import wlib as W

W.set_polite()
rng = np.random.default_rng(1)


def all_trees(items):
    items = list(items)
    if len(items) == 1:
        yield items[0]
        return
    first = items[0]
    rest = items[1:]
    # split rest into (A, B) with first in left part
    for r in range(0, len(rest)):
        for A in itertools.combinations(rest, r):
            B = [x for x in rest if x not in A]
            if not B:
                continue
            for tl in all_trees([first] + list(A)):
                for tr in all_trees(B):
                    yield (tl, tr)


def brute(p, n):
    z = W.empty_prob(p, n)
    best = None
    cnt = 0
    for t in all_trees(range(n)):
        c = W.tree_cost(z, t)
        cnt += 1
        if best is None or c < best[0]:
            best = (c, t)
    return best, cnt


maxdiff = 0.0
for n in (3, 4, 5):
    for trial in range(40 if n < 5 else 12):
        tt = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
        p = W.spectrum(tt)
        (cb, tb), cnt = brute(p, n)
        z = W.empty_prob(p, n)
        best, arg = W.tree_dp(z, n)
        d = abs(cb - best[(1 << n) - 1])
        maxdiff = max(maxdiff, d)
    print(f"n={n}: #binary trees={cnt}, max |brute - dp| so far = {maxdiff:.3e}")

# identities
for name, tt, n in [("bent m=2", W.fam_bent(2), 4), ("bent m=3", W.fam_bent(3), 6), ("AND5", W.fam_and(5), 5),
                    ("maj5", W.fam_majority(5), 5), ("recmaj d2", W.fam_recmaj(2), 9), ("tribes 2x3", W.fam_tribes(2, 3), 6)]:
    p = W.spectrum(tt)
    H = W.H_of(p); I = W.I_of(p, n)
    Ht, t = W.tree_markov_H(p, n)
    L = W.levelwise_product_cost(p, n)
    print(f"{name:12s} n={n:2d} H={H:.6f} I={I:.6f} H/I={H/I:.4f}  treeMarkov*={Ht:.6f} ({Ht/I:.4f})  levelwise={L:.6f} ({L/I:.4f})  tree={t}")

# recmaj natural tree cost should equal ... check that the natural ternary tree gives exactly H (Markov along composition)
p = W.spectrum(W.fam_recmaj(2)); z = W.empty_prob(p, 9)
nat = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
print("recmaj d2 natural ternary tree cost + root bit =", W.h2(float(p[0])) + W.tree_cost(z, nat), " H =", W.H_of(p))
