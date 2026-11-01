from itertools import combinations, permutations
V=['t0','t1','t2','a0','a1','a2','b0','b1','b2','r0','s0','r1','s1','r2','s2','z']
adj_txt={
't0':'t1,a0,a2,b0,b1,b2,r0',
't1':'t2,a0,a1,a2,b0,b2,r1',
't2':'t0,a0,b1,r0,s0,r2,s2',
'a0':'a1,b0,b2,r0,r1,s1,s2',
'a1':'t0,t2,a2,b0,r1,s1,r2',
'a2':'t2,a0,b2,r0,s0,r1,z',
'b0':'t2,a2,b1,s0,r1,s1,r2',
'b1':'t1,a0,a1,a2,b2,s1,s2',
'b2':'t2,a1,b0,r1,s1,r2,z',
'r0':'t1,a1,b0,b2,s0,r1,r2',
's0':'a0,a1,b1,b2,r1,s2,z',
'r1':'t0,t2,b1,s1,r2,s2,z',
's1':'t0,t1,t2,a2,r2,s2,z',
'r2':'t0,t1,a0,a2,b1,s2,z',
's2':'t0,t1,a1,a2,b0,b2,z',
'z':'t0,t1,t2,a0,a1,b0,b1'}
adj={u:set(vs.split(',')) if vs else set() for u,vs in adj_txt.items()}

def arc(u,v): return v in adj[u]
def acyclic(S):
    S=set(S); state={v:0 for v in S}
    def dfs(u):
        state[u]=1
        for v in adj[u]&S:
            if state[v]==1: return False
            if state[v]==0 and not dfs(v): return False
        state[u]=2; return True
    return all(state[u] or dfs(u) for u in list(S))
def reach(S,start,rev=False):
    S=set(S); seen={start}; st=[start]
    while st:
        u=st.pop()
        nei=([v for v in S if u in adj[v]] if rev else list(adj[u]&S))
        for v in nei:
            if v not in seen: seen.add(v); st.append(v)
    return seen
def strong_after(rem):
    S=set(V)-set(rem); s=next(iter(S))
    return len(reach(S,s))==len(S) and len(reach(S,s,True))==len(S)
def directed_triangle(C):
    a,b,c=C
    return arc(a,b) and arc(b,c) and arc(c,a)

assert all(len(adj[v])==7 for v in V)
assert all(v not in adj[v] for v in V)
assert all(not (arc(u,v) and arc(v,u)) for u in V for v in V if u!=v)
for k in range(3):
    for rem in combinations(V,k): assert strong_after(rem)
for u in V:
    for v in adj[u]:
        assert any(q not in (u,v) and arc(q,u) and arc(q,v) for q in V), (u,v)
T=('t0','t1','t2'); A=('a0','a1','a2'); B=('b0','b1','b2')
assert directed_triangle(T) and directed_triangle(A) and directed_triangle(B)
R={'r0','s0','r1','s1','r2','s2','z'}
assert acyclic(R)
for i in range(3):
    assert arc(f't{i}',f'r{i}') and arc(f'r{i}',f's{i}') and arc(f's{i}','z')
assert set(adj['z']) & set(T) == set(T)
assert set(adj['z']) & set(A) == {'a0','a1'}
assert set(adj['z']) & set(B) == {'b0','b1'}
assert not (set(adj['z']) & R)

# Since the graph is oriented, all directed cycles have length at least three;
# T,A,B are triangles, so this three-cycle packing is globally minimum in total order.
Q=('t1','t2','r0')
assert directed_triangle(Q)
R_Q=(set(V)-set(Q)-set(A)-set(B))
assert acyclic(R_Q)

tris=[]
for C in combinations(V,3):
    for p in permutations(C):
        if directed_triangle(p): tris.append(tuple(p)); break
pack=None
for cs in combinations(tris,4):
    U=set(); ok=True
    for c in cs:
        if U & set(c): ok=False; break
        U |= set(c)
    if ok: pack=cs;break
assert pack is not None
print('PASS')
print('vertices',len(V),'arcs',sum(len(adj[v]) for v in V),'outdegree',sorted({len(adj[v]) for v in V}))
print('3_vertex_strong',True,'arc_dominated',True,'remainder_acyclic',True)
print('pinwheel_fans', {'T':3,'A':2,'B':2})
print('neutral_exchange',Q,'new_remainder',sorted(R_Q),'new_remainder_acyclic',True)
print('four_triangle_pack',pack)

# Highly asymmetric digon boundary: complete bidirected K_11 minus six directed arcs.
DV=[f'd{i}' for i in range(11)]
dadj={u:{v for v in DV if v!=u} for u in DV}
for v in ['d8','d9','d10']: dadj['d0'].remove(v)
for v in ['d9','d10']: dadj['d1'].remove(v)
dadj['d2'].remove('d10')
assert 'd4' in dadj['d3'] and 'd3' in dadj['d4']
deg=[len(dadj[v]) for v in DV]
assert deg==[7,8,9,10,10,10,10,10,10,10,10]
left=[v for v in DV if v not in {'d3','d4'}]
after={v:len(dadj[v]&set(left)) for v in left}
assert min(after.values())==5 and after['d0']==5
print('digon_adversary_degree_vector',deg)
print('digon_deleted','d3,d4','surviving_min_outdegree',min(after.values()),'d0_outdegree',after['d0'])
