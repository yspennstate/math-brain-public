from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter

def mat_rank(M):
    A=[list(map(F,row)) for row in M]
    if not A:
        return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        p=A[r][c]
        A[r]=[x/p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def det(M):
    A=[list(map(F,row)) for row in M]
    n=len(A)
    assert all(len(row)==n for row in A)
    s=F(1)
    for c in range(n):
        piv=next((i for i in range(c,n) if A[i][c]),None)
        if piv is None:
            return F(0)
        if piv!=c:
            A[c],A[piv]=A[piv],A[c]
            s=-s
        p=A[c][c]
        s*=p
        for i in range(c+1,n):
            if A[i][c]:
                q=A[i][c]/p
                for j in range(c+1,n):
                    A[i][j]-=q*A[c][j]
                A[i][c]=F(0)
    return s

def solve2(M,b):
    a,c=M[0]; d,e=M[1]
    D=a*e-c*d
    if D==0:
        return None
    return ((b[0]*e-c*b[1])/D,(a*b[1]-b[0]*d)/D)

def solve_square(M,b):
    n=len(M)
    aug=[list(map(F,M[i]))+[F(b[i])] for i in range(n)]
    for c in range(n):
        piv=next(i for i in range(c,n) if aug[i][c])
        aug[c],aug[piv]=aug[piv],aug[c]
        p=aug[c][c]
        aug[c]=[z/p for z in aug[c]]
        for i in range(n):
            if i!=c and aug[i][c]:
                q=aug[i][c]
                aug[i]=[aug[i][j]-q*aug[c][j] for j in range(n+1)]
    return tuple(aug[i][-1] for i in range(n))

def affine_dim(points):
    if len(points)<=1:
        return 0
    base=points[0]
    D=[[p[j]-base[j] for j in range(len(base))] for p in points[1:]]
    return mat_rank(D)

def avg(points):
    n=F(len(points))
    return tuple(sum(p[j] for p in points)/n for j in range(len(points[0])))

def volume4_from_facets(points, facets):
    facets=[frozenset(f) for f in facets]
    assert all(affine_dim([points[i] for i in FF])==3 for FF in facets)
    total=F(0)
    for fi,FF in enumerate(facets):
        gF=avg([points[i] for i in FF])
        ridges=set()
        for gj,GG in enumerate(facets):
            if gj==fi:
                continue
            R=FF & GG
            if len(R)>=3 and affine_dim([points[i] for i in R])==2:
                ridges.add(frozenset(R))
        for RR in ridges:
            gR=avg([points[i] for i in RR])
            edges=set()
            for GG in facets:
                E=RR & GG
                if len(E)>=2 and affine_dim([points[i] for i in E])==1:
                    edges.add(frozenset(E))
            assert all(len(E)==2 for E in edges)
            for E in edges:
                ia,ib=tuple(E)
                cols=[gF,gR,points[ia],points[ib]]
                M=[[cols[c][r] for c in range(4)] for r in range(4)]
                total += abs(det(M))/F(24)
    return total

# Five oriented cube-edge section vertices. Row j is interior in coordinate j,
# all other coordinates are saturated; coordinate 6 is oriented to +1.
Q=[
    [F(1,6), -1, -1, 1, 1, 1],
    [1, F(1,7), -1, -1, -1, 1],
    [-1, 1, F(-1,4), 1, 1, 1],
    [-1, -1, 1, F(-1,9), 1, 1],
    [-1, 1, 1, -1, F(-1,6), 1],
]
Q=[[F(x) for x in row] for row in Q]

# Exact codimension-two section L=ker(B).
B=[
    [F(564),F(245),F(224),F(-189),F(564),F(0)],
    [F(564),F(140),F(504),F(315),F(0),F(235)],
]

assert all(sum(B[r][k]*Q[j][k] for k in range(6))==0
           for r in range(2) for j in range(5))
assert mat_rank(Q)==4
assert all(mat_rank([Q[i] for i in I])==4 for I in combinations(range(5),4))

# Unique affine dependence; all coefficients nonzero.
lam=[F(-12),F(7),F(8),F(9),F(-12)]
assert sum(lam)==0 and all(x!=0 for x in lam)
assert all(sum(lam[i]*Q[i][j] for i in range(5))==0 for j in range(6))

# Signed-subset contraction identities from the sign matrix.
S=[{2,3,4},{0,3},{0,1},{1,4},{1}]
for j in range(5):
    sj=sum(lam[i] for i in S[j])
    cj=-sj/lam[j]
    assert F(0)<cj<F(1)
    assert Q[j][j]==1-2*cj
    for i in range(5):
        if i!=j:
            assert Q[i][j] == (-1 if i in S[j] else 1)

# Equality-case circuit lines for omitted directions 1,...,5 are pairwise distinct.
for i,j in combinations(range(5),2):
    assert B[0][i]*B[1][j]-B[1][i]*B[0][j] != 0

# Exhaustive exact enumeration of vertices of L cap [-1,1]^6.
verts=set()
for sat in combinations(range(6),4):
    free=[i for i in range(6) if i not in sat]
    M=[[B[r][free[c]] for c in range(2)] for r in range(2)]
    if det(M)==0:
        continue
    for signs in product((-1,1), repeat=4):
        x=[None]*6
        rhs=[F(0),F(0)]
        for idx,s in zip(sat,signs):
            x[idx]=F(s)
            for r in range(2):
                rhs[r]-=B[r][idx]*F(s)
        sol=solve2(M,rhs)
        x[free[0]],x[free[1]]=sol
        if all(F(-1)<=z<=F(1) for z in x):
            verts.add(tuple(x))

def sat_count(x):
    return sum(abs(z)==1 for z in x)

hist=Counter(sat_count(x) for x in verts)
assert len(verts)==22
assert hist==Counter({4:12,5:10})

Qset={tuple(row) for row in Q}
expected_five=Qset | {tuple(-z for z in row) for row in Q}
actual_five={x for x in verts if sat_count(x)==5}
assert actual_five==expected_five

# Every coordinate inequality is a genuine 3D facet of the section.
for i in range(6):
    for s in (-1,1):
        pts=[x for x in verts if x[i]==s]
        assert affine_dim(pts)==3

# Choose A with rows spanning L. Its columns are the six primal vertex representatives.
A=[Q[i][:] for i in range(4)]
assert mat_rank(A)==4
assert all(sum(B[r][k]*A[a][k] for k in range(6))==0
           for r in range(2) for a in range(4))

Ppoints=[]
labels=[]
for j in range(6):
    v=tuple(A[a][j] for a in range(4))
    Ppoints.append(v); labels.append((j,1))
    Ppoints.append(tuple(-z for z in v)); labels.append((j,-1))
labidx={lab:i for i,lab in enumerate(labels)}

vlist=sorted(verts)
Pfacets=[]
for q in vlist:
    f=[]
    for j,z in enumerate(q):
        if z==1:
            f.append(labidx[(j,1)])
        elif z==-1:
            f.append(labidx[(j,-1)])
    Pfacets.append(f)

assert len(Pfacets)==22
assert Counter(map(len,Pfacets))==Counter({4:12,5:10})
V,Fcnt=12,22
I=sum(map(len,Pfacets))
assert I==98
assert I==4*Fcnt+V-2

# Exact volume of P from its facet/ridge/edge complex.
volP=volume4_from_facets(Ppoints,Pfacets)
assert volP==F(36937,4536)

# Coordinates of the 22 polar vertices in the A-row basis.
M4=[[A[a][j] for a in range(4)] for j in range(4)]
assert det(M4)!=0
Ypoints=[]
for q in vlist:
    y=solve_square(M4,[q[j] for j in range(4)])
    assert all(sum(A[a][j]*y[a] for a in range(4))==q[j] for j in range(6))
    Ypoints.append(y)

# The 12 polar facets correspond to coordinate equalities q_i=+/-1.
Yfacets=[]
for i in range(6):
    for s in (-1,1):
        ids=[k for k,q in enumerate(vlist) if q[i]==s]
        assert affine_dim([Ypoints[k] for k in ids])==3
        Yfacets.append(ids)

volPolar=volume4_from_facets(Ypoints,Yfacets)
assert volPolar==F(17281169,11938752)

VP=volP*volPolar
mahler=F(32,3)
assert VP==F(638314539353,54154179072)
assert VP-mahler==F(60669962585,54154179072)
assert VP/mahler==F(638314539353,577644576768)
assert VP>mahler

print("rank(Q) =",mat_rank(Q))
print("affine_dependence_lambda =",[str(x) for x in lam])
print("section_vertex_count =",len(verts))
print("saturation_histogram =",dict(sorted(hist.items())))
print("five_edge_pairs =",len(actual_five)//2)
print("first_five_B_columns_pairwise_nonparallel = True")
print("primal_V_F_I =",(V,Fcnt,I))
print("incidence_equality =",I,"=",4*Fcnt+V-2)
print("vol(P) =",volP)
print("vol(P^circ) =",volPolar)
print("volume_product =",VP)
print("Mahler_4D_constant =",mahler)
print("exact_excess =",VP-mahler)
print("ratio_to_Mahler =",VP/mahler)
print("ALL_EXACT_CHECKS_PASS = True")
