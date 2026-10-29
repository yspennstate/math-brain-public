"""Section 13 constants under a wide slope gap: does lambda_1 have to grow with Delta? (agent J)"""
import json, random, lyapY_indep as L
rng = random.Random(4242); out = []
for Dl in (25.0, 100.0):
    for lam1 in (100, 10**4):
        wn, wo = L.run_cell(rng, 3, 1.0, Dl, 150, lam1=lam1, adversarial=True)
        row = dict(m=3, g2=1.0, Delta=Dl, lam1=lam1, max_rate_new=wn); out.append(row); print(json.dumps(row), flush=True)
json.dump(out, open("stress_delta.json", "w"), indent=1)
