"""Is the Veronese correction explained by the row's kurtosis along a TYPICAL direction?

The paper's mechanism: the Veronese row has kurtosis 15 and 9 along pure coordinates but a random
direction mixes Theta(d^2) coordinates, so along a typical direction the kurtosis decays to 3 - the
leading order is generic and the first correction is large because the decay is slow.

Two numbers decide whether that accounts for the SIZE.

  (1) kappa_typ(d) = E<z,u>^4 / (E<z,u>^2)^2 for u uniform on the unit sphere of Sym_d^0, and
      kappa_null(d), the same with u = A, the null direction the design itself selects.
      A is orthogonal to every FITTED row by construction, so the moments are taken on a FRESH row.
      If the two agree, a typical direction is the right reference; if kappa_null is much larger,
      the selected direction is not typical and the mechanism needs the selection in it.

  (2) the correction a given kurtosis actually buys. In the i.i.d.-coordinate family measured at
      d=14, excess(kappa)/excess(3) runs 0.85, 1.01, 1.19, 1.79 at kappa = 1, 3, 5, 9. The Veronese
      excess at d=14 is about 25 times the uniform-direction excess. A kurtosis near 4-5 buys 1.2.
      So if kappa_null is also near 4-5, kurtosis alone does not account for the size and the
      dependence between the row's coordinates - the row is rank one - is doing the work.
"""
import os, sys, time, json
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "2"
import numpy as np

BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
DS = [int(x) for x in (sys.argv[1].split(",") if len(sys.argv) > 1 else "8,10,14,20,28".split(","))]


def rows_sphere(n, d, rng):
    """<z(x), B_j> for z(x) = x x^T - I/d, x uniform on S^{d-1}, in the Sym_d^0 basis."""
    X = rng.standard_normal((n, d)); X /= np.linalg.norm(X, axis=1, keepdims=True)
    iu = np.triu_indices(d, 1)
    off = np.sqrt(2.0) * X[:, iu[0]] * X[:, iu[1]]
    S = X ** 2
    cum = np.cumsum(S, axis=1)
    j = np.arange(1, d)
    dia = (cum[:, :d - 1] - j * S[:, 1:]) / np.sqrt(j * j + j)
    return np.concatenate([off, dia], axis=1)


print(f"{'d':>4} {'m':>6} {'designs':>8} | {'kappa_typ':>10} {'kappa_null':>11} {'ratio':>7}"
      f" | {'E<z,A>^2':>10} {'E<z,u>^2':>10}", flush=True)
out = []
for d in DS:
    m = d * (d + 1) // 2 - 1
    rng = np.random.default_rng(31337 + d)
    n_typ, n_null = [], []
    v_typ, v_null = [], []
    t0 = time.time()
    ndes = 0
    while time.time() - t0 < BUDGET:
        R = rows_sphere(m - 1, d, rng)
        c = np.empty(m)
        try:
            c[:m - 1] = -np.linalg.solve(R[:, :m - 1], R[:, m - 1])
        except np.linalg.LinAlgError:
            continue
        c[m - 1] = 1.0; c /= np.linalg.norm(c)
        ndes += 1
        F = rows_sphere(400, d, rng)                 # fresh rows, independent of the design
        u = rng.standard_normal(m); u /= np.linalg.norm(u)
        pn = F @ c
        pt = F @ u
        n_null.append((float(np.mean(pn ** 4)), float(np.mean(pn ** 2))))
        n_typ.append((float(np.mean(pt ** 4)), float(np.mean(pt ** 2))))
    m4n = np.mean([a for a, b in n_null]); m2n = np.mean([b for a, b in n_null])
    m4t = np.mean([a for a, b in n_typ]); m2t = np.mean([b for a, b in n_typ])
    kn, kt = m4n / m2n ** 2, m4t / m2t ** 2
    print(f"{d:4d} {m:6d} {ndes:8d} | {kt:10.3f} {kn:11.3f} {kn/kt:7.3f} | {m2n:10.4f} {m2t:10.4f}", flush=True)
    out.append(dict(d=d, m=m, n=ndes, kappa_typ=kt, kappa_null=kn, var_null=m2n, var_typ=m2t))
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "kurtosis_null_direction.json"), "w"), indent=1)

print("\nkappa - 3 against 1/d (the paper's decay claim), both directions:")
print(f"{'d':>4} {'(kt-3)*d':>10} {'(kn-3)*d':>10}")
for r in out:
    print(f"{r['d']:4d} {(r['kappa_typ']-3)*r['d']:10.2f} {(r['kappa_null']-3)*r['d']:10.2f}")
