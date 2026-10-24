from itertools import combinations

V = tuple(range(4))
E = ((0,2),(0,3),(1,2),(1,3))
e = (0,1)
f = (2,3)

def is_forest(mask):
    p=list(V)
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(E):
        if mask>>i & 1:
            ru,rv=find(u),find(v)
            if ru==rv:
                return False
            p[rv]=ru
    return True

def connected(mask,u,v):
    p=list(V)
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(a,b) in enumerate(E):
        if mask>>i & 1:
            ra,rb=find(a),find(b)
            if ra!=rb:
                p[rb]=ra
    return find(u)==find(v)

def addable(mask,g):
    return not connected(mask,*g)

def jointly_addable(mask,g,h):
    # base mask is already a forest
    p=list(V)
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b:
            return False
        p[b]=a
        return True
    for i,(a,b) in enumerate(E):
        if mask>>i & 1:
            assert union(a,b)
    return union(*g) and union(*h)

def edges(mask):
    return tuple(E[i] for i in range(len(E)) if mask>>i & 1)

N = tuple(m for m in range(1<<len(E)) if is_forest(m))
Nset=set(N)
A={m for m in N if addable(m,e)}
B={m for m in N if addable(m,f)}
D={m for m in N if jointly_addable(m,e,f)}
I=A & B
Q=I-D

n00=len(Nset-A-B)
n10=len(A-B)
n01=len(B-A)
n11=len(I)
q=len(Q)
Delta=len(A)*len(B)-len(N)*len(D)
Delta_cells=n10*n01-n00*n11+len(N)*q

L={(F,H) for F in Nset-A for H in D}
R={(F,H) for F in A for H in B-D}

assert (len(N),len(A),len(B),len(D)) == (15,9,9,5)
assert (n00,n10,n01,n11,q)==(4,2,2,7,2)
assert Delta==Delta_cells==6
assert len(L)==30 and len(R)==36

# All four C4 decompositions: first coordinate gets 3 edges, second gets the omitted edge.
full=(1<<len(E))-1
S=set()
for i in range(len(E)):
    H=1<<i
    F=full ^ H
    S.add((F,H))
assert len(S)==4
assert S <= L

# Strong recoloring support: allow ANY recoloring of the pair, with no radius or
# path restriction, as long as union and intersection of the two coordinates
# are preserved and the output lies in the exact target R.
def recolor_neighbors(F,H):
    U=F|H
    I0=F&H
    out=set()
    for Fp,Hp in R:
        if (Fp|Hp)==U and (Fp&Hp)==I0:
            out.add((Fp,Hp))
    return out

NS=set()
for x in S:
    NS |= recolor_neighbors(*x)

assert len(NS)==2
expected_R={
    ((1<<1)|(1<<2), (1<<0)|(1<<3)),  # F'={03,12}, H'={02,13}
    ((1<<0)|(1<<3), (1<<1)|(1<<2)),  # F'={02,13}, H'={03,12}
}
assert NS==expected_R

# Direct partner-style one-way transfer support: choose ANY subset S of F,
# with no path/radius restriction, and set F'=F\S, H'=H union S.
def transfer_neighbors(F,H):
    out=set()
    sub=F
    while sub:
        Fp=F & ~sub
        Hp=H | sub
        if (Fp,Hp) in R:
            out.add((Fp,Hp))
        sub=(sub-1)&F
    return out

L1 = (sum(1<<E.index(x) for x in ((0,3),(1,2),(1,3))), 1<<E.index((0,2)))
L2 = (sum(1<<E.index(x) for x in ((0,2),(0,3),(1,2))), 1<<E.index((1,3)))
assert L1 in L and L2 in L
T1=transfer_neighbors(*L1)
T2=transfer_neighbors(*L2)
assert len(T1)==len(T2)==1 and T1==T2
only=next(iter(T1))
assert only == ((1<<E.index((0,3)))|(1<<E.index((1,2))),
                (1<<E.index((0,2)))|(1<<E.index((1,3))))

# A strictly broader cut/join support may change union/intersection:
# delete k edges from F and add k (not necessarily the same) base edges to H.
# This is only a diagnostic survivor, not a theorem. Verify that it repairs K4.
def cut_join_neighbors(F,H):
    out=set()
    for Fp,Hp in R:
        if Fp & ~F:
            continue
        if H & ~Hp:
            continue
        if F.bit_count()-Fp.bit_count() != Hp.bit_count()-H.bit_count():
            continue
        if F.bit_count()==Fp.bit_count():
            continue
        out.add((Fp,Hp))
    return out

def maximum_matching_size(left, neigh):
    matchR={}
    def aug(x,seen):
        for y in neigh(*x):
            if y in seen:
                continue
            seen.add(y)
            if y not in matchR or aug(matchR[y],seen):
                matchR[y]=x
                return True
        return False
    got=0
    for x in sorted(left):
        if aug(x,set()):
            got+=1
    return got

cj_match=maximum_matching_size(L,cut_join_neighbors)
assert cj_match==len(L)==30

print("GRAPH K4 marked e=01 f=23; G0 edges", E)
print("COUNTS N A B D =", len(N),len(A),len(B),len(D))
print("CELLS n00 n10 n01 n11 q =", n00,n10,n01,n11,q)
print("RAYLEIGH_GAP =", Delta, "CELL_FORMULA =", Delta_cells)
print("RESIDUAL_SIZES L R =", len(L),len(R))
print("UNION_RECOLOR_HALL_WITNESS left =", len(S), "neighbors =", len(NS), "deficiency =", len(S)-len(NS))
for j,(F,H) in enumerate(sorted(S),1):
    print("  ULEFT",j,"F=",edges(F),"H=",edges(H))
for j,(F,H) in enumerate(sorted(NS),1):
    print("  URIGHT",j,"F=",edges(F),"H=",edges(H))
print("ONE_WAY_TRANSFER_WITNESS left=2 neighbors=1 deficiency=1")
for j,(F,H) in enumerate((L1,L2),1):
    print("  TLEFT",j,"F=",edges(F),"H=",edges(H),"neighbors=",[(edges(a),edges(b)) for a,b in transfer_neighbors(F,H)])
print("EXTERNAL_CUT_JOIN_DIAGNOSTIC_MATCH =", cj_match, "/", len(L))
print("STATUS=ALL_EXACT_ASSERTIONS_PASSED")
