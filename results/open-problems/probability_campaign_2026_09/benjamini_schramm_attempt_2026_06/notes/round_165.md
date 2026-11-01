# Round 165

Date: 2026-06-09

## Aim

Turn the volume-sensitive endpoint-anchor collapse into a direct exclusion
criterion for the remaining geometric obstruction.

## Main addition

Added
`prop:volume-sensitive-large-scale-buffered-tube-criterion`.

Under the volume-growth hypothesis
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,\qquad 1\le \omega<\Delta,
\]
the proposition says that it is enough to rule out buffered tube configurations
at scales
\[
  2^j>B\log_\Delta\bar\chi_p
\]
throughout the endpoint-anchor parameter range
\[
  0<\theta<1/31,\qquad
  5\theta<a<B<\frac{1-21\theta}{2}.
\]
If those large-scale buffered tube configurations cannot occur near
criticality, then
\[
  \lim_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}=0.
\]
With the standard quasi-transitive finite-window hypothesis, this yields
\[
  p_c(G)<p_{2\to2}(G).
\]

## Proof mechanism

The proof is the contrapositive of
`cor:volume-sensitive-endpoint-anchor-collapse`, followed by the existing
sublinear two-replica criterion.  The result packages the current remaining
task as a clean geometric exclusion problem: eliminate large-scale buffered
tubes.

## Status

This is still conditional.  It clarifies the next target but does not yet prove
that the large-scale buffered tube configurations are impossible.
