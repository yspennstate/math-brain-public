from fractions import Fraction
from itertools import combinations

# Exact route-kill for the too-strong whole-h discriminant strategy in P14.
# A has vertices 0..6 and terminals x,y,z = 0,1,2.
A_EDGES = [
    (0,3),(0,4),(1,3),(1,4),(1,5),(1,6),
    (2,4),(2,5),(3,4),(3,6),(4,5),(5,6),
]
E_INDEX = 0   # e=(0,3)
F_INDEX = 7   # f=(2,5)
TERMINALS = (0,1,2)
W = 7
G_EDGES = A_EDGES + [(W,0),(W,1),(W,2)]


def forest_ok(n, edges, mask):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i,(u,v) in enumerate(edges):
        if (mask >> i) & 1:
            a,b = find(u),find(v)
            if a == b:
                return False, None
            parent[a] = b
    return True, find


def constrained_partition_counts():
    # state order: d=x|y|z, a=xy|z, b=xz|y, c=yz|x, t=xyz
    out = {c:[0,0,0,0,0] for c in range(4)}
    for mask in range(1 << len(A_EDGES)):
        ok, find = forest_ok(7, A_EDGES, mask)
        if not ok:
            continue
        roots = [find(t) for t in TERMINALS]
        if roots[0] == roots[1] == roots[2]:
            s = 4
        elif roots[0] == roots[1] != roots[2]:
            s = 1
        elif roots[0] == roots[2] != roots[1]:
            s = 2
        elif roots[1] == roots[2] != roots[0]:
            s = 3
        else:
            s = 0
        e = (mask >> E_INDEX) & 1
        f = (mask >> F_INDEX) & 1
        out[0][s] += 1
        if e: out[1][s] += 1
        if f: out[2][s] += 1
        if e and f: out[3][s] += 1
    return out


def triangle_base_and_defect(counts):
    mu = Fraction(1,4)
    F, d = [], []
    for C in range(4):
        dc,a,b,c,t = counts[C]
        val = (Fraction(dc)*(1+3*mu+3*mu*mu)
               + Fraction(a+b+c)*(1+2*mu) + Fraction(t))
        F.append(val)
        d.append(Fraction(dc))
    Z,Ze,Zf,Zef = F
    D,De,Df,Def = d
    q0 = Ze*Zf - Z*Zef
    q1 = Ze*Df + De*Zf - Z*Def - D*Zef
    q2 = De*Df - D*Def
    return F,d,(q0,q1,q2)


def direct_pair_counts(n, edges, ei, fi):
    Z=Ze=Zf=Zef=0
    for mask in range(1 << len(edges)):
        ok,_ = forest_ok(n, edges, mask)
        if not ok: continue
        Z += 1
        e = (mask >> ei) & 1
        f = (mask >> fi) & 1
        if e: Ze += 1
        if f: Zf += 1
        if e and f: Zef += 1
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef


def connected_after_delete(vertices_deleted):
    alive = [v for v in range(8) if v not in vertices_deleted]
    if not alive: return True
    adj = {v:[] for v in alive}
    for u,v in G_EDGES:
        if u in adj and v in adj:
            adj[u].append(v); adj[v].append(u)
    seen={alive[0]}; stack=[alive[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==len(alive)


def exact_three_connected():
    for k in (0,1,2):
        for S in combinations(range(8),k):
            if not connected_after_delete(set(S)):
                return False,S
    return True,None


def automorphism_check():
    sigma={0:2,2:0,3:5,5:3,1:1,4:4,6:6,7:7}
    canon=lambda e: tuple(sorted(e))
    E={canon(e) for e in G_EDGES}
    image={canon((sigma[u],sigma[v])) for u,v in G_EDGES}
    return image==E, canon((sigma[0],sigma[3]))==canon((2,5))

counts = constrained_partition_counts()
expected = {
    0:[406,286,128,286,430],
    1:[100,181,51,57,239],
    2:[100,57,51,181,239],
    3:[24,38,22,38,134],
}
assert counts == expected, counts
F,d,(q0,q1,q2)=triangle_base_and_defect(counts)
assert F == [Fraction(18133,8),Fraction(3465,4),Fraction(3465,4),Fraction(655,2)]
assert d == [Fraction(406),Fraction(100),Fraction(100),Fraction(24)]
assert (q0,q1,q2)==(Fraction(64555,8),Fraction(-14114),Fraction(256))
D=q1*q1-4*q0*q2
assert D==190941956 and D>0
q_phys=q0+q1*Fraction(1,16)+q2*Fraction(1,256)
q_one=q0+q1+q2
assert q_phys==Fraction(28753,4) and q_phys>0
assert q_one==Fraction(-46309,8) and q_one<0

direct=direct_pair_counts(8,G_EDGES,E_INDEX,F_INDEX)
assert direct==(9168,3490,3490,1316,115012), direct
assert direct[-1] == 16*q_phys
three_conn,bad=exact_three_connected()
assert three_conn, bad
auto,swaps=automorphism_check()
assert auto and swaps

print('A_edges=',A_EDGES)
print('terminals=',TERMINALS,'e=',A_EDGES[E_INDEX],'f=',A_EDGES[F_INDEX])
print('partition_counts=',counts)
print('triangle_base_F=',F)
print('defect_d=',d)
print('q0_q1_q2=',(q0,q1,q2))
print('discriminant=',D)
print('q(1/16)=',q_phys)
print('q(1)=',q_one)
print('star_direct_Z_Ze_Zf_Zef_Delta=',direct)
print('G_is_3_vertex_connected=',three_conn)
print('automorphism_(0 2)(3 5)_preserves_G_and_swaps_pair=',auto and swaps)
print('VERDICT: whole-h/discriminant strengthening is FALSE; physical h=1/16 remains strictly positive.')
print('ROUTE_KILL_EXACT_PASS')
