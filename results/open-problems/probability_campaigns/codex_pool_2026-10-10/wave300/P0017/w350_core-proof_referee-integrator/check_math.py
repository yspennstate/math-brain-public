"""Exact finite reproductions; these are not a proof of KLS."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import combinations, product
import json
import random
import time

ROOT=Path(__file__).resolve().parent
started=time.monotonic()
gate=json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
deadline=gate['limits']['cpu_arithmetic_deadline_seconds']
counts={'sharpness_pairs':0,'sharpness_components':0,'random_block_symmetric_tensors':0,'brute_binary_tensors':0,'gaussian_channel_calibrations':0,'wick_raw_moment_dimensions':0,'missing_second_symmetry_counterexamples':0}
rng=random.Random(350)

def checkpoint():
    if time.monotonic()-started>deadline: raise RuntimeError('Fresh gate deadline exceeded; no partial PASS is allowed')

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def projected_component(values,p,q,k,l):
    # Average actual choices of the p original first-block positions within q positions.
    return sum((F(choose(k,r)*choose(q-k,p-r),comb(q,p))*values[r][k+l-r] for r in range(p+1) if 0<=k+l-r<=q),F(0))

for p in range(1,6):
    for q in range(p,10):
        checkpoint()
        c=comb(q,p)
        values=[[F((-1)**r,comb(q,p-r)) if s==p-r else F(0) for s in range(q+1)] for r in range(p+1)]
        src=sum((comb(p,r)*comb(q,s)*values[r][s]**2 for r in range(p+1) for s in range(q+1)),F(0))
        dst=F(0)
        for k in range(q+1):
            for l in range(p+1):
                actual=projected_component(values,p,q,k,l)
                expected=F((-1)**k,c*comb(q,k)) if k+l==p else F(0)
                assert actual==expected,(p,q,k,l,actual,expected)
                counts['sharpness_components']+=1
                dst+=comb(q,k)*comb(p,l)*actual**2
        assert src>0 and src==c*c*dst,(p,q,src,dst)
        counts['sharpness_pairs']+=1
        for _ in range(4):
            v=[[F(rng.randrange(-9,10),rng.randrange(1,5)) for s in range(q+1)] for r in range(p+1)]
            a=sum((comb(p,r)*comb(q,s)*v[r][s]**2 for r in range(p+1) for s in range(q+1)),F(0))
            b=sum((comb(q,k)*comb(p,l)*projected_component(v,p,q,k,l)**2 for k in range(q+1) for l in range(p+1)),F(0))
            assert a<=c*c*b,(p,q,a,b)
            counts['random_block_symmetric_tensors']+=1

# A separate coordinate enumeration uses subsets rather than the grouped formula.
for p in range(1,4):
    for q in range(p,5):
        if p+q>7: continue
        v=[[F(rng.randrange(-4,5)) for s in range(q+1)] for r in range(p+1)]
        a=b=F(0)
        for word in product((0,1),repeat=p+q):
            a+=v[sum(word[:p])][sum(word[p:])]**2
            avg=F(0)
            for selected in combinations(range(q),p):
                r=sum(word[i] for i in selected)
                s=sum(word)-r
                avg+=v[r][s]/comb(q,p)
            b+=avg**2
        assert a<=comb(q,p)**2*b
        counts['brute_binary_tensors']+=1
        checkpoint()

# Explicit p=1,q=2 tensor antisymmetric in positions 1,2, with position 3=e1.
bad={(0,1,0):F(1),(1,0,0):F(-1)}
bad_norm=sum((x*x for x in bad.values()),F(0))
bad_projected=sum(((bad.get(w,F(0))+bad.get((w[1],w[0],w[2]),F(0)))/2)**2 for w in product((0,1),repeat=3))
assert bad_norm==2 and bad_projected==0
counts['missing_second_symmetry_counterexamples']=1

for numerator in range(1,11):
    for denominator in range(1,11):
        t=F(numerator,denominator)
        retention=1/(1+t)
        explained=t/(1+t)
        assert retention+explained==1
        # Linear Gaussian witness; no square-root floating arithmetic is needed.
        assert 1/(t*retention)==1+1/t
        counts['gaussian_channel_calibrations']+=1

for n in range(1,17):
    value=0
    for i,j,k in product(range(n),repeat=3):
        x=int(i==0 and j==k)+int(j==0 and i==k)+int(k==0 and i==j)
        value+=x*x
    assert value==3*n+6,(n,value)
    counts['wick_raw_moment_dimensions']+=1

checkpoint()
result={'status':'PASS','command':'python -X utf8 check_math.py','counts':counts,'elapsed_seconds':round(time.monotonic()-started,6),'gate':'COMPUTE_GATE.json','trust':'Exact Python rational arithmetic; no formal proof assistant, no full-target proof.'}
out=ROOT/'measurements'
out.mkdir(exist_ok=True)
(out/'math_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result),flush=True)
