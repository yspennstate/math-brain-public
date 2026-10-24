"""Structure of the best arity-7 restriction of Numaro's g: minimal true points, influences, composition-primality
(cofactor criterion: G = F(g(x_A), x_B) for some block 2 <= |A| <= k-1 iff the cofactors over x_A take at most two
distinct functions of x_B), and an independent recomputation of c_G with gate-reformulation/bigates.spec."""
import sys, os, itertools, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "2026-09-22-gate-reformulation"))
import fgate as F
F.lowprio()
import numaro as N
import bigates, gam

g, core, hosts = N.load()
assign = ['f'] * 7 + [0, 1] + [0, 0, 0, 0, 0, 1, 1, 1, 0]
vals, free = N.restriction_table(g, assign)
k = 7
print("free coordinates", free, " true cells", int((vals < 0).sum()), "of", 1 << k)
T = [x for x in range(1 << k) if vals[x] < 0]
mins = [x for x in T if not any((y != x) and ((y & x) == y) for y in T)]
print("monotone:", all(vals[x | (1 << i)] <= vals[x] for x in range(1 << k) for i in range(k)))
print("minimal true points (as sets of inputs):", [[i for i in range(k) if (m >> i) & 1] for m in mins])
Tf = [x for x in range(1 << k) if vals[x] > 0]
maxf = [x for x in Tf if not any((y != x) and ((y & x) == x) for y in Tf)]
print("maximal false points (complement sets = minimal transversals):", [[i for i in range(k) if not (m >> i) & 1] for m in maxf])

def is_prime(vals, k):
    worst = None
    for r in range(2, k):
        for A in itertools.combinations(range(k), r):
            B = [i for i in range(k) if i not in A]
            rows = set()
            for a in range(1 << r):
                row = []
                for b in range(1 << len(B)):
                    x = 0
                    for l, i in enumerate(A):
                        x |= ((a >> l) & 1) << i
                    for l, i in enumerate(B):
                        x |= ((b >> l) & 1) << i
                    row.append(int(vals[x]))
                rows.add(tuple(row))
            if len(rows) <= 2:
                return False, A
    return True, None
print("composition-prime:", is_prime(vals, k))

pot = F.Pot(os.path.join(HERE, "..", "..", "inputs", "cert_vi_h96k40.npz"), 0.0)
res = json.load(open(os.path.join(HERE, "..", "logs", "restr_opt_h96_k2_7.json")))
row = [r for r in res if r["k"] == 7 and r["assign"] == [str(a) for a in assign]][0]
p = np.array(row["p"])
c, D, W = F.cG(vals, p[None, :], pot)
Gm = gam.Gam(os.path.join(HERE, "..", "..", "inputs", "cert_vi_h96k40.npz"), 0.0)
D2, den2, po2 = bigates.stat(vals, p, Gm)
print("fgate:   c = %.12e  D = %.12e  W = %.12e" % (c[0], D[0], W[0]))
print("bigates: c = %.12e  D = %.12e  W = %.12e  p_out = %.12f" % (-D2 / den2, D2, den2, po2))
print("biases:", ["%.10f" % x for x in p])
D0, W0, po0, It0 = F.stats(vals, p[None, :], pot)
print("It:", ["%.5f" % x for x in It0[0]], " It/V:", ["%.5f" % x for x in It0[0] / (4 * p * (1 - p))])
