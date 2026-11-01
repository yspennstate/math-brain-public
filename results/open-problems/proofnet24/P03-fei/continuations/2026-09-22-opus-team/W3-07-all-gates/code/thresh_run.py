"""Bracket the FEI constant of read-once formulas over AND/OR/NOT/XOR plus a gate set by column-generation value
iteration at a list of constants C.

usage: thresh_run.py SET tag C1,C2,... [rounds] [thr] [fine]
  fine = 'fine' uses the grid with an extra step-2^-13 block on [0.44, 1/2]
"""
import os, sys, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio(4)
import colgen as CG
import run_policy as RP

spec = sys.argv[1]
tag = sys.argv[2]
Cs = [float(x) for x in sys.argv[3].split(",")]
rounds = int(sys.argv[4]) if len(sys.argv) > 4 else 6
thr = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-6
fine = len(sys.argv) > 6 and sys.argv[6] == "fine"
warm = sys.argv[7] if len(sys.argv) > 7 else os.environ.get("W307_WARM", "")
grid = V.Grid(fine=(0.44, 2.0 ** -13)) if fine else V.Grid()
gates = RP.gate_list(spec) if spec != "none" else []
print("set %s: %d gates; grid %d nodes" % (spec, len(gates), grid.N), flush=True)
summary = []
for C in Cs:
    t0 = time.time()
    G0 = None
    if warm:
        dw = np.load(warm)
        if abs(float(dw["C"]) - C) < 1e-15 and len(dw["G"]) == grid.N:
            G0 = np.asarray(dw["G"], float)
            print("warm start from %s" % warm, flush=True)
    res, fams, hist = CG.run(C, gates, grid, "%s C=%.9f" % (tag, C), rounds=rounds, thr=thr,
                             log=lambda s: print(s, flush=True), G0=G0)
    G = res["G"]
    row = dict(C=C, result=res["reason"], nfam=len(fams), rounds=hist, V_half_minus_C=float(G[0] * 0.5 - C),
               minV=float((G * grid.ps).min()),
               shape={str(p): float(grid.V(G, p)[0] - C) for p in (0.5, 0.4999, 0.4995, 0.499, 0.498, 0.495, 0.49, 0.485,
                                                                   0.48, 0.47, 0.45, 0.4)},
               secs=time.time() - t0)
    summary.append(row)
    np.savez(os.path.join(HERE, "..", "logs", "fp_%s_C%.9f.npz" % (tag, C)), xs=grid.xs, G=G, C=C, M=grid.M, K=grid.K)
    print("RESULT %s C=%.9f: %s  V(1/2)-C %+.3e  min V %.3e  families %d  (%.0f s)" % (tag, C, res["reason"],
          row["V_half_minus_C"], row["minV"], len(fams), row["secs"]), flush=True)
    print("   V - C near 1/2: " + "  ".join("%s:%+.2e" % (k, v) for k, v in row["shape"].items()), flush=True)
json.dump(summary, open(os.path.join(HERE, "..", "logs", "thresh_%s.json" % tag), "w"), indent=1)
