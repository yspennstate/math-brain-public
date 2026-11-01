"""Exhaustive (n <= 4) and sampled (n = 5, 6) comparison of reference families, vectorized over functions.

For each function: H, I, and
  CSmin  = min over all binary trees of the count-splitting reference cost,
  HITmin = min over all binary trees of the hit-only tree-Markov cost,
  LW     = level-wise product (conditional Bernoulli) optimum  [n <= 4 only; vectorized via exchangeable bound check]
Reports max ratios and argmax functions.
"""
import itertools, sys, time, json
import numpy as np
import wlib as W

W.set_polite()


def all_trees(items):
    items = list(items)
    if len(items) == 1:
        yield items[0]
        return
    first, rest = items[0], items[1:]
    for r in range(0, len(rest)):
        for A in itertools.combinations(rest, r):
            B = [x for x in rest if x not in A]
            if not B:
                continue
            for tl in all_trees([first] + list(A)):
                for tr in all_trees(B):
                    yield (tl, tr)


def internal_nodes(t, out):
    if isinstance(t, (int, np.integer)):
        return
    out.append((W.tree_mask(t[0]), W.tree_mask(t[1])))
    internal_nodes(t[0], out)
    internal_nodes(t[1], out)
    return out


def ent_rows(P):
    """row-wise entropy in bits of nonnegative matrix rows."""
    with np.errstate(divide="ignore", invalid="ignore"):
        L = np.where(P > 0, -P * np.log2(np.where(P > 0, P, 1.0)), 0.0)
    return L.sum(axis=1)


def law(Pmat, labels, L):
    """Pmat: (F, 2^n) spectral laws; labels: (2^n,) ints in [0, L). Returns (F, L) laws."""
    M = np.zeros((len(labels), L))
    M[np.arange(len(labels)), labels] = 1.0
    return Pmat @ M


def run(n, Pmat, tag, log):
    N = 1 << n
    S = np.arange(N)
    pop = W.popcounts(N)
    F = Pmat.shape[0]
    H = ent_rows(Pmat)
    I = Pmat @ pop
    Hsize = ent_rows(law(Pmat, pop, n + 1))
    trees = list(all_trees(range(n)))
    node_cache_cs = {}
    node_cache_hit = {}

    def node_cost(B1, B2, trunc):
        key = (B1, B2)
        cache = node_cache_hit if trunc else node_cache_cs
        if key not in cache:
            c1 = pop[S & B1]
            c2 = pop[S & B2]
            if trunc:
                c1 = np.minimum(c1, 1); c2 = np.minimum(c2, 1)
            joint = ent_rows(law(Pmat, c1 * (n + 1) + c2, (n + 1) ** 2))
            tot = ent_rows(law(Pmat, np.minimum(c1 + c2, 1) if trunc else c1 + c2, 2 * n + 2))
            cache[key] = joint - tot
        return cache[key]

    root_hit = ent_rows(law(Pmat, np.minimum(pop, 1), 2))
    CSmin = np.full(F, np.inf); HITmin = np.full(F, np.inf)
    for t in trees:
        nodes = internal_nodes(t, [])
        cs = Hsize.copy(); hit = root_hit.copy()
        for (B1, B2) in nodes:
            cs += node_cost(B1, B2, False)
            hit += node_cost(B1, B2, True)
        CSmin = np.minimum(CSmin, cs)
        HITmin = np.minimum(HITmin, hit)
    ok = I > 1e-12
    res = {"n": n, "tag": tag, "F": int(F)}
    for name, V in (("H", H), ("CSmin", CSmin), ("HITmin", HITmin)):
        r = np.where(ok, V / np.where(ok, I, 1), 0)
        j = int(np.argmax(r))
        res[f"max {name}/I"] = float(r[j]); res[f"argmax {name}/I"] = j
    for name, V in (("CSmin-H", CSmin - H), ("HITmin-H", HITmin - H)):
        r = np.where(ok, V / np.where(ok, I, 1), 0)
        j = int(np.argmax(r))
        res[f"max ({name})/I"] = float(r[j]); res[f"argmax ({name})/I"] = j
        res[f"max {name} (bits)"] = float(np.max(V))
    # does CS ever lose to HIT? fraction where CSmin <= HITmin
    res["frac CSmin<=HITmin"] = float(np.mean(CSmin <= HITmin + 1e-12))
    print(json.dumps(res), file=log, flush=True)
    print(json.dumps(res), flush=True)
    return H, I, CSmin, HITmin


def main():
    log = open("../logs/exhaustive_small.log", "a")
    rng = np.random.default_rng(11)
    for n in (2, 3, 4):
        N = 1 << n
        X = np.arange(1 << N, dtype=np.int64)
        tts = 1 - 2 * ((X[:, None] >> np.arange(N)[None, :]) & 1)
        Pmat = W.wht(tts.astype(np.float64)) ** 2
        t0 = time.time()
        H, I, CS, HIT = run(n, Pmat, "all functions", log)
        # print the extremal functions
        ok = I > 1e-12
        for nm, V in (("CSmin/I", CS / np.where(ok, I, 1)), ("(CSmin-H)/I", (CS - H) / np.where(ok, I, 1)),
                      ("HITmin/I", HIT / np.where(ok, I, 1))):
            j = int(np.argmax(np.where(ok, V, 0)))
            print(f"  n={n} argmax {nm}: table={tts[j].tolist()} H={H[j]:.5f} I={I[j]:.5f} CS={CS[j]:.5f} HIT={HIT[j]:.5f}", file=log, flush=True)
            print(f"  n={n} argmax {nm}: table={tts[j].tolist()} H={H[j]:.5f} I={I[j]:.5f} CS={CS[j]:.5f} HIT={HIT[j]:.5f}", flush=True)
        print(f"  [{time.time()-t0:.1f}s]", flush=True)
    for n, F in ((5, 100000), (6, 20000)):
        N = 1 << n
        tts = rng.choice(np.array([-1.0, 1.0]), size=(F, N))
        # add biased random functions too (Pr[true] = q) to reach unbalanced / sparse spectra
        q = rng.uniform(0.02, 0.5, size=(F // 2, 1))
        tts[F // 2:] = np.where(rng.uniform(size=(F // 2, N)) < q, -1.0, 1.0)
        Pmat = W.wht(tts) ** 2
        t0 = time.time()
        H, I, CS, HIT = run(n, Pmat, f"random {F} (half balanced-uniform, half biased)", log)
        ok = I > 1e-12
        j = int(np.argmax(np.where(ok, (CS - H) / np.where(ok, I, 1), 0)))
        print(f"  n={n} argmax (CS-H)/I table={tts[j].astype(int).tolist()} H={H[j]:.5f} I={I[j]:.5f} CS={CS[j]:.5f}", file=log, flush=True)
        print(f"  [{time.time()-t0:.1f}s]", flush=True)


if __name__ == "__main__":
    main()
