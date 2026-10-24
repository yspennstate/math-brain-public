"""Sharpness of the low-energy credit: F = Mux_z(b, b'), b quadratic bent on m bits, b' = b with one point flipped.
delta = Inf_z = 2^-m.  Report cost = H(F) - (H(b)+H(b'))/2, the credit bound h(delta) + (2/ln2) delta, and
cost/delta - log2(1/delta).  Exact Walsh integers, float logs (evidence; asymptotics derived in NOTES)."""
import numpy as np
from fei_lib import fwht_int, entropy_from_W
LN2 = np.log(2)
def h2(t): return -t*np.log2(t)-(1-t)*np.log2(1-t)
for m in range(2, 19, 2):
    idx = np.arange(1 << m)
    par = np.zeros(1 << m, dtype=np.int64)
    for j in range(0, m, 2):
        par ^= ((idx >> j) & 1) & ((idx >> (j+1)) & 1)
    b = 1 - 2*par
    bp = b.copy(); bp[0] = -bp[0]
    Wb = fwht_int(b); Wbp = fwht_int(bp)
    Hb = entropy_from_W(Wb, m); Hbp = entropy_from_W(Wbp, m)
    # F on m+1 bits: selector = low bit
    F = np.empty(1 << (m+1), dtype=np.int64); F[0::2] = b; F[1::2] = bp
    HF = entropy_from_W(fwht_int(F), m+1)
    d = 2.0**-m; cost = HF - (Hb+Hbp)/2
    bound = h2(d) + 2*d/LN2
    print(m, 'cost/delta=%.6f' % (cost/d), ' log2(1/delta)+3/ln2=%.6f' % (m + 3/LN2), ' bound/delta=%.6f' % (bound/d), ' cost/bound=%.6f' % (cost/bound))
