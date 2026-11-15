"""Exact checks of dimensions and inequalities in the heat-trace lemma."""
from fractions import Fraction
from math import factorial
import json
from pathlib import Path


def partitions(n,maximum=None):
    if n==0:
        yield ()
        return
    if maximum is None:maximum=n
    for k in range(min(n,maximum),1-1,-1):
        for tail in partitions(n-k,k):yield (k,)+tail


def dimension(lam):
    hooks=1
    for i,row in enumerate(lam):
        for j in range(row):
            hooks*=row-j+sum(v>j for v in lam[i+1:])
    return factorial(sum(lam))//hooks


def main():
    rows=[]
    for n in range(3,21):
        dims={};parts=list(partitions(n))
        total=0
        for lam in parts:
            dim=dimension(lam);total+=dim*dim
            col=[sum(row>j for row in lam) for j in range(lam[0])]
            r=Fraction(sum(a*a for a in lam)-sum(a*a for a in col),n*(n-1))
            j=n-lam[0]
            assert (1-r)/2>=Fraction(j,2*(n-1))
            dims[j]=dims.get(j,0)+dim*dim
        assert total==factorial(n)
        assert all(v<=n**(2*j) for j,v in dims.items())
        rows.append(dict(n=n,partitions=len(parts),dimension_square_sum=total))
    Path('data/heat_trace_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('Passed all partition identities and bounds for n=3,...,20')


if __name__=='__main__':main()
