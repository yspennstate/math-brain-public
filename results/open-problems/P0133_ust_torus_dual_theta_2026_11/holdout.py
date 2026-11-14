"""Out-of-sample test of the shape polynomial of shape_fit.py.

Fits log w as a polynomial of total degree --deg in (e1, e3) on the training files (log Z free per modulus), then on
each test file keeps that w fixed and fits only its own log Z. Prints chi2/dof on the test cells and the worst test
residuals in standard errors.
Usage: python holdout.py [--min 200] [--deg 3] train1 train2 ... -- test1 test2 ..."""
import math
import sys

import numpy as np

from mesh_table import angles, load


def cells(fn, mn):
    (n1, n2, s), cnt, tot = load(fn)
    tau = complex(s, n2) / n1
    out = []
    for k, c in cnt.items():
        if k == "fig8" or c < mn:
            continue
        ct = [1.0 / math.tan(math.radians(t)) for t in angles(k, tau)]
        Q = sum(abs(x + y * tau) ** 2 for x, y in k) / tau.imag
        out.append((math.log(c / tot), math.sqrt(c), sum(ct), ct[0] * ct[1] * ct[2], Q, k))
    return out


def design(rows, mons):
    return np.array([[e1 ** p1 * e3 ** p3 for p1, p3 in mons] for _, _, e1, e3, _, _ in rows])


def main():
    args = sys.argv[1:]
    mn, deg = 200, 3
    while args and args[0] in ("--min", "--deg"):
        if args[0] == "--min":
            mn = int(args[1])
        else:
            deg = int(args[1])
        args = args[2:]
    cut = args.index("--")
    train, test = args[:cut], args[cut + 1:]
    mons = [(i, d - i) for d in range(1, deg + 1) for i in range(d, -1, -1)]
    tr = [cells(f, mn) for f in train]
    rows = [r for c in tr for r in c]
    Z = np.zeros((len(rows), len(train)))
    j = 0
    for i, c in enumerate(tr):
        Z[j:j + len(c), i] = -1.0
        j += len(c)
    A = np.hstack([design(rows, mons), Z])
    y = np.array([r[0] for r in rows])
    w = np.array([r[1] for r in rows])
    sol, *_ = np.linalg.lstsq(A * w[:, None], y * w, rcond=None)
    res = (y - A @ sol) * w
    print(f"train: cells {len(rows)}  files {len(train)}  chi2/dof {float(res @ res) / (len(rows) - A.shape[1]):.2f}")
    coef = sol[:len(mons)]
    tot_chi, tot_dof, worst = 0.0, 0, []
    for fn in test:
        c = cells(fn, mn)
        if len(c) < 2:
            continue
        f = design(c, mons) @ coef
        yy = np.array([r[0] for r in c])
        ww = np.array([r[1] for r in c])
        logZ = float(np.sum(ww ** 2 * (f - yy)) / np.sum(ww ** 2))
        rr = (yy - f + logZ) * ww
        tot_chi += float(rr @ rr)
        tot_dof += len(c) - 1
        print(f"  test {fn}: cells {len(c)}  chi2/dof {float(rr @ rr) / (len(c) - 1):.2f}")
        worst += [(abs(v), v, fn, r[4], math.exp(r[0])) for v, r in zip(rr, c)]
    print(f"test total: chi2/dof {tot_chi / max(tot_dof, 1):.2f}  (dof {tot_dof})")
    for _, v, fn, Q, P in sorted(worst, reverse=True)[:10]:
        print(f"  {v:+6.2f} se  Q {Q:.3f}  P {P:.5f}  {fn}")


if __name__ == "__main__":
    main()
