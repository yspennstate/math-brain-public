"""At the weights where alon_search.py found its smallest ratios, print the graph and the bottom of both spectra.

A bottom eigenvalue of L(G, sigma) of multiplicity > 1 at the minimiser means the matching state rho of
Proposition 1 (N4_PROOF.md) can be mixed there.
usage: extremal_spectra.py file.tsv [rows]
"""
import sys
import numpy as np
from alon_search import edge_ops


def main():
    rows = []
    for line in open(sys.argv[1], encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 6:
            continue
        rows.append((float(p[3]), int(p[0]), p[1], p[2], np.array([float(v) for v in p[5].split()])))
    rows.sort(key=lambda r: r[0])
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for ratio, n, tau, sig, w in rows[:k]:
        At, edges, _, _ = edge_ops(tuple(int(c) for c in tau))
        As, _, _, _ = edge_ops(tuple(int(c) for c in sig))
        et = np.linalg.eigvalsh(np.tensordot(w, At, axes=1))
        es = np.linalg.eigvalsh(np.tensordot(w, As, axes=1))
        g = " ".join("%d%d:%.3f" % (e[0], e[1], v) for e, v in zip(edges, w) if v > 2e-3)
        mt = int((et < et[0] + 1e-4 * max(1.0, es[-1])).sum())
        ms = int((es < es[0] + 1e-4 * max(1.0, es[-1])).sum())
        print("n=%d tau=%s sigma=%s ratio=%.6f" % (n, tau, sig, ratio))
        print("  edges: " + g)
        print("  tau   bottom: %s  (multiplicity %d of %d)" % (" ".join("%.4f" % v for v in et[:5]), mt, len(et)))
        print("  sigma bottom: %s  (multiplicity %d of %d)" % (" ".join("%.4f" % v for v in es[:5]), ms, len(es)))


if __name__ == "__main__":
    main()
