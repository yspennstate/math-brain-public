# Round 161

Date: 2026-06-09 12:12 +03:00

## Aim

Convert the volume-sensitive localized anchored incidence obstruction into a
matched obstruction while preserving the improved logarithmic gate scale.

## Main addition

Added
`cor:volume-sensitive-matched-anchored-incidence-obstruction`.

Under the volume-growth assumption
\[
  |B(u,R)|\le C_{\rm vol}\omega^R
\]
and the parameter inequalities
\[
  2B\log_\Delta\omega<1,
  \qquad
  \theta<B,
  \qquad
  (2a+\theta)\log_\Delta\omega
  <
  1-2\theta-4\theta\log_\Delta\omega,
\]
the localized obstruction can be chosen with
\[
  2^j\ge a\log_\Delta\bar\chi_p.
\]
Writing
\[
  \widehat\kappa_j^{\rm vol}(p)
  =
  \frac{\sigma_j^3}{16C_{\rm vol}^3}
  \bar\chi_p^{1-2\theta-4\theta\log_\Delta\omega},
  \qquad
  m=\lceil\widehat\kappa_j^{\rm vol}(p)\rceil,
\]
one obtains matched triples
\[
  (z_i,a_i,y_i)_{i=1}^m
\]
with distinct \(z_i\)'s, distinct \(a_i\)'s, distinct \(y_i\)'s, separated
anchors, and
\[
  d(x,z_i)\in(2^j,2^{j+1}],\quad
  d(a_i,z_i)=r_p,\quad
  d(x,a_i),d(y_i,a_i)\in(2^j-r_p,2^{j+1}+r_p],
\]
with all \(y_i\in B(x,2^{j+2}+2r_p)\).

## Proof mechanism

Form the bipartite graph between the gate set \(A\) and the localized point set
\(Y\), joining \(a_z\) to \(y\) when \(d(y,a_z)\in I_{j,p}^{\rm gate}\).  The
localized obstruction gives \(|A|\ge\widehat\kappa_j^{\rm vol}(p)\) and every
left degree at least \(\widehat\kappa_j^{\rm vol}(p)\).  Since these quantities
are integer-valued after taking ceilings, Hall's theorem gives a matching of
size \(m\).

## Status

This is still an obstruction extraction, not a solution of the full
Benjamini--Schramm/\(L^2\) target.  The next useful step is to formulate the
volume-sensitive exclusion criterion dual to this matched obstruction and then
seek the geometric contradiction that rules out these matched configurations.
