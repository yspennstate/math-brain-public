import itertools, collections, json, hashlib

ADJ = {0: [1, 7, 8, 10, 11, 12, 14], 1: [2, 5, 7, 10, 11, 12, 16], 2: [3, 5, 6, 7, 9, 14, 15], 3: [4, 5, 9, 10, 11, 12, 14], 4: [0, 5, 6, 11, 14, 15, 16], 5: [0, 6, 10, 12, 14, 15, 16], 6: [0, 1, 3, 7, 12, 13, 16], 7: [3, 4, 8, 10, 11, 14, 15], 8: [1, 2, 3, 4, 9, 12, 15], 9: [0, 1, 4, 5, 11, 14, 16], 10: [2, 4, 6, 8, 9, 11, 13], 11: [2, 5, 6, 8, 12, 13, 14], 12: [2, 4, 7, 9, 10, 15, 16], 13: [2, 3, 7, 8, 12, 15, 16], 14: [6, 8, 10, 12, 13, 15, 16], 15: [0, 1, 3, 6, 9, 10, 11], 16: [0, 2, 3, 7, 8, 10, 11]}
V = set(ADJ)
E = {(u,v) for u,vs in ADJ.items() for v in vs}
H = [0,1,2,3,4]
U = [5,6,7,8,9]
S = [10,11,12]
R = [13,14,15,16]
q,r0,r1,r2 = 13,14,15,16
p,x,pp = 10,11,12
R2 = [q,pp,r1,r2]
W = [x,r0,p]

def cyc_edges(c):
    return {(c[i], c[(i+1)%len(c)]) for i in range(len(c))}

def is_acyclic(nodes):
    nodes=set(nodes); state={v:0 for v in nodes}
    def dfs(u):
        state[u]=1
        for v in ADJ[u]:
            if v not in nodes: continue
            if state[v]==1: return False
            if state[v]==0 and not dfs(v): return False
        state[u]=2
        return True
    return all(state[u] or dfs(u) for u in list(nodes))

def reach(src, rem):
    if src in rem: return set()
    seen={src}; dq=collections.deque([src])
    while dq:
        u=dq.popleft()
        for v in ADJ[u]:
            if v in rem or v in seen: continue
            seen.add(v); dq.append(v)
    return seen

def strong_after_remove(rem):
    left=V-set(rem)
    return all(reach(s,set(rem))>=left for s in left)

def common_preds(u,v):
    return sorted(z for z in V if z not in (u,v) and u in ADJ[z] and v in ADJ[z])

# Exact full-graph certificate.
assert V == set(range(17))
assert all(len(ADJ[u]) == 7 and u not in ADJ[u] for u in V)
assert all((v,u) not in E for u,v in E)  # oriented
for C in (H,U,S,W):
    assert cyc_edges(C) <= E
for C in (H,U,S):
    ce=cyc_edges(C)
    assert all((a,b) in ce or (a,b) not in E for a in C for b in C if a!=b)  # chordless
assert is_acyclic(R)
assert is_acyclic(R2)
assert strong_after_remove(())
for k in (1,2):
    for rem in itertools.combinations(sorted(V),k):
        assert strong_after_remove(rem)
assert all(any(z not in (u,v) and (z,u) in E and (z,v) in E for z in V) for u,v in E)

# Exact F2 profile and the source-triangle domination lock.
profile = {
    "H": sorted(set(ADJ[q]) & set(H)),
    "U": sorted(set(ADJ[q]) & set(U)),
    "S": sorted(set(ADJ[q]) & set(S)),
    "R": sorted(set(ADJ[q]) & set(R)),
}
assert profile == {"H":[2,3],"U":[7,8],"S":[12],"R":[15,16]}
assert r0 not in ADJ[q] and q in ADJ[r0]
for a,b in ((x,r0),(r0,p),(p,x),(x,q),(p,q),(r0,q)):
    assert b in ADJ[a]
assert common_preds(r0,q) == [x]
assert common_preds(x,q) == [p]
assert common_preds(p,q) == [r0]

# This local realization is not a target counterexample: explicit four-pack.
four_pack = [[0,1,5],[2,3,10],[4,6,7],[8,9,11]]
assert all(cyc_edges(C) <= E for C in four_pack)
assert sum(map(len,four_pack)) == len(set().union(*map(set,four_pack)))

# Symbolic finite sanity for the uniform predecessor-closure step:
# a nonempty predecessor-closed subset of a directed cycle is the whole cycle.
closure_cases=0
for n in range(3,13):
    for mask in range(1,1<<n):
        P={i for i in range(n) if mask>>i & 1}
        pred_closed=all(((v-1)%n) in P for v in P)
        if pred_closed:
            closure_cases += 1
            assert len(P)==n

# Arithmetic sanity for the F2 heavy-cycle replacement contradiction:
# m=2 fan targets are disjoint from a predecessor chain of j+1 inports.
chain_cases=0
for n in range(3,101):
    for j in range(0,n):
        if j+1 <= n-2:
            chain_cases += 1
            assert j+2 <= n-1

payload={
    "certificate": {
        "n":17,
        "arcs":len(E),
        "outdegree":7,
        "old_remainder_acyclic":is_acyclic(R),
        "exchanged_remainder_acyclic":is_acyclic(R2),
        "three_vertex_strong":all(strong_after_remove(rem) for k in (0,1,2) for rem in itertools.combinations(sorted(V),k)),
        "all_arcs_dominated":all(any(z not in (u,v) and (z,u) in E and (z,v) in E for z in V) for u,v in E),
        "F2_profile":profile,
        "unique_lock_common_predecessors":{
            "r0_to_q":common_preds(r0,q),
            "x_to_q":common_preds(x,q),
            "p_to_q":common_preds(p,q)
        },
        "lock_triangle":W,
        "four_pack":four_pack
    },
    "symbolic": {
        "predecessor_closure_cases":closure_cases,
        "chain_arithmetic_cases":chain_cases,
        "n_cycle_max":12,
        "chain_n_max":100
    },
    "result":"PASS"
}
canon=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
payload["payload_sha256"]=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
