# Round 012 log

Date: 2026-06-08

## Focus

Extracted an explicit lattice-factor family from the nonbacktracking product
criterion.

## Result

For \(r\ge1\), if
\[
  \sqrt{d-1}\ge2\sqrt r+2,
\]
then
\[
  p_c(T_d\square\mathbb Z^r)<p_{2\to2}(T_d\square\mathbb Z^r).
\]

## Calculation

Put \(q=d-1\) and \(s=\sqrt q\).  For \(H=\mathbb Z^r\),
\[
  \Delta=2r,\qquad \|A_H\|_{2\to2}=2r.
\]
The nonbacktracking criterion becomes
\[
  \beta(d+2r,2s+2r)<s^2.
\]
The second branch of \(\beta\) applies, giving the explicit inequality
\[
  s+r+\sqrt{r(2s+r-2)}<s^2.
\]

Define
\[
  F_r(s)=s^2-s-r-\sqrt{r(2s+r-2)}.
\]
For \(s\ge2\sqrt r+2\), \(F'_r(s)>0\), and \(F_r(2\sqrt r+2)>0\).  Hence the
criterion holds in this regime.

## Interpretation

This gives a uniform high-branching theorem for \(T_d\) times a lattice
factor.  It remains diagnostic rather than a final product theorem: known
product methods are much stronger, and the SAW-operator route still does not
reach low-branching cases such as \(T_3\square\mathbb Z^r\).
