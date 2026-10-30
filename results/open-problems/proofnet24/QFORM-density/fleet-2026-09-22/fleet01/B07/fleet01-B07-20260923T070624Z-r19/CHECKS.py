from fractions import Fraction
from itertools import combinations, product
import random


def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def subdet3(A,R,C):
    return det3([[A[r][c] for c in C] for r in R])


def mat_square(A):
    n=len(A)
    return [[sum(A[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def overlap_masses(A):
    n=len(A)
    W=[0,0,0,0]
    triples=list(combinations(range(n),3))
    for R in triples:
        sR=set(R)
        for C in triples:
            d=subdet3(A,R,C)
            W[len(sR.intersection(C))]+=d*d
    return W


def e3_principal(B):
    return sum(det3([[B[r][c] for c in I] for r in I]) for I in combinations(range(len(B)),3))


def coarse_best(A,h):
    n=len(A)
    W=overlap_masses(A)[h]
    triples=list(combinations(range(n),3))
    items=[]
    for R in triples:
        sR=set(R)
        for C in triples:
            if len(sR.intersection(C))==h:
                d=subdet3(A,R,C)
                if d:
                    items.append((R,C,d*d))
    if h==3:
        return W
    ncolors=2 if h==0 else 3
    best=0
    for color in product(range(ncolors),repeat=n):
        total=0
        for R,C,w in items:
            sR=set(R); sC=set(C)
            if h==0:
                ok=all(color[x]==0 for x in R) and all(color[x]==1 for x in C)
            else:
                ok=(all(color[x]==0 for x in sR&sC)
                    and all(color[x]==1 for x in sR-sC)
                    and all(color[x]==2 for x in sC-sR))
            if ok:
                total+=w
        best=max(best,total)
    return best


random.seed(20260923)
factors=[Fraction(1,64),Fraction(16,3125),Fraction(1,64),Fraction(1,1)]
identity_tests=color_tests=0
for n in range(3,7):
    reps=3 if n<6 else 2
    for _ in range(reps):
        A=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                v=random.randint(-3,3)
                A[i][j]=A[j][i]=v
        W=overlap_masses(A)
        assert sum(W)==e3_principal(mat_square(A))
        identity_tests+=1
        for h in range(4):
            if W[h]:
                assert Fraction(coarse_best(A,h),W[h])>=factors[h]
                color_tests+=1

coarse=[Fraction(1,256),Fraction(4,3125),Fraction(1,256),Fraction(1,4)]
core=[x/2 for x in coarse]
diffuse=[x/12 for x in coarse]
print('exact_identity_tests',identity_tests)
print('bruteforce_coloring_tests',color_tests)
print('active_packet_constants',coarse)
print('core_half_constants',core)
print('diffuse_twelfth_constants',diffuse)
print('QFORM_COARSE_ROLE_COLORING_CHECK_PASS')
