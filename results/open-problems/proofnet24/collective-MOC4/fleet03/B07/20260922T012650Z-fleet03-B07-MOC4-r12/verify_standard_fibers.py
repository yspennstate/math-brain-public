from itertools import permutations
from fractions import Fraction

H = [
    [1,1,1,1],
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
]
PAIR_CLASSES = [
    {frozenset((0,1)), frozenset((2,3))},
    {frozenset((0,2)), frozenset((1,3))},
    {frozenset((0,3)), frozenset((1,2))},
]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(x) for x in zip(*A)]

def pm(sig):
    P=[[0]*4 for _ in range(4)]
    for i,j in enumerate(sig):
        P[i][j]=1
    return P

def induced(sig):
    out=[]
    reps=[frozenset((0,1)),frozenset((0,2)),frozenset((0,3))]
    for S in reps:
        image=frozenset(sig[i] for i in S)
        out.append(next(k for k,C in enumerate(PAIR_CLASSES) if image in C))
    return tuple(out)

fibers={}
for sig in permutations(range(4)):
    M=mm(mm(H,pm(sig)),tr(H))
    M=[[Fraction(x,4) for x in row] for row in M]
    assert M[0][0] == 1
    assert all(M[0][j] == 0 for j in range(1,4))
    assert all(M[i][0] == 0 for i in range(1,4))
    S=[[int(M[i+1][j+1]) for j in range(3)] for i in range(3)]
    assert all(sum(abs(x) for x in row)==1 for row in S)
    assert all(sum(abs(S[i][j]) for i in range(3))==1 for j in range(3))
    rho=induced(sig)
    R=[[0]*3 for _ in range(3)]
    for i,j in enumerate(rho):
        R[i][j]=1
    assert [[abs(x) for x in row] for row in S] == R
    signs=tuple(S[i][rho[i]] for i in range(3))
    assert signs[0]*signs[1]*signs[2] == 1
    fibers.setdefault(rho,set()).add(signs)

expected={(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)}
assert len(fibers)==6
assert all(v==expected for v in fibers.values())
print('PASS')
print('permutations_checked',24)
print('fibers_checked',6)
print('fiber_sign_patterns',sorted(expected))
