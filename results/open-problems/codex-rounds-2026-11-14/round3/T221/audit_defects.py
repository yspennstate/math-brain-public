"""Independent finite-name and finite-model checks for T221.

Standard library only; bounded inputs, one process, no worker threads.
The positive-gap formal pattern below is inconsistent with group laws.
It tests the inequality without claiming an RBS counterexample.
"""

import csv
import itertools as it
import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent
OLD = Path('~/codex_op_1114/briefs/T221')
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(120)


def entropy(ps):
    return -sum(float(p) * math.log(float(p)) for p in ps if p)


def sign_entropy_sum(terms):
    """Exact sign of sum coefficient*H(distribution), without log rounding.

    Expanding -q log q directly gives a product of rational powers.
    A common denominator clears those powers. No entropy-gap-specific
    integer formula from the earlier script is used.
    """
    den = math.lcm(*(q.denominator for _, ps in terms for q in ps if q))
    value = F(1)
    for coefficient, ps in terms:
        for q in ps:
            if q:
                value *= q ** (-coefficient * int(q * den))
    return (value > 1) - (value < 1)


def table(mask, *bits):
    index = 0
    for bit in bits:
        index = 2 * index + bit
    return (mask >> index) & 1


def earlier_recheck():
    with (OLD / 'local_code_audit.csv').open() as handle:
        old = {(F(r['p_one']), int(r['f_mask']), int(r['decoder_mask'])): r
               for r in csv.DictReader(handle)}
    records = []
    checks = 0
    for p in (F(1, 2), F(1, 3), F(2, 3)):
        signs = Counter()
        for encoder in range(16):
            for decoder in range(16):
                marginal_y, marginal_r = defaultdict(F), defaultdict(F)
                names = set()
                for x in it.product((0, 1), repeat=5):
                    # Full names on C5, rather than the earlier 3-bit law.
                    y = tuple(table(encoder, x[j], x[(j + 1) % 5])
                              for j in range(5))
                    r = tuple(x[j] ^ table(decoder, y[j], y[(j + 1) % 5])
                              for j in range(5))
                    recovered = tuple(r[j] ^ table(decoder, y[j], y[(j + 1) % 5])
                                      for j in range(5))
                    assert recovered == x
                    names.add((y, r))
                    checks += 1
                    ones = sum(x)
                    mass = p**ones * (1 - p)**(5 - ones)
                    marginal_y[y[0]] += mass
                    marginal_r[r[0]] += mass
                assert len(names) == 32
                assert sum(marginal_y.values()) == sum(marginal_r.values()) == 1
                yp, rp = list(marginal_y.values()), list(marginal_r.values())
                sign = sign_entropy_sum([(1, yp), (1, rp), (-1, [p, 1-p])])
                previous = old[p, encoder, decoder]
                assert sign == int(previous['exact_gap_sign'])
                assert marginal_r.get(1, 0) == F(previous['error'])
                assert abs(entropy(yp) - float(previous['H_Y'])) < 1e-12
                assert abs(entropy(rp) - float(previous['H_R'])) < 1e-12
                signs[sign] += 1
        records.append({'p_one': str(p), 'pairs': sum(signs.values()),
                        'negative': signs[-1], 'zero': signs[0],
                        'positive': signs[1]})
    assert len(old) == 768
    return {'full_cycle_length': 5, 'pointwise_full_name_checks': checks,
            'cases': records, 'old_csv_rows_matched': len(old)}


def compose(p, q):
    """p composed with q."""
    return tuple(p[q[i]] for i in range(len(p)))


def regular_s3():
    elements = list(it.permutations(range(3)))
    e = (0, 1, 2)
    a, b = (1, 0, 2), (0, 2, 1)
    assert compose(a, b) != compose(b, a)
    index = {g: i for i, g in enumerate(elements)}
    support, dec = (e, a, b), (a, b)
    # Right translations: T_s(T_t(v)) = T_ts(v).
    trans = {g: tuple(index[compose(v, g)] for v in elements) for g in elements}
    for t in dec:
        for s in support:
            assert compose(trans[s], trans[t]) == trans[compose(t, s)]
    cases = 0
    maximum_difference = 0.0
    min_slack = math.inf
    for p in (F(1, 2), F(1, 3)):
        hp = entropy([p, 1-p])
        for encoder in range(256):
            joint = [defaultdict(F) for _ in elements]
            ys = [defaultdict(F) for _ in elements]
            # Enumerate ALL six independent labels, with their full weights.
            for x in it.product((0, 1), repeat=6):
                ones = sum(x)
                mass = p**ones * (1-p)**(6-ones)
                z = tuple(table(encoder, *(x[trans[s][v]] for s in support))
                          for v in range(6))
                for v in range(6):
                    name = tuple(z[trans[t][v]] for t in dec)
                    joint[v][x[v], name] += mass
                    ys[v][z[v]] += mass
            costs = []
            for v in range(6):
                names = defaultdict(F)
                for (_, name), mass in joint[v].items():
                    names[name] += mass
                conditional = entropy(joint[v].values()) - entropy(names.values())
                # A second derivation averages posterior entropies.
                posterior = sum(float(mass) * entropy(
                    [joint[v].get((bit, name), F(0)) / mass for bit in (0, 1)])
                    for name, mass in names.items())
                maximum_difference = max(maximum_difference, abs(conditional-posterior))
                assert abs(conditional-posterior) < 1e-12
                costs.append(entropy(ys[v].values()) + conditional)
                assert ys[v] == ys[0] and joint[v] == joint[0]
            slack = sum(costs) / 6 - hp
            min_slack = min(min_slack, slack)
            assert slack >= -1e-12
            cases += 1
    return {'group': 'S3', 'cases': cases, 'all_vertices_good': True,
            'minimum_information_slack': min_slack,
            'maximum_conditional_entropy_discrepancy': maximum_difference}


