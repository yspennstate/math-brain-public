from itertools import product

F3=range(3)
ALL=frozenset((r,s,t) for r in F3 for s in F3 for t in F3)
U=frozenset((r,s,0) for r in F3 for s in F3)

def B(R):
    out=set()
    for r,s,w in product(F3,F3,F3):
        x=(w-1-r)%3
        for rr,c,q in R:
            if rr==x and c==(w+q)%3 and c!=s:
                out.add((r,s,w)); break
    return frozenset(out)

def M(R,S):
    out=set()
    for r,s in product(F3,F3):
        a=[t for rr,ss,t in R if rr==r and ss==s]
        b=[t for rr,ss,t in S if rr==r and ss==s]
        for x in a:
            for y in b:
                out.add((r,s,(x+y)%3))
    return frozenset(out)

def T(R,S):
    out=set()
    for r,s,x,y in product(F3,F3,F3,F3):
        w01=(1+r+x)%3; w12=(1+x+y)%3; w20=(1+y+r)%3
        c1=(w01+w12)%3; c2=(w12+w20)%3; t=(w20+w01)%3
        ok1=[]
        for rr,s1,q1 in R:
            if rr==x and s1==(c1+q1)%3:
                ok1.append(s1)
        ok2=[]
        for rr,s2,q2 in S:
            if rr==y and s2==(c2+q2)%3:
                ok2.append(s2)
        if any(s!=s1 and s1!=s2 and s2!=s for s1 in ok1 for s2 in ok2):
            out.add((r,s,t))
    return frozenset(out)

def diag(R):
    return frozenset((r,s,t) for r,s,t in R if s==t)

# Leaf-triangle relation and bridge stabilization.
R0=T(U,U)
assert R0==frozenset((r,(r-1)%3,t) for r in F3 for t in F3)
R1=B(R0)
assert R1==frozenset((r,s,t) for r,s,t in ALL if t!=(s+r-1)%3)
R2=B(R1)
assert R2==frozenset((r,s,t) for r,s,t in ALL if t!=(1-r)%3)
R3=B(R2)
assert R3==ALL and B(R3)==ALL
R=[R0,R1,R2,R3]

A=frozenset((r,s,(1-r-s)%3) for r in F3 for s in F3)
C=frozenset((r,s,(s+r-1)%3) for r in F3 for s in F3)

# Exact central-triangle table for two leaf-triangle branches.
tri_table={}
for i in range(4):
    for j in range(4):
        Q=T(R[i],R[j])
        tri_table[(i,j)]=Q
        expected=A if (i,j)==(0,0) else C if (i,j)==(2,2) else ALL
        assert Q==expected, (i,j,len(Q),len(expected))
        assert diag(Q)

# Y topology: three triangle leaves joined through one bridge-tree branching vertex.
y_min=99; y_arg=None
for a,b,c in product(range(4), repeat=3):
    Q=M(M(R[a],R[b]),R[c])
    d=len(diag(Q))
    assert d>0
    if d<y_min: y_min=d; y_arg=(a,b,c,Q)

# Path topology: a central triangle, with one leaf-triangle branch on each of two distinct vertices.
p_min=99; p_arg=None
for a,b in product(range(4), repeat=2):
    Q=T(R[a],R[b])
    d=len(diag(Q))
    assert d>0
    if d<p_min: p_min=d; p_arg=(a,b,Q)

# First strong-mod-3 obstruction at four triangular cycle blocks.
# Central triangle has two R2 branches; move that central piece two bridges away,
# and merge at the outer root with a direct leaf triangle.
central=T(R2,R2)
assert central==C
BC=B(central)
assert BC==frozenset((r,s,(1-r)%3) for r in F3 for s in F3)
B2C=B(BC)
assert B2C==frozenset((r,s,t) for r,s,t in ALL if s!=(r-1)%3)
bad_relation=M(R0,B2C)
assert bad_relation==frozenset()

