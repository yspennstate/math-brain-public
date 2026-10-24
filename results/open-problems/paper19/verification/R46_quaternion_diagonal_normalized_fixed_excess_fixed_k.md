# R46 verification - quaternion diagonal and normalized fixed-excess fixed-k transfer

## Scope

Round R46 added `cor:quat-diagonal-normalized-fixed-excess-fixed-k`, a
quaternion-specific diagonal-transfer consequence of R45.  For iid standard
quaternion Gaussian \(G_m\in\HH^{N_m\times m}\), fixed \(r,k\), and positive
real diagonal row/column weights with total logarithmic extreme \(o_P(m)\), the
weighted matrix inherits:

- singular-value lower base \(h(\gamma)/(4k(k+r))\);
- normalized column-Gram lower base \(h(\gamma)/(2k(k+r))\);
- common-coupling a.s. lower envelopes under a.s. \(o(m)\) diagonal extrema.

The corollary includes full-matrix row-normalized and column-normalized
quaternion Gaussian matrices as special cases.

This remains lower-side-only diagonal bookkeeping.  It does not add an upper
side, exact fixed-excess/normalized law beyond the square \(r=0,k=1\) case
handled later in R47, selected-column or fixed-excess non-diagonal covariance
transfer, spherical-radial quaternion transfer, beta interpolation,
proportional Wishart edge, or row-Gram statement for \(r>0\).

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Archimedes the 2nd: `019f0e4e-f106-77f3-bbed-a972f1d77ba7`
- Hegel the 2nd: `019f0e4f-12dc-79e0-b204-19d04dfad19f`
- Pasteur the 2nd: `019f0e4f-44f8-76c3-8fb9-ce27fa990a53`
- Ramanujan the 2nd: `019f0e4f-59fb-7400-afb1-aac8a2411504`
- Curie the 2nd: `019f0e4f-7146-75b2-8a80-73b684d35421`

All five found the result safe with narrow guardrails.  The common warnings
were: use positive real diagonal weights only, keep quaternionic singular values
and Hermitian eigenvalues counted once, normalize full matrix columns rather
than selected-submatrix columns, and do not reapply iid Laguerre laws after
normalization.

## Checks

For positive real diagonal weights
\[
  \widetilde A_m=D_m^{\rm row}A_mE_m
\]
with total logarithmic extreme \(\Delta_m\), the quaternionic min--max
singular-value inequalities give, uniformly over \(|T|=m+r\),
\[
  e^{-\Delta_m}\sigma_{m-k+1}(A_T)
  \le \sigma_{m-k+1}(\widetilde A_T)
  \le e^{\Delta_m}\sigma_{m-k+1}(A_T).
\]
Real positive scalars are central in \(\HH\), so there is no noncommutativity
issue.  Taking minima over \(T\) gives the \(\Delta_m/m\) log comparison for
\(M^{(r)}[k]\).  The column-Gram identity
\[
  \lambda_{(k)}((m+r)^{-1}A_T^*A_T)
  =(m+r)^{-1}\sigma_{m-k+1}(A_T)^2
\]
gives the \(2\Delta_m/m\) log comparison for \(\Lambda^{(r)}[k]\).

For standard quaternion Gaussian entries in the paper's normalization, row and
column norm squares are \((1/4)\chi^2_{4m}\) and \((1/4)\chi^2_{4N_m}\).  Markov
upper tails and ball-volume lower tails imply that the row/column logarithmic
extrema are \(o_P(m)\), and are \(o(m)\) a.s. on any common coupling after the
summable \(O(m)\)-size row/column unions.

## Files changed

- `parts/ensembles.tex`: added
  `cor:quat-diagonal-normalized-fixed-excess-fixed-k`.
- `STATE.md`: added row `V.A-rect-kth-diag` and the R46 round log.
- `PLAN.md`: recorded the quaternion diagonal and normalized consequence under
  V.A.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added a compact
  Lane O sentence inside `laneO:cor:conditioning-variants`.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
passed twice.  The final standalone PDF is 63 pages / 879,535 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` passed twice in
the fleet master.  The final master PDF is 857 pages / 7,782,880 bytes.

Targeted log scans for undefined citations/references, rerun requests, and
multiply-defined labels return only the final `Output written` lines.
