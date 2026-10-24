# account04/B07 handoff — 20260923T161510Z-account04-B07-coordinate-core-r2

Status: supporting theorem proved; full QFORM open; continuity separate.

## New theorem

If an actual original-coordinate block of size \(m=r+3\) has
\[
A[I,I]=D+R+E,\qquad |D_{ii}|\ge d,\quad \operatorname{rank}R\le r,
\quad |E|_{\max}\le\varepsilon,
\]
then
\[
s_3(A[I,I])\ge d-(r+3)\varepsilon
\]
and, when positive,
\[
\|p_{X^TAX}\|_\infty\le
\frac{2\sqrt{6\pi(r+3)}}{d-(r+3)\varepsilon}.
\]

For a slab ratio \(\rho\) with \(|E|_{\max}\le c/\rho\), \(r+3\) such diagonals force
\[
\rho\le\frac{(r+3)c+2\sqrt{6\pi(r+3)}}d.
\]
At \(r=28,c=32\sqrt{2e}\), the threshold is \(<2361.337/d\).

Account01/B07 r28 at commit \`45934a636682207f422de4ab3f94c658030ba1ac\` gives a physical edge
\[
|A_{ij}|\ge2^{-5/4}\Omega^{1/4}
\]
in the double-heavy near-rank-two branch. Unless the indefinite pair exit pays, this regenerates a physical diagonal of size at least \(2^{-9/4}\Omega^{1/4}\). If this happens on \(r+3\) distinct coordinates, the new core theorem pays the density directly.

Remaining debt: control the one-hub Plücker faces and the dimension-growing entrywise-small dense tail. Do not delete the tail as a small quadratic error.

Pins: brain \`f89c6ddf42332d9cd8fc47501cb1061716ee9071a\`; Claude continuation \`7ffd1ed79398611eb06752f622be0ce33dcacb5a\`; partner \`45934a636682207f422de4ab3f94c658030ba1ac\`; report commit \`dab16464e87c939cc0cf3fd01d070045290192fa\`; report blob \`ed36c3d3a257f39cd2edcc3fb657a769fbe17a46\`.

Report: https://github.com/yspennstate/math-open-problems/blob/dab16464e87c939cc0cf3fd01d070045290192fa/proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md
