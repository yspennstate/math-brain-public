from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
from qcomplex_fraction import Z,O,add,neg,sub,mul,conj,eye,madd,msub,mmul,mstar,minv,det,diag

def P(p): return [[O if j==p[i] else Z for j in range(4)] for i in range(4)]
def ctype(p):
    seen=[False]*4; L=[]
    for i in range(4):
        if not seen[i]:
            j=i; n=0
            while not seen[j]: seen[j]=True; n+=1; j=p[j]
            L.append(n)
    return tuple(sorted(L,reverse=True))

coords=[F(483,50),F(-63,25),F(-72,25),F(-163,50),F(33,50),F(23,5),F(-139,25),F(9,25),F(-187,50),F(6,5),F(147,50),F(3,10),F(31,10),F(-14,25),F(1,50),F(-7,2)]
K=[[Z]*4 for _ in range(4)]
for i in range(4): K[i][i]=(F(0),coords[i])
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for q,(i,j) in enumerate(pairs):
    w=(coords[4+2*q],coords[5+2*q]); K[i][j]=w; K[j][i]=neg(conj(w))
I=eye(4); U=mmul(minv(madd(I,K)),msub(I,K)); assert mmul(U,mstar(U))==I

a=[(F(18),F(-17)),(F(-20),F(2)),(F(15),F(-22)),(F(-21),F(2))]
b=[(F(-19),F(4)),(F(25),F(-5)),(F(18),F(-1)),(F(-18),F(1))]
A=diag(a); B=diag(b)
def L(z): return F(-5782)*z[0]+F(19099)*z[1]
def h(V): return L(det(madd(A,mmul(mmul(V,B),mstar(V)))))

S4=list(permutations(range(4))); classes=defaultdict(list)
for p in S4: classes[ctype(p)].append(p)
h0=h(U); row={p:h(mmul(P(p),U)) for p in S4}; col={p:h(mmul(U,P(p))) for p in S4}
for cls in classes.values(): assert sum((row[p] for p in cls),F(0))==sum((col[p] for p in cls),F(0))
T=classes[(2,1,1)]; C3=classes[(3,1)]
G=sum((h0-row[p] for p in T),F(0)); A3=sum((row[p] for p in C3),F(0))/8
assert G==sum((h0-col[p] for p in T),F(0))==4*(h0-A3)
assert h0==3*(sum((row[p] for p in T),F(0))/6)-2*A3
expected_gap=F(2774999449515476249040000,431850208768934029)
assert F(-61633500)-h0==expected_gap
print('PASS exact Cayley unitary reconstruction')
print('partner_support_gap =', expected_gap)
print('common_transposition_gap_sum_G =', G)
print('pair_hessian_trace_minus4G =', -4*G)
print('PASS all five conjugacy-class balances and central cubature')
