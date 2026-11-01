"""Unproved apex-real-rootedness exploration for the disjoint-pair route.

Exact coefficients from ordinary forest partition DP; numpy roots are only
an exploratory diagnostic. They never certify a theorem or a failure.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from random import Random
import json
import numpy as np


def canon(row):
    names={};return tuple(names.setdefault(x,len(names))for x in row)


def forest_partition_dp(n,edges):
    frontier={tuple(range(n)):1}
    for u,v,w in edges:
        out=defaultdict(int)
        for state,mass in frontier.items():
            out[state]+=mass
            if state[u]!=state[v]:
                target=canon(tuple(state[u]if x==state[v]else x for x in state))
                out[target]+=mass*w
        frontier=out
    return frontier


def apex_coefficients(n,edges,profile):
    coefficients=[0]*(n+1)
    for state,mass in forest_partition_dp(n,edges).items():
        sums=defaultdict(int)
        for label,x in zip(state,profile):sums[label]+=x
        poly=[1]
        for x in sums.values():
            following=[0]*(len(poly)+1)
            for i,value in enumerate(poly):following[i]+=value;following[i+1]+=x*value
            poly=following
        for i,value in enumerate(poly):coefficients[i]+=mass*value
    return coefficients


def sturm_real_count(coefficients):
    def trim(poly):
        while len(poly)>1 and not poly[-1]:poly.pop()
        return poly
    def remainder(left,right):
        left=left[:]
        while len(left)>=len(right) and any(left):
            degree=len(left)-len(right);factor=left[-1]/right[-1]
            for i,value in enumerate(right):left[degree+i]-=factor*value
            trim(left)
        return left
    polynomial=trim(list(map(F,coefficients)))
    sequence=[polynomial,[i*x for i,x in enumerate(polynomial)][1:]]
    while len(sequence[-1])>1:
        following=[-x for x in remainder(sequence[-2],sequence[-1])]
        if not any(following):break
        following=[x/abs(following[-1])for x in following];sequence.append(following)
    positive=[1 if p[-1]>0 else -1 for p in sequence]
    negative=[s*(-1 if (len(p)-1)%2 else 1)for p,s in zip(sequence,positive)]
    variations=lambda signs:sum(a!=b for a,b in zip(signs,signs[1:]))
    return variations(negative)-variations(positive)


def main():
    rng=Random(421009);report={'status':'exploration, not a universal theorem','counts':{},'candidate':None,'floating_false_alerts_exactly_checked':[]}
    cases=[]
    for n in range(3,10):
        trials=30 if n<=7 else 10
        cases += [(n,[(i,j,10**k)for i in range(n)for j in range(i+1,n)],[1]*n)
                  for k in (0,1,2,3)]
        for _ in range(trials):
            edges=[(i,j,rng.randrange(1,31))for i in range(n)for j in range(i+1,n)if rng.random()<.7]
            profile=[rng.randrange(1,31)for i in range(n)]
            cases.append((n,edges,profile))
    for n,edges,profile in cases:
        coefficients=apex_coefficients(n,edges,profile)
        roots=np.roots(list(reversed(coefficients)))
        report['counts'][str(n)]=report['counts'].get(str(n),0)+1
        imaginary=max(abs(root.imag)for root in roots)
        if imaginary>1e-5*max(1,max(abs(root.real)for root in roots)):
            exact_count=sturm_real_count(coefficients)
            if exact_count==n:
                report['floating_false_alerts_exactly_checked'].append({'vertices':n,'edges':edges,'profile':profile,
                    'exact_apex_coefficients_ascending':list(map(str,coefficients)),'exact_sturm_distinct_real_roots':exact_count})
                continue
            report['candidate']={'vertices':n,'edges':edges,'profile':profile,
                'exact_apex_coefficients_ascending':list(map(str,coefficients)),
                'float_roots':[[float(root.real),float(root.imag)]for root in roots],
                'exact_sturm_distinct_real_roots':exact_count}
            print('Exact fewer distinct real roots at',n,'vertices; multiplicities need checking.',flush=True)
            break
    print('Exploratory counts',report['counts'],'exactly rejected float alerts',len(report['floating_false_alerts_exactly_checked']),flush=True)
    Path(__file__).with_name('forest_apex_real_rootedness_exploration_results.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
