"""Small exact-arithmetic and source audit for T136. No numerical SK simulation."""

import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import resource
import sys
import time
from fractions import Fraction as Q

started = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
# All allocations below are bounded finite lists (at most 16 spin vectors).
# macOS rejects changing RLIMIT_DATA here; check actual peak RSS below.
assert os.environ.get("OMP_NUM_THREADS") == "1"
root = Path(__file__).resolve().parent
previous = Path("~/codex_op_1114/briefs/AV_T136")
results = {}

# Compare quotations with fresh source environments, byte for byte.
verify = (root / "VERIFY.md").read_text()
fence = chr(96) * 3
blocks = re.findall(fence + r"tex\n(.*?)\n" + fence, verify, flags=re.S)
assert len(blocks) == 5
sources = [
    "limiting-law-introduction.tex",
    "limiting-law-introduction.tex",
    "limiting-law-introduction.tex",
    "scale-introduction.tex",
    "zero-temperature-main.tex",
]
for block, source in zip(blocks, sources):
    assert block in (root / "sources" / source).read_text(), source
results["verbatim_theorem_blocks"] = len(blocks)

# Recheck earlier scope evidence against fresh primary-source text.
earlier_names = {
    "limiting-law-introduction.tex": "candidate-1-01-introduction.tex",
    "scale-introduction.tex": "candidate-2-introduction.tex",
    "zero-temperature-main.tex": "candidate-3-main.tex",
    "limiting-law-reduction.tex": "law-reduction.txt",
    "limiting-law-foundations.tex": "candidate-1-02-foundations.tex",
    "EventuallyNatPos.lean": "conditional-lean.txt",
    "281.md": "zero-doc.txt",
}
same = {}
for fresh, earlier in earlier_names.items():
    a = (root / "sources" / fresh).read_text()
    b = (previous / "sources" / earlier).read_text()
    same[fresh] = a.rstrip("\n") == b.rstrip("\n")
results["fresh_vs_earlier_text_equal_ignoring_final_newlines"] = same

# beta^2 is factored out. Check every pair of Ising configurations.
cases = 0
for n in (2, 3, 4):
    spins = list(itertools.product((-1, 1), repeat=n))
    for sigma, tau in itertools.product(spins, repeat=2):
        products = [s * t for s, t in zip(sigma, tau)]
        pair_cov = Q(sum(products[i] * products[j]
                         for i in range(n) for j in range(i + 1, n)), n)
        overlap = Q(sum(products), n)
        overlap_cov = (n * overlap**2 - 1) / 2
        ordered_cov = Q(sum(products[i] * products[j]
                            for i in range(n) for j in range(n)), 2*n)
        assert pair_cov == overlap_cov
        assert pair_cov + Q(1, 2) == ordered_cov == n * overlap**2 / 2
        assert n * Q(1, 2*n) == Q(1, 2)
        cases += 1
results["exact_covariance_spin_pairs"] = cases
results["completion_variance_divided_by_beta_squared"] = "1/2"

# Recheck the earlier powers independently with Fraction arithmetic.
s, N, D = Q(1), Q(-6), Q(-1, 2)
stencil_order = 23
powers = {
    "sD": s + D,
    "sN2D_to_minus_r_minus_1": s + 2*N - (stencil_order + 1)*D,
    "sNx12": s + N + 12,
    "increment_x5_times_sN": 5 + s + N,
}
assert list(powers.values()) == [Q(1, 2), Q(1), Q(7), Q(0)]
results["x_powers_excluding_epsilon_and_increment_saving"] = {
    k: str(v) for k, v in powers.items()
}

# New tail constant: integral evaluation and independent simplification.
A = math.log(3) / 4
b = A / 2
via_integral = math.exp(2*b) * (1 + b / (2*(A-b)))
via_power = 1.5 * 3**0.25
assert math.isclose(via_integral, via_power, rel_tol=1e-14)
assert Q(1, 2) / (2*(1-Q(1, 2))) == Q(1, 2)
results["new_tail_constant"] = {
    "A": A, "b": b, "integral_evaluation": via_integral,
    "three_halves_times_three_to_one_quarter": via_power,
    "scaled_exponential_noise_variance": 4,
}

# Check the gauge normalization at rational couplings using spin weights.
max_error = 0.0
for n in (2, 3, 4):
    spins = list(itertools.product((-1, 1), repeat=n))
    edges = list(itertools.combinations(range(n), 2))
    couplings = [Q(2*k - len(edges), 7) for k in range(len(edges))]
    def linear(spin, gg):
        return sum(float(g)*spin[i]*spin[j] for (i, j), g in zip(edges, gg))
    weights = [math.exp(linear(spin, couplings)) for spin in spins]
    partition_average = sum(weights) / len(spins)
    identity = sum(w / partition_average for w in weights) / len(spins)
    max_error = max(max_error, abs(identity - 1))
    for eta in spins:
        transformed = [g*eta[i]*eta[j] for (i, j), g in zip(edges, couplings)]
        new_partition = sum(math.exp(linear(spin, transformed)) for spin in spins)
        assert math.isclose(new_partition, sum(weights), rel_tol=1e-14)
assert max_error < 1e-14
results["finite_gauge_normalization_max_float_error"] = max_error

# Confirm report format and reject accidental control escapes in documents.
assert (root / "REPORT.md").read_text().splitlines()[0].startswith("VERDICT: PROVED ")
for name in ("VERIFY.md", "PROOF.md", "REPORT.md", "LOG.md"):
    text = (root / name).read_text()
    assert not any(ord(c) < 32 and c not in "\n\t" for c in text), name
results["document_checks"] = "pass"
results["source_sha256"] = {
    p.name: hashlib.sha256(p.read_bytes()).hexdigest()
    for p in sorted((root / "sources").iterdir()) if p.is_file()
}
results["elapsed_seconds"] = time.monotonic() - started
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
results["peak_rss_bytes"] = rss if sys.platform == "darwin" else rss * 1024
assert results["peak_rss_bytes"] < 1024**3
assert results["elapsed_seconds"] < 60
output = json.dumps(results, indent=2, ensure_ascii=False)
(root / "audit.txt").write_text(output + "\n")
print(output)
