"""Independent exact polynomial transfer-matrix audit for the Klein-four host.

This enumerates no ten-vertex assignment. It multiplies a root-free 16-state
transfer matrix over an exact integer monomial dictionary, then checks the
Schur derivative algebra and ordered nonnegative coefficient certificate.
"""
import json,math
from pathlib import Path
from collections import Counter

def monomial(x,y,k,l):
    # Root-free similarity version: T_(x,y),(k,l)=p_(x^y)p_(x^l)p_(k^y).
    exp=[0]*4
    for a in[x^y,x^l,k^y]:exp[a]+=1
    return tuple(exp)

def main():
    states=[(x,y)for x in range(4)for y in range(4)]
    T=[[monomial(x,y,k,l)for k,l in states]for x,y in states]
    total=Counter()
    for start in range(16):
        current=[Counter()for _ in states];current[start][(0,0,0,0)]=1
        for _ in range(5):
            nxt=[Counter()for _ in states]
            for i,poly in enumerate(current):
                for j,shift in enumerate(T[i]):
                    for mon,c in poly.items():nxt[j][tuple(mon[k]+shift[k]for k in range(4))]+=c
            current=nxt
        total.update(current[start])
    P={mon:1024*c for mon,c in total.items()}
    original=json.loads(Path(__file__).with_name('continuation_20261002_klein4_schur.json').read_text())
    expected={tuple(map(int,k.split(','))):c for k,c in original['density_polynomial'].items()}
    assert P==expected
    # Form gradient difference independently, then polynomial long division
    # by x0−x1, rather than the author's antisymmetric-pair formula.
    remainder=Counter()
    for mon,c in P.items():
        for i,sign in[(0,1),(1,-1)]:
            if mon[i]:
                e=list(mon);e[i]-=1;remainder[tuple(e)]+=sign*c*mon[i]
    remainder=Counter({k:v for k,v in remainder.items()if v});Q=Counter()
    while remainder:
        exp=max(remainder);c=remainder[exp];assert exp[0]>0
        q=list(exp);q[0]-=1;q=tuple(q);Q[q]+=c
        remainder[exp]-=c
        other=list(q);other[1]+=1;remainder[tuple(other)]+=c
        remainder=Counter({k:v for k,v in remainder.items()if v})
    assert {','.join(map(str,k)):v for k,v in Q.items()if v}==original['schur_derivative_quotient']
    ordered=Counter()
    for(a,b,c,d),coef in Q.items():
        # Expand p0=A+D, p1=A, p2=B+E, p3=B.
        for i in range(a+1):
            for j in range(c+1):ordered[(a+b-i,c+d-j,i,j)]+=coef*math.comb(a,i)*math.comb(c,j)
    assert all(c>=0 for c in ordered.values());assert ordered[(0,0,13,0)]==61440
    assert {','.join(map(str,k)):v for k,v in ordered.items()if v}==original['ordered_quotient_coefficients']
    out={'status':'independent exact transfer-polynomial and long-division audit PASS','transfer_dimension':16,
         'transfer_length':5,'polynomial_coefficients_match':True,'ordered_nonnegative_terms':sum(bool(c)for c in ordered.values()),
         'pure_difference_coefficient':ordered[(0,0,13,0)],'quantitative_schur_gap_coefficient':61440//60}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

if __name__=='__main__':main()
