import sys
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles/engine")
from tk_core import all_pairings
from exact_volume import pairing_volume_exact

k = 4
pms = list(all_pairings(2 * k))
exact = sum((F(pairing_volume_exact(pm, "T")) for pm in pms), F(0))
print("pairings", len(pms), "engine m8 =", exact, float(exact))

# independent Monte Carlo: slot forms W_l = x0 + sum_{s<l} sigma(s) t_{v(s)}
rng = np.random.default_rng(7)
Nsamp = 2_000_000
tot = 0.0
for pm in pms:
    pair_id, seen, rows = {}, set(), []
    for s in range(2 * k):
        a = min(s, pm[s])
        if a not in pair_id:
            pair_id[a] = len(pair_id)
    x0 = rng.random(Nsamp)
    t = rng.uniform(-1, 1, (Nsamp, k))
    W = x0.copy()
    ok = (W >= 0) & (W <= 1)
    opened = set()
    for s in range(2 * k):
        c = pair_id[min(s, pm[s])]
        sig = 1 if c not in opened else -1
        opened.add(c)
        W = W + sig * t[:, c]
        if s < 2 * k - 1:
            ok &= (W >= 0) & (W <= 1)
    tot += ok.mean() * 2 ** k
print("Monte Carlo m8 ~", round(tot, 3), " (908/15 =", round(908 / 15, 3), ", 1435/24 =", round(1435 / 24, 3), ")")
