"""Test bed at larger n: desirability structure, the dominance profile K, Theorem 2's bound, the
coarse-graining bound (Theorem 3), the entropy change under full shifting, and the composition lemma.

Families: Numaro's 18-variable record function g; perfect matching of K_{m,m} (m = 3, 4); tribes;
majority; recursive ternary majority (depth 2); random monotone functions and their shifted forms;
random shifted functions at n = 10..14.
"""
import sys, math, time, itertools
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
from monolib import setup_process, fwht_float, popcounts, desirability_array

LOG2 = math.log(2.0)
Bc = 3.0 * math.sqrt(3.0 / math.pi)
L1 = 2.0 * math.log(Bc) + 2.0
INP = "../../inputs/numaro18_pm1_table.npy"


def C_of_K(K):
    L = L1 + math.log(K)
    a = (1.0 + math.sqrt(1.0 + 4.0 / L)) / 2.0
    return 3.0 + (1.0 + math.log(a / (a - 1.0)) + a * L) / LOG2


C3 = None  # constant of Theorem 3, set below


def spectrum(f01, n):
    F = 1.0 - 2.0 * f01.astype(np.float64)
    c = fwht_float(F)
    return c


def HI(c, n, pc=None):
    p = c * c
    if pc is None:
        pc = popcounts(n)
    nz = p > 1e-300
    H = float(-(p[nz] * np.log2(p[nz])).sum())
    I = float((pc * p).sum())
    return H, I


def relevant(f01, n):
    xs = np.arange(1 << n)
    rel = []
    for i in range(n):
        lo = xs[((xs >> i) & 1) == 0]
        if np.any(f01[lo] != f01[lo | (1 << i)]):
            rel.append(i)
    return rel


def chain_cover(dom, rel):
    """Minimum chain cover of the desirability preorder on rel (Dilworth via bipartite matching on
    the strict order of the quotient, with equivalent coordinates merged into one class).
    Returns (width, list of chains as lists of coordinates in decreasing desirability)."""
    # equivalence classes
    classes = []
    seen = set()
    for i in rel:
        if i in seen:
            continue
        cl = [j for j in rel if dom[i, j] and dom[j, i]]
        for j in cl:
            seen.add(j)
        classes.append(cl)
    m = len(classes)
    rep = [cl[0] for cl in classes]
    # strict order a > b (a more desirable than b): dom[b, a] and not dom[a, b]
    rows, cols = [], []
    for a in range(m):
        for b in range(m):
            if a != b and dom[rep[b], rep[a]] and not dom[rep[a], rep[b]]:
                rows.append(a)
                cols.append(b)
    if rows:
        G = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(m, m))
        match = maximum_bipartite_matching(G, perm_type='column')
    else:
        match = -np.ones(m, dtype=int)
    nmatch = int((match >= 0).sum())
    width = m - nmatch
    # build chains: a -> match[a] (a above match[a])
    nxt = {a: int(match[a]) for a in range(m) if match[a] >= 0}
    has_prev = set(nxt.values())
    chains = []
    for a in range(m):
        if a in has_prev:
            continue
        ch = []
        cur = a
        while True:
            ch.extend(classes[cur])
            if cur in nxt:
                cur = nxt[cur]
            else:
                break
        chains.append(ch)
    return width, chains


def profile_K(dom, rel):
    dsz = {i: sum(1 for j in rel if dom[i, j]) for i in rel}
    K = 0.0
    for d in range(1, len(rel) + 1):
        cnt = sum(1 for i in rel if dsz[i] <= d)
        K = max(K, cnt / d)
    return K, dsz


def pattern_entropy(c, n, chains):
    """H(Pi) where Pi = set of chains hit by the spectral sample."""
    N = 1 << n
    lab = np.zeros(N, dtype=np.int64)
    xs = np.arange(N)
    for k, ch in enumerate(chains):
        mask = 0
        for i in ch:
            mask |= (1 << i)
        lab |= (((xs & mask) != 0).astype(np.int64) << k)
    p = c * c
    agg = np.bincount(lab, weights=p)
    agg = agg[agg > 1e-300]
    return float(-(agg * np.log2(agg)).sum())


