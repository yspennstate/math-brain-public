from fractions import Fraction
from itertools import combinations

V = range(4)
E = list(combinations(V,2))

def invert(A):
    n=len(A)
    M=[list(map(Fraction,row))+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q:
                M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

# K4 reduced Laplacian, root vertex 3 deleted.
L=[[Fraction(0) for _ in range(3)] for __ in range(3)]
for u,v in E:
    if u<3: L[u][u]+=1
    if v<3: L[v][v]+=1
    if u<3 and v<3:
        L[u][v]-=1; L[v][u]-=1
K=invert(L)

def b(e):
    u,v=e
    x=[Fraction(0) for _ in range(3)]
    if u<3: x[u]+=1
    if v<3: x[v]-=1
    return x

def bil(x,y):
    return sum(x[i]*K[i][j]*y[j] for i in range(3) for j in range(3))

def is_tree(S):
    if len(S)!=3: return False
    p=list(V)
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v in S:
        a,c=f(u),f(v)
        if a==c: return False
        p[a]=c
    return len({f(i) for i in V})==1

trees=[set(S) for S in combinations(E,3) if is_tree(S)]
assert len(trees)==16
tau=Fraction(16)

edge_checks=0
pair_checks=0
adjacent_values=set()
disjoint_values=set()
for i,e in enumerate(E):
    be=b(e)
    formula=tau*bil(be,be)
    direct=sum(e in T for T in trees)
    assert formula==direct==8
    edge_checks += 1
    for f in E[i+1:]:
        bf=b(f)
        formula2=tau*(bil(be,be)*bil(bf,bf)-bil(be,bf)**2)
        direct2=sum(e in T and f in T for T in trees)
        assert formula2==direct2
        if len(set(e+f))==3:
            adjacent_values.add(direct2)
        else:
            disjoint_values.add(direct2)
        pair_checks += 1

assert adjacent_values=={3}
assert disjoint_values=={4}
print("P14 transfer-current audit on K4")
print("spanning trees:", len(trees))
print("one-edge checks:", edge_checks, "all count 8")
print("two-edge checks:", pair_checks)
print("adjacent-edge pair count:", next(iter(adjacent_values)))
print("disjoint-edge pair count:", next(iter(disjoint_values)))
print("PASS")
