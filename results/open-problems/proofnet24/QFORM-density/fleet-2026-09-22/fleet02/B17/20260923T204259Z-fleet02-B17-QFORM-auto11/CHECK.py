from fractions import Fraction
from math import sqrt, log

# Exact physical matrix A=(1/6)M.
Mint = [
    [1,1,-2,-2,-2,-2],
    [1,1,-2,-2,-2,-2],
    [-2,-2,1,1,-2,-2],
    [-2,-2,1,1,-2,-2],
    [-2,-2,-2,-2,1,1],
    [-2,-2,-2,-2,1,1],
]
A = [[Fraction(x,6) for x in row] for row in Mint]

def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))]
            for i in range(len(X))]

def rank_q(X):
    B=[row[:] for row in X]
    m,n=len(B),len(B[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if B[i][c] != 0), None)
        if p is None:
            continue
        B[r],B[p]=B[p],B[r]
        z=B[r][c]
        B[r]=[x/z for x in B[r]]
        for i in range(m):
            if i != r and B[i][c] != 0:
                z=B[i][c]
                B[i]=[B[i][j]-z*B[r][j] for j in range(n)]
        r += 1
    return r

A2=mm(A,A); A3=mm(A2,A)
assert A3 == A
assert rank_q(A) == 3
assert sum(A[i][i] for i in range(6)) == 1
# Symmetry + A^3=A + rank 3 + trace 1 forces nonzero spectrum {1,1,-1}.

pstar = (-165/4 + 12*sqrt(3) + 15*sqrt(2)
         + 22*sqrt(3)*log((sqrt(6)+3*sqrt(2))/6)
         + sqrt(3)*log((1+sqrt(2)-1/sqrt(3))/(1+sqrt(2)+1/sqrt(3))))
assert pstar < 508/125
assert pstar < 3*sqrt(2)

# General countable-fragment certificate at latent nonkernel-center gap Delta>=84.
assert Fraction(140,33) - (Fraction(508,125)+Fraction(588,3311)) == Fraction(148,177375)
assert 140*140 < 18*33*33  # 140/33 < 3 sqrt(2)

# Explicit eta=1/1000 two-fragment stress family, global R>=110 certificate.
assert 506*1000**4 - 508*999**4 == 28954031492
# Hence (999/1000)^4*(508/125) < 506/125.
assert Fraction(140,33) - (Fraction(506,125)+Fraction(588,3031)) == Fraction(766,1786125)

print('PASS QFORM-DENSE-FRAGMENT-GLOBAL-AGGREGATE-v1')
print('rank(A)=', rank_q(A), 'trace(A)=', sum(A[i][i] for i in range(6)))
print('A^3=A:', A3 == A, '=> nonzero spectrum {1,1,-1}')
print('p_* = %.15f' % pstar)
print('3sqrt(2)-p_* = %.15f' % (3*sqrt(2)-pstar))
print('Delta>=84 upper = %.15f' % float(Fraction(508,125)+Fraction(588,3311)))
print('140/33 = %.15f' % float(Fraction(140,33)))
print('R>=110 upper = %.15f' % float(Fraction(506,125)+Fraction(588,3031)))
print('R>=110 rational margin to 140/33 =', Fraction(766,1786125))
