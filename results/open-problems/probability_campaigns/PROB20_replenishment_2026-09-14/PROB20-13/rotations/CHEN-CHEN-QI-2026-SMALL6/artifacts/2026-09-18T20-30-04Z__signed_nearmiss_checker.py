from itertools import combinations
from collections import defaultdict, deque

class DSU:
    def __init__(self, xs):
        self.p = {x:x for x in xs}
        self.r = {x:0 for x in xs}
    def find(self, x):
        p = self.p[x]
        if p != x:
            self.p[x] = self.find(p)
        return self.p[x]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True

def c4_free(e1, m, n):
    s = set(e1)
    for r1, r2 in combinations(range(1,m+1), 2):
        common = sum(((r1,c) in s and (r2,c) in s) for c in range(1,n+1))
        if common >= 2:
            return False
    return True

def signed_deviation(m, n, e1, e2):
    e1 = [tuple(x) for x in e1]
    e2 = [(tuple(a), tuple(b)) for a,b in e2]
    occupied = set(e1)
    for a,b in e2:
        if a in occupied or b in occupied or a == b:
            raise AssertionError("not simple")
        occupied.add(a); occupied.add(b)

    dsu = DSU(occupied)
    for a,b in e2:
        if a[0] == b[0] or a[1] == b[1]:
            dsu.union(a,b)

    def build():
        roots = sorted({dsu.find(x) for x in occupied})
        members = defaultdict(list)
        for x in occupied:
            members[dsu.find(x)].append(x)

        nodes = {}
        pairroots = []
        for a,b in combinations(roots, 2):
            nodes[frozenset((a,b))] = len(pairroots)
            pairroots.append((a,b))

        adj = [[] for _ in pairroots]
        ground = set()
        ineq = set()

        for k,(ra,rb) in enumerate(pairroots):
            if any(x[0] == y[0] or x[1] == y[1]
                   for x in members[ra] for y in members[rb]):
                ground.add(k)

        unresolved = []
        for a,b in e2:
            ra, rb = dsu.find(a), dsu.find(b)
            if ra == rb:
                continue
            k = nodes[frozenset((ra,rb))]
            unresolved.append((a,b,k))
            ineq.add(k)

        def diag_node(p,q):
            if p not in occupied or q not in occupied:
                return None
            rp, rq = dsu.find(p), dsu.find(q)
            if rp == rq:
                return None
            return nodes[frozenset((rp,rq))]

        for i,k in combinations(range(1,m+1), 2):
            for j,l in combinations(range(1,n+1), 2):
                a = diag_node((i,j),(k,l))
                b = diag_node((i,l),(k,j))
                if a is None and b is None:
                    continue
                if a is None:
                    ground.add(b)
                elif b is None:
                    ground.add(a)
                elif a == b:
                    ground.add(a)
                else:
                    adj[a].append(b)
                    adj[b].append(a)

        parity = {}
        forced = set()
        comps = []
        for start in range(len(pairroots)):
            if start in parity:
                continue
            parity[start] = 0
            q = deque([start])
            comp = []
            odd = False
            while q:
                v = q.popleft()
                comp.append(v)
                for w in adj[v]:
                    want = parity[v] ^ 1
                    if w not in parity:
                        parity[w] = want
                        q.append(w)
                    elif parity[w] != want:
                        odd = True
            grounded = any(v in ground for v in comp)
            ineq_parities = {parity[v] for v in comp if v in ineq}
            both = (0 in ineq_parities and 1 in ineq_parities)
            if odd or grounded or both:
                forced.update(comp)
            comps.append((comp, odd, grounded, both))
        return roots, pairroots, forced, unresolved, comps

    history = []
    rounds = 0
    while True:
        rounds += 1
        roots, pairs, forced, unresolved, comps = build()
        free = [c for c in comps if not (c[1] or c[2] or c[3])]
        history.append((len(roots), len(unresolved), len(pairs),
                        len(forced), len(free),
                        tuple(sorted(len(c[0]) for c in free))))
        changed = False
        for a,b,k in unresolved:
            if k in forced:
                changed |= dsu.union(a,b)
        if not changed:
            break
        if rounds > len(e2) + 2:
            raise AssertionError("closure loop")

    allresolved = all(dsu.find(a) == dsu.find(b) for a,b in e2)
    roots, pairs, forced, unresolved, comps = build()
    free = [c for c in comps if not (c[1] or c[2] or c[3])]
    return {
        "all_e2_resolved": allresolved,
        "roots": len(roots),
        "nodes": len(pairs),
        "forced": len(forced),
        "free_components": len(free),
        "free_sizes": tuple(sorted(len(c[0]) for c in free)),
        "accepted": allresolved and len(forced) == len(pairs),
        "rounds": rounds,
        "unresolved_e2": len(unresolved),
        "history": tuple(history),
    }

