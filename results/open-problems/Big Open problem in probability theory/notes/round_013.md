# Round 013 log

Date: 2026-06-08

## Focus

Extracted a general spectral-factor corollary from the nonbacktracking product
criterion and improved the lattice threshold.

## Spectral-factor result

Let \(T_d\) be the \(d\)-regular tree, put \(s=\sqrt{d-1}\), and let \(H\) be
an infinite connected \(\Delta\)-regular bounded-degree graph.  Set
\[
  \alpha=\|A_H\|_{2\to2}.
\]
If
\[
  s\ge 2+\max\{\sqrt\alpha,\Delta^{1/4}\},
\]
then
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H).
\]

## Proof idea

The nonbacktracking criterion asks for
\[
  \beta(d+\Delta,2s+\alpha)<s^2.
\]
If \(2s+\alpha\le2\sqrt{s^2+\Delta}\), this follows from
\[
  \sqrt{s^2+\Delta}<s^2,
\]
which is forced by \(s\ge2+\Delta^{1/4}\).

If \(2s+\alpha>2\sqrt{s^2+\Delta}\), the larger nonbacktracking root is below
\(s^2\) once
\[
  s^2>(2s+\alpha)/2
\]
and
\[
  s^4-(2s+\alpha)s^2+(s^2+\Delta)>0.
\]
Both follow from \(s\ge2+\sqrt\alpha\), since
\[
  s^4-(2s+\alpha)s^2+(s^2+\Delta)
  =
  s^2((s-1)^2-\alpha)+\Delta.
\]

## Improved lattice threshold

For \(H=\mathbb Z^r\), the direct lattice calculation gives the stronger
simple sufficient condition
\[
  \sqrt{d-1}\ge2+\sqrt{2r},
\]
improving the previous safe threshold \(2+2\sqrt r\).

## Interpretation

The spectral-factor statement is easy to apply to regular factors with known
adjacency norm.  It is still a high-branching theorem, but it makes clear
which feature of the other factor matters for Route A7: the adjacency spectral
radius, not just maximum degree.
