"""Exact finite conditional-law checks and source checks; no simulation."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import os
import re
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
# macOS in this sandbox rejects lowering RLIMIT_DATA even from infinity.
# Enumeration is bounded by 3**6 samples and at most 36 allocations per sample;
# measured peak RSS is checked below. The CPU limit is accepted.
root = Path(__file__).resolve().parent
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# Joint enumeration includes nonuniform references, every full allocation,
# exposed eligibility indicators, frozen paths, and mutual collision tests.
prob = [tuple(F(w, 4 * i + 6) for w in (i + 1, i + 2, 2 * i + 3))
        for i in range(6)]
assert all(sum(row) == 1 for row in prob)
edges = ((0, 1), (0, 3), (1, 4), (2, 3), (2, 5), (3, 4))

def avoids(s):
    return all(not (s[i] == s[j] and s[i] != 0) for i, j in edges)

fibers = defaultdict(lambda: defaultdict(F))
allocations = 0
valid_samples = 0
for state in product(range(3), repeat=6):
    eligible = tuple(int(x > 0) for x in state)
    lists = [tuple(i for i in site if eligible[i])
             for site in (range(3), range(3, 6))]
    if min(map(len, lists)) < 2 or not avoids(state):
        continue
    valid_samples += 1
    w = F(1)
    for i, x in enumerate(state):
        w *= prob[i][x]
    n, m = map(len, lists)
    allocation_probability = F(1, n * (n - 1) * m * (m - 1))
    assert allocation_probability * n * (n - 1) * m * (m - 1) == 1
    for left in permutations(lists[0], 2):
        for right in permutations(lists[1], 2):
            alloc = left + right
            selected = (left[0], right[0])
            frozen = tuple((i, x) for i, x in enumerate(state)
                           if i not in selected)
            key = (eligible, alloc, frozen)
            fibers[key][tuple(state[i] for i in selected)] += (
                w * allocation_probability)
            allocations += 1

pair_checks = frozen_checks = 0
for (eligible, alloc, frozen), joint in fibers.items():
    selected = (alloc[0], alloc[2])
    fixed = dict(frozen)
    a = {}
    own = {}
    for i in selected:
        own[i] = {}
        for x in (1, 2):
            collision = any(
                j in fixed and x == fixed[j] and x != 0
                for edge in edges if i in edge
                for j in edge if j != i)
            own[i][x] = F(0) if collision else prob[i][x]
            frozen_checks += int(collision)
        a[i] = sum(own[i].values())
        assert a[i] > 0
    conditioned_product = {}
    for retained in product((1, 2), repeat=2):
        full = dict(fixed)
        full.update(zip(selected, retained))
        assert tuple(int(full[i] > 0) for i in range(6)) == eligible
        w = F(1)
        for i, x in zip(selected, retained):
            w *= own[i][x] / a[i]
        if not avoids(full):
            w = F(0)
            pair_checks += 1
        if w:
            conditioned_product[retained] = w
    Z = sum(conditioned_product.values())
    total = sum(joint.values())
    assert 0 < Z <= 1 and total > 0
    lhs = {state: w / total for state, w in joint.items()}
    rhs = {state: w / Z for state, w in conditioned_product.items()}
    assert lhs == rhs, (eligible, alloc, frozen, lhs, rhs)
assert pair_checks > 0 and frozen_checks > 0
print(f'PASS: exact conditional law on {len(fibers)} positive exposed fibers; '
      f'{valid_samples} path samples and {allocations} joint allocation records')

# An extra full-sample condition, or path-dependent selection, changes the law.
fair = {(a, b): F(1, 4) for a, b in product((0, 1), repeat=2)}
certified = {s: w for s, w in fair.items() if any(s)}
total = sum(certified.values())
certified = {s: w / total for s, w in certified.items()}
assert set(certified.values()) == {F(1, 3)} and certified != fair
selection_bias = {1: F(1, 2) * F(2, 3), 2: F(1, 2) * F(1, 3)}
assert selection_bias[1] / sum(selection_bias.values()) == F(2, 3)
assert F(2, 3) != F(1, 2)
# Constant winding weight cancels exactly for arbitrary nonuniform masses.
masses, winding_weight = (F(2, 7), F(3, 11)), F(5, 13)
assert [winding_weight * x / (winding_weight * sum(masses))
        for x in masses] == [x / sum(masses) for x in masses]
assert 50 > 2 * 10 and 50 - 23 > 1
print('PASS: certificate and path-dependent-selection counterexamples; '
      'exact cancellation of constant winding weight; confinement margin')

def covariance(H, a, b):
    return 2 * (min(a, b) - a * b / H)

checks = 0
for H in (F(1), F(2), F(11, 3)):
    for s in (H / 7, H / 2, H * F(4, 5)):
        L = H - s
        for q, qp in ((L / 11, L / 3), (L / 2, L / 2), (L / 3, L)):
            b, bp = 1 - q / L, 1 - qp / L
            assert covariance(H, s, s + q) == b * covariance(H, s, s)
            residual = (covariance(H, s + q, s + qp)
                        - b * covariance(H, s, s + qp)
                        - bp * covariance(H, s + q, s)
                        + b * bp * covariance(H, s, s))
            assert residual == 2 * (min(q, qp) - q * qp / L)
            checks += 1
assert 3 * 12 + 6 * 4 == 60
assert -1 + 3 * F(1, 12) + F(1, 2) == -F(1, 4)
assert F(1, 2)**-3 == 8
assert 2 * 43**3 == 159014 and 41**3 < 43**3
print(f'PASS: {checks} rational prior-result covariance checks; '
      'midpoint Jacobian 8, exponent -1/4, prior anchor constant 159014')

dossier = (root / 'VERIFY.md').read_text()
for i in range(3):
    source = (root / 'sources' / f'introduction-current-{i}.tex').read_text()
    theorem = re.search(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', source)[0]
    assert dossier.count(theorem) == 1
    main = (root / 'sources' / f'main-current-{i}.tex').read_text()
    assert re.findall(r'\\author\{([^}]+)\}', main) == ['OpenAI']
source = (root / 'sources/groups-current.tex').read_text()
lemma = re.search(r'\\begin\{lemma\}\[Exact conditional law\][\s\S]*?\\end\{lemma\}', source)[0]
assert (root / 'PROOF.md').read_text().count(lemma) == 1
prefix = source.split(r'\label{lem:conditional-law}')[0]
assert len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|definition|remark)\}', prefix)) == 2
assert 'No certificate event is included' in source
assert 'probabilities of all\nallocations depend only on the recorded eligibility indicators' in source
assert 'without a positive-temperature assertion' in (root / 'sources/lean-267-current.md').read_text()
formal = (root / 'sources/HardSphere-current.lean').read_text()
statement = formal.split('theorem condensation_with_mixed :')[1]
assert 'IsGroundVector' in statement and 'GroundSupported' in statement
assert (root / 'REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
assert dossier.count('```') % 2 == 0
assert (root / 'PROOF.md').read_text().count('```') % 2 == 0
print('PASS: three exact theorem quotes and author lines; exact Lemma 7.2 quote; '
      'exposure restrictions, ground-state Lean scope and report format')

manifest = {}
for p in sorted((root / 'sources').glob('*current*')):
    if p.is_file():
        manifest[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
(root / 'sources/ROUND5_SHA256.json').write_text(json.dumps(manifest, indent=2) + '\n')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
assert rss_bytes < 1_000_000_000
print(f'PASS: inherited nice {os.getpriority(os.PRIO_PROCESS, 0)}, '
      f'OMP_NUM_THREADS=1, peak RSS {rss_bytes} bytes')
