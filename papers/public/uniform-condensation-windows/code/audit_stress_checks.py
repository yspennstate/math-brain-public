#!/usr/bin/env python3
"""Additional exact tests prepared during the five-pass manuscript review.

This script rederives the tested finite formulas without importing the earlier
checkers. It is not a formal proof of any asymptotic theorem and is not an
independent referee review. Python standard library only.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
import json
import random


def falling(n: int, q: int) -> int:
    if not 0 <= q <= n:
        raise ValueError('The falling factorial requires 0 <= q <= n.')
    z = 1
    for i in range(q):
        z *= n-i
    return z


def compositions(total: int, n: int, cap: int):
    if n == 0:
        if total == 0:
            yield ()
        return
    for j in range(min(total, cap)+1):
        for rest in compositions(total-j, n-1, cap):
            yield (j,)+rest


def randomized_insertion() -> dict:
    rng = random.Random(20260917)
    sharp_cases = coarse_cases = large_mass_cases = overlaps = 0
    min_sharp_slack = None
    for trial in range(18000):
        n = rng.randrange(5,81)
        k = rng.randrange(2,25)
        u = rng.randrange(1,k)
        t = rng.randrange(0,min(n//2,10)+1)
        a = Counter({0:n})
        # Place each background ball in a distinct previously empty coordinate.
        # Then sometimes merge positive boxes, respecting the cap.
        a[0] -= t
        if t:
            a[1] = t
        for _ in range(t):
            occupied = [j for j in a if j > 0 and a[j] > 0]
            if not occupied:
                break
            j = rng.choice(occupied)
            candidates = [ell for ell in occupied if j+ell <= u and
                          (j != ell or a[j] >= 2)]
            if candidates:
                ell = rng.choice(candidates)
                a[j] -= 1
                a[ell] -= 1
                a[j+ell] += 1
                a[0] += 1
        Q = rng.randrange(1,min(n-t,10)+1)
        parts = [rng.randrange(1,k) for _ in range(Q-1)]
        counts = Counter(parts)
        r = sum(parts)
        m = t+k+r
        numerator = falling(a[0],Q)
        denom = 1
        sharp_denom = 1
        for j,mult in counts.items():
            denom *= falling(a[j]+mult,mult)
            sharp_denom *= falling(min(n,m//j),mult)
        actual = F(numerator,denom)
        sharp = F(falling(n-t,Q),sharp_denom)
        assert actual >= sharp > 0
        # Independently compare permutation counts of the two count vectors.
        b = a.copy()
        b[0] -= Q
        b[k] += 1
        b.update(counts)
        assert sum(b.values()) == n and sum(j*c for j,c in b.items()) == m
        da = db = 1
        for mult in a.values(): da *= factorial(mult)
        for mult in b.values(): db *= factorial(mult)
        assert F(da,db) == actual
        sharp_cases += 1
        if m >= 2*k:
            large_mass_cases += 1
        min_sharp_slack = actual/sharp if min_sharp_slack is None else min(min_sharp_slack,actual/sharp)
        K = rng.randrange(2,12)
        flags = [j >= K and bool(rng.getrandbits(1)) for j in parts]
        R = sum(flags)
        C = len(parts)-R
        large_sizes = {j for j,f in zip(parts,flags) if f}
        small_sizes = {j for j,f in zip(parts,flags) if not f}
        if n*K >= 2*m and 2*(t+Q) <= n:
            assert actual >= F(n,2**(C+1))
            coarse_cases += 1
            if large_sizes & small_sizes:
                overlaps += 1
    return {'sharp_type_comparisons':sharp_cases,
            'coarse_type_comparisons':coarse_cases,
            'cases_with_m_at_least_2k':large_mass_cases,
            'coarse_cases_with_same_size_in_both_roles':overlaps,
            'minimum_actual_over_sharp_bound':str(min_sharp_slack),
            'PASS':True}


def labelled_double_counting() -> dict:
    specs = [(7,3,2,2,(1,1)),(8,4,3,3,(2,2)),(9,5,3,2,(1,3,3))]
    rows = []
    for n,k,u,t,parts in specs:
        Q=1+len(parts)
        r=sum(parts)
        m=k+r+t
        assert t+Q <= n
        inverse=Counter()
        records=0
        backgrounds=0
        for x in compositions(t,n,u):
            zeros=[i for i,v in enumerate(x) if v==0]
            backgrounds += 1
            assert len(zeros) >= n-t
            for indices in permutations(zeros,Q):
                y=list(x)
                y[indices[0]]=k
                for idx,size in zip(indices[1:],parts): y[idx]=size
                assert sum(y)==m and y.count(k)==1
                inverse[tuple(y)]+=1
                records+=1
        bound=1
        for j,mult in Counter(parts).items():
            bound *= falling(min(n,m//j),mult)
        assert max(inverse.values()) <= bound
        assert records >= backgrounds*falling(n-t,Q)
        assert F(len(inverse),backgrounds) >= F(falling(n-t,Q),bound)
        rows.append({'n':n,'m':m,'k':k,'backgrounds':backgrounds,
                     'labelled_records':records,'different_images':len(inverse),
                     'maximum_inverse_multiplicity':max(inverse.values()),
                     'upper_inverse_multiplicity_bound':bound,'PASS':True})
    return {'examples':rows,'PASS':True}


def geometric_boundaries() -> dict:
    # Exact finite sums plus exact remaining tail for each geometric series.
    rows=[]
    for a in (F(2),F(3,2),F(11,10),F(101,100)):
        for D in (2,3,11):
            horizon=D+30
            direct=sum((a**(1-D)/(a-1) if t <= D-1 else a**(-t)/(a-1)
                        for t in range(1,horizon+1)),F(0))
            direct += a**(-horizon)/(a-1)**2
            formula=a**(1-D)*(F(D-1)/(a-1)+1/(a-1)**2)
            assert direct == formula
            for L in (0,1,17):
                M=L+35
                sum_T=sum((a**(1-j) for j in range(L,M+1)),F(0))+a**(1-M)/(a-1)
                assert sum_T == a**(2-L)/(a-1)
                sum_U=sum((j*a**(1-j) for j in range(L,M+1)),F(0))
                sum_U += a**(1-M)*(F(M+1)/(a-1)+1/(a-1)**2)
                assert sum_U == a**(2-L)*(F(L)/(a-1)+1/(a-1)**2)
            rows.append({'a':str(a),'D':D,'PASS':True})
    return {'kernel_and_endpoint_rows':rows,
            'exact_tail_identities':12*7,'PASS':True}


def root_enumeration() -> dict:
    rows=[]
    total=identities=classes=0
    for n in range(2,12):
        groups={}
        def generate(position: int, remaining: int, slots: int, first: int, counts: tuple):
            if position == n:
                if remaining == 0 and slots == 0:
                    yield first,counts
                return
            for j in range(remaining+1):
                new_slots=slots-1+j
                if (position < n-1 and new_slots <= 0) or (position == n-1 and new_slots != 0):
                    continue
                yield from generate(position+1,remaining-j,new_slots,j if position==0 else first,counts+(j,))
        count=0
        for first,degrees in generate(0,n-1,1,0,()):
            key=tuple(sorted(Counter(degrees).items()))
            groups.setdefault(key,Counter())[first]+=1
            count+=1
        assert count == comb(2*n-2,n-1)//n
        for key,roots in groups.items():
            multiplicities=dict(key)
            denominator=1
            for z in multiplicities.values(): denominator *= factorial(z)
            number=sum(roots.values())
            assert number == F(factorial(n-1),denominator)
            for j,mult in key:
                assert F(roots.get(j,0),number) == F(j*mult,n-1)
                identities += 1
            D=max(multiplicities)
            if D > F(n-1,2):
                assert multiplicities[D]==1 and F(roots.get(D,0),number)==F(D,n-1)
            classes+=1
        rows.append({'n':n,'trees':count,'classes':len(groups)})
        total+=count
    return {'plane_trees':total,'conditional_root_identities':identities,
            'degree_count_classes':classes,'sizes':rows,'PASS':True}


def main() -> None:
    out={'insertion':randomized_insertion(),
         'labelled_double_counting':labelled_double_counting(),
         'geometric_endpoints':geometric_boundaries(),
         'root':root_enumeration(),
         'status':'ALL_STRESS_CHECKS_PASS',
         'scope':'Additional exact finite tests by the same assistant; no independent referee or formal asymptotic certification.'}
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
