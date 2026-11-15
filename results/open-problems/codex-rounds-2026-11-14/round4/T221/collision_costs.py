"""Finite collision table for T221; standard library, one process/thread.

All state written by this script stays beside this file. Predecessor
artifacts are not imported or executed. Natural logarithms throughout.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
import itertools as it
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent
signal.alarm(180)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def reduce_word(w):
    out = []
    for letter in w:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def partitions(n):
    """Restricted-growth strings, each set partition exactly once."""
    def extend(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for label in range(maximum + 2):
                yield from extend(prefix + [label], max(maximum, label))
    yield from extend([0], 0)


def canon(values):
    names = {}
    return tuple(names.setdefault(v, len(names)) for v in values)


def complete(words, pi, rank):
    """Return completed generator permutations, or None for inadmissible pi."""
    index = {w: i for i, w in enumerate(words)}
    n = max(pi) + 1
    output = {}
    for letter in range(1, rank + 1):
        forward, backward = {}, {}
        for i, word in enumerate(words):
            nxt = reduce_word(word + (letter,))
            if nxt not in index:
                continue
            source, target = pi[i], pi[index[nxt]]
            if source in forward and forward[source] != target:
                return None
            if target in backward and backward[target] != source:
                return None
            forward[source], backward[target] = target, source
        free_sources = sorted(set(range(n)) - forward.keys())
        free_targets = sorted(set(range(n)) - backward.keys())
        forward.update(zip(free_sources, free_targets))
        perm = tuple(forward[i] for i in range(n))
        assert sorted(perm) == list(range(n))
        output[letter] = perm
        inverse = [None] * n
        for i, j in enumerate(perm):
            inverse[j] = i
        output[-letter] = tuple(inverse)
    return output


def evaluate(word, root, permutations):
    for letter in word:
        root = permutations[letter][root]
    return root


def H(ps):
    return -sum(float(q) * math.log(float(q)) for q in ps if q)


def exact_sign(terms):
    """Sign of sum c*H(ps), c and ps rational, via rational powers.

    Expand each entropy as -sum q log q, clear all denominators c*q,
    and compare the resulting rational product with 1. This deliberately
    does not call the entropy function or use floating-point tolerances.
    """
    powers = defaultdict(F)
    for coefficient, probabilities in terms:
        for q in probabilities:
            if q:
                powers[q] -= coefficient * q
    den = math.lcm(*(q.denominator for q in powers.values()))
    ratio = F(1)
    for q, power in powers.items():
        ratio *= q ** int(den * power)
    return (ratio > 1) - (ratio < 1)


WORDS = [(), (1,), (2,), (1, 1), (1, 2), (2, 1), (2, 2)]
# Encoder positions: 1,a,b. Decoder positions: 1,a,b.
ENCODER = (0, 1, 2)
NAMES = ((0, 1, 2), (1, 3, 4), (2, 5, 6))


def distributions(pi, p):
    """Direct class-label enumeration, without a permutation action."""
    n = max(pi) + 1
    ey, joint, names = defaultdict(F), defaultdict(F), defaultdict(F)
    for labels in it.product((0, 1), repeat=n):
        mass = p**sum(labels) * (1-p)**(n-sum(labels))
        if not mass:
            continue
        inputs = tuple(labels[j] for j in pi)
        e = math.prod(inputs[j] for j in ENCODER)
        name = tuple(math.prod(inputs[j] for j in row) for row in NAMES)
        ey[e] += mass
        joint[inputs[0], name] += mass
        names[name] += mass
    assert sum(ey.values()) == sum(joint.values()) == sum(names.values()) == 1
    conditional = H(joint.values()) - H(names.values())
    # Independent entropy calculation by posterior averaging.
    posterior = sum(float(mass) * H(
        [joint.get((bit, name), F(0)) / mass for bit in (0, 1)])
        for name, mass in names.items())
    assert abs(conditional - posterior) < 2e-12
    terms = [(F(1), list(ey.values())), (F(1), list(joint.values())),
             (F(-1), list(names.values()))]
    return H(ey.values()) + conditional, terms, abs(conditional-posterior)


def target_conditioned_on_children(p):
    """An independent two-child posterior formula for the seven-word target.

    A child output is 1 with probability p^3. Conditional on that output,
    its root bit has probability q=1 or p(1-p^2)/(1-p^3). The two child
    bits remain conditionally independent. This uses no set partition or
    seven-bit enumeration.
    """
    hp = H([p, 1-p])
    terms = [(F(1), [p**3, 1-p**3]), (F(1), [p, 1-p])]
    children = []
    if p**3:
        children.append((p**3, F(1)))
    if 1-p**3:
        children.append((1-p**3, p*(1-p*p)/(1-p**3)))
    mutual_information = 0.0
    for (mass0, q0), (mass1, q1) in it.product(children, repeat=2):
        mass, q = mass0*mass1, q0*q1
        mutual_information += float(mass)*(H([p*q, 1-p*q])-float(p)*H([q, 1-q]))
        terms.extend([(-mass, [p*q, 1-p*q]), (mass*p, [q, 1-q])])
    return H([p**3, 1-p**3]) + hp-mutual_information, terms


def check_full_model(perms, p, table):
    """Full independent labels and Z vector, not a local collision sum."""
    n = len(perms[1])
    zlaw = defaultdict(F)
    local_joint = [defaultdict(F) for _ in range(n)]
    local_e = [defaultdict(F) for _ in range(n)]
    for x in it.product((0, 1), repeat=n):
        mass = p**sum(x) * (1-p)**(n-sum(x))
        if not mass:
            continue
        z = tuple(x[v] * x[perms[1][v]] * x[perms[2][v]] for v in range(n))
        zlaw[z] += mass
        for v in range(n):
            name = (z[v], z[perms[1][v]], z[perms[2][v]])
            local_joint[v][x[v], name] += mass
            local_e[v][z[v]] += mass
    total_cost = 0.0
    alpha = beta = 0
    for v in range(n):
        pi = canon(evaluate(w, v, perms) for w in WORDS)
        assert pi in table
        names = defaultdict(F)
        for (_, name), mass in local_joint[v].items():
            names[name] += mass
        direct = H(local_e[v].values()) + H(local_joint[v].values()) - H(names.values())
        assert abs(direct - table[pi]) < 2e-12
        total_cost += direct
        alpha += len({pi[i] for i in ENCODER}) != 3
        beta += len(set(pi)) != 7
    hp = H([p, 1-p])
    # Full-name chain identity H(U)=H(Z)+H(U|Z), checked by posterior U|Z.
    posterior_u = defaultdict(list)
    for x in it.product((0, 1), repeat=n):
        mass = p**sum(x) * (1-p)**(n-sum(x))
        if mass:
            z = tuple(x[v] * x[perms[1][v]] * x[perms[2][v]] for v in range(n))
            posterior_u[z].append(mass / zlaw[z])
    full_cond = sum(float(zlaw[z]) * H(qs) for z, qs in posterior_u.items())
    assert abs(n*hp - H(zlaw.values()) - full_cond) < 3e-12
    slack = total_cost/n - hp
    assert slack >= -3e-12
    target = tuple(range(7))
    c0 = table[target]
    a = H([p**3, 1-p**3])
    c = c0-a
    delta = hp-c0
    # Independent numerical check of the predecessor's separate-defect bound.
    assert delta <= (alpha/n)*(math.log(2)-a) + (beta/n)*(hp-c) + 3e-12
    return slack


def main():
    started = time.monotonic()
    all_pi = list(partitions(7))
    assert len(all_pi) == 877  # Bell number B_7, independently count below.
    # Recurrence for Bell numbers, independent of partition generation.
    bells = [1]
    for n in range(7):
        bells.append(sum(math.comb(n, j)*bells[j] for j in range(n+1)))
    assert bells[7] == len(all_pi)
    valid = {}
    for pi in all_pi:
        perms = complete(WORDS, pi, 2)
        if perms is not None:
            assert canon(evaluate(w, 0, perms) for w in WORDS) == pi
            valid[pi] = perms
    # Exercise inverse-letter paths and both directions of injectivity.
    signed_words = [(), (1,), (-1,)]
    signed_valid = []
    for pi in partitions(3):
        perms = complete(signed_words, pi, 1)
        if perms is not None:
            assert canon(evaluate(w, 0, perms) for w in signed_words) == pi
            signed_valid.append(pi)
    assert signed_valid == [(0, 0, 0), (0, 1, 1), (0, 1, 2)]

    # Necessity is checked separately by all permutation pairs on four points.
    observed = set()
    assignments = 0
    for a, b in it.product(it.permutations(range(4)), repeat=2):
        perms = {1:a, 2:b}
        for root in range(4):
            pi = canon(evaluate(w, root, perms) for w in WORDS)
            assert pi in valid
            observed.add(pi)
        assignments += 1

    rows, summaries = [], []
    max_cond_difference = 0.0
    completion_checks = 0
    for p in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1)):
        table, exact = {}, {}
        branch = exact_sign([(F(1), [p, 1-p]), (F(-1), [p*p, 1-p*p])])
        j = 1 if branch >= 0 else 2
        expected = H([p, 1-p]) + float(p)*H([p**j, 1-p**j])
        formula_terms = [(F(1), [p, 1-p]), (p, [p**j, 1-p**j])]
        for pi in valid:
            cost, terms, discrepancy = distributions(pi, p)
            table[pi], exact[pi] = cost, terms
            max_cond_difference = max(max_cond_difference, discrepancy)
            # Exact signs audit both the cap and the floating comparison.
            sign = exact_sign(terms + [(-c, qs) for c, qs in formula_terms])
            assert sign <= 0
            assert cost <= expected + 2e-12
            rows.append({'p_one': str(p), 'partition': pi, 'cost': cost,
                         'exact_sign_cost_minus_cap': sign})
        min_slack = math.inf
        for perms in valid.values():
            min_slack = min(min_slack, check_full_model(perms, p, table))
            completion_checks += 1
        target = tuple(range(7))
        alternate_target, alternate_terms = target_conditioned_on_children(p)
        assert abs(table[target]-alternate_target) < 2e-12
        assert exact_sign(exact[target] + [(-c, qs) for c, qs in alternate_terms]) == 0
        target_sign = exact_sign(exact[target] + [(F(-1), [p, 1-p])])
        assert target_sign >= 0
        maximizers = [pi for pi in valid if exact_sign(
            exact[pi] + [(-c, qs) for c, qs in formula_terms]) == 0]
        assert maximizers
        # Explicit C2/C3 attainments are separate from the completion routine.
        two = {1:(1, 0), 2:(1, 0)}
        three = {1:(1, 2, 0), 2:(2, 0, 1)}
        for perms, exponent in ((two, 1), (three, 2)):
            pi = canon(evaluate(w, 0, perms) for w in WORDS)
            assert pi in table
            expected_terms = [(F(1), [p, 1-p]), (p, [p**exponent, 1-p**exponent])]
            assert exact_sign(exact[pi] + [(-c, qs) for c, qs in expected_terms]) == 0
        summaries.append({'p_one': str(p), 'maximizing_exponent': j,
                          'maximum_cost': expected,
                          'universal_cap': math.log(2)+H([p, 1-p]),
                          'cap_improvement': math.log(2)+H([p, 1-p])-expected,
                          'number_of_maximizers': len(maximizers),
                          'target_cost': table[target],
                          'target_delta': H([p, 1-p])-table[target],
                          'target_posterior_formula_discrepancy':abs(table[target]-alternate_target),
                          'exact_sign_target_cost_minus_base': target_sign,
                          'minimum_full_model_information_slack': min_slack})

    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    output = {'group_pattern':'F2, S=D=(1,a,b), seven distinct words',
              'all_partitions':len(all_pi), 'admissible_partitions':len(valid),
              'rejected_partitions':len(all_pi)-len(valid),
              'maximum_completion_vertices':max(max(pi)+1 for pi in valid),
              'negative_letter_admissible_patterns':signed_valid,
              'four_vertex_assignments':assignments,
              'four_vertex_root_checks':4*assignments,
              'four_vertex_distinct_patterns':len(observed),
              'bases':summaries,
              'completed_model_base_checks':completion_checks,
              'maximum_conditional_entropy_discrepancy':max_cond_difference,
              'exact_arithmetic':'Fraction probabilities and entropy-product signs',
              'nice_priority':os.getpriority(os.PRIO_PROCESS, 0),
              'peak_rss_bytes':rss, 'elapsed_seconds':time.monotonic()-started}
    (ROOT/'collision_table.json').write_text(json.dumps(rows, indent=2)+'\n')
    (ROOT/'collision_summary.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