@lru_cache(maxsize=None)
def formal_local_entropies(pattern):
    """Fair bits at positions (root, a, b, ca, cb), with given collisions."""
    n = max(pattern) + 1
    joint, marginal_z, marginal_n = Counter(), Counter(), Counter()
    for x in it.product((0, 1), repeat=n):
        root, xa, xb, xca, xcb = (x[j] for j in pattern)
        z, name = xa & xb, xca & xcb
        joint[root, name] += 1
        marginal_z[z] += 1
        marginal_n[name] += 1
    den = 2**n
    h_z = entropy([F(v, den) for v in marginal_z.values()])
    h_cond = entropy([F(v, den) for v in joint.values()]) - entropy(
        [F(v, den) for v in marginal_n.values()])
    return h_z, h_cond


def canonical(values):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in values)


def positive_formal_pattern():
    # Formal pattern: ca=cb=e while e,a,b are distinct. It cannot be a
    # group pattern, by cancellation. Its positive delta is ONLY an audit.
    hp = math.log(2)
    aa = entropy([F(1, 4), F(3, 4)])
    cc = 0.0
    delta = hp - aa
    threshold = delta / (math.log(2) + delta)
    # Independently simplify the constants:
    # delta=(3/4)log(3)-log(2), threshold=1-4log(2)/(3log(3)).
    assert abs(delta - (0.75*math.log(3)-math.log(2))) < 1e-14
    assert abs(threshold - (1-4*math.log(2)/(3*math.log(3)))) < 1e-14
    good_cost = formal_local_entropies((0, 1, 2, 0, 0))
    assert abs(good_cost[0]-aa) < 1e-14 and good_cost[1] == cc
    results = []
    for n in (3, 4):
        permutations = list(it.permutations(range(n)))
        min_eta, min_q, cases = 1.0, math.inf, 0
        max_information_excess = -math.inf
        for a in permutations:
            for b in permutations:
                for c in permutations:
                    e_bad = d_bad = union_bad = 0
                    q = 0
                    costs = []
                    for v in range(n):
                        ca, cb = a[c[v]], b[c[v]]
                        # E={(ca,1),(cb,1)}; I={(1,a),(1,b),(a,b)}.
                        q += (ca != v) + (cb != v)
                        q += (v == a[v]) + (v == b[v]) + (a[v] == b[v])
                        encoder_good = a[v] != b[v]
                        decoder_good = ca == cb == v
                        eg, dg = not encoder_good, not decoder_good
                        e_bad += eg
                        d_bad += dg
                        # The W-pattern also requires root,a,b distinct.
                        word_good = decoder_good and len({v, a[v], b[v]}) == 3
                        union_bad += not word_good
                        hz, hc = formal_local_entropies(canonical((v,a[v],b[v],ca,cb)))
                        if encoder_good:
                            assert abs(hz-aa) < 1e-12
                        if decoder_good:
                            assert abs(hc-cc) < 1e-12
                        costs.append(hz+hc)
                    eta = union_bad / n
                    assert eta + 1e-12 >= threshold
                    assert q / n + 1e-12 >= eta
                    assert delta <= (e_bad/n)*(hp-aa)+(d_bad/n)*(hp-cc)+1e-12
                    information_excess = hp - sum(costs)/n
                    max_information_excess = max(max_information_excess, information_excess)
                    assert information_excess <= 1e-12
                    min_eta = min(min_eta, eta)
                    min_q = min(min_q, q/n)
                    cases += 1
        results.append({'vertices': n, 'all_generator_assignments': cases,
                        'minimum_word_bad_fraction': min_eta,
                        'minimum_Q': min_q,
                        'maximum_information_excess': max_information_excess})
    return {'warning': 'inconsistent formal pattern; not a group or RBS witness',
            'delta': delta, 'defect_threshold': threshold, 'cases': results,
            'cached_local_patterns': formal_local_entropies.cache_info().currsize}


def main():
    started = time.monotonic()
    out = {'earlier_result': earlier_recheck(),
           'noncommutative_check': regular_s3(),
           'positive_gap_arithmetic_check': positive_formal_pattern()}
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    out.update(nice_priority=os.getpriority(os.PRIO_PROCESS, 0),
               peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-started)
    (ROOT/'audit_defects.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
