#!/usr/bin/env python3
"""Exact checks of phase comparison and polynomial-tag affine-fibre gluing."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random
from verify_polynomial_symmetry import (
    ZERO, binary_entropy, constant, derivative, entropy_counts, expand,
    metrics, nonnegative, pack, phase, restriction,
)

SEED=202609201143
COUNTS=Counter()

def phase_comparison(f,E,sigma):
    n=len(f).bit_length()-1
    g=tuple(v*sigma[pack(x,E)] for x,v in enumerate(f))
    mf=metrics(f);mg=metrics(g)
    R=tuple(i for i in range(n) if i not in E)
    pf=[0]*(1<<len(R));pg=pf.copy()
    for s in range(1<<n):
        pf[pack(s,R)]+=mf[1][s];pg[pack(s,R)]+=mg[1][s]
    assert pf==pg
    HY=entropy_counts(pf)
    assert ((mg[4]-mf[4])-((mg[4]-HY)-(mf[4]-HY))).zero()
    budget=ZERO
    for i in E:budget=budget+binary_entropy(mg[3][i])
    nonnegative(mf[4]+budget-mg[4],'phase comparison marginal bound')
    COUNTS['phase_comparison_cases']+=1
    return g

def all_boolean(n):
    for b in range(1<<(1<<n)):
        yield tuple(-1 if (b>>x)&1 else 1 for x in range(1<<n))

def invertible_rows(n,rng):
    # Start with identity and apply invertible elementary row operations.
    rows=[1<<i for i in range(n)]
    if n>1:
        for _ in range(8*n):
            i,j=rng.sample(range(n),2);rows[i]^=rows[j]
    return rows

def affine_partition_labels(m,k,rng):
    rows=invertible_rows(m,rng)
    shift=rng.randrange(1<<m)
    transformed=[sum(((row&y).bit_count()&1)<<i for i,row in enumerate(rows))^shift
                 for y in range(1<<m)]
    # Leaves of a physical restriction tree, subsequently pulled back by
    # an invertible affine transformation. This permits oblique affine cells.
    leaves=[tuple(range(1<<m))]
    while len(leaves)<min(1<<k,1<<m) and rng.randrange(5):
        options=[i for i,L in enumerate(leaves) if len(L)>1]
        if not options:break
        idx=rng.choice(options);L=leaves.pop(idx)
        axes=[i for i in range(m) if len({(x>>i)&1 for x in L})==2]
        axis=rng.choice(axes)
        leaves.extend(tuple(x for x in L if ((x>>axis)&1)==b) for b in (0,1))
    labels=rng.sample(range(1<<k),len(leaves))
    table={x:label for L,label in zip(leaves,labels) for x in L}
    pi=tuple(table[x] for x in transformed)
    for a in set(pi):
        cell=[y for y,v in enumerate(pi) if v==a];b=cell[0]
        V={y^b for y in cell}
        assert all(x^y in V for x in V for y in V)
    return pi

def core_g(m,rng,quadratic):
    monos=[a for a in range(1<<m) if a.bit_count()<= (2 if quadratic else min(m,7))]
    P=frozenset(rng.sample(monos,rng.randrange(min(len(monos),10)+1)))
    g=phase(P,m)
    if quadratic:return g,F(4)
    groups=[tuple(range(m//2)),tuple(range(m//2,m))]
    groups=[G for G in groups if G]
    tables=[[rng.choice((-1,1)) for _ in range(len(G)+1)] for G in groups]
    out=[]
    for y,v in enumerate(g):
        for G,table in zip(groups,tables):v*=table[sum((y>>i)&1 for i in G)]
        out.append(v)
    return tuple(out),F(301,25)

def tag_case(k,m,pi,g,Q,K0):
    f=tuple((-1 if (x&pi[y]).bit_count()%2 else 1)*g[y]
            for y in range(1<<m) for x in range(1<<k))
    # Affine terms may be discarded without changing entropy or folded influences.
    nonlinear=frozenset(a for a in Q if a.bit_count()>=2)
    T=tuple(i for i in range(k) if any(a&(1<<i) for a in nonlinear))
    sigma=tuple(phase(nonlinear,k)[expand(z,T)] for z in range(1<<len(T)))
    h=phase_comparison(f,T,sigma)
    mf=metrics(f);mh=metrics(h)
    phase_metrics=metrics(phase(nonlinear,k))
    assert mf[3][k:]==mh[3][k:]
    Jy=sum(mh[3][k:],F(0))
    nonnegative(constant(K0*Jy)-mf[4],'prior affine-fibre base bound')
    weighted=constant(K0*Jy)
    r=max((a.bit_count() for a in nonlinear),default=0)
    for i in T:
        Di=derivative(nonlinear,i);s=max(a.bit_count() for a in Di)
        assert s>=1
        ai=1-2*phase_metrics[2][i]
        bi=F(sum(1 if not ((a>>i)&1) else -1 for a in pi),len(pi))
        assert 1-2*mh[2][i]==ai*bi
        assert mh[3][i]>=F(1,1<<s)
        weighted=weighted+binary_entropy(F(1,1<<s))*((1<<s)*mh[3][i])
        COUNTS['exact_tag_derivative_gap_checks']+=1
    nonnegative(weighted-mh[4],'derivative-degree weighted tag bound')
    if r>=2:
        coeff=binary_entropy(F(1,1<<(r-1)))*(1<<(r-1))
        if coeff.interval()[1]<=K0:
            nonnegative(constant(K0*sum(mh[3],F(0)))-mh[4],'unchanged tag constant')
        else:
            assert coeff.interval()[0]>=K0
            nonnegative(coeff*sum(mh[3],F(0))-mh[4],'degree-dependent tag constant')
    else:
        assert (mf[4]-mh[4]).zero()
    COUNTS['affine_fibre_tag_cases']+=1
    COUNTS['tag_actual_degree_'+str(r)]+=1
    COUNTS['constant_four_cases' if K0==4 else 'constant_12_04_core_cases']+=1

def run():
    rng=random.Random(SEED)
    for n in range(4):
        for f in all_boolean(n):
            for mask in range(1<<n):
                E=tuple(i for i in range(n) if mask&(1<<i))
                for sigma in all_boolean(len(E)):
                    phase_comparison(f,E,sigma)
                    COUNTS['exhaustive_phase_comparison_cases']+=1
    for k in range(2,8):
        for m in range(1,min(5,10-k)+1):
            for rep in range(10):
                pi=affine_partition_labels(m,k,rng)
                quadratic=(rep%2==0)
                g,K0=core_g(m,rng,quadratic)
                r=min(k,2+rep%6)
                mons=[a for a in range(1<<k) if a.bit_count()<=r]
                Q=frozenset(rng.sample(mons,min(len(mons),1+rep)))
                tag_case(k,m,pi,g,Q,K0)
    for r in range(2,12):
        k=r;m=1;pi=(0,1<<(k-1));g=(1,1)
        Q=frozenset({(1<<k)-1})
        tag_case(k,m,pi,g,Q,F(301,25))
        COUNTS['high_degree_tag_witnesses']+=1
    constants=[]
    for s in (1,2,3,10,11):
        expr=binary_entropy(F(1,1<<s))*(1<<s)
        lo,hi=expr.interval()
        constants.append({'derivative_degree':s,'lower':str(lo),'upper':str(hi),
                          'below_four_certified':hi<4,'below_12_04_certified':hi<F(301,25)})
        if s==2:assert hi<4
        if s==10:assert hi<F(301,25)
        if s==11:assert lo>F(301,25)
    here=Path(__file__).parent
    return {'status':'PASS','full_FEI_proved':False,'independent_audit':False,
            'formal_verification':False,'publication_priority_cleared':False,
            'seed':SEED,'counts':dict(sorted(COUNTS.items())),
            'arithmetic':'exact integer Walsh, exact rational influences, prime-log identities and outward rational logarithm enclosures',
            'degree_constants':constants,
            'source_sha256':{name:hashlib.sha256((here/name).read_bytes()).hexdigest()
                             for name in ('verify_tag_phase.py','verify_polynomial_symmetry.py')},
            'scope':'Parameter families overlap. Finite checks do not prove all-dimensional statements or recursive closure.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    out=run();text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text,encoding='utf-8')
    print(text)
