"""rec_lambda.py - first-order behaviour of a coin gate around the uniform measure.

For the gate in LABFILE ("m k labels") and e in a list, prints at p = 1/2 + e:
    G_p, J_p, p' - 1/2,  U = G_p - c J_p + c  (c = G/(J-1) of the gate at p = 1/2),  U / e,  (p' - 1/2) / e.
lambda = dU/de at 0.  If lambda != 0 the Bellman value near 1/2 has the form
    W(1/2 + e) = c + (lambda / (J ln J)) e ln(1/|e|) + O(e)     (one-sided), with the gate and with its dual.
usage: python rec_lambda.py LABFILE
"""
import sys

import numpy as np

from tower_vi2 import coin_parts, coin_stats


def main():
    parts = open(sys.argv[1], encoding="utf-8").readline().split()
    m = int(parts[0])
    labs = [ord(ch) - 48 for ch in parts[2]]
    rows = coin_parts(m, labs)
    G0, J0, P0 = coin_stats(m, rows, [0.5])
    c = G0[0] / (J0[0] - 1)
    print("p=1/2: G %.12f J %.12f p' %.12f  c = G/(J-1) = %.12f" % (G0[0], J0[0], P0[0], c))
    es = [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 1e-6]
    for sgn in (1, -1):
        for e in es:
            p = 0.5 + sgn * e
            G, J, P = coin_stats(m, rows, [p])
            U = G[0] - c * J[0] + c
            print("e %+9.1e  G %.10f J %.10f  p'-1/2 %+.3e  U %+.3e  U/e %+.6f  (p'-1/2)/e %+.6f"
                  % (sgn * e, G[0], J[0], P[0] - 0.5, U, U / (sgn * e), (P[0] - 0.5) / (sgn * e)))


if __name__ == "__main__":
    main()
