"""Exact multiscale quantities on the hard families (every mask J, exact expectation over x).

usage: python families.py [small|numaro|all]
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "F4-proof-attempt", "code"))
from mslib import polite, multiscale_summary, per_size_sums
import feilib
from families_lib import maj_plus_maxfalse_flip

polite()
which = sys.argv[1] if len(sys.argv) > 1 else "small"


def and_or_chain(n):
    """x1 AND (x2 OR (x3 AND (x4 OR ...))) : -1 = true."""
    def ev(b):
        v = int(b[n - 1])
        for i in range(n - 2, -1, -1):
            v = (int(b[i]) & v) if (i % 2 == 0) else (int(b[i]) | v)
        return -1 if v else 1
    return feilib.tt_from_func(n, ev)


def maj3_of_maj3():
    return feilib.rec_maj3(2)


fams = []
if which in ("small", "all"):
    fams += [("one_point8", feilib.one_point(8), 8), ("one_point12", feilib.one_point(12), 12),
             ("one_point16", feilib.one_point(16), 16)]
    fams += [(f"bent_plus_flip m={2*m2}", feilib.bent_plus_flip(m2), 2 * m2 + 1) for m2 in (2, 3, 4, 5, 6, 7)]
    fams += [("bent_ip16", feilib.bent_ip(8), 16)]
    fams += [(f"maj{n}+maxfalse_flip", maj_plus_maxfalse_flip(n), n + 1) for n in (5, 9, 13, 15)]
    fams += [(f"maj{n}", feilib.majority(n), n) for n in (5, 9, 13, 15)]
    fams += [(f"tribes w{w} s{s}", feilib.tribes(w, s), w * s) for (w, s) in ((2, 4), (2, 6), (2, 8), (3, 4), (3, 5), (4, 4))]
    fams += [("recmaj3 depth2", maj3_of_maj3(), 9)]
    fams += [(f"addressing k{k}", feilib.addressing(k), k + (1 << k)) for k in (2, 3)]
    fams += [(f"and_or_chain{n}", and_or_chain(n), n) for n in (8, 12, 16)]
if which in ("numaro", "all"):
    g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
    fams += [("numaro18", g.astype(np.int64), 18)]

deltas = (0.1, 0.25, 0.5, 0.75, 0.9)
rows = []
for name, tt, n in fams:
    t0 = time.time()
    out, EH, HT, inf, H, I = multiscale_summary(tt, n, deltas)
    out = {k: (float(v) if not isinstance(v, str) else v) for k, v in out.items()}
    out["name"] = name
    out["sec"] = round(time.time() - t0, 1)
    rows.append(out)
    print(f"{name:26s} n={n:2d} H/I={out['H/I']:.4f} rho0={out.get('rho0', 0):.4f} avgcoord={out.get('avgcoord', 0):.4f} | "
          + " ".join(f"k{d}={out[f'kappa_{d}']:.4f}" for d in deltas)
          + f" | M/L(0.5)={out['M_0.5'] / max(out['L_0.5'], 1e-300):.3f} L(0.5)={out['L_0.5']:.4f}  [{out['sec']}s]", flush=True)
    if name == "numaro18":
        np.savez_compressed(os.path.join(HERE, "..", "logs", "numaro18_profile.npz"), EH=EH, HT=HT, inf=inf, H=H, I=I,
                            cEH=per_size_sums(EH, n), cHT=per_size_sums(HT, n))

with open(os.path.join(HERE, "..", "logs", f"families_{which}.json"), "w") as fo:
    json.dump(rows, fo, indent=1)
