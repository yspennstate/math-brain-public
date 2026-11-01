#!/usr/bin/env python3
"""Exact finite checker for HARD8-01 witness-pair decomposition.

Claims checked:
  (1) Four colored witness pairs modulo S_8 x S_4 reduce to 23 unlabeled
      loopless multigraphs with four edges on eight vertices.
  (2) There are 31,465 labeled multisets of four unordered pairs; the class
      counts agree exactly with orbit-stabilizer counts from explicit
      automorphism enumeration.
  (3) In the singleton-witness, rank-7-letter architecture, a witness pattern
      admits one rank-7 escaping letter for every color iff the underlying
      four-edge multigraph is a simple forest. Exactly 8 of the 23 patterns do.
  (4) The displayed 8-state, 4-letter automaton has four distinct rank-7,
      non-idempotent letters, every ternary deletion is nonsynchronizing with
      its displayed singleton witness pair, and its exact reset threshold is 31.

All calculations use integers/bitmasks only. No randomness, floating point,
timeouts, SAT/SMT, or heuristic acceptance is used.
"""
from itertools import combinations_with_replacement, permutations, product
from collections import Counter, deque
from math import factorial
from hashlib import sha256

N = 8
EDGES = [(i,j) for i in range(N) for j in range(i+1,N)]
FULL = (1 << N) - 1


def matrix_from_comb(comb):
    m = [[0]*N for _ in range(N)]
    for idx in comb:
        a,b = EDGES[idx]
        m[a][b] += 1
        m[b][a] += 1
    return m


def degrees(m):
    return [sum(row) for row in m]


def degree_class_orders(deg):
    """All vertex orders respecting degree classes; zero vertices need no permutation."""
    out = []
    for d in sorted(set(deg), reverse=True):
        vs = [i for i,x in enumerate(deg) if x == d]
        if d == 0:
            out.append([tuple(vs)])
        else:
            out.append(permutations(vs))
    return out


def edge_code(m, order):
    return tuple(m[order[i]][order[j]] for i in range(N) for j in range(i+1,N))


def canonical_key(m):
    deg = degrees(m)
    best = None
    for pieces in product(*degree_class_orders(deg)):
        order = tuple(v for piece in pieces for v in piece)
        code = edge_code(m, order)
        if best is None or code < best:
            best = code
    return (tuple(sorted(deg, reverse=True)), best)


