from fractions import Fraction
import math
import numpy as np
from scipy.linalg import expm

# Finite sanity model for the normalizing-voltage theorem.
# Gamma = Z/7, S = {+-1,+-2}; A = C2^2; Lambda = Z/3.
Gamma = tuple(range(7))
S = (1,6,2,5)
A = ((0,0),(1,0),(0,1),(1,1))
Lam = tuple(range(3))
e1, e2 = (1,0), (0,1)
TA = (e1,e2)
TL = (1,2)
phi = {1:e1, 6:e1, 2:e2, 5:e2}

def ax(a,b):
    return (a[0]^b[0], a[1]^b[1])

states = tuple((g,a,l) for g in Gamma for a in A for l in Lam)
idx = {x:i for i,x in enumerate(states)}
D = len(S)+len(TA)+len(TL)
N = len(states)

# Exact rational transition matrix.
Qx = [[Fraction(0) for _ in range(N)] for __ in range(N)]
for x,(g,a,l) in enumerate(states):
    for s in S:
        y=((g+s)%7, ax(a,phi[s]), l)
        Qx[x][idx[y]] += Fraction(1,D)
    for h in TA:
        y=(g,ax(a,h),l)
        Qx[x][idx[y]] += Fraction(1,D)
    for u in TL:
        y=(g,a,(l+u)%3)
        Qx[x][idx[y]] += Fraction(1,D)

assert all(sum(row)==1 for row in Qx)
assert all(Qx[i][j]==Qx[j][i] for i in range(N) for j in range(N))

# Exact projection checks: Gamma moves at rate 4/8=1/2; Lambda at 2/8=1/4.
for x,(g,a,l) in enumerate(states):
    gm = {}
    lm = {}
    for y,(gg,aa,ll) in enumerate(states):
        if Qx[x][y]:
            gm[gg]=gm.get(gg,Fraction(0))+Qx[x][y]
            lm[ll]=lm.get(ll,Fraction(0))+Qx[x][y]
    assert gm[g] == Fraction(1,2)
    assert all(gm[(g+s)%7] == Fraction(1,8) for s in S)
    assert lm[l] == Fraction(3,4)
    assert all(lm[(l+u)%3] == Fraction(1,8) for u in TL)

# Exact normalizer/commutation check on hidden K=A x Lambda.
K = tuple((a,l) for a in A for l in Lam)
kidx = {x:i for i,x in enumerate(K)}
M = len(K)
Wx = [[Fraction(0) for _ in range(M)] for __ in range(M)]
for x,(a,l) in enumerate(K):
    for h in TA:
        Wx[x][kidx[(ax(a,h),l)]] += Fraction(1,4)
    for u in TL:
        Wx[x][kidx[(a,(l+u)%3)]] += Fraction(1,4)

def matmul(A0,B0):
    n=len(A0); m=len(B0[0]); p=len(B0)
    return [[sum(A0[i][k]*B0[k][j] for k in range(p))
             for j in range(m)] for i in range(n)]

for h in (e1,e2):
    Rx = [[Fraction(0) for _ in range(M)] for __ in range(M)]
    for x,(a,l) in enumerate(K):
        Rx[x][kidx[(ax(a,h),l)]]=1
    assert matmul(Wx,Rx)==matmul(Rx,Wx)

# Voltage values span C2^2, whereas Hom(Z7,C2^2) is trivial.
span = {(0,0)}
changed=True
while changed:
    changed=False
    for a in tuple(span):
        for b in phi.values():
            c=ax(a,b)
            if c not in span:
                span.add(c); changed=True
assert len(span)==4
assert math.gcd(7,2)==1

# Numerical CT TV check (sanity only, not part of asymptotic proof).
Q=np.array([[float(z) for z in row] for row in Qx])
PG=np.zeros((7,7))
for g in Gamma:
    for s in S:
        PG[g,(g+s)%7]+=1/4
PL=np.zeros((3,3))
for l in Lam:
    for u in TL:
        PL[l,(l+u)%3]+=1/2
PA=np.zeros((4,4))
for i,a in enumerate(A):
    for h in TA:
        PA[i,A.index(ax(a,h))]+=1/2

def ct_tv(P,t):
    H=expm(float(t)*(P-np.eye(P.shape[0])))
    return 0.5*np.abs(H[0]-1/P.shape[0]).sum()

print(f"toy_vertices={N} toy_degree={D}")
print("exact_rows_symmetric=PASS")
print("exact_projection_rates=Gamma:1/2,Lambda:1/4")
print("exact_normalizer_commutation=PASS")
print("exact_voltage_span=C2^2; Hom(Z7,C2^2)=0")
for t in (.5,1,2,4,8,12):
    dh=ct_tv(Q,t)
    dg=ct_tv(PG,t/2)
    dl=ct_tv(PL,t/4)
    da=ct_tv(PA,t/4)
    lo=max(dg,dl)
    up=dg+dl+da
    assert lo <= dh+1e-10 and dh <= up+1e-10
    print(f"t={t:4.1f} H={dh:.12f} lower={lo:.12f} upper={up:.12f}")

gap=(3-math.sqrt(5))/7
old=(3-math.sqrt(5))/math.log(5)
beta=.5*(1-math.log(5)/math.log(13))
print(f"class_gap_lower={gap:.12f}")
print(f"old_L2_alpha_threshold={old:.12f}")
print("explicit_alpha=2.000000000000")
print(f"nonLRE_beta={beta:.12f}")
assert 2>old
assert beta>0
print("ALL_CHECKS_PASS")
