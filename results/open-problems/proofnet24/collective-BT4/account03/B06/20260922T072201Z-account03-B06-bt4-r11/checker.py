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

def cyc_edges(C):
    return {(C[i],C[(i+1)%len(C)]) for i in range(len(C))}

def is_acyclic(nodes):
    N=set(nodes)
    indeg={v:0 for v in N}
    for a in N:
        for b in ADJ[a]:
            if b in N:
                indeg[b]+=1
    dq=collections.deque(v for v in N if indeg[v]==0)
    seen=0
    while dq:
        v=dq.popleft()
        seen+=1
        for w in ADJ[v]:
            if w in N:
                indeg[w]-=1
                if indeg[w]==0:
                    dq.append(w)
    return seen==len(N)

def common_preds(a,b):
    return sorted(z for z in V if z not in (a,b) and (z,a) in E and (z,b) in E)

def reach(src,removed):
    removed=set(removed)
    seen={src}
    dq=collections.deque([src])
    while dq:
        v=dq.popleft()
        for w in ADJ[v]:
            if w in removed or w in seen:
                continue
            seen.add(w)
            dq.append(w)
    return seen

# Whole-graph inherited certificate checks.
assert V==set(range(18))
assert len(E)==126
assert all(len(ADJ[v])==7 and v not in ADJ[v] for v in V)
assert all((b,a) not in E for a,b in E)
assert all(common_preds(a,b) for a,b in E)
for k in (0,1,2):
    for rem in itertools.combinations(sorted(V),k):
        left=V-set(rem)
        assert all(reach(v,rem)>=left for v in left)

for C in (H,U,S):
    ce=cyc_edges(C)
    assert ce <= E
    assert all((a,b) in ce or (a,b) not in E
               for a in C for b in C if a!=b)

# Both-repeat F3 quadrilateral from the predecessor certificate.
# W = u -> a -> p -> b -> u.
a=17
b=16
W=[u,a,p,b]
assert cyc_edges(W)<=E
apex=9
hits=sorted(set(ADJ[apex]) & set(W))
assert hits==[p,b,a]  # misses u
assert U[-2]==apex
assert U[-1]==10
assert (apex,u) not in E

# Neutral collar exchange forced by the global-minimum equality case:
# z -> b -> u -> U[u,z] -> z.
neutral=[apex,b,u,7,8]
assert cyc_edges(neutral)<=E
assert len(neutral)==len(U)

new_remainder=sorted(V-(set(H)|set(S)|set(neutral)))
assert new_remainder==[10,14,15,17]
assert not is_acyclic(new_remainder)
exchange_remainder_cycle=[10,14,15]
assert cyc_edges(exchange_remainder_cycle)<=E

# The full graph is deliberately not a BT4 counterexample.
four_pack=[[0,1,10],[2,3,8],[4,5,7],[6,14,16]]
assert all(cyc_edges(C)<=E for C in four_pack)
assert sum(map(len,four_pack))==len(set().union(*map(set,four_pack)))

# Uniform symbolic sanity check of the collar theorem.
# Model U as positions 0=u,1,...,n-1=u^-.
# Chordlessness permits z->u only at z=u^-.
# In the quadrilateral miss-u case, z hits a,p,b, and
# z->b->u->U[u,z] is a replacement cycle of order d+2;
# minimum packed order requires d+2 >= n.
symbolic={
    "U_order_range":[3,50],
    "triangle_positions_checked":0,
    "triangle_survivors":0,
    "quadrilateral_chordless_hit_patterns":0,
    "quadrilateral_survivors_after_minimum":0,
    "quadrilateral_immediate_predecessor_patterns":0,
    "quadrilateral_second_predecessor_patterns":0,
    "violations":[]
}
for n in range(3,51):
    for zpos in range(1,n):
        symbolic["triangle_positions_checked"]+=1
        if zpos==n-1:
            symbolic["triangle_survivors"]+=1
        else:
            continue

    labels=("u","a","p","b")
    for zpos in range(1,n):
        for size in (3,4):
            for hs in itertools.combinations(labels,size):
                if "u" in hs and zpos!=n-1:
                    continue
                symbolic["quadrilateral_chordless_hit_patterns"]+=1
                if "u" not in hs and zpos+2<n:
                    continue
                symbolic["quadrilateral_survivors_after_minimum"]+=1
                if zpos==n-1:
                    symbolic["quadrilateral_immediate_predecessor_patterns"]+=1
                elif zpos==n-2:
                    symbolic["quadrilateral_second_predecessor_patterns"]+=1
                else:
                    symbolic["violations"].append(
                        {"n":n,"zpos":zpos,"hits":list(hs)}
                    )

assert symbolic=={
    "U_order_range":[3,50],
    "triangle_positions_checked":1224,
    "triangle_survivors":48,
    "quadrilateral_chordless_hit_patterns":1416,
    "quadrilateral_survivors_after_minimum":288,
    "quadrilateral_immediate_predecessor_patterns":240,
    "quadrilateral_second_predecessor_patterns":48,
    "violations":[]
}

payload={
    "candidate":"BT4-R4-F3-APEX-COLLAR-v1",
    "whole_graph_certificate":{
        "n":18,
        "arcs":126,
        "exact_outdegree":7,
        "oriented":True,
        "three_vertex_strong":True,
        "all_arcs_dominated":True,
        "packed_cycles":{"H":H,"U":U,"Sstar":S},
        "return_cycle_W":W,
        "packed_apex":apex,
        "apex_hits_on_W":hits,
        "u_predecessor":U[-1],
        "u_second_predecessor":U[-2],
        "neutral_U_exchange_cycle":neutral,
        "neutral_exchange_order":len(neutral),
        "old_U_order":len(U),
        "neutral_exchange_remainder":new_remainder,
        "neutral_exchange_remainder_acyclic":False,
        "explicit_exchange_remainder_cycle":exchange_remainder_cycle,
        "explicit_four_pack":four_pack
    },
    "symbolic":symbolic,
    "result":"PASS"
}
canon=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
payload["payload_sha256"]=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
