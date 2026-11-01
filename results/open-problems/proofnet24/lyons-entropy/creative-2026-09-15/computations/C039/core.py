"""Exact C039 indexing, contrast, parameter polytope and interpolation.

C004 supplies the rational signed inverse and unimodular triangle-flow basis.
All other geometry in this file belongs to C039's three-block construction.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

E=tuple(range(6))
SETS=sum((list(combinations(E,k)) for k in (2,3,4)),[])
SIX={s:i for i,s in enumerate(SETS)}
AB=[(A,B) for A in combinations(E,2) for B in combinations([i for i in E if i not in A],2)]
AIX={ab:i for i,ab in enumerate(AB)}
D=[[0]*90 for _ in SETS]
for j,(A,B) in enumerate(AB):
    J=tuple(i for i in E if i not in A+B)
    T=tuple(i for i in E if i not in B)
    for X,sign in [(A,1),(T,1)]+[(tuple(sorted(A+(i,))),-1) for i in J]:
        D[SIX[X]][j]=sign

PAIR_COORDS=((0,1),(1,2),(0,2))
def contrast_coeff(X):
    out=[F(0)]*5
    if len(X)==4:X=tuple(i for i in E if i not in X)
    if len(X)==2:
        i,j=X;r,s=i//2,j//2
        if r==s:out[0]=F(1,9)
        else:out[0]=F(1,18);out[1+PAIR_COORDS.index((r,s))]=-F((-1)**(i+j),18)
    elif len(set(i//2 for i in X))<3:out[0]=-F(1,9)
    else:
        sig=[(-1)**i for i in X]
        out[0]=-F(1,12)
        for k,(r,s) in enumerate(PAIR_COORDS):out[1+k]=F(sig[r]*sig[s],36)
        out[4]=-F(sig[0]*sig[1]*sig[2],36)
    return out
C=[contrast_coeff(X) for X in SETS]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def matvec(M,x):return [dot(row,x) for row in M]
def contrast(p):return matvec(C,(F(1),)+tuple(p))

def simple_dual():
    out=[]
    for X in SETS:
        if len(X)==4:X=tuple(i for i in E if i not in X)
        if len(X)==2:out.append(F(int(X[0]//2!=X[1]//2 and X[0]%2!=X[1]%2)))
        elif len(set(i//2 for i in X))<3:out.append(F(0))
        else:
            minus=sum(i%2 for i in X)
            out.append(F(1 if minus==2 else -1 if minus==3 else 0))
    return out

# H_i p <= c_i: cube, all middle marginals, eight additional transport cuts.
INEQUALITIES=[]
for j in range(3):
    for sign in (-1,1):
        h=[F(0)]*4;h[j]=F(sign);INEQUALITIES.append((tuple(h),F(1)))
for eps in product((-1,1),repeat=3):
    if eps[0]*eps[1]*eps[2]!=1:continue
    for sign in (-1,1):INEQUALITIES.append((tuple(map(F,eps+(sign,))),F(3)))
for eps in product((-1,1),repeat=3):
    if eps[0]*eps[1]*eps[2]!=1:continue
    for sign in (-1,1):INEQUALITIES.append((tuple(F(-3*x) for x in eps)+(F(2*sign),),F(9)))

SEEDS=[(F(1),F(1),F(1),F(0)),
       (F(-1),F(-1),F(-1),F(0)),
       (F(-1),F(-1),F(-1,5),F(6,5)),
       (F(-1),F(-1,3),F(-1,3),F(2)),
       (F(-3,7),F(-3,7),F(-3,7),F(18,7)),
       (F(0),F(0),F(0),F(3))]

def solve(M,b):
    n=len(b);a=[list(map(F,row))+[F(x)] for row,x in zip(M,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return None
        a[j],a[pivot]=a[pivot],a[j]
        p=a[j][j];a[j]=[v/p for v in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                q=a[i][j];a[i]=[u-q*v for u,v in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

def exact_vertices():
    vs=set();nonsingular=0
    for ids in combinations(range(len(INEQUALITIES)),4):
        p=solve([INEQUALITIES[i][0] for i in ids],[INEQUALITIES[i][1] for i in ids])
        if p is None:continue
        nonsingular+=1
        if all(dot(h,p)<=c for h,c in INEQUALITIES):vs.add(p)
    return sorted(vs),nonsingular

SYMMETRIES=[]
for pi in permutations(range(3)):
    for flips in product((0,1),repeat=3):
        perm=tuple(2*pi[i//2]+((i%2)^flips[i//2]) for i in E)
        SYMMETRIES.append(perm)

def act_point(p,perm):
    out=[F(0)]*4;tsign=1
    for r in range(3):tsign*=(-1)**(perm[2*r]%2)
    for k,(r,s) in enumerate(PAIR_COORDS):
        rr,ss=sorted((perm[2*r]//2,perm[2*s]//2))
        sign=(-1)**((perm[2*r]%2)+(perm[2*s]%2))
        out[PAIR_COORDS.index((rr,ss))]=sign*p[k]
    out[3]=tsign*p[3]
    return tuple(out)

def act_weights(x,perm):
    out=[F(0)]*90
    for (A,B),v in zip(AB,x):
        A=tuple(sorted(perm[i] for i in A));B=tuple(sorted(perm[i] for i in B))
        out[AIX[A,B]]=v
    return out

def vertex_tables(seed_tables):
    out={}
    for s,x in zip(SEEDS,seed_tables):
        for perm in SYMMETRIES:out.setdefault(act_point(s,perm),act_weights(x,perm))
    return out

def barycentric(p,vertices):
    """No LP: at most four radial moves through strictly smaller faces.

    Return rational vertex coefficients for rational p. The same formulas with
    real arithmetic define the theorem for every real point in the polytope.
    """
    p=tuple(map(F,p));vertices=list(vertices)
    assert all(dot(h,p)<=c for h,c in INEQUALITIES)
    result={v:F(0) for v in vertices};remaining=F(1);steps=0
    face=vertices
    while True:
        q=tuple(sum((v[j] for v in face),F(0))/len(face) for j in range(4))
        if p==q:
            for v in face:result[v]+=remaining/len(face)
            break
        direction=tuple(x-y for x,y in zip(p,q))
        candidates=[((c-dot(h,q))/dot(h,direction),i) for i,(h,c) in enumerate(INEQUALITIES) if dot(h,direction)>0]
        radius,i=min(candidates);assert radius>=1
        portion=remaining*(1-1/radius)
        for v in face:result[v]+=portion/len(face)
        remaining/=radius
        p=tuple(q[j]+radius*direction[j] for j in range(4))
        h,c=INEQUALITIES[i]
        newface=[v for v in face if dot(h,v)==c]
        assert newface and len(newface)<len(face)
        face=newface;steps+=1;assert steps<=4
    assert sum(result.values())==1 and min(result.values())>=0
    return {v:w for v,w in result.items() if w},steps

def coupling(p,tables):
    weights,steps=barycentric(p,tables)
    return [sum((weight*tables[v][j] for v,weight in weights.items()),F(0)) for j in range(90)],weights,steps

def right_inverse():
    beta={(2,0,0):1788,(1,1,0):-702,(1,0,1):378,(0,2,0):588,(0,1,1):-222,(0,0,2):228}
    gamma={(2,1,0):-1222,(2,0,1):838,(1,2,0):838,(1,1,1):-357,(1,0,2):338,(0,2,1):338,(0,1,2):-122}
    result=[]
    for A,B in AB:
        J=tuple(i for i in E if i not in A+B);row=[]
        for X in SETS:
            a,j,b=(len(set(X)&set(V)) for V in (A,J,B))
            z=beta[a,j,b] if len(X)==2 else gamma[a,j,b] if len(X)==3 else beta[2-b,2-j,2-a]
            row.append(F(z,12600))
        result.append(row)
    return result

def flows():
    result=[]
    for h in E:
        for e in E:
            if h==e:continue
            for triple in combinations([i for i in E if i not in (h,e)],3):
                f=[0]*90
                for k in range(3):
                    a,b=triple[k],triple[(k+1)%3]
                    f[AIX[tuple(sorted((h,a))),tuple(sorted((e,b)))]]+=1
                    f[AIX[tuple(sorted((h,b))),tuple(sorted((e,a)))]]-=1
                result.append(f)
    return result

FLOW_COLUMNS=[0,1,2,4,5,6,8,9,10,13,14,20,21,22,24,25,26,28,29,30,33,34,40,41,42,44,45,46,48,49,50,53,54,60,61,62,64,65,66,70,73,74,81,82,85,86,90]
FLOW_ROWS=[6,7,13,0,1,15,3,4,9,8,10,30,31,37,16,18,39,17,19,33,32,34,36,42,55,25,26,57,29,12,45,20,40,43,48,61,22,49,63,46,28,52,50,67,21,69,51]
def flow_coordinates(v):
    fs=flows();basis=[[fs[j][i] for j in FLOW_COLUMNS] for i in range(90)]
    t=solve([basis[i] for i in FLOW_ROWS],[v[i] for i in FLOW_ROWS]);assert t is not None
    assert matvec(basis,t)==list(v)
    return t
