"""Does the FOURTH MOMENT alone fix the 1/d correction, and is the dependence affine?

Extends kurtosis_law.py with the two things that run could not settle.

  SPARSITY CONFOUND. The three-point law P(+-1/sqrt q) = q/2 has kurtosis 1/q and leaves only m/kappa
  nonzero coordinates in a row of length m. At d=14, m=104, kappa=9 leaves 11.6 and kappa=15 leaves
  6.9 - the row stops being a typical direction and the excess explodes (kappa=15 sat 11 to 18
  standard errors off the affine fit while kappa<=9 sat within 3). Running the same kappa at larger m
  separates a fourth-moment effect from a sparsity effect: if the curvature is sparsity it flattens
  as m grows at fixed kappa, and if it is the fourth moment it does not.

  SUFFICIENCY AT MORE THAN ONE POINT. That run compared a three-point law with the Gaussian at
  kappa = 3 only. Here three pairs of laws are matched on their fourth moment and on nothing else:
  uniform vs three-point at kappa = 1.8, Gaussian vs three-point at 3, Laplace vs three-point at 6.
  If the excesses agree within each pair, the correction is a functional of the first four moments.
"""
import os, sys, time, json
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

KS = (2, 3, 4, 5)
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}
D = int(sys.argv[1]) if len(sys.argv) > 1 else 24
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0


def r_threepoint(n, m, kap, rng):
    q = 1.0 / kap
    return (np.where(rng.random((n, m)) < q, 1.0, 0.0)
            * np.where(rng.random((n, m)) < 0.5, -1.0, 1.0)) / np.sqrt(q)


def r_gauss(n, m, kap, rng):
    return rng.standard_normal((n, m))


def r_uniform(n, m, kap, rng):                      # kurtosis 9/5 = 1.8
    return rng.uniform(-np.sqrt(3.0), np.sqrt(3.0), (n, m))


def r_laplace(n, m, kap, rng):                      # kurtosis 6
    return rng.laplace(0.0, 1 / np.sqrt(2.0), (n, m))


def to_matrix(c, d):
    iu = np.triu_indices(d, 1)
    n_off = len(iu[0])
    A = np.zeros((d, d))
    A[iu] = c[:n_off] / np.sqrt(2.0)
    A = A + A.T
    jj = np.arange(1, d)
    w = c[n_off:] / np.sqrt(jj * jj + jj)
    diag = np.zeros(d)
    for idx, j in enumerate(jj):
        diag[:j] += w[idx]; diag[j] -= j * w[idx]
    A[np.diag_indices(d)] = diag
    return A


def sweep(d, gen, kap, budget, rng):
    m = d * (d + 1) // 2 - 1
    acc = {k: [] for k in KS}
    t0 = time.time()
    while time.time() - t0 < budget:
        R = gen(m - 1, m, kap, rng)
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


rng = np.random.default_rng(90915)
m = D * (D + 1) // 2 - 1
print(f"d = {D}, m = {m}, {BUDGET:.0f}s per arm\n")
arms = [("uniform", r_uniform, 1.8), ("3pt", r_threepoint, 1.8),
        ("gauss", r_gauss, 3.0), ("3pt", r_threepoint, 3.0),
        ("laplace", r_laplace, 6.0), ("3pt", r_threepoint, 6.0),
        ("3pt", r_threepoint, 1.0), ("3pt", r_threepoint, 2.0),
        ("3pt", r_threepoint, 5.0), ("3pt", r_threepoint, 9.0)]
res = []
print(f"{'law':>9} {'kappa':>6} {'nonzero/row':>12} {'designs':>8} | " +
      " ".join(f"m{2*k}-C{k}".rjust(13) for k in KS))
for name, gen, kap in arms:
    out, n = sweep(D, gen, kap, BUDGET, rng)
    nz = m / kap if name == "3pt" else m
    res.append(dict(name=name, kappa=kap, n=n, nz=nz,
                    **{f"e{k}": out[k][0] - CAT[k] for k in KS},
                    **{f"se{k}": out[k][1] for k in KS}))
    print(f"{name:>9} {kap:6.1f} {nz:12.1f} {n:8d} | " +
          " ".join(f"{out[k][0]-CAT[k]:8.4f}+-{out[k][1]:.4f}".rjust(13) for k in KS), flush=True)
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"kurtosis_law2_d{D}.json"), "w"), indent=1)

print("\n-- fourth-moment sufficiency: matched pairs, same kappa, different law --")
for kap, a, b in ((1.8, "uniform", "3pt"), (3.0, "gauss", "3pt"), (6.0, "laplace", "3pt")):
    ra = [r for r in res if r["name"] == a and r["kappa"] == kap][0]
    rb = [r for r in res if r["name"] == b and r["kappa"] == kap][0]
    print(f"   kappa={kap}: {a} vs {b}")
    for k in KS:
        d_ = rb[f"e{k}"] - ra[f"e{k}"]; se = np.hypot(ra[f"se{k}"], rb[f"se{k}"])
        print(f"      k={k}: {ra[f'e{k}']:+9.5f} vs {rb[f'e{k}']:+9.5f}   diff {d_:+9.5f} +- {se:.5f}"
              f"  ({abs(d_)/se if se else 0:4.1f} s.e.)")

print("\n-- affine in kappa?  three-point arms only, and with the sparsest dropped --")
tp = sorted([r for r in res if r["name"] == "3pt"], key=lambda r: r["kappa"])
for lab, sub in (("all", tp), ("nonzero/row > 25", [r for r in tp if r["nz"] > 25])):
    x = np.array([r["kappa"] for r in sub])
    if len(x) < 3:
        continue
    print(f"   [{lab}]  kappa = " + " ".join(f"{v:g}" for v in x))
    for k in KS:
        y = np.array([r[f"e{k}"] for r in sub]); w = 1 / np.array([r[f"se{k}"] for r in sub]) ** 2
        X = np.vstack([np.ones_like(x), x]).T; sw = np.sqrt(w)
        bb, *_ = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)
        r_ = (y - X @ bb) / np.array([r[f"se{k}"] for r in sub])
        print(f"      k={k}: a={bb[0]:+9.5f} b={bb[1]:+9.5f} chi2={float((w*(y-X@bb)**2).sum()):8.1f}/{len(x)-2}"
              f"  resid= " + " ".join(f"{v:+5.1f}" for v in r_))
