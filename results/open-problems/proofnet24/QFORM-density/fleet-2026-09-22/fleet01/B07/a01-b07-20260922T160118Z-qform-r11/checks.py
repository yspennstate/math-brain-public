from fractions import Fraction
from itertools import combinations


def det(M):
    M=[row[:] for row in M]
    n=len(M)
    out=Fraction(1)
    sign=1
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            M[c],M[p]=M[p],M[c]
            sign *= -1
        piv=M[c][c]
        out *= piv
        for r in range(c+1,n):
            fac=M[r][c]/piv
            for j in range(c+1,n):
                M[r][j] -= fac*M[c][j]
    return sign*out


def sub(M,R,C):
    return [[M[i][j] for j in C] for i in R]


def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))]
            for i in range(len(X))]

# Partner stress matrix A=I_4-J_4/3.
A=[[Fraction(int(i==j),1)-Fraction(1,3) for j in range(4)] for i in range(4)]
A2=mm(A,A)

# P=I-J/4 is projector onto the three +1 eigendirections.
P=[[Fraction(int(i==j),1)-Fraction(1,4) for j in range(4)] for i in range(4)]
for R in combinations(range(4),3):
    assert det(sub(P,R,R)) == Fraction(1,4)
    assert det(sub(A,R,R)) == 0
    assert det(sub(A2,R,R)) == Fraction(1,3)

# Packet J={0,1}, T=J has two row triples and selected-core mass 1/2.
packet=[(0,1,2),(0,1,3)]
mT=sum(det(sub(P,R,R)) for R in packet)
assert mT == Fraction(1,2)
row_volume=sum(det(sub(A2,R,R)) for R in packet)
assert row_volume == Fraction(2,3)
assert row_volume >= mT

# Exact Cauchy-Binet and overlap decomposition.
classes={h:Fraction(0) for h in range(4)}
for R in packet:
    cb=Fraction(0)
    for K in combinations(range(4),3):
        d=det(sub(A,R,K))
        cb += d*d
        classes[len(set(R)&set(K))] += d*d
    assert cb == det(sub(A2,R,R))

assert classes[0] == 0
assert classes[1] == 0
assert classes[2] == Fraction(2,3)
assert classes[3] == 0
assert sum(classes.values()) == row_volume

# Optimized coloring capture probabilities used in the report.
assert Fraction(1,2)**6 == Fraction(1,64)                       # h=0
assert Fraction(1,5)*Fraction(2,5)**4 == Fraction(16,3125)      # h=1
assert Fraction(1,2)**2*Fraction(1,4)**2 == Fraction(1,64)      # h=2

print('QFORM_PLUCKER_TO_PHYSICAL_ROWVOLUME_CHECK_PASS')
print('mT=', mT)
print('row_volume=', row_volume)
print('overlap_classes=', classes)
