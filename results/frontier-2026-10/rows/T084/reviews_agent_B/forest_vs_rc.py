"""Subcritical comparison on K_n, adjacent pair: RC weight lam^|A| q^k = q^n (lam/q)^|A| q^cyc(A), so RC(q, lam) is the forest
measure at t = lam/q tilted by q^cyc. Prints 1 - Z Z_ef / Z_e^2 for RC and for forests at t (forest_kn.margin, exact tree counts)."""
import json
from mpmath import mpf, mp
from kn_gibbs import run
from forest_kn import margin
from mpmath import nstr
out = []
for n in (10, 20, 40):
    for q in ("0.5", "0.9"):
        for nl in ("0.1", "0.25", "0.5", "1", "1.5", "2"):
            lam = mpf(nl) / n; t = lam / mpf(q)
            rc = run(n, q, lam); fm = margin(n, t)
            out.append({"n": n, "q": float(q), "n_lambda": float(nl), "rc_margin": rc["one_minus_ratio"], "forest_margin_at_t": nstr(fm, 8),
                        "ratio": float(mpf(rc["one_minus_ratio"]) / fm)})
            print(json.dumps(out[-1]), flush=True)
json.dump(out, open("forest_vs_rc.json", "w"), indent=1)
