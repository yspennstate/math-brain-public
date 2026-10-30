#!/usr/bin/env python3
"""Exact finite checks for the FEI template-collapse continuation.

Universal statements are proved in REPORT.md. The scalar entropy inequality
uses the exact interval certificate here plus the analytic tail/Lipschitz proof.
No floating-point diagnostic is a substitute for a proof or a rigorous bound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
import math
from pathlib import Path
import numpy as np


def fwht(x: np.ndarray) -> np.ndarray:
    a = np.asarray(x, dtype=np.int64).copy()
    N = a.shape[-1]
    if N == 0 or N & (N-1):
        raise ValueError('last dimension must be a positive power of two')
    h = 1
    while h < N:
        v = a.reshape(*a.shape[:-1], -1, 2, h)
        left, right = v[..., 0, :].copy(), v[..., 1, :].copy()
        v[..., 0, :], v[..., 1, :] = left+right, left-right
        h *= 2
    return a


def rank2(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            k = row.bit_length()-1
            if k in pivots:
                row ^= pivots[k]
            else:
                pivots[k] = row
                break
    return len(pivots)


def template_data(n: int):
    N = 1 << n
    edges = list(combinations(range(n), 2))
    monomials = [np.ones(N, dtype=np.int64)]
    monomials += [np.array([(s >> i) & 1 for s in range(N)], dtype=np.int64)
                  for i in range(n)]
    monomials += [monomials[1+i]*monomials[1+j] for i,j in edges]
    phases = np.zeros((1, N), dtype=np.int64)
    for term in monomials:
        phases = np.concatenate((phases, phases ^ term), axis=0)
    signs = 1-2*phases
    ranks = []
    for code in range(len(signs)):
        rows = [0]*n
        for k,(i,j) in enumerate(edges):
            if code >> (n+1+k) & 1:
                rows[i] ^= 1 << j
                rows[j] ^= 1 << i
        r = rank2(rows)
        assert r % 2 == 0
        ranks.append(r)
    return signs, np.array(ranks, dtype=np.int64)


def exact_templates() -> dict:
    rows = []
    total_pairs = total_quadratics = 0
    for n in range(5):
        N = 1 << n
        signs, ranks = template_data(n)
        transforms = fwht(signs)
        for i,r in enumerate(ranks):
            expected_amp = N // (1 << (int(r)//2))
            assert np.count_nonzero(transforms[i]) == (1 << int(r))
            assert np.all((transforms[i] == 0) | (np.abs(transforms[i]) == expected_amp))
        ids = np.arange(1 << N, dtype=np.uint32)
        values = 1-2*((ids[:,None] >> np.arange(N, dtype=np.uint32)) & 1).astype(np.int64)
        W = fwht(values)
        b = np.array([1 << (int(r)//2) for r in ranks], dtype=np.int64)
        pair_count = 0
        # All Boolean truth tables and all quadratic templates through n=4.
        for start in range(0, len(W), 128):
            ws = W[start:start+128]
            L = np.abs(ws).sum(axis=1)
            A = ws @ signs.T
            # A/N is the phase correlation. b is the quadratic spectral l1 norm.
            assert np.all(np.abs(A) <= N*b)
            twice_bad = L[:,None]-A
            assert np.all(twice_bad >= 0)
            assert np.all(twice_bad % 2 == 0)
            costs = b*(N+twice_bad)
            assert np.all(costs >= L[:,None])
            assert np.all(costs.min(axis=1) == L)
            pair_count += ws.shape[0]*len(signs)
        total_pairs += pair_count
        total_quadratics += len(signs)
        rows.append({'n':n,'boolean_truth_tables':len(values),
                     'quadratic_templates':len(signs),'exact_pairs':pair_count})
    return {'status':'PASS','all_quadratic_phase_checks':total_quadratics,
            'all_boolean_template_pairs':total_pairs,'by_dimension':rows,
            'arithmetic':'int64; largest comparison is safely below 2^63'}


def fibre_collapse_checks() -> dict:
    count = 0
    for n in range(4):
        N = 1 << n
        phases, ranks = template_data(n)
        ids = np.arange(1 << N, dtype=np.uint32)
        W = fwht(1-2*((ids[:,None] >> np.arange(N, dtype=np.uint32)) & 1).astype(np.int64))
        L = np.abs(W).sum(axis=1)
        edges = list(combinations(range(n), 2))
        for code, sigma in enumerate(phases):
            polar = [0]*n
            for e,(i,j) in enumerate(edges):
                if code >> (1+n+e) & 1:
                    polar[i] ^= 1 << j
                    polar[j] ^= 1 << i
            labels = [sum(((s & row).bit_count() % 2) << i
                          for i,row in enumerate(polar)) for s in range(N)]
            cells = sorted(set(labels))
            assert len(cells) == 1 << int(ranks[code])
            G = np.zeros((len(W),len(cells)),dtype=np.int64)
            B = np.zeros_like(G)
            for j,t in enumerate(cells):
                inds = [s for s,v in enumerate(labels) if v == t]
                signed = W[:,inds]*sigma[inds]
                G[:,j] = np.maximum(signed,0).sum(axis=1)
                B[:,j] = np.maximum(-signed,0).sum(axis=1)
            assert np.all(((G-B)**2).sum(axis=1) == N*N)
            C_num = ((G+B)**2).sum(axis=1)
            assert np.all(C_num == N*N+4*(G*B).sum(axis=1))
            assert np.all(len(cells)*C_num >= L*L)
            if ranks[code] == 0:
                assert np.all(C_num == L*L)
            count += len(W)
    return {'status':'PASS','exact_boolean_template_fibre_instances':count,
            'scope':'all Boolean functions and quadratic templates through three variables',
            'identities':['sum(G-B)^2=1','C=1+4 sum G*B','2^r C >= M^2'],
            'normalization':'integer numerators; common Walsh denominator 2^n'}


def ln_series(y: F, terms: int = 40) -> tuple[F,F]:
    if not F(1) <= y <= F(2):
        raise ValueError('series argument outside [1,2]')
    z = (y-1)/(y+1)
    z2, term, val = z*z, z, F(0)
    for k in range(terms):
        val += 2*term/(2*k+1)
        term *= z2
    error = 2*term/((2*terms+1)*(1-z2))
    return val, val+error


LN2 = ln_series(F(2))
assert LN2[0] > F(2,3)
assert LN2[1] < F(3,4)


@lru_cache(None)
def log2_interval(x: F) -> tuple[F,F]:
    if x <= 0:
        raise ValueError('logarithm requires x>0')
    y, k = x, 0
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1
    lo,hi = ln_series(y)
    # log2 x = k + ln(y)/ln(2); numerator is nonnegative.
    return F(k)+lo/LN2[1], F(k)+hi/LN2[0]


@lru_cache(None)
def entropy_interval(p: F) -> tuple[F,F]:
    if not 0 <= p <= 1:
        raise ValueError('probability out of range')
    if p in (0,1):
        return F(0),F(0)
    a,b = log2_interval(p)
    c,d = log2_interval(1-p)
    return -p*b-(1-p)*d, -p*a-(1-p)*c


def scalar_certificate() -> dict:
    nodes = []
    for k in range(32,257):
        t = F(k,256)
        x = t*t/(1+t*t)
        q = (1+t)*(1+t)/(2*(1+t*t))
        # q=1/2+sqrt(x(1-x)), certified by an exact squared identity.
        assert (q-F(1,2))**2 == x*(1-x)
        h_lo,h_hi = entropy_interval(x)
        q_lo,q_hi = entropy_interval(q)
        lo = F(9,4)*x-1+h_lo/8+q_lo
        hi = F(9,4)*x-1+h_hi/8+q_hi
        nodes.append((x,lo,hi))
    minimum = None
    for left,right in zip(nodes,nodes[1:]):
        certified = min(left[1],right[1])-F(3,2)*(right[0]-left[0])
        assert certified > F(1,1000)
        minimum = certified if minimum is None else min(minimum,certified)
    assert nodes[0][0] == F(1,65)
    assert nodes[-1][0] == F(1,2)
    return {'status':'PASS','rational_nodes':len(nodes),'closed_cells':len(nodes)-1,
            'parameterization':'t=k/256, k=32,...,256; x=t^2/(1+t^2)',
            'certified_interval':['1/65','1/2'],
            'each_cell_lower_bound_strictly_greater_than':'1/1000',
            'minimum_lower_bound_float_diagnostic':float(minimum),
            'ln2_certified_interval_contained_in':['2/3','3/4'],
            'series_terms':40,
            'outside_grid_proof':'analytic tail on [0,1/64], trivial bound on [1/2,1]',
            'Lipschitz_constant_exact':3,
            'theorem':'R(x)<=h2(x)/8+9*x/4 for all x in [0,1]'}


def tribes_checks() -> dict:
    direct=[]
    for w in (1,2,3):
        s=1 << w
        n=w*s
        # w=3 has 24 variables. Use a product coefficient construction, then
        # independently materialize small w=1,2 truth tables only.
        delta=F(1,s); q=1-delta; u=q**s
        M=1+2*(2*q)**s-4*u
        I=2*w*q**(s-1)
        assert u < F(1,2)
        assert u >= F(1,4)
        assert I <= w
        assert M >= 1 << (s-1)
        if w<=2:
            N=1 << n
            values=np.empty(N,dtype=np.int64)
            mask=(1 << w)-1
            for x in range(N):
                none=all(((x >> (j*w)) & mask) != mask for j in range(s))
                values[x]=1 if none else -1
            W=fwht(values)
            actualM=F(int(np.abs(W).sum()),N)
            actualI=F(sum(int(a*a)*i.bit_count() for i,a in enumerate(W)),N*N)
            assert actualM==M and actualI==I
            v=4*u*(1-u)
            # Entropy equality is checked using certified intervals independently.
            lo=hi=F(0)
            for a in W:
                if a:
                    p=F(int(a*a),N*N)
                    pl,ph=log2_interval(p)
                    lo-=p*ph; hi-=p*pl
            hp=entropy_interval(delta); hu=entropy_interval(u); hv=entropy_interval(v)
            ls=log2_interval(F(s-1))
            beta=(hp[0]+delta*ls[0],hp[1]+delta*ls[1])
            expected=(hv[0]+4*u*(s*beta[0]-hu[1]),
                      hv[1]+4*u*(s*beta[1]-hu[0]))
            assert max(lo,expected[0])<=min(hi,expected[1])
            assert hi-lo < F(1,10**25)
            # Balanced lift has concatenated spectra, exact influence shift one.
            WF=fwht(np.concatenate((values,-values)))
            assert np.count_nonzero(WF[:N])==0
            assert np.array_equal(WF[N:],2*W)
            IF=F(sum(int(a*a)*i.bit_count() for i,a in enumerate(WF)),4*N*N)
            assert IF==I+1
            direct.append({'w':w,'tribes':s,'variables':n,'balanced_lift_variables':n+1,
                           'M_exact':str(M),'I_exact':str(I),'balanced_I_exact':str(I+1),
                           'entropy_float_diagnostic':float((lo+hi)/2),
                           'scope':'full integer Walsh transform and rational log intervals'})
    examples=[]
    for w in (2,4,6,10,16):
        s=1 << w
        logq=math.log1p(-1/s)
        u=math.exp(s*logq)
        If=1+2*w*math.exp((s-1)*logq)
        h=lambda x: -x*math.log2(x)-(1-x)*math.log2(1-x)
        hb=(2/s-1)*logq/math.log(2)+2*w/s
        H=h(4*u*(1-u))+4*u*(s*hb-h(u))
        # lower bound is exact rational; no need to compute a huge M.
        low=F(2*(s-1),w+1)
        examples.append({'w':w,'balanced_variables':w*s+1,
                         'coarse_cost_over_I_lower_bound_exact':str(low),
                         'actual_H_over_I_float_diagnostic':H/If})
    return {'status':'PASS','direct_checks':direct,'analytic_family_examples':examples,
            'all_w_claim':'proved analytically; examples do not enumerate large truth tables',
            'limit_H_over_I':4}


def majority_checks() -> dict:
    M, I, H, support = 1, F(1), F(0), 1
    table = []
    for d in range(1,9):
        M = (3*M+M**3)//2
        support = 3*support+support**3
        assert support >= (1 << (2*3**(d-1)))
        I = F(3,2)*I
        H = 2+F(3,2)*H
        exponent = (3**(d-1)+1)//2
        assert M >= (1 << exponent)
        assert H == 4*(I-1)
        table.append({'depth':d,'variables':3**d,'I_exact':str(I),'H_exact':str(H),
                      '2_log_M_lower_bound_exact':2*exponent,
                      'minimum_exact_phase_rank_lower_bound':2*3**(d-1),
                      'coarse_cost_over_I_lower_bound_exact':str(F(2*exponent)/I),
                      'M_bit_length':M.bit_length()})
    # Direct independent 9-bit two-level majority, including its quadratic signs.
    values=[]
    for x in range(512):
        bits=[1-2*((x >> i) & 1) for i in range(9)]
        inner=[1 if sum(bits[3*j:3*j+3])>0 else -1 for j in range(3)]
        values.append(1 if sum(inner)>0 else -1)
    W=fwht(np.array(values,dtype=np.int64))
    assert int(np.abs(W).sum()) == 7*512
    for s,a in enumerate(W):
        if a:
            k=s.bit_count()
            assert k % 2 == 1
            assert (a>0) == ((k*(k-1)//2) % 2 == 0)
    Inum=sum(int(a*a)*s.bit_count() for s,a in enumerate(W))
    Hnum=0
    for a in W:
        if a:
            z=abs(int(a))
            assert z & (z-1) == 0
            Hnum+=int(a*a)*2*(9-(z.bit_length()-1))
    assert F(Inum,512**2)==F(9,4)
    assert F(Hnum,512**2)==5
    return {'status':'PASS','exact_recursive_examples':table,
            'direct_nine_bit_case':{'M':7,'I':'9/4','H':5,'support':int(np.count_nonzero(W)),
                                    'phase':'sum_{i<j} s_i*s_j'},
            'scope':'all-depth claim is analytic; only nine-bit truth table is materialized here',
            'novelty':'recursive majority is inherited; its use refutes the new global phase-budget target'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--part',choices=['all','templates','fibres','scalar','tribes','majority'],default='all')
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    funcs={'templates':exact_templates,'fibres':fibre_collapse_checks,'scalar':scalar_certificate,'tribes':tribes_checks,'majority':majority_checks}
    work=funcs if args.part=='all' else {args.part:funcs[args.part]}
    result={'schema_version':1,'full_FEI':'OPEN_NOT_PROVED',
            'verification_kind':'self-check and exact scalar interval certificate, not independent audit',
            'checks':{name:fun() for name,fun in work.items()}}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text,encoding='utf-8')
    print(text)

if __name__=='__main__':
    main()
