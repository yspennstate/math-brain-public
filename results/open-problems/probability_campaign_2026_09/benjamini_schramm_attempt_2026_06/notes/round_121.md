# Round 121 log

## Goal

Convert the separated fan obstruction into an exact criterion for finishing the
far-leg route.

## Result

Added `def:separated-fans` and `prop:fan-exclusion-criterion`.

The definition packages the Round 120 witness as an
\((\epsilon,\eta,\theta,J,H)\)-separated fan at \(p\): a finite set \(K\), root
\(x\in K\), annular scale \(j\), and separated remote set \(Z\) satisfying the
explicit size, distance, separation, and backscatter lower bounds.

The criterion says that if, for every \(0<\epsilon\le1\), some choice of
\(\eta>0\), \(0<\theta<1/2\), \(J,H\), and a near-critical interval excludes
all such separated fans, then
\[
  \mathcal R_p^*/\bar\chi_p\to0.
\]
Under the existing mean-field susceptibility hypothesis, this implies
\[
  p_c(G)<p_{2\to2}(G).
\]

## Interpretation

The remaining proof target is now sharply localized.  It is enough to rule out
polynomially many separated logarithmic-scale backscatter centers for every
possible obstruction strength \(\epsilon\).
