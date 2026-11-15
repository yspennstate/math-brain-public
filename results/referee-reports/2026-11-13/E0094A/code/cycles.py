"""Single-chord census and exhaustive cycle matching search through n=14."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[k]='1'
import csv
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from regular_graphs import gap, matchings
from exact_spectra import polynomial,certify_bracket
import sympy as s


def cycle(n):
    a=np.zeros((n,n))
    for i in range(n):a[i,(i+1)%n]=a[(i+1)%n,i]=1
    return a


def main():
    rows=[]; exact=[]
    for n in range(4,42,2):
        a=cycle(n);g0=1-np.cos(2*np.pi/n)
        for w in [.01,.5,1.,5.,1000.]:
            for k in range(2,n//2+1):
                b=a.copy();b[0,k]=b[k,0]=w
                g=gap(b)
                bound=g0/(1+2*w*np.cos(np.pi*k/n)**2/(n+w))
                assert g<=bound+1e-11
                if k==n//2:assert abs(g-g0)<1e-11
                rows.append(dict(n=n,k=k,w=w,gap=g,cycle_gap=g0,upper_bound=bound))
                if n<=16 and w in [.5,1.,5.]:
                    # Integer conductance scaling leaves the normalized spectrum unchanged.
                    d=s.Rational(str(w)).q
                    bi=(b*d).round().astype(int).tolist()
                    p=polynomial(bi)
                    lo,hi,q=certify_bracket(bi,g)
                    x=p.gen
                    if k==n//2:
                        minimal=s.Poly(s.minimal_polynomial(1-s.cos(2*s.pi/n),x),x)
                        assert p.rem(minimal).is_zero
                    exact.append(dict(n=n,k=k,w=w,polynomial=str(s.factor(p.as_expr())),bracket=[lo,hi,q]))
    with open('data/cycle_chords.csv','w') as f:
        out=csv.DictWriter(f,list(rows[0]));out.writeheader();out.writerows(rows)
    Path('data/cycle_exact.json').write_text(json.dumps(exact,indent=2)+'\n')
    matchrows=[]
    for n in range(4,15,2):
        a=cycle(n);best=-1.;bm=None;count=0
        for m in matchings(list(range(n)),a):
            b=a.copy()
            for u,v in m:b[u,v]=b[v,u]=1
            g=gap(b);count+=1
            if g>best+1e-12:best,bm=g,m
        anti=a.copy()
        for i in range(n//2):anti[i,i+n//2]=anti[i+n//2,i]=1
        row=dict(n=n,matchings=count,best_gap=best,best_matching=bm,antipodal_gap=gap(anti))
        matchrows.append(row);print(row,flush=True)
    Path('data/cycle_matchings.json').write_text(json.dumps(matchrows,indent=2)+'\n')


if __name__=='__main__':main()
