"""Exact certificate for the seven-input witness G7 against the read-once potential cert_vi_h96k40.

G7 is the monotone gate whose minimal true sets are {1,3}, {0,4}, {2,3,4}, {0,1,5}, {1,4,6}, {2,4,6}, {1,5,6}
(inputs 0..6).  It is the restriction of Numaro's g with core coordinates 0..6 free, x7 = 0, x8 = 1, auxiliaries
14, 15, 16 fixed true and the other auxiliaries fixed false; this script checks that identity when the Numaro table is
present, then evaluates D and c = -D/W exactly (exact_gate.check) at rational bias vectors."""
import sys, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import exact_gate as X

MINTERMS = [(1, 3), (0, 4), (2, 3, 4), (0, 1, 5), (1, 4, 6), (2, 4, 6), (1, 5, 6)]
k = 7
table = []
for x in range(1 << k):
    true = any(all((x >> i) & 1 for i in m) for m in MINTERMS)
    table.append(-1 if true else 1)
print("G7: %d true points of %d" % (sum(1 for v in table if v < 0), 1 << k))

try:
    import numpy as np, numaro as N
    g, core, hosts = N.load()
    vals, free = N.restriction_table(g, ['f'] * 7 + [0, 1] + [0, 0, 0, 0, 0, 1, 1, 1, 0])
    print("equals the Numaro restriction (core 0..6 free, x7=0, x8=1, aux 14,15,16 true):",
          bool(np.array_equal(vals.astype(int), np.array(table))))
except Exception as e:
    print("Numaro table not checked:", e)

npz = os.path.join(HERE, "..", "..", "inputs", "cert_vi_h96k40.npz")
AND_REF = Fr(4055, 10**6)     # the AND margin of this potential is about 4.05500e-3 (numerical, logs/and_cmax_h96k40.out)
H = Fr(1, 2)
for name, ps in (("rational", [H, H, Fr(7, 24), H, H, Fr(2, 7), Fr(5, 17)]),
                 ("dyadic", [H, H, Fr(9, 32), H, H, Fr(9, 32), Fr(5, 16)])):
    print("%s bias p = (%s)" % (name, ", ".join(str(p) for p in ps)))
    out = X.check(table, ps, npz)
    lo = out["c"][0]
    print("  certified: c_G7 > %.12f, which is %.2f times the numerical AND margin 4.055e-3" % (float(lo), float(lo / AND_REF)))
    print("  certified: D < 0 is %s ; c lower bound > 0.01 (the certified arity-2 margin) is %s" %
          (out["D"][1] < 0, lo > Fr(1, 100)))
