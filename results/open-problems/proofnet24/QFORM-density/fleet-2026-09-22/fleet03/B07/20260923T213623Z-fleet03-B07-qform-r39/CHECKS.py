from itertools import combinations, product
from decimal import Decimal, getcontext, ROUND_CEILING
import random, math


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def minor_det3(A,I,J):
    return det3([[A[i][j] for j in J] for i in I])


def masses(A):
    n=len(A); M=[0,0,0,0]; triples=list(combinations(range(n),3))
    for I in triples:
        SI=set(I)
        for J in triples:
            d=minor_det3(A,I,J)
            M[len(SI.intersection(J))]+=d*d
    return M


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A): return sum(A[i][i] for i in range(len(A)))


def e3_by_traces(B):
    B2=matmul(B,B); B3=matmul(B2,B)
    p1,p2,p3=tr(B),tr(B2),tr(B3)
    num=p1**3-3*p1*p2+2*p3
    assert num%6==0
    return num//6


def crossing_mass(A,L):
    n=len(A); L=set(L); R=set(range(n))-L
    if len(L)<3 or len(R)<3: return 0
    ans=0
    for I in combinations(sorted(L),3):
        for J in combinations(sorted(R),3):
            d=minor_det3(A,I,J); ans+=d*d
    return ans


def G1(A,col):
    H=[i for i,c in enumerate(col) if c==0]
    L=[i for i,c in enumerate(col) if c==1]
    R=[i for i,c in enumerate(col) if c==2]
    ans=0
    for a in H:
        for U in combinations(L,2):
            for V in combinations(R,2):
                d=minor_det3(A,(a,)+U,(a,)+V); ans+=d*d
    return ans


def G2(A,col):
    H=[i for i,c in enumerate(col) if c==0]
    L=[i for i,c in enumerate(col) if c==1]
    R=[i for i,c in enumerate(col) if c==2]
    ans=0
    for S in combinations(H,2):
        for u in L:
            for v in R:
                d=minor_det3(A,S+(u,),S+(v,)); ans+=d*d
    return ans


random.seed(3907)
for rep in range(12):
    n=6
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            x=random.randint(-3,3); A[i][j]=A[j][i]=x
    M=masses(A)
    A2=matmul(A,A)
    assert sum(M)==e3_by_traces(A2)

    sumcross=0
    for bits in product([0,1], repeat=n):
        sumcross += crossing_mass(A,[i for i,b in enumerate(bits) if b])
    assert 64*sumcross==(2**n)*M[0]

    # Old r20 q=1 probabilities p(H,L,R)=(1,2,2)/5.
    sw1=0
    # Old r20 q=2 probabilities p(H,L,R)=(2,1,1)/4.
    sw2=0
    for col in product(range(3), repeat=n):
        hcount=sum(c==0 for c in col); lr=n-hcount
        sw1 += (2**lr)*G1(A,col)
        sw2 += (2**hcount)*G2(A,col)
    assert 3125*sw1==16*(5**n)*M[1]
    assert 64*sw2==(4**n)*M[2]

C3=3*(2**(4/3))*math.exp(1/3)
Cmac=C3*(2**(4/3))

# High-precision arithmetic is required here: N0 is about 1e39, so binary64
# cannot certify its final digits. Decimal precision 120 is ample.
getcontext().prec=120
sqrt2=Decimal(2).sqrt()
hD=(Decimal(2)*sqrt2-Decimal(1))/Decimal(1572864)
Nstar=Decimal(65536)/(Decimal(27)*(hD**6))
N0=int(Nstar.to_integral_value(rounding=ROUND_CEILING))
assert N0==983551868769507679208432245932178290488

def count_disjoint(n):
    return math.comb(n,3)*math.comb(n-3,3) if n>=6 else 0

lo,hi=6,10_000_000
while lo<hi:
    mid=(lo+hi)//2
    if count_disjoint(mid)>=N0: hi=mid
    else: lo=mid+1
assert lo==5730381
assert count_disjoint(lo-1)<N0<=count_disjoint(lo)

print('EXACT_INTEGER_INSTANCES=12')
print('C3=',repr(C3))
print('O0_MACRO_DENSITY_CONSTANT=',repr(Cmac))
print('h_decimal=',hD)
print('N0_threshold_decimal=',Nstar)
print('N0_MIN=',N0)
print('n_MIN=',lo)
print('STATUS=PASS')
