# R43 verification - random diagonal fixed-k transfer

Date: 2026-06-28.

## Scope

Record the pathwise random positive diagonal row/column-weight transfer for
fixed-excess fixed-\(k\) singular-value statistics and normalized column-Gram
lower sides.

## Agent audit

The first R42 attempt produced only two completed audit agents and three
transport failures, so no theorem text was merged from that incomplete audit.
The round was restarted with exactly five fresh read-only audit agents.  All
five completed and approved the compact-remark form.  They agreed that the
result is only pathwise diagonal bookkeeping and should not be promoted to a new
upper-side or exact-law theorem.

## Mathematical checks

- For \(\widetilde A_m=D_m^{\rm row}A_mE_m\), with strictly positive finite
  diagonal entries, define
  \[
    \Delta_m^{\rm diag}
    =
    \max_i|\log(D_m^{\rm row})_{ii}|+\max_j|\log(E_m)_{jj}|.
  \]
- For every row set \(|T|=m+r\), the min--max singular-value inequalities give
  \[
    e^{-\Delta_m^{\rm diag}}\sigma_{m-k+1}(A_{m,T})
    \le
    \sigma_{m-k+1}(\widetilde A_{m,T})
    \le
    e^{\Delta_m^{\rm diag}}\sigma_{m-k+1}(A_{m,T}).
  \]
- Taking minima over row sets gives the fixed-excess fixed-\(k\) log comparison
  on the positivity event:
  \[
    \left|m^{-1}\log M_{\widetilde A}^{(r)}[k]
      -m^{-1}\log M_A^{(r)}[k]\right|
    \le \Delta_m^{\rm diag}/m.
  \]
- The normalized column-Gram statistic is the square of the singular-value
  statistic times \((m+r)^{-1}\), so the corresponding log error is at most
  \(2\Delta_m^{\rm diag}/m\).
- Therefore lower sides transfer under
  \(\Delta_m^{\rm diag}=o_\PP(m)\), and a.s. lower envelopes transfer under
  \(\Delta_m^{\rm diag}=o(m)\) on the common coupling.

## Guardrails

- Diagonal entries must be strictly positive and finite; zeros or infinities
  break the logarithmic sandwich.
- Dependence on the base matrix is harmless because the comparison is pathwise.
- The statement is for fixed \(r,k\), lower sides and lower envelopes only.
- The Gram object is the normalized column Gram \((m+r)^{-1}A_T^*A_T\), not a
  row-Gram statistic for \(r>0\).
- No non-diagonal covariance transfer, upper side, exact law, quaternion
  fixed-excess fixed-\(k\) law, or proportional-excess Wishart-edge statement is
  implied.

## Files changed

- `parts/ensembles.tex`: added `rem:random-diagonal-fixed-k`.
- `STATE.md`: broadened rows `V.B-rand` and `V.B-col` and added the R43 round
  log.
- `PLAN.md`: recorded the random diagonal fixed-excess fixed-\(k\) transfer
  under V.B.
- `master/chO_phase_retrieval_rmt.tex`: added one compact sentence to
  `laneO:cor:conditioning-variants`.
- `MASTER_STATE.md`: recorded the master integration.

## Build verification

Standalone:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  twice.
- Output: `extremal_hard_edge.pdf` has 60 pages and 858,101 bytes.
- Targeted log scan matched only:
  `Output written on extremal_hard_edge.pdf (60 pages, 858101 bytes).`

Master:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` twice.
- Output: `master.pdf` has 856 pages and 7,776,464 bytes.
- Copied to `~/Downloads/master.pdf`.
- Targeted log scan matched only:
  `Output written on master.pdf (856 pages, 7776464 bytes).`

Known residual diagnostics are unchanged in kind: the standalone keeps the
pre-existing `\theHfootnote` warning and known layout warnings; the master keeps
its large pre-existing warning/overfull-box background.
