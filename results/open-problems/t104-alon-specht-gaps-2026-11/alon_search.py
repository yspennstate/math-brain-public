"""Search for small values of lambda_min(G, tau) / lambda_min(G, sigma) over weighted graphs G on [n].

Setting (G. Alon, arXiv 2610.22151): for a partition nu of n let rho_nu be the Specht module and
L(G, nu) = sum_{i<j} w_ij (I - rho_nu((i j))).  Conjecture 1.5 there: for all [n] != sigma, sigma dominating tau,
lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) for every weighted graph G.  Theorem 1.3 there: a positive constant
exists exactly when sigma dominates tau.

Representation matrices are built in Young's orthogonal form, so every L is symmetric.

usage: alon_search.py n starts seed [mode]
  mode = dom   (default) pairs with sigma dominating tau, sigma != tau, sigma != [n]
  mode = nondom          pairs with sigma NOT dominating tau (control: the ratio should go to 0)
  mode = selftest        check the representation (relations, star Laplacian spectrum) and stop
Prints one line per pair: n, tau, sigma, best ratio found, number of starts, the weights at the best point.
"""
import sys, itertools, math
import numpy as np
from scipy.optimize import minimize


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def syts(shape):
    """Standard Young tableaux of the shape, each as a tuple pos[k-1] = (row, col) of the entry k."""
    n = sum(shape)
    out = []

    def rec(cur, pos):
        k = len(pos)
        if k == n:
            out.append(tuple(pos))
            return
        for r in range(len(shape)):
            c = cur[r]
            if c < shape[r] and (r == 0 or cur[r - 1] > c):
                cur[r] += 1
                pos.append((r, c))
                rec(cur, pos)
                pos.pop()
                cur[r] -= 1

    rec([0] * len(shape), [])
    return out


def adjacent(shape):
    """Matrices of s_1 .. s_{n-1} in Young's orthogonal form."""
    T = syts(shape)
    idx = {t: a for a, t in enumerate(T)}
    n = sum(shape)
    d = len(T)
    mats = []
    for k in range(1, n):
        M = np.zeros((d, d))
        for a, t in enumerate(T):
            (r1, c1), (r2, c2) = t[k - 1], t[k]
            ax = (c2 - r2) - (c1 - r1)          # content of k+1 minus content of k
            M[a, a] = 1.0 / ax
            if abs(ax) > 1:
                u = list(t)
                u[k - 1], u[k] = u[k], u[k - 1]
                b = idx[tuple(u)]
                M[a, b] = math.sqrt(1.0 - 1.0 / (ax * ax))
        mats.append(M)
    return mats, T


def edge_ops(shape):
    """A[e] = I - rho((i j)) for the edges e = (i, j), i < j, in lexicographic order; plus the tableaux."""
    s, T = adjacent(shape)
    n = sum(shape)
    d = len(T)
    t = {}
    for i in range(1, n):
        t[(i, i + 1)] = s[i - 1]
        for j in range(i + 2, n + 1):
            t[(i, j)] = s[j - 2] @ t[(i, j - 1)] @ s[j - 2]
    edges = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    A = np.stack([np.eye(d) - t[e] for e in edges])
    return A, edges, T, s


def dominates(sig, tau):
    a = b = 0
    for r in range(max(len(sig), len(tau))):
        a += sig[r] if r < len(sig) else 0
        b += tau[r] if r < len(tau) else 0
        if a < b:
            return False
    return True


def selftest(n):
    worst = 0.0
    for nu in partitions(n):
        A, edges, T, s = edge_ops(nu)
        d = len(T)
        I = np.eye(d)
        for k in range(n - 1):
            worst = max(worst, abs(s[k] @ s[k] - I).max(), abs(s[k] - s[k].T).max())
            if k + 1 < n - 1:
                worst = max(worst, abs(s[k] @ s[k + 1] @ s[k] - s[k + 1] @ s[k] @ s[k + 1]).max())
            for m in range(k + 2, n - 1):
                worst = max(worst, abs(s[k] @ s[m] - s[m] @ s[k]).max())
        # star Laplacian S_k = sum_{i<k} (I - (i k)) is diagonal with entries k - 1 - content_T(k)  (Lemma 4.2)
        for k in range(2, n + 1):
            S = sum(A[edges.index((i, k))] for i in range(1, k))
            want = np.diag([k - 1 - (t[k - 1][1] - t[k - 1][0]) for t in T])
            worst = max(worst, abs(S - want).max())
    print("selftest n=%d: largest deviation %.2e over %d partitions" % (n, worst, len(list(partitions(n)))))
    return worst


def lam(A, w):
    L = np.tensordot(w, A, axes=1)
    ev, V = np.linalg.eigh(L)
    return ev[0], V[:, 0]


def make_obj(At, As):
    def f(x):
        w = x * x
        lt, vt = lam(At, w)
        ls, vs = lam(As, w)
        if ls <= 1e-13 or lt <= 1e-13:
            return 50.0, np.zeros_like(x)
        gt = np.einsum("i,eij,j->e", vt, At, vt)
        gs = np.einsum("i,eij,j->e", vs, As, vs)
        return math.log(lt / ls), (gt / lt - gs / ls) * 2.0 * x
    return f


def starts(n, m, edges, rng, k):
    """Random starting weights of several shapes: flat, heavy-tailed, sparse, path-like, star-like."""
    out = []
    for a in range(k):
        kind = a % 5
        if kind == 0:
            w = rng.uniform(0.2, 1.0, m)
        elif kind == 1:
            w = np.exp(rng.normal(0.0, 2.5, m))
        elif kind == 2:
            w = rng.uniform(0.0, 1.0, m) * (rng.uniform(0, 1, m) < 0.5) + 1e-3
        elif kind == 3:
            perm = rng.permutation(n) + 1
            w = np.full(m, 1e-3)
            for q in range(n - 1):
                e = tuple(sorted((perm[q], perm[q + 1])))
                w[edges.index(e)] = np.exp(rng.normal(0.0, 1.5))
        else:
            c = rng.integers(1, n + 1)
            w = np.array([np.exp(rng.normal(0.0, 1.5)) if c in e else 1e-3 * rng.uniform(0, 1) for e in edges])
        out.append(np.sqrt(w / w.max()))
    return out


def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    seed = int(sys.argv[3])
    mode = sys.argv[4] if len(sys.argv) > 4 else "dom"
    if mode == "selftest":
        selftest(n)
        return
    rng = np.random.default_rng(seed)
    parts = [p for p in partitions(n) if p != (n,)]
    ops = {}
    edges = None
    for p in parts:
        A, edges, T, s = edge_ops(p)
        ops[p] = A
    m = len(edges)
    for tau in parts:
        for sig in parts:
            if sig == tau:
                continue
            dom = dominates(sig, tau)
            if (mode == "dom") != dom:
                continue
            f = make_obj(ops[tau], ops[sig])
            best, bw = float("inf"), None
            for x0 in starts(n, m, edges, rng, k):
                r = minimize(f, x0, jac=True, method="L-BFGS-B", options={"maxiter": 400})
                w = r.x * r.x
                lt, _ = lam(ops[tau], w)
                ls, _ = lam(ops[sig], w)
                if ls > 1e-12 and lt / ls < best:
                    best, bw = lt / ls, w / w.max()
            print("%d\t%s\t%s\t%.9f\t%d\t%s" % (n, "".join(map(str, tau)), "".join(map(str, sig)), best, k,
                                                " ".join("%.4g" % v for v in bw)), flush=True)


if __name__ == "__main__":
    main()
