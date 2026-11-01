"""The Veronese leave-one-out normal, built from its definition rather than from the driver.

A is the unit traceless symmetric matrix whose quadratic form kills the design:

    A in Sym_d^0,  ||A||_F = 1,  x_i^T A x_i = 0  for i = 1 .. m-1,   m = dim Sym_d^0 = d(d+1)/2 - 1

Two things make this the right object and make the whitening free. The centred Veronese
z(x) = x x^T - I/d is traceless (Tr x x^T = 1 for a unit vector), so the design lives in Sym_d^0 and
never leaves it; and O(d) acts irreducibly on Sym_d^0, so by Schur the covariance of z is a SCALAR
multiple of the identity there - whitening cannot change a direction, only a length. So the null
direction needs no covariance at all, and <A, z(x)> = Tr(A x x^T) = x^T A x once Tr A = 0.

The first version of this script centred the Veronese inside the full Sym_d and read
d^{k-1} Tr(A^{2k}) = 1.0000 for every k and every d. That is not a result: centring makes every row
traceless, so the identity is orthogonal to all of them, the null space is span(I), and A = I/sqrt(d)
has a flat spectrum by construction. The degeneracy is the reason the object must be defined inside
Sym_d^0 with m = p - 1 rather than in Sym_d with p.

Target: d^{k-1} Tr(A^{2k}) -> C_k = 2, 5, 14, 42 (Catalan), the even moments of the semicircle,
which is what a uniformly random direction in Sym_d^0 gives. Run: python veronese_local2.py [dmax] [reps]
"""
import os, sys, time
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
REPS = int(sys.argv[2]) if len(sys.argv) > 2 else 200
KS = (2, 3, 4, 5)
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}


def basis(d):
    """Orthonormal basis of Sym_d^0 (traceless symmetric), Frobenius inner product. m = d(d+1)/2 - 1."""
    B = []
    iu = np.triu_indices(d, 1)
    for a, b in zip(*iu):                      # off-diagonal: (E_ab + E_ba)/sqrt(2)
        M = np.zeros((d, d)); M[a, b] = M[b, a] = 1 / np.sqrt(2.0); B.append(M)
    for j in range(1, d):                      # traceless diagonal: Gram-Schmidt on the diagonal
        v = np.zeros(d); v[:j] = 1.0; v[j] = -j
        v /= np.linalg.norm(v); B.append(np.diag(v))
    return np.array(B)                          # (m, d, d)


def run(d, reps, rng, generic=False):
    B = basis(d); m = B.shape[0]
    assert m == d * (d + 1) // 2 - 1
    out = {k: [] for k in KS}
    res, edge = [], []
    for _ in range(reps):
        if generic:                             # a uniformly random direction in Sym_d^0
            c = rng.standard_normal(m); c /= np.linalg.norm(c)
        else:
            X = rng.standard_normal((m - 1, d)); X /= np.linalg.norm(X, axis=1, keepdims=True)
            # row i, column j:  <z(x_i), B_j> = x_i^T B_j x_i
            Zb = np.einsum("id,jde,ie->ij", X, B, X)          # (m-1, m)
            # null vector by a linear solve, then checked against the true residual
            c = np.empty(m)
            try:
                c[:m - 1] = -np.linalg.solve(Zb[:, :m - 1], Zb[:, m - 1])
            except np.linalg.LinAlgError:
                continue
            c[m - 1] = 1.0
            c /= np.linalg.norm(c)
            res.append(float(np.abs(Zb @ c).max()))
        A = np.einsum("j,jde->de", c, B)
        A /= np.linalg.norm(A, "fro")
        w = np.linalg.eigvalsh(A)
        for k in KS:
            out[k].append(d ** (k - 1) * float(np.sum(w ** (2 * k))))
        edge.append(np.sqrt(d) * float(np.abs(w).max()))
    return out, res, edge


print(f"{'d':>3} {'m':>5} {'rep':>4} | " + " ".join(f"d^{k-1}Tr(A^{2*k})".rjust(13) for k in KS) +
      " |  edge  resid", flush=True)
print(f"{'':>3} {'':>5} {'':>4} | " + " ".join(f"(Catalan {CAT[k]:.0f})".rjust(13) for k in KS) +
      " |  (2.0)", flush=True)
rows = []
for d in (6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32):
    if d > DMAX:
        break
    m = d * (d + 1) // 2 - 1
    rng = np.random.default_rng(777 + d)
    t0 = time.time()
    r = max(30, min(REPS, int(REPS * (16.0 / d) ** 3)))
    ver, res, edge = run(d, r, rng)
    gen, _, edg = run(d, r, rng, generic=True)
    if not ver[2]:
        continue
    f = lambda v: f"{np.mean(v):8.4f}"
    print(f"{d:3d} {m:5d} {len(ver[2]):4d} | " + " ".join(f(ver[k]).rjust(13) for k in KS) +
          f" | {np.mean(edge):5.2f}  {np.mean(res):.0e}   [{time.time()-t0:4.1f}s]", flush=True)
    print(f"{'':>3} {'generic':>5} {len(gen[2]):4d} | " + " ".join(f(gen[k]).rjust(13) for k in KS) +
          f" | {np.mean(edg):5.2f}", flush=True)
    rows.append(dict(d=d, m=m, n=len(ver[2]),
                     **{f"v{k}": float(np.mean(ver[k])) for k in KS},
                     **{f"vse{k}": float(np.std(ver[k]) / np.sqrt(len(ver[k]))) for k in KS},
                     **{f"g{k}": float(np.mean(gen[k])) for k in KS},
                     edge=float(np.mean(edge)), edge_gen=float(np.mean(edg))))

print("\n-- fit  d^{k-1}Tr(A^{2k}) = C_k + b/d  on the Veronese arm, and the same on the generic arm --")
print(" k   Catalan    Veronese: C_hat    b        | generic: C_hat     b")
for k in KS:
    for lab, key in (("ver", "v"), ("gen", "g")):
        x = np.array([1.0 / r["d"] for r in rows]); y = np.array([r[f"{key}{k}"] for r in rows])
        b, c = np.polyfit(x, y, 1)
        if lab == "ver":
            line = f"{k:2d}   {CAT[k]:6.0f}      {c:8.4f}  {b:+9.3f}   "
        else:
            print(line + f"|          {c:8.4f}  {b:+9.3f}")
import json
json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "veronese_local2.json"), "w"), indent=1)
print("\nwrote veronese_local2.json")
