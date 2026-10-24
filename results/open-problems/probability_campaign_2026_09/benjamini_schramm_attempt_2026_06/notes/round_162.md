# Round 162

Date: 2026-06-09

## Aim

Promote the volume-sensitive matched anchored incidence obstruction into a
formal exclusion criterion.

## Main addition

Added
`prop:volume-sensitive-matched-anchored-incidence-criterion`.

The proposition says that if, under the volume-growth hypothesis
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,
\]
one can rule out all near-critical matched configurations with
\[
  m=\left\lceil
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega}
  \right\rceil
\]
and improved lower scale
\[
  2^j\ge a\log_\Delta\bar\chi_p,
\]
then
\[
  \lim_{p\uparrow p_c}\frac{\mathcal R_p^*}{\bar\chi_p}=0.
\]
With the usual connected, locally finite, quasi-transitive, and susceptibility
upper-bound assumptions, this yields
\[
  p_c(G)<p_{2\to2}(G).
\]

## Proof mechanism

The proof is the exact contrapositive of the new volume-sensitive matched
obstruction, followed by the existing sublinear two-replica criterion.  This
makes the volume-sensitive matched configuration a standalone target for
geometric exclusion.

## Status

The result is still conditional: it packages the obstruction into a criterion
but does not yet rule out the matched configurations.  The next pressure point
is the later matched-count scale amplification, which currently uses the older
non-volume count.  It should be tightened to use the volume-sensitive exponent
\[
  1-2\theta-4\theta\log_\Delta\omega.
\]
