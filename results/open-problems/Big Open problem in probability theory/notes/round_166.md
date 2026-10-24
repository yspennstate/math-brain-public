# Round 166

Date: 2026-06-09

## Aim

Extract a probabilistic consequence from the large-scale buffered tube
obstruction by opening the short gate tubes independently.

## Main addition

Added
`cor:volume-sensitive-large-scale-open-buffered-tube-obstruction`.

Under the volume-growth hypothesis
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,\qquad 1\le\omega<\Delta,
\]
and endpoint-anchor parameters
\[
  0<\theta<1/31,\qquad
  5\theta<a<B<\frac{1-21\theta}{2},
\]
the counterexample obstruction can be chosen as a buffered tube configuration
with
\[
  2^j>B\log_\Delta\bar\chi_p.
\]
Moreover, if
\[
  N_{\rm open}
  =
  \#\{i:\text{ every edge of }\gamma_i\text{ is open}\},
\]
then
\[
  \mathbb P_p\!\left(N_{\rm open}\ge
  \frac{\sigma_j^3}{864\Delta^8}\bar\chi_p^{1-20\theta}\right)
  \ge
  1-\exp\!\left[
    -\frac{\sigma_j^3}{3456\Delta^8}\bar\chi_p^{1-20\theta}
  \right].
\]

## Proof mechanism

Use the large-scale configuration from
`cor:volume-sensitive-endpoint-anchor-collapse`.  The paths
\(\gamma_i\) are vertex-disjoint, hence their opening events are independent.
Since \(p\) can be chosen close enough to \(p_c\) that \(p\ge1/\Delta\),
\[
  t p^{r_p}
  \ge
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-20\theta}.
\]
The existing Chernoff lower-tail lemma then gives the displayed probability
bound.

## Status

This still does not rule out large-scale tubes, but it upgrades the remaining
deterministic obstruction into a high-probability open-tube obstruction.  This
is the next object to compare against annular crossing/operator estimates.
