#!/usr/bin/env python3
"""Exact finite checks of the non-Boolean all-direction-capacity obstruction.
Python 3.10+, NumPy via the included verify_packets helper. Not full FEI.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from itertools import combinations
from pathlib import Path
import hashlib, json, random
from verify_packets import pair, pair_expr, expr_add, log2

SEED=2026092071

def parity(t): return t.bit_count()&1

def make(q:int,w:int):
    assert q>=4 and q&(q-1)==0
    K=q*q;m=3*K//4;n=2*q*w+m
    centres=[];a={}
    for x in range(q):
        U=((1<<w)-1)<<(x*w)
        for y in range(q):
            V=((1<<w)-1)<<((q+y)*w)
            c=U|V;z=x*q+y;centres.append(c);a[c]=q//2
            for i in range(1,m+1):
                a[c|(1<<(2*q*w+i-1))]=1-2*parity(z&i)
    return K,m,n,centres,a

def square(a):
    result=defaultdict(int);items=list(a.items())
    for j,(s,u) in enumerate(items):
        result[0]+=u*u
        for t,v in items[j+1:]: result[s^t]+=2*u*v
    return {s:u for s,u in result.items() if u}

def sparse_checks():
    rows=[];rng=random.Random(SEED);capacities=edges=restrictions=0
    for q,w in ((4,1),(4,2),(4,3),(4,5),(8,1)):
        K,m,n,centres,a=make(q,w)
        assert sum(u*u for u in a.values())==K*K
        sq=square(a)
        assert sq[0]==K*K
        assert all(s==0 or s.bit_count()>=2*w for s in sq)
        assert all(s==0 or (s&((1<<(2*q*w))-1)).bit_count()>=2*w for s in sq)
        fourth=F(sum(u*u for u in sq.values()),K**4)
        assert 1<fourth<=9
        I=[]
        for j in range(n):
            count=sum(u*u for s,u in a.items() if (s>>j)&1)
            expected=K*K//(q if j<2*q*w else K)
            assert count==expected
            I.append(F(count,K*K))
            for s,u in a.items():
                capacity=I[-1] if (s>>j)&1 else 1-I[-1]
                assert F(abs(u),K)<=capacity
                capacities+=1
        assert sum(I)==2*w+F(3,4)
        # Direct selected-edge expression and absence of control erasure edges.
        edge_expr={};cnt=0
        for s,u in a.items():
            for j in range(n):
                if (s>>j)&1:continue
                t=s|(1<<j)
                if t not in a:continue
                assert j>=2*q*w
                edge_expr=expr_add(edge_expr,pair_expr(abs(u),abs(a[t])),F(1,K*K))
                cnt+=1
        assert cnt==K*m
        expected=expr_add({},pair_expr(q//2,1),F(3,4))
        assert edge_expr==expected
        edges+=cnt
        # All-plus controls give q/2 for EVERY data assignment: cancellation
        # is verified coefficientwise in the restricted data polynomial.
        restricted=defaultdict(int)
        for s,u in a.items():restricted[s>>(2*q*w)]+=u
        restricted={s:u for s,u in restricted.items() if u}
        assert restricted=={0:K*q//2}
        assert F(K*q//2,K)>=2
        # Include every one-coordinate assignment and seeded deeper assignments.
        testsets=[()] + [(j,) for j in range(n)]
        testsets += [tuple(sorted(rng.sample(range(n),rng.randrange(0,2*w)))) for _ in range(70)]
        for js in testsets:
            mask=sum(1<<j for j in js)
            for rep in range(2 if js else 1):
                b=sum((rng.randrange(2)<<j) for j in js)
                num=sum(u*(1-2*parity(s&b)) for s,u in sq.items() if not s&~mask)
                assert num==K*K
                restrictions+=1
        lo,hi=pair(q//2,1)
        entropy=(F(3,4)*lo,F(3,4)*hi)
        assert entropy[0]>0
        rows.append({'q':q,'w':w,'physical_variables':n,'nonzero_coefficients':len(a),
                     'nonzero_square_coefficients':len(sq),'erasure_edges':cnt,
                     'exact_energy':str(sum(I)),'exact_fourth_moment':str(fourth),
                     'all_plus_control_value':str(F(q,2))})
    return {'cases':rows,'physical_coefficient_capacity_assertions':capacities,
            'exact_positive_erasure_edges':edges,'restriction_assignments':restrictions}

def direction_types():
    out=[]
    for q in (4,8,16):
        K=q*q;m=3*K//4;centres=leaves=0
        centre_min=None;leaf_min=None
        for ka in range(q+1):
            signs_a=([1] if ka<q else [])+([-1] if ka>0 else [])
            for kb in range(q+1):
                signs_b=([1] if kb<q else [])+([-1] if kb>0 else [])
                for t in range(m+1):
                    c=(q-2*ka)*(q-2*kb)*(K-2*t)
                    signs_d=([1] if t<m else [])+([-1] if t>0 else [])
                    for sa in signs_a:
                        for sb in signs_b:
                            num=K*K+sa*sb*c
                            assert num>=2*K*K//q
                            assert num>=K*q # coefficient 1/(2q)
                            centre_min=num if centre_min is None else min(centre_min,num)
                            centres+=1
                            for di in signs_d:
                                num=K*K+sa*sb*di*c
                                assert num>=2*K # coefficient 1/K
                                leaf_min=num if leaf_min is None else min(leaf_min,num)
                                leaves+=1
        out.append({'q':q,'centre_types':centres,'leaf_types':leaves,
                    'minimum_centre_agreement_mass':str(F(centre_min,2*K*K)),
                    'minimum_leaf_agreement_mass':str(F(leaf_min,2*K*K)),
                    'scope':'All combinatorial direction types and feasible target signs; every physical direction reduces to such a type.'})
    return out

def parameters():
    rows=[]
    for k,w in ((2,1),(4,1),(16,2),(64,4),(256,8)):
        K=1<<(2*k)
        # The positive second entropy term gives a strict lower bound.
        low=F(3*(2*k-2),8*w+3)
        assert low>0
        rows.append({'log2_K':2*k,'w':w,'strict_B_over_energy_lower':str(low),
                    'exact_square_cancellation_order':2*w-1,
                    'truth_table_enumerated':False})
    return rows


def homogeneous_pair(r:F,s:F):
    if not r or not s:return F(0),F(0)
    a,b=log2(1+s/r);c,d=log2(1+r/s)
    return r*a+s*c,r*b+s*d

def projection_hierarchy():
    rows=[];codimensions=0
    for n in (16,32,64,128,256,1024):
        eps=F(2,n);base=eps/F(2**n)
        p2=base+(1-eps)/(4*comb(n,2))
        p3=base+3*(1-eps)/(4*comb(n,3))
        maximum=max(base,p2,p3)
        assert maximum<=eps*eps/4
        norm=base*2**n+(p2-base)*comb(n,2)+(p3-base)*comb(n,3)
        assert norm==1
        energy=eps*n/2+(1-eps)*F(11,4)
        assert energy==F(15,4)-F(11,2*n)<F(15,4)
        for k in range(1,n+1):
            cellmass=eps/F(2**k)
            rhs=2**(k-1)*cellmass
            assert rhs==eps/2 and maximum<=rhs*rhs
            codimensions+=1
        loglo,loghi=log2(F(n-2,9))
        lower=(1-eps)*F(3,5)*loglo
        assert lower>0
        record={'n':n,'exact_energy':str(energy),
                'maximal_atom_bound':'1/n^2',
                'certified_B_over_energy_lower_floor':int(lower),
                'affine_subspaces_enumerated':False,'truth_table_enumerated':False}
        if n<=128:
            full_lo=full_hi=eps*n
            for k in (1,2,3):
                r=p2 if k==2 else p3 if k==3 else base
                t=p2 if k+1==2 else p3 if k+1==3 else base
                lo,hi=homogeneous_pair(r,t);edges=comb(n,k)*(n-k)
                full_lo+=edges*(lo-2*base);full_hi+=edges*(hi-2*base)
            claimed=(1-eps)*F(9,4)*loghi
            assert full_lo>claimed
            record['full_erasure_interval_verified']=True
        rows.append(record)
    return {'cases':rows,'codimension_certificates':codimensions,
            'scope':'Exact level and uniform-cell formulas. The actual signed square-convolution constraints and dyadic amplitudes are NOT asserted for these functions.'}

def main():
    out={'status':'PASS','date':'2026-09-20','seed':SEED,
         'full_FEI_proved':False,'Boolean_counterexample':False,
         'independent_audit':False,'formal_proof_assistant_used':False,
         'sparse':sparse_checks(),'direction_types':direction_types(),
         'analytic_parameter_examples':parameters(),'projection_hierarchy':projection_hierarchy()}
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_name('capacity_verification.json').write_text(text)
    print(text,end='')
if __name__=='__main__': main()
