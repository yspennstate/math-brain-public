"""Independent subset audit for heterogeneous four-twin matching formula.

This implementation enumerates only the 4s hub edges, never calls a partition
transfer routine, and tests adding the two marked edges by union-find roots.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def direct(xs):
    s=len(xs);edges=[(i,4+j,x) for j,x in enumerate(xs) for i in range(4)]
    A=B=C=D=F(0)
    for mask in range(1<<(4*s)):
        parent=list(range(4+s));weight=F(1)
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        cyclic=False
        for k,(u,v,w) in enumerate(edges):
            if mask>>k&1:
                ru,rv=root(u),root(v)
                if ru==rv:cyclic=True;break
                parent[ru]=rv;weight*=w
        if cyclic:continue
        A+=weight
        if root(0)!=root(1):B+=weight
        if root(2)!=root(3):C+=weight
        if root(0)!=root(1):
            parent[root(0)]=root(1)
            if root(2)!=root(3):D+=weight
    assert B==C
    return B*C-A*D

def formula(xs):
    aa=[1+4*x for x in xs]
    r=F(0)
    for i,j in combinations(range(len(xs)),2):
        p=F(1)
        for k,a in enumerate(aa):
            if k not in (i,j):p*=a*a
        r+=4*xs[i]**2*xs[j]**2*(1+xs[i]+xs[j])**2*p
    for i,j,k in combinations(range(len(xs)),3):
        p=F(1)
        for l,a in enumerate(aa):
            if l not in (i,j,k):p*=a*a
        r+=8*xs[i]**2*xs[j]**2*xs[k]**2*(aa[i]*aa[j]+aa[i]*aa[k]+aa[j]*aa[k])*p
    return r

def main():
    cases=[[],[F(2)],[F(1),F(2)],[F(1,2),F(3,2)],[F(0),F(2)],
           [F(1),F(2),F(3)],[F(1,2),F(2,3),F(3,4)],
           [F(1),F(2),F(3),F(4)],[F(0),F(1),F(2),F(3)]]
    records=[]
    for xs in cases:
        actual=direct(xs);expected=formula(xs)
        assert actual==expected,(xs,actual,expected)
        records.append({'hub_weights':[str(x) for x in xs],'rayleigh_difference':str(actual),'passed':True})
        print('passed',list(map(str,xs)),str(actual),flush=True)
    Path(__file__).with_name('twin_matching_independent_audit_results.json').write_text(json.dumps({'checks':records,'all_passed':True},indent=2))
if __name__=='__main__':main()
