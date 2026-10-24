#!/usr/bin/env python3
"""Exact finite tests for uniform condensation windows and sampling sharpness.

Run from this directory. Requires only the Python standard library and the
included predecessor checker. Assertions use integers/Fraction; floats are
rounded displays. No test is an independent audit of an asymptotic proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from collections import Counter
from math import factorial, comb
import hashlib
import json
from pathlib import Path
import importlib.util


def load_predecessor():
    """Use the bundled checker, or its pinned immutable repository sibling."""
    here = Path(__file__).resolve().parent
    candidates = [here / 'check_full_path.py',
                  here.parent / 'direct_janson1840_full_path_11-47-17Z' / 'check_full_path.py']
    expected = 'd06ea210b6b02eac50611c98585cabe210e765619ed70ede75ce3384013dbf36'
    for script in candidates:
        if script.is_file():
            if hashlib.sha256(script.read_bytes()).hexdigest() != expected:
                raise RuntimeError(f'Predecessor checker hash mismatch: {script}')
            spec = importlib.util.spec_from_file_location('pinned_predecessor_checker', script)
            if spec is None or spec.loader is None:
                raise RuntimeError(f'Cannot load predecessor checker: {script}')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    raise FileNotFoundError('The bundled or repository-sibling predecessor checker is required.')


prior = load_predecessor()


def coefficient_powers(weights: dict[int, int], n_max: int, degree: int) -> list[list[int]]:
    if n_max < 0 or degree < 0 or weights.get(0) != 1:
        raise ValueError('Require nonnegative limits and normalized w_0=1.')
    if any(j < 0 or w < 0 for j, w in weights.items()):
        raise ValueError('Weights and indices must be nonnegative.')
    arrays = [[1]+[0]*degree]
    for _ in range(n_max):
        current = arrays[-1]
        nxt = [0]*(degree+1)
        for size, weight in weights.items():
            if size <= degree:
                for mass in range(degree-size+1):
                    nxt[mass+size] += weight*current[mass]
        arrays.append(nxt)
    return arrays


def binary_bound(value: F) -> int:
    """Largest integer L such that value <= 2**(-L), exactly."""
    if value <= 0:
        raise ValueError('Require a positive rational.')
    L = value.denominator.bit_length()-value.numerator.bit_length()
    def holds(exponent: int) -> bool:
        return (value.numerator*(1 << exponent) <= value.denominator
                if exponent >= 0 else
                value.numerator <= value.denominator*(1 << -exponent))
    while not holds(L):
        L -= 1
    while holds(L+1):
        L += 1
    return L


def finite_window() -> dict:
    # A fixed infinite law is obtained by adding w_{j!}=2**((j!)**2), j>=5.
    # All those indices exceed the largest tested mass and do not enter here.
    weights = {0:1, 2:2**4, 3:2**9, 5:2**25, 17:2**289}
    small = {j:w for j,w in weights.items() if j < 17}
    all_coeffs = coefficient_powers(weights, 44, 22)
    small_coeffs = coefficient_powers(small, 44, 22)
    scaled_coeffs = coefficient_powers({3*j:w for j,w in weights.items()},44,66)
    representations = {3:([3],0,1), 4:([2,2],0,2), 5:([5],1,0)}
    k,K,t = 17,4,0
    worst_actual, worst_bound, worst_sharp = F(0),F(0),F(0)
    actual_pair = bound_pair = sharp_pair = None
    count = 0
    for m in range(20,23):
        r=m-k
        parts,R,C=representations[r]
        W=1
        for j in parts: W*=weights[j]
        assert sum(parts)==r
        for n in range((m+1)//2,2*m+1):
            assert F(1,2) <= F(m,n) <= 2
            assert m < 2*k and n*K >= 2*m and 2*(t+1+R+C) <= n
            z=all_coeffs[n][m]
            numerator=small_coeffs[n][m]
            assert z>0 and numerator>0
            # There is at most one size-17 box, so this identity is exact.
            assert z == numerator+n*weights[k]*small_coeffs[n-1][r]
            lower=F(n,2**(C+1))*weights[k]*W
            assert z >= lower
            p=F(numerator,z)
            bound=F(numerator)/lower
            denominator=1
            for size,multiplicity in Counter(parts).items():
                denominator *= prior.falling(min(n,m//size),multiplicity)
            sharp_lower = F(prior.falling(n-t,1+R+C),denominator)*weights[k]*W
            assert z >= sharp_lower >= lower
            sharp_bound = F(numerator)/sharp_lower
            assert 0 < p <= sharp_bound <= bound < 1
            if sharp_bound>worst_sharp: worst_sharp,sharp_pair=sharp_bound,(m,n)
            # Every small supported size is <= 3m/4, while 17 > 3m/4.
            assert max(small) <= F(3*m,4) < k
            if p>worst_actual: worst_actual,actual_pair=p,(m,n)
            if bound>worst_bound: worst_bound,bound_pair=bound,(m,n)
            assert scaled_coeffs[n][3*m] == z
            assert all(scaled_coeffs[n][j]==0 for j in range(67) if j%3)
            count += 1
    L=binary_bound(worst_bound)
    L_sharp=binary_bound(worst_sharp)
    assert worst_actual <= worst_bound <= F(1,2**L)
    return {
        'integer_pairs_checked':count,'mass_window':[20,22],
        'density_interval':['1/2','2'],'epsilon':'1/4',
        'distinguished_size':17,'threshold_event':'Y_max <= (3/4)*m',
        'maximum_actual_probability':str(worst_actual),
        'maximum_insertion_bound':str(worst_bound),
        'maximum_sharp_insertion_bound':str(worst_sharp),
        'maximum_sharp_insertion_bound_rounded':float(worst_sharp),
        'worst_sharp_pair_m_n':sharp_pair,
        'uniform_sharp_bound_at_most_2_to_minus':L_sharp,
        'maximum_actual_probability_rounded':float(worst_actual),
        'maximum_insertion_bound_rounded':float(worst_bound),
        'worst_actual_pair_m_n':actual_pair,'worst_bound_pair_m_n':bound_pair,
        'uniform_insertion_bound_at_most_2_to_minus':L,
        'span_three_coefficient_checks':count,'PASS':True,
        'scope':'One exact finite window for an explicitly specified fixed infinite law.'}


def prefix_checks() -> dict:
    # Logarithms are measured in base 2. All displayed natural-log quantities
    # in the manuscript are divided by log(2), preserving every inequality.
    a,b,D,i0,J0,Nmax=F(2),F(4),11,4,18,120
    M,C0=F(32),F(0)
    theta=prior.theta(a,D)
    kappa=M*a**(1-J0)/(a-1)
    assert theta < F(1,4) and kappa < F(1,4)
    T=a**(2-J0)/(a-1)
    U=a**(2-J0)*(F(J0)/(a-1)+1/(a-1)**2)
    L=i0+1
    tail_l=a**(1-L)*(F(L)/(a-1)+1/(a-1)**2)
    cases=[]
    total_checks=0
    patterns=[
        lambda i:F(i//4),
        lambda i: F(0) if i<4 else (F(1) if i<40 else F(2+(i-40)//20)),
        lambda i: F(0) if i<4 else (F(1) if i==4 else
                                   (F(1000) if i<70 else F(2000+(i-70)//7))),
        lambda i: F(0) if i<4 else sum((F(1,j) for j in range(4,i+1)),F(0)),
    ]
    for index,fn in enumerate(patterns):
        B=[fn(i) for i in range(Nmax+1)]
        assert all(B[i]>=B[i-1] for i in range(1,len(B)))
        record_level=0
        sizes,p=[1],[F(0)]
        for i in range(1,Nmax+1):
            if B[i]>B[i-1]: record_level=i
            sizes.append(2**record_level)
            p.append(b*record_level/sizes[-1])
        assert sizes[i0]>=4 and B[i0]>=0
        Pi=a/(a-1)**2*(p[i0]+b*a*tail_l)
        C=(theta*(B[J0-1]-B[i0])+2*a*a*Pi+M*B[J0-1]*T+b*U+C0*T)
        weighted=F(0)
        positive_max=F(0)
        min_slack=None
        for J in range(J0,Nmax+1):
            if B[J]>B[J-1]:
                k=sizes[J]
                assert k==2**J
                E=2*sum((a**(i+1)*(B[J-1]-B[i]+p[i])
                         for i in range(i0,J-D+1)),F(0))+M*B[J-1]+C0
                G=k*(B[J]-B[J-1])-b*J-E
                weighted += G/k
                positive_max=max(positive_max,G)
            lower=(1-theta-kappa)*(B[J]-B[J0-1])-C
            assert weighted >= lower
            assert positive_max >= lower/T
            slack=weighted-lower
            min_slack=slack if min_slack is None else min(min_slack,slack)
            total_checks += 1
        cases.append({'pattern':index+1,'prefixes_checked':Nmax-J0+1,
                      'minimum_exact_slack':str(min_slack),
                      'final_record_growth':str(B[-1]-B[J0-1]),
                      'PASS':True})
    return {'prefix_inequalities_checked':total_checks,'theta':str(theta),
            'kappa':str(kappa),'logarithm_units':'base 2; exact rational rescaling',
            'patterns':cases,'PASS':True,
            'scope':'Finite algebra, not a test of the zero-radius limit.'}


def sampling_checks() -> dict:
    powers=[]
    for j in range(3,18):
        n=2**j
        support=[1]+[2**i for i in range(1,j+1)]
        largest=max(k for k in support if k<=n-1)
        assert largest==n//2
        powers.append({'n':n,'maximum_permitted_size':largest,'ratio_to_n':str(F(largest,n))})
    facts=[]
    for j in range(3,14):
        n=factorial(j)
        largest=max(k for k in [1]+[factorial(i) for i in range(2,j+1)] if k<=n-1)
        assert largest==factorial(j-1) and F(largest,n)==F(1,j)
        facts.append({'factorial_index':j,'ratio_to_n':str(F(largest,n))})
    sample=list(range(2,21))+list(range(40,50))+list(range(75,81))
    sample+=list(range(150,159))+list(range(250,270))
    theta=F(3,2)
    lefts=[n for n,nn in zip(sample,sample[1:]) if nn>=theta*n]
    assert lefts==[2,20,49,80,158]
    for n in sample:
        largest=max([1]+[k for k in lefts if k<n])
        assert largest <= max(F(1),F(n)/theta)
    return {'powers_of_two_cases':len(powers),'powers_of_two':powers,
            'factorial_cases':len(facts),'factorial_ratios':facts,
            'irregular_dense_run_samples':len(sample),'large_gap_left_endpoints':lefts,
            'irregular_sample_bound_theta':str(theta),'PASS':True,
            'scope':'Deterministic support bounds; no simulation.'}


def root_checks() -> dict:
    cases,identities,total_trees=0,0,0
    rows=[]
    for n in range(2,11):
        groups={}
        def generate(position: int, remaining: int, slots: int, prefix: tuple[int,...]):
            if position==n:
                if remaining==0 and slots==0:
                    yield prefix
                return
            for degree in range(remaining+1):
                next_slots=slots-1+degree
                if position<n-1 and next_slots<=0:
                    continue
                if position==n-1 and next_slots!=0:
                    continue
                yield from generate(position+1,remaining-degree,next_slots,prefix+(degree,))
        count=0
        for degrees in generate(0,n-1,1,()):
            key=tuple(sorted(Counter(degrees).items()))
            roots=groups.setdefault(key,Counter())
            roots[degrees[0]]+=1
            count+=1
        assert count==comb(2*n-2,n-1)//n
        for key,roots in groups.items():
            counts=dict(key)
            number=sum(roots.values())
            denominator=1
            for multiplicity in counts.values(): denominator*=factorial(multiplicity)
            assert F(factorial(n-1),denominator)==number
            for degree,multiplicity in counts.items():
                assert F(roots.get(degree,0),number)==F(degree*multiplicity,n-1)
                identities+=1
            cases+=1
        total_trees+=count
        rows.append({'n':n,'plane_trees':count,'degree_count_classes':len(groups)})
    return {'plane_trees_enumerated':total_trees,'degree_count_classes':cases,
            'conditional_root_identities':identities,'sizes':rows,'PASS':True,
            'scope':'A finite check of the known size-biased root identity, not a new root law.'}


def main() -> None:
    predecessor={'insertion':prior.insertion_checks(),'kernel':prior.kernel_checks(),
                 'plateau':prior.plateau_checks(),'greedy':prior.greedy_checks()}
    assert all(v['PASS'] for v in predecessor.values())
    out={'finite_window':finite_window(),'finite_prefix_margin':prefix_checks(),
         'sampling':sampling_checks(),'root_identity':root_checks(),
         'predecessor_checks_reexecuted':{
             'occupation_count_identities':predecessor['insertion']['exact_type_identities_checked'],
             'kernel_cases':predecessor['kernel']['finite_nonnegative_convolution_cases'],
             'plateau_cases':predecessor['plateau']['cases_including_398_scale_plateau'],
             'greedy_cases':predecessor['greedy']['exact_geometric_decompositions_and_energy_bounds'],
             'status':'ALL_EXACT_CHECKS_PASS'},
         'predecessor_checker_sha256':hashlib.sha256(Path(prior.__file__).read_bytes()).hexdigest(),
         'status':'ALL_EXACT_CHECKS_PASS',
         'scope':'Exact finite evidence only; zero independent asymptotic proof audits.'}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
