"""Independent verification; standard library only, no audit-script imports."""

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

HERE = Path(__file__).resolve().parent
PREVIOUS = Path('~/codex_op_1114r5/briefs/T221')
WORDS = ('','a','b','aa','ab','ba','bb')
TRIPLES = ((0,1,2),(1,3,4),(2,5,6))


def block_partitions(n):
    if n == 0:
        yield ()
    else:
        for blocks in block_partitions(n-1):
            for i in range(len(blocks)):
                yield blocks[:i]+(blocks[i]+(n-1,),)+blocks[i+1:]
            yield blocks+((n-1,),)


def normalize(values):
    encountered = []
    result = []
    for v in values:
        if v not in encountered:
            encountered.append(v)
        result.append(encountered.index(v))
    return tuple(result)


def types_independent():
    result = []
    count = 0
    for blocks in block_partitions(7):
        count += 1
        pi = normalize(next(i for i,b in enumerate(blocks) if j in b) for j in range(7))
        valid = True
        for targets in ((1,3,5),(2,4,6)):
            edges = {(pi[i],pi[j]) for i,j in enumerate(targets)}
            if len({u for u,v in edges}) != len(edges) or len({v for u,v in edges}) != len(edges):
                valid = False
        if valid:
            result.append(pi)
    assert count == 877 and len(result) == 103
    return sorted(result)


def law_by_inclusion_exclusion(pi):
    # Events: root bit 1, followed by the three conjunctions equalling 1.
    sets = [{pi[0]}]+[{pi[i] for i in t} for t in TRIPLES]
    law = {}
    for events in product((0,1), repeat=4):
        must_be_one = set().union(*(s for s,v in zip(sets,events) if v))
        zero_events = [s for s,v in zip(sets,events) if not v]
        mass = Q(0)
        for k in range(len(zero_events)+1):
            for chosen in combinations(zero_events,k):
                union = must_be_one.union(*chosen)
                mass += Q((-1)**k, 2**len(union))
        assert mass >= 0
        if mass:
            law[events] = mass
    assert sum(law.values()) == 1
    return law


def factor(n):
    out = Counter()
    candidate = 2
    while candidate*candidate <= n:
        while n % candidate == 0:
            out[candidate] += 1
            n //= candidate
        candidate += 1
    if n > 1:
        out[n] += 1
    return out


def entropy_form(law):
    form = defaultdict(Q)
    for q in law:
        for prime,power in factor(q.numerator).items():
            form[prime] -= q*power
        for prime,power in factor(q.denominator).items():
            form[prime] += q*power
    return form


def cost_form(law):
    output, names = defaultdict(Q), defaultdict(Q)
    for (r,e,a,b),q in law.items():
        output[e] += q
        names[e,a,b] += q
    form = defaultdict(Q)
    for coefficient,probabilities in ((1,output.values()),(1,law.values()),(-1,names.values())):
        for p,c in entropy_form(probabilities).items():
            form[p] += coefficient*c
    return {p:c for p,c in form.items() if c}


def form_sign(form):
    den = math.lcm(*(q.denominator for q in form.values()))
    positive = negative = 1
    for p,c in form.items():
        k = int(c*den)
        if k > 0:
            positive *= p**k
        elif k < 0:
            negative *= p**(-k)
    return (positive>negative)-(positive<negative)


def determinant_by_pivots(matrix):
    # Fraction elimination, independent of the audit's Leibniz expansion.
    a = [[Q(v) for v in row] for row in matrix]
    answer = Q(1)
    for k in range(len(a)):
        i = next(i for i in range(k,len(a)) if a[i][k])
        if i != k:
            a[k],a[i] = a[i],a[k]
            answer *= -1
        pivot = a[k][k]
        answer *= pivot
        for i in range(k+1,len(a)):
            multiplier = a[i][k]/pivot
            for j in range(k,len(a)):
                a[i][j] -= multiplier*a[k][j]
    return answer


def root_type(a,b,v):
    positions = []
    for w in WORDS:
        z = v
        for letter in w:
            z = {'a':a,'b':b}[letter][z]
        positions.append(z)
    return normalize(positions)


