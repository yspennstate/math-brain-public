import itertools
import math
import numpy as np
from scipy.optimize import linprog

# Deterministic regression only; the proof is symbolic in REPORT.md.
rng = np.random.default_rng(2026092311)

BASE = 5 * math.e / (2 ** (1 / 5))
HALL4 = BASE * (4 ** (1 / 10))
LIVE_HALL = HALL4 * ((96 / 7) ** (1 / 10))
LIVE_EVENT_32 = BASE * (32 ** (1 / 10)) * ((96 / 7) ** (1 / 10))

print(f"base={BASE:.15f}")
print(f"hall_log4={HALL4:.15f}")
print(f"live_hall={LIVE_HALL:.15f}")
print(f"live_event_eta_1_32={LIVE_EVENT_32:.15f}")
print(f"fixed_minor_ratio={21/512:.15f}")

# Check the weighted Hall characterization for a law mu on 2-subsets R
# and a law kappa on singleton K, with allowed transport edges K notin R.
def hall_ok(mu, pairs, kap, universe):
    for b, k in enumerate(universe):
        p_k = sum(mu[a] for a, R in enumerate(pairs) if k in R)
        if kap[b] > 1 - p_k + 1e-10:
            return False
    for b, k in enumerate(universe):
        for c in range(b + 1, len(universe)):
            l = universe[c]
            atom = sum(mu[a] for a, R in enumerate(pairs) if set(R) == {k, l})
            if kap[b] + kap[c] > 1 - atom + 1e-10:
                return False
    return True

def lp_feasible(mu, pairs, kap, universe):
    edges = [(a, b) for a, R in enumerate(pairs)
             for b, k in enumerate(universe) if k not in R]
    Aeq, beq = [], []
    for a in range(len(pairs)):
        Aeq.append([1.0 if aa == a else 0.0 for aa, bb in edges])
        beq.append(mu[a])
    for b in range(len(universe)):
        Aeq.append([1.0 if bb == b else 0.0 for aa, bb in edges])
        beq.append(kap[b])
    out = linprog(np.zeros(len(edges)), A_eq=np.asarray(Aeq),
                  b_eq=np.asarray(beq), bounds=[(0, None)] * len(edges),
                  method="highs")
    return out.success

mismatches = 0
for _ in range(500):
    U = list(range(5))
    pairs = list(itertools.combinations(U, 2))
    mu = rng.random(len(pairs)); mu /= mu.sum()
    kap = rng.random(len(U)); kap /= kap.sum()
    mismatches += hall_ok(mu, pairs, kap, U) != lp_feasible(mu, pairs, kap, U)

print(f"hall_lp_mismatches={mismatches}/500")
print("STATUS=PASS" if mismatches == 0 else "STATUS=FAIL")
