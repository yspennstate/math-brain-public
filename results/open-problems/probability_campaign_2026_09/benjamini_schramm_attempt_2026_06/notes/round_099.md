# Round 099 log

## Goal

Make the order of limits in the far-leg tightness condition explicit.

## Result

Added `cor:far-leg-tail-limit`.

With the notation
\[
  \Theta_p(R)=\sup_K\mathcal R_p^{>R}(K)/\bar\chi_p,
\]
the sublinear two-replica condition is equivalent to
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}\Theta_p(R)=0.
\]

The proof uses only monotonicity in \(R\) and
`prop:far-leg-square-criterion`.

## Interpretation

The target estimate is now a true tail-tightness statement.  Any future proof
has to control the near-critical limsup at fixed \(R\), then show this control
vanishes as \(R\) grows.
