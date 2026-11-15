"""T221: independent collision audit and a stationarity relaxation.

One process/thread, bounded to 103 columns. Only local files are written.
HiGHS locates candidates; rational identities and integer products certify
the reported witnesses independently of solver tolerances.
"""

import itertools
import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path
import resource
import signal
import sys
import time
import warnings

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(180)
ROOT = Path(__file__).resolve().parent
OLD = Path('~/codex_op_1114r4/briefs/T221')
TRIPLES = ((0, 1, 2), (1, 3, 4), (2, 5, 6))
EDGES = (((0, 1), (1, 3), (2, 5)),
         ((0, 2), (1, 4), (2, 6)))


def canon(values):
    labels = {}
    return tuple(labels.setdefault(v, len(labels)) for v in values)


def partitions(n):
    # Insert the final element in each old block or in a new block.
    # This recursion differs from the preceding restricted-growth search.
    if not n:
        yield ()
        return
    for blocks in partitions(n-1):
        for j in range(len(blocks)):
            yield blocks[:j] + (blocks[j] + (n-1,),) + blocks[j+1:]
        yield blocks + ((n-1,),)


def types():
    all_types = []
    for blocks in partitions(7):
        labels = {v: i for i, block in enumerate(blocks) for v in block}
        pi = canon(labels[v] for v in range(7))
        all_types.append(pi)
    assert len(set(all_types)) == len(all_types) == 877
    return sorted(pi for pi in all_types if all(
        (pi[u] == pi[v]) == (pi[x] == pi[y])
        for edges in EDGES for u, x in edges for v, y in edges))


def prime_factors(n):
    out = Counter()
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def add_log(out, coefficient, rational):
    for p, power in prime_factors(rational.numerator).items():
        out[p] += coefficient * power
    for p, power in prime_factors(rational.denominator).items():
        out[p] -= coefficient * power


def entropy_form(probabilities):
    out = defaultdict(Q)
    for q in probabilities:
        if q:
            add_log(out, -q, q)
    return {p: c for p, c in out.items() if c}


def combine(*terms):
    out = defaultdict(Q)
    for coefficient, form in terms:
        for prime, c in form.items():
            out[prime] += coefficient*c
    return {p: c for p, c in out.items() if c}


def value(form):
    return sum(float(c)*math.log(p) for p, c in form.items())


def sign(form):
    den = math.lcm(*(c.denominator for c in form.values()))
    numerator = denominator = 1
    for prime, c in form.items():
        exponent = int(c*den)
        if exponent >= 0:
            numerator *= prime**exponent
        else:
            denominator *= prime**(-exponent)
    return (numerator > denominator) - (numerator < denominator)


def cost(pi, p):
    n = max(pi)+1
    output, joint, names = defaultdict(Q), defaultdict(Q), defaultdict(Q)
    for ones in itertools.product((False, True), repeat=n):
        mass = p**sum(ones) * (1-p)**(n-sum(ones))
        if not mass:
            continue
        x = tuple(ones[v] for v in pi)
        y = tuple(int(all(x[v] for v in triple)) for triple in TRIPLES)
        output[y[0]] += mass
        names[y] += mass
        joint[x[0], y] += mass
    form = combine((1, entropy_form(output.values())),
                   (1, entropy_form(joint.values())),
                   (-1, entropy_form(names.values())))
    # A separate posterior computation uses only root=1 joint masses.
    posterior = 0.0
    for name, mass in names.items():
        q = joint.get((True, name), Q(0))/mass
        posterior += float(mass)*value(entropy_form((q, 1-q)))
    direct = value(entropy_form(output.values()))+posterior
    assert abs(value(form)-direct) < 2e-12
    return form


def pattern(a, b, root):
    return canon((root, a[root], b[root], a[a[root]], b[a[root]],
                  a[b[root]], b[b[root]]))


def matrix(types):
    sigmas = sorted({canon(pi[i] for i in triple)
                     for pi in types for triple in TRIPLES})
    rows = [[1]*len(types)]
    for triple in TRIPLES[1:]:
        for sigma in sigmas:
            rows.append([int(canon(pi[i] for i in TRIPLES[0]) == sigma)
                         - int(canon(pi[i] for i in triple) == sigma)
                         for pi in types])
    return rows, sigmas