def main():
    start = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS,0) >= 15
    signal.alarm(180)
    report = json.loads((HERE/'compatibility_result.json').read_text())
    old = json.loads((PREVIOUS/'stationarity_table.json').read_text())
    types = types_independent()
    assert types == [tuple(row['type']) for row in old]
    costs = {}
    alpha = {2:Q(1,2),3:-Q(3,4),7:-Q(7,16),11:Q(11,16)}
    beta = {2:-Q(1),5:-Q(5,8),7:Q(7,8)}
    sigmas = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
    columns = []
    zero_slacks = 0
    for pi,row in zip(types,old):
        cost = cost_form(law_by_inclusion_exclusion(pi))
        costs[pi] = cost
        assert cost == {int(p):Q(c) for p,c in row['cost_log_form'].items()}
        restrictions = [normalize(pi[i] for i in triple) for triple in TRIPLES]
        d = [int(restrictions[0] == s)-int(restrictions[g] == s)
             for g in (1,2) for s in sigmas]
        assert row['stationarity_column'] == [1]+d
        j = int(pi[0] == pi[4])-int(pi[0] == pi[5])
        column = [d[2],d[3],d[6],d[8],j]
        columns.append(column)
        for desc in report['single_pair_conjugacy_rows']:
            u,v = desc['first_pair']
            s,t = desc['second_pair']
            direct = int(pi[u] == pi[v])-int(pi[s] == pi[t])
            assert sum(Q(c)*v for c,v in zip(desc['basis_coefficients'],column)) == direct
        assert report['new_inequality_column'][types.index(pi)] == (
            int(pi[1] == pi[6] and pi[4] != pi[5])
            -int(pi[1] != pi[6] and pi[4] != pi[5]))
        slack = defaultdict(Q,cost)
        slack[2] -= 1
        for p,c in alpha.items():
            slack[p] -= d[3]*c
        for p,c in beta.items():
            slack[p] -= d[6]*c
        sign = form_sign(slack)
        assert sign >= 0
        zero_slacks += not sign
    assert zero_slacks == 3
    selected = [types.index(tuple(pi)) for pi in report['rank_five_minor_types']]
    minor = [[columns[j][i] for j in selected] for i in range(5)]
    assert minor == report['rank_five_minor']
    assert determinant_by_pivots(minor) == 1

    # Directly verify all eleven reference-difference identities from the proof.
    # Six vanish by terminal-letter cancellation, four are d-rows, one is J.
    expected = {((0,1),(1,3)):None, ((0,1),(2,4)):None, ((0,1),(2,5)):2,
                ((0,2),(1,4)):0, ((0,2),(1,5)):None, ((0,2),(2,6)):None,
                ((0,4),(0,5)):4,
                ((1,2),(3,4)):1, ((1,2),(3,5)):None,
                ((1,2),(4,6)):None, ((1,2),(5,6)):3}
    assert len(expected) == 11
    for pi,c in zip(types,columns):
        for ((u,v),(s,t)),i in expected.items():
            assert int(pi[u] == pi[v])-int(pi[s] == pi[t]) == (0 if i is None else c[i])

    bad = tuple(report['new_impossible_singleton'])
    completion = report['new_singleton_completion']
    assert root_type(completion['a'],completion['b'],0) == bad
    # Independent short law, obtained by first conditioning on U in PROOF.md.
    manual_counts = {(0,0,0,0):14,(0,0,0,1):2,
                     (1,0,0,0):10,(1,0,1,0):2,
                     (1,1,0,0):1,(1,1,0,1):1,(1,1,1,0):1,(1,1,1,1):1}
    assert {k:Q(v,32) for k,v in manual_counts.items()} == law_by_inclusion_exclusion(bad)
    assert costs[bad] == {2:Q(9,2),3:Q(3,4),5:-Q(5,16),7:-Q(21,16)}
    assert 2**56*3**12 > 5**5*7**21

    # Verify the quantitative lemma directly as set cardinalities,
    # independently of any type table or row elimination.
    models = roots = equality_models = 0
    for n in range(1,6):
        for a in permutations(range(n)):
            for b in permutations(range(n)):
                same = {v for v in range(n) if a[v] == b[b[v]]}
                different = {v for v in range(n) if a[b[v]] != b[a[v]]}
                pos = len(same & different)
                neg = len(different-same)
                assert pos <= neg
                assert len(different) <= 2*(n-len(same))
                equality_models += pos == neg and pos > 0
                models += 1
                roots += n
    assert models == sum(math.factorial(n)**2 for n in range(1,6)) == 15017
    assert roots == sum(n*math.factorial(n)**2 for n in range(1,6)) == 74421
    sharp = report['sharp_model']
    a,b = sharp['a'],sharp['b']
    assert sorted(a) == sorted(b) == list(range(4))
    assert [root_type(a,b,v) for v in range(4)] == [tuple(pi) for pi in sharp['types']]
    assert {v for v in range(4) if a[v] == b[b[v]]} == {1,3}
    assert all(a[b[v]] != b[a[v]] for v in range(4))
    assert costs[(0,0,0,0,0,0,0)] == {2:Q(1)}
    assert costs[(0,1,1,0,0,0,0)] == {2:Q(3,2)}

    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform == 'darwin' else 1024)
    assert rss < 1024**3
    output = {'independent_type_count':len(types),'exact_costs_matched':len(costs),
              'dual_slacks_nonnegative':103,'dual_zero_slacks':zero_slacks,
              'pair_row_identities':11,'rank_five_minor_determinant':1,
              'manual_singleton_law_matched':True,'boundary_models_checked':models,
              'roots_checked':roots,'nontrivial_equality_models':equality_models,
              'sharp_distances':[1,'1/2'],'nice_priority':os.getpriority(os.PRIO_PROCESS,0),
              'peak_rss_bytes':rss,'elapsed_seconds':time.monotonic()-start}
    (HERE/'independent_verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
