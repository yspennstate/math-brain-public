"""Exact cube8 last affine chamber Sidorenko test. No theorem claim yet."""
from collections import Counter
from pathlib import Path
from math import comb,factorial
import itertools,json


def compositions(n,k,prefix=()):
    if k==1:yield prefix+(n,);return
    for a in range(n+1):yield from compositions(n-a,k-1,prefix+(a,))

def signs(p):
    output=[]
    for a in range(1,8):
        pivot=a&-a
        reps=[x for x in range(8) if not x&pivot]
        sign=1
        for x in reps:sign*=1 if p[x]>p[x^a] else -1
        output.append(sign)
    return output


def shear(P,i):
    R=Counter()
    for n,c in P.items():
        for k in range(n[i]+1):
            z=list(n);z[i]-=k;z[i+1]+=k
            R[tuple(z)]+=c*comb(n[i],k)
    return dict(R)


def main():
    order=[3,5,6,7,4,2,1,0] # descending for ranks (0,1,2,7,3,6,5,4)
    P={}
    for line in Path(__file__).with_name('continuation_20261002_cube8_vertex_polynomial.tsv').read_text().splitlines():
        key,c=map(int,line.split());n=tuple((key>>(4*i))&15 for i in range(8))
        P[tuple(n[i] for i in order)]=8**6*c
    for i in range(7):
        P=shear(P,i);print('shear',i,'terms',len(P),flush=True)
    gap={}
    for n in compositions(15,8):
        c=factorial(15)//__import__('math').prod(factorial(v) for v in n)
        for i,v in enumerate(n):c*=((i+1)**v)
        g=P.get(n,0)-c
        if g:gap[n]=g
    negatives=[(n,c) for n,c in gap.items() if c<0]
    out={'status':'exact last-chamber exploration; analytic audit pending','descending_order':order,
         'host_ranks': [0,1,2,7,3,6,5,4],
         'gap_nonzero_terms':len(gap),'gap_negative_terms':len(negatives),
         'negative_examples':[(list(n),c) for n,c in negatives[:30]],
         'gap_coefficients':{','.join(map(str,n)):c for n,c in sorted(gap.items())}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='gap_coefficients'},indent=2))
if __name__=='__main__':main()
