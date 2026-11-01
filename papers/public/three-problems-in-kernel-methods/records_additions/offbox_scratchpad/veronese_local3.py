"""Does d^{k-1} Tr(A^{2k}) reach the Catalan numbers, or only the k=2 one?

Same object as veronese_local2.py - A is the unit traceless symmetric matrix with x_i^T A x_i = 0 on
m-1 uniform points of the sphere, m = dim Sym_d^0 = d(d+1)/2 - 1 - but the design matrix is built
directly instead of by an einsum over the basis, which drops the cost per design from O(m^2 d^2) to
O(m^2) and puts d = 48..64 within reach on a laptop core.

For the basis fixed in veronese_local2 the entries are explicit: against the off-diagonal element
(E_ab + E_ba)/sqrt2 the quadratic form x^T B x is sqrt2 x_a x_b, and against the j-th traceless
diagonal direction (e_1 + ... + e_j - j e_{j+1})/sqrt(j^2+j) it is
(x_1^2 + ... + x_j^2 - j x_{j+1}^2)/sqrt(j^2+j), which is a running cumulative sum over the squares.

The question is whether the deviation from Catalan at d <= 16 (k=3 reading ~8 against 5) is a 1/d
correction that dies, or the limit itself. A 1/d correction must fall like 1/d; anything flat in d
is not a correction.
"""
import os, sys, time, json
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

KS = (2, 3, 4, 5)
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}
DS = [int(x) for x in (sys.argv[1].split(",") if len(sys.argv) > 1 else "8,12,16,24,32,40,48".split(","))]
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0     # seconds per d


def design_rows(X, d):
    """Rows  <z(x_i), B_j> = x_i^T B_j x_i  for the basis of Sym_d^0 fixed above. X is (n, d) unit rows."""
    n = X.shape[0]
    iu = np.triu_indices(d, 1)
    off = np.sqrt(2.0) * X[:, iu[0]] * X[:, iu[1]]              # (n, d(d-1)/2)
    S = X ** 2
    cum = np.cumsum(S, axis=1)                                   # cum[:, j-1] = x_1^2+...+x_j^2
    j = np.arange(1, d)
    dia = (cum[:, :d - 1] - j * S[:, 1:]) / np.sqrt(j * j + j)   # (n, d-1)
    return np.concatenate([off, dia], axis=1)                    # (n, m)


def to_matrix(c, d):
    iu = np.triu_indices(d, 1)
    n_off = len(iu[0])
    A = np.zeros((d, d))
    A[iu] = c[:n_off] / np.sqrt(2.0)
    A = A + A.T
    j = np.arange(1, d)
    w = c[n_off:] / np.sqrt(j * j + j)
    diag = np.zeros(d)
    diag[:d - 1] += np.cumsum(w[::-1])[::-1] * 0                  # placeholder, filled below
    # the j-th diagonal direction is (e_1+...+e_j - j e_{j+1})/sqrt(j^2+j)
    for idx, jj in enumerate(j):
        diag[:jj] += w[idx]
        diag[jj] -= jj * w[idx]
    A[np.diag_indices(d)] = diag
    return A


def one(d, rng, generic=False):
    m = d * (d + 1) // 2 - 1
    if generic:
        c = rng.standard_normal(m); c /= np.linalg.norm(c)
        return c, 0.0
    X = rng.standard_normal((m - 1, d)); X /= np.linalg.norm(X, axis=1, keepdims=True)
    Zb = design_rows(X, d)
    c = np.empty(m)
    try:
        c[:m - 1] = -np.linalg.solve(Zb[:, :m - 1], Zb[:, m - 1])
    except np.linalg.LinAlgError:
        return None, None
    c[m - 1] = 1.0
    c /= np.linalg.norm(c)
    return c, float(np.abs(Zb @ c).max())


print("checking the fast row construction against the explicit basis at d=7 ...", flush=True)
d0 = 7
B = []
iu0 = np.triu_indices(d0, 1)
for a, b in zip(*iu0):
    M = np.zeros((d0, d0)); M[a, b] = M[b, a] = 1 / np.sqrt(2.0); B.append(M)
