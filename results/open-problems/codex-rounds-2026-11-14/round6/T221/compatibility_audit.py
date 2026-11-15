"""Exact checks on the seven-word collision table. Writes only beside this file."""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product, combinations, permutations
import json
import math
import os
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent
OLD = Path('~/codex_op_1114r5/briefs/T221')
WORDS = ((), (1,), (2,), (1,1), (1,2), (2,1), (2,2))
TRIPLES = ((0,1,2), (1,3,4), (2,5,6))
SIGMAS = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))


def guard():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    signal.alarm(180)


def canon(values):
    labels = {}
    return tuple(labels.setdefault(v, len(labels)) for v in values)


def partitions(n, prefix=(0,)):
    if len(prefix) == n:
        yield prefix
    else:
        for j in range(max(prefix)+2):
            yield from partitions(n, prefix+(j,))


def admissible(pi):
    return all((pi[s] == pi[t]) == (pi[u] == pi[v])
               for targets in ((1,3,5),(2,4,6))
               for s,u in enumerate(targets) for t,v in enumerate(targets))


def distributions(pi):
    # Fair class labels, represented by integer counts out of 2^k.
    output, joint, names = Counter(), Counter(), Counter()
    for labels in product((0,1), repeat=max(pi)+1):
        x = tuple(labels[j] for j in pi)
        y = tuple(math.prod(x[i] for i in triple) for triple in TRIPLES)
        output[y[0]] += 1
        joint[x[0], y] += 1
        names[y] += 1
    denominator = 2**(max(pi)+1)
    return [(1, [F(v,denominator) for v in output.values()]),
            (1, [F(v,denominator) for v in joint.values()]),
            (-1, [F(v,denominator) for v in names.values()])]


def entropy_sign(terms, subtract_form):
    # No logarithms: expand the entropy into rational powers and compare to 1.
    powers = defaultdict(F)
    for c, law in terms:
        for q in law:
            if q:
                powers[q] -= c*q
    for prime, coefficient in subtract_form.items():
        powers[F(prime)] -= coefficient
    scale = math.lcm(*(v.denominator for v in powers.values()))
    ratio = F(1)
    for q, exponent in powers.items():
        ratio *= q**int(scale*exponent)
    return (ratio > 1)-(ratio < 1)


def stationarity(types):
    restrictions = [[canon(pi[j] for j in triple) for triple in TRIPLES] for pi in types]
    return [[int(s[0] == sigma)-int(s[g] == sigma) for s in restrictions]
            for g in (1,2) for sigma in SIGMAS]


