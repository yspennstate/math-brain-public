"""Positive control for the policy check: raise F1's g-fixed point V_g (C_rec) by a bump of height b on [0.494, 0.4985]
(and its mirror) and check that the search finds the arity-10 restrictions and G7 violating the bumped potential,
while the unbumped potential gives D >= -1e-10 for the same gates."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio(4)
import policy as PO
import run_policy as RP
pot = RP.G_from(os.path.join(HERE, "..", "..", "F1-biased-record", "logs", "vig_all10_Crec.npz"))
grid, G = pot.grid, pot.G
gates = [g for g in RP.gate_list("restr:10") if g[0] in ("restr10_20", "restr10_0", "restr10_15")] + RP.gate_list("g7")
for b in (0.0, 0.002, 0.01):
    Gb = G.copy()
    m = (grid.ps >= 0.494) & (grid.ps <= 0.4985)
    Gb[m] = G[m] + b / grid.ps[m]
    for name, tab in gates:
        k = int(round(np.log2(len(tab))))
        r = PO.check_gate(tab, k, grid, Gb, nstart=8, maxsub=2)
        print("bump %.3f  %-11s  D_min %+.4e at p_out %.5f" % (b, name, r["D"], r["pout"]), flush=True)
