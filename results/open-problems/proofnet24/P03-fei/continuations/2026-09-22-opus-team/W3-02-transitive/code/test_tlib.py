"""Self-test of tlib: orbit-sum evaluation against the direct Walsh transform, orbit counts."""
import sys, time
import numpy as np
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tlib
tlib.setup_process()
rng = np.random.default_rng(1)

cases = []
for n in (5, 6, 7, 8, 9, 10):
    cases.append(("Z%d" % n, tlib.cyclic_gens(n), n))
cases.append(("D8", tlib.dihedral_gens(8), 8))
for m in (4, 5):
    g, n, _ = tlib.graph_gens(m)
    cases.append(("K%d" % m, g, n))
g, n = tlib.bipartite_gens(3, 3); cases.append(("K33", g, n))
g, n = tlib.bipartite_gens(3, 4); cases.append(("K34", g, n))
g, n = tlib.wreath_gens(2, 4); cases.append(("S2wrS4", g, n))
g, n = tlib.wreath_gens(3, 3); cases.append(("S3wrS3", g, n))
cases.append(("AGL1_7", tlib.affine_line_gens(7), 7))
cases.append(("Z2^3", tlib.translations_F2(3), 8))
g, n, _ = tlib.hypergraph3_gens(5); cases.append(("H3_5", g, n))
for name, gens, n in cases:
    t0 = time.time()
    V = tlib.InvariantSpace(gens, n, name)
    errs = []
    for trial in range(5):
        F = rng.choice([-1.0, 1.0], size=V.k)
        f = V.truth_table(F)
        H, I, c = tlib.spectral_stats(f)
        H2, I2, c2 = V.stats(F)
        # check fhat constant on orbits and equal to orbit-sum value
        err = np.max(np.abs(c - c2[V.lab]))
        errs.append(max(err, abs(H - H2), abs(I - I2)))
        # invariance check
        for gg in V.gens:
            im = tlib.perm_masks(gg, n)
            assert np.array_equal(f[im], f), "not invariant"
    print("%-8s n=%2d orbits=%4d transitive=%s maxerr=%.2e  (%.2fs)" % (name, n, V.k, V.transitive, max(errs), time.time() - t0))
