# R47 verification - exact square quaternion diagonal and normalized transfer

## Scope

Round R47 added `cor:quat-square-diagonal-normalized-exact`, a square-row
upgrade that is separate from the fixed-excess lower-side R46 corollary.
For iid standard quaternion Gaussian \(G_m\in\HH^{N_m\times m}\), \(N_m/m\to
\gamma>1\), and
\[
  \widetilde G_m=D_m^{\rm row}G_mE_m
\]
with positive real diagonal row/column weights, possibly random and dependent
on \(G_m\), the total logarithmic extreme
\[
  \Delta_m^{\rm diag}
  =
  \max_i|\log(D_m^{\rm row})_{ii}|
  +
  \max_j|\log(E_m)_{jj}|
\]
transfers the square-row statistic pathwise.  If
\(\Delta_m^{\rm diag}=o_P(m)\), then
\[
  m^{-1}\log\min_{|T|=m}\smin((\widetilde G_m)_T)
  \to -h(\gamma)/4
\]
in probability.  The normalized square Gram statistic has base
\(-h(\gamma)/2\) by `cor:gram-transfer`.

The corollary includes row-normalized quaternion Gaussian rows and
full-matrix column-normalized quaternion Gaussian columns.  It gives only an
a.s. lower envelope under a.s. \(o(m)\) diagonal extrema; it does not add an
a.s. exact law.

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Rawls the 2nd: `019f0e57-57f8-7452-b63c-7be5978cd8e0`
- Meitner the 2nd: `019f0e57-5874-71f2-b47e-85b4c1394aaf`
- Linnaeus the 2nd: `019f0e57-58c1-7b11-8914-0f9fc56d2420`
- Bohr the 2nd: `019f0e57-590f-77c1-a057-5699fa66a78c`
- Fermat the 2nd: `019f0e57-595a-7e61-80f4-b980d9e98193`

Consensus:

- PASS for the square \(r=0,k=1\) exact-in-probability transfer.
- Keep the new statement separate from R46, which remains only lower-side for
  general fixed excess and fixed \(k\).
- Positive real diagonal weights are essential; real scalars are central in
  \(\HH\).
- Dependence of the diagonal weights on \(G_m\) is harmless because the proof
  is pathwise.
- Full-matrix column normalization is covered as a global right diagonal
  factor; selected-submatrix column renormalization is not covered.
- Do not claim selected-column/two-sided non-diagonal covariance transfer,
  quaternion-valued diagonal weights, fixed-excess exact laws, quaternion
  spherical-radial universality, or an a.s. exact law.  The square all-column
  right-factor transfer is handled separately in R48.

## Pathwise check

For each \(|T|=m\),
\[
  (\widetilde G_m)_T=(D_m^{\rm row})_T(G_m)_TE_m .
\]
With
\[
  \Delta_m^{\rm diag}
  =
  \max_i|\log(D_m^{\rm row})_{ii}|
  +
  \max_j|\log(E_m)_{jj}|,
\]
the min--max inequalities give
\[
  e^{-\Delta_m^{\rm diag}}\smin((G_m)_T)
  \le \smin((\widetilde G_m)_T)
  \le e^{\Delta_m^{\rm diag}}\smin((G_m)_T)
\]
uniformly over \(T\).  Therefore
\[
  \left|
  m^{-1}\log M_{\widetilde G,\HH}
  -
  m^{-1}\log M_{G,\HH}
  \right|
  \le \Delta_m^{\rm diag}/m .
\]
The source theorem `thm:quaternion-gaussian-base` gives
\(m^{-1}\log M_{G,\HH}\to-h(\gamma)/4\) in probability, so
\(\Delta_m^{\rm diag}=o_P(m)\) transfers the exact square-row base.

For quaternion normalization, row norm squares are \((1/4)\chi^2_{4m}\) and
column norm squares are \((1/4)\chi^2_{4N_m}\).  The same Markov upper-tail and
ball-volume lower-tail estimates used in R46 give logarithmic norm extremes
\(o_P(m)\), and \(o(m)\) a.s. on common couplings after the \(O(m)\) unions.

## Files changed

- `parts/ensembles.tex`: added
  `cor:quat-square-diagonal-normalized-exact` and clarified the quaternion
  lower-side guardrails.
- `STATE.md`: added row `V.A-square-diag` and the R47 round log.
- `PLAN.md`: split the exact square diagonal/normalization transfer from the
  fixed-excess lower-side quaternion paragraph.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the
  Lane O square quaternion diagonal/normalization transfer.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
passed twice.  The final standalone PDF is 64 pages / 885,584 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` passed twice in
the fleet master.  The final master PDF is 857 pages / 7,784,020 bytes.

Targeted log scans for undefined citations/references, rerun requests, and
multiply-defined labels return only the final `Output written` lines.
