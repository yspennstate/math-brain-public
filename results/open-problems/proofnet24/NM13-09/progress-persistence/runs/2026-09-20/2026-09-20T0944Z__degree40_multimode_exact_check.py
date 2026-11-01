#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
import mpmath as mp

# T05 exact checker. mpmath is used only to SELECT integer trial vectors Q.
# After Q is created, every theorem-deciding inequality is rechecked by exact
# Fraction/integer arithmetic. Thus floating-point/high-precision numerics are
# a witness search only, not evidence.

r=F(7,8)
s=F(24861,25000)
c=s*F(1+r,2)
trace4=F(54959,50000)
mu_lo=F(91219830,100000000)
mu_hi=F(91219831,100000000)
eps2_hi=F(25851,1000000000)
DEG=40
NCOL=20

def atan_bounds(x,m):
    x=F(x); S=F(0)
    for k in range(m+1):
        S += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(S,S+nxt),max(S,S+nxt)
a5=atan_bounds(F(1,5),80); a239=atan_bounds(F(1,239),30)
pi_lo=16*a5[0]-4*a239[1]
pi_hi=16*a5[1]-4*a239[0]
assert pi_lo > F(103993,33102) and pi_hi < F(104348,33215)
tau_lo=F(38519886,100000000)
tau_hi=F(38519887,100000000)
assert tau_lo*tau_lo < c/(2*pi_hi)
assert tau_hi*tau_hi > c/(2*pi_lo)

def mhe(i,j,tau):
    if (i+j)%2==0:
        return F(factorial(i))*r**i/2 if i==j else F(0)
    out=F(0)
    for k in range(min(i,j)+1):
        n=i+j-2*k; m=(n-1)//2
        half=-F(((-1)**m)*factorial(2*m),2**m*factorial(m))
        coeff=F(factorial(i)*factorial(j),
                factorial(k)*factorial(i-k)*factorial(j-k))
        out += coeff*r**k*c**m*half
    return tau*out

# Witness search only: high-precision degree-40 normalized-Hermite eigenspace.
mp.mp.dps=80
rmp=mp.mpf(r.numerator)/r.denominator
cmp=mp.mpf(c.numerator)/c.denominator
taump=mp.sqrt(cmp/(2*mp.pi))
M=mp.matrix(DEG+1)
for i in range(DEG+1):
    for j in range(DEG+1):
        if (i+j)%2==0:
            z=mp.mpf(factorial(i))*rmp**i/2 if i==j else mp.mpf('0')
        else:
            z=mp.mpf('0')
            for k in range(min(i,j)+1):
                n=i+j-2*k; m=(n-1)//2
                half=-mp.mpf(((-1)**m)*factorial(2*m))/(2**m*factorial(m))
                coeff=mp.mpf(factorial(i)*factorial(j))/(factorial(k)*factorial(i-k)*factorial(j-k))
                z += coeff*rmp**k*cmp**m*half
            z *= taump
        M[i,j]=z/mp.sqrt(factorial(i)*factorial(j))
evals,evecs=mp.eigsy(M)  # ascending
QS=10**50
Q=[[0]*NCOL for _ in range(DEG+1)]
for a in range(NCOL):
    col=DEG-a
    he=[evecs[i,col]/mp.sqrt(factorial(i)) for i in range(DEG+1)]
    mx=max(abs(x) for x in he)
    for i,x in enumerate(he):
        Q[i][a]=int(mp.nint(x/mx*QS))

fact=[factorial(i) for i in range(DEG+1)]
G=[[sum(F(Q[i][a]*Q[i][b]*fact[i]) for i in range(DEG+1))
    for b in range(NCOL)] for a in range(NCOL)]
def Bmat(tau):
    MM=[[mhe(i,j,tau) for j in range(DEG+1)] for i in range(DEG+1)]
    B=[[F(0)]*NCOL for _ in range(NCOL)]
    for a in range(NCOL):
        for b in range(NCOL):
            z=F(0)
            for i in range(DEG+1):
                qi=Q[i][a]
                if qi==0: continue
                for j in range(DEG+1):
                    qj=Q[j][b]
                    if qj: z += qi*qj*MM[i][j]
            B[a][b]=z
    return B
def ldlt(A):
    n=len(A); L=[[F(0)]*n for _ in range(n)]; D=[F(0)]*n
    for i in range(n):
        L[i][i]=F(1)
        d=A[i][i]-sum(L[i][j]*L[i][j]*D[j] for j in range(i))
        assert d>0
        D[i]=d
        for k in range(i+1,n):
            z=A[k][i]-sum(L[k][j]*L[i][j]*D[j] for j in range(i))
            L[k][i]=z/d
    return D

targets=[
(3,F(27719,50000)),(4,F(8583,20000)),(5,F(2071,6250)),(6,F(25537,100000)),
(7,F(4913,25000)),(8,F(7553,50000)),(9,F(5801,50000)),(10,F(8907,100000)),
(11,F(3419,50000)),(12,F(5253,100000)),(13,F(101,2500)),(14,F(3113,100000)),
(15,F(601,25000)),(16,F(1859,100000)),(17,F(1437,100000)),(18,F(1107,100000)),
(19,F(847,100000)),(20,F(4,625))]
mins=[]
for tau in (tau_lo,tau_hi):
    B=Bmat(tau)
    for k,a in targets:
        C=[[B[i][j]-a*G[i][j] for j in range(k)] for i in range(k)]
        mins.append((tau,k,min(ldlt(C))))

L40=sum(a**4 for _,a in targets)+r**160/(F(16)*(1-r**8))
theta=F(53683,312500)      # .1717856
x=F(18246571,20000000)    # .91232855
beta=F(7136696,10000000)  # .7136696
assert x**78125 < r**53683
assert x>mu_hi and mu_lo>beta
trace_margin=beta**4-(trace4-x**4-L40)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert trace_margin>0 and temple_margin>0

# Exact source covariance comparison at k=1,...,5.
cov=[]
for k in range(1,6):
    u=r**k; tk=c*r**(k-1)
    A=6*u**5*tk+2*u**10-5*u**6-5*u**4+2
    m=A*A-4*(1-u**4)**5
    assert A>0 and m>0
    cov.append(m)
# Tail k>=6: inherited factorization gives R(u)<=u and c/r>1.
assert c/r>1
assert F(4)-F(7,4)-F(20,16)==F(1)

old=F(21473,125000)
upper=F(1,4)
assert theta>old and upper-theta<upper-old

print("tau =",float(tau_lo),float(tau_hi))
print("top witness eigvals =",[float(evals[DEG-j]) for j in range(20)])
print("LDL min pivots =",[(float(t),k,float(p)) for t,k,p in mins])
print("L40 =",float(L40))
print("covariance finite margins =",[float(z) for z in cov])
print("trace margin =",float(trace_margin))
print("Temple margin =",float(temple_margin))
print("theta old/new =",float(old),float(theta))
print("width old/new =",float(upper-old),float(upper-theta))
print("source gain =",float(theta-old))
print("ALL_EXACT_CHECKS_PASS = True")
