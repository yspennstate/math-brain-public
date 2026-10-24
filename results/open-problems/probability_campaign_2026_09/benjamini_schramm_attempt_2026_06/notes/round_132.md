# Round 132 log

## Goal

Remove the ambient witness set \(K\) from the uniform deterministic
gate-incidence target.

## Result

Added `cor:localized-anchored-incidence-obstruction` and
`prop:localized-anchored-incidence-criterion`.

Given the uniform deterministic gate-incidence obstruction, set
\[
  A=\{a_z:z\in Z^\sharp\}
\]
and let \(Y\) be the union of all \(K\)-vertices incident to the selected gates
in the expanded gate annulus.  Since the anchors are \(2r_p\)-separated and
\(d(a_z,z)=r_p\), the map \(z\mapsto a_z\) is injective.  Therefore
\[
  |A|\ge\widehat\kappa_j(p),
  \qquad
  |Y|\ge\widehat\kappa_j(p).
\]

Every \(y\in Y\) lies near the original root:
\[
  d(x,y)\le 2^{j+2}+2r_p.
\]

The resulting localized configuration has:

- separated anchors \(Z\) with \(d(x,z)\in(2^j,2^{j+1}]\);
- selected gates \(A\), one at distance \(r_p\) from each anchor;
- a finite set \(Y\subseteq B(x,2^{j+2}+2r_p)\);
- every gate incident to at least \(\widehat\kappa_j(p)\) vertices of \(Y\).

## Interpretation

The obstruction is now a finite metric incidence configuration around a single
root.  The original large finite witness \(K\) no longer appears in the target.
