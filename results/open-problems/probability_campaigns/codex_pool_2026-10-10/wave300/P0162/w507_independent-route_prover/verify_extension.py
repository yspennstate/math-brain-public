"""Only the arbitrary-phase/arbitrary-vertex extension, not core-lane repeats."""
import json
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from verify_obstruction import fresh_gate, entropy, walsh_raw, direct_influence, closed_form

root = Path(__file__).resolve().parent
gate = fresh_gate()
started = time.perf_counter()
m, n = 4, 16
base = [1 - 2 * ((((z >> 0) & 1) * ((z >> 1) & 1) + ((z >> 2) & 1) * ((z >> 3) & 1)) % 2) for z in range(n)]
entropies = []
sensitivities = set()
influences = set()
max_entropy_error = 0.0
best = None
reference = float(closed_form(m)["H"])
count = 0
for phase in range(1, n):
    for vertex in range(n):
        if time.perf_counter() - started > 30:
            raise RuntimeError("Extension verification time cap exceeded")
        g = [v * (1 - 2 * ((phase & z).bit_count() % 2)) for z, v in enumerate(base)]
        assert all(abs(x) == 4 for x in walsh_raw(g))
        h = list(g)
        h[vertex] *= -1
        f = g + h
        sensitivity = sum(g[vertex] != g[vertex ^ (1 << j)] for j in range(m))
        actual = sum((direct_influence(f, j) for j in range(m + 1)), Fraction())
        expected = Fraction(m, 2) + Fraction(m + 1 - 2 * sensitivity, n)
        assert actual == expected
        hf = entropy(f)
        error = abs(hf - reference)
        assert error < 2e-12
        max_entropy_error = max(max_entropy_error, error)
        sensitivities.add(sensitivity)
        influences.add(str(actual))
        ratio = hf / float(actual)
        if best is None or ratio > best["ratio"]:
            best = {"phase": phase, "vertex": vertex, "sensitivity": sensitivity,
                    "I": str(actual), "ratio": ratio}
        count += 1
assert sensitivities == set(range(m + 1))
assert best["sensitivity"] == m
parity_base = [v * (1 - 2 * (z.bit_count() % 2)) for z, v in enumerate(base)]
parity_h = list(parity_base)
parity_h[0] *= -1
parity_f = parity_base + parity_h
parity_i = sum((direct_influence(parity_f, j) for j in range(m + 1)), Fraction())
assert parity_i == Fraction(m, 2) - Fraction(m - 1, n)
assert abs(entropy(parity_f)/float(parity_i)-best["ratio"]) < 2e-12
extrema = []
with localcontext() as context:
    context.prec = 180
    for dimension in (4, 6, 8, 10, 16, 32, 64):
        values = closed_form(dimension)
        size = Decimal(1 << dimension)
        lower = Decimal(dimension)/2 - (dimension-1)/size
        upper = Decimal(dimension)/2 + (dimension+1)/size
        hf = Decimal(values["H"])
        extrema.append({"m": dimension, "minimum_I": str(lower), "maximum_I": str(upper),
                        "minimum_H_over_I": str(hf/upper), "maximum_H_over_I": str(hf/lower),
                        "evaluation": "proved entropy formula; no truth table at this dimension unless m=4"})
receipt = {"status": "PASS", "command": "python -X utf8 verify_extension.py", "compute_gate": gate,
           "elapsed_seconds": time.perf_counter()-started, "noncanonical_phase_vertex_cases": count,
           "local_sensitivities_attained": sorted(sensitivities), "global_influences_attained": sorted(influences),
           "maximum_entropy_invariance_error": max_entropy_error, "observed_class_extremizer_m4": best,
           "full_parity_twist_at_zero_attains_maximum": True, "closed_form_class_extrema": extrema,
           "scope": "L4-L5 extension; excludes phase-zero canonical truth tables already reproduced in another lane; no global FEI proof or agent audit."}
(root / "EXTENSION_MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key:receipt[key] for key in ("status","elapsed_seconds","noncanonical_phase_vertex_cases","local_sensitivities_attained","observed_class_extremizer_m4")}))
