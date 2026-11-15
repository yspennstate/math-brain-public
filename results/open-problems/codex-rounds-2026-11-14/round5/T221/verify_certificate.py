"""Independent, standard-library verification of the T221 finite certificate.

Joint laws are computed by inclusion-exclusion of conjunction events,
not by enumerating independent label assignments. No predecessor script
or numerical optimizer is imported. All output stays in this folder.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(180)
ROOT = Path(__file__).resolve().parent
TRIPLES = ((0, 1, 2), (1, 3, 4), (2, 5, 6))


def partitions(prefix=(0,)):
    if len(prefix) == 7:
        yield prefix
    else:
        for k in range(max(prefix)+2):
            yield from partitions(prefix+(k,))


def valid(pi):
    for images in ((1, 3, 5), (2, 4, 6)):
        forward, backward = {}, {}
        for j, image in enumerate(images):
            source, target = pi[j], pi[image]
            if source in forward and forward[source] != target:
                return False
            if target in backward and backward[target] != source:
                return False
            forward[source] = target
            backward[target] = source
    return True


def joint_law(pi, p):
    sets = ({pi[0]}, *({pi[i] for i in t} for t in TRIPLES))
    law = {}
    for bits in product((0, 1), repeat=4):
        positives = [sets[j] for j in range(4) if bits[j]]
        negatives = [sets[j] for j in range(4) if not bits[j]]
        mass = F(0)
        for selected in product((0, 1), repeat=len(negatives)):
            required = set().union(*positives, *(s for s, take in zip(negatives, selected) if take))
            mass += (-1)**sum(selected)*p**len(required)
        assert mass >= 0
        if mass:
            law[bits] = mass
    assert sum(law.values()) == 1
    return law


def cost_terms(pi, p):
    joint = joint_law(pi, p)
    ey, names = defaultdict(F), defaultdict(F)
    for (r, y0, ya, yb), mass in joint.items():
        ey[y0] += mass
        names[y0, ya, yb] += mass
    return [(F(1), list(ey.values())), (F(1), list(joint.values())),
            (F(-1), list(names.values()))]


def compare(terms, log_form):
    # Exact sign of sum c H(qs) - sum log_form[n] log n.
    powers = defaultdict(F)
    for c, qs in terms:
        for q in qs:
            if q:
                powers[q] -= c*q
    for n, c in log_form.items():
        powers[F(n)] -= c
    den = math.lcm(*(v.denominator for v in powers.values()))
    ratio = F(1)
    for q, exponent in powers.items():
        ratio *= q**int(exponent*den)
    return (ratio > 1)-(ratio < 1)


def canon(values):
    labels = {}
    return tuple(labels.setdefault(v, len(labels)) for v in values)


def dot(row, values):
    return sum(F(a)*b for a, b in zip(row, values))


def determinant(matrix):
    # Leibniz expansion is small (4! terms) and independent of elimination.
    from itertools import permutations
    out = 0
    for p in permutations(range(len(matrix))):
        inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))
        out += (-1)**inversions*math.prod(matrix[i][p[i]] for i in range(len(p)))
    return out


def main():
    started = time.monotonic()
    table = json.loads((ROOT/'stationarity_table.json').read_text())
    certificate = json.loads((ROOT/'stationarity_certificate.json').read_text())
    result = json.loads((ROOT/'stationarity_result.json').read_text())
    types = [tuple(row['type']) for row in table]
    assert types == sorted(pi for pi in partitions() if valid(pi))
    assert len(types) == len(certificate) == 103
    old = json.loads(Path('~/codex_op_1114r4/briefs/T221/collision_table.json').read_text())
    old = {(F(row['p_one']), tuple(row['partition'])): row['cost'] for row in old}
    maximum_difference = 0.0
    for p in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1)):
        for pi in types:
            terms = cost_terms(pi, p)
            value = -sum(float(c*q)*math.log(float(q)) for c, qs in terms for q in qs if q)
            maximum_difference = max(maximum_difference, abs(value-old[p, pi]))
            assert abs(value-old[p, pi]) < 2e-12
    A = {int(n): F(c) for n, c in result['dual_alpha'].items()}
    B = {int(n): F(c) for n, c in result['dual_beta'].items()}
    zeros = 0
    for row, cert in zip(table, certificate):
        pi = tuple(row['type'])
        assert pi == tuple(cert['type'])
        sigmas = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
        restrictions = [canon(pi[i] for i in triple) for triple in TRIPLES]
        expected_column = [1]+[int(restrictions[0] == sigma)-int(restrictions[g] == sigma)
                              for g in (1,2) for sigma in sigmas]
        assert row['stationarity_column'] == expected_column
        terms = cost_terms(pi, F(1, 2))
        form = {int(n): F(c) for n, c in row['cost_log_form'].items()}
        assert compare(terms, form) == 0
        slack = {int(n): F(c) for n, c in cert['slack_log_form'].items()}
        reconstructed = defaultdict(F, slack)
        reconstructed[2] += 1
        for n, c in A.items():
            reconstructed[n] += row['stationarity_column'][4]*c
        for n, c in B.items():
            reconstructed[n] += row['stationarity_column'][7]*c
        assert compare(terms, reconstructed) == 0
        # compare([], -slack) is exactly the sign of slack.
        exact = compare([], {n: -c for n, c in slack.items()})
        assert exact == cert['exact_slack_sign'] >= 0
        zeros += exact == 0

    # Independently verify every reported grouped minimum, not only the dual.
    grouped_pairs = set()
    for group in result['grouped_dual_check']:
        pair = tuple(group['column_pair'])
        grouped_pairs.add(pair)
        minimum_type = tuple(group['minimum_cost_type'])
        minimum_form = {int(n):F(c) for n,c in group['minimum_cost_log_form'].items()}
        assert compare(cost_terms(minimum_type,F(1,2)),minimum_form) == 0
        for row in table:
            if (row['stationarity_column'][4],row['stationarity_column'][7]) == pair:
                assert compare(cost_terms(tuple(row['type']),F(1,2)),minimum_form) >= 0
    assert grouped_pairs == {(row['stationarity_column'][4],row['stationarity_column'][7]) for row in table}
    assert 2**20*11**11 > 3**18*7**7
    assert 2**16*11**11 > 3**6*7**14
    assert 2**14*5**10 > 3**9*7**7

    # Exact attainable extrema, independent of the numerical LP output.
    assert compare(cost_terms((0,0,0,0,0,0,0),F(1,2)),{2:F(1)}) == 0
    assert compare(cost_terms((0,1,1,0,0,0,0),F(1,2)),{2:F(3,2)}) == 0

    # Rank <= 4 follows without elimination from four zero rows and two sums.
    columns = [row['stationarity_column'][1:] for row in table]
    assert all(all(c[j] == 0 for j in (0, 1, 5, 7)) for c in columns)
    assert all(sum(c[:5]) == sum(c[5:]) == 0 for c in columns)
    # Certify rank >= 4 by a nonzero minor on the four surviving free rows.
    representatives = {}
    for j, c in enumerate(columns):
        representatives.setdefault(tuple(c[i] for i in (2, 3, 6, 8)), j)
    for indices in combinations(representatives.values(), 4):
        minor = [[columns[j][i] for j in indices] for i in (2, 3, 6, 8)]
        det = determinant(minor)
        if det:
            break
    else:
        raise AssertionError('No rank-four minor')

    # The all-distinct triple singleton is stationary but violates a word identity.
    bad = tuple(result['stationary_but_impossible_type'])
    row = table[types.index(bad)]
    assert row['stationarity_column'] == [1]+[0]*10
    # Explicit six-point completion, separately from the abstract admissibility test.
    a, b = (1, 3, 4, 0, 2, 5), (2, 0, 5, 1, 3, 4)
    root_pattern = canon((0, a[0], b[0], a[a[0]], b[a[0]], a[b[0]], b[b[0]]))
    assert root_pattern == bad

    # Re-derive tight-type laws using the four-bit and three-bit formulas in PROOF.md.
    alpha_type = (0, 1, 1, 2, 3, 2, 3)
    beta_type = (0, 1, 2, 0, 1, 2, 0)
    assert compare(cost_terms(alpha_type, F(1, 2)), {2:F(3,2),3:-F(3,4),7:-F(7,16),11:F(11,16)}) == 0
    assert compare(cost_terms(beta_type, F(1, 2)), {2:F(2),5:F(5,8),7:-F(7,8)}) == 0
    # The dual coefficients themselves are independently reconstructed.
    assert A == {2:F(1,2),3:-F(3,4),7:-F(7,16),11:F(11,16)}
    assert B == {2:-F(1),5:-F(5,8),7:F(7,8)}

    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    out = {'types_reenumerated':len(types), 'inclusion_exclusion_costs_checked':515,
           'maximum_predecessor_cost_difference':maximum_difference,
           'certificate_inequalities_checked':103, 'exact_zero_slacks':zeros,
           'grouped_minima_checked':len(grouped_pairs),
           'stationarity_rank':4, 'rank_four_minor_types':[types[i] for i in indices],
           'rank_four_minor':minor,'rank_four_minor_determinant':det,
           'impossible_type_six_point_completion':{'a':a,'b':b},
           'nice_priority':os.getpriority(os.PRIO_PROCESS,0),
           'peak_rss_bytes':rss,'elapsed_seconds':time.monotonic()-started}
    (ROOT/'independent_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
