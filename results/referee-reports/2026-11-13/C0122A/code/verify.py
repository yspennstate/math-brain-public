"""Audit source hashes, problem identification, and report parameter arithmetic.

No random sampling, numerical libraries, subprocesses, or worker threads.
"""
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "sources/manifest.json").read_text())
hashes = {}
for entry in manifest:
    if "text_sha256" in entry:
        actual = hashlib.sha256((root / "sources" / entry["file"]).read_bytes()).hexdigest()
        assert actual == entry["text_sha256"]
        hashes[entry["file"]] = actual

original = (root / "sources/chatterjee_0810.4221v2.txt").read_text()
resolution = (root / "sources/ding_eldan_zhai_1311.5592v2.txt").read_text()
assert 'Show that chaos implies multiple peaks even when the correlations' in original
assert 'thereby solving Open Problem 5 in [4]' in resolution
assert 'Theorem 1.2.' in resolution
assert 'http://arxiv.org/abs/0810.4221' in resolution

# Monomials use coordinates (a, sigma, m), with v = a sigma^2.
v = (F(1), F(2), F(0))
eps = (F(1, 8), F(2), F(0))
delta = (F(1, 8), F(0), F(1))
zeta = (F(1, 8), F(0), F(0))
exponent = tuple(2*eps[k] + delta[k] + zeta[k]
                 - (F(0), F(2), F(1))[k] - v[k] for k in range(3))
failure = tuple(v[k] - 2*delta[k] for k in range(3))
assert exponent == (F(-1, 2), F(0), F(0))
assert failure == (F(3, 4), F(2), F(-2))

numeric = []
for a, sigma, b in [(1e-2, 2.5, 3), (1e-6, .125, 10), (1e-12, 30, 100)]:
    m = b*sigma
    variance = a*sigma**2
    e, d, z = sigma**2*a**.125, m*a**.125, a**.125
    direct_exponent = e**2*d*z/(m*sigma**2*variance)
    direct_failure = variance/d**2
    assert math.isclose(direct_exponent, a**-.5, rel_tol=1e-12)
    assert math.isclose(direct_failure, a**.75/b**2, rel_tol=1e-12)
    numeric.append({"a": a, "sigma": sigma, "b": b,
                    "exponent_without_c": direct_exponent,
                    "failure_without_C_or_zeta": direct_failure})

assert (root / "REPORT.md").read_text().splitlines()[0] == "RESOLVED_IN_LITERATURE"
output = {"source_hashes_verified": hashes,
          "explicit_open_problem_identification_verified": True,
          "parameter_exponent_a_sigma_m": [str(x) for x in exponent],
          "failure_exponent_a_sigma_m": [str(x) for x in failure],
          "independent_numeric_substitutions": numeric,
          "nice_value": os.getpriority(os.PRIO_PROCESS, 0),
          "simulations_run": False,
          "reason_no_simulations": "User requested stopping upon a literature resolution."}
(root / "data").mkdir(exist_ok=True)
(root / "data/verification.json").write_text(json.dumps(output, indent=2) + "\n")
print("Source identity, hashes, exact exponents, and numeric substitutions verified.")
