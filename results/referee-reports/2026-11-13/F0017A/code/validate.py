"""Independent integer Bareiss checks, complete small cases, and sign invariance."""
import collections
import itertools
import json
import os
from pathlib import Path
import random
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
EXE=ROOT/'code/enumerate'

def bareiss(a):
    a=[list(r) for r in a]
    n=len(a)
    if not n:return 1
    prev=1;sgn=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return 0
        if p!=k:a[k],a[p]=a[p],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%prev==0
                a[i][j]=val//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]

def values(rows,n):
    p=subprocess.run([str(EXE),'values',str(n),*map(str,rows)],capture_output=True,text=True,check=True)
    return json.loads(p.stdout)

def matrix(rows,n,mask):
    return [[(1 if mask>>i&1 else -1) if i==j else (1 if rows[i]>>j&1 else -1) for j in range(n)] for i in range(n)]

def main():
    start=time.time();rng=random.Random(170017);checked=0;invariance=0
    for n in range(1,9):
        for sample in range(12):
            rows=[rng.getrandbits(n)&~(1<<i) for i in range(n)]
            r=values(rows,n)
            for mask,d in enumerate(r['determinants']):
                assert d==bareiss(matrix(rows,n,mask)),(n,sample,mask,d)
                checked+=1
            # Independent row/column multiplications permute the diagonal cube.
            rs=[rng.choice([-1,1]) for _ in range(n)]
            cs=[rng.choice([-1,1]) for _ in range(n)]
            b=[sum((int((1 if rows[i]>>j&1 else -1)*rs[i]*cs[j]>0)<<j) for j in range(n) if i!=j) for i in range(n)]
            assert values(b,n)['singular_switchings']==r['singular_switchings']
            invariance+=1
    # Entire off-diagonal probability space at n<=4, with no symmetry reduction.
    brute={}
    for n in range(1,5):
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        hist=collections.Counter()
        for bits in range(1<<len(edges)):
            rows=[0]*n
            for k,(i,j) in enumerate(edges):rows[i]|=((bits>>k)&1)<<j
            z=sum(bareiss(matrix(rows,n,s))==0 for s in range(1<<n))
            hist[z]+=1
        p=subprocess.run([str(EXE),'exhaustive',str(n)],capture_output=True,text=True,check=True)
        ex=json.loads(p.stdout);ratio=(1<<len(edges))//ex['representatives']
        assert dict(hist)=={int(k):v*ratio for k,v in ex['histogram'].items()}
        brute[n]=dict(hist)
    out=dict(status='PASS',seed=170017,integer_determinants_checked=checked,
             sign_invariance_checks=invariance,unreduced_histograms=brute,
             elapsed_seconds=time.time()-start,inherited_nice=os.getpriority(os.PRIO_PROCESS,0))
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'data/validation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
