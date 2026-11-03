# T021: check the general-P recursion (q31_readonce_general.stepP) against exact truth tables on random read-once trees
# with UNEQUAL children: random NAND trees (every read-once AND/OR/NOT formula is one, up to negating inputs and output,
# which leaves D_k and I_k unchanged). Convention as q31_tree_entropy: -1 = true, a gate is +1 iff all its children are -1.
# At each gate on the path to x_k, P = prod over the path child's siblings of Pr[sibling = -1].
import random, numpy as np, mpmath as mp
from q31_tree_entropy import wht, ent
from q31_readonce_general import stepP
mp.mp.dps = 50
def rand_tree(nvars, rng):
    leaves = list(range(nvars)); rng.shuffle(leaves); nodes = [("x", i) for i in leaves]
    while len(nodes) > 1:
        k = min(len(nodes), rng.choice([2, 2, 3, 4]))
        grp = [nodes.pop(rng.randrange(len(nodes))) for _ in range(k)]
        nodes.append(("g", grp))
    return nodes[0]
def evalt(t, X):
    if t[0] == "x": return X[:, t[1]]
    v = np.ones(X.shape[0], dtype=bool)
    for c in t[1]: v &= (evalt(c, X) == -1)
    return np.where(v, 1, -1)
def path(t, k):  # sibling lists from the leaf x_k up to the root
    if t[0] == "x": return [] if t[1] == k else None
    for i, c in enumerate(t[1]):
        p = path(c, k)
        if p is not None: return p + [[s for j, s in enumerate(t[1]) if j != i]]
    return None
def depth(t): return 0 if t[0] == "x" else 1 + max(depth(c) for c in t[1])
rng = random.Random(7); worst = 0.0; cases = 0; trees = 0; maxdepth = 0
for trial in range(60):
    n = rng.randint(3, 13); t = rand_tree(n, rng)
    if t[0] == "x": continue
    trees += 1; maxdepth = max(maxdepth, depth(t))
    N = 1 << n; X = np.where(((np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1) == 1, -1, 1)
    f = evalt(t, X); c = wht(f); H = ent(c); S = np.arange(N)
    for k in range(n):
        m = 1 << k; lo = S[(S & m) == 0]
        Dk = H - (ent(wht(f[lo])) + ent(wht(f[lo | m]))) / 2; Ik = float((c[lo | m] ** 2).sum())
        st = (mp.mpf(0), mp.mpf(1), mp.mpf(0))
        for sibs in path(t, k):
            P = 1.0
            for s in sibs: P *= float((evalt(s, X) == -1).mean())
            st = stepP(st, mp.mpf(P))
        worst = max(worst, abs(Dk - float(st[2])), abs(Ik - float(st[1]))); cases += 1
print("random read-once NAND trees with unequal children: %d trees (depth <= %d), %d (tree, coordinate) cases" % (trees, maxdepth, cases))
print("max |recursion - truth table| over D_k and I_k = %.2e" % worst)
print("general-P recursion exact on every case (err < 1e-9):", worst < 1e-9)
