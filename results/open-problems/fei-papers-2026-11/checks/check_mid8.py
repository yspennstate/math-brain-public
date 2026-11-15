import sys, json
from fractions import Fraction as F
from itertools import combinations
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles"
sys.path.insert(0, R + "/engine")
import tk_core
from tk_core import all_pairings, canonical
from exact_volume import volume_from_halfspaces, pairing_volume_exact

# ---------- volume lookup from orbit tables (volume is dihedral invariant)
VOL = {}
for n in (4, 6, 8, 10):
    d = json.load(open(f"{R}/data/volumes_T{n}.json"))
    VOL[n] = {tuple(json.loads(k)): F(v["volume"]) for k, v in d["orbits"].items()}
def vol(pm):
    n = len(pm)
    if n == 0:
        return F(1)
    if n == 2:
        return F(1)
    return VOL[n][tuple(canonical(pm))]

def pm_of(word):
    pos = {}
    for i, ch in enumerate(word):
        pos.setdefault(ch, []).append(i)
    pm = [None] * len(word)
    for a, b in pos.values():
        pm[a], pm[b] = b, a
    return tuple(pm)

# ---------- 1. profile at x = 1/2, cluster equation
def profile_half(pm):
    rows = tk_core.dedupe_rows(tk_core.toeplitz_forms(pm))
    k = len(pm) // 2
    hs = []
    for r in rows:
        a = tuple(r[1:]); c = F(r[0], 2)  # x0 = 1/2
        if not any(a):
            continue
        hs.append((a, c)); hs.append((tuple(-v for v in a), 1 - c))
    return volume_from_halfspaces(hs, [(-1, 1)] * k)

def is_concat(pm):
    n = len(pm)
    for c in range(2, n, 2):
        if all((pm[i] < c) == (i < c) for i in range(n)):
            return True
    return False
def is_nest(pm):
    return pm[0] == len(pm) - 1

Fk, Jd = [F(1)], [F(0)]
for k in range(1, 5):
    fs = []; jj = F(0)
    for pm in all_pairings(2 * k):
        f = profile_half(pm); fs.append(f)
        if not is_concat(pm) and not is_nest(pm):
            jj += f
    Fk.append(sum(fs, F(0))); Jd.append(jj)
print("F_k(1/2)", [str(x) for x in Fk], "want 1,1,11/4,47/4,12823/192")
M = [F(1), F(1), F(8, 3), F(11), F(908, 15)]
# 1/F series
inv = [F(1)]
for n in range(1, 5):
    inv.append(-sum(Fk[j] * inv[n - j] for j in range(1, n + 1)))
J = [ (1 if n == 0 else 0) - (M[n - 1] if n >= 1 else 0) - inv[n] for n in range(5)]
print("J by inversion", [str(x) for x in J[1:]], "direct", [str(x) for x in Jd[1:]], "want 0,3/4,55/12,6139/192")

# ---------- 2. three words with one cycle block
for w in ("abcdabcd", "abacbdcd", "abcadbcd"):
    print(w, vol(pm_of(w)))

# ---------- 3. coarse invariants at order 8
def height(pm):
    h, out = 0, []
    for i in range(len(pm)):
        h += 1 if pm[i] > i else -1
        out.append(h)
    return tuple(out)
def chords(pm):
    return [(i, pm[i]) for i in range(len(pm)) if i < pm[i]]
def ncross(pm):
    c = chords(pm)
    return sum(1 for (a, b), (x, y) in combinations(c, 2) if a < x < b < y or x < a < y < b)
def nnest(pm):
    c = chords(pm)
    return sum(1 for (a, b), (x, y) in combinations(c, 2) if a < x < y < b or x < a < b < y)
def classes(n, key):
    cl = {}
    for pm in all_pairings(n):
        cl.setdefault(key(pm), set()).add(vol(pm))
    return cl
P8 = list(all_pairings(8))
print("order 8 distinct volumes", sorted(set(vol(p) for p in P8)))
hc = classes(8, height)
print("height: classes", len(hc), "impure", sum(len(v) > 1 for v in hc.values()), "(1,2,1,0,1,2,1,0)->", sorted(hc[(1, 2, 1, 0, 1, 2, 1, 0)]))
cc = classes(8, ncross)
print("crossings:", {k: sorted(map(str, v)) for k, v in sorted(cc.items())})
nc = classes(8, nnest)
print("nestings: classes", len(nc), "impure", sum(len(v) > 1 for v in nc.values()), "nest0", sorted(map(str, nc[0])))
cn = classes(8, lambda p: (ncross(p), nnest(p)))
print("(cross,nest): classes", len(cn), "impure", sum(len(v) > 1 for v in cn.values()))
print("height abacbdcd", height(pm_of("abacbdcd")), "abcadbcd", height(pm_of("abcadbcd")))

# ---------- 4. interlacement graph classes through order 10
import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash as wl
def cgraph(pm):
    c = chords(pm); G = nx.Graph(); G.add_nodes_from(range(len(c)))
    for i, j in combinations(range(len(c)), 2):
        (a, b), (x, y) = c[i], c[j]
        if a < x < b < y or x < a < y < b:
            G.add_edge(i, j)
    return G
tot_conn = tot_disc = 0
for n in (6, 8, 10):
    reps = []  # (graph, set of volumes)
    for pm in all_pairings(n):
        G = cgraph(pm); v = vol(pm)
        for rep in reps:
            if nx.is_isomorphic(rep[0], G):
                rep[1].add(v); break
        else:
            reps.append([G, {v}])
    conn = [r for r in reps if nx.is_connected(r[0])]
    disc = [r for r in reps if not nx.is_connected(r[0])]
    tot_conn += len(conn); tot_disc += len(disc)
    imp = [(sorted(d for _, d in r[0].degree()), sorted(map(str, r[1]))) for r in reps if len(r[1]) > 1]
    print(f"order {n}: classes {len(reps)} connected {len(conn)} (impure {sum(len(r[1])>1 for r in conn)}) disconnected {len(disc)} (impure {sum(len(r[1])>1 for r in disc)}) impure:", imp)
print("totals connected", tot_conn, "disconnected", tot_disc)
for w in ("aabcbcdede", "ababcdedec"):
    print(w, vol(pm_of(w)))
