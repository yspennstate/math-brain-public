"""Do the negative defects found by the policy check lower the potential AT GRID NODES?

For the N gates with the most negative D in a policy JSON: re-run the policy search, turn the end points with D < 0 into
families (colgen.families_from: the solver bias is solved so that the output lands exactly on grid nodes), and evaluate
one sweep of these families against the stored potential.  A defect that is an artefact of interpolating V between
nodes gives no node below the stored value; a real improvement lowers some node.  If some node is lowered, iterate
AND/OR/XOR plus these families from the stored potential and report the change.

usage: node_test.py POT.npz POLICY.json N [tag]
"""
import os, sys, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio(4)
import policy as PO
import colgen as CG
import run_policy as RP

pot = RP.G_from(sys.argv[1])
pol = json.load(open(sys.argv[2]))
N = int(sys.argv[3])
tag = sys.argv[4] if len(sys.argv) > 4 else "x"
grid, G, C = pot.grid, pot.G, pot.C
names = [r["name"] for r in pol["rows"][:N]]
specs = set()
for nm in names:
    if nm.startswith("npn3"): specs.add("npn3")
    elif nm.startswith("npn4"): specs.add("npn4")
    elif nm.startswith("mono5"): specs.add("mono5")
    elif nm.startswith("restr"): specs.add("restr:%s" % nm[5:].split("_")[0])
    elif nm == "AND2": specs.add("and")
    elif nm == "G7": specs.add("g7")
gates = {n: t for n, t in RP.gate_list(",".join(sorted(specs)))}
fams = []
for nm in names:
    tab = gates[nm]
    k = int(round(np.log2(len(tab))))
    r = PO.check_gate(tab, k, grid, G, nstart=16)
    bad = r["D_all"] < 0
    if bad.any():
        fams.extend(CG.families_from(nm, tab, k, r["P_all"][bad], grid, D=r["D_all"][bad], window=0.5))
    print("%-12s D_min %+.4e at p_out %.6f -> %d families" % (nm, r["D"], r["pout"], len(fams)), flush=True)
Vn = G * grid.ps
Vfull = np.concatenate([Vn, Vn[1:]])
worst = 0.0
where = None
for fam in fams:
    b, arg = fam.sweep(grid, G, C)
    d = b - Vfull
    j = int(np.argmin(d))
    if d[j] < worst:
        worst = float(d[j]); where = (fam.name, float(grid.rs[j]))
print("largest lowering of a node by one sweep of the %d families: %+.3e %s" % (len(fams), worst, where), flush=True)
if worst < -1e-12:
    res = V.iterate(grid, C, families=fams, G0=G, verbose=False)
    Gn = res["G"]
    print("iterated from the stored potential with AND/OR/XOR + these families: %s after %d sweeps; V(1/2)-C %+.3e;"
          " max lowering %.3e at p = %.6f" % (res["reason"], res["it"], Gn[0] * 0.5 - C,
                                               float(np.max((G - Gn) * grid.ps)), float(grid.ps[np.argmax((G - Gn) * grid.ps)])))