def rank(matrix):
    a = [[Q(v) for v in row] for row in matrix]
    k = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        q = a[k][j]
        a[k] = [v/q for v in a[k]]
        for i in range(k+1, len(a)):
            q = a[i][j]
            a[i] = [v-q*w for v, w in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def rational_candidate(x, rows):
    out = [Q(float(v)).limit_denominator(100000) for v in x]
    assert min(out) >= 0
    assert [sum(v*c for v, c in zip(out, row)) for row in rows] == [1]+[0]*(len(rows)-1)
    return out


def serialize_form(form):
    return {str(p): str(c) for p, c in sorted(form.items())}


def main():
    start = time.monotonic()
    ts = types()
    assert len(ts) == 103
    previous = json.loads((OLD/'collision_table.json').read_text())
    table = {}
    maximum_difference = 0.0
    for p in (Q(0), Q(1, 3), Q(1, 2), Q(2, 3), Q(1)):
        table[p] = {pi: cost(pi, p) for pi in ts}
        old = {tuple(r['partition']): r['cost'] for r in previous if Q(r['p_one']) == p}
        assert set(old) == set(ts)
        for pi in ts:
            maximum_difference = max(maximum_difference, abs(value(table[p][pi])-old[pi]))
        h = entropy_form((p, 1-p))
        branch = max((1, 2), key=lambda j: value(entropy_form((p**j, 1-p**j))))
        cap = combine((1, h), (p, entropy_form((p**branch, 1-p**branch))))
        assert all(sign(combine((1, form), (-1, cap))) <= 0 for form in table[p].values())
        for a, b, j in [((1, 0), (1, 0), 1), ((1, 2, 0), (2, 0, 1), 2)]:
            branch_form = combine((1, h), (p, entropy_form((p**j, 1-p**j))))
            for root in range(len(a)):
                assert table[p][pattern(a, b, root)] == branch_form
    assert maximum_difference < 2e-12
    with (ROOT/'LOG.md').open('a') as f:
        f.write('\n## 3. Independent predecessor recheck passed\n\n'
                'Read REPORT.md, LOG.md, PROOF.md and scripts in all three predecessor folders. '
                'The chain rule gives nH(p) <= sum_v [H(Z_v)+H(U_v|N_v)] because Z is a function of U '
                'and each N_v is a subtuple of Z. On the prefix classes, equality preservation and '
                'reflection make each prescribed generator map an injective partial map, which '
                'extends by pairing unused sources and targets. Thus the previous main claims hold.\n\n'
                'This independent script constructs set partitions by block insertion, tests all '
                'pairwise equality equivalences on the generator edges, and computes rational '
                'probabilities with entropy as rational combinations of logarithms of primes. '
                f'All 103 types and 515 predecessor costs matched; maximum floating discrepancy {maximum_difference}. '
                'Exact integer-product comparisons verify every analytic cap, and explicit C2/C3 '
                'models attain both cap branches at every root for all five bases.\n')

    # All numerical libraries are loaded only after the independent recheck.
    import numpy as np
    from scipy.optimize import linprog, OptimizeWarning
    rows, sigmas = matrix(ts)
    rhs = [1]+[0]*(len(rows)-1)
    fair = table[Q(1, 2)]
    objective = [value(fair[pi]) for pi in ts]
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=OptimizeWarning, message='Unrecognized options detected.*')
        opt = linprog(objective, A_eq=np.array(rows), b_eq=rhs,
                      bounds=(0, None), method='highs-ds', options={'threads': 1})
        maximum = linprog([-v for v in objective], A_eq=np.array(rows), b_eq=rhs,
                          bounds=(0, None), method='highs-ds', options={'threads': 1})
    assert opt.success and maximum.success
    weights = rational_candidate(opt.x, rows)
    min_form = combine(*[(q, fair[pi]) for pi, q in zip(ts, weights) if q])
    witness = [{'type': pi, 'weight': str(q), 'cost': value(fair[pi]),
                'cost_log_form': serialize_form(fair[pi])}
               for pi, q in zip(ts, weights) if q]
    max_weights = rational_candidate(maximum.x, rows)
    max_form = combine(*[(q, fair[pi]) for pi, q in zip(ts, max_weights) if q])
    assert max_form == {2: Q(3, 2)}

    # Exact dual certificate reconstructed from the two nontrivial tight types.
    # Rows 4 and 7 are the only nonzero stationarity multipliers needed.
    h = {2: Q(1)}
    alpha = combine((1, fair[(0, 1, 1, 2, 3, 2, 3)]), (-1, h))
    beta = combine((1, h), (-1, fair[(0, 1, 2, 0, 1, 2, 0)]))
    assert sign(alpha) > 0 and sign(beta) > 0
    certificate = []
    grouped = {}
    for j, pi in enumerate(ts):
        excess = combine((1, fair[pi]), (-1, h),
                         (-rows[4][j], alpha), (-rows[7][j], beta))
        exact = sign(excess)
        assert exact >= 0
        pair = (rows[4][j], rows[7][j])
        if pair not in grouped or sign(combine((1, fair[pi]), (-1, fair[grouped[pair]]))) < 0:
            grouped[pair] = pi
        certificate.append({'type': pi, 'slack_log_form': serialize_form(excess),
                            'exact_slack_sign': exact})
    assert sum(r['exact_slack_sign'] == 0 for r in certificate) == 3

    # A stationary singleton not realizable as a type-frequency distribution.
    # Every triple has three distinct classes, so all stationarity rows vanish.
    # But ab fixes its root while ba does not, contradicting conjugacy globally.
    impossible = (0, 1, 2, 3, 0, 4, 5)
    j = ts.index(impossible)
    assert [row[j] for row in rows] == rhs
    assert impossible[0] == impossible[4] and impossible[0] != impossible[5]

    # Independent exhaustive small models check stationarity at all roots.
    model_count = root_count = 0
    for n in (1, 2, 3, 4):
        for a, b in itertools.product(itertools.permutations(range(n)), repeat=2):
            histogram = Counter(pattern(a, b, r) for r in range(n))
            x = [Q(histogram[pi], n) for pi in ts]
            assert [sum(v*c for v, c in zip(x, row)) for row in rows] == rhs
            assert sum(q*int(pi[0] == pi[4]) for pi, q in zip(ts, x)) == sum(
                q*int(pi[0] == pi[5]) for pi, q in zip(ts, x))
            form = combine(*[(q, fair[pi]) for pi, q in zip(ts, x) if q])
            assert sign(combine((1, form), (-1, {2: Q(1)}))) >= 0
            model_count += 1
            root_count += n
    out = {'predecessor_types': len(ts), 'predecessor_costs_checked': 515,
           'maximum_predecessor_cost_discrepancy': maximum_difference,
           'triple_patterns': sigmas, 'stationarity_rows': len(rows)-1,
           'rank_with_normalization': rank(rows),
           'stationary_minimum_float': opt.fun,
           'stationary_minimum_candidate_log_form': serialize_form(min_form),
           'candidate_minus_base_sign_exact': sign(combine((1, min_form), (-1, {2: Q(1)}))),
           'candidate': witness, 'stationary_maximum': value(max_form),
           'stationary_maximum_log_form': serialize_form(max_form),
           'dual_alpha': serialize_form(alpha), 'dual_alpha_float': value(alpha),
           'dual_beta': serialize_form(beta), 'dual_beta_float': value(beta),
           'dual_exact_nonnegative_slacks': len(certificate),
           'dual_exact_zero_slacks': sum(r['exact_slack_sign'] == 0 for r in certificate),
           'minimum_unconstrained_cost': min(value(form) for form in fair.values()),
           'grouped_dual_check': [
               {'column_pair': pair, 'minimum_cost_type': pi,
                'minimum_cost': value(fair[pi]),
                'minimum_cost_log_form': serialize_form(fair[pi])}
               for pair, pi in sorted(grouped.items())],
           'stationary_but_impossible_type': impossible,
           'impossible_type_cost': value(fair[impossible]),
           'small_model_assignments': model_count, 'small_model_root_checks': root_count,
           'nice_priority': os.getpriority(os.PRIO_PROCESS, 0),
           'elapsed_seconds': time.monotonic()-start}
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    out['peak_rss_bytes'] = rss
    (ROOT/'stationarity_result.json').write_text(json.dumps(out, indent=2)+'\n')
    (ROOT/'stationarity_table.json').write_text(json.dumps([
        {'type': pi, 'cost_log_form': serialize_form(fair[pi]),
         'stationarity_column': [row[j] for row in rows]}
        for j, pi in enumerate(ts)], indent=2)+'\n')
    (ROOT/'stationarity_certificate.json').write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