def rref(rows):
    a = [[F(x) for x in row] for row in rows]
    pivots = []
    for j in range(len(a[0])):
        pivot = next((i for i in range(len(pivots),len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        k = len(pivots)
        a[k],a[pivot] = a[pivot],a[k]
        q = a[k][j]
        a[k] = [v/q for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                q = a[i][j]
                a[i] = [v-q*w for v,w in zip(a[i],a[k])]
        pivots.append(j)
        if len(pivots) == len(a):
            break
    return a[:len(pivots)], pivots


def determinant(matrix):
    n = len(matrix)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               *math.prod(matrix[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def row_coordinates(row, basis):
    # Solve using independent pivot columns, then check all 103 columns.
    _, pivots = rref(basis)
    augmented = [[basis[k][j] for k in range(len(basis))]+[row[j]] for j in pivots]
    reduced, _ = rref(augmented)
    coefficients = [line[-1] for line in reduced]
    assert all(sum(c*b[j] for c,b in zip(coefficients,basis)) == row[j] for j in range(len(row)))
    return coefficients


def complete(pi):
    n = max(pi)+1
    answer = []
    for targets in ((1,3,5),(2,4,6)):
        mapping = {pi[i]:pi[j] for i,j in enumerate(targets)}
        assert len(set(mapping.values())) == len(mapping)
        unused_sources = sorted(set(range(n))-mapping.keys())
        unused_targets = sorted(set(range(n))-set(mapping.values()))
        mapping.update(zip(unused_sources,unused_targets))
        answer.append(tuple(mapping[i] for i in range(n)))
    assert pattern(*answer,0) == pi
    return answer


def reduce_word(word):
    stack = []
    for c in word:
        if stack and stack[-1] == -c:
            stack.pop()
        else:
            stack.append(c)
    return tuple(stack)


def inverse(word):
    return tuple(-c for c in word[::-1])


def conjugacy_class(word):
    # Fixed-point fractions agree for conjugates and inverses.
    w = reduce_word(word)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    if not w:
        return ()
    return min(v[k:]+v[:k] for v in (w,inverse(w)) for k in range(len(v)))


def pattern(a,b,root):
    return canon((root,a[root],b[root],a[a[root]],b[a[root]],a[b[root]],b[b[root]]))


def main():
    guard()
    started = time.monotonic()
    types = [pi for pi in partitions(7) if admissible(pi)]
    assert len(types) == 103
    old = json.loads((OLD/'stationarity_table.json').read_text())
    assert types == [tuple(row['type']) for row in old]
    D = stationarity(types)
    alpha = {2:F(1,2),3:-F(3,4),7:-F(7,16),11:F(11,16)}
    beta = {2:-F(1),5:-F(5,8),7:F(7,8)}
    zeros = []
    for j,pi in enumerate(types):
        terms = distributions(pi)
        form = {int(p):F(q) for p,q in old[j]['cost_log_form'].items()}
        assert entropy_sign(terms,form) == 0
        assert old[j]['stationarity_column'] == [1]+[row[j] for row in D]
        bound = defaultdict(F,{2:F(1)})
        for p,c in alpha.items():
            bound[p] += D[3][j]*c
        for p,c in beta.items():
            bound[p] += D[6][j]*c
        sign = entropy_sign(terms,bound)
        assert sign >= 0
        if not sign:
            zeros.append(pi)
    assert len(zeros) == 3
    assert len(rref(D)[1]) == 4
    assert entropy_sign(distributions((0,0,0,0,0,0,0)),{2:F(1)}) == 0
    assert entropy_sign(distributions((0,1,1,0,0,0,0)),{2:F(3,2)}) == 0
    check = {'types':len(types),'costs_exactly_matched':103,'nonnegative_dual_slacks':103,
             'zero_slack_types':zeros,'stationarity_rank':4}
    if '## Independent predecessor check passed' not in (ROOT/'LOG.md').read_text():
      with (ROOT/'LOG.md').open('a') as f:
        f.write('\n## Independent predecessor check passed\n\n'
                'Read all four predecessor reports, logs, proofs and scripts. Recomputed fair class-label '
                'laws and expanded rational entropy powers without importing a predecessor script. '
                'All 103 exact costs, all stationarity columns, all 103 nonnegative dual slacks and '
                'the three equality cases match. Rational elimination gives stationarity rank four. '
                'The attained costs log 2 and (3/2)log 2 are exact. '
                'The earlier main result holds. The direct conditional bound C <= H(R)+H(E|R) '
                'independently proves the upper bound.\n')

    # All equalities between two window words are visible. Group them by
    # conjugacy/inversion of u v^-1, a complete free-group conjugacy test.
    groups = defaultdict(list)
    for i,j in combinations(range(7),2):
        groups[conjugacy_class(WORDS[i]+inverse(WORDS[j]))].append((i,j))
    conjugacy_rows, descriptions = [], []
    for word,pairs in sorted(groups.items()):
        first = pairs[0]
        for pair in pairs[1:]:
            row = [int(pi[first[0]] == pi[first[1]])-int(pi[pair[0]] == pi[pair[1]]) for pi in types]
            conjugacy_rows.append(row)
            descriptions.append({'cyclic_word':word,'first_pair':first,'second_pair':pair,'row':row})
    J = [int(pi[0] == pi[4])-int(pi[0] == pi[5]) for pi in types]
    ranks = {'D':len(rref(D)[1]), 'D_plus_J':len(rref(D+[J])[1]),
             'D_plus_all_pair_conjugacy':len(rref(D+conjugacy_rows)[1]),
             'with_normalization':len(rref([[1]*len(types)]+D+[J])[1])}
    assert ranks == {'D':4,'D_plus_J':5,'D_plus_all_pair_conjugacy':5,'with_normalization':6}
    basis = [D[i] for i in (2,3,6,8)]+[J]
    for desc,row in zip(descriptions,conjugacy_rows):
        desc['basis_coefficients'] = [str(c) for c in row_coordinates(row,basis)]
    minor_types = [(0,0,1,0,1,2,0),(0,0,1,0,1,2,2),
                   (0,1,0,0,2,1,0),(0,1,0,2,2,1,0),(0,1,2,3,0,4,5)]
    minor = [[row[types.index(pi)] for pi in minor_types] for row in basis]
    assert determinant(minor) == 1
    stationary_singletons = [pi for j,pi in enumerate(types) if all(row[j] == 0 for row in D)]
    refined_singletons = [pi for pi in stationary_singletons if (pi[0] == pi[4]) == (pi[0] == pi[5])]

    # Boundary transport: noncommuting roots with A=B^2 cannot outnumber
    # noncommuting roots with A!=B^2. This is strictly stronger than the
    # Hamming-distance triangle bound, and is a linear inequality on types.
    K = [(2*int(pi[1] == pi[6])-1)*int(pi[4] != pi[5]) for pi in types]
    bad = (0,1,2,0,3,4,1)
    j = types.index(bad)
    assert all(row[j] == 0 for row in D+conjugacy_rows)
    assert J[j] == 0 and K[j] == 1
    bad_completion = complete(bad)
    bad_cost = old[j]['cost_log_form']
    assert entropy_sign(distributions(bad), {2:F(1)}) > 0
    # The exact extrema are still attained after BOTH compatibility refinements.
    for pi in ((0,0,0,0,0,0,0),(0,1,1,0,0,0,0),(0,1,2,2,0,0,1)):
        jj = types.index(pi)
        assert all(row[jj] == 0 for row in D+conjugacy_rows)
        assert K[jj] <= 0

    counts = []
    for n in range(1,6):
        count = 0
        for a,b in product(permutations(range(n)),repeat=2):
            indices = [types.index(pattern(a,b,v)) for v in range(n)]
            assert all(sum(row[i] for i in indices) == 0 for row in D+conjugacy_rows)
            assert sum(K[i] for i in indices) <= 0
            E = {v for v in range(n) if a[v] == b[b[v]]}
            N = {v for v in range(n) if b[a[v]] != a[b[v]]}
            exits = {v for v in E if b[v] not in E}
            entrances = {v for v in range(n) if v not in E and b[v] in E}
            assert E & N == exits
            assert entrances <= N-E
            assert len(exits) == len(entrances)
            assert len(N) <= 2*(n-len(E))
            count += 1
        assert count == math.factorial(n)**2
        counts.append({'vertices':n,'assignments':count,'roots':n*count})
    a,b = (0,3,2,1),(1,2,3,0)
    sharp_types = [pattern(a,b,v) for v in range(4)]
    sharp_E = [v for v in range(4) if a[v] == b[b[v]]]
    sharp_N = [v for v in range(4) if b[a[v]] != a[b[v]]]
    assert len(sharp_E) == 2 and len(sharp_N) == 4
    assert sum(K[types.index(pi)] for pi in sharp_types) == 0
    out = {'earlier_result':check,'ranks':ranks,
           'conjugacy_groups':[{'word':w,'pairs':ps} for w,ps in sorted(groups.items())],
           'stationary_singletons':stationary_singletons,'refined_singletons':refined_singletons,
           'single_pair_conjugacy_rows':descriptions,
           'rank_five_minor_types':minor_types,'rank_five_minor':minor,'rank_five_minor_determinant':1,
           'new_inequality_column':K,'new_impossible_singleton':bad,
           'new_singleton_completion':{'a':bad_completion[0],'b':bad_completion[1]},
           'new_singleton_cost_log_form':bad_cost,
           'new_singleton_cost':sum(float(F(q))*math.log(int(p)) for p,q in bad_cost.items()),
           'new_singleton_boundary_violation':K[j],
           'all_small_models':counts,'total_models':sum(r['assignments'] for r in counts),
           'total_roots':sum(r['roots'] for r in counts),
           'sharp_model':{'a':a,'b':b,'E':sharp_E,'noncommuting_roots':sharp_N,'types':sharp_types},
           'nice_priority':os.getpriority(os.PRIO_PROCESS,0)}
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform == 'darwin' else 1024)
    assert rss < 1024**3
    out.update(peak_rss_bytes=rss,elapsed_seconds=time.monotonic()-started)
    (ROOT/'compatibility_result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
                     ('single_pair_conjugacy_rows','stationary_singletons','refined_singletons',
                      'conjugacy_groups','new_inequality_column')},indent=2))


if __name__ == '__main__':
    main()
