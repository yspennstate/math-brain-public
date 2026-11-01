"""Exact finite checks for the affine-influence / variance FEI continuation.

All accepted comparisons use integers, Fraction, or certified log expressions
from the explicitly attributed prior_exact_entropy.py dependency. No Lean,
independent audit, or universal FEI proof is claimed. Run with Python >= 3.10.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib
import json
import random
import time

import prior_exact_entropy as E


def canonical(f):
    return tuple(x*f[0] for x in f)


def rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            bit = v.bit_length()-1
            if bit not in pivots:
                pivots[bit] = v
                break
            v ^= pivots[bit]
    return len(pivots)


@lru_cache(None)
def affine_data(f):
    N = len(f); n = N.bit_length()-1
    assert N == 1 << n and set(f) <= {-1, 1}
    walsh = E.fwht(f)
    numerator = E.fwht([x*x for x in walsh])
    assert all(x % N == 0 for x in numerator)
    corr_counts = [x//N for x in numerator]
    alpha = tuple(F(N-v, 2*N) for v in corr_counts)
    weights = tuple(min(x, 1-x) for x in alpha)
    chosen = []
    for v in sorted(range(1, N), key=lambda v: (weights[v], v)):
        if rank(chosen+[v]) > len(chosen):
            chosen.append(v)
        if len(chosen) == n:
            break
    assert len(chosen) == n
    M = sum((weights[v] for v in chosen), F(0))
    influences = tuple(alpha[1 << i] for i in range(n))
    var = 1-F(sum(f), N)**2
    max_mass = F(max(x*x for x in walsh), N*N)
    return {'n': n, 'alpha': alpha, 'weights': weights, 'basis': tuple(chosen),
            'M': M, 'I': sum(influences), 'I_i': influences,
            'J': sum(min(x, 1-x) for x in influences),
            'Var': var, 'max_mass': max_mass}


@lru_cache(None)
def variance_sum(f):
    if all(v == f[0] for v in f):
        return F(0)
    N = len(f)
    children = Counter(E.derivative(f, z) for z in range(N))
    return affine_data(f)['Var'] + sum((multiplicity*variance_sum(child)
                      for child, multiplicity in children.items()), F(0))/(2*N)


@lru_cache(None)
def allocation_sum(f):
    if all(v == f[0] for v in f):
        return E.LogExpr()
    N = len(f)
    children = Counter(E.derivative(f, z) for z in range(N))
    return E.information(f)['A'] + sum((multiplicity*allocation_sum(child)
                        for child, multiplicity in children.items()), E.LogExpr())/(2*N)


def rank_integral(data):
    n = data['n']; weights = data['weights']
    breaks = sorted(set(weights) | {F(0), F(1, 2)})
    total = F(0)
    for a, b in zip(breaks, breaks[1:]):
        cheap = [v for v in range(len(weights)) if weights[v] <= a]
        total += (b-a)*(n-rank(cheap))
    return total


def one_point(d):
    return canonical(tuple(-1 if x == 0 else 1 for x in range(1 << d)))


def sharp_variance_formula(d):
    prob = F(1); sum_prob = F(0)
    for ell in range(1, d+1):
        prob *= 1-F(2**(ell-1), 2**d)
        sum_prob += prob
    return F(4, 2**d)*sum_prob


def test_variance():
    functions = set(); raw_count = 0
    for n in range(4):
        for bits in range(1 << (1 << n)):
            f = canonical(tuple(1 if (bits >> x) & 1 else -1 for x in range(1 << n)))
            functions.add(f); raw_count += 1
    rng = random.Random(2026091901)
    for n, count in [(4, 96), (5, 20)]:
        for _ in range(count):
            functions.add(canonical(tuple(rng.choice((-1, 1)) for x in range(1 << n))))
    best = F(0); rows = []
    for f in sorted(functions, key=lambda f: (len(f), f)):
        data = affine_data(f); V = variance_sum(f)
        Vstar = V + (1-data['max_mass'])-data['Var']
        assert 0 <= V <= 2*data['I']
        assert 0 <= Vstar <= 2*data['M'] <= 2*data['J']
        assert data['M'] == rank_integral(data)
        if data['I']:
            best = max(best, V/data['I'])
    for d in range(1, 6):
        f = one_point(d)
        assert variance_sum(f) == sharp_variance_formula(d)
    for d in [4, 8, 16, 32, 64, 128]:
        value = sharp_variance_formula(d)/F(2*d, 2**d)
        assert max(F(0), 2-F(4, d)) <= value <= 2
        rows.append({'one_point_dimension': d, 'V_over_I': E.show(value)})
    # Exact scalar supersolution check on rational arguments.
    for k in range(1, 101):
        delta = F(k, 200); t = 2*delta*(1-delta)
        gap = 4*delta*E.log_rat(1/delta)-4*delta*(1-delta)-2*t*E.log_rat(1/t)
        gap.nonnegative()
    return {'status': 'PASS', 'raw_all_truth_tables_through_dimension_3': raw_count,
            'distinct_functions_checked': len(functions), 'memoized_chain_states': variance_sum.cache_info().currsize,
            'largest_observed_V_over_I': E.show(best), 'one_point_direct_chain_dimensions': [1,2,3,4,5],
            'supersolution_rational_points': 100, 'sharpness_values': rows,
            'scope': 'Universal statements rely on the proof; finite rational checks are self-checks.'}


def monotone_predicted(f):
    data = affine_data(f)
    a = max(data['I_i'], default=F(0))
    q = 1-data['alpha'][-1]
    return data['I']-a+min(a, q)


def test_monotone():
    count = 0; all_small = []
    for n in range(1, 5):
        for bits in range(1 << (1 << n)):
            f = tuple(1 if (bits >> x) & 1 else -1 for x in range(1 << n))
            if E.increasing(f):
                all_small.append(f); count += 1
    tested_inclusions = tested_antipodal = 0
    for f in all_small:
        data = affine_data(f); n = data['n']; alpha = data['alpha']
        assert data['M'] == monotone_predicted(f)
        assert data['M'] == rank_integral(data)
        for v in range(len(f)):
            for i in range(n):
                if not (v >> i) & 1:
                    assert alpha[v] <= alpha[v | (1 << i)]
                    assert alpha[v] <= 1-data['I_i'][i]
                    tested_inclusions += 1; tested_antipodal += 1
        # Compare entire threshold-rank formula, not just its integral.
        for t in sorted(set(data['weights']) | {F(0), F(1, 2)}):
            light = sum(a <= t for a in data['I_i'])
            predicted_rank = min(n, light + int(1-alpha[-1] <= t))
            actual_rank = rank([v for v, w in enumerate(data['weights']) if w <= t])
            assert predicted_rank == actual_rank
    rng = random.Random(2026091902); samples = {}
    for n in range(5, 9):
        for k in range(100):
            if k % 2:
                terms = [rng.randrange(1 << n) for _ in range(rng.randrange(1, 2*n))]
                f = tuple(1 if any((x&t)==t for t in terms) else -1 for x in range(1 << n))
            else:
                weights = [rng.randrange(1, 31) for _ in range(n)]
                thresh = rng.randrange(1, sum(weights)+1)
                f = tuple(1 if sum(weights[i] for i in range(n) if (x >> i)&1) >= thresh else -1
                          for x in range(1 << n))
            assert E.increasing(f)
            assert affine_data(f)['M'] == monotone_predicted(f)
        samples[str(n)] = 100
    # Brute-force all unordered bases in dimensions <=3 confirms greedy independently.
    bases_checked = 0
    for f in all_small:
        data = affine_data(f); n = data['n']
        if n > 3: continue
        values = []
        for basis in combinations(range(1, 1 << n), n):
            if rank(basis) == n:
                values.append(sum(data['weights'][v] for v in basis)); bases_checked += 1
        assert min(values) == data['M']
    return {'status': 'PASS', 'all_monotone_functions_dimensions_1_to_4': count,
            'subset_inclusion_checks': tested_inclusions, 'omitted_coordinate_checks': tested_antipodal,
            'random_monotone_samples': samples, 'independently_enumerated_basis_instances': bases_checked,
            'scope': 'Exact all-small checks plus fixed-seed monotone DNF and threshold samples.'}


def tensor(f, g):
    n = len(f).bit_length()-1
    return canonical(tuple(f[x & (len(f)-1)]*g[x >> n] for x in range(len(f)*len(g))))


def test_tensor():
    functions = [canonical(tuple(1 if (bits >> x)&1 else -1 for x in range(4))) for bits in range(16)]
    pairs = 0; threshold_checks = 0
    for f in functions:
        for g in functions:
            fg = tensor(f, g); a,b,c = affine_data(f), affine_data(g), affine_data(fg)
            assert c['M'] == a['M']+b['M']
            for t in sorted(set(c['weights'])):
                ra = rank([v for v,w in enumerate(a['weights']) if w<=t])
                rb = rank([v for v,w in enumerate(b['weights']) if w<=t])
                rc = rank([v for v,w in enumerate(c['weights']) if w<=t])
                assert rc == ra+rb; threshold_checks += 1
            pairs += 1
    rng = random.Random(2026091903)
    for _ in range(60):
        n = rng.choice([2, 3, 4]); m = rng.choice([1, 2, 3])
        f=canonical(tuple(rng.choice([-1,1]) for x in range(1 << n)))
        g=canonical(tuple(rng.choice([-1,1]) for x in range(1 << m)))
        assert affine_data(tensor(f,g))['M'] == affine_data(f)['M']+affine_data(g)['M']
        pairs += 1
    return {'status': 'PASS', 'tensor_pairs': pairs, 'threshold_rank_equalities': threshold_checks}


def random_surjection(rows, columns, rng):
    matrix = [1 << i for i in range(rows)] + [rng.randrange(1 << rows) for _ in range(columns-rows)]
    # Elementary column additions implement an invertible input reparameterization.
    for _ in range(5*columns):
        i,j = rng.sample(range(columns), 2)
        matrix[i] ^= matrix[j]
    rng.shuffle(matrix)
    assert rank(matrix) == rows
    return matrix


def lift(f, matrix, translation, character):
    N = 1 << len(matrix)
    syndromes = [0]*N
    for x in range(1, N):
        bit=x&-x
        syndromes[x]=syndromes[x^bit]^matrix[bit.bit_length()-1]
    return canonical(tuple(f[syndromes[x]^translation]*(-1 if (x&character).bit_count()%2 else 1)
                           for x in range(N)))


def majority_formula(shape):
    if shape == 'x': return (-1,1)
    assert len(shape) == 3
    return E.compose_variable(E.majority(3), [majority_formula(s) for s in shape])


def test_positive_class():
    maj = majority_formula(('x','x','x'))
    unbalanced_tree = majority_formula((('x','x','x'),'x','x'))
    two_branches = majority_formula((('x','x','x'),('x','x','x'),'x'))
    regular2 = majority_formula((('x','x','x'),('x','x','x'),('x','x','x')))
    seeds = [('point2',one_point(2)), ('point3',one_point(3)), ('point4',one_point(4)),
             ('majority3',canonical(maj)), ('unequal_majority5',canonical(unbalanced_tree)),
             ('unequal_majority7',canonical(two_branches)), ('regular_majority9',canonical(regular2))]
    # Quadratic phases: all choices on three variables, with linear terms irrelevant to M and H.
    for mask in range(8):
        f = canonical(tuple((-1)**sum(((mask >> k)&1)*((x>>i)&1)*((x>>j)&1)
                        for k,(i,j) in enumerate([(0,1),(0,2),(1,2)])) for x in range(8)))
        data = affine_data(f)
        assert (E.basic(f)['H']-2*data['M']).is_zero()
    quad=canonical(tuple(-1 if (x&1) and (x&2) else 1 for x in range(4)))
    seeds += [('quadratic2',quad), ('point2_times_majority3',tensor(one_point(2),maj)),
              ('point2_times_quadratic2',tensor(one_point(2),quad))]
    seed_rows=[]
    for name,f in seeds:
        data=affine_data(f); H=E.basic(f)['H']
        (4*data['M']-H).nonnegative()
        seed_rows.append({'name':name, 'variables':data['n'], 'H':E.show(H),
                          'minimum_affine_influence':str(data['M']), 'ordinary_influence':str(data['I'])})
    rng = random.Random(2026091904); count=0; allocation_checks=0
    for name,f in seeds:
        n=affine_data(f)['n']
        for _ in range(5):
            N=n+rng.randrange(0,3)
            matrix=random_surjection(n,N,rng)
            Ff=lift(f,matrix,rng.randrange(1<<n),rng.randrange(1<<N))
            data=affine_data(Ff)
            assert data['M']==affine_data(f)['M']
            assert (E.basic(Ff)['H']-E.basic(f)['H']).is_zero()
            (4*data['M']-E.basic(Ff)['H']).nonnegative()
            assert data['M']<=data['J']<=data['I']
            if N<=5:
                (8*data['M']-allocation_sum(Ff)).nonnegative()
                allocation_checks+=1
            count+=1
    # Unequal read-once trees: actual entropy identity, rather than guessed recurrence.
    for f in [maj, unbalanced_tree, two_branches, regular2]:
        b=E.basic(canonical(f)); a=affine_data(canonical(f))
        assert (b['H']-4*(sum(b['I'])-1)).is_zero()
        assert a['M']==a['I']-max(a['I_i'])
    # Known nondegenerate quadratic phases: the new variance resource stays bounded.
    bent_rows=[]
    for n in [2,4,6,8]:
        f=canonical(tuple((-1)**sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(n//2))
                          for x in range(1<<n)))
        a=affine_data(f)
        Vstar=variance_sum(f)+1-a['max_mass']-a['Var']
        assert (E.basic(f)['H']-n).is_zero()
        assert a['M']==F(n,2) and Vstar==F(3,2)*(1-F(1,2**n))
        bent_rows.append({'variables':n,'entropy':n,'Vstar':str(Vstar),'M':str(a['M'])})
    clause_rows=[]
    for r in [4,8,16,32,64,128]:
        a=F(1,2**(r-1)); lo,hi=E.ln_unit(1/(1-a))
        loglo,loghi=lo/E.LN2[1],hi/E.LN2[0]
        other=(4*a-2*a*a)*(r-1)
        Hlo=2*(1-a)**2*loglo+other; Hhi=2*(1-a)**2*loghi+other
        assert 0<=Hlo<=Hhi<=4*r*a
        clause_rows.append({'clause_dimension':r,
                            'H_over_M_lower':E.decimal_bound(Hlo/(r*a),12,True),
                            'H_over_M_upper':E.decimal_bound(Hhi/(r*a),12,False)})
    return {'status':'PASS','seed_classes':seed_rows, 'surjective_affine_mixed_examples':count,
            'full_allocation_chain_checks':allocation_checks,'quadratic_three_variable_phases':8,
            'bounded_variance_unbounded_entropy_family':bent_rows, 'constant_four_sharpness':clause_rows,
            'scope':'Physical-input linear mixtures are tested; joint row rank is required in the theorem.'}


def test_shared_shift():
    raw_count=0; identities=0; covariance_nonzero=0
    for n in range(4):
        N=1<<n
        for bits in range(1<<N):
            f=canonical(tuple(1 if (bits>>x)&1 else -1 for x in range(N)))
            w=E.fwht(f)
            c=[[sum(w[s]*w[s^u]*w[s^k]*w[s^k^u] for s in range(N))
                for k in range(N)] for u in range(N)]
            assert all(c[u][k]==c[k][u] for u in range(N) for k in range(N))
            assert all(sum(c[u][k] for u in range(N))==0 for k in range(1,N))
            Dm=[E.fwht(E.derivative(f,z)) for z in range(N)]
            for u in range(N):
                for z in range(N):
                    # c is the Fourier expansion in the shared shift, denominator N^4.
                    numerator=sum(c[u][k]*(-1 if (k&z).bit_count()%2 else 1) for k in range(N))
                    assert numerator==Dm[z][u]**2*N*N
                for v in range(N):
                    actual=sum(Dm[z][u]**2*Dm[z][v]**2 for z in range(N))*N**3
                    assert actual==sum(c[u][k]*c[v][k] for k in range(N))
                    identities+=1
            if any(c[u][k] for u in range(N) for k in range(1,N)):
                covariance_nonzero+=1
            raw_count+=1
    def two_bit_allocation(p):
        r=p[0]*p[3]; s=p[1]*p[2]
        value=E.LogExpr({2:1-sum(x*x for x in p)})
        for z in [r,s]:
            if z: value+=(-2*z)*E.log_rat(z/(r+s))
        return value
    pa=[F(16,25),F(0),F(0),F(9,25)]
    pb=[F(14,25),F(7,50),F(7,50),F(4,25)]; theta=F(4,5)
    pc=[theta*a+(1-theta)*b for a,b in zip(pa,pb)]
    gap=two_bit_allocation(pc)-theta*two_bit_allocation(pa)-(1-theta)*two_bit_allocation(pb)
    assert gap.interval()[1]<0
    return {'status':'PASS','truth_tables':raw_count,'pair_law_identities':identities,
            'arbitrary_law_concavity_counterexample':{'p':[str(x) for x in pa],
               'q':[str(x) for x in pb],'mixture_weight':str(theta),'concavity_gap':E.show(gap),
               'scope':'Arbitrary probability laws, NOT asserted to be squared Boolean spectra.'},
            'functions_with_nonzero_shared_shift_covariance':covariance_nonzero,
            'scope':'Exact amplitude-derived pair law; the shared shift is not replaced by independence.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--part',choices=['all','variance','monotone','tensor','class','shared_shift'],default='all')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); started=time.monotonic()
    here=Path(__file__).resolve().parent
    out={'full_FEI_proved':False, 'independent_audit':False, 'lean_used':False,
         'acceptance_arithmetic':'Integers, Fraction, or outward rational logarithm enclosures',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'prior_entropy_dependency_sha256':hashlib.sha256((here/'prior_exact_entropy.py').read_bytes()).hexdigest()}
    for name,job in [('variance',test_variance),('monotone',test_monotone),('tensor',test_tensor),('class',test_positive_class),('shared_shift',test_shared_shift)]:
        if args.part in ('all',name): out[name]=job()
    out['status']='ALL_REQUESTED_CHECKS_PASS';out['elapsed_seconds']=round(time.monotonic()-started,3)
    text=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text)
if __name__=='__main__':main()