# Build the exact rooted graph for M(F,B^2(T(B^2(F),B^2(F)))).
class RG:
    def __init__(self, edges, root, n):
        self.edges=set(tuple(sorted(e)) for e in edges); self.root=root; self.n=n

def Ug(): return RG(set(),0,1)

def remap(g, mapping):
    return RG({tuple(sorted((mapping[u],mapping[v]))) for u,v in g.edges}, mapping[g.root], max(mapping.values())+1)

def Bg(g):
    mp={v:v+1 for v in range(g.n)}
    h=remap(g,mp)
    return RG(h.edges|{(0,h.root)},0,g.n+1)

def Mg(g,h):
    eg=set(); nextv=1; mg={g.root:0}
    for v in range(g.n):
        if v!=g.root: mg[v]=nextv; nextv+=1
    mh={h.root:0}
    for v in range(h.n):
        if v!=h.root: mh[v]=nextv; nextv+=1
    for u,v in g.edges: eg.add(tuple(sorted((mg[u],mg[v]))))
    for u,v in h.edges: eg.add(tuple(sorted((mh[u],mh[v]))))
    return RG(eg,0,nextv)

def Tg(g,h):
    eg=set(); root=0; nextv=1
    mg={}
    for v in range(g.n):
        mg[v]=nextv; nextv+=1
    v1=mg[g.root]
    mh={}
    for v in range(h.n):
        mh[v]=nextv; nextv+=1
    v2=mh[h.root]
    for u,v in g.edges: eg.add(tuple(sorted((mg[u],mg[v]))))
    for u,v in h.edges: eg.add(tuple(sorted((mh[u],mh[v]))))
    eg.update({tuple(sorted((root,v1))),tuple(sorted((v1,v2))),tuple(sorted((v2,root)))})
    return RG(eg,root,nextv)

Fgraph=Tg(Ug(),Ug())
badgraph=Mg(Fgraph, Bg(Bg(Tg(Bg(Bg(Fgraph)),Bg(Bg(Fgraph))))))
assert badgraph.n==15 and len(badgraph.edges)==18
assert len(badgraph.edges)-badgraph.n+1==4

# Integer {0,1,2} witness on the same graph. This proves the strong-mod-3 failure
# is a proof-route obstruction, not a counterexample to P^l<=2.
rho={0:0,1:0,2:2,3:0,4:0,5:0,6:1,7:1,8:0,9:1,10:0,11:2,12:0,13:0,14:2}
adj={v:set() for v in range(badgraph.n)}
for u,v in badgraph.edges:
    adj[u].add(v); adj[v].add(u)
sigma={v:len(adj[v])*(1+rho[v])+sum(rho[u] for u in adj[v]) for v in adj}
assert max(rho.values())<=2
assert all(sigma[u]!=sigma[v] for u,v in badgraph.edges)
mod_conflicts=sorted((u,v,sigma[u]%3) for u,v in badgraph.edges if sigma[u]%3==sigma[v]%3)
assert mod_conflicts

print('R0_size=',len(R0),'R1_size=',len(R1),'R2_size=',len(R2),'R3_size=',len(R3))
print('bridge_state_sizes=',[len(x) for x in R])
print('bridge_stabilizes_at_k=3=',R3==ALL)
print('triangle_table_special_cases=R0R0:A,R2R2:C,all_other:ALL')
print('three_cycle_Y_min_diagonal=',y_min,'arg=',y_arg[:3])
print('three_cycle_PATH_min_diagonal=',p_min,'arg=',p_arg[:2])
print('three_cycle_triangular_core_all_cases_PASS=True')
print('four_cycle_bad_relation_size=',len(bad_relation))
print('four_cycle_graph_n=',badgraph.n,'m=',len(badgraph.edges),'cyclomatic=',len(badgraph.edges)-badgraph.n+1)
print('four_cycle_edges=',sorted(badgraph.edges))
print('integer_witness_rho=',rho)
print('integer_witness_sigma=',sigma)
print('integer_witness_mod3_conflicts=',mod_conflicts)
print('integer_witness_proper=True')
print('VERDICT=PASS')
