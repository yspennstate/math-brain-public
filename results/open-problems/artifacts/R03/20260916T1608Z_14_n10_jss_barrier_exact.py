from fractions import Fraction
from itertools import product

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A)
    if n==0: return 1
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]

def gl2(m):
    z=1
    for i in range(m):
        z *= 2**m - 2**i
    return z

def normalized_binary(B):
    n=len(B)
    b11=B[0][0]
    N=[[B[i][j]*B[i][0]*B[0][j]*b11 for j in range(n)] for i in range(n)]
    A=[[(1-N[i][j])//2 for j in range(1,n)] for i in range(1,n)]
    return N,A

# Exhaustive self-check of sign/binary singularity equivalence through n=4.
for n in range(1,5):
    sing_sign=0
    for flat in product((-1,1), repeat=n*n):
        B=[flat[i*n:(i+1)*n] for i in range(n)]
        N,A=normalized_binary(B)
        assert all(x==1 for x in N[0])
        assert all(N[i][0]==1 for i in range(n))
        dB=det_bareiss(B)
        dN=det_bareiss(N)
        dA=det_bareiss(A)
        assert (dB==0)==(dN==0)==(dA==0)
        assert dN == ((-2)**(n-1))*dA
        sing_sign += (dB==0)
    if n==1:
        sing_bin=0
    else:
        m=n-1
        sing_bin=0
        for flat in product((0,1), repeat=m*m):
            A=[flat[i*m:(i+1)*m] for i in range(m)]
            sing_bin += det_bareiss(A)==0
    assert Fraction(sing_sign,2**(n*n)) == Fraction(sing_bin,2**((n-1)**2))
    print("normalize-check",n,sing_sign,"PASS")

# General finite-field certificate at n=10.
n=10
m=n-1
T=2**(m*m)
G=gl2(m)
p_upper=Fraction(T-G,T)
b_upper=2**n*p_upper - 2*n*(n-1)
print("GL(9,2)",G)
print("F2 upper p10",p_upper, float(p_upper))
print("certified b10",b_upper, float(b_upper))

# Approved OEIS A046747 order-9 datum; arithmetic transformation only.
# This script DOES NOT independently certify the OEIS enumeration.
S9=902_616_230_040_448_613_437_952
p_oeis=Fraction(S9,2**81)
b_oeis=2**10*p_oeis-180
print("OEIS-A046747 S9",S9)
print("OEIS-derived candidate exact p10",p_oeis,float(p_oeis))
print("OEIS-derived candidate exact b10",b_oeis,float(b_oeis))
assert p_oeis <= p_upper
assert b_oeis <= b_upper

# Prior exact small values from A046747 through order 8, for regression only.
S=[None,1,10,338,42976,21040112,39882864736,292604283435872,8286284310367538176,S9]
for nn in range(2,11):
    p=Fraction(S[nn-1],2**((nn-1)**2))
    b=2**nn*p-2*nn*(nn-1)
    print("source-table b",nn,b,float(b))

print("SELF-CHECK PASS")
