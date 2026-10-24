from itertools import combinations

def components_count(n, edges):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for u,v in edges:
        ru,rv = find(u),find(v)
        if ru != rv:
            parent[rv] = ru
    return len({find(i) for i in range(n)})

def is_forest(n, edges, subset):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for idx in subset:
        u,v = edges[idx]
        ru,rv = find(u),find(v)
        if ru == rv:
            return False
        parent[rv] = ru
    return True

def bases(n, edges):
    rank = n - components_count(n, edges)
    return [frozenset(s) for s in combinations(range(len(edges)), rank)
            if is_forest(n, edges, s)]

def internal_activity(B, base_set):
    active = set()
    for b in B:
        if all(x in B or frozenset((set(B)-{b})|{x}) not in base_set
               for x in range(b)):
            active.add(b)
    return frozenset(active)

def direct_counts(n, edges):
    Z = Ze = Zf = Zef = 0
    m = len(edges)
    for r in range(m+1):
        for s in combinations(range(m), r):
            if not is_forest(n, edges, s):
                continue
            Z += 1
            a = 0 in s
            b = 1 in s
            Ze += int(a)
            Zf += int(b)
            Zef += int(a and b)
    return Z,Ze,Zf,Zef

def activity_counts(n, edges):
    Bs = bases(n, edges)
    base_set = set(Bs)
    W = {(0,0):0,(1,0):0,(0,1):0,(1,1):0}
    Q = 0
    for B in Bs:
        IA = internal_activity(B, base_set)
        w = 1 << len(IA)
        W[(int(0 in B),int(1 in B))] += w
        if 1 in B and 0 not in B:
            if frozenset((set(B)-{1})|{0}) in base_set:
                Q += w
    return W,Q

graphs = pairs = 0
for n in range(2,6):
    universe = list(combinations(range(n),2))
    for mask in range(1 << len(universe)):
        E = [universe[i] for i in range(len(universe)) if (mask >> i) & 1]
        if len(E) < 2:
            continue
        graphs += 1
        for ei,fi in combinations(range(len(E)),2):
            edges = [E[ei],E[fi]] + [g for j,g in enumerate(E) if j not in (ei,fi)]
            Z,Ze,Zf,Zef = direct_counts(n, edges)
            W,Q = activity_counts(n, edges)
            assert sum(W.values()) == Z
            assert W[(1,0)] + W[(1,1)] == 2*Ze
            assert W[(0,1)] + W[(1,1)] + Q == 2*Zf
            assert W[(1,1)] == 4*Zef
            rhs = (W[(1,0)]*W[(0,1)]
                   - W[(0,0)]*W[(1,1)]
                   + Q*(W[(1,0)] + W[(1,1)]))
            assert rhs == 4*(Ze*Zf - Z*Zef)
            pairs += 1

# K5, disjoint marked edges e=01, f=23.
n = 5
all_edges = list(combinations(range(n),2))
marked = [(0,1),(2,3)]
edges = marked + [g for g in all_edges if g not in marked]
Z,Ze,Zf,Zef = direct_counts(n, edges)
W,Q = activity_counts(n, edges)
gap = Ze*Zf - Z*Zef

print("ACTIVITY_UNROOTING_EXHAUSTIVE_PASS")
print("graphs_n2_to_n5_with_at_least_two_edges =", graphs)
print("marked_pairs_checked =", pairs)
print("K5_disjoint: Z,Ze,Zf,Zef =", (Z,Ze,Zf,Zef))
print("K5_disjoint: W00,W10,W01,W11,Q =",
      (W[(0,0)],W[(1,0)],W[(0,1)],W[(1,1)],Q))
print("K5_disjoint: 4*Delta =", 4*gap, "Delta =", gap)
print("ACTIVITY_TWO_CHANNEL_IDENTITY_PASS")
