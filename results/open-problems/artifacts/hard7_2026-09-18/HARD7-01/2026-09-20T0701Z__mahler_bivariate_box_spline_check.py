from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter

def rank(M):
    A=[list(map(F,row)) for row in M]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def det(M):
    A=[list(map(F,row)) for row in M]; n=len(A); s=F(1)
    assert all(len(row)==n for row in A)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i][c]),None)
        if p is None: return F(0)
        if p!=c: A[c],A[p]=A[p],A[c]; s=-s
        z=A[c][c]; s*=z
        for i in range(c+1,n):
            if A[i][c]:
                q=A[i][c]/z
                for j in range(c+1,n): A[i][j]-=q*A[c][j]
                A[i][c]=F(0)
    return s

def solve(M,b):
    n=len(M); A=[list(map(F,M[i]))+[F(b[i])] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if A[i][c])
        A[c],A[p]=A[p],A[c]
        z=A[c][c]; A[c]=[x/z for x in A[c]]
        for i in range(n):
            if i!=c and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[c][j] for j in range(n+1)]
    return tuple(A[i][-1] for i in range(n))

def affdim(P):
    if len(P)<=1: return 0
    p=P[0]
    return rank([[q[j]-p[j] for j in range(len(p))] for q in P[1:]])

def avg(P):
    n=F(len(P)); return tuple(sum(p[j] for p in P)/n for j in range(len(P[0])))

def vol4(points, facets):
    facets=[frozenset(f) for f in facets]
    assert all(affdim([points[i] for i in Ff])==3 for Ff in facets)
    ans=F(0)
    for a,Ff in enumerate(facets):
        gF=avg([points[i] for i in Ff])
        ridges=set()
        for b,G in enumerate(facets):
            if a==b: continue
            R=Ff&G
            if len(R)>=3 and affdim([points[i] for i in R])==2: ridges.add(frozenset(R))
        for R in ridges:
            gR=avg([points[i] for i in R])
            edges=set()
            for G in facets:
                E=R&G
                if len(E)>=2 and affdim([points[i] for i in E])==1: edges.add(frozenset(E))
            assert all(len(E)==2 for E in edges)
            for E in edges:
                i,j=tuple(E); cols=[gF,gR,points[i],points[j]]
                M=[[cols[c][r] for c in range(4)] for r in range(4)]
                ans += abs(det(M))/F(24)
    return ans

def enum_section(B):
    V=set()
    for sat in combinations(range(6),4):
        free=[i for i in range(6) if i not in sat]
        M=[[B[r][j] for j in free] for r in range(2)]
        if det(M)==0: continue
        for eps in product((-1,1),repeat=4):
            x=[None]*6; rhs=[F(0),F(0)]
            for i,s in zip(sat,eps):
                x[i]=F(s)
                for r in range(2): rhs[r]-=B[r][i]*s
            z=solve(M,rhs); x[free[0]],x[free[1]]=z
            if all(-1<=q<=1 for q in x): V.add(tuple(x))
    return sorted(V)

# Generic rank-two Gale matrix: every 2x2 minor is nonzero.
B=[[F(-7),F(-10),F(4),F(-6),F(6),F(8)],
   [F(2), F(5),  F(6),F(1), F(-6),F(1)]]
assert rank(B)==2
assert all(det([[B[r][j] for j in J] for r in range(2)])!=0
           for J in combinations(range(6),2))

# Rational basis of ker(B), as rows, so BA^T=0.
A=[[F(16,3),F(-10,3),1,0,0,0],
   [F(-4,3),F(1,3),0,1,0,0],
   [F(-2),F(2),0,0,1,0],
   [F(10,3),F(-23,15),0,0,0,1]]
assert rank(A)==4
assert all(sum(B[r][j]*A[a][j] for j in range(6))==0
           for r in range(2) for a in range(4))

C=enum_section(B)
assert len(C)==38
assert Counter(sum(abs(z)==1 for z in x) for x in C)==Counter({4:38})
for i in range(6):
    for s in (-1,1):
        assert affdim([x for x in C if x[i]==s])==3

# Facets of P=conv{+-v_i} are the generic section vertices.
Ppts=[]; labs=[]
for j in range(6):
    v=tuple(A[a][j] for a in range(4))
    Ppts += [v,tuple(-z for z in v)]; labs += [(j,1),(j,-1)]
li={lab:i for i,lab in enumerate(labs)}
Pfac=[]; N=Counter()
for q in C:
    ids=[]; I=[]
    for j,z in enumerate(q):
        if z==1: ids.append(li[(j,1)]); I.append(j)
        elif z==-1: ids.append(li[(j,-1)]); I.append(j)
    assert len(ids)==4
    Pfac.append(ids)
    J=tuple(i for i in range(6) if i not in I)
    N[J]+=1
