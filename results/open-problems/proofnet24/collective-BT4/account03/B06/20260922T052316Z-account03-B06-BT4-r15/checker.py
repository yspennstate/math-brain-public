import itertools, collections, json, hashlib

ADJ = {
0:[1,8,9,11,13,14,15],
1:[2,9,10,11,13,15,17],
2:[3,6,7,9,11,13,16],
3:[4,6,8,11,13,15,17],
4:[5,6,10,11,13,14,16],
5:[0,6,7,8,9,14,16],
6:[0,1,7,12,13,14,17],
7:[0,1,4,8,14,15,16],
8:[1,2,4,9,11,15,17],
9:[3,4,10,11,14,16,17],
10:[0,2,3,6,11,14,17],
11:[5,6,7,12,14,15,16],
12:[0,1,2,7,8,13,14],
13:[5,7,8,9,10,11,17],
14:[2,3,8,13,15,16,17],
15:[2,4,5,6,10,12,16],
16:[0,1,3,6,8,10,12],
17:[0,2,4,5,7,11,12]
}
V=set(ADJ)
E={(a,b) for a,vs in ADJ.items() for b in vs}
H=[0,1,2,3,4,5]
U=[6,7,8,9,10]
S=[11,12,13]  # post-pivot packed source triangle p->x->s->p
p,x,s,q=11,12,13,14
K=[15,16,17]
u=6
OLD_R=[x]+K
RSTAR=[q]+K
Q=[ [p,s]+[r for r in K if r!=ri] for ri in K ]

def cyc_edges(C):
    return {(C[i],C[(i+1)%len(C)]) for i in range(len(C))}

def induced_arcs(nodes):
    N=set(nodes)
    return sum((a in N and b in N) for a,b in E)

def is_acyclic(nodes):
    N=set(nodes)
    state={v:0 for v in N}
    def dfs(v):
        state[v]=1
        for w in ADJ[v]:
            if w not in N: continue
            if state[w]==1: return False
            if state[w]==0 and not dfs(w): return False
        state[v]=2
        return True
    return all(state[v] or dfs(v) for v in list(N))

def reach(src, removed):
    removed=set(removed)
    seen={src}; dq=collections.deque([src])
    while dq:
        v=dq.popleft()
        for w in ADJ[v]:
            if w in removed or w in seen: continue
            seen.add(w); dq.append(w)
    return seen

def strong_after_remove(removed):
    removed=set(removed); left=V-removed
    return all(reach(v,removed) >= left for v in left)

def common_preds(a,b):
    return sorted(z for z in V if z not in (a,b) and (z,a) in E and (z,b) in E)

assert V==set(range(18))
assert len(E)==126
assert all(len(ADJ[v])==7 and v not in ADJ[v] for v in V)
assert all((b,a) not in E for a,b in E)
for C in (H,U,S):
    assert cyc_edges(C) <= E
    ce=cyc_edges(C)
    assert all((a,b) in ce or (a,b) not in E for a in C for b in C if a!=b)

assert (p,q) in E and (q,s) in E and (x,q) in E
assert all((r,x) in E for r in K)
assert set(ADJ[x]) & set(H) == {0,1,2}
assert set(ADJ[x]) & set(U) == {7,8}
assert set(ADJ[x]) & set(S) == {13}
assert set(ADJ[x]) & set(RSTAR) == {q}
assert all((h,x) not in E for h in H)
assert (u,x) in E and all((v,x) not in E for v in U if v!=u)

profile={
    "H":sorted(set(ADJ[q]) & set(H)),
    "U":sorted(set(ADJ[q]) & set(U)),
    "S":sorted(set(ADJ[q]) & set(S)),
    "R":sorted(set(ADJ[q]) & set(RSTAR)),
}
assert profile=={"H":[2,3],"U":[8],"S":[13],"R":[15,16,17]}

assert is_acyclic(OLD_R) and is_acyclic(RSTAR)
assert [v for v in OLD_R if not (set(ADJ[v]) & set(OLD_R))] == [x]
old_a=induced_arcs(OLD_R); assert old_a==4
q_counts=[]
for nodes in Q:
    assert is_acyclic(nodes)
    q_counts.append(induced_arcs(nodes))
assert q_counts==[4,4,4]
assert all(a<=old_a for a in q_counts)

cover={}
for r in K:
    cover[r]=[w for w in (p,u) if all((w,t) in E for t in (q,r,x))]
assert cover=={15:[p],16:[p],17:[u]}
assert common_preds(p,x)==[17]
assert (u,17) in E and (17,p) in E and (u,p) not in E

assert all(common_preds(a,b) for a,b in E)
for k in (0,1,2):
    for rem in itertools.combinations(sorted(V),k):
        assert strong_after_remove(rem)

four_pack=[[0,1,10],[2,3,8],[4,5,7],[6,13,11]]
assert all(cyc_edges(C) <= E for C in four_pack)
assert sum(map(len,four_pack)) == len(set().union(*map(set,four_pack)))

labels=(1,2,3)
symbolic={"assignments":0,"both_repeated":0,"only_p_repeated":0,
          "only_u_repeated":0,"dominator_scenarios":0,
          "opposite_cross_scenarios":0}
for lab in itertools.product(labels, repeat=3):
    symbolic["assignments"] += 1
    P={i for i,L in enumerate(lab) if L&1}
    Uc={i for i,L in enumerate(lab) if L&2}
    assert P | Uc == {0,1,2}
    rp,ru=(len(P)>=2),(len(Uc)>=2)
    assert rp or ru
    if rp and ru: symbolic["both_repeated"] += 1
    elif rp: symbolic["only_p_repeated"] += 1
    else: symbolic["only_u_repeated"] += 1

    pdom=(["u"]+[i for i in range(3) if i not in P]) if rp else []
    udom=(["p"]+[i for i in range(3) if i not in Uc]) if ru else []

    for d in pdom:
        symbolic["dominator_scenarios"] += 1
        if d!="u": assert d in Uc
    for d in udom:
        symbolic["dominator_scenarios"] += 1
        if d!="p": assert d in P

    if rp and ru:
        for dp in pdom:
            for du in udom:
                symbolic["opposite_cross_scenarios"] += 1
                Ip=set() if dp=="u" else {dp}
                Iu=set() if du=="p" else {du}
                assert Ip.isdisjoint(Iu)

assert symbolic=={
    "assignments":27,
    "both_repeated":13,
    "only_p_repeated":7,
    "only_u_repeated":7,
    "dominator_scenarios":64,
    "opposite_cross_scenarios":37,
}

payload={
    "certificate":{
        "n":18,
        "arcs":len(E),
        "outdegree":7,
        "three_vertex_strong":all(
            strong_after_remove(rem)
            for k in (0,1,2)
            for rem in itertools.combinations(sorted(V),k)
        ),
        "all_arcs_dominated":all(common_preds(a,b) for a,b in E),
        "old_remainder_arc_count":old_a,
        "triangle_exchange_remainder_arc_counts":q_counts,
        "old_remainder_acyclic":is_acyclic(OLD_R),
        "postpivot_remainder_acyclic":is_acyclic(RSTAR),
        "triangle_exchange_remainders_acyclic":all(is_acyclic(nodes) for nodes in Q),
        "F3_profile":profile,
        "witness_cover":cover,
        "p_to_x_common_predecessors":common_preds(p,x),
        "short_cross":[u,17,p],
        "short_cross_direct":(u,p) in E,
        "four_pack":four_pack
    },
    "symbolic":symbolic,
    "result":"PASS"
}
canon=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
payload["payload_sha256"]=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
