"""All LTFs with nondecreasing integer weight vectors 1 <= w_1 <= ... <= w_n <= W (n = 3..7) and every threshold
between consecutive values of w.x: max H/I per n (compare with the best AND/OR chain), and the worst
value/bound ratios of the lemmas of Theorem B (P1, P2, Sigma, total)."""
import sys, math, itertools
import numpy as np
from ltf_core import linform, ltf_table, spectrum, HI
from check_rank import analyse
from chains import all_chains

for n, W in [(3, 6), (4, 6), (5, 6), (6, 6), (7, 5)]:
    best = (0, None); worst = {k: 0.0 for k in ["p1", "p2", "sig", "tot"]}
    seen = set(); cnt = 0
    for w in itertools.combinations_with_replacement(range(1, W + 1), n):
        w = np.array(w, float)
        v = np.unique(np.round(linform(w), 9))
        for th in 0.5 * (v[:-1] + v[1:]):
            f = ltf_table(w, th)
            key = f.tobytes()
            if key in seen:
                continue
            seen.add(key); cnt += 1
            r = analyse(w, th)
            if r is None:
                continue
            if r["ratio"] > best[0]:
                best = (r["ratio"], (w.tolist(), th))
            for k in worst:
                worst[k] = max(worst[k], r[k])
    P, H, I = all_chains(n)
    ch = max(H / I)
    print("n=%d W=%d distinct functions=%d  max H/I=%.8f at %s   best chain %.8f   worst lemma ratios %s" % (
        n, W, cnt, best[0], best[1], ch, {k: round(v, 4) for k, v in worst.items()}), flush=True)