def shift_fully(f01, n):
    """Apply S_ij (shift j -> i) for all i < j until stable: the result is regular with order 0 >= 1 >= ..."""
    g = f01.copy()
    xs = np.arange(1 << n)
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                sel = (((xs >> i) & 1) == 0) & (((xs >> j) & 1) == 1)
                x = xs[sel]
                y = x ^ ((1 << i) | (1 << j))
                mv = (g[x] == 1) & (g[y] == 0)
                if mv.any():
                    g[x[mv]] = 0
                    g[y[mv]] = 1
                    changed = True
    return g


def analyse(name, f01, n, do_shift=True):
    c = spectrum(f01, n)
    pc = popcounts(n)
    H, I = HI(c, n, pc)
    dom = desirability_array(f01, n)
    rel = relevant(f01, n)
    w, chains = chain_cover(dom, rel)
    K, dsz = profile_K(dom, rel)
    Hpi = pattern_entropy(c, n, chains)
    line = (f"{name:34s} n={n:2d} H={H:9.5f} I={I:9.5f} H/I={H/I:7.4f} width={w:3d} K={K:6.3f} "
            f"C(K)={C_of_K(K):7.3f} H(Pi)/I={Hpi/I:7.4f} thm3 slack=(H - H(Pi))/I={(H-Hpi)/I:7.4f} <= {C3:.4f}")
    if do_shift:
        g = shift_fully(f01, n)
        cg = spectrum(g, n)
        Hg, Ig = HI(cg, n, pc)
        line += f"  | shifted: H={Hg:9.5f} I={Ig:9.5f} (H-Hs)/I={(H-Hg)/I:7.4f}"
    print(line, flush=True)
    return H, I


def tribes(w, s):
    n = w * s
    xs = np.arange(1 << n)
    f = np.zeros(1 << n, dtype=np.uint8)
    for t in range(s):
        mask = ((1 << w) - 1) << (t * w)
        f |= ((xs & mask) == mask).astype(np.uint8)
    return f, n


def majority(n):
    pc = popcounts(n)
    return (2 * pc > n).astype(np.uint8), n


def recmaj(depth):
    n = 3 ** depth
    xs = np.arange(1 << n)
    vals = [((xs >> i) & 1).astype(np.uint8) for i in range(n)]
    while len(vals) > 1:
        vals = [((vals[k] + vals[k + 1] + vals[k + 2]) >= 2).astype(np.uint8) for k in range(0, len(vals), 3)]
    return vals[0], n


def perfect_matching(m):
    n = m * m
    xs = np.arange(1 << n)
    f = np.zeros(1 << n, dtype=np.uint8)
    for perm in itertools.permutations(range(m)):
        mask = 0
        for a in range(m):
            mask |= 1 << (a * m + perm[a])
        f |= ((xs & mask) == mask).astype(np.uint8)
    return f, n


