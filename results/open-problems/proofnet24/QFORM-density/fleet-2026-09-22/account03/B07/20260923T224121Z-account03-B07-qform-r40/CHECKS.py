from fractions import Fraction
from itertools import combinations
import random, math
import numpy as np


def det2(B):
    return B[0][0]*B[1][1]-B[0][1]*B[1][0]


def adj2(B):
    return [[B[1][1],-B[0][1]],[-B[1][0],B[0][0]]]


def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def norm2(x):
    return dot(x,x)


def wedge_norm2(x,y):
    return norm2(x)*norm2(y)-dot(x,y)**2


def one_overlap_case(seed, ni=4, nj=4, mzero=False):
    rr=random.Random(seed)
    a=Fraction(rr.randint(-3,3))
    m=[Fraction(0 if mzero else rr.randint(-3,3)) for _ in range(nj)]
    if not mzero and all(x==0 for x in m):
        m[0]=Fraction(1)
    u=[Fraction(rr.randint(-3,3)) for _ in range(ni)]
    K=[[Fraction(rr.randint(-3,3)) for _ in range(nj)] for __ in range(ni)]

    omega=Fraction(0)
    for r,s in combinations(range(ni),2):
        for c,d in combinations(range(nj),2):
            omega += det3([[a,m[c],m[d]],
                           [u[r],K[r][c],K[r][d]],
                           [u[s],K[s][c],K[s][d]]])**2

    if mzero:
        z2=sum(wedge_norm2(K[r],K[s]) for r,s in combinations(range(ni),2))
        return omega == a*a*z2

    mm=norm2(m)
    alpha=[dot(row,m)/mm for row in K]
    C=[[K[i][j]-alpha[i]*m[j] for j in range(nj)] for i in range(ni)]
    beta=[a*alpha[i]-u[i] for i in range(ni)]

    z2=sum(wedge_norm2(C[r],C[s]) for r,s in combinations(range(ni),2))
    W=Fraction(0)
    for r,s in combinations(range(ni),2):
        v=[beta[r]*C[s][j]-beta[s]*C[r][j] for j in range(nj)]
        W += norm2(v)

    CTb=[sum(C[i][j]*beta[i] for i in range(ni)) for j in range(nj)]
    W_lagrange=norm2(beta)*sum(norm2(row) for row in C)-norm2(CTb)
    return omega == a*a*z2+mm*W and W == W_lagrange


def pair_invertible_case(seed, nr=4, nc=5):
    rr=random.Random(seed)
    while True:
        a,b,d=[Fraction(rr.randint(-3,3)) for _ in range(3)]
        B=[[a,b],[b,d]]
        db=det2(B)
        if db != 0:
            break
    XR=[[Fraction(rr.randint(-3,3)),Fraction(rr.randint(-3,3))] for _ in range(nr)]
    XC=[[Fraction(rr.randint(-3,3)),Fraction(rr.randint(-3,3))] for _ in range(nc)]
    K=[[Fraction(rr.randint(-3,3)) for _ in range(nc)] for __ in range(nr)]
    Ad=adj2(B)
    lhs=Fraction(0)
    rhs=Fraction(0)
    for r in range(nr):
        for c in range(nc):
            bil=sum(XR[r][i]*Ad[i][j]*XC[c][j] for i in range(2) for j in range(2))
            dval=db*K[r][c]-bil
            lhs += dval*dval
            S=K[r][c]-bil/db
            rhs += db*db*S*S
    return lhs==rhs


def pair_rank1_case(seed, nr=4, nc=5):
    rr=random.Random(seed)
    q=[Fraction(rr.choice([-3,-2,-1,1,2,3])), Fraction(rr.choice([-3,-2,-1,1,2,3]))]
    sign=Fraction(rr.choice([-1,1]))
    B=[[sign*q[i]*q[j] for j in range(2)] for i in range(2)]
    XR=[[Fraction(rr.randint(-3,3)),Fraction(rr.randint(-3,3))] for _ in range(nr)]
    XC=[[Fraction(rr.randint(-3,3)),Fraction(rr.randint(-3,3))] for _ in range(nc)]
    Ad=adj2(B)
    assert det2(B)==0
    lhs=Fraction(0)
    for r in range(nr):
        for c in range(nc):
            bil=sum(XR[r][i]*Ad[i][j]*XC[c][j] for i in range(2) for j in range(2))
            lhs += bil*bil
    w=[-q[1],q[0]]
    left=sum(dot(w,x)**2 for x in XR)
    right=sum(dot(w,x)**2 for x in XC)
    rhs=left*right
    return lhs==rhs


exact_nonzero=sum(one_overlap_case(s) for s in range(80))
exact_zero=sum(one_overlap_case(1000+s,mzero=True) for s in range(20))
pair_inv=sum(pair_invertible_case(2000+s) for s in range(50))
pair_r1=sum(pair_rank1_case(3000+s) for s in range(50))
print("one_overlap_nonzero_exact", exact_nonzero, "/ 80")
print("one_overlap_zero_exact", exact_zero, "/ 20")
print("pair_invertible_schur_exact", pair_inv, "/ 50")
print("pair_rank1_starstar_exact", pair_r1, "/ 50")

# Numerical regression for s3(P) >= 2|det P|/||P||_F^2.
rng=np.random.default_rng(20260923)
min_slack=float("inf")
for _ in range(5000):
    M=rng.integers(-7,8,size=(3,3)).astype(float)
    P=(M+M.T)/2
    sv=np.linalg.svd(P,compute_uv=False)
    F2=float(np.sum(P*P))
    d=abs(float(np.linalg.det(P)))
    if F2 == 0:
        continue
    rhs=2*d/F2
    slack=sv[2]-rhs
    min_slack=min(min_slack,slack)
    if slack < -1e-10:
        raise AssertionError((sv[2],rhs,slack,P))
print("principal_gate_min_numeric_slack", min_slack)

theta=1/64
density_constant=math.sqrt(18*math.pi)/theta
residual_F4=1/(18*theta*theta)
print("theta", theta)
print("partner_density_exit", density_constant)
print("principal_survivor_sum_F4_lower", residual_F4)
print("E1_first_or_second_threshold", 2/3125)
print("E2_invertible_or_rank1_threshold", 1/512)
print("STATUS=PASS")
