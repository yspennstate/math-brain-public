"""Is the 1/d correction to the semicircle moments a linear function of the row's fourth moment?

The paper explains the large first correction by the kurtosis of the Veronese row along a typical
direction (15 and 9 along pure coordinates, decaying to 3 like a random direction mixes Theta(d^2)
coordinates). That is a mechanism, not a law. This tests the law.

Model: the rows are vectors in R^m with i.i.d. coordinates, mean 0, variance 1, kurtosis kappa;
A is the un-vectorization into Sym_d^0 of the unit normal to m-1 of them. At kappa = 3 with Gaussian
coordinates the normal is exactly uniform, so A is a Frobenius-normalized traceless GOE matrix and
the moments are Catalan + O(1/d) with the generic constant. Sweeping kappa asks two questions:

  (a) is  d^{k-1} Tr(A^{2k}) - C_k  affine in kappa at fixed d?
  (b) does kappa alone decide it - i.e. does a THREE-POINT law at kappa = 3, which is not Gaussian,
      give the same answer as the Gaussian?

(b) is the sharp one. If a non-Gaussian law with the Gaussian's fourth moment lands on the Gaussian
answer, the correction is a fourth-moment functional and the Veronese's excess is predicted by its
own typical-direction kurtosis alone. If it does not, the correction sees more than four moments.

The three-point law P(+-1/sqrt q) = q/2, P(0) = 1-q has mean 0, variance 1 and kurtosis 1/q, so one
dial covers kappa in [1, infinity): q = 1 is Rademacher (kappa 1), q = 1/3 gives kappa 3, and so on.
"""
import os, sys, time, json
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

KS = (2, 3, 4, 5)
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}
D = int(sys.argv[1]) if len(sys.argv) > 1 else 16
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 90.0


def rows_threepoint(n, m, kappa, rng):
    q = 1.0 / kappa
    U = rng.random((n, m))
    S = np.where(U < q, 1.0, 0.0) * np.where(rng.random((n, m)) < 0.5, -1.0, 1.0)
    return S / np.sqrt(q)


def rows_gauss(n, m, kappa, rng):
    return rng.standard_normal((n, m))


def to_matrix(c, d):
    iu = np.triu_indices(d, 1)
    n_off = len(iu[0])
    A = np.zeros((d, d))
    A[iu] = c[:n_off] / np.sqrt(2.0)
    A = A + A.T
    w = c[n_off:] / np.sqrt(np.arange(1, d) ** 2 + np.arange(1, d))
    diag = np.zeros(d)
    for idx, jj in enumerate(np.arange(1, d)):
        diag[:jj] += w[idx]; diag[jj] -= jj * w[idx]
    A[np.diag_indices(d)] = diag
    return A


def sweep(d, gen, kappa, budget, rng):
    m = d * (d + 1) // 2 - 1
    acc = {k: [] for k in KS}
    t0 = time.time()
    while time.time() - t0 < budget:
        R = gen(m - 1, m, kappa, rng)
        c = np.empty(m)
        try:
            c[:m - 1] = -np.linalg.solve(R[:, :m - 1], R[:, m - 1])
        except np.linalg.LinAlgError:
            continue
        c[m - 1] = 1.0
        c /= np.linalg.norm(c)
        A = to_matrix(c, d); A /= np.linalg.norm(A, "fro")
        w = np.linalg.eigvalsh(A)
        for k in KS:
            acc[k].append(d ** (k - 1) * float(np.sum(w ** (2 * k))))
    n = len(acc[2])
    return {k: (float(np.mean(acc[k])), float(np.std(acc[k]) / np.sqrt(max(n, 1)))) for k in KS}, n


rng = np.random.default_rng(20260915)
print(f"d = {D},  m = {D*(D+1)//2 - 1},  {BUDGET:.0f}s per arm\n")
arms = [("gauss", rows_gauss, 3.0)] + [(f"3pt k={k:g}", rows_threepoint, float(k)) for k in (1, 2, 3, 5, 9, 15)]
res = []
print(f"{'row law':>10} {'kappa':>6} {'designs':>8} | " + " ".join(f"m{2*k}-C{k}".rjust(11) for k in KS))
for name, gen, kap in arms:
    out, n = sweep(D, gen, kap, BUDGET, rng)
    res.append(dict(name=name, kappa=kap, n=n, **{f"e{k}": out[k][0] - CAT[k] for k in KS},
                    **{f"se{k}": out[k][1] for k in KS}))
    print(f"{name:>10} {kap:6.1f} {n:8d} | " +
          " ".join(f"{out[k][0]-CAT[k]:7.3f}+-{out[k][1]:.3f}".rjust(11) for k in KS), flush=True)

print("\n(a) affine in kappa?  least squares  excess = a + b*kappa  on the three-point arms only")
tp = [r for r in res if r["name"].startswith("3pt")]
x = np.array([r["kappa"] for r in tp])
for k in KS:
    y = np.array([r[f"e{k}"] for r in tp]); w = 1.0 / np.array([r[f"se{k}"] for r in tp]) ** 2
    Xd = np.vstack([np.ones_like(x), x]).T
    b, *_ = np.linalg.lstsq(Xd * np.sqrt(w)[:, None], y * np.sqrt(w), rcond=None)
    pred = Xd @ b
    chi2 = float((w * (y - pred) ** 2).sum())
    print(f"   k={k}: excess = {b[0]:+8.4f} {b[1]:+8.4f}*kappa    chi2 = {chi2:8.1f} on {len(x)-2} dof"
          f"   (zero-excess kappa = {-b[0]/b[1]:6.2f})")

print("\n(b) does kappa alone decide it?  Gaussian vs three-point at the SAME kappa = 3")
g = [r for r in res if r["name"] == "gauss"][0]
t3 = [r for r in res if r["name"] == "3pt k=3"][0]
for k in KS:
    diff = t3[f"e{k}"] - g[f"e{k}"]; se = np.hypot(t3[f"se{k}"], g[f"se{k}"])
    print(f"   k={k}: three-point {t3[f'e{k}']:+8.4f}   gauss {g[f'e{k}']:+8.4f}   "
          f"difference {diff:+8.4f} +- {se:.4f}  ({abs(diff)/se:5.1f} s.e.)")
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"kurtosis_law_d{D}.json"), "w"), indent=1)
