"""Best moves at a target truth probability r under a saved slack function V (AND split, pair g-families, uniform-core g).
Usage: python trace_policy.py <vig npz> r [r ...]
"""
import sys
import numpy as np
from ro_gamma import Grid, E_fun
from vi_g import FAMILIES, build_family, h2
from vi_full import ef_table, solve_muc
import fast_gate as FG

d = np.load(sys.argv[1]); C = float(d["C"]); G = d["G"]; grid = Grid(int(d["M"]), int(d["K"]))
V = lambda q: grid.gamma_at(G, np.atleast_1d(np.asarray(q, dtype=float)))
A = ef_table()


def moves(r):
    out = []
    # AND split r = p q (OR is AND of complements at 1 - r)
    for rr, lab in ((r, "AND"), (1 - r, "OR")):
        ps = np.linspace(rr + 1e-6, 1 - 1e-6, 20001); qs = rr / ps; ok = qs < 1 - 1e-9
        ps, qs = ps[ok], qs[ok]
        val = qs * V(ps) + ps * V(qs) - ps * qs * E_fun(ps, qs, np.log2(1 / ps), np.log2(1 / qs))
        k = int(np.argmin(val))
        out.append((float(val[k]), "%s(p=%.6f,q=%.6f)" % (lab, ps[k], qs[k])))
    fg = np.arange(1, 512) / 512
    for nm, (K, j) in FAMILIES.items():
        fam = build_family(K, j, np.array([r]), fg)
        if len(fam["r_idx"]) == 0:
            continue
        p = fam["p"]; Vv = 4 * p * (1 - p)
        cost = (fam["It"] / Vv * (V(p.ravel()).reshape(p.shape) + h2(Vv.ravel()).reshape(p.shape))).sum(axis=1) + C * fam["Irest"] - fam["Ht"]
        k = int(np.argmin(cost))
        out.append((float(cost[k]), "g-%s K=%s p_in=%s" % (nm, K, np.array2string(p[k], precision=6))))
    for mua in (0.0,):
        m = solve_muc(A, 1 - 2 * r, mua)
        if m is not None:
            pc = (1 - m) / 2
            q = np.array([pc] * 9 + [(1 - mua) / 2] * 9)
            Ht, It, po, c = FG.evaluate(q)
            Vv = 4 * q * (1 - q)
            cost = float((It / Vv * (V(q) + h2(Vv))).sum() - Ht)
            out.append((cost, "g-uniformcore p_core=%.6f (p_out=%.6f)" % (pc, po)))
    out.sort()
    return out


for r in [float(x) for x in sys.argv[2:]]:
    print("r = %.6f: V(r) - C = %+.4e" % (r, V(r)[0] - C))
    for val, desc in moves(r)[:6]:
        print("   %+.4e  %s" % (val - C, desc))
