"""Closed-form candidates for the superbase weight: log P_tau(S) = sum_j a_j f_j(shape(S)) - log Z(tau), log Z free.

Each candidate is a short list of shape features (Q = sum |v|^2 / Im tau = 2 sum cot, angles A <= B <= C of the
triangle). Prints chi2/dof per candidate with its coefficients, so a two- or three-term form can be set against the
cubic of shape_fit.py. Usage: python cand_fit.py [--min 200] files..."""
import math
import sys

import numpy as np

from mesh_table import angles, load

FEATS = {
    "Q": lambda Q, a: Q,
    "logQ": lambda Q, a: math.log(Q),
    "1/Q": lambda Q, a: 1.0 / Q,
    "Q^2": lambda Q, a: Q * Q,
    "logsin": lambda Q, a: sum(math.log(math.sin(math.radians(t))) for t in a),
    "e3": lambda Q, a: math.prod(1.0 / math.tan(math.radians(t)) for t in a),
    "cotC": lambda Q, a: 1.0 / math.tan(math.radians(a[2])),
    "cotA": lambda Q, a: 1.0 / math.tan(math.radians(a[0])),
    "logA": lambda Q, a: math.log(math.radians(a[0])),
}
# features summed over the three sides, L_i = |v_i|^2 / Im tau (a product form w = prod_i g(L_i))
SIDE = {
    "SlogL": lambda L: sum(math.log(x) for x in L),
    "SL2": lambda L: sum(x * x for x in L),
    "S1/L": lambda L: sum(1.0 / x for x in L),
    "SsqrtL": lambda L: sum(math.sqrt(x) for x in L),
    "SL3": lambda L: sum(x ** 3 for x in L),
    "Lmax": lambda L: L[2],
    "logLmax": lambda L: math.log(L[2]),
}
CANDS = [["Q"], ["Q", "logQ"], ["Q", "1/Q"], ["Q", "Q^2"], ["Q", "logsin"], ["Q", "e3"], ["Q", "cotC"],
         ["Q", "cotA"], ["Q", "logA"], ["Q", "logQ", "logsin"], ["Q", "cotA", "cotC"], ["Q", "logA", "cotC"],
         ["Q", "SlogL"], ["Q", "SlogL", "SL2"], ["Q", "SlogL", "S1/L"], ["Q", "SlogL", "SsqrtL"],
         ["Q", "SL2", "SL3"], ["Q", "SlogL", "SL2", "S1/L"], ["Q", "logQ", "SlogL", "SL2"],
         ["Q", "Lmax"], ["Q", "logLmax"], ["Q", "logQ", "logLmax"], ["Q", "SlogL", "logLmax"]]


def main():
    args = sys.argv[1:]
    mn = 200
    if args and args[0] == "--min":
        mn, args = int(args[1]), args[2:]
    rows = []
    for fn in args:
        (n1, n2, s), cnt, tot = load(fn)
        tau = complex(s, n2) / n1
        for k, c in cnt.items():
            if k == "fig8" or c < mn:
                continue
            Q = sum(abs(x + y * tau) ** 2 for x, y in k) / tau.imag
            L = sorted(abs(x + y * tau) ** 2 / tau.imag for x, y in k)
            rows.append((fn, Q, angles(k, tau), math.log(c / tot), math.sqrt(c), L))
    files = sorted({r[0] for r in rows})
    fi = {f: i for i, f in enumerate(files)}
    y = np.array([r[3] for r in rows])
    w = np.array([r[4] for r in rows])
    Z = np.zeros((len(rows), len(files)))
    for j, r in enumerate(rows):
        Z[j, fi[r[0]]] = -1.0
    print(f"cells {len(rows)}  files {len(files)}")
    for cand in CANDS:
        F = np.array([[FEATS[f](r[1], r[2]) if f in FEATS else SIDE[f](r[5]) for f in cand] for r in rows])
        A = np.hstack([F, Z])
        sol, *_ = np.linalg.lstsq(A * w[:, None], y * w, rcond=None)
        res = (y - A @ sol) * w
        dof = len(rows) - A.shape[1]
        print(f"  {'+'.join(cand):18s} chi2/dof {float(res @ res) / dof:8.2f}  "
              + " ".join(f"{f}={sol[i]:+.4f}" for i, f in enumerate(cand)))


if __name__ == "__main__":
    main()
