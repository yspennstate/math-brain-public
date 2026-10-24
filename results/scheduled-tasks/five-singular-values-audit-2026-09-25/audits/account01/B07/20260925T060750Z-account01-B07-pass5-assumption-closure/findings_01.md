# Pass 5 findings, part 1

Source pin: ec211ba2d77a4a9850168c6af1574ea651feaa7c / c4f2a997cf336ee974e15409b5bccdd8cca039d8.

L41 p1: FALSE exposition. The abstract omits the no-pivot hypothesis from the random-sign conversion. Proposition 6.4 has the needed hypothesis; no theorem-chain effect.

L62 p1: UNCHECKED current-literature claim. A targeted current search did not establish the exact status claim. No proof dependency.

L65 p1: FALSE wording. The proof supplies a square-root/logarithmic upper envelope, not necessarily an actual singularity.

L148 p3: GAP. The approximation-number identity is correct with zero padding, but the proof invokes the first j right singular vectors even if j exceeds matrix dimension. Repair: if j>min(m,n), rank(T)<j and B=T makes the minimum and padded s_j both zero. Downstream uses are in range.

L222 p5: PASS, and this corrects my earlier B07 reports. The phrase 'factors with beta_i=0 are at most one' means the factor values are <=1, not cardinality <=1. For beta_i=0, w_i=0 and the factor f_i((Uy)_i)<=1 is independent of z, so any number can be dropped.

L319-321 p7: GAP. Insert Jensen/Cauchy-Schwarz |E F|^2 <= E|F|^2 before averaging the fixed-X_{I'} Plancherel bound. No constant changes.
