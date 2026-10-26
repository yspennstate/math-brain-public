"""Independent order-eight construction: build all 105 pairing polytopes,
compute each exact volume, and reproduce the core-sorted histogram and the
corrected eighth moment 908/15 (paper, Section 11).

Run:  python -u verify_order8.py
"""
import sys, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

hist = {}
total = Fr(0)
n = 0
for pm in tk_core.all_pairings(8):
    v = pairing_volume_exact(pm, "T")
    hist[v] = hist.get(v, 0) + 1
    total += v
    n += 1

want = {Fr(1): 14, Fr(2, 3): 28, Fr(1, 2): 32, Fr(9, 20): 4, Fr(2, 5): 5,
        Fr(11, 30): 22}
print(f"pairings: {n}")
print("histogram:", {str(k): v for k, v in sorted(hist.items(), reverse=True)})
assert n == 105, n
assert hist == want, (hist, want)
assert total == Fr(908, 15), total
print("m8(gamma_T) =", total, " (corrects the published 964/15)")

# Hankel at order eight over the 24 parity-mixing pairings
histH = {}
totalH = Fr(0)
for pm in tk_core.parity_pairings(8):
    v = pairing_volume_exact(pm, "H")
    histH[v] = histH.get(v, 0) + 1
    totalH += v
print("Hankel histogram:", {str(k): v for k, v in sorted(histH.items(), reverse=True)})
assert totalH == Fr(281, 15), totalH
print("m8(gamma_H) =", totalH, " (matches Bryc-Dembo-Jiang)")
print("ORDER-8 CHECK PASSED")
