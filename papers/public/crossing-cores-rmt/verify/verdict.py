"""THE VERDICT: run when the kappa_8^T sweep completes.

1. kappa_8^T from the 21,994 raw orbit volumes (sum size x volume).
2. Cross-check against the extension's implied 687080/9.
3. m_16(gamma_T) and the (13.2) Schur threshold: the order-16 free
   conditional-positivity verdict, independently derived from raw polytopes.
4. Conjecture tests at the new order: s_8 = m_16/Cat_8 extends the
   semicircle-mixture minors; b_8^2 extends the Jacobi-increment sequence;
   the kappa-ratio point extends the 2 rho^2 asymptotic.

Run:  python -u verdict.py
"""
import json, os
from fractions import Fraction as Fr
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))

def cat(k):
    return comb(2 * k, k) // (k + 1)

with open(os.path.join(HERE, "kappa8_orbits_T.json"), encoding="utf-8") as f:
    orb = json.load(f)["orbits"]
with open(os.path.join(HERE, "kappa8_volumes_T.json"), encoding="utf-8") as f:
    vols = json.load(f)

missing = [k for k in orb if k not in vols]
print(f"orbits: {len(orb)}, volumes: {len(vols)}, missing: {len(missing)}")
if missing:
    print("SWEEP INCOMPLETE - no verdict yet")
    raise SystemExit(1)

kappa8 = Fr(0)
for key, size in orb.items():
    kappa8 += Fr(vols[key]) * size
print(f"kappa_8^T (raw polytopes) = {kappa8} = {float(kappa8):.6f}")
EXT = Fr(687080, 9)
print(f"extension implied value    = {EXT} = {float(EXT):.6f}")
print("MATCH" if kappa8 == EXT else f"*** MISMATCH (diff {kappa8 - EXT}) ***")

KNOWN = Fr(29362422, 105)
m16 = KNOWN + kappa8
print(f"\nm_16(gamma_T) = {m16} = {float(m16):.4f}")
THRESH = Fr(3863516832738344459, 10908088231950)
print(f"threshold     = {THRESH} = {float(THRESH):.4f}")
if m16 >= THRESH:
    print(f"VERDICT: m_16 ABOVE threshold by {float(m16 - THRESH):.4f} - the "
          f"order-16 free conditional-positivity test PASSES; free infinite "
          f"divisibility of gamma_T remains open (as the extension found).")
else:
    print(f"VERDICT: m_16 BELOW threshold by {float(THRESH - m16):.4f} - "
          f"gamma_T is NOT freely infinitely divisible (new theorem).")

mT = {0: Fr(1), 1: Fr(1), 2: Fr(8,3), 3: Fr(11), 4: Fr(908,15), 5: Fr(415),
      6: Fr(23840,7), 7: Fr(325719,10)}
mT[8] = m16

s = [mT[k]/cat(k) for k in range(9)]
def minors(seq, shift):
    out = []
    tmax = (len(seq)-1-shift)//2
    for t in range(0, tmax+1):
        sz = t+1
        A = [[seq[i+j+shift] for j in range(sz)] for i in range(sz)]
        det = Fr(1)
        for c in range(sz):
            piv = next((r for r in range(c, sz) if A[r][c] != 0), None)
            if piv is None:
                det = Fr(0); break
            if piv != c:
                A[c], A[piv] = A[piv], A[c]; det = -det
            det *= A[c][c]
            for r in range(c+1, sz):
                if A[r][c]:
                    fq = A[r][c]/A[c][c]
                    for cc in range(c, sz):
                        A[r][cc] -= fq*A[c][cc]
        out.append(det)
    return out

h0 = minors(s, 0)
h1 = minors(s, 1)
print(f"\nmixture minors with raw-derived s_8: "
      f"H0 {'all +' if all(d > 0 for d in h0) else 'NONPOSITIVE'}, "
      f"H1 {'all +' if all(d > 0 for d in h1) else 'NONPOSITIVE'}")

L = {2*k: v for k, v in mT.items()}
for n in range(0, 17):
    L.setdefault(n, Fr(0))
polys = {0: {0: Fr(1)}, 1: {1: Fr(1)}}
def lp(p, q):
    t = Fr(0)
    for i, a in p.items():
        for j, b in q.items():
            t += a*b*L.get(i+j, Fr(0))
    return t
h = {0: Fr(1)}
b2 = {}
for k in range(1, 9):
    h[k] = lp(polys[k], polys[k])
    b2[k] = h[k]/h[k-1]
    if k < 8:
        nxt = {}
        for i, a in polys[k].items():
            nxt[i+1] = nxt.get(i+1, Fr(0)) + a
        for i, a in polys[k-1].items():
            nxt[i] = nxt.get(i, Fr(0)) - b2[k]*a
        polys[k+1] = nxt
inc = float(b2[8] - b2[7])
print(f"Jacobi increment b_8^2 - b_7^2 = {inc:.5f} (sequence was descending "
      f"0.69342 -> 0.68952 at k=4->3... target rho^2 = 0.68707)")
kap7 = Fr(206797, 30)
ratio = float(kappa8 / kap7) / 8
print(f"kappa ratio kappa_8/(8 kappa_7) = {ratio:.5f} "
      f"(sequence 1.4833, 1.4213, 1.4002, 1.3899, 1.3844 -> this; "
      f"unified-conjecture target 2 rho^2 = 1.37414)")
print("\nVERDICT SCRIPT COMPLETE")
