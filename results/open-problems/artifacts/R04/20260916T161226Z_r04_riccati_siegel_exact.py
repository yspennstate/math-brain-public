import itertools
from fractions import Fraction as F
import random, math
import networkx as nx
import sympy as sp

print('R04 exact checker: Riccati/Siegel transfer and block covariance')

# ---------- exact matrix helpers via sympy Rational ----------
def Jmat(w):
    Z=sp.zeros(w); I=sp.eye(w)
    return Z.row_join(-I).col_join(I.row_join(Z))

def rand_lower(w, seed):
    rr=random.Random(seed)
    B=sp.zeros(w)
    for i in range(w):
        for j in range(i+1):
            # nonzero diagonal, small integers elsewhere
            val=rr.choice([-3,-2,-1,1,2,3]) if i==j else rr.randint(-3,3)
            B[i,j]=sp.Rational(val, rr.choice([1,2,3]))
    return B

def rand_sym(w, seed):
    rr=random.Random(seed)
    A=sp.zeros(w)
    for i in range(w):
        for j in range(i,w):
            val=sp.Rational(rr.randint(-4,4), rr.choice([1,2,3]))
            A[i,j]=A[j,i]=val
    return A

for w in range(1,6):
    for seed in range(4):
        B=rand_lower(w,100*w+seed)
        D=rand_sym(w,200*w+seed)
        z=sp.Rational(7,5)
        Binv=B.inv()
        A=Binv*(z*sp.eye(w)-D)
        C=-Binv
        E=B.T
        M=A.row_join(C).col_join(E.row_join(sp.zeros(w)))
        assert sp.simplify(M.T*Jmat(w)*M-Jmat(w)) == sp.zeros(2*w)

        R=rand_sym(w,300*w+seed)
        K=z*sp.eye(w)-D-R
        if K.det()==0:
            continue
        Phi=B.T*K.inv()*B
        assert sp.simplify(Phi-Phi.T)==sp.zeros(w)
        # graph action: M [I;R] = [Top;Bottom], and Bottom*Top^{-1}=Phi
        GR=sp.eye(w).col_join(R)
        image=M*GR
        Top=image[:w,:]
        Bottom=image[w:,:]
        assert Top.det()!=0
        assert sp.simplify(Bottom*Top.inv()-Phi)==sp.zeros(w)
print('C5 symplectic identity and inverse-free Riccati graph action: PASS')

# ---------- exact covariance-map enumeration ----------
def lower_entries(w):
    return [(i,j) for i in range(w) for j in range(i+1)]

def B_map_BT_X_B(X):
    w=len(X); out=[[F(0) for _ in range(w)] for __ in range(w)]
    v=F(1,2*w+1)
    # E B_{a p} B_{b q}: nonzero iff (a,p)==(b,q), a>=p
    for p in range(w):
        out[p][p]=v*sum(X[a][a] for a in range(p,w))
    return out

def B_map_B_X_BT(X):
    w=len(X); out=[[F(0) for _ in range(w)] for __ in range(w)]
    v=F(1,2*w+1)
    for p in range(w):
        out[p][p]=v*sum(X[a][a] for a in range(0,p+1))
    return out

def D_map(X):
    w=len(X); v=F(1,2*w+1); tr=sum(X[i][i] for i in range(w))
    out=[[F(0) for _ in range(w)] for __ in range(w)]
    for p in range(w):
        for q in range(w):
            out[p][q]=v*X[q][p]
            if p==q:
                out[p][q]+=v*(tr-X[p][p])
    return out

def addm(*Ms):
    w=len(Ms[0]); return [[sum(M[i][j] for M in Ms) for j in range(w)] for i in range(w)]

for w in range(1,16):
    rr=random.Random(900+w)
    X=[[F(rr.randint(-5,5), rr.randint(1,5)) for j in range(w)] for i in range(w)]
    BT=B_map_BT_X_B(X); BB=B_map_B_X_BT(X); DD=D_map(X)
    total=addm(BT,BB,DD)
    v=F(1,2*w+1); tr=sum(X[i][i] for i in range(w))
    for p in range(w):
        for q in range(w):
            target=v*X[q][p]
            if p==q: target += 2*v*tr
            assert total[p][q]==target
