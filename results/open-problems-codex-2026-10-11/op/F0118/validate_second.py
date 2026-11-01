from fractions import Fraction as F
from itertools import product,permutations
from collections import defaultdict
from pathlib import Path
import json,sympy as S
ROOT=Path(__file__).resolve().parent
def histogram(p1,p2):
    assert sum(p1.values())==sum(p2.values())==1
    h=defaultdict(F)
    for y in set(p1)|set(p2):
        a=p1.get(y,F(0));d=p2.get(y,F(0))
        if a+d:h[abs(a-d)/(a+d)]+=(a+d)/2
    assert sum(h.values())==1
    return h
def H(h,t):return sum(w*max(z-t,0) for z,w in h.items())
def branch(q,alpha,beta):
    def M(lam,i,j):return lam*int(i==j)+(1-lam)/q
    rows=[]
    for root in [0,1]:
        rows.append({(x,y):sum(M(alpha,root,j)*M(beta,j,x)*M(beta,j,y) for j in range(q))
                     for x,y in product(range(q),repeat=2)})
    return rows
def formula(q,alpha,beta,t):
    c=(1-beta)/q;s=1-beta;a=alpha*beta;h=(1-alpha)*beta*beta/s;k=1+2*beta*(1-alpha)/s
    A=h*c+k*c*c;B=k*c*c;u=a*(beta+2*c);v=a*c;m=2*(q-2)
    return max(u-t*(2*A+u),0)+m*max(v-t*(2*B+v),0)
comparisons=0;laws=0
for alpha,beta in product([F(1,4),F(1,2),F(3,4)],repeat=2):
    old=None
    for q in range(2,9):
        hist=histogram(*branch(q,alpha,beta));laws+=1
        for t in set(hist)|{F(0),F(1)}:assert H(hist,t)==formula(q,alpha,beta,t)
        if old:
            assert all(H(hist,t)>=H(old,t) for t in set(hist)|set(old)|{F(0),F(1)})
            comparisons+=1
        old=hist
# One heterogeneous three-branch tree, using exact direct product likelihoods.
hs=[]
for q in [3,4]:
    bs=[branch(q,*ab) for ab in [(F(1,3),F(1,2)),(F(1,2),F(2,3)),(F(3,4),F(1,3))]]
    laws_root=[]
    for i in [0,1]:
        rows={}
        for ys in product(*(b[i].keys() for b in bs)):
            val=F(1)
            for b,y in zip(bs,ys):val*=b[i][y]
            rows[ys]=val
        laws_root.append(rows)
    hs.append(histogram(*laws_root))
assert all(H(hs[1],t)>=H(hs[0],t) for t in set(hs[0])|set(hs[1])|{F(0),F(1)})
# Rooted-partition witness: independently enumerate actual block colors.
parts=[((0,0,1,1,0),1),((0,0,1,2,2),9),((0,1,0,2,1),8),((0,1,1,0,2),5),((0,1,2,3,4),4)]
hp=[]
for q in [4,5]:
    conditional=[]
    for root in [1,2]:
        rows=defaultdict(F)
        for p,w in parts:
            n=max(p)
            for colors in product(range(1,q+1),repeat=n):
                labels=(root,)+colors
                word=tuple(labels[p[i]] for i in range(1,5))
                rows[word]+=F(w,27*q**n)
        conditional.append(rows)
    hp.append(histogram(*conditional))
t=F(225,233);assert H(hp[1],t)-H(hp[0],t)==-F(167,5032800)
assert H(hp[0],0)==F(3,4) and H(hp[1],0)==F(529,675)
# Symmetric-posterior witness: use the analytical orbit payoff, not LP matrices.
mu=[((F(0),F(1,6),F(5,6)),F(2,5)),((F(0),F(1,3),F(2,3)),F(1,25)),
    ((F(0),F(1,2),F(1,2)),F(2,5)),((F(1,6),F(1,3),F(1,2)),F(4,25))]
nu=[((F(0),F(0),F(1)),F(2,5)),((F(1,6),F(1,6),F(2,3)),F(2,5)),((F(1,3),)*3,F(1,5))]
def orbitH(law,t,lam):
    total=F(0)
    for p,w in law:
        v=[(1-lam)/3+lam*x for x in p]
        total+=w*sum(max(abs(v[i]-v[j])-t*(v[i]+v[j]),0) for i,j in [(0,1),(0,2),(1,2)])/2
    return total
knots=[F(0),F(1,5),F(1,3),F(1,2),F(3,5),F(2,3),F(1)]
expected=[F(1,75),0,0,F(1,100),F(8,375),F(1,150),0]
assert [orbitH(mu,t,F(1))-orbitH(nu,t,F(1)) for t in knots]==expected
assert orbitH(mu,F(1,5),F(1,2))==F(37,250)
assert orbitH(nu,F(1,5),F(1,2))==F(13,75)
# Exact polynomial identities underlying the general branch derivative proof.
a,h,k,c,s,beta,eta,t=S.symbols('a h k c s beta eta t')
A=h*c+k*c*c;B=k*c*c;u=a*(beta+2*c);v=a*c;m=2*s/c-4
assert S.expand(u*B-v*A-a*c*c*(k*beta-h+k*c))==0
mass=a*(beta+2*s)+(2*h-2*a+4*s*k)*c-6*k*c*c
assert S.simplify(2*A+u+m*(2*B+v)-mass)==0
assert S.simplify(u+m*v-a*(beta+2*s-2*c))==0
D=a+2*k*c
assert S.expand(D-eta*(a-h-2*k*s+6*k*c)-((1-eta)*D+eta*(h+2*k*(s-2*c))))==0
assert S.simplify(S.diff(u-t*(2*A+u),c)-(2*a-t*(2*h+2*a+4*k*c)))==0
assert S.simplify(S.diff(u+m*v-t*mass,c)-(-2*a-t*(2*h-2*a+4*s*k-12*k*c)))==0
result={'branch_laws_checked':laws,'branch_adjacent_Blackwell_comparisons':comparisons,
        'heterogeneous_three_branch_comparisons':1,'partition_witness_difference':'-167/5032800',
        'edge_composition_witness_difference':'-19/750','symbolic_general_derivative_checks':'passed',
        'all_arithmetic':'exact rational/integer or symbolic polynomial arithmetic; no numerical tolerances'}
(ROOT/'second_validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result),flush=True)
