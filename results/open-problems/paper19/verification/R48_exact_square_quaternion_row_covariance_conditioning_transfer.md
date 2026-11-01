# R48 verification - exact square quaternion row/covariance conditioning transfer

## Scope

Round R48 added `cor:quat-square-row-covariance-conditioning-exact`, a
square-row all-column right-factor transfer for quaternion Gaussian matrices.
For iid standard quaternion Gaussian \(G_m\in\HH^{N_m\times m}\),
\(N_m/m\to\gamma>1\), set
\[
  B_m=D_m^{\rm row}G_mS_m,
\]
where \(D_m^{\rm row}\) is a positive real diagonal row factor, possibly
absent, and \(S_m\in\HH^{m\times m}\) is invertible.  The factors may be random
and dependent on \(G_m\).  If
\[
  \Delta_m^{\rm rf}
  =
  \max_i|\log(D_m^{\rm row})_{ii}|
  +\bigl|\log\smin(S_m)\bigr|+\bigl|\log\|S_m\|\bigr|=o_P(m),
\]
with the row term omitted when absent, then
\[
  m^{-1}\log\min_{|T|=m}\smin((B_m)_T)
  \to -h(\gamma)/4
\]
in probability.  The normalized square Gram statistic has base
\(-h(\gamma)/2\).

This is a square row-submatrix statement with one global all-column right
factor.  It is not a fixed-excess exact law, selected-column covariance
transfer, non-square Wishart-edge statement, quaternion spherical-radial
universality theorem, or a.s. exact law.

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Carver the 2nd: `019f0e61-c517-7353-a900-c3051c5c3931`
- Hypatia the 2nd: `019f0e61-c558-7ae0-a3c7-3be6858ce524`
- Kierkegaard the 2nd: `019f0e61-c5a7-7053-b57e-b58ad5863c6a`
- Aristotle the 2nd: `019f0e61-c5f1-7f61-a4f1-115474dba190`
- Heisenberg the 2nd: `019f0e61-c63c-7f12-ace2-147d5e6c6e57`

Consensus:

- PASS for the exact square row-submatrix transfer.
- The row-weight control must be two-sided:
  \(\max_i|\log d_{im}|\), not only an upper row-weight extreme.
- The right-factor hypothesis must control absolute singular-value scale:
  \(|\log\smin(S_m)|+|\log\|S_m\||=o_P(m)\).  Condition number alone is
  insufficient, since \(S_m=e^{cm}U_m\) shifts the exponent while preserving
  condition number.
- Quaternion noncommutativity is harmless because the proof uses operator
  singular-value inequalities, not commutation with \(G_T^*G_T\).
- Dependence on \(G_m\) is harmless because the comparison is pathwise.
- Avoid quaternion determinant language; invertible right factors preserve rank
  and kernels by bijectivity.
- The result only covers one global right factor shared by all square row
  submatrices.  It does not cover selected-column/two-sided minors.

## Pathwise check

For each \(|T|=m\),
\[
  (B_m)_T=(D_m^{\rm row})_T(G_m)_TS_m .
\]
The quaternion min--max inequalities give
\[
  \smin((D_m^{\rm row})_T)\smin(S_m)\smin((G_m)_T)
  \le
  \smin((B_m)_T)
  \le
  \|(D_m^{\rm row})_T\|\,\|S_m\|\,\smin((G_m)_T),
\]
uniformly over \(T\).  Hence
\[
  \left|
  m^{-1}\log M_{B,\HH}
  -
  m^{-1}\log M_{G,\HH}
  \right|
  \le \Delta_m^{\rm rf}/m .
\]
Theorem `thm:quaternion-gaussian-base` gives the source convergence
\(m^{-1}\log M_{G,\HH}\to-h(\gamma)/4\).  The normalized Gram convergence is
then the pathwise identity in `cor:gram-transfer`.

If \(\Delta_m^{\rm rf}=o(m)\) almost surely on a common coupling, the same
comparison transfers only the lower envelopes from the R45/R47 lower-envelope
input.  It does not give an a.s. exact law.

## Files changed

- `parts/ensembles.tex`: added
  `cor:quat-square-row-covariance-conditioning-exact` and clarified the
  selected-column covariance guardrail.
- `STATE.md`: added row `V.A-square-cov` and the R48 round log.
- `PLAN.md`: recorded square all-column right-factor conditioning and qualified
  selected-column covariance caveats.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the Lane
  O compact right-factor transfer paragraph.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
passed twice.  The final standalone PDF is 65 pages / 890,610 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` passed twice in
the fleet master.  The final master PDF is 858 pages / 7,787,229 bytes.

Targeted log scans for undefined citations/references, rerun requests, and
multiply-defined labels return only the final `Output written` lines.
