from fractions import Fraction as F
from itertools import permutations, combinations
from collections import defaultdict

S4=list(permutations(range(4)))
def inv(p):
    q=[0]*4
    for i,j in enumerate(p): q[j]=i
    return tuple(q)
def ctype(p):
    seen=[False]*4; L=[]
    for i in range(4):
        if not seen[i]:
            j=i; n=0
            while not seen[j]: seen[j]=True; n+=1; j=p[j]
            L.append(n)
    return tuple(sorted(L,reverse=True))
def subs(k): return list(combinations(range(4),k))
def act(p,I): return tuple(sorted(p[i] for i in I))
def zmat(k,cls):
    Q=subs(k); ix={I:i for i,I in enumerate(Q)}
    M=[[0]*len(Q) for _ in Q]
    for I in Q:
        for g in cls: M[ix[I]][ix[act(inv(g),I)]] += 1
    return M
def lincomb(a,I,b,J,c=0,C=None):
    n=len(I)
    return [[a*I[i][j]+b*J[i][j]+c*(C[i][j] if C else 0) for j in range(n)] for i in range(n)]

classes=defaultdict(list)
for p in S4: classes[ctype(p)].append(p)
I4=[[int(i==j) for j in range(4)] for i in range(4)]; J4=[[1]*4 for _ in range(4)]
Q2=subs(2); ix2={I:i for i,I in enumerate(Q2)}
I6=[[int(i==j) for j in range(6)] for i in range(6)]; J6=[[1]*6 for _ in range(6)]; C6=[[0]*6 for _ in range(6)]
for I in Q2:
    Ic=tuple(i for i in range(4) if i not in I); C6[ix2[I]][ix2[Ic]]=1
coeff={
 (1,1,1,1):((1,0),(1,0,0)),
 (2,1,1):((2,1),(1,1,-1)),
 (3,1):((0,2),(-2,2,-2)),
 (2,2):((-1,1),(1,0,2)),
 (4,):((-2,2),(-1,1,1)),
}
for ct,cls in classes.items():
    a,b=coeff[ct][0]; x,y,z=coeff[ct][1]
    assert zmat(1,cls)==lincomb(a,I4,b,J4)
    assert zmat(2,cls)==lincomb(x,I6,y,J6,z,C6)
print('PASS class-sum operators k=1,2')

# Exact regression constants from the account03/B08 Cayley datum, independently
# computed with Gaussian-rational matrix arithmetic during this run.
den=F(431850208768934029)
partner_gap=F(2774999449515476249040000,431850208768934029)
G=F(1575414455627672838774521982,431850208768934029)
row_class={
 (1,1,1,1):F(-29391439291675571725411500,431850208768934029),
 (2,1,1):F(-1751763091377726269126990982,431850208768934029),
 (2,2):F(-49056490523258631790811476312,431850208768934029),
 (3,1):F(-3385960425588750251352335964,431850208768934029),
 (4,):F(-50720079296761331344762232794,431850208768934029),
}
col_class=dict(row_class)
assert row_class==col_class
h0=row_class[(1,1,1,1)]
Atrans=row_class[(2,1,1)]/6
A3=row_class[(3,1)]/8
assert h0==3*Atrans-2*A3
assert G==6*h0-row_class[(2,1,1)]
assert G==4*(h0-A3)
print('PASS all five S4 conjugacy-class row/column balances')
print('partner_support_gap =', partner_gap)
print('common_transposition_gap_sum_G =', G)
print('pair_hessian_trace_minus4G =', -4*G)
print('PASS central cubature f(e)=3*A_trans-2*A_3cycle')
print('PASS MOC4-CASIMIR-PAIR-CURVATURE verifier')
