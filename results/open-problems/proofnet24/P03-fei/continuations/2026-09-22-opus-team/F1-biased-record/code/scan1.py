"""One biased input of g fed by a read-once formula of measure p_i, the other 17 inputs single variables.

s(F)  = (It_i/V_i)(Gamma(p_i) + h(V_i)) + C sum_{j != i} It_j - Htilde_g(p)
D     = s(F) - Gamma(p_out)            (D < 0: g lowers the slack function at p_out)
Usage: python scan1.py <gamma npz>
"""
import sys
import numpy as np
from gate import load_table, evaluate, N, h2
from ro_gamma import load_gamma

gam, C = load_gamma(sys.argv[1])
t = load_table()
print("C = %.15f" % C)
for i in (0, 9):
    rows = []
    for p in np.concatenate([np.linspace(0.01, 0.99, 99), [3 / 8, 5 / 8, 0.45, 0.55, 0.48, 0.52, 0.49, 0.51]]):
        pv = [0.5] * N; pv[i] = p
        Ht, It, po = evaluate(t, pv)
        V = 4 * p * (1 - p)
        s = It[i] / V * (gam(np.array([p]))[0] + h2(np.array([V]))[0]) + C * (It.sum() - It[i]) - Ht
        D = s - gam(np.array([po]))[0]
        rows.append((p, po, s, D))
    rows.sort()
    print("input %d:" % i)
    for p, po, s, D in rows:
        print("  p_i=%.4f  p_out=%.6f  s(F)=%.8f  Gamma(p_out)=%.8f  D=%+.3e" % (p, po, s, s - D, D))
