#!/usr/bin/env python3
"""Targeted check for the pivotal-subcube rigidity statement.

Enumerates all Boolean functions for n <= 4. This is not a proof of FEI and is
not used as the proof of the classification theorem; it is only an attempted
refutation / small-case sanity check for the new structural lemma.
"""
from __future__ import annotations
import collections
import json
import math

def fwht(vals):
    a=[float(x) for x in vals]
    h=1
    while h < len(a):
        for b in range(0,len(a),2*h):
            for k in range(h):
                x,y=a[b+k],a[b+h+k]
                a[b+k],a[b+h+k]=x+y,x-y
        h*=2
    n=len(a)
    return [x/n for x in a]

def entropy_influence(vals):
    a=fwht(vals)
    p=[x*x for x in a]
    H=sum(q*math.log2(1/q) for q in p if q)
    I=sum(s.bit_count()*p[s] for s in range(len(p)))
    return H,I

def pivotal_subcube(vals,n,i):
    others=[j for j in range(n) if j != i]
    hits=[]
    for r in range(1 << (n-1)):
        x=0
        for k,j in enumerate(others):
            x |= ((r >> k) & 1) << j
        if vals[x] != vals[x | (1 << i)]:
            hits.append(r)
    if not hits:
        return {"relevant":False,"alpha":0.0,"fixed":{}}
    if len(hits) & (len(hits)-1):
        return None
    fixed={}
    for k,j in enumerate(others):
        bits={(r >> k) & 1 for r in hits}
        if len(bits)==1:
            fixed[j]=next(iter(bits))
    expected=[]
    for r in range(1 << (n-1)):
        ok=True
        for j,b in fixed.items():
            k=others.index(j)
            if ((r >> k) & 1) != b:
                ok=False
                break
        if ok:
            expected.append(r)
    if set(expected) != set(hits):
        return None
    return {"relevant":True,"alpha":len(hits)/(1 << (n-1)),"fixed":fixed}

def classify(vals,n):
    info=[]
    for i in range(n):
        d=pivotal_subcube(vals,n,i)
        if d is None:
            return None
        info.append(d)
    rel=[i for i,d in enumerate(info) if d["relevant"]]
    N={i:set(info[i]["fixed"]) for i in rel}
    for i in rel:
        for j in rel:
            if i != j and ((j in N[i]) != (i in N[j])):
                raise AssertionError("asymmetric dependency")
    unseen=set(rel)
    comps=[]
    while unseen:
        s=next(iter(unseen))
        unseen.remove(s)
        comp={s}
        stack=[s]
        while stack:
            u=stack.pop()
            for v in N[u]:
                if v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    stack.append(v)
        comps.append(sorted(comp))
    for C in comps:
        Cset=set(C)
        for i in C:
            if N[i] != Cset-{i}:
                raise AssertionError("dependency component not a clique")
    blocks=[]
    for C in comps:
        if len(C)==1:
            blocks.append((C,{C[0]:0}))
        else:
            b={}
            for k in C:
                choices={info[i]["fixed"][k] for i in C if i != k}
                if len(choices) != 1:
                    raise AssertionError("inconsistent subcube center")
                b[k]=next(iter(choices))
            blocks.append((C,b))
    pred=[]
    for x in range(1 << n):
        v=1
        for C,b in blocks:
            center=all(((x >> k)&1)==bit for k,bit in b.items())
            v *= -1 if center else 1
        pred.append(v)
    if vals != pred and vals != [-v for v in pred]:
        raise AssertionError("product-of-one-point factorization failed")
    return tuple(sorted((len(C) for C in comps), reverse=True))

def main():
    result={}
    for n in range(1,5):
        accepted=0
        failures=0
        patterns=collections.Counter()
        max_ratio=0.0
        for truth in range(1 << (1 << n)):
            vals=[1 if ((truth >> x)&1) else -1 for x in range(1 << n)]
            if any(pivotal_subcube(vals,n,i) is None for i in range(n)):
                continue
            accepted += 1
            try:
                pattern=classify(vals,n)
            except AssertionError:
                failures += 1
                continue
            patterns[str(pattern)] += 1
            H,I=entropy_influence(vals)
            if I:
                max_ratio=max(max_ratio,H/I)
        result[str(n)]={
            "accepted_functions":accepted,
            "classification_failures":failures,
            "max_H_over_I":max_ratio,
            "component_size_patterns":dict(sorted(patterns.items())),
        }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