print('C6 exact two-sided block covariance map S[X]=v X^T + 2v Tr(X) I: PASS')

# first two singular-value moments of lower triangular B
for w in range(1,101):
    v=F(1,2*w+1)
    n=[w-p for p in range(w)]  # n_p=W-p for p=0,...,W-1
    m1=v*F(w+1,2)
    # exact Wick formula
    direct = v*v*(sum(k*k+2*k for k in n) + sum(n[max(p,q)] for p in range(w) for q in range(w) if p!=q))/w
    formula=v*v*F((w+1)*(4*w+5),6)
    assert direct==formula
    # complement normalization
    for p in range(w):
        assert v*n[p] + v*(p+1) == v*(w+1)
print('C7 triangular-coupling moments and complementary row/column normalization: PASS; mu1=v(W+1)/2, mu2=v^2(W+1)(4W+5)/6, ratio->8/3')

# ---------- independent R05 n=9 audit through Cayley classification ----------
# External theorem used in report: every vertex-transitive graph of order p^2 is Cayley.
def cayley_Z9(mask):
    pairs=[(1,8),(2,7),(3,6),(4,5)]
    S=set()
    for i,pr in enumerate(pairs):
        if (mask>>i)&1: S.update(pr)
    G=nx.Graph(); G.add_nodes_from(range(9))
    for x in range(9):
        for s in S: G.add_edge(x,(x+s)%9)
    return G

els=[(a,b) for a in range(3) for b in range(3)]
idx={x:i for i,x in enumerate(els)}
pairs2=[((0,1),(0,2)),((1,0),(2,0)),((1,1),(2,2)),((1,2),(2,1))]
def cayley_F9(mask):
    S=set()
    for i,pr in enumerate(pairs2):
        if (mask>>i)&1: S.update(pr)
    G=nx.Graph(); G.add_nodes_from(range(9))
    for x in els:
        for s in S:
            y=((x[0]+s[0])%3,(x[1]+s[1])%3)
            G.add_edge(idx[x],idx[y])
    return G

def arc_transitive(G):
    if not nx.is_connected(G) or G.number_of_edges()==0: return False
    arcs=[(u,v) for u,v in G.edges() for (u,v) in ((u,v),(v,u))]
    base=arcs[0]; images=set()
    gm=nx.algorithms.isomorphism.GraphMatcher(G,G)
    for mp in gm.isomorphisms_iter():
        images.add((mp[base[0]],mp[base[1]]))
        if len(images)==len(arcs):
            return True
    return False

conn=[]
for typ,fn in [('Z9',cayley_Z9),('F3xF3',cayley_F9)]:
    for mask in range(1,16):
        G=fn(mask)
        if nx.is_connected(G): conn.append((typ,mask,G))
classes=[]
for typ,mask,G in conn:
    hit=None
    for C in classes:
        if nx.is_isomorphic(G,C['G']): hit=C; break
    if hit is None: classes.append({'G':G,'members':[(typ,mask)]})
    else: hit['members'].append((typ,mask))
reps=[C['G'] for C in classes if arc_transitive(C['G'])]
assert sorted(G.degree(0) for G in reps)==[2,4,6,8]
assert len(reps)==4
# identify the four standard types
C9=nx.cycle_graph(9)
K9=nx.complete_graph(9)
K333=nx.complete_multipartite_graph(3,3,3)
assert any(nx.is_isomorphic(G,C9) for G in reps)
assert any(nx.is_isomorphic(G,K9) for G in reps)
assert any(nx.is_isomorphic(G,K333) for G in reps)
# degree-4 representative has SRG parameters (9,4,1,2)
G4=[G for G in reps if G.degree(0)==4][0]
for u,vv in itertools.combinations(range(9),2):
    cn=len(set(G4[u])&set(G4[vv]))
    assert cn==(1 if G4.has_edge(u,vv) else 2)
print('R05 n=9 Cayley candidates connected',len(conn),'isomorphism classes',len(classes))
print('R05 n=9 independent Cayley-classification audit: PASS; exactly 4 arc-transitive types, degrees', sorted(G.degree(0) for G in reps))

print('SELF-CHECK PASS')
