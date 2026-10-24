"""Cross-check of hc.evaluate (formula + maximum-matching grouping) against the independent audit checker
(audit/fei_audit.py: exact integer Walsh transform of the full table, arb entropy) on random cores with holes."""
import sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'audit'))
from hc import evaluate, groups_from_matching
import fei_audit


def full_table(c0, m, groups):
    k = len(groups)
    Nc = 1 << m
    T = np.empty((1 << k, Nc), dtype=np.int64)
    T[:] = c0
    yv = np.arange(1 << k)
    for j, g in enumerate(groups):
        col = np.where((yv >> j) & 1, -1, 1)
        for x in g:
            T[:, x] = col
    return T.reshape(-1)


if __name__ == '__main__':
    rng = np.random.default_rng(7)
    m = 7
    N = 1 << m
    for trial in range(6):
        while True:
            c0 = rng.choice([-1, 1], size=N).astype(np.int64)
            # holes: a few random cells plus a few random edges
            nh = int(rng.integers(3, 7))
            for _ in range(nh):
                x = int(rng.integers(N)); c0[x] = 0
                if rng.random() < 0.6:
                    c0[x ^ (1 << int(rng.integers(m)))] = 0
            # balance by flipping cells
            s = int(c0.sum())
            idx = np.where(c0 == (1 if s > 0 else -1))[0]
            rng.shuffle(idx)
            for x in idx[: abs(s) // 2]:
                c0[x] = -c0[x]
            if c0.sum() == 0:
                break
        groups = groups_from_matching(c0, m)
        if m + len(groups) > 20:
            continue
        ev = evaluate(c0, m)
        tab = full_table(c0, m, groups)
        p, I, H = fei_audit.table_quantities(tab)
        ok_I = abs(float(I) - ev['I']) < 1e-12
        ok_H = abs(float(H.mid()) - ev['H']) < 1e-9
        print(f"trial {trial}: n={m+len(groups)} holes={ev['holes']} pairs={ev['pairs']} singles={ev['singles']} "
              f"I formula {ev['I']:.12f} audit {float(I):.12f} ok={ok_I} | H formula {ev['H']:.12f} audit {float(H.mid()):.12f} ok={ok_H}")
