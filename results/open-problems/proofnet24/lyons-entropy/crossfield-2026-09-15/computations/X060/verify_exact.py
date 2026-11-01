"""X060 exact, standard-library certificate. No optimization or floats."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

N=6
PAIRS=list(combinations(range(N),2)); TRIPLES=list(combinations(range(N),3))
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def transpose(A): return [list(c) for c in zip(*A)]
def mm(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(A,c): return [[c*a for a in r] for r in A]
def det(A):
    if not A: return F(1)
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))
def charpoly(A):
    n=len(A); B=eye(n); cs=[F(1)]
    for k in range(1,n+1):
        AB=mm(A,B); c=-tr(AB)/k; cs.append(c); B=add(AB,scale(eye(n),c))
    assert all(v==0 for row in B for v in row)
    return cs

def polyprod(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def house(v):
    d=sum(x*x for x in v)
    return [[F(i==j)-F(2*v[i]*v[j],d) for j in range(N)] for i in range(N)]
def cols(Q,ii): return [[r[i] for i in ii] for r in Q]
def pairlaw(U): return {J:det([U[i] for i in J])**2 for J in PAIRS}
def effects(U,V):
    out={}
    for M in TRIPLES:
        row=[]
        for j in range(len(V[0])):
            row.append(det([U[i]+[V[i][j]] for i in M]))
        out[M]=[[a*b for b in row] for a in row]
    return out

def examine(U,V,W=None):
    assert mm(transpose(U),U)==eye(2)
    assert mm(transpose(V),V)==eye(4)
    assert mm(transpose(U),V)==[[0]*4 for _ in range(2)]
    h=pairlaw(U); eff=effects(U,V)
    assert sum(h.values())==1
    total=[[F(0)]*4 for _ in range(4)]
    for E in eff.values(): total=add(total,E)
    assert total==eye(4)
    rows=[]
    for R in TRIPLES:
        RR=set(R); FF=[M for M in TRIPLES if len(RR.intersection(M))>=2]
        assert len(FF)==10
        B=[[F(0)]*4 for _ in range(4)]
        for M in FF: B=add(B,eff[M])
        UR=[U[i] for i in R]; C=mm(transpose(UR),UR); t=tr(C); d=det(C)
        expected=polyprod(polyprod([1,-t,d],[1,-(t-d)]),[1,-d])
        assert charpoly(B)==expected
        assert sum(h[J] for J in PAIRS if set(J)<=RR)==d
        degrees={J:sum(set(J)<=set(M) for M in FF) for J in PAIRS}
        assert all(degrees[J]==(4 if set(J)<=RR else 2 if len(set(J)&RR)==1 else 0) for J in PAIRS)
        excess=sum(h[J]*max(degrees[J]-2,0) for J in PAIRS)
        capacity=sum(h[J]*min(degrees[J],2) for J in PAIRS)
        assert excess==2*d and capacity==2*(t-d) and tr(B)==2*t
        rec={'R':R,'angle_trace':str(t),'angle_product':str(d),'characteristic_polynomial':list(map(str,expected))}
        if W is not None:
            g=F(0)
            for M in FF:
                for j in range(2):
                    g+=det([U[i]+[W[i][j]] for i in M])**2
            assert capacity-g>=0
            rec['actual_cap_gap']=str(capacity-g)
        rows.append(rec)
    return rows

Q=eye(N)
for v in [(1,2,3,4,5,6),(2,-1,3,-2,1,4),(3,1,-2,4,2,-1)]: Q=mm(Q,house(v))
assert mm(transpose(Q),Q)==eye(N)
U=cols(Q,[2,3]); V=cols(Q,[0,1,4,5]); W=cols(Q,[0,1])
rows=examine(U,V,W)
# Exact interior principal-angle example attaining the universal slack.
x=F(9,25); y=F(144,169)
u1=[F(3,5),0,0,F(4,5),0,0]; u2=[0,F(12,13),0,0,F(5,13),0]
v1=[F(4,5),0,0,F(-3,5),0,0]; v2=[0,F(5,13),0,0,F(-12,13),0]
e=[0,0,1,0,0,0]; f=[0,0,0,0,0,1]
Us=transpose([u1,u2]); Vs=transpose([v1,v2,e,f]); Ws=transpose([e,v1])
sharp=examine(Us,Vs,Ws)[0]
assert sharp['R']==(0,1,2)
assert F(sharp['actual_cap_gap'])==x*(1-y)==F(9,169)
# The two thresholds are strictly positive without any decimal logarithm.
# e^4 > sum_{j=0}^{7} 4^j/j! > 48, so 8-2 log(48)>0.
term=F(1); esum=term
for j in range(1,8): term*=F(4,j); esum+=term
assert esum>48
out={'status':'PASS','exact_cut_characteristic_polynomials':40,'generic_frame_all_20_cut_checks':rows,
     'sharp_example':sharp,'exp4_lower_bound':str(esum),
     'claims':'All tests are rational identities; the complex all-parameter proof is in agents/X060.md.'}
Path(__file__).with_name('verified_output.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 40 exact spectral identities; 20 generic cap gaps; sharp gap 9/169; exp(4)>48.')
