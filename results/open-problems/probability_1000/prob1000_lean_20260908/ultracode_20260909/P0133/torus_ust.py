# P0133 / Schramm Problem 6.2: the triple of homotopy classes of the dual
# complement of the UST on an n x m torus grid.
# Exact enumeration (small tori) and Wilson-algorithm Monte Carlo (large tori).
import numpy as np, sys, time, json
from numba import njit

# vertex index = y*n + x ; 0 <= x < n (width), 0 <= y < m (height)
# direction d: 0 right (+x), 1 left (-x), 2 up (+y), 3 down (-y)

@njit(cache=True)
def wilson(n, m, seed):
    np.random.seed(seed)
    N = n*m
    intree = np.zeros(N, np.bool_)
    nxt = np.full(N, -1, np.int64)
    dr = np.full(N, -1, np.int64)
    intree[0] = True
    for i in range(N):
        u = i
        while not intree[u]:
            r = np.random.randint(4)
            x = u % n; y = u // n
            if r == 0: v = y*n + (x+1) % n
            elif r == 1: v = y*n + (x-1+n) % n
            elif r == 2: v = ((y+1) % m)*n + x
            else: v = ((y-1+m) % m)*n + x
            nxt[u] = v; dr[u] = r
            u = v
        u = i
        while not intree[u]:
            intree[u] = True
            u = nxt[u]
    return nxt, dr

@njit(cache=True)
def step(d):
    if d == 0: return 1, 0
    if d == 1: return -1, 0
    if d == 2: return 0, 1
    return 0, -1

