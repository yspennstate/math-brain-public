#!/usr/bin/env python3
"""Exact finite checks for the full-path condensation proof candidate.

All assertions use integers or fractions.Fraction. These are tests of finite
identities/inequalities, NOT a formalization of the asymptotic theorem and NOT
an independent audit. No external dependencies.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from math import factorial
import json
import random


def falling(n: int, r: int) -> int:
    if r < 0 or n < r:
        return 0
    out = 1
    for j in range(r):
        out *= n-j
    return out


def types(total: int, support: list[int], boxes: int):
    """Positive-size occupation counts, including zero-size padding."""
    support = sorted(set(support))
    def rec(i: int, left: int, used: int, counts: dict[int, int]):
        if i == len(support):
            if left == 0 and used <= boxes:
                yield {0: boxes-used, **counts}
            return
        size = support[i]
        for number in range(min(left//size, boxes-used)+1):
            if number:
                counts[size] = number
            else:
                counts.pop(size, None)
            yield from rec(i+1, left-number*size, used+number, counts)
        counts.pop(size, None)
    yield from rec(0, total, 0, {})


def type_mass(counts: dict[int, int], weights: dict[int, int], n: int) -> F:
    assert sum(counts.values()) == n
    denominator, product = 1, 1
    for size, count in counts.items():
        denominator *= factorial(count)
        product *= weights[size]**count
    return F(factorial(n)*product, denominator)


def coefficient(weights: dict[int, int], n: int, degree: int) -> int:
    c = [1]+[0]*degree
    for _ in range(n):
        nxt = [0]*(degree+1)
        for j, w in weights.items():
            if j <= degree:
                for s in range(degree-j+1):
                    nxt[s+j] += c[s]*w
        c = nxt
    return c[degree]


def insertion_checks() -> dict:
    # Includes repeated sizes, overlap of large/terminal roles, sparse support,
    # and weights above the distinguished giant (which may only help).
    specs = [
        (12, 7, 1, [2], [], 2, [1,2,3]),
        (16, 9, 3, [3], [2], 3, [1,2,3,4]),
        (20, 11, 2, [3], [3], 3, [1,2,3,4]),
        (24, 13, 3, [3,3], [1], 3, [1,2,3,4]),
        (24, 13, 4, [5], [2], 4, [2,3,5]),
        (16, 9, 2, [], [1,1], 3, [1,2,4]),
    ]
    records, checked = [], 0
    for n, k, t, large, terminal, K, support in specs:
        R, C = len(large), len(terminal)
        r = sum(large)+sum(terminal)
        m, Q = k+r+t, 1+R+C
        assert k > max(support+large+terminal, default=0)
        assert m < 2*k and n*K >= 2*m and 2*(t+Q) <= n
        assert all(x >= K for x in large)
        sizes = set([0,k,m]+support+large+terminal)
        weights = {j: (1 if j == 0 else (j+1)**2+1) for j in sizes}
        additions = Counter(large+terminal)
        reservoir_weight = 1
        for j in large+terminal:
            reservoir_weight *= weights[j]
        factor = F(n, 2**(C+1))*weights[k]*reservoir_weight
        background_sum, target_sum = F(0), F(0)
        least_ratio = None
        target_types = set()
        for a in types(t, support, n):
            b = dict(a)
            b[0] -= Q
            b[k] = 1
            for j, count in additions.items():
                b[j] = b.get(j,0)+count
            assert all(v >= 0 for v in b.values())
            assert sum(j*v for j,v in b.items()) == m
            key = tuple(sorted(b.items()))
            assert key not in target_types
            target_types.add(key)
            ma, mb = type_mass(a, weights, n), type_mass(b, weights, n)
            denominator = 1
            for j, count in additions.items():
                for ell in range(1, count+1):
                    denominator *= a.get(j,0)+ell
            exact_ratio = F(weights[k]*reservoir_weight*falling(a[0],Q), denominator)
            assert mb/ma == exact_ratio
            assert mb >= factor*ma
            least_ratio = mb/(factor*ma) if least_ratio is None else min(least_ratio,mb/(factor*ma))
            background_sum += ma
            target_sum += mb
            checked += 1
        assert background_sum == coefficient({0:1, **{j:weights[j] for j in support}},n,t)
        z = coefficient(weights,n,m)
        assert z >= target_sum >= factor*background_sum
        records.append({'n':n,'m':m,'k':k,'t':t,'R':R,'C':C,
                        'background_types':len(target_types),
                        'minimum_type_ratio_over_lemma_bound':str(least_ratio),
                        'exact_partition_over_lemma_bound':str(F(z)/(factor*background_sum))})
    return {'exact_type_identities_checked':checked,'examples':records,'PASS':True}


def theta(q: F, D: int) -> F:
    return 2*q**(3-D)*(F(D-1)/(q-1)+1/(q-1)**2)


def kernel_checks() -> dict:
    rows = []
    for q in (F(2),F(3,2),F(5,4),F(9,8),F(17,16)):
        D = 2
        while theta(q,D) >= F(1,8):
            D += 1
        kernel_mass = q**(1-D)*(F(D-1)/(q-1)+1/(q-1)**2)
        # Directly sum the first D+40 lag coefficients, and its exact tail.
        direct = F(0)
        for lag in range(1,D+41):
            direct += q**(-D)*q/(q-1) if lag <= D-1 else q**(-lag)/(q-1)
        tail = q**(-D-40)/(q-1)**2
        assert direct+tail == kernel_mass
        assert 2*q*q*kernel_mass == theta(q,D)
        assert theta(q,D) < F(1,8)
        rows.append({'q':str(q),'D':D,'theta_exact':str(theta(q,D)),
                     'theta_display':float(theta(q,D)),'strictly_below_one_eighth':True})
    # Finite convolution checks with nonnegative increments and skipped scales.
    rng = random.Random(1840)
    tests = 0
    for q,D,N in ((F(2),12,45),(F(3,2),24,60)):
        powers = {d:q**d for d in range(-N-2,N+3)}
        for _ in range(8):
            d = [F(0)]+[F(rng.randrange(0,50),rng.randrange(1,10)) if rng.random()<.22 else F(0) for _ in range(N)]
            B = [F(0)]
            for x in d[1:]: B.append(B[-1]+x)
            lhs=F(0)
            for J in range(1,N+1):
                if d[J] > 0:
                    lhs += 2*q*q*sum((powers[i-J]*(B[J-1]-B[i]) for i in range(0,J-D+1)),F(0))
            assert lhs <= theta(q,D)*sum(d)
            tests += 1
    return {'parameter_rows':rows,'finite_nonnegative_convolution_cases':tests,'PASS':True}


def plateau_checks() -> dict:
    patterns = [[0,3,19,45,75,100],[0,1,2,3,4,5,50,200],
                [0,2,400,499],[0,100,101,300,301,499]]
    tests=0
    largest_fraction=F(0)
    for q in (F(2),F(3,2),F(5,4)):
        for active in patterns:
            N=active[-1]
            for D in (2,7,12):
                p={a:F(a+1)*q**(-a) for a in active}
                lhs=F(0)
                # Sum over whole plateau pieces, with the actual cutoff J-D.
                for J in active[1:]:
                    for pos,a in enumerate(active[:-1]):
                        b=active[pos+1]
                        stop=min(b-1,J-D)
                        if stop >= a:
                            geometric=(q**(stop+1)-q**a)/(q-1)*q**(-J)
                            lhs += p[a]*geometric
                bound=q/(q-1)**2*sum(p.values())
                assert lhs <= bound
                largest_fraction=max(largest_fraction,lhs/bound)
                tests+=1
    return {'cases_including_398_scale_plateau':tests,
            'largest_lhs_over_upper_bound':str(largest_fraction),'PASS':True}


def greedy_checks() -> dict:
    # Logarithms in base 2 make this finite algebra exact: f(2**i) is an
    # integer, and the corrected slope (f+4 log_2(size))/size is rational.
    K,i0,hstar=4,3,1
    M=2**(i0+1)
    max_level=20
    H={0:F(0)}
    s={0:1}
    f={1:0}
    for i in range(1,max_level+1):
        value=F(1+(i+1).bit_length()-1)
        f[2**i]=int(2**i*value-4*i)
        if value > H[i-1]: H[i],s[i]=value,2**i
        else: H[i],s[i]=H[i-1],s[i-1]
        assert F(f[s[i]]+4*(s[i].bit_length()-1),s[i])==H[i]
    count=0
    for original in list(range(16,400))+[511,512,513,999,1024,2049,8191]:
        r=original
        pieces=[]
        stages=[]
        while r.bit_length()-2 >= i0:
            i=r.bit_length()-2
            size=s[i]
            copies=(r-hstar)//size
            assert copies>=1 and size>=K
            stages.append(i)
            pieces.extend([size]*copies)
            old=r
            r -= copies*size
            assert hstar <= r < hstar+size and r < 2**(i+1)
            assert r.bit_length()-2 < i
            assert copies*size <= old
        assert hstar <= r < M
        assert sum(pieces)+r == original
        assert len(stages)==len(set(stages))
        J=original.bit_length()+4
        h=H[J-1]
        deficit=h*original-sum(f[j] for j in pieces) # terminal: r ones, f(1)=0
        upper=F(M)*h
        for i in range(i0,original.bit_length()-1):
            penalty=F(4*(s[i].bit_length()-1),s[i])
            assert h >= H[i]
            upper += 2**(i+2)*(h-H[i]+penalty)
        assert deficit <= upper
        count+=1
    return {'exact_geometric_decompositions_and_energy_bounds':count,
            'terminal_range':[hstar,M-1],
            'logarithm_units':'base 2, exact rational rescaling','PASS':True}


def main() -> None:
    results={'insertion':insertion_checks(),'kernel':kernel_checks(),
             'plateau':plateau_checks(),'greedy':greedy_checks(),
             'status':'ALL_EXACT_CHECKS_PASS',
             'scope':'Finite type identities, coefficient inequalities, convolution constants, plateau charging and greedy algebra only; not a formal or independent asymptotic proof audit.'}
    print(json.dumps(results,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
