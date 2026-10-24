"""Enumerate the physical restrictions of Numaro's g with nominal arity <= 10, drop dummy inputs, dedupe by a spectral
invariant, and save the distinct restricted gates (essential arity 2..10) to logs/restr_gates.npz.
usage: restr_enum.py [max_nominal]"""
import sys, os, time, pickle
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()
import numaro as N

maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 10
g, core, hosts = N.load()
print("hosts:", hosts, flush=True)
t0 = time.time()
seen = {}
count = 0
per = {}
for assign, na in N.enumerate_restrictions(g, core, hosts, max_nominal=maxn):
    count += 1
    vals, free = N.restriction_table(g, assign)
    k = len(free)
    vals2, ess = N.drop_dummies(vals, k)
    ke = len(ess)
    if ke < 2:
        continue
    C = F.spectrum(vals2, np.full((1, ke), 0.5))[0]
    w = np.rint(np.abs(C) * (1 << ke)).astype(np.int64)
    inf = np.rint((C * C) @ F.sel(ke) * (1 << (2 * ke))).astype(np.int64)
    key = (ke, int(np.rint(vals2.sum())), tuple(sorted(inf.tolist())), tuple(np.sort(w).tolist()))
    per.setdefault(ke, [0, 0])
    per[ke][0] += 1
    if key not in seen:
        seen[key] = (vals2.astype(np.int8), [free[i] for i in ess], assign)
        per[ke][1] += 1
print("restrictions enumerated: %d (%.0f s)" % (count, time.time() - t0))
for ke in sorted(per):
    print("  essential arity %2d: %7d restrictions, %6d distinct spectral classes" % (ke, per[ke][0], per[ke][1]))
out = {}
for key, (v, fr, a) in seen.items():
    out.setdefault(key[0], []).append((v, fr, a))
pickle.dump(out, open(os.path.join(HERE, "..", "logs", "restr_gates.pkl"), "wb"))
print("saved")