for jj in range(1, d0):
    v = np.zeros(d0); v[:jj] = 1.0; v[jj] = -jj; v /= np.linalg.norm(v); B.append(np.diag(v))
B = np.array(B)
rng = np.random.default_rng(1)
Xc = rng.standard_normal((5, d0)); Xc /= np.linalg.norm(Xc, axis=1, keepdims=True)
slow = np.einsum("id,jde,ie->ij", Xc, B, Xc)
print("   max|fast - explicit| =", f"{np.abs(design_rows(Xc, d0) - slow).max():.2e}")
cc = rng.standard_normal(B.shape[0])
print("   max|to_matrix - sum c_j B_j| =", f"{np.abs(to_matrix(cc, d0) - np.einsum('j,jde->de', cc, B)).max():.2e}")
print("   traceless:", f"{abs(np.trace(to_matrix(cc, d0))):.2e}", flush=True)

print(f"\n{'d':>4} {'m':>6} {'rep':>5} | " + " ".join(f"d^{k-1}Tr(A^{2*k})".rjust(12) for k in KS) +
      " |  edge  resid", flush=True)
rows = []
for d in DS:
    m = d * (d + 1) // 2 - 1
    rng = np.random.default_rng(4242 + d)
    acc = {k: [] for k in KS}; gacc = {k: [] for k in KS}; res = []; edge = []; gedge = []
    t0 = time.time()
    while time.time() - t0 < BUDGET:
        c, r = one(d, rng)
        if c is None:
            continue
        A = to_matrix(c, d); A /= np.linalg.norm(A, "fro")
        w = np.linalg.eigvalsh(A)
        for k in KS:
            acc[k].append(d ** (k - 1) * float(np.sum(w ** (2 * k))))
        res.append(r); edge.append(np.sqrt(d) * float(np.abs(w).max()))
        cg, _ = one(d, rng, generic=True)
        Ag = to_matrix(cg, d); Ag /= np.linalg.norm(Ag, "fro")
        wg = np.linalg.eigvalsh(Ag)
        for k in KS:
            gacc[k].append(d ** (k - 1) * float(np.sum(wg ** (2 * k))))
        gedge.append(np.sqrt(d) * float(np.abs(wg).max()))
    n = len(acc[2])
    if n < 5:
        print(f"{d:4d} {m:6d} {n:5d} | too slow at this budget", flush=True); continue
    fm = lambda v: f"{np.mean(v):8.4f}"
    print(f"{d:4d} {m:6d} {n:5d} | " + " ".join(fm(acc[k]).rjust(12) for k in KS) +
          f" | {np.mean(edge):5.2f}  {np.mean(res):.0e}", flush=True)
    print(f"{'':>4} {'generic':>6} {n:5d} | " + " ".join(fm(gacc[k]).rjust(12) for k in KS) +
          f" | {np.mean(gedge):5.2f}", flush=True)
    rows.append(dict(d=d, m=m, n=n,
                     **{f"v{k}": float(np.mean(acc[k])) for k in KS},
                     **{f"vse{k}": float(np.std(acc[k]) / np.sqrt(n)) for k in KS},
                     **{f"g{k}": float(np.mean(gacc[k])) for k in KS},
                     **{f"gse{k}": float(np.std(gacc[k]) / np.sqrt(n)) for k in KS},
                     edge=float(np.mean(edge)), gedge=float(np.mean(gedge))))
    json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "veronese_local3.json"), "w"), indent=1)

print("\n-- is the excess over Catalan a 1/d correction?  (value - C_k) * d should be FLAT if it is --")
print("   d  " + "  ".join(f"k={k}".rjust(9) for k in KS) + "     | generic arm")
for r in rows:
    a = "  ".join(f"{(r[f'v{k}'] - CAT[k]) * r['d']:9.2f}" for k in KS)
    b = "  ".join(f"{(r[f'g{k}'] - CAT[k]) * r['d']:7.2f}" for k in KS)
    print(f"{r['d']:4d}  {a}     | {b}")
