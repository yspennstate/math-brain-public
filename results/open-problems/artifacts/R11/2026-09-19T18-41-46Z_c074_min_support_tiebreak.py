from fractions import Fraction as F
from itertools import combinations

def rref_rank(mat):
    A=[list(map(F,row)) for row in mat]
    if not A: return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def phi(x,p=5,d=3): return pow(x,d,p)
def vt(t,A,B,p=5,d=3):
    vals={x:phi((t+x)%p,p,d) for x in set(A)|set(B)}
    q=F(0)
    for u in range(1,p):
        good=(all(vals[a]<u for a in A) and all(vals[b]>=u for b in B)) or (all(vals[b]<u for b in B) and all(vals[a]>=u for a in A))
        if good:q+=F(p,2*u*(p-u))
    return q
coords=[((0,),(1,)),((0,),(2,)),((1,),(2,)),((0,),(1,2)),((0,1),(2,)),((0,2),(1,))]
V={t:[vt(t,A,B) for A,B in coords] for t in range(5)}
target=[sum((V[t][j] for t in range(5)),F(0))/5 for j in range(6)]

def matrices(S):
    A=[[V[t][j] for t in S] for j in range(6)] + [[F(1) for _ in S]]
    b=target+[F(1)]
    return A,b

def solves(S,W):
    A,b=matrices(S)
    return all(sum((row[i]*W[i] for i in range(len(S))),F(0))==bb for row,bb in zip(A,b))

# All supports of size <=3 are affine-infeasible except (1,2,4), whose unique solution has a negative weight.
for r in range(1,4):
    for S in combinations(range(5),r):
        A,b=matrices(S)
        rankA=rref_rank(A); rankAug=rref_rank([row+[bb] for row,bb in zip(A,b)])
        if S==(1,2,4):
            W=(F(-1,5),F(4,5),F(2,5))
            assert rankA==3 and rankAug==3 and solves(S,W) and min(W)<0
        else:
            assert rankAug>rankA, (S,rankA,rankAug)

# Four-supports preceding (0,1,3,4) lexicographically have unique affine solutions with a negative weight.
S=(0,1,2,3); W=(F(2,5),F(3,5),F(-2,5),F(2,5))
A,b=matrices(S); assert rref_rank(A)==4 and rref_rank([row+[bb] for row,bb in zip(A,b)])==4 and solves(S,W) and min(W)<0
S=(0,1,2,4); W=(F(0),F(-1,5),F(4,5),F(2,5))
A,b=matrices(S); assert rref_rank(A)==4 and rref_rank([row+[bb] for row,bb in zip(A,b)])==4 and solves(S,W) and min(W)<0

# The next four-support is the first nonnegative feasible support, with strictly positive weights.
S=(0,1,3,4); W=(F(4,15),F(1,3),F(4,15),F(2,15))
A,b=matrices(S); assert rref_rank(A)==4 and rref_rank([row+[bb] for row,bb in zip(A,b)])==4
assert solves(S,W) and sum(W)==1 and all(w>0 for w in W)

print('C074_MIN_SUPPORT_TIEBREAK_EXACT_CHECK')
print('minimum_nonnegative_support=4')
print('lex_first_minimum_support=0,1,3,4')
print('weights=4/15,1/3,4/15,2/15')
print('ALL_EXACT_MIN_SUPPORT_CHECKS_PASS')
