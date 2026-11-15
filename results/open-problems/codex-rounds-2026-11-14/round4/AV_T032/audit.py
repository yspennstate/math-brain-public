"""Elementary checks supporting a local lemma audit; no stochastic simulation."""
from fractions import Fraction as F
from pathlib import Path
from math import ceil, fsum, sqrt
import hashlib
import json
import os
import re
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
root = Path(__file__).resolve().parent
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

dossier = (root / 'VERIFY.md').read_text()
for i in range(3):
    source = (root / 'sources' / f'introduction-current-{i}.tex').read_text()
    theorem = re.search(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', source)[0]
    assert dossier.count(theorem) == 1
source = (root / 'sources/bridges-current.tex').read_text()
lemma = re.search(r'\\begin\{lemma\}\[A single replacement\][\s\S]*?\\end\{lemma\}', source)[0]
assert (root / 'PROOF.md').read_text().count(lemma) == 1
print('PASS: all three theorem quotations and Lemma 6.3 match current source exactly')

# Derive the conditional residual covariance from the whole bridge covariance.
def covariance(H, a, b):
    return 2 * (min(a, b) - a * b / H)

cases = 0
for H in (F(1), F(2), F(7, 3)):
    for frac in (F(1, 5), F(1, 2), F(3, 4)):
        s = H * frac
        L = H - s
        for q, qp in ((L / 20, L / 10), (L / 2, L / 2), (L / 3, L)):
            aq, ap = 1 - q / L, 1 - qp / L
            assert covariance(H, s, s + q) - aq * covariance(H, s, s) == 0
            residual = (covariance(H, s + q, s + qp)
                        - aq * covariance(H, s, s + qp)
                        - ap * covariance(H, s + q, s)
                        + aq * ap * covariance(H, s, s))
            assert residual == 2 * (min(q, qp) - q * qp / L)
            cases += 1
assert 3 * 12 + 6 * 4 == 60
assert 3 * 3 * 2**2 + 3 * 2 * 2**2 == 60
print(f'PASS: {cases} exact rational bridge covariance checks; fourth moment 60 by two expansions')

# Direct sums, with an integral upper bound on the omitted infinite tail.
# These checks corroborate the analytic summation proof; they do not replace it.
mesh_cases = 0
for ratio in (F(1, 2), F(2, 5), F(1, 4), F(1, 11), F(1, 101), F(1, 1000)):
    tau, h0 = float(ratio), 1.0
    n = ceil(F(1, 2) / ratio)
    stop = n + 20000
    partial = fsum((j * tau)**(-1.5) for j in range(n, stop))
    tail_upper = 2 * tau**(-1.5) / sqrt(stop - 1)
    assert partial + tail_upper <= 3 * sqrt(2) / (tau * sqrt(h0))
    assert partial + tail_upper <= 8 / (tau * sqrt(h0))
    mesh_cases += 1
assert F(1, 2)**(-3) == 8
assert 24 > 2 * (10 + 1 + sqrt(3) / 2)
assert 5 > 3 + 1 + sqrt(3) / 2
assert 50 - (13 + 10) > 1
assert F(-1) + 3 * F(1, 12) + F(1, 2) == -F(1, 4)
assert F(-1) + 3 * F(1, 12) + F(1, 2) - 1 == -F(5, 4)
print(f'PASS: {mesh_cases} independent mesh sums with tail bounds; Jacobian 8, drift 24, lift gap, exponent -1/4')

assert 41**3 < 43**3 == 79507
assert 2 * 43**3 == 159014
assert F(99, 100) * F(9, 10) == F(891, 1000)
assert F(98, 100) * F(9, 10) == F(441, 500)
assert 30 - 11 - 11 == 8
print('PASS: earlier insertion constants and normalization bounds independently reproduced')

slab = (root / 'sources/slab-current.tex').read_text()
prefix = slab.split(r'\label{def:regular}')[0]
assert len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|definition|remark)\}', prefix)) == 2
assert (root / 'REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
assert dossier.count('```') % 2 == 0
print('PASS: regularity is Definition 5.2; report and dossier formatting')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
assert rss_bytes < 1_000_000_000
print(f'PASS: one thread requested, inherited nice {os.getpriority(os.PRIO_PROCESS, 0)}, peak RSS {rss_bytes} bytes')

manifest = {}
for path in sorted((root / 'sources').glob('*current*')):
    manifest[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
# All writes stay in this task folder.
(root / 'sources/ROUND4_SHA256.json').write_text(json.dumps(manifest, indent=2) + '\n')