def random_monotone(n, rng, nmin=None, lo=None, hi=None):
    """Up-closure of a random family of sets drawn around the middle layer."""
    N = 1 << n
    pc = popcounts(n)
    xs = np.arange(N)
    if nmin is None:
        nmin = rng.integers(2, 2 * n)
    k = rng.integers(max(1, n // 2 - 1), n // 2 + 2, size=nmin)
    gens = []
    for kk in k:
        gens.append(int(rng.choice(np.nonzero(pc == kk)[0])))
    f = np.zeros(N, dtype=np.uint8)
    for gset in gens:
        f |= ((xs & gset) == gset).astype(np.uint8)
    return f


def lex(a, m):
    """Initial segment of the binary order of size a on m bits (coordinate m-1 most significant)."""
    xs = np.arange(1 << m)
    return (xs < a).astype(np.uint8)


def composition_check(rng, trials=200):
    """Composition lemma: F = G(f_1..f_k) with G read-once AND/OR and arbitrary leaves.
    Check H(F) <= 6.4573 I(F) + sum_j Inf_j^mu(G) H(f_j), and Hart: I(lex) <= I(f_j)."""
    worst = -1e9
    hart_worst = -1e9
    for t in range(trials):
        k = int(rng.integers(2, 4))
        sizes = [int(rng.integers(1, 5)) for _ in range(k)]
        n = sum(sizes)
        if n > 14:
            continue
        leaves = []
        for s in sizes:
            while True:
                f = rng.integers(0, 2, size=1 << s).astype(np.uint8)
                if 0 < f.sum() < (1 << s):
                    break
            leaves.append(f)
        # G: random read-once AND/OR formula over k inputs with random negations
        xs = np.arange(1 << n)
        vals = []
        off = 0
        for s, f in zip(sizes, leaves):
            sub = (xs >> off) & ((1 << s) - 1)
            v = f[sub]
            if rng.random() < 0.3:
                v = 1 - v
            vals.append(v.astype(np.uint8))
            off += s
        # combine left to right with random AND/OR
        acc = vals[0]
        infl_leaf = []
        for v in vals[1:]:
            acc = (acc & v) if rng.random() < 0.5 else (acc | v)
        F = acc
        c = spectrum(F, n)
        H, I = HI(c, n)
        # influence of block j on F under the leaf biases = Pr[block j pivotal] = It_j/V_j
        rhs = 6.4573 * I
        off = 0
        for s, f in zip(sizes, leaves):
            # pivotality of block j: F changes when leaf value flips; estimate exactly by recomputing with
            # the leaf forced to 0 and 1
            cf = spectrum(f, s)
            Hf, If = HI(cf, s)
            # recompute F with leaf j forced
            vals0 = []
            vals1 = []
            # rebuild quickly: evaluate the formula structure again is complex; instead use the identity
            # sum over the block's coordinates of Inf_i(F) = Pr[block pivotal] * I(f_j)
            blockI = 0.0
            p = c * c
            pcn = popcounts(n)
            for i in range(off, off + s):
                blockI += float(p[((xs >> i) & 1) == 1].sum())
            piv = blockI / If if If > 0 else 0.0
            rhs += piv * Hf
            # Hart check
            a = int(f.sum())
            g = lex(a, s)
            cg = spectrum(g, s)
            Hg, Ig = HI(cg, s)
            hart_worst = max(hart_worst, Ig - If)
            off += s
        worst = max(worst, H - rhs)
    print(f"composition lemma: max over {trials} random instances of H(F) - [6.4573 I(F) + sum_j piv_j H(f_j)] = {worst:.6f} (must be <= 0)")
    print(f"Hart: max of I(lex_a) - I(f) over leaves = {hart_worst:.3e} (must be <= 0)")


def main():
    global C3
    setup_process()
    a = (1.0 + math.sqrt(1.0 + 4.0 / L1)) / 2.0
    C3 = 1.0 + (1.0 + math.log(a / (a - 1.0)) + a * L1) / LOG2
    print(f"C(1) = {C_of_K(1.0):.10f}, Theorem 3 constant c3 = {C3:.10f}")
    rng = np.random.default_rng(20260923)
    # Numaro's g
    T = np.load(INP)
    f = (T == -1).astype(np.uint8)
    analyse("Numaro g (18)", f, 18, do_shift=True)
    for m in (3, 4):
        f, n = perfect_matching(m)
        analyse(f"perfect matching K_{m},{m}", f, n)
    for (w, s) in [(2, 3), (2, 5), (3, 3), (3, 4), (4, 3), (2, 8)]:
        f, n = tribes(w, s)
        analyse(f"tribes w={w} s={s}", f, n)
    for n in (5, 9, 13):
        f, n = majority(n)
        analyse(f"majority {n}", f, n)
    f, n = recmaj(2)
    analyse("recursive MAJ3 depth 2", f, n)
    for n in (10, 12, 14):
        for t in range(3):
            f = random_monotone(n, rng)
            if f.sum() in (0, 1 << n):
                continue
            analyse(f"random monotone n={n} #{t}", f, n)
    for n in (10, 12, 14):
        for t in range(3):
            f = shift_fully(random_monotone(n, rng), n)
            if f.sum() in (0, 1 << n):
                continue
            analyse(f"random SHIFTED n={n} #{t}", f, n, do_shift=False)
    composition_check(rng)


if __name__ == "__main__":
    main()
