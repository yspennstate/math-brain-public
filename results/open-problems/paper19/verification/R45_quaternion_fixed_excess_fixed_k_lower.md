# R45 verification - quaternion fixed-excess fixed-k lower sides

## Scope

Round R45 added the quaternion lower-side analogue of the real/complex
fixed-excess fixed-\(k\) Gaussian theorem.  The new inputs are:

- `lem:quat-rect-kth-laguerre-tail`: for iid standard quaternion Gaussian
  \(G\in\HH^{(m+r)\times m}\), fixed \(r,k\),
  \[
    \Pr\{\sigma_{m-k+1}(G)\le t\}
    \le C_{\HH,r,k}m^{B_{\HH,r,k}}t^{4k(k+r)}.
  \]
- `thm:quat-fixed-excess-fixed-k-lower`: finite-budget and fixed-aspect
  lower sides for
  \(M_{\HH,m}^{(r)}[k]=\min_{|T|=m+r}\sigma_{m-k+1}(A_{m,T})\), with base
  \(h(\gamma)/(4k(k+r))\).
- `cor:quat-rect-kth-gram-lower`: normalized column-Gram lower side with base
  \(h(\gamma)/(2k(k+r))\).

This is lower-side only.  It does not add an upper side, exact fixed-excess
quaternion law, beta interpolation, spherical-radial quaternion transfer,
proportional-excess Wishart edge, or row-Gram statement for \(r>0\).

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Einstein the 2nd: `019f0e44-8f55-7991-8219-dc3fc282c43d`
- Schrodinger the 2nd: `019f0e44-a3f2-7b31-bae1-8fc55339e5e8`
- Noether the 2nd: `019f0e44-b76f-7e53-a057-42982e8ad5a8`
- Locke the 2nd: `019f0e44-ce5f-72a3-a91b-257d83b6756b`
- Hume the 2nd: `019f0e44-eb5e-7882-ab6f-856e9dd66efc`

Four agents accepted the fixed-\(k\) lower side once the beta-4
Laguerre--Selberg tail is written explicitly.  One agent recommended the
conservative \(k=1\) theorem unless the beta-4 tail is proved.  The final text
therefore includes the explicit beta-4 tail proof and keeps all exact-law and
upper-side claims out.

## Checks

For \(G^*G\), the quaternion Wishart eigenvalues have beta-Laguerre density
with beta \(4\) and Laguerre exponent \(q=2(r+1)\).  On
\(\lambda_k\le\delta\), integrating the bottom \(k\) eigenvalues over
\([0,\delta]^k\) contributes
\[
  \delta^{kq+4\binom{k}{2}}=\delta^{2k(k+r)}.
\]
Since \(\sigma_{m-k+1}=\sqrt{\lambda_k}\), \(\delta=t^2\) gives the
singular-value exponent \(4k(k+r)\).  The remaining variables are controlled by
the Laguerre--Selberg normalization ratio with parameter \(q+4k\), which is
polynomial in \(m\) for fixed \(r,k\).

The row-set union bound gives the finite-budget theorem.  The fixed-aspect and
almost-sure lower-envelope statements follow by taking an exponential
\(\varepsilon\)-slack and applying first Borel--Cantelli on a common coupling.
The column-Gram corollary is the pathwise identity
\[
  \lambda_{(k)}((m+r)^{-1}A_T^*A_T)=(m+r)^{-1}\sigma_{m-k+1}(A_T)^2.
\]

## Files changed

- `parts/ensembles.tex`: added the beta-4 tail lemma, quaternion fixed-excess
  fixed-\(k\) lower-side theorem, and column-Gram corollary; updated the
  fixed-excess quaternion conjecture to say only the matching upper side remains
  open.
- `STATE.md`: added row `V.A-rect-kth` and updated related guardrails.
- `PLAN.md`: recorded the quaternion lower-side result and remaining exact-law
  gaps.
- `extremal_hard_edge.tex`: updated the abstract summary.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the Lane
  O compact paragraph `laneO:par:quat-rect-fixed-k-lower`.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex` passed
twice.  The final standalone PDF is 62 pages / 874,041 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` passed twice in
the fleet master.  The final master PDF is 857 pages / 7,782,365 bytes.

Targeted log scans for undefined references, undefined citations,
multiply-defined labels, and rerun requests return only the final `Output
written` lines.
