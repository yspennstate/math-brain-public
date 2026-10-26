"""Rigorous bracket on kappa_8^T from a partial sweep.

Every reduced Toeplitz core with at least four pairs has volume at most
9/20 (Theorem 9.1, proved), and volumes are nonnegative, so at any moment

    S_done  <=  kappa_8^T  <=  S_done + (9/20) * W_remaining,

where S_done is the size-weighted sum over completed orbits and
W_remaining is the number of labelled words not yet covered.  This gives
a certified interval that tightens monotonically as the sweep runs, and
lets the comparison against the extension's implied value be made -- or
at least bounded -- before the sweep finishes.

Run:  python -u partial_bracket.py
"""
import json, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "kappa8_orbits_T.json"), encoding="utf-8") as f:
    meta = json.load(f)
orbits = meta["orbits"]
W_TOTAL = meta["n_words"]

with open(os.path.join(HERE, "kappa8_volumes_T.json"), encoding="utf-8") as f:
    vols = json.load(f)

S = Fr(0)
W_done = 0
for key, vol in vols.items():
    size = orbits.get(key)
    if size is None:
        continue
    S += Fr(vol) * size
    W_done += size
W_rem = W_TOTAL - W_done

CAP = Fr(9, 20)
lo = S
hi = S + CAP * W_rem

TARGET = Fr(687080, 9)
KNOWN = Fr(29362422, 105)
THRESH = Fr(3863516832738344459, 10908088231950)

print(f"orbits done   : {len(vols)} / {len(orbits)}")
print(f"words covered : {W_done} / {W_TOTAL}  ({100.0*W_done/W_TOTAL:.2f}%)")
print(f"partial sum   : {float(S):.4f}")
print(f"certified bracket for kappa_8^T:")
print(f"   lower {float(lo):.4f}   upper {float(hi):.4f}   width {float(hi-lo):.4f}")
print(f"extension's implied value: {TARGET} = {float(TARGET):.4f}")
inside = lo <= TARGET <= hi
print(f"   target inside the bracket: {inside}"
      + ("" if inside else "   *** THE SWEEP CONTRADICTS THE EXTENSION ***"))

m16_lo = KNOWN + lo
m16_hi = KNOWN + hi
print(f"\nimplied m_16 bracket: [{float(m16_lo):.2f}, {float(m16_hi):.2f}]")
print(f"Schur threshold (13.2): {float(THRESH):.2f}")
if m16_lo >= THRESH:
    print("   VERDICT ALREADY CERTIFIED: m_16 exceeds the threshold on the "
          "partial data alone - the order-16 free-ID test PASSES.")
elif m16_hi < THRESH:
    print("   VERDICT ALREADY CERTIFIED: m_16 is below the threshold - "
          "gamma_T is NOT freely infinitely divisible.")
else:
    need = THRESH - KNOWN - S
    print(f"   not yet decided from partial data; the remaining orbits must "
          f"contribute at least {float(need):.2f} for the test to pass "
          f"(they can contribute at most {float(CAP*W_rem):.2f}).")
