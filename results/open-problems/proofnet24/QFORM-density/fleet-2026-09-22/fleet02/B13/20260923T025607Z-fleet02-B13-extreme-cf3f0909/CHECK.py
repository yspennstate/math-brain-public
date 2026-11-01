from fractions import Fraction
import itertools, random, math

def det(M):
    A=[list(map(Fraction,row)) for row in M]
    n=len(A); sign=1; out=Fraction(1)
    for i in range(n):
        p=next((r for r in range(i,n) if A[r][i]),None)
        if p is None: return Fraction(0)
        if p!=i:
            A[i],A[p]=A[p],A[i]; sign=-sign
        piv=A[i][i]; out*=piv
        for r in range(i+1,n):
            if A[r][i]:
                q=A[r][i]/piv
                for c in range(i,n): A[r][c]-=q*A[i][c]
    return sign*out

def sub(A,rows,cols):
    return [[A[r][c] for c in cols] for r in rows]

def e3(M):
    z=Fraction(0)
    for S in itertools.combinations(range(len(M)),3):
        for T in itertools.combinations(range(len(M[0])),3):
            z += det(sub(M,S,T))**2
    return z

rng=random.Random(20260923)
for trial in range(7):
    n=9; A=[[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(r,n):
            v=rng.randint(-5,5); A[r][c]=A[c][r]=v
    if A[0][0]==0: A[0][0]=3
    a=Fraction(A[0][0])
    S=[[Fraction(A[r][c])-Fraction(A[r][0])*Fraction(A[0][c])/a for c in range(1,n)] for r in range(1,n)]
    M=[row[4:8] for row in S[0:4]]
    Z=e3(M)
    W=Fraction(0)
    I=[1,2,3,4]; J=[5,6,7,8]
    for R in itertools.combinations(I,3):
        for C in itertools.combinations(J,3):
            W += det(sub(A,(0,)+R,(0,)+C))**2
    assert W == a*a*Z

Khalf=4*(4/3)**(3/4)
C=Khalf*(6.787)**(3/4)
print('QFORM_B13_ANCHORED4_CHECK_PASS')
print('exact_random_matrices=7')
print(f'K_half={Khalf:.15f}')
print(f'C_cross3_to_Linf={C:.15f}')
