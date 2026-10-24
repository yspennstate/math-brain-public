#!/usr/bin/env python3
"""Exact sharp rank-two Sidorenko certificates. Standard library only.
Not a verification of arbitrary-rank Sidorenko.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json

EDGES = [(i, 5 + (i+j) % 5) for i in range(5) for j in range(3)]

def clean(p): return {k:F(v) for k,v in p.items() if v}
def addterm(p, a, b, c): p[a,b] += F(c)
def factor_term(p, a, b, exponent, coefficient):
    assert a >= 0 and b >= 0 and exponent >= 0
    for j in range(exponent+1): addterm(p,a+j,b,coefficient*(-1)**j*comb(exponent,j))
def bernstein(p, degrees):
    n,m=degrees
    assert all(a<=n and b<=m for a,b in p)
    return [[sum((c*F(comb(i,a),comb(n,a))*F(comb(j,b),comb(m,b))
                    for (a,b),c in p.items() if a<=i and b<=j),F(0))
                for j in range(m+1)] for i in range(n+1)]
def power_from_bernstein(B):
    n,m=len(B)-1,len(B[0])-1
    p=defaultdict(F)
    for i,row in enumerate(B):
        for j,b in enumerate(row):
            for a in range(n-i+1):
                for c in range(m-j+1):
                    addterm(p,i+a,j+c,b*comb(n,i)*comb(m,j)*comb(n-i,a)*comb(m-j,c)*(-1)**(a+c))
    return clean(p)
def eval_poly(p,x,y): return sum((c*x**a*y**b for (a,b),c in p.items()),F(0))
def encoded(p): return [[a,b,str(c)] for (a,b),c in sorted(p.items())]

def main():
    counts=Counter()
    for mask in range(1<<len(EDGES)):
        d=[0]*10
        for j,(a,b) in enumerate(EDGES):
            if mask>>j&1: d[a]+=1;d[b]+=1
        if 1 not in d:
            assert d.count(3)%2==0
            counts[mask.bit_count(),d.count(2),d.count(3)]+=1
    assert sum(counts.values())==625
    expected={(0,0,0):1,(4,4,0):5,(6,6,0):15,(7,4,2):5,
      (8,5,2):10,(8,8,0):30,(9,6,2):60,(10,4,4):15,(10,7,2):70,
      (10,10,0):13,(11,5,4):60,(11,8,2):95,(12,3,6):10,(12,6,4):145,
      (13,4,6):75,(14,2,8):15,(15,0,10):1}
    assert dict(counts)==expected
    Q=defaultdict(F); D=defaultdict(F)
    for (e,n2,n3),c in counts.items():
        if e==0: continue
        k=n3//2
        factor_term(Q,e-k-4,k,2*k,c*(-1)**e)
        if k:
            factor_term(D,e-k-6,k-1,2*k-2,-k*c*(-1)**e)
    Q,D=clean(Q),clean(D)
    # D = - Q_v / [r^2 (1-r)^2]; verify in the power basis.
    minus_dv=clean({(a,b-1):-b*c for (a,b),c in Q.items() if b})
    restored=defaultdict(F)
    for (a,b),c in D.items(): factor_term(restored,a+2,b,2,c)
    assert clean(restored)==minus_dv
    BD=bernstein(D,(12,4)); assert power_from_bernstein(BD)==D
    assert min(map(min,BD))==F(125,33)
    R=dict(Q); R[0,0]-=5; R=clean(R)
    assert all(a>=2 for a,b in R)
    R={(a-2,b):c for (a,b),c in R.items()}
    BR=bernstein(R,(14,5)); assert power_from_bernstein(BR)==R
    assert min(map(min,BR))==10
    # Stronger usable remainder 10 r^7, in addition to 5 r^4+10 r^6.
    R7=dict(R); R7[0,0]=R7.get((0,0),F(0))-10
    R7[1,0]=R7.get((1,0),F(0))-10;R7=clean(R7)
    B7=bernstein(R7,(14,5));assert power_from_bernstein(B7)==R7
    assert min(map(min,B7))>=0
    # Independently evaluate the extremal TWO-STATE KERNEL, no square roots.
    extremal_tests=0
    for r in [F(1,50),F(1,10),F(1,4),F(1,2),F(3,4),F(1)]:
        masses=[r/(1+r),1/(1+r)]
        W=[[F(0),1+r],[1+r,1-r*r]]
        assert all(sum(masses[j]*W[i][j] for j in range(2))==1 for i in range(2))
        direct=F(0)
        for word in product(range(2),repeat=10):
            term=F(1)
            for i in word: term*=masses[i]
            for a,b in EDGES: term*=W[word[a]][word[b]]
            direct+=term
        assert direct==1+r**4*eval_poly(Q,r,F(1))
        assert direct>=1+5*r**4+10*r**6+10*r**7
        extremal_tests+=1
    # Explicit failure of componentwise spectral positivity on three equal blocks.
    A=[[0,3,0],[3,0,0],[0,0,3]]
    negative=[[F(-3,2),F(3,2),0],[F(3,2),F(-3,2),0],[0,0,0]]
    positive=[[F(1,2),F(1,2),-1],[F(1,2),F(1,2),-1],[-1,-1,2]]
    assert all(F(A[i][j])==1+negative[i][j]+positive[i][j] for i in range(3) for j in range(3))
    assert 1+negative[0][0]==F(-1,2)
    # Adding a separately admissible negative eigencomponent can DECREASE t_H.
    Fmat=[[-negative[i][j] for j in range(3)] for i in range(3)]
    def build(a,b):
        return [[1+a*Fmat[i][j]+b*positive[i][j] for j in range(3)] for i in range(3)]
    def density3(A):
        C={(a,b,c):sum(A[x][a]*A[x][b]*A[x][c] for x in range(3))/3
           for a,b,c in product(range(3),repeat=3)}
        answer=F(0)
        for w in product(range(3),repeat=5):
            term=F(1)
            for i in range(5):term*=C[w[i],w[(i+1)%5],w[(i+2)%5]]
            answer+=term/3**5
        return answer
    combined=build(F(-3,5),F(-1,5)); first=build(F(-3,5),0); second=build(0,F(-1,5))
    assert all(x>=0 for A in [combined,first,second] for row in A for x in row)
    assert all(sum(row)==3 for A in [combined,first,second] for row in A)
    d0,d1,d2=map(density3,[combined,first,second])
    assert d0==F(86497056981,30517578125)
    assert d1==F(28616512,9765625) and d2==F(985357817649,976562500000)
    assert d0-d1==F(-2929543019,30517578125)<0
    assert d0-d1-d2+1==F(-102540694257,976562500000)<0
    out={'status':'ALL_EXACT_CHECKS_PASS' ,'source_graph_edges':EDGES,
      'edge_subsets_enumerated':1<<15,'surviving_edge_subsets':625,
      'counts':[[*k,c] for k,c in sorted(counts.items())],
      'Q_power_coefficients':encoded(Q),'D_power_coefficients':encoded(D),
      'monotonicity_Bernstein_degrees':[12,4],
      'monotonicity_Bernstein_coefficients':[[str(x) for x in row] for row in BD],
      'monotonicity_Bernstein_min':'125/33','monotonicity_identity_reconstructed':True,
      'remainder_Bernstein_degrees':[14,5],
      'remainder_Bernstein_coefficients':[[str(x) for x in row] for row in BR],
      'remainder_Bernstein_min':'10','remainder_identity_reconstructed':True,
      'seventh_order_Bernstein_min':str(min(map(min,B7))),
      'direct_extremal_kernel_tests':extremal_tests,
      'spectral_truncation_negative_entry':'-1/2',
      'rank3_counterexample':{'combined_density':str(d0),'first_component_density':str(d1),'second_component_density':str(d2),'addition_difference':str(d0-d1),'superadditivity_gap':str(d0-d1-d2+1)},
      'scope':'Sharp rank-two regular-kernel theorem and obstructions; NOT unrestricted Sidorenko.'}
    Path(__file__).with_name('sidorenko_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if 'coefficients' not in k and k!='counts'},indent=2))
if __name__=='__main__': main()
