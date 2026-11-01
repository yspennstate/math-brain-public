"""Small exact checks of the finite-box escape estimate. No simulation."""
import json
import time
from fractions import Fraction as F
from pathlib import Path

start = time.perf_counter()
kappa = F(1, 4)
checks = []
for r in range(1, 8):
    m = r + 1
    for law in ("symmetric", "inward", "right_biased"):
        def right(x):
            if law == "symmetric" or (law == "inward" and x == 0):
                return F(1, 2)
            if law == "right_biased" or x < 0:
                return 1 - kappa
            return kappa
        for initial in range(-r, r + 1):
            mass = {initial: F(1)}
            for t in range(1, 121):
                nxt = {}
                for x, probability in mass.items():
                    for y, p in ((x + 1, right(x)), (x - 1, 1 - right(x))):
                        if -r <= y <= r:
                            nxt[y] = nxt.get(y, F(0)) + probability * p
                mass = nxt
                survival = sum(mass.values(), F(0))
                bound = (1 - kappa ** m) ** (t // m)
                assert survival <= bound, (r, law, initial, t, survival, bound)
                checks.append(survival <= bound)
    assert time.perf_counter() - start < 60, "compute gate expired"
result = {"command":"python -B -X utf8 verify_range_clock.py", "exact_inequalities_checked":len(checks), "failed":0, "elapsed_seconds":round(time.perf_counter()-start,6), "radii":[1,7], "step_range":[1,120], "laws":["symmetric","inward","right_biased"], "limitation":"Finite exact instances support the escape inequality; written proof is in LEMMAS.md. This is not a proof of C0041 or a formal theorem receipt."}
Path(__file__).with_name("range_clock_checks.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