def automorphism_count(m):
    deg = degrees(m)
    count = 0
    classes = []
    perm_iters = []
    for d in sorted(set(deg), reverse=True):
        vs = [i for i,x in enumerate(deg) if x == d]
        classes.append(vs)
        perm_iters.append(permutations(vs))
    for pieces in product(*perm_iters):
        p = list(range(N))
        for vs, imgs in zip(classes, pieces):
            for v,img in zip(vs, imgs):
                p[v] = img
        ok = True
        for i in range(N):
            for j in range(i+1,N):
                if m[i][j] != m[p[i]][p[j]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count


def multiset_edges_from_matrix(m):
    es = []
    for i in range(N):
        for j in range(i+1,N):
            es.extend([(i,j)] * m[i][j])
    return es


def is_simple_forest(es):
    if len(set(es)) != len(es):
        return False
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a,b in es:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def enumerate_preserve_rank7(preserved, own):
    """All rank-7 transformations preserving each preserved pair setwise and escaping own."""
    pedges = list(dict.fromkeys(tuple(sorted(e)) for e in preserved))
    partials = [dict()]
    for a,b in pedges:
        new = []
        for d in partials:
            for ia,ib in ((a,b),(b,a)):
                dd = d.copy()
                ok = True
                for q,v in ((a,ia),(b,ib)):
                    if q in dd and dd[q] != v:
                        ok = False
                        break
                    dd[q] = v
                if ok:
                    new.append(dd)
        partials = new
    constrained = set()
    for e in pedges:
        constrained.update(e)
    free = [q for q in range(N) if q not in constrained]
    ans = []
    own = tuple(sorted(own))
    for d in partials:
        for vals in product(range(N), repeat=len(free)):
            t = [None]*N
            for q,v in d.items():
                t[q] = v
            for q,v in zip(free, vals):
                t[q] = v
            if len(set(t)) != N-1:
                continue
            a,b = own
            if t[a] != t[b] and tuple(sorted((t[a],t[b]))) == own:
                continue
            ans.append(tuple(t))
    return ans


def apply_subset(mask, t):
    out = 0
    while mask:
        bit = mask & -mask
        q = bit.bit_length()-1
        out |= 1 << t[q]
        mask -= bit
    return out


def subset_bfs(letters):
    """Return exact reset threshold and one shortest reset word, or (None,None)."""
    dist = [-1] * (1 << N)
    parent = [None] * (1 << N)
    dist[FULL] = 0
    dq = deque([FULL])
    while dq:
        s = dq.popleft()
        nd = dist[s] + 1
        for a,t in enumerate(letters):
            u = apply_subset(s,t)
            if dist[u] != -1:
                continue
            dist[u] = nd
            parent[u] = (s,a)
            if u & (u-1) == 0:
                word = []
                cur = u
                while cur != FULL:
                    prev, letter = parent[cur]
                    word.append(letter)
                    cur = prev
                word.reverse()
                return nd, tuple(word)
            dq.append(u)
    return None, None


def compose(t,u):
    return tuple(u[t[q]] for q in range(N))


def pair_image(p,t):
    a,b = p
    x,y = t[a], t[b]
    if x == y:
        return None
    return tuple(sorted((x,y)))


def pair_mergeable(pair, letters):
    seen = {tuple(sorted(pair))}
    dq = deque(seen)
    while dq:
        p = dq.popleft()
        for t in letters:
            u = pair_image(p,t)
            if u is None:
                return True
            if u not in seen:
                seen.add(u)
                dq.append(u)
    return False


# ---------------------------------------------------------------------------
# 1. Witness-pattern orbit census.
# ---------------------------------------------------------------------------
classes = {}
class_counts = Counter()
for comb in combinations_with_replacement(range(len(EDGES)), 4):
    m = matrix_from_comb(comb)
    k = canonical_key(m)
    class_counts[k] += 1
    if k not in classes:
        classes[k] = m

assert sum(class_counts.values()) == 31465
assert len(classes) == 23
assert 31465 == (31*30*29*28)//24  # C(28+4-1,4) = C(31,4)

orbit_rows = []
for k,m in classes.items():
    aut = automorphism_count(m)
    orbit = factorial(N)//aut
    observed = class_counts[k]
    assert orbit == observed
    es = multiset_edges_from_matrix(m)
    orbit_rows.append((k, es, aut, orbit, is_simple_forest(es)))
assert sum(row[3] for row in orbit_rows) == 31465

# Stable ordering for printed representatives.
orbit_rows.sort(key=lambda row: row[0])

# ---------------------------------------------------------------------------
# 2. Singleton-witness rank-7 feasibility.
# ---------------------------------------------------------------------------
feasible = []
for idx,(_,es,aut,orbit,forest) in enumerate(orbit_rows):
    pool_sizes = []
    for j in range(4):
        pool = enumerate_preserve_rank7([es[i] for i in range(4) if i != j], es[j])
        pool_sizes.append(len(pool))
    ok = all(s > 0 for s in pool_sizes)
    assert ok == forest
    if ok:
        feasible.append((idx, es, tuple(pool_sizes)))
assert len(feasible) == 8

# ---------------------------------------------------------------------------
# 3. Exact counterexample-oriented test candidate for the architecture.
# ---------------------------------------------------------------------------
WITNESSES = ((0,1),(0,2),(1,3),(4,5))
LETTERS = (
    (2,3,0,1,5,4,4,7),
    (0,1,7,3,4,5,2,2),
    (0,1,2,7,4,5,3,3),
    (0,1,2,3,7,6,4,4),
)
assert len(set(LETTERS)) == 4
for t in LETTERS:
    assert len(set(t)) == 7
    assert compose(t,t) != t

# The displayed witness multigraph is a simple forest and belongs to the census.
wm = [[0]*N for _ in range(N)]
for a,b in WITNESSES:
    wm[a][b] += 1; wm[b][a] += 1
assert canonical_key(wm) in classes
assert is_simple_forest(list(WITNESSES))

# Every deletion is nonsynchronizing for two independently checked reasons:
# (i) its designated witness pair is preserved setwise by each remaining letter;
# (ii) exact pair-BFS cannot merge that witness.
for i,p in enumerate(WITNESSES):
    remaining = tuple(LETTERS[j] for j in range(4) if j != i)
    for j,t in enumerate(LETTERS):
        if j == i:
            continue
        assert pair_image(p,t) == tuple(sorted(p))
    assert not pair_mergeable(p, remaining)
    d,w = subset_bfs(remaining)
    assert d is None and w is None

rt, word = subset_bfs(LETTERS)
assert rt == 31
assert len(word) == 31
# Replay the word to a singleton.
s = FULL
for a in word:
    s = apply_subset(s, LETTERS[a])
assert s & (s-1) == 0

serialization = "W=" + repr(WITNESSES) + "\nL=" + repr(LETTERS) + "\nword=" + repr(word) + "\n"
digest = sha256(serialization.encode()).hexdigest()

print("HARD8_01_WITNESS_RANK7_EXACT")
print("N", N)
print("LABELED_WITNESS_MULTISETS", 31465)
print("WITNESS_ORBITS_S8xS4", len(classes))
print("ORBIT_STABILIZER_SUM", sum(row[3] for row in orbit_rows))
print("SIMPLE_FOREST_ORBITS", sum(1 for row in orbit_rows if row[4]))
print("SINGLETON_RANK7_FEASIBLE_ORBITS", len(feasible))
print("FEASIBLE_IFF_SIMPLE_FOREST", "PASS")
print("FEASIBLE_PATTERNS")
for idx,es,sizes in feasible:
    print(idx, es, sizes)
print("CANDIDATE_WITNESSES", WITNESSES)
for i,t in enumerate(LETTERS):
    print("LETTER", i, t)
print("CANDIDATE_ALL_LETTERS_RANK", 7)
print("CANDIDATE_ALL_LETTERS_NONIDEMPOTENT", "PASS")
print("CANDIDATE_ALL_TERNARY_DELETIONS_NONSYNC", "PASS")
print("CANDIDATE_RESET_THRESHOLD", rt)
print("CANDIDATE_SHORTEST_RESET_WORD", word)
print("CANDIDATE_SHA256", digest)
print("ALL_EXACT_CHECKS_PASSED")
