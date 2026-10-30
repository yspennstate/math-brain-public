#!/usr/bin/env python3
import itertools, json
V=tuple(range(17))
ARCS=set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 14), (1, 2), (1, 3), (1, 5), (1, 6), (1, 10), (1, 11), (1, 15), (2, 3), (2, 5), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (3, 5), (3, 6), (3, 8), (3, 10), (3, 12), (3, 13), (3, 14), (4, 1), (4, 2), (4, 3), (4, 5), (4, 10), (4, 12), (4, 15), (5, 0), (5, 6), (5, 8), (5, 10), (5, 11), (5, 12), (5, 16), (6, 0), (6, 2), (6, 4), (6, 7), (6, 11), (6, 14), (6, 16), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 13), (8, 1), (8, 4), (8, 6), (8, 7), (8, 9), (8, 13), (8, 16), (9, 1), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 10), (10, 0), (10, 6), (10, 7), (10, 8), (10, 11), (10, 12), (10, 15), (11, 0), (11, 3), (11, 4), (11, 7), (11, 8), (11, 9), (11, 12), (12, 1), (12, 6), (12, 7), (12, 8), (12, 9), (12, 13), (12, 15), (13, 0), (13, 1), (13, 2), (13, 4), (13, 5), (13, 6), (13, 9), (13, 10), (13, 11), (13, 14), (14, 1), (14, 2), (14, 4), (14, 5), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 15), (15, 0), (15, 2), (15, 3), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 11), (15, 13), (15, 16), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 7), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14)])
q=0
R=(0,1,2,3)
S=(4,5,6,7)
TWO=(8,9,10,11)
ONE=(12,13,14,15,16)
bmm,bm,b=12,13,14

def cyc(C):
    return all((C[i], C[(i+1)%len(C)]) in ARCS for i in range(len(C)))

def strong(vertices):
    vertices=set(vertices)
    if len(vertices)<=1: return True
    s=next(iter(vertices))
    def reach(reverse=False):
        seen={s}; stack=[s]
        while stack:
            x=stack.pop()
            for a,c in ARCS:
                u,v=(c,a) if reverse else (a,c)
                if u==x and v in vertices and v not in seen:
                    seen.add(v); stack.append(v)
        return seen
    return reach()==vertices and reach(True)==vertices

assert all(a!=c for a,c in ARCS)
assert all(not ((c,a) in ARCS) for a,c in ARCS)
missing=[(i,j) for i in V for j in V if i<j and (i,j) not in ARCS and (j,i) not in ARCS]
assert missing==[(0,12)]
deg={v:sum(a==v for a,c in ARCS) for v in V}
assert min(deg.values())==7
assert max(deg.values())==12
assert cyc(S) and cyc(TWO) and cyc(ONE)
assert set(c for a,c in ARCS if a==q and c in R)=={1,2,3}
assert set(c for a,c in ARCS if a==q and c in S)=={4}
assert set(c for a,c in ARCS if a==q and c in TWO)=={8,9}
assert set(c for a,c in ARCS if a==q and c in ONE)=={14}
assert (bm,q) in ARCS and (q,b) in ARCS
assert (q,bmm) not in ARCS and (bmm,q) not in ARCS
# Redirected neutral pivot on support cycle: c=4, c^-=7, c^--=6.
assert (7,q) in ARCS and (6,q) in ARCS and (q,4) in ARCS
SUPPORT_PIVOT=(6,0,4,5)
assert cyc(SUPPORT_PIVOT)
# R is transitively acyclic 0>1>2>3 in the chosen local profile.
assert all((i,j) in ARCS for i,j in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
# Dense local adversary also survives deletion of any <=2 vertices.
for k in range(3):
    for D in itertools.combinations(V,k):
        assert strong(set(V)-set(D))
fourpack=((0,1,5),(2,3,6),(4,10,7),(8,13,11))
assert all(cyc(C) for C in fourpack)
assert len(set().union(*map(set,fourpack)))==12
# The displayed packed 4/4/5 cycles are deliberately not globally minimum:
triple=((0,1,5),(2,3,6),(4,10,7))
assert all(cyc(C) for C in triple)

# Exact digon threshold adversary: bidirected K8 has delta+=7; delete
# the two vertices of any chosen digon and the surviving delta+ is exactly 5.
W=range(8)
K8={(i,j) for i in W for j in W if i!=j}
d0={i:sum(a==i for a,c in K8) for i in W}
surv=set(W)-{0,1}
K6={(a,c) for a,c in K8 if a in surv and c in surv}
d1={i:sum(a==i for a,c in K6) for i in surv}
assert min(d0.values())==7 and min(d1.values())==5

out={
  "status":"PASS",
  "oriented_adversary":{
    "vertices":17,
    "arcs":len(ARCS),
    "missing_unordered_pairs":missing,
    "min_outdegree":min(deg.values()),
    "max_outdegree":max(deg.values()),
    "outdegree_vector":[deg[v] for v in V],
    "three_vertex_strong":True,
    "q_profile":{
      "R_out":[1,2,3],"support_out":[4],"two_fan":[8,9],"one_fan":[14],
      "wedge":[13,0,14],"predecessor_two":12,"q_pred2_nonedge":True
    },
    "packed_cycles":[list(S),list(TWO),list(ONE)],
    "support_redirect_pivot":[6,0,4,5],
    "support_redirect_frees":7,
    "explicit_four_pack":[list(x) for x in fourpack],
    "global_minimum_packing_assumption":False
  },
  "digon_threshold_adversary":{
    "graph":"complete_bidirected_K8",
    "min_outdegree_before":7,
    "delete_digon_vertices":[0,1],
    "min_outdegree_after":5
  }
}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
