"""Fit the superbase law as P_tau(S) = w(shape(S)) / Z(tau).

Each superbase S of the torus with modulus tau spans a triangle. Its shape determines the lattice up to similarity, so
with w free (--deg 0) the fit only tests conformal invariance (cells of PSL2(Z)-equivalent moduli must agree). With
--deg k, log w is a polynomial of total degree k in e1 = cot A + cot B + cot C (= Q / 2) and e3 = cot A cot B cot C
(with cot A cot B + cot B cot C + cot C cot A = 1 these two fix the shape), and log Z(tau) is free per modulus.
Weighted least squares over every (file, superbase) cell with at least --min counts; prints chi2, the coefficients and
the worst residuals in standard errors.
Usage: python shape_fit.py [--min 200] [--deg k] files...   (plain or .gz tsv from ust_metal / ust_torus_shear.py)"""
import math
import sys
from collections import defaultdict

import numpy as np

from mesh_table import angles, load


def main():
    args = sys.argv[1:]
    mn, deg = 200, 0
    while args and args[0] in ("--min", "--deg"):
        if args[0] == "--min":
            mn = int(args[1])
        else:
            deg = int(args[1])
        args = args[2:]
    pooled = {}
    for fn in args:
        meta, cnt, tot = load(fn)
        if meta in pooled:
            pooled[meta][0].update(cnt)
            pooled[meta][1] += tot
        else:
            pooled[meta] = [cnt, tot]
    rows = []  # (tau key, shape key, logP, var, Q, meta)
    for meta, (cnt, tot) in pooled.items():
        n1, n2, s = meta
        tau = complex(s, n2) / n1
        tk = (round(tau.real, 4), round(tau.imag, 4))
        for k, c in cnt.items():
            if k == "fig8" or c < mn:
                continue
            a = angles(k, tau)
            sk = (round(a[0], 1), round(a[1], 1))
            Q = sum(abs(x + y * tau) ** 2 for x, y in k) / tau.imag
            ct = [1.0 / math.tan(math.radians(t)) for t in a]
            rows.append((tk, sk, math.log(c / tot), 1.0 / c, Q, meta, (ct[0] + ct[1] + ct[2], ct[0] * ct[1] * ct[2])))
    taus = sorted({r[0] for r in rows})
    shapes = sorted({r[1] for r in rows})
    ti = {t: i for i, t in enumerate(taus)}
    si = {s: i for i, s in enumerate(shapes)}
    nt, ns = len(taus), len(shapes)
    mons = [(i, d - i) for d in range(1, deg + 1) for i in range(d, -1, -1)]
    nw = ns if deg == 0 else len(mons)
    A = np.zeros((len(rows), nw + nt))
    y = np.zeros(len(rows))
    w = np.zeros(len(rows))
    for j, r in enumerate(rows):
        if deg == 0:
            A[j, si[r[1]]] = 1.0
        else:
            e1, e3 = r[6]
            for m, (p1, p3) in enumerate(mons):
                A[j, m] = e1 ** p1 * e3 ** p3
        A[j, nw + ti[r[0]]] = -1.0
        y[j] = r[2]
        w[j] = 1.0 / math.sqrt(r[3])
    if deg == 0:
        A = A[:, [c for c in range(nw + nt) if c != nw]]  # tau 0 fixes the gauge
    sol, *_ = np.linalg.lstsq(A * w[:, None], y * w, rcond=None)
    res = (y - A @ sol) * w
    dof = len(rows) - A.shape[1]
    chi2 = float(res @ res)
    print(f"cells {len(rows)}  moduli {nt}  shapes {ns}  dof {dof}  chi2 {chi2:.1f}  chi2/dof {chi2 / max(dof, 1):.2f}")
    print("shapes seen at more than one modulus:",
          sum(1 for s in shapes if len({r[0] for r in rows if r[1] == s}) > 1))
    order = np.argsort(-np.abs(res))
    print("worst residuals (se):")
    for j in order[:15]:
        r = rows[j]
        print(f"  {res[j]:+6.2f}  tau {r[0]}  shape {r[1]}  Q {r[4]:.3f}  P {math.exp(r[2]):.5f}  mesh {r[5]}")
    if deg > 0:
        print("log w = " + " ".join(f"{sol[m]:+.5f} e1^{p1} e3^{p3}" for m, (p1, p3) in enumerate(mons)))
        return
    print("log w by shape (gauge: first modulus), with Q at the first modulus it appears:")
    for s in shapes:
        qs = [r[4] for r in rows if r[1] == s]
        print(f"  {s}  log w {sol[si[s]]:+8.4f}  moduli {len({r[0] for r in rows if r[1] == s})}  Q {min(qs):.3f}")


if __name__ == "__main__":
    main()
