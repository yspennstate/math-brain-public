from itertools import product
from math import log2
import random

def entropy(vals):
    n=len(vals)
    counts={}
    for y in vals:
        counts[y]=counts.get(y,0)+1
    out=0.0
    for c in counts.values():
        p=c/n
        out -= p*log2(p)
    return out

def influences(labels,m):
    N=1<<m
    ans=[]
    for k in range(m):
        ans.append(sum(labels[x]!=labels[x^(1<<k)] for x in range(N))/N)
    return ans

def cond_entropy(labels,m,revealed):
    N=1<<m
    groups={}
    for x in range(N):
        key=tuple((x>>k)&1 for k in revealed)
        groups.setdefault(key,[]).append(labels[x])
    return sum((len(v)/N)*entropy(v) for v in groups.values())

def expected_cond_uniform(labels,m,s):
    t=1-s
    out=0.0
    for mask in range(1<<m):
        R=[k for k in range(m) if (mask>>k)&1]
        pr=1.0
        for k in range(m):
            pr *= t if (mask>>k)&1 else s
        out += pr*cond_entropy(labels,m,R)
    return out

def expected_cond_weighted(labels,m,svec):
    out=0.0
    for mask in range(1<<m):
        R=[k for k in range(m) if (mask>>k)&1]
        pr=1.0
        for k,s in enumerate(svec):
            pr *= (1-s) if (mask>>k)&1 else s
        out += pr*cond_entropy(labels,m,R)
    return out

uniform_cases=0
uniform_max=0.0
for m in range(1,4):
    N=1<<m
    for labels in product(range(2), repeat=N):
        I=sum(influences(labels,m))
        for s in (0.0,0.125,0.25,0.5,0.75,1.0):
            lhs=expected_cond_uniform(labels,m,s)
            rhs=s*I
            assert lhs <= rhs+1e-12
            uniform_cases += 1
            if rhs>0:
                uniform_max=max(uniform_max,lhs/rhs)

random.seed(20260922)
weighted_cases=0
weighted_max=0.0
for m in range(1,5):
    N=1<<m
    for _ in range(500):
        q=random.randint(2,5)
        labels=[random.randrange(q) for _ in range(N)]
        svec=[random.random() for _ in range(m)]
        inf=influences(labels,m)
        lhs=expected_cond_weighted(labels,m,svec)
        rhs=sum(s*i for s,i in zip(svec,inf))
        assert lhs <= rhs+1e-11
        weighted_cases += 1
        if rhs>0:
            weighted_max=max(weighted_max,lhs/rhs)

print(f"binary_uniform_cases={uniform_cases} max_ratio={uniform_max:.16f}")
print(f"multilabel_weighted_cases={weighted_cases} max_ratio={weighted_max:.16f}")
print(f"label_constant_239_over_112={239/112:.16f}")
print(f"combined_constant_299_over_112={299/112:.16f}")
