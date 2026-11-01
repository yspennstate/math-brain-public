from itertools import product

# Exact 10-vertex subcubic tree:
# central c joined to three degree-3 vertices v1,v2,v3;
# each vi joined to two leaves ai,bi.
V = ['c','v1','v2','v3','a1','b1','a2','b2','a3','b3']
E = [
    ('c','v1'),('c','v2'),('c','v3'),
    ('v1','a1'),('v1','b1'),
    ('v2','a2'),('v2','b2'),
    ('v3','a3'),('v3','b3'),
]
B = {'c','v1','v2','v3'}

def is_matching(S):
    used=set()
    for i in S:
        u,v=E[i]
        if u in used or v in used:
            return False
        used.add(u); used.add(v)
    return True

def covers_B(S):
    cov=set()
    for i in S:
        cov.update(E[i])
    return B <= cov

def exactly_one_B_each(S):
    return all(((u in B)+(v in B)==1) for i in S for (u,v) in [E[i]])

def degrees_after_delete(S):
    d={v:0 for v in V}
    S=set(S)
    for i,(u,v) in enumerate(E):
        if i in S:
            continue
        d[u]+=1
        d[v]+=1
    return d

all_matchings=[]
for mask in range(1<<len(E)):
    S=[i for i in range(len(E)) if (mask>>i)&1]
    if is_matching(S):
        all_matchings.append(S)

bad_old=[S for S in all_matchings if covers_B(S) and exactly_one_B_each(S)]
corrected=[S for S in all_matchings if covers_B(S) and max(degrees_after_delete(S).values())<=2]

assert len(bad_old)==0, bad_old
assert corrected, 'No matching saturating degree-3 vertices found'

# An explicit corrected matching: one B--B edge plus two leaf edges.
Mexp=[E.index(('c','v1')),E.index(('v2','a2')),E.index(('v3','a3'))]
assert is_matching(Mexp) and covers_B(Mexp)
assert max(degrees_after_delete(Mexp).values())<=2

# Also verify an exact proper 3-edge-coloring exists and each color class covers B.
proper=[]
for cols in product(range(3), repeat=len(E)):
    ok=True
    for v in V:
        incident=[cols[i] for i,(u,w) in enumerate(E) if u==v or w==v]
        if len(incident)!=len(set(incident)):
            ok=False
            break
    if ok:
        proper.append(cols)
        break
assert proper
cols=proper[0]
for color in range(3):
    Mc=[i for i,c0 in enumerate(cols) if c0==color]
    assert is_matching(Mc)
    assert covers_B(Mc)
    assert max(degrees_after_delete(Mc).values())<=2

print('vertices=',len(V))
print('edges=',len(E))
print('degree3_vertices=',sorted(B))
print('total_matchings=',len(all_matchings))
print('old_claim_matchings_exactly_one_B_endpoint=',len(bad_old))
print('corrected_saturating_matchings=',len(corrected))
print('explicit_corrected_matching=',[E[i] for i in Mexp])
print('proper_3_edge_coloring=',list(zip(E,cols)))
print('ALL_EXACT_CHECKS_PASS')
