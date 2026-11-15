#!/usr/bin/env python3
"""Supplementary checks of the harmonic control and an explicit phase point."""
import json
import os
import resource
from fractions import Fraction
from pathlib import Path
from conserved_charges import exponents, local_column, modular_row_rank

assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
root = Path(__file__).resolve().parent
alphas = exponents(4, 6)
harmonic = [local_column(a, cubic=0) for a in alphas]
keys = sorted(set().union(*(c.keys() for c in harmonic)))
rows = [[c.get(k, 0) for c in harmonic] for k in keys]
assert modular_row_rank(rows, 1000003)["rank"] == 177
print("Independent modular harmonic check: rank=177, nullity=33")

# Differentiate J directly using the original vector field at one phase point.
n = 5
r = [1, 2, 0, 0, 0]
p = [3, -1, 4, 2, -2]
force = lambda x: x + x**3
dr = [p[i] - p[(i - 1) % n] for i in range(n)]
dp = [force(r[(i + 1) % n]) - force(r[i]) for i in range(n)]
dj = sum(dp[i] * (r[i] + r[(i + 1) % n])
         + p[i] * (dr[i] + dr[(i + 1) % n]) for i in range(n))
assert dj == 6
print("Direct quartic-current derivative at r=(1,2,0,0,0): +6")
a, b = 2, 3
assert b * Fraction(a, b) / a == 1
print("Scaling identity: b*s^2/a = 1 exactly for s^2=a/b")
data = json.loads((root / "charge_data.json").read_text())
assert len(data["row_monomials_interleaved_r_p"]) == len(data["sparse_matrix_rows"]) == 631
assert len(set(map(tuple, data["row_monomials_interleaved_r_p"]))) == 631
assert all(len(w) // 2 <= 3 and sum(w) <= 8 for w in data["row_monomials_interleaved_r_p"])
assert (root / "REPORT.md").read_text().splitlines()[0] == (
    "VERDICT: PROVED degree-six two-site polynomial charge classification for uniformly convex quartic chains")
assert not (root / "SOLVED_ELSEWHERE.md").exists()
print("Artifact consistency: PASS")
