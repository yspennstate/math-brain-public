"""Independent exact admission check; domain frozen in out/FROZEN_SPEC.json."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json, time

run = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0
def ck(t):
    global checks
    checks += 1
    assert t, checks

def gate(x):
    return 2*int(all(x))-1

def measure(x,p):
    w=F(1)
    for b,q in zip(x,p): w *= q if b else 1-q
    return w

def spectrum(p):
    # E[f prod (X-p)]/(prod p(1-p)) is the multilinear coefficient.
    active=[i for i,q in enumerate(p) if 0<q<1]
    out={}
    for bits in product([0,1],repeat=len(active)):
        s=tuple(i for i,b in zip(active,bits) if b)
        moment=F(0)
        for x in product([0,1],repeat=3):
            z=F(gate(x))*measure(x,p)
            for i in s:z*=x[i]-p[i]
            moment+=z
        scale=F(1)
        for i in s:scale*=p[i]*(1-p[i])
        out[s]=moment*moment/scale
    ck(sum(out.values())==1)
    return out

grid=list(product([F(1,4),F(1,2),F(3,4)],repeat=3))
corners=list(product([F(0),F(1)],repeat=3))
faces=[]
for i in range(3):
    for b in [F(0),F(1)]:
        p=[F(1,3)]*3;p[i]=b;faces.append(tuple(p))
rows=[]
for case,p in enumerate(grid+corners+faces):
    P=spectrum(p)
    row={'biases':list(map(str,p)), 'spectrum':{str(s):str(w) for s,w in P.items()},'pairs':[]}
    if case<len(grid):
        full=P[(0,1,2)];ck(full>0)
        for pair in combinations(range(3),2):
            k=next(i for i in range(3) if i not in pair)
            values=[]
            for b in [0,1]:
                z=0
                for a in product([0,1],repeat=2):
                    x=[0]*3;x[k]=b
                    for i,bit in zip(pair,a):x[i]=bit
                    z+=(-1)**(2-sum(a))*gate(x)
                ck(z%2==0);values.append(F(z,2))
            ck(values==[0,1])
            mean=(1-p[k])*values[0]+p[k]*values[1]
            variance=(1-p[k])*(values[0]-mean)**2+p[k]*(values[1]-mean)**2
            vpair=F(1)
            for i in pair:vpair*=4*p[i]*(1-p[i])
            ck(mean==p[k]);ck(variance==mean*(1-mean))
            ck(variance==4*full/vpair)
            ck(P[pair]==vpair*mean*mean/4)
            # Any retained fraction a<1 of the only strict superset fails
            # the minimum variance of an integer-valued variable of this mean.
            for a in [F(0),F(1,3),F(1,2),F(2,3),F(1)]:
                retained=4*a*full/vpair
                ck((retained>=mean*(1-mean))==(a==1))
            # Exact rational log lower bound ln(1/m)>2(1-m)/(1+m)>0.
            loglower=2*(1-mean)/(1+mean)
            residual_lower=vpair*mean*mean*loglower/2
            ck(residual_lower>0)
            row['pairs'].append({'pair':pair,'mean':str(mean),'variance':str(variance),'required_owner_fraction':'1','residual_positive_lower_bound':str(residual_lower)})
        ck(sum(F(d['required_owner_fraction']) for d in row['pairs'])==3)
    rows.append(row)
    (run/'out'/'CASES.json').write_text(json.dumps(rows,indent=2),encoding='utf-8',newline='')

# At fair bias deleting the triple from a pair gives constant 1/2,
# which violates integer admission, and an unnormalized squared law.
p=(F(1,2),)*3;P=spectrum(p)
ck(all(P[s]==F(1,16) for s in P if s))
ck(P[()]==F(9,16))
ck(sum(w for s,w in P.items() if len(s)!=3)==F(15,16))
ck(F(1,2) not in [F(i) for i in range(-2,3)])
conditioned_empty=P[()]/F(15,16)
ck(conditioned_empty==F(3,5))
# All possible means of a Boolean gate on the same fair three-bit cube.
# This rejects every choice of Fourier phases, not just inherited signs.
ck(conditioned_empty not in {F(j-4,4)**2 for j in range(9)})
# Renormalizing that deletion does not repair Booleanity: at all-one input
# the signed inverse Walsh value is (3/4)/sqrt(15/16), whose square is 3/5.
ck(F(3,4)**2/F(15,16)==F(3,5))

# Reused variables are physically contracted before transform, not replaced
# by independent wires: AND(X,X,Y)=AND(X,Y).
p0,q=F(1,3),F(2,5)
actual_mean=2*p0*q-1;independent_mean=2*p0*p0*q-1
ck(actual_mean!=independent_mean)
ck(actual_mean**2==F(121,225));ck(independent_mean**2==F(1681,2025))

# Fair AND2: fixing physical X=0 is constant; spectral X-absence is fair.
ck([F(1),F(0)]!=[F(1,2),F(1,2)])
result={'status':'PASS','cases':len(rows),'interior_cases':len(grid),'pairs':3*len(grid),'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'exact Fraction','all_bias_proof':'PROOF.md; finite checks are supporting evidence only','claim_scope':'exclusive integer-profile packet ownership fails; FEI remains OPEN'}
(run/'out'/'CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='')
print(json.dumps(result))
