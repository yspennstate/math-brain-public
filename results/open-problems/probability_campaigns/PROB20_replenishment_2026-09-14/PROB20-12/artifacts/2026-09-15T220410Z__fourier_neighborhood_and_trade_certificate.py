"""Exact certificate for PROB20-12, 2026-09-15.

Checks:
  * the positive Fourier (2,2,2) union coupling with min atom 1/216;
  * exact rank 38 of the 45 x 90 marginal map;
  * an explicit unimodular 38 x 38 right-inverse minor with ||M^{-1}||_{inf<-inf}=45;
  * all 135 six-state 3-vs-3 marginal-preserving trades;
  * trade orbit split 15 global + 120 anchor-local;
  * exact ranks 15, 47, and 52, so the 135 trades span the full real kernel;
  * a displayed 52 x 52 trade minor has determinant -3.
"""
import itertools
from collections import defaultdict
import sympy as sp

V = tuple(range(6))
C = tuple(range(3))
EDGES = list(itertools.combinations(V, 2))
EID = {e:i for i,e in enumerate(EDGES)}

def edge(e): return tuple(sorted(e))
def ix(c,e): return 15*c + EID[edge(e)]
def circdist(e):
    d = abs(e[0]-e[1])
    return min(d, 6-d)

# 90 labeled pair partitions / balanced colorings.
ST=[]; COL=[]; UM=[]
for col in itertools.product(C, repeat=6):
    if all(col.count(c)==2 for c in C):
        x=[0]*45; m=[]
        for c in C:
            pts=tuple(v for v in V if col[v]==c)
            x[ix(c,pts)] = 1
            m.append(edge(pts))
        ST.append(x); COL.append(col); UM.append(tuple(sorted(m)))
assert len(ST)==90
A = sp.Matrix(ST).T
assert A.rank()==38

# Fourier seed marginal: consecutive frequency pairs in the 6-point DFT.
mu_by_dist={1:sp.Rational(1,36), 2:sp.Rational(1,12), 3:sp.Rational(1,9)}
# State weight is determined by the distance multiset of the underlying uncolored matching.
num_by_type={
    (1,1,1):1,
    (1,2,2):1,
    (1,1,3):1,
    (2,2,3):7,
    (3,3,3):4,
}
q0=[]
for m in UM:
    typ=tuple(sorted(circdist(e) for e in m))
    q0.append(sp.Rational(num_by_type[typ],216))
assert sum(q0)==1
assert min(q0)==sp.Rational(1,216)
mu0=A*sp.Matrix(q0)
for c in C:
    for e in EDGES:
        assert mu0[ix(c,e)]==mu_by_dist[circdist(e)]

# Optimality of the common positive margin: any fixed colored distance-1 edge
# occurs in exactly 6 states and has marginal 1/36, hence min_s q_s <= 1/216.
for c in C:
    e=(0,1)
    inc=[s for s,x in enumerate(ST) if x[ix(c,e)]==1]
    assert len(inc)==6
    assert sum(q0[s] for s in inc)==sp.Rational(1,36)

# Explicit 38x38 unimodular minor / right inverse.
CP=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,16,18,19,20,27,30,31,32,33,34,35,36,42,43,44,45,46,47,48,60,61,62,69,84]
RP=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,35,36,37,39,40]
M=A.extract(RP,CP)
assert M.det(method='domain-ge')==-1
Minv=M.inv()
assert all(sp.denom(z)==1 for z in Minv)
row_l1=[sum(abs(z) for z in Minv.row(i)) for i in range(38)]
assert max(row_l1)==45

# Enumerate all 3-vs-3 collisions of marginal vectors.
D=defaultdict(list)
for tri in itertools.combinations(range(90),3):
    s=tuple(ST[tri[0]][k]+ST[tri[1]][k]+ST[tri[2]][k] for k in range(45))
    D[s].append(tri)
TR=[]
for ls in D.values():
    if len(ls)>1:
        for i in range(len(ls)):
            for j in range(i+1,len(ls)):
                if set(ls[i]).isdisjoint(ls[j]):
                    TR.append((ls[i],ls[j]))
assert len(TR)==135
T=sp.zeros(90,135)
for j,(pos,neg) in enumerate(TR):
    for s in pos:T[s,j]=1
    for s in neg:T[s,j]=-1
assert A*T==sp.zeros(45,135)
assert T.rank()==52
assert 90-A.rank()==52

# Two natural symmetry types.
global_idx=[]; local_idx=[]
for j,(pos,neg) in enumerate(TR):
    mats={UM[s] for s in pos+neg}
    (global_idx if len(mats)==1 else local_idx).append(j)
assert len(global_idx)==15 and len(local_idx)==120
assert T[:,global_idx].rank()==15
assert T[:,local_idx].rank()==47

# Exact independence certificate for 52 selected six-state trades.
TC=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,48,50,51,56,58,60,61,63,81,82]
RR=[0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,30,31,32,33,34,35,36,37,38,39,40,48,49,50,51,52,60,61,63,64,65,66,67,68,72,74,75]
assert T.extract(RR,TC).det(method='domain-ge')==-3

print('states',len(ST))
print('marginal_map_rank',A.rank(),'kernel_dim',90-A.rank())
print('seed_min_atom',min(q0),'seed_total',sum(q0))
print('right_inverse_minor_det',M.det(method='domain-ge'),'max_row_l1',max(row_l1))
print('six_state_trades',len(TR),'global',len(global_idx),'local',len(local_idx))
print('trade_ranks',T[:,global_idx].rank(),T[:,local_idx].rank(),T.rank())
print('trade_minor_det',T.extract(RR,TC).det(method='domain-ge'))
print('ALL EXACT CHECKS PASSED')
