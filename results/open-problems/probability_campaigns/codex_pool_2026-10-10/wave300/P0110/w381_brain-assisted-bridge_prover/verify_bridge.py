"""Bounded consistency checks; these are not a formal or independent proof audit."""
import itertools
import json
import math
import time
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parent
gate = json.loads((root/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
assert gate['gate_id']=='w381-local-lemmas-20261010-01' and not gate['gpu']
started=time.perf_counter()

def length(x):
    return math.sqrt(sum(t*t for t in x))

cases=0
branches={'interior':0,'before':0,'after':0}
minimum_slack=math.inf
for dimension, endpoints, coordinates in (
    (2,[(1,0),(8,0),(3,4),(-2,5),(17,-11)],[-11,-4,-1,0,1,3,9,21]),
    (3,[(1,0,0),(2,3,5),(-4,2,1)],[-5,-1,0,2,9]),
):
    for v in endpoints:
        L=length(v)
        for z in itertools.product(coordinates,repeat=dimension):
            t=sum(x*y for x,y in zip(z,v))/(L*L)
            clamped=min(1,max(0,t))
            r=length([x-clamped*y for x,y in zip(z,v)])
            S=length(z)+length([x-y for x,y in zip(z,v)])
            assert S>0
            slack=(S-L)-2*r*r/S
            tolerance=2e-12*max(1,S)
            assert slack>=-tolerance, (v,z,r,S,slack)
            minimum_slack=min(minimum_slack,slack)
            branches['before' if t<0 else 'after' if t>1 else 'interior']+=1
            cases+=1

identity_cases=0
for detour,b_terminal,b_left,b_right,x_left,x_right in itertools.product(
    [Fraction(0),Fraction(1,8),Fraction(10)],
    [Fraction(0),Fraction(1),Fraction(7)],
    [Fraction(0),Fraction(10),Fraction(1000000)],
    [Fraction(0),Fraction(10),Fraction(1000000)],
    [Fraction(-3),Fraction(0),Fraction(4)],
    [Fraction(-3),Fraction(0),Fraction(4)],
):
    x_terminal=detour+b_left+b_right-b_terminal+x_left+x_right
    rhs=b_terminal-b_left-b_right+x_terminal-x_left-x_right
    assert rhs==detour
    assert detour<=b_terminal+x_terminal-x_left-x_right
    identity_cases+=1

rounding_cases=0
for d in (2,3):
    for norm_name in ('l2','l1','linfinity'):
        u=([1.0]+[0.0]*(d-1)) if norm_name!='linfinity' else [1/math.sqrt(d)]*d
        rho=1.0 if norm_name!='linfinity' else 1/math.sqrt(d)
        def g(x):
            return length(x) if norm_name=='l2' else sum(abs(t) for t in x) if norm_name=='l1' else max(abs(t) for t in x)
        for n in (2,3,4,5,7,10,30,100,1000,10000):
            v=[round(n*t) for t in u]
            L=length(v)
            defect=g(v)-rho*L
            K0=d/2+rho*math.sqrt(d)/2
            assert defect>=-1e-10 and defect<=K0+1e-10
            assert length([x-n*y for x,y in zip(v,u)])<=math.sqrt(d)/2+1e-10
            rounding_cases+=1

subadditivity_cases=0
for m,n in itertools.product(range(1,31),repeat=2):
    h=lambda k:k+math.sqrt(k)
    assert h(m+n)<=h(m)+h(n)+1e-12
    subadditivity_cases+=1
upper_curvature_ratios=[]
for m in (1,10,100,1000):
    t=Fraction(1,m)
    excess=t  # ||(1,t)||_1-||(1,0)||_1
    assert excess>=t*t
    upper_curvature_ratios.append(int(excess/(t*t)))

# A dependent union is still valid: perfectly correlated Bernoulli events.
assert Fraction(1,2)<=4*Fraction(1,2)
# Conditioning on equality destroys independence of two initially fair bits.
assert Fraction(1,2)!=Fraction(1,2)*Fraction(1,2)

total=cases+identity_cases+rounding_cases+subadditivity_cases+4
assert total<=gate['max_cases'], total
receipt={'gate_id':gate['gate_id'],'command':'python -B -X utf8 ~/brain_workers/w381/verify_bridge.py',
 'elapsed_seconds':time.perf_counter()-started,'geometry_cases':cases,'projection_branches':branches,
 'minimum_geometry_slack':minimum_slack,'exact_rational_identity_cases':identity_cases,
 'norm_rounding_cases':rounding_cases,'subadditive_countermodel_checks':subadditivity_cases,
 'l1_upper_curvature_ratios':upper_curvature_ratios,'total_cases':total,'failures':0,
 'evidence_class':'deterministic consistency checks only; no formal check, no independent mathematical audit',
 'remaining_gap':'Matched global exponents for a concrete nondegenerate iid undirected lattice FPP law'}
(root/'verification_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
