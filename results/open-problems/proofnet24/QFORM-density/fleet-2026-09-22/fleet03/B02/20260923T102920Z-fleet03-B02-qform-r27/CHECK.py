import itertools
import math
import numpy as np

# Constant regression.
C0 = 5*math.e/2**(1/5)
C_eta = C0*4**(1/10)
C_live = C_eta*(1536/21)**(1/10)
C_hyb = 2**(11/18)*3**(7/6)*math.e**(5/6)
C_hyb_eta = C_hyb*4**(1/12)
C_hyb_live = C_hyb_eta*(1536/21)**(1/12)

print(f"C0={C0:.15f}")
print(f"C_eta={C_eta:.15f}")
print(f"C_live={C_live:.15f}")
print(f"C_hyb={C_hyb:.15f}")
print(f"C_hyb_eta={C_hyb_eta:.15f}")
print(f"C_hyb_live={C_hyb_live:.15f}")

# Finite sanity check of the eta=1/4 structural complement.
# This is not proof: the proof is the inclusion-exclusion/union argument in REPORT.md.
rng = np.random.default_rng(270923)
rows = list(itertools.combinations(range(6), 2))
cols = list(itertools.combinations(range(6), 2))
pairs = [(r, c) for r in rows for c in cols]
R0 = {0, 1}
C0set = {0, 1}
eta = 0.25
cases = 0
violations = 0
worst_max_anchor = 1.0

for _ in range(5000):
    base = rng.exponential(size=len(pairs))
    factors = np.array([
        (8.0 if not set(r).isdisjoint(R0) else 0.2)
        * (8.0 if not set(c).isdisjoint(C0set) else 0.2)
        for r, c in pairs
    ])
    w = base*factors
    w /= w.sum()

    delta_r = sum(w[z] for z, (r, c) in enumerate(pairs)
                  if set(r).isdisjoint(R0))
    delta_c = sum(w[z] for z, (r, c) in enumerate(pairs)
                  if set(c).isdisjoint(C0set))

    if delta_r < eta and delta_c < eta:
        cases += 1
        anchor_masses = []
        for rr in R0:
            for cc in C0set:
                anchor_masses.append(sum(
                    w[z] for z, (r, c) in enumerate(pairs)
                    if rr in r and cc in c
                ))
        max_anchor = max(anchor_masses)
        worst_max_anchor = min(worst_max_anchor, max_anchor)
        if max_anchor + 1e-12 < 1/8:
            violations += 1

print(f"concentrated_cases={cases}")
print(f"worst_observed_max_anchor={worst_max_anchor:.15f}")
print(f"violations={violations}")
print("STATUS=PASS" if violations == 0 else "STATUS=FAIL")
