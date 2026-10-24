from fractions import Fraction as F
from itertools import combinations, product, permutations
from collections import Counter

def mat_rank(M):
    A=[list(map(F,row)) for row in M]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        p=A[r][c]; A[r]=[x/p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def det(M):
    A=[list(map(F,row)) for row in M]
    n=len(A)
    assert all(len(row)==n for row in A)
    s=F(1)
    for c in range(n):
        piv=next((i for i in range(c,n) if A[i][c]),None)
        if piv is None: return F(0)
        if piv!=c:
            A[c],A[piv]=A[piv],A[c]; s=-s
        p=A[c][c]; s*=p
        for i in range(c+1,n):
            if A[i][c]:
                q=A[i][c]/p
                for j in range(c+1,n):
                    A[i][j]-=q*A[c][j]
                A[i][c]=F(0)
    return s

def solve_square(M,b):
    n=len(M)
    aug=[list(map(F,M[i]))+[F(b[i])] for i in range(n)]
    for c in range(n):
        piv=next((i for i in range(c,n) if aug[i][c]),None)
        if piv is None: return None
        aug[c],aug[piv]=aug[piv],aug[c]
        p=aug[c][c]; aug[c]=[z/p for z in aug[c]]
        for i in range(n):
            if i!=c and aug[i][c]:
                q=aug[i][c]
                aug[i]=[aug[i][j]-q*aug[c][j] for j in range(n+1)]
    return tuple(aug[i][-1] for i in range(n))

def affine_dim(points):
    if len(points)<=1: return 0
    b=points[0]
    return mat_rank([[p[j]-b[j] for j in range(len(b))] for p in points[1:]])

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
            if gj==fi: continue
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

def facet_cone_contributions(points, facets):
    facets=[frozenset(f) for f in facets]
    out=[]
    for fi,FF in enumerate(facets):
        gF=avg([points[i] for i in FF]); total=F(0)
        ridges=set()
        for gj,GG in enumerate(facets):
            if gj==fi: continue
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
        out.append(total)
    return out

# Exact V=12 boundary witness from the preceding HARD7-01 run.
Q=[
    [F(1,6), -1, -1, 1, 1, 1],
    [1, F(1,7), -1, -1, -1, 1],
    [-1, 1, F(-1,4), 1, 1, 1],
    [-1, -1, 1, F(-1,9), 1, 1],
    [-1, 1, 1, -1, F(-1,6), 1],
]
Q=[[F(x) for x in row] for row in Q]
A=[row[:] for row in Q[:4]]
V=[tuple(A[r][j] for r in range(4)) for j in range(6)]
a=[-1,3,3,3,-1,-6]

# Signed primal points are +v_i,-v_i in this order.
P0=[]
for v in V:
    P0.append(v); P0.append(tuple(-x for x in v))

# Polynomial arithmetic for exact right-hand support tests.
def padd(p,q):
    n=max(len(p),len(q)); r=[F(0)]*n
    for i,x in enumerate(p): r[i]+=x
    for i,x in enumerate(q): r[i]+=x
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def pmul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]+=x*y
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def perm_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

PERMS5=[(p,perm_sign(p)) for p in permutations(range(5))]
moving=[]
for i,v in enumerate(V):
    for s in (1,-1):
        row=[[F(s)*v[j],F(s)*v[j]*F(a[i])] for j in range(4)]
        row.append([F(1)])
        moving.append(row)

def det5poly(row_ids):
    total=[F(0)]
    for perm,sgn in PERMS5:
        term=[F(sgn)]
        for rr,col in enumerate(perm):
            term=pmul(term,moving[row_ids[rr]][col])
        total=padd(total,term)
    return total

def nz_taylor_sign(p):
    for c in p:
        if c: return 1 if c>0 else -1
    return 0

# Exhaust all tetrahedral candidates. A 4-set is a support facet for all
# sufficiently small t>0 iff all nonzero first Taylor signs of the five-point
# affine determinants agree.
right_facets=[]
persistent_coplanar=0
for f in combinations(range(12),4):
    ss=[]
    for k in range(12):
        if k in f: continue
        ss.append(nz_taylor_sign(det5poly(list(f)+[k])))
    nz=[s for s in ss if s]
    if not nz:
        persistent_coplanar+=1
    elif len(set(nz))==1:
        right_facets.append(tuple(f))
assert len(right_facets)==34

def simplicial_volume(points, facets):
    z=F(0)
    for f in facets:
        assert len(f)==4
        cols=[points[i] for i in f]
        M=[[cols[c][r] for c in range(4)] for r in range(4)]
        z+=abs(det(M))/F(24)
    return z

