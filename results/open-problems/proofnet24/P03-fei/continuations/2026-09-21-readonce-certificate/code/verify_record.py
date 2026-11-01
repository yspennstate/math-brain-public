"""Positive control for fei_recsys: materialize the actual finite Boolean function of a recursive system at a given
level with a fixed inner depth, compute its H, I, Pr[true] by brute force (Walsh transform over all 2^n inputs), and
compare with the (p, I, H) that the Lemma-3.1 recursion predicts for exactly that finite function.

Construction (matches evaluate()): level 0 = a fresh variable for every symbol (or a given base expression);
level m: kappa_0 = F_{m-1}; kappa_{j+1} = G(slots) with 'x' -> fresh variable, ('T',i,'prev') -> fresh copy of
F^{(i)}_{m-1}, ('T',i,'cur') -> fresh copy of kappa_j; F_m = kappa_d. Every copy is on disjoint variables.
"""
import sys, math
import numpy as np
sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
import fei_recsys as R

class Expr:
    """expression tree: ('var', idx) or ('gate', tt, k, [children])"""
    def __init__(self, kind, *args):
        self.kind = kind; self.args = args
    def varset(self):
        if self.kind == "var":
            return {self.args[0]}
        out = set()
        for c in self.args[2]:
            out |= c.varset()
        return out
    def nvars(self):
        return len(self.varset())

def materialize(system, level, depth, counter):
    """returns list of Expr, one per symbol, at the given level; counter is a one-element list for fresh variable ids"""
    def fresh():
        e = Expr("var", counter[0]); counter[0] += 1; return e
    if level == 0:
        return [fresh() for _ in system]
    prev = None  # lazily rebuilt copies: each reference needs a FRESH copy on new variables
    def copy_prev(i):
        return materialize(system, level - 1, depth, counter)[i]
    outs = []
    for j, (tt, k, wiring) in enumerate(system):
        kappa = copy_prev(j)   # kappa_0 = F_{m-1}
        for _ in range(depth):
            kids = []
            for w in wiring:
                if w[0] == "x":
                    kids.append(fresh())
                elif w[2] == "prev":
                    kids.append(copy_prev(w[1]))
                else:
                    if w[1] != j:
                        raise ValueError("cur reference to another symbol not supported in the materializer")
                    kids.append(rebuild(kappa, counter))
            kappa = Expr("gate", tt, k, kids)
        outs.append(kappa)
    return outs

def rebuild(e, counter):
    """a fresh copy of expression e on new variables"""
    if e.kind == "var":
        c = Expr("var", counter[0]); counter[0] += 1; return c
    tt, k, kids = e.args
    return Expr("gate", tt, k, [rebuild(c, counter) for c in kids])

def evaluate_expr(e, X, vmap):
    """X: array (N, nvars) of booleans (True = input true); vmap: variable id -> column; returns boolean array (N,)"""
    if e.kind == "var":
        return X[:, vmap[e.args[0]]]
    tt, k, kids = e.args
    vals = [evaluate_expr(c, X, vmap) for c in kids]
    idx = np.zeros(X.shape[0], dtype=np.int64)
    for i, v in enumerate(vals):
        idx |= v.astype(np.int64) << i
    return ((tt >> idx) & 1).astype(bool)

def brute_stats(e):
    n = e.nvars()
    if n > 22:
        raise ValueError("too many variables: %d" % n)
    N = 1 << n
    ar = np.arange(N)
    X = ((ar[:, None] >> np.arange(n)[None, :]) & 1).astype(bool)
    vmap = {v: i for i, v in enumerate(sorted(e.varset()))}
    truth = evaluate_expr(e, X, vmap)
    f = np.where(truth, -1.0, 1.0)
    # Walsh transform
    a = f.copy(); h = 1
    while h < N:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy(); a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(-1); h *= 2
    a /= N
    pS = a * a; nz = pS > 1e-18
    H = float(-(pS[nz] * np.log2(pS[nz])).sum())
    pop = np.array([bin(s).count("1") for s in range(N)])
    I = float((pop * pS).sum())
    p = float(truth.mean())
    return p, I, H, n

def recursion_fixed_depth(system, level, depth, starts=None):
    """the same recursion as evaluate() but with exactly `depth` inner iterations per level"""
    r = len(system)
    prev = [tuple(starts[j]) if starts else R.FRESH for j in range(r)]
    for m in range(level):
        cur = list(prev)
        for it in range(depth):
            new = []
            for j, (tt, k, wiring) in enumerate(system):
                ins = [R.FRESH if w[0] == "x" else (prev[w[1]] if w[2] == "prev" else cur[w[1]]) for w in wiring]
                p_out, It, Ht = R.biased_stats(R.tt_values(tt, k), k, [s[0] for s in ins])
                I = 0.0; H = Ht
                for s, iti in zip(ins, It):
                    pl = R.plus(s); I += iti * pl[0]; H += iti * pl[1]
                new.append((p_out, I, H))
            cur = new
        prev = cur
    return prev

def check(system, level, depth, label=""):
    counter = [0]
    exprs = materialize(system, level, depth, counter)
    ok = True
    pred = recursion_fixed_depth(system, level, depth)
    for j, e in enumerate(exprs):
        p, I, H, n = brute_stats(e)
        pp, pI, pH = pred[j]
        err = max(abs(p - pp), abs(I - pI), abs(H - pH))
        print("  %s level %d depth %d symbol %d: n=%2d brute (p %.6f I %.6f H %.6f ratio %.5f) recursion (p %.6f I %.6f H %.6f) maxerr %.1e %s"
              % (label, level, depth, j, n, p, I, H, H / I, pp, pI, pH, err, "OK" if err < 1e-9 else "MISMATCH"))
        ok &= err < 1e-9
    return ok

if __name__ == "__main__":
    nand_beta = [(R.NAND2, 2, [("T", 0, "prev"), ("T", 0, "cur")])]
    ok = True
    for level, depth in ((1, 1), (1, 2), (1, 4), (2, 1), (2, 2), (3, 1)):
        ok &= check(nand_beta, level, depth, "NAND(prev,cur)")
    chain = [(R.CHAIN23, 3, [("x",), ("x",), ("T", 0, "prev")])]
    for level in (1, 2, 3, 5):
        ok &= check(chain, level, 1, "chain")
    # a system with a fresh variable, a prev and a cur input in a 3-input gate
    g = R.gate_from_fn(lambda a, b, c: (a and b) or (not c), 3)
    sysg = [(g, 3, [("x",), ("T", 0, "prev"), ("T", 0, "cur")])]
    for level, depth in ((1, 2), (2, 1), (2, 2)):
        ok &= check(sysg, level, depth, "mixed3")
    print("POSITIVE CONTROL:", "PASS" if ok else "FAIL")
