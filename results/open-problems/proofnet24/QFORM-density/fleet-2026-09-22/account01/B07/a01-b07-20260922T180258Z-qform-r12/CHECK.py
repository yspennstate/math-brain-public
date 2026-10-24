from fractions import Fraction
from itertools import combinations, permutations
from math import pi, e, sqrt


def det(A):
    n=len(A)
    if n==0:
        return Fraction(1)
    ans=Fraction(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=Fraction(-1 if inv%2 else 1)
        for i,j in enumerate(p):
            term*=A[i][j]
        ans+=term
    return ans


def submat(A,rows,cols):
    return [[A[i][j] for j in cols] for i in rows]

# Exact calibrated diagonal DPP fixture.
ys=[Fraction(73,27),Fraction(73,27),Fraction(1,24)]
ks=[y/(1+y) for y in ys]
theta=sum(ks,Fraction(0))
D=Fraction(1)
for y in ys:
    D*=1+y
avoid=(1-ks[0])*(1-ks[1])
joint=1-avoid
assert theta==Fraction(3,2)
assert ks[0]>Fraction(29,40) and ks[1]>Fraction(29,40)
assert avoid<Fraction(11,40)
assert joint>Fraction(9,20)

# Exact balanced-core factorization fixture.
N=[[Fraction(2),Fraction(1),Fraction(0)],
   [Fraction(1),Fraction(3),Fraction(2)],
   [Fraction(0),Fraction(1),Fraction(1)]]
T=(0,); S=(0,); L0=(1,2); R0=(1,2)
W=Fraction(0)
for k in range(3):
    for I in combinations(L0,k):
        for J in combinations(R0,k):
            W+=det(submat(N,T+I,S+J))**2
Neff=[[Fraction(5,2),Fraction(2)],[Fraction(1),Fraction(1)]]
NNt=[[sum(Neff[i][k]*Neff[j][k] for k in range(2)) for j in range(2)] for i in range(2)]
Iplus=[[NNt[i][j]+(1 if i==j else 0) for j in range(2)] for i in range(2)]
rhs=Fraction(4)*det(Iplus)
assert W==rhs==Fraction(54)

# Account03/B09 source constant for q=29/20, theta=3/2, r=39/20.
q=29/20
theta_f=3/2
r=39/20
p=r/(r-1)
beta=theta_f/(2*q)
Lq=pi*e*sqrt(2/q)
Pr=1+(1-r/2)**(-1/r)
Cr=r**(1/(2*r))/p**(1/(2*p))
C=Pr*(2*pi)**(-0.5)*Cr**(r/2)*(2*(Lq/2)*beta*r/(beta*r-1))**0.5
Cfinal=C*2**(1/24)
assert beta*r>1
assert Cfinal<107

print('theta =',theta)
print('heavy k =',ks[:2],'threshold =',Fraction(29,40))
print('D =',D)
print('heavy-set avoidance =',avoid,'< 11/40')
print('joint hit (diagonal fixture) =',joint,'> 9/20')
print('square-core packet W =',W)
print('factorized RHS =',rhs)
print('beta*r =',beta*r)
print('analytic coefficient before E reduction =',C)
print('final coefficient =',Cfinal,'< 107')
print('STATUS=QFORM_O1_TWOSIDED_HEAVY_PACKET_CHECK_PASS')