# Right chamber triangulates the degenerate boundary exactly.
volP0_from_right=simplicial_volume(P0,right_facets)
volP0=F(36937,4536)
assert volP0_from_right==volP0

# Primal right derivative: each cone-simplex determinant scales by the
# product of its four vertex-pair radii.
dP=F(0)
for f in right_facets:
    cols=[P0[i] for i in f]
    M=[[cols[c][r] for c in range(4)] for r in range(4)]
    w=abs(det(M))/F(24)
    dP += w*sum(F(a[i//2]) for i in f)
assert dP==F(23879,9072)

# Enumerate the polar exactly for arbitrary rational radial scale.
def polar_data(scales):
    reps=[tuple(scales[i]*x for x in V[i]) for i in range(6)]
    Y=set()
    for inds in combinations(range(6),4):
        M=[[reps[i][r] for r in range(4)] for i in inds]
        if det(M)==0: continue
        for sig in product((-1,1),repeat=4):
            y=solve_square(M,sig)
            if y is None: continue
            vals=[sum(reps[i][r]*y[r] for r in range(4)) for i in range(6)]
            if all(abs(z)<=1 for z in vals): Y.add(y)
    Y=sorted(Y)
    facets=[]
    for i in range(6):
        for s in (-1,1):
            ids=[k for k,y in enumerate(Y)
                 if sum(reps[i][r]*y[r] for r in range(4))==s]
            assert affine_dim([Y[k] for k in ids])==3
            facets.append(frozenset(ids))
    return reps,Y,facets

_,Y0,Cfacets0=polar_data([F(1)]*6)
assert len(Y0)==22
volC0=volume4_from_facets(Y0,Cfacets0)
assert volC0==F(17281169,11938752)

# First variation of the polar support numbers h_i(t)=1/(1+a_i t).
# In dimension four, if c_i is the cone-volume of the opposite facet pair
# at h_i=1, then d|C|/dh_i = 4 c_i.
facet_cones=facet_cone_contributions(Y0,Cfacets0)
pair_cones=[facet_cones[2*i]+facet_cones[2*i+1] for i in range(6)]
expected_pairs=[
    F(757,5292),
    F(1147331,3411072),
    F(1353,5264),
    F(3025,11844),
    F(587,4704),
    F(7900217,23877504),
]
assert pair_cones==expected_pairs
dC=-4*sum(F(a[i])*pair_cones[i] for i in range(6))
assert dC==F(-111179,94752)

M0=volP0*volC0
assert M0==F(638314539353,54154179072)
dM=dP*volC0+volP0*dC
assert dM==F(-622210883645,108308358144)
assert dM<0

# Independent exact nearby-point sanity check at t=1/1000.
t=F(1,1000)
scales=[F(1)+t*F(ai) for ai in a]
reps1,Y1,Cfacets1=polar_data(scales)
assert len(Y1)==34

# Every polar vertex has exactly four saturated inequalities, hence gives one
# tetrahedral primal facet. Verify it agrees with the Taylor chamber.
P1=[]
labels=[]
for i,v in enumerate(reps1):
    P1.append(v); labels.append((i,1))
    P1.append(tuple(-x for x in v)); labels.append((i,-1))
labidx={lab:k for k,lab in enumerate(labels)}
Pfac1=[]
sat_hist=Counter()
for y in Y1:
    sat=[]
    for i in range(6):
        z=sum(reps1[i][r]*y[r] for r in range(4))
        if z==1: sat.append((i,1))
        elif z==-1: sat.append((i,-1))
    sat_hist[len(sat)]+=1
    Pfac1.append(tuple(sorted(labidx[x] for x in sat)))
assert sat_hist==Counter({4:34})
assert set(Pfac1)==set(right_facets)

volP1=simplicial_volume(P1,Pfac1)
volC1=volume4_from_facets(Y1,Cfacets1)
M1=volP1*volC1
assert M1<M0

print("direction_a =",a)
print("right_hand_tetrahedral_facets =",len(right_facets))
print("persistent_coplanar_4sets =",persistent_coplanar)
print("volP0 =",volP0)
print("volC0 =",volC0)
print("pair_cone_volumes =",[str(x) for x in pair_cones])
print("dP_right =",dP)
print("dC_right =",dC)
print("dMahler_right =",dM)
print("dMahler_right_decimal =",float(dM))
print("t_check =",t)
print("polar_vertices_at_t =",len(Y1))
print("volP_t =",volP1)
print("volC_t =",volC1)
print("Mahler_t =",M1)
print("Mahler_0 =",M0)
print("exact_drop_at_t =",M1-M0)
print("ALL_EXACT_CHECKS_PASS = True")
