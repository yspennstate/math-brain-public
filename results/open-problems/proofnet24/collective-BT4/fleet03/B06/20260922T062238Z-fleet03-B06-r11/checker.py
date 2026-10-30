import itertools, collections, json, hashlib

ADJ = {
0:[1,6,8,9,11,13,14],
1:[2,9,10,13,14,15,17],
2:[3,6,7,9,11,13,16],
3:[4,6,8,11,13,15,17],
4:[5,6,10,11,13,14,16],
5:[0,6,7,8,9,14,16],
6:[1,7,12,13,14,15,17],
7:[0,1,4,8,14,15,16],
8:[1,2,4,9,11,15,17],
9:[3,4,10,11,14,16,17],
10:[0,2,3,6,11,14,17],
11:[1,5,7,12,14,15,16],
12:[0,1,2,7,8,13,14],
13:[5,7,8,9,10,11,17],
14:[2,3,8,13,15,16,17],
15:[0,2,4,5,10,12,16],
16:[0,1,3,6,8,10,12],
17:[0,2,4,5,7,11,12]
}
V=set(ADJ)
E={(a,b) for a,vs in ADJ.items() for b in vs}
H=[0,1,2,3,4,5]
U=[6,7,8,9,10]
S=[11,12,13]
p,x,s,q=11,12,13,14
K=[15,16,17]
u=6
OLD_R=[x]+K
RSTAR=[q]+K
Q=[[p,s]+[r for r in K if r!=ri] for ri in K]

def cyc_edges(C):
    return {(C[i],C[(i+1)%len(C)]) for i in range(len(C))}

def induced_arcs(nodes):
    N=set(nodes)
    return sum((a in N and b in N) for a,b in E)

def is_acyclic(nodes):
    N=set(nodes)
    indeg={v:0 for v in N}
    for a in N:
        for b in ADJ[a]:
            if b in N: indeg[b]+=1
    dq=collections.deque(v for v in N if indeg[v]==0)
    seen=0
    while dq:
        v=dq.popleft(); seen+=1
        for w in ADJ[v]:
            if w in N:
                indeg[w]-=1
                if indeg[w]==0: dq.append(w)
    return seen==len(N)

def reach(src,removed):
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
    return all(reach(v,removed)>=left for v in left)

def common_preds(a,b):
    return sorted(z for z in V if z not in (a,b) and (z,a) in E and (z,b) in E)

assert V==set(range(18))
assert len(E)==126
assert all(len(ADJ[v])==7 and v not in ADJ[v] for v in V)
assert all((b,a) not in E for a,b in E)

for C in (H,U,S):
    ce=cyc_edges(C)
    assert ce <= E
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
    "H":sorted(set(ADJ[q])&set(H)),
    "U":sorted(set(ADJ[q])&set(U)),
    "S":sorted(set(ADJ[q])&set(S)),
    "R":sorted(set(ADJ[q])&set(RSTAR)),
}
assert profile=={"H":[2,3],"U":[8],"S":[13],"R":[15,16,17]}

assert is_acyclic(OLD_R) and is_acyclic(RSTAR)
assert [v for v in OLD_R if not (set(ADJ[v])&set(OLD_R))]==[x]
old_a=induced_arcs(OLD_R); assert old_a==4
q_counts=[]
for nodes in Q:
    assert is_acyclic(nodes)
    q_counts.append(induced_arcs(nodes))
assert q_counts==[4,4,4]

cover={}
for r in K:
    cover[r]=[w for w in (p,u) if all((w,t) in E for t in (q,r,x))]
assert cover=={15:[p,u],16:[p],17:[u]}
A={r for r in K if p in cover[r]}
B={r for r in K if u in cover[r]}
assert A=={15,16} and B=={15,17}

assert common_preds(p,x)==[17]
assert common_preds(u,x)==[16]
assert (u,p) not in E and (p,u) not in E

W=[u,17,p,16]
assert cyc_edges(W)<=E
assert set(W)&set(K)=={16,17}
assert set(W)&(set(H)|set(U)|set(S))=={u,p}

outside_remainder=[q]+sorted(set(K)-set(W))
rem_hit_counts={v:len(set(ADJ[v])&set(W)) for v in outside_remainder}
assert rem_hit_counts=={14:2,15:1}
assert len(set(ADJ[x])&set(W))==0

three_hit={v:sorted(set(ADJ[v])&set(W)) for v in V-set(W)
           if len(set(ADJ[v])&set(W))>=3}
packed=(set(H)|set(U)|set(S))
assert three_hit
assert all(v in packed and v!=x for v in three_hit)
assert three_hit[9]==[11,16,17]

assert all(common_preds(a,b) for a,b in E)
for k in (0,1,2):
    for rem in itertools.combinations(sorted(V),k):
        assert strong_after_remove(rem)

four_pack=[[0,1,10],[2,3,8],[4,5,7],[6,14,16]]
assert all(cyc_edges(C)<=E for C in four_pack)
assert sum(map(len,four_pack))==len(set().union(*map(set,four_pack)))

symbolic={"cover_assignments":27,"both_repeat_profiles":0,
          "all_both_impossible_profiles":0,"admissible_cross_scenarios":0,
          "triangle_returns":0,"quadrilateral_returns":0}
for lab in itertools.product((1,2,3), repeat=3):
    AA={i for i,L in enumerate(lab) if L&1}
    BB={i for i,L in enumerate(lab) if L&2}
    assert AA|BB=={0,1,2}
    if len(AA)<2 or len(BB)<2:
        continue
    symbolic["both_repeat_profiles"]+=1
    pd=["u"]+sorted(set(range(3))-AA)
    ud=["p"]+sorted(set(range(3))-BB)
    valid=0
    for dp in pd:
        for du in ud:
            if dp=="u" and du=="p":
                continue
            I1=set() if dp=="u" else {dp}
            I2=set() if du=="p" else {du}
            assert I1.isdisjoint(I2)
            I=I1|I2
            wlen=2+len(I)
            assert wlen in (3,4)
            assert len(I)<=2
            for t in set(range(3))-I:
                can_hit_p=t not in AA
                can_hit_u=t not in BB
                assert int(can_hit_p)+int(can_hit_u)+len(I)<=2
            valid+=1
            symbolic["admissible_cross_scenarios"]+=1
            symbolic["triangle_returns" if wlen==3 else "quadrilateral_returns"]+=1
    if not valid:
        assert AA==BB=={0,1,2}
        symbolic["all_both_impossible_profiles"]+=1

assert symbolic=={
    "cover_assignments":27,
    "both_repeat_profiles":13,
    "all_both_impossible_profiles":1,
    "admissible_cross_scenarios":24,
    "triangle_returns":18,
    "quadrilateral_returns":6,
}

payload={
    "certificate":{
        "n":18,
        "arcs":len(E),
        "outdegree":7,
        "oriented":True,
        "three_vertex_strong":True,
        "all_arcs_dominated":True,
        "old_remainder_arc_count":old_a,
        "triangle_exchange_remainder_arc_counts":q_counts,
        "F3_profile":profile,
        "witness_cover":{str(r):cover[r] for r in K},
        "p_x_common_predecessors":common_preds(p,x),
        "u_x_common_predecessors":common_preds(u,x),
        "p_u_nonadjacent":True,
        "forced_short_return_cycle":W,
        "outside_remainder_hit_counts":rem_hit_counts,
        "packed_three_hit_witnesses":three_hit,
        "sharp_witness_missing_u":9,
        "four_pack":four_pack,
    },
    "symbolic":symbolic,
    "result":"PASS"
}
canon=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
payload["payload_sha256"]=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