@njit(cache=True)
def displacements(n, m, nxt, dr):
    # X[v], Y[v]: which fundamental domain the lift of v (in the tree copy through vertex 0) lies in
    N = n*m
    X = np.zeros(N, np.int64); Y = np.zeros(N, np.int64)
    known = np.zeros(N, np.bool_); known[0] = True
    stack = np.empty(N, np.int64)
    for i in range(N):
        if known[i]: continue
        k = 0; u = i
        while not known[u]:
            stack[k] = u; k += 1
            u = nxt[u]
        while k > 0:
            k -= 1; u = stack[k]; p = nxt[u]
            sx, sy = step(dr[u])
            # lift(p) = lift(u) + step  =>  X[p] = X[u] + (x_u + sx - x_p)/n
            X[u] = X[p] - ((u % n) + sx - (p % n)) // n
            Y[u] = Y[p] - ((u // n) + sy - (p // n)) // m
            known[u] = True
    return X, Y

@njit(cache=True)
def triple_from_tree(n, m, nxt, dr, X, Y):
    # returns (k, cls): the set of nonzero fundamental-cycle classes of non-tree edges (up to sign)
    N = n*m
    cls = np.zeros((3, 2), np.int64); k = 0
    for u in range(N):
        for d in range(0, 4, 2):   # right and up: each undirected edge once
            x = u % n; y = u // n
            if d == 0: v = y*n + (x+1) % n
            else: v = ((y+1) % m)*n + x
            if (nxt[u] == v and dr[u] == d) or (nxt[v] == u and dr[v] == d+1):
                continue   # tree edge
            sx, sy = step(d)
            cx = X[u] - X[v] + ((u % n) + sx - (v % n)) // n
            cy = Y[u] - Y[v] + ((u // n) + sy - (v // n)) // m
            if cx == 0 and cy == 0: continue
            if cx < 0 or (cx == 0 and cy < 0): cx = -cx; cy = -cy
            found = False
            for j in range(k):
                if cls[j, 0] == cx and cls[j, 1] == cy: found = True
            if not found:
                if k == 3: return -1, cls
                cls[k, 0] = cx; cls[k, 1] = cy; k += 1
    return k, cls

@njit(cache=True)
def mc(n, m, nsamp, seed, out):
    for s in range(nsamp):
        nxt, dr = wilson(n, m, seed + s)
        X, Y = displacements(n, m, nxt, dr)
        k, cls = triple_from_tree(n, m, nxt, dr, X, Y)
        out[s, 0] = k
        for j in range(3):
            out[s, 1+2*j] = cls[j, 0]; out[s, 2+2*j] = cls[j, 1]

def canon(k, cls):
    L = sorted([tuple(int(t) for t in cls[j]) for j in range(k)])
    return tuple(L)

def check_unimodular(k, cls):
    # theta case: three classes a,b,c with c = +-a +-b and |det(a,b)|=1 ; figure-eight: two classes with |det|=1
    if k == 2:
        a, b = cls[0], cls[1]
        return abs(a[0]*b[1]-a[1]*b[0]) == 1
    if k == 3:
        a, b, c = cls
        if abs(a[0]*b[1]-a[1]*b[0]) != 1: return False
        for s in (1, -1):
            for t in (1, -1):
                if (c[0] == s*a[0]+t*b[0]) and (c[1] == s*a[1]+t*b[1]): return True
        return False
    return False

def run_mc(n, m, nsamp, seed=12345):
    out = np.zeros((nsamp, 7), np.int64)
    t = time.time()
    mc(n, m, nsamp, seed, out)
    dt = time.time() - t
    counts = {}
    bad = 0
    for s in range(nsamp):
        k = int(out[s, 0])
        cls = [(int(out[s, 1+2*j]), int(out[s, 2+2*j])) for j in range(3)][:max(k, 0)]
        if k < 0 or not check_unimodular(k, cls):
            bad += 1; continue
        key = canon(k, cls)
        counts[key] = counts.get(key, 0) + 1
    return counts, bad, dt

# ---------- exact enumeration by edge subsets (small tori) ----------
@njit(cache=True)
def exact(n, m, tally, keys, maxkeys):
    N = n*m; E = 2*N
    eu = np.empty(E, np.int64); ev = np.empty(E, np.int64); ed = np.empty(E, np.int64)
    for u in range(N):
        x = u % n; y = u // n
        eu[2*u] = u; ev[2*u] = y*n + (x+1) % n; ed[2*u] = 0
        eu[2*u+1] = u; ev[2*u+1] = ((y+1) % m)*n + x; ed[2*u+1] = 2
    ntrees = 0; nkeys = 0
    parent = np.empty(N, np.int64)
    nxt = np.empty(N, np.int64); dr = np.empty(N, np.int64)
    adj = np.empty((N, 4), np.int64); adjd = np.empty((N, 4), np.int64); deg = np.empty(N, np.int64)
    queue = np.empty(N, np.int64)
    seen = np.empty(N, np.bool_)
    mask = (1 << (N-1)) - 1
    top = 1 << E
    while mask < top:
        for i in range(N): parent[i] = i
        ok = True
        for e in range(E):
            if (mask >> e) & 1:
                a = eu[e]
                while parent[a] != a: a = parent[a]
                b = ev[e]
                while parent[b] != b: b = parent[b]
                if a == b:
                    ok = False; break
                parent[a] = b
        if ok:
            ntrees += 1
            for i in range(N): deg[i] = 0
            for e in range(E):
                if (mask >> e) & 1:
                    a = eu[e]; b = ev[e]
                    adj[a, deg[a]] = b; adjd[a, deg[a]] = ed[e]; deg[a] += 1
                    adj[b, deg[b]] = a; adjd[b, deg[b]] = ed[e] + 1; deg[b] += 1
            for i in range(N): seen[i] = False
            seen[0] = True; nxt[0] = -1; dr[0] = -1
            qh = 0; qt = 0; queue[qt] = 0; qt += 1
            while qh < qt:
                a = queue[qh]; qh += 1
                for j in range(deg[a]):
                    b = adj[a, j]
                    if not seen[b]:
                        seen[b] = True
                        nxt[b] = a; dr[b] = adjd[a, j] ^ 1   # direction from b to a
                        queue[qt] = b; qt += 1
            X, Y = displacements(n, m, nxt, dr)
            k, cls = triple_from_tree(n, m, nxt, dr, X, Y)
            for i in range(k):
                for j in range(i+1, k):
                    if (cls[j, 0] < cls[i, 0]) or (cls[j, 0] == cls[i, 0] and cls[j, 1] < cls[i, 1]):
                        t0 = cls[i, 0]; t1 = cls[i, 1]
                        cls[i, 0] = cls[j, 0]; cls[i, 1] = cls[j, 1]
                        cls[j, 0] = t0; cls[j, 1] = t1
            found = -1
            for q in range(nkeys):
                if keys[q, 0] == k:
                    same = True
                    for i in range(k):
                        if keys[q, 1+2*i] != cls[i, 0] or keys[q, 2+2*i] != cls[i, 1]: same = False
                    if same:
                        found = q; break
            if found < 0:
                found = nkeys
                keys[nkeys, 0] = k
                for i in range(3):
                    keys[nkeys, 1+2*i] = cls[i, 0] if i < k else 0
                    keys[nkeys, 2+2*i] = cls[i, 1] if i < k else 0
                nkeys += 1
            tally[found] += 1
        c = mask & -mask
        r = mask + c
        mask = (((r ^ mask) >> 2) // c) | r
    return ntrees, nkeys

def run_exact(n, m, maxkeys=2000):
    tally = np.zeros(maxkeys, np.int64); keys = np.zeros((maxkeys, 7), np.int64)
    t = time.time()
    ntrees, nkeys = exact(n, m, tally, keys, maxkeys)
    dt = time.time() - t
    counts = {}
    for q in range(nkeys):
        k = int(keys[q, 0])
        cls = [(int(keys[q, 1+2*i]), int(keys[q, 2+2*i])) for i in range(k)]
        assert check_unimodular(k, cls), (k, cls)
        counts[canon(k, cls)] = int(tally[q])
    return ntrees, counts, dt

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "exact":
        n, m = int(sys.argv[2]), int(sys.argv[3])
        ntrees, counts, dt = run_exact(n, m)
        print(f"exact {n}x{m}: trees={ntrees} time={dt:.1f}s")
        for key, c in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"  {key}: {c}  ({c/ntrees:.6f})")
        json.dump({"n": n, "m": m, "ntrees": ntrees, "counts": {str(k): c for k, c in counts.items()}},
                  open(f"exact_{n}x{m}.json", "w", encoding="utf-8"), indent=1)
    else:
        n, m, nsamp = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        seed = int(sys.argv[5]) if len(sys.argv) > 5 else 12345
        counts, bad, dt = run_mc(n, m, nsamp, seed)
        print(f"mc {n}x{m}: samples={nsamp} bad={bad} time={dt:.1f}s")
        for key, c in sorted(counts.items(), key=lambda kv: -kv[1])[:25]:
            print(f"  {key}: {c}  ({c/nsamp:.5f} +- {np.sqrt(c)/nsamp:.5f})")
        json.dump({"n": n, "m": m, "nsamp": nsamp, "seed": seed, "bad": bad,
                   "counts": {str(k): c for k, c in counts.items()}},
                  open(f"mc_{n}x{m}_{nsamp}_{seed}.json", "w", encoding="utf-8"), indent=1)
