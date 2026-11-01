"""Attack T1-sharp:  H(F) <= H(p) + sum_k p_k [H(q_k) + H(G_k)]  for pairwise orthogonal leaves.
Moment analysis (NOTES 5.3) predicts a first-order violation for UNBALANCED two-cell partitions when leaf
G_2 has small coefficients aligned with G_1 on supp(G_1) and G_1 has small coefficients anti-aligned on supp(G_2).
Hill-climb over orthogonal leaf pairs (moves preserve E[G1 G2]=0) on a fixed unbalanced 2-cell partition.
"""
import sys
import numpy as np
from fei_lib import fwht_int, fwht_float, entropy_from_W, entropy_probs


def gap(lab, leaves, a, n):
    N = 1 << a
    m = len(leaves)
    B = np.array([leaves[lab[b]] for b in range(N)])
    F = B.T.reshape(-1)
    HF = entropy_from_W(fwht_int(F), a + n)
    p = np.array([np.mean(lab == k) for k in range(m)])
    tot = entropy_probs(p)
    for k in range(m):
        ak = (lab == k).astype(float)
        ah = fwht_float(ak) / N
        tot += p[k] * (entropy_probs(ah ** 2 / p[k]) + entropy_from_W(fwht_int(leaves[k]), n))
    return HF - tot


def climb(a, n, lab, rng, iters=4000):
    N = 1 << n
    # random orthogonal pair
    while True:
        g1 = rng.choice([-1, 1], size=N)
        g2 = rng.choice([-1, 1], size=N)
        if int(np.dot(g1, g2)) == 0:
            break
    best = gap(lab, [g1, g2], a, n)
    for it in range(iters):
        h1, h2 = g1.copy(), g2.copy()
        mv = rng.integers(3)
        if mv == 0:      # flip two points of g1 with opposite products to keep dot = 0
            prod = h1 * h2
            i = rng.choice(np.where(prod == 1)[0]) if np.any(prod == 1) else None
            j = rng.choice(np.where(prod == -1)[0]) if np.any(prod == -1) else None
            if i is None or j is None:
                continue
            h1[i] *= -1
            h1[j] *= -1
        elif mv == 1:
            prod = h1 * h2
            i = rng.choice(np.where(prod == 1)[0]) if np.any(prod == 1) else None
            j = rng.choice(np.where(prod == -1)[0]) if np.any(prod == -1) else None
            if i is None or j is None:
                continue
            h2[i] *= -1
            h2[j] *= -1
        else:            # flip one point in both (keeps product)
            i = rng.integers(N)
            h1[i] *= -1
            h2[i] *= -1
        assert int(np.dot(h1, h2)) == 0
        gnew = gap(lab, [h1, h2], a, n)
        if gnew >= best:
            best, g1, g2 = gnew, h1, h2
    return best, g1, g2


if __name__ == '__main__':
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
    results = []
    for (a, cell1) in [(2, [0]), (3, [0]), (3, [0, 1, 2]), (2, [0, 1, 3]), (3, [0, 3, 5, 6])]:
        lab = np.ones(1 << a, dtype=np.int64)
        lab[cell1] = 0
        for n in (3, 4):
            for rep in range(3):
                best, g1, g2 = climb(a, n, lab, rng, iters=3000)
                results.append((best, a, cell1, n, ''.join('1' if v < 0 else '0' for v in g1), ''.join('1' if v < 0 else '0' for v in g2)))
                print(a, cell1, n, rep, 'best gap', best, flush=True)
    results.sort(reverse=True)
    print('TOP', results[:3])
