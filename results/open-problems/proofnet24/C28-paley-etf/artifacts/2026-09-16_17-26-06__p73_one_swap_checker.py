#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

p=73
S=(0,1,2,3,5,32,38,41,45,46,52,54,58,61)
INF=p
m=14

assert sp.isprime(p) and p%4==1
assert (m-1)**5 < p**3 <= m**5

def chi(a):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

# full projective Paley conference matrix, finite points 0..p-1 and infinity=p
C=[[0]*(p+1) for _ in range(p+1)]
for i in range(p):
    for j in range(p):
        if i!=j: C[i][j]=chi(i-j)
    C[i][INF]=C[INF][i]=1

# candidate finite principal matrix
A=sp.Matrix([[C[i][j] for j in S] for i in S])
x=sp.symbols('x')
cp=sp.factor(A.charpoly(x).as_expr())
expected=(x-5)*(x-3)**2*(x-1)**3*(x+1)**3*(x+3)**3*(x**2+2*x-51)
assert sp.expand(cp-expected)==0

# Exact switching/equitable structure.
X=(0,5,38,46,54,61)
Y=(1,2,3,32,41,45,52,58)
assert set(X)|set(Y)==set(S) and not(set(X)&set(Y))
d={0:-1,5:-1,38:-1,46:1,54:1,61:1,
   1:1,2:1,3:1,32:1,41:1,45:-1,52:-1,58:-1}
B={(u,v): d[u]*C[u][v]*d[v] for u in S for v in S}
# Cross block is exactly -J.
assert all(B[u,v]==-1 for u in X for v in Y)
# Internal +1 graphs have degrees 1 on X and 4 on Y.
for u in X:
    assert sum(B[u,v]==1 for v in X if v!=u)==1
    assert sum(B[u,v] for v in X)==-3
    assert sum(B[u,v] for v in Y)==-8
for u in Y:
    assert sum(B[u,v]==1 for v in Y if v!=u)==4
    assert sum(B[u,v] for v in X)==-6
    assert sum(B[u,v] for v in Y)==1
Q=sp.Matrix([[-3,-8],[-6,1]])
assert sp.factor(Q.charpoly(x).as_expr())==x**2+2*x-51

# Exact LDL positivity test for integer symmetric matrices.
def ldl_positive(M):
    n=len(M)
    L=[[Fraction(0) for _ in range(n)] for __ in range(n)]
    D=[Fraction(0) for _ in range(n)]
    for i in range(n):
        L[i][i]=Fraction(1)
        di=Fraction(M[i][i])
        for k in range(i):
            di -= L[i][k]*L[i][k]*D[k]
        if di <= 0:
            return False, i, di, D
        D[i]=di
        for j in range(i+1,n):
            val=Fraction(M[j][i])
            for k in range(i):
                val -= L[j][k]*L[i][k]*D[k]
            L[j][i]=val/di
    return True,n,None,D

neighbors=0
min_pivot=None
min_pivot_witness=None
for a in S:
    for b in range(p+1):
        if b in S: continue
        T=tuple(sorted((set(S)-{a})|{b}))
        assert len(T)==m
        # M=A_T+8I; positivity means lambda_min(A_T)>-8 exactly.
        M=[[C[u][v] + (8 if i==j else 0) for j,v in enumerate(T)] for i,u in enumerate(T)]
        ok,idx,bad,D=ldl_positive(M)
        assert ok, (a,b,idx,bad)
        for piv in D:
            if min_pivot is None or piv < min_pivot:
                min_pivot=piv; min_pivot_witness=(a,b)
        neighbors += 1
assert neighbors==14*((p+1)-m)==840

# Rational square-root bounds used in the strict comparison.
rlo=Fraction(1068,125)      # 8.544 < sqrt(73)
rhi=Fraction(1709,200)      # sqrt(73) < 8.545
slo=Fraction(721,200)       # 3.605 < sqrt(13)
shi=Fraction(1803,500)      # sqrt(13) < 3.606
assert rlo*rlo < 73 < rhi*rhi
assert slo*slo < 13 < shi*shi
# candidate Gram denominator positive from rlo - 1 - 2*shi > 0
assert rlo - 1 - 2*shi > 0
# candidate squared condition number >44 iff 90 sqrt(13)>43(sqrt(73)-1)
assert 90*slo > 43*(rhi-1)
# every neighbor has lambda_min>-8 and lambda_max<=13 by Gershgorin;
# f(r)=(r+13)/(r-8) decreases for r>8, so q_neighbor<2693/68<44.
neighbor_q_upper=(rlo+13)/(rlo-8)
assert neighbor_q_upper==Fraction(2693,68)
assert neighbor_q_upper < 44

print('C28_PALEY_ETF_P73_ONE_SWAP_EXACT_CHECK')
print('p=73 m=14 regime_epsilon=1/10')
print('candidate_subset='+repr(S))
print('charpoly='+str(cp))
print('switch_partition_X='+repr(X))
print('switch_partition_Y='+repr(Y))
print('quotient_charpoly='+str(sp.factor(Q.charpoly(x).as_expr())))
print('cross_block_all_minus_one=PASS')
print('internal_plus_degrees_X=1_regular Y=4_regular')
print('projective_one_swap_neighbors_checked='+str(neighbors))
print('all_neighbor_A_plus_8I_exact_LDL_positive=PASS')
print('minimum_LDL_pivot='+str(min_pivot))
print('minimum_LDL_pivot_witness_remove_add='+repr(min_pivot_witness))
print('neighbor_kappa_squared_upper_lt='+str(neighbor_q_upper))
print('candidate_kappa_squared_gt=44')
print('STRICT_ONE_SWAP_LOCAL_MAXIMUM=PASS')
print('ALL_EXACT_CHECKS_PASS')