assert sum(N.values())==38
VP0=vol4(Ppts,Pfac)
assert VP0==F(223,45)

# Express section vertices in the A^T coordinates of P^circ.
I0=next(I for I in combinations(range(6),4)
        if det([[A[a][j] for a in range(4)] for j in I])!=0)
M0=[[A[a][j] for a in range(4)] for j in I0]
Y=[]
for q in C:
    y=solve(M0,[q[j] for j in I0])
    assert all(sum(A[a][j]*y[a] for a in range(4))==q[j] for j in range(6))
    Y.append(y)
Yfac=[]
for j in range(6):
    for s in (-1,1):
        ids=[k for k,q in enumerate(C) if q[j]==s]
        assert affdim([Y[k] for k in ids])==3
        Yfac.append(ids)
VPOL=vol4(Y,Yfac)
assert VPOL==F(233633729,95040000)
M=VP0*VPOL
assert M==F(52100321567,4276800000)

# Complementary minors. Here |det A_{J^c}|/|det B_J|=1/15.
for J in combinations(range(6),2):
    I=tuple(i for i in range(6) if i not in J)
    dA=abs(det([[A[a][j] for j in I] for a in range(4)]))
    dB=abs(det([[B[r][j] for j in J] for r in range(2)]))
    assert dA*15==dB

# The report proves analytically that p_J is the corresponding continuous
# uniform hit probability. In this basis p_J=|det A_{J^c}|*|P^circ|/16.
p={}
for J in combinations(range(6),2):
    I=tuple(i for i in range(6) if i not in J)
    dA=abs(det([[A[a][j] for j in I] for a in range(4)]))
    p[J]=dA*VPOL/F(16)
    assert 0<p[J]<=1

sumNp=sum(F(N[J])*p[J] for J in combinations(range(6),2))
assert sumNp==F(52100321567,2851200000)
assert M==F(2,3)*sumNp
assert sumNp-F(16)==F(6481121567,2851200000)>0

# Refute the tempting pointwise strengthening p_J >= N_J/16.
# For J=(1,3) zero-based, directly integrate the four-dimensional preimage
# polytope by exact H-polytope vertex/facet enumeration.
J=(1,3); I=[i for i in range(6) if i not in J]
BJ=[[B[r][j] for j in J] for r in range(2)]
BI=[[B[r][i] for i in I] for r in range(2)]
D=det(BJ)
inv=[[BJ[1][1]/D,-BJ[0][1]/D],[-BJ[1][0]/D,BJ[0][0]/D]]
T=[[-sum(inv[r][k]*BI[k][c] for k in range(2)) for c in range(4)] for r in range(2)]
ineq=[]
for k in range(4):
    a=[F(0)]*4; a[k]=1; ineq.append((tuple(a),F(1)))
    a=[F(0)]*4; a[k]=-1; ineq.append((tuple(a),F(1)))
for r in range(2):
    ineq.append((tuple(T[r]),F(1)))
    ineq.append((tuple(-z for z in T[r]),F(1)))
R=set()
for active in combinations(range(len(ineq)),4):
    MM=[ineq[h][0] for h in active]
    if det(MM)==0: continue
    u=solve(MM,[ineq[h][1] for h in active])
    if all(sum(a[k]*u[k] for k in range(4))<=c for a,c in ineq): R.add(u)
R=sorted(R)
Rfac=[]
for a,c in ineq:
    ids=[i for i,u in enumerate(R) if sum(a[k]*u[k] for k in range(4))==c]
    if len(ids)>=4 and affdim([R[i] for i in ids])==3: Rfac.append(ids)
direct_p=vol4(R,Rfac)/F(16)
assert len(R)==38 and len(Rfac)==12
assert N[J]==4
q=F(N[J],16)
assert direct_p==p[J]==F(233633729,1140480000)
assert q==F(1,4)
assert direct_p-q==F(-51486271,1140480000)<0

print("generic_section_vertices =",len(C))
print("generic_primal_facets =",sum(N.values()))
print("vol(P) =",VP0)
print("vol(P^circ) =",VPOL)
print("volume_product =",M)
print("sum_J N_J p_J =",sumNp)
print("identity_product_minus_two_thirds_sum =",M-F(2,3)*sumNp)
print("BS12_margin_for_this_example =",sumNp-16)
print("bad_pair_zero_based =",J)
print("N_J/16 =",q)
print("direct_p_J =",direct_p)
print("pointwise_gap_p_minus_q =",direct_p-q)
print("direct_probability_region_vertices_facets =",(len(R),len(Rfac)))
print("ALL_EXACT_CHECKS_PASS = True")
