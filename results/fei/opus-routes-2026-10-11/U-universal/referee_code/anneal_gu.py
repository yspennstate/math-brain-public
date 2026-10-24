"""Annealing stress test of CONJECTURE GU on compositions maj_k(h, ..., h): maximise G/I over inner tables h on m bits.
EVIDENCE only (float logs).  Time-boxed; single process."""
import json, math, sys, time
import numpy as np
from rec_fast import Gate, stats_sym
from rec import majk
from gu_values import g5

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 200.0
results = []


def score(gate, h):
    if abs(int(h.sum())) == h.size:
        return -1e9, None
    s = stats_sym(gate, h)
    if s is None:
        return -1e9, None
    return s['G_over_I'], s


for (k, m, start) in [(5, 5, 'g5'), (3, 6, 'random'), (5, 6, 'g5pad')]:
    gate = Gate(majk(k))
    if start == 'g5':
        h = g5.copy()
    elif start == 'g5pad':
        h = np.concatenate([g5, g5]).astype(np.int64)    # g5 with a dummy sixth bit
    else:
        h = rng.choice([-1, 1], size=1 << m).astype(np.int64)
    cur, cs = score(gate, h); best, bs, bh = cur, cs, h.copy()
    t0 = time.time(); T = 0.05; steps = 0
    while time.time() - t0 < BUDGET:
        h2 = h.copy()
        for _ in range(int(rng.integers(1, 3))):
            h2[int(rng.integers(h.size))] *= -1
        v, s = score(gate, h2)
        steps += 1
        if v > cur or rng.random() < math.exp((v - cur) / T):
            h, cur = h2, v
            if v > best:
                best, bs, bh = v, s, h2.copy()
        T = max(0.002, T * 0.9995)
    row = dict(outer=f'maj{k}', m=m, start=start, steps=steps, best_G_over_I=best, stats=bs, table=[int(x) for x in bh])
    results.append(row)
    print(json.dumps({kk: vv for kk, vv in row.items() if kk != 'table'}), flush=True)
with open(f'anneal_gu_results_{sys.argv[1] if len(sys.argv) > 1 else 7}.json', 'w', encoding='utf-8') as fh:
    json.dump(results, fh, indent=1)
