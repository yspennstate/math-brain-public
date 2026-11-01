"""A032 exact uniform-cube spectral admission. Python integers/Fraction only."""
from fractions import Fraction
from math import isqrt
from itertools import product

VERSION = 'A032-phase-exact-v1'

def walsh(values):
    a = list(values)
    assert len(a) and len(a) & (len(a)-1) == 0
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                u, v = a[k], a[k+h]
                a[k], a[k+h] = u+v, u-v
        h *= 2
    return a

def admit(probabilities, max_support=16):
    p = [Fraction(x) for x in probabilities]
    N = len(p)
    if not N or N & (N-1) or min(p) < 0 or sum(p) != 1:
        return {'status':'INVALID_PROBABILITY_LAW'}
    magnitudes = []
    for s, q in enumerate(p):
        z = q*N*N
        if z.denominator != 1 or isqrt(z.numerator)**2 != z.numerator:
            return {'status':'IMPOSSIBLE', 'certificate':'WALSH_INTEGER_SQUARE', 'label':s, 'scaled_mass':str(z)}
        magnitudes.append(isqrt(z.numerator))
    support = [i for i, a in enumerate(magnitudes) if a]
    if (N >= 2 and any(a % 2 for a in magnitudes)) or (N >= 4 and len({a % 4 for a in magnitudes}) != 1):
        return {'status':'IMPOSSIBLE', 'certificate':'COMMON_MOD4'}
    # Each unordered pair belongs to exactly one nonzero XOR equation.
    pairs = {}
    for j, s in enumerate(support):
        for t in support[j+1:]:
            pairs.setdefault(s ^ t, []).append((s,t,magnitudes[s]*magnitudes[t]))
    for u, terms in sorted(pairs.items()):
        weights = [v for s,t,v in terms]
        total = sum(weights)
        possible = {0}
        for w in weights:
            possible |= {v+w for v in list(possible)}
        if total % 2 or total//2 not in possible:
            return {'status':'IMPOSSIBLE', 'certificate':'XOR_PARTITION', 'xor':u, 'terms':terms, 'total':total, 'subset_sums':sorted(possible)}
    if len(support) > max_support:
        return {'status':'INCONCLUSIVE', 'reason':'EXPLICIT_PHASE_BUDGET', 'support':len(support)}
    count = 0
    for signs in product((1,-1), repeat=len(support)-1):
        count += 1
        a = [0]*N
        a[support[0]] = magnitudes[support[0]]
        for s, sign in zip(support[1:], signs):
            a[s] = sign*magnitudes[s]
        inverse = walsh(a)
        if all(abs(v) == N for v in inverse):
            truth = [v//N for v in inverse]
            assert walsh(truth) == a
            return {'status':'REALIZABLE', 'truth_table':truth, 'walsh_integers':a, 'phases_checked':count}
    return {'status':'IMPOSSIBLE', 'certificate':'COMPLETE_PHASE_ENUMERATION', 'phases_checked':count, 'phase_domain':2**(len(support)-1)}

def direct_walsh(truth):
    return [sum(v * (-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(truth)) for s in range(len(truth))]

def affine_admit(labelled_probabilities, ambient_n, max_rank=4):
    """Sparse ambient interface; output is an exact lifted truth-table formula."""
    law={int(s):Fraction(p) for s,p in labelled_probabilities.items() if Fraction(p)}
    if not law or min(law)<0 or max(law)>=(1<<ambient_n) or min(law.values())<0 or sum(law.values())!=1:
        return {'status':'INVALID_PROBABILITY_LAW'}
    shift=min(law); basis=[]; coordinates={0:0}
    for label in sorted(law):
        v=label^shift
        if v not in coordinates:
            bit=1<<len(basis)
            coordinates.update({w^v:c^bit for w,c in list(coordinates.items())})
            basis.append(v)
    rank=len(basis)
    if rank>max_rank:
        return {'status':'INCONCLUSIVE','reason':'EXPLICIT_AFFINE_RANK_BUDGET','rank':rank}
    compressed=[Fraction(0)]*(1<<rank)
    for label,p in law.items(): compressed[coordinates[label^shift]]=p
    result=admit(compressed)
    result.update({'ambient_n':ambient_n,'affine_shift':shift,'basis':basis,'rank':rank,
                   'lifting_formula':'f(x)=(-1)^(shift dot x) * reduced_truth_table[(basis_j dot x)_j]'})
    return result