E1 = [
    (1,1),(1,2),(1,3),
    (2,1),(2,4),(2,5),
    (3,2),(3,4),(3,6),
    (4,3),(4,5),(4,6),
    (5,1),(5,6),
    (6,2),(6,5),
]
assert len(E1) == 16
assert c4_free(E1,6,6)

SOURCE_E1 = [
    (1,1),(1,2),
    (2,3),(2,4),
    (3,1),(3,3),(3,5),
    (4,2),(4,4),(4,5),
    (5,2),(5,3),(5,6),
    (6,1),(6,4),(6,6),
]
SOURCE_E2 = [
    ((1,4),(6,5)),
    ((1,5),(2,2)),
    ((3,6),(6,2)),
    ((2,6),(4,3)),
    ((1,6),(2,5)),
    ((3,4),(5,1)),
    ((1,3),(4,1)),
    ((5,5),(6,3)),
]
SOURCE_HOLES = [(2,1),(3,2),(4,6),(5,4)]
assert len(SOURCE_E1) + len(SOURCE_E2) == 24
assert len(SOURCE_E1) + 2*len(SOURCE_E2) + len(SOURCE_HOLES) == 36
source = signed_deviation(6,6,SOURCE_E1,SOURCE_E2)
assert source["accepted"]
assert source["roots"] == 24
assert source["nodes"] == 276
assert source["forced"] == 276
assert source["free_components"] == 0

ext = []
for a,b in combinations(SOURCE_HOLES,2):
    r = signed_deviation(6,6,SOURCE_E1,SOURCE_E2+[(a,b)])
    ext.append((a,b,r["accepted"],r["all_e2_resolved"],
                r["unresolved_e2"],r["forced"],r["nodes"]))
assert len(ext) == 6
assert sum(int(x[2]) for x in ext) == 0

NEAR_E2 = [
    ((1,4),(4,1)),
    ((1,5),(5,5)),
    ((1,6),(2,2)),
    ((2,3),(3,1)),
    ((3,3),(6,6)),
    ((3,5),(6,1)),
    ((4,2),(5,3)),
    ((4,4),(6,4)),
    ((5,2),(5,4)),
]
NEAR_HOLES = [(2,6),(6,3)]
assert len(E1) + len(NEAR_E2) == 25
assert len(E1) + 2*len(NEAR_E2) + len(NEAR_HOLES) == 36
near = signed_deviation(6,6,E1,NEAR_E2)
assert near["all_e2_resolved"]
assert near["roots"] == 25
assert near["nodes"] == 300
assert near["forced"] == 287
assert near["free_components"] == 4
assert near["free_sizes"] == (3,3,3,4)
assert not near["accepted"]
compact_history = tuple((x[0],x[1],x[3],x[4]) for x in near["history"])
assert compact_history == (
    (31,6,198,110),
    (28,3,241,49),
    (27,2,259,30),
    (26,1,283,15),
    (25,0,287,4),
)

print("SOURCE_N24 accepted=%s roots=%d nodes=%d forced=%d free_components=%d" %
      (source["accepted"],source["roots"],source["nodes"],source["forced"],source["free_components"]))
print("SOURCE_N24_ONE_EDGE_EXTENSIONS tested=%d accepted=%d" %
      (len(ext),sum(int(x[2]) for x in ext)))
for a,b,accepted,resolved,unres,forced,nodes in ext:
    print("  extension=%s--%s accepted=%s all_e2_resolved=%s unresolved_e2=%d forced=%d/%d" %
          (a,b,accepted,resolved,unres,forced,nodes))
print("NEAR_N25 holes=%s all_e2_resolved=%s roots=%d nodes=%d forced=%d free_components=%d free_sizes=%s accepted=%s" %
      (NEAR_HOLES,near["all_e2_resolved"],near["roots"],near["nodes"],near["forced"],
       near["free_components"],near["free_sizes"],near["accepted"]))
print("NEAR_N25_COMPACT_HISTORY=%s" % (compact_history,))
print("ALL_EXACT_CHECKS_PASS")
