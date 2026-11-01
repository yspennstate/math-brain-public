# Round 164

Date: 2026-06-09

## Aim

Propagate the sharper Round 163 volume-sensitive matched-count scale
amplification into the endpoint-anchor parameter range.

## Main addition

Added
`cor:volume-sensitive-endpoint-anchor-collapse`.

Under the endpoint-anchor parameter range
\[
  0<\theta<1/31,
  \qquad
  5\theta<a<B<\frac{1-21\theta}{2},
\]
and the volume-growth hypothesis
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,
  \qquad
  1\le\omega<\Delta,
\]
the buffered tube configuration can be chosen with
\[
  2^j>B\log_\Delta\bar\chi_p.
\]

## Parameter check

Writing \(\alpha=\log_\Delta\omega<1\), the endpoint-anchor range implies the
Round 163 hypotheses:
\[
  2B\alpha<2B<1-21\theta
  <
  1-2\theta-4\theta\alpha,
\]
and
\[
  (2a+\theta)\alpha<2a+\theta<2B+\theta<1-20\theta
  <
  1-2\theta-4\theta\alpha.
\]
Thus the volume-sensitive matched-count scale amplification applies directly
throughout the endpoint-anchor parameter range.

## Status

This does not solve the full problem.  It removes another dependency on the
older bounded-degree matched-count route in the volume-growth branch and makes
the endpoint-compatible collapse available from the sharper volume-sensitive
count.
