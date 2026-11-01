"""Checks: count-splitting is exact for symmetric f (any tree) and for compositions along the composition tree."""
import numpy as np
import wlib as W
import countsplit as CS
W.set_polite()
rng = np.random.default_rng(3)
for name, tt, n, trees in [
    ("maj9", W.fam_majority(9), 9, {"balanced": CS.balanced_tree(range(9)), "caterpillar": CS.caterpillar(range(9)),
                                     "random-bal": CS.balanced_tree(list(rng.permutation(9)))}),
    ("recmaj d2", W.fam_recmaj(2), 9, {"natural ternary": CS.ternary_tree(2), "natural binarized": CS.binarize(CS.ternary_tree(2)),
                                        "balanced": CS.balanced_tree(range(9)), "caterpillar": CS.caterpillar(range(9))}),
    ("tribes 3x4", W.fam_tribes(3, 4), 12, {"tribe tree": CS.binarize(tuple(tuple(range(3*j, 3*j+3)) for j in range(4))),
                                             "balanced": CS.balanced_tree(range(12))}),
]:
    p = W.spectrum(tt); H = W.H_of(p); I = W.I_of(p, n)
    print(f"{name}: H={H:.6f} I={I:.6f} H/I={H/I:.4f}")
    for tn, t in trees.items():
        cs = CS.cs_cost(p, n, t)
        hit = CS.cs_cost(p, n, t, truncate=True)
        tm, _ = W.tree_markov_H(p, n, t) if all(len(x) == 2 for x in [t] if isinstance(x, tuple)) else (float('nan'), None)
        print(f"   {tn:18s} countsplit={cs:.6f} ({cs/I:.4f})  hit-only={hit:.6f} ({hit/I:.4f})  tree_markov_H check={tm:.6f}")
