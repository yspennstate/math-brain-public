# Round 238

Round 238 refines the many tangential-run obstruction by typing each
two-sided same-sphere run according to the adjacent levels from which it is
entered and exited.

For a level-\(u\) tangential run \([a,b]\), the two-sided type
\((\eta,\zeta)\in\{-1,+1\}^2\) records
\[
  d(x,v_{a-1})=u+\eta,\qquad d(x,v_{b+1})=u+\zeta .
\]
At most two tangential runs can be one-sided, so if
\(R_x^u(\gamma)>R\) with \(R\ge2\), then for
\[
  P_R=\left\lfloor\frac{R-2}{4}\right\rfloor
\]
one of the four crossing types occurs more than \(P_R\) times.  This gives
the profile bound
\[
  \mathfrak T^{\rm many}_R
  \le
  \sum_{\eta,\zeta\in\{-1,+1\}}\mathfrak C^{\eta,\zeta}_{P_R}.
\]

The new adjacent-crossing localized ladder and subdivision criterion replace
the undifferentiated many-run family by four typed adjacent-crossing profile
families.  Under the standing non-profile assumptions, the route to
\(p_c(G)<p_{2\to2}(G)\) now uses finite-defect bins, near-tail bins, a
terminal far tail, same-sphere spread, long tangential runs, the four
adjacent-crossing tangential families, spread exterior returns, and
exact-level repeated exterior returns.
