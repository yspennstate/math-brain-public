"""Same kurtosis, different dependence: the direct test of what sets the 1/d correction.

The Veronese row and an i.i.d.-coordinate row are matched on their kurtosis along a typical
direction and on nothing else. The Gaussian Veronese row has kurtosis exactly 3 + 12 Tr(U^4), so
3 + 24/d along a typical direction; the three-point law with q = 1/kappa is then set to that same
kappa. If the fourth moment decided the correction the two arms would agree. The measured Veronese
excess at d=14 is about 0.50 at k=2 and the i.i.d. arm's is about 0.019, so they should differ by
more than twenty fold if dependence is what matters.

A third arm sweeps the RANK: rows (X X^T - r I)/sqrt(2r) with X a d x r Gaussian matrix are a sum of
r independent rank-one forms, so their kurtosis along U is 3 + 12 Tr(U^4)/r exactly, and r = 1 is the
Veronese. That gives the correction as a function of a dependence dial with the kurtosis moving in a
known way, which is what a derivation of the constant would have to reproduce.
"""
import os, sys, time, json
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

KS = (2, 3, 4, 5)
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}
D = int(sys.argv[1]) if len(sys.argv) > 1 else 14
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
P = D * (D + 1) // 2                      # full Sym_d, the Gaussian construction's ambient space


def basis_full(d):
    """Orthonormal basis of Sym_d: off-diagonals (E_ab+E_ba)/sqrt2 then the diagonal E_aa."""
    iu = np.triu_indices(d, 1)
    return iu


def rows_wishart(n, d, r, rng):
    """<(XX^T - rI)/sqrt(2r), B_j> for X a d x r Gaussian; r=1 is the Veronese row (xx^T - I)/sqrt2."""
    X = rng.standard_normal((n, d, r))
    W = np.einsum("idr,ier->ide", X, X)
    iu = np.triu_indices(d, 1)
    off = np.sqrt(2.0) * W[:, iu[0], iu[1]]
    dia = np.einsum("idd->id", W) - r
    return np.concatenate([off, dia], axis=1) / np.sqrt(2.0 * r)


def rows_iid(n, m, kappa, rng):
    q = 1.0 / kappa
    return (np.where(rng.random((n, m)) < q, 1.0, 0.0)
            * np.where(rng.random((n, m)) < 0.5, -1.0, 1.0)) / np.sqrt(q)


def to_matrix_full(c, d):
    iu = np.triu_indices(d, 1); n_off = len(iu[0])
    A = np.zeros((d, d))
    A[iu] = c[:n_off] / np.sqrt(2.0)
    A = A + A.T
    A[np.diag_indices(d)] = c[n_off:]
    return A


def moments(gen, dim, budget, rng, **kw):
    d = dim
    acc = {k: [] for k in KS}
    t0 = time.time()
    while time.time() - t0 < budget:
        R = gen(P - 1, rng=rng, **kw)
        c = np.empty(P)
        try:
            c[:P - 1] = -np.linalg.solve(R[:, :P - 1], R[:, P - 1])
        except np.linalg.LinAlgError:
            continue
        c[P - 1] = 1.0; c /= np.linalg.norm(c)
        A = to_matrix_full(c, d); A /= np.linalg.norm(A, "fro")
        w = np.linalg.eigvalsh(A)
        for k in KS:
            acc[k].append(d ** (k - 1) * float(np.sum(w ** (2 * k))))
    n = len(acc[2])
    return {k: (float(np.mean(acc[k])), float(np.std(acc[k]) / np.sqrt(max(n, 1)))) for k in KS}, n


rng = np.random.default_rng(606060)
kap_typ = 3.0 + 24.0 / D
print(f"d = {D}, p = {P}.  kurtosis of the rank-1 (Veronese) row along a typical direction = 3 + 24/d "
      f"= {kap_typ:.3f}\n")
arms = [("veronese r=1", rows_wishart, dict(d=D, r=1)),
        ("iid kappa-matched", rows_iid, dict(m=P, kappa=kap_typ)),
        ("iid gaussian-kurt", rows_iid, dict(m=P, kappa=3.0)),
        ("wishart r=2", rows_wishart, dict(d=D, r=2)),
        ("wishart r=4", rows_wishart, dict(d=D, r=4)),
        ("wishart r=8", rows_wishart, dict(d=D, r=8))]
res = []
print(f"{'arm':>19} {'kurt(typ)':>10} {'designs':>8} | " + " ".join(f"m{2*k}-C{k}".rjust(14) for k in KS))
for name, gen, kw in arms:
    out, n = moments(gen, D, BUDGET, rng, **kw)
    kt = kap_typ if name.startswith("veronese") else (
         kw.get("kappa") if "kappa" in kw else 3.0 + 24.0 / D / kw["r"])
    res.append(dict(name=name, kurt=kt, n=n, **{f"e{k}": out[k][0] - CAT[k] for k in KS},
                    **{f"se{k}": out[k][1] for k in KS}))
    print(f"{name:>19} {kt:10.3f} {n:8d} | " +
          " ".join(f"{out[k][0]-CAT[k]:8.4f}+-{out[k][1]:.4f}".rjust(14) for k in KS), flush=True)
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     f"matched_kurtosis_d{D}.json"), "w"), indent=1)

v = res[0]; m_ = res[1]
print(f"\nmatched on kurtosis {kap_typ:.3f}, differing only in dependence:")
for k in KS:
    print(f"   k={k}: rank-one {v[f'e{k}']:+9.4f}   i.i.d. {m_[f'e{k}']:+9.4f}   "
          f"ratio {v[f'e{k}']/m_[f'e{k}']:7.2f}")
print("\nrank sweep - kurtosis falls as 3 + 24/(d r); does the excess follow?")
print(f"{'r':>3} {'kurt':>8} {'excess k=2':>12} {'x rank-1':>9}")
for name, r_ in (("veronese r=1", 1), ("wishart r=2", 2), ("wishart r=4", 4), ("wishart r=8", 8)):
    row = [x for x in res if x["name"] == name]
    if row:
        print(f"{r_:3d} {3+24/D/r_:8.3f} {row[0]['e2']:12.4f} {row[0]['e2']/v['e2']:9.3f}")
