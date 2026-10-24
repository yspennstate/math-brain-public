# R39 verification - fixed-excess fixed-k conditioning transfer

Date: 2026-06-28.

## Scope

Extend the deterministic conditioning transfer from fixed-excess minimum
singular values to fixed-excess fixed-\(k\) singular values and their normalized
column-Gram lower sides.

## Agent audit

Launched exactly five read-only audit agents for the active round.  All five
approved the transfer under the existing hypotheses of
Proposition~\ref{prop:cov-transfer}.  They flagged one necessary guardrail:
subexponential condition number alone is not enough for covariance transfer;
the proof needs subexponential absolute lower and upper covariance extremes.

## Mathematical checks

- For rectangular \(X\), invertible \(L,R\), and every singular-value index
  \(j\),
  \[
    s_{\min}(L)s_{\min}(R)\sigma_j(X)
    \le \sigma_j(LXR)
    \le s_{\max}(L)s_{\max}(R)\sigma_j(X).
  \]
- With \(A_{m,T}=D_TG_{m,T}\Sigma_m^{1/2}\), the same constants work for every
  row set \(T\):
  \[
    \alpha_m\sigma_{m-k+1}(G_{m,T})
    \le \sigma_{m-k+1}(A_{m,T})
    \le \beta_m\sigma_{m-k+1}(G_{m,T}),
  \]
  where
  \(\alpha_m=(\min_i d_{im})\sqrt{\lambda_{\min}(\Sigma_m)}\) and
  \(\beta_m=(\max_i d_{im})\sqrt{\lambda_{\max}(\Sigma_m)}\).
- The existing deterministic hypotheses give
  \(m^{-1}\log\alpha_m=o(1)\) and \(m^{-1}\log\beta_m=o(1)\), so taking minima
  over \(|T|=m+r\), logs, and dividing by \(m\) transfers the fixed-excess
  fixed-\(k\) singular-value log scale.
- Corollary~\ref{rect-kth:fixed-aspect-lower} then transfers the lower-side
  base \(h(\gamma)/(d_\F k(k+r))\).
- Squaring the same sandwich gives the normalized column-Gram comparison; the
  normalization contributes only \(m^{-1}\log(m+r)=o(1)\).  The lower-side Gram
  base is therefore \(2h(\gamma)/(d_\F k(k+r))\).
- The statement is lower-side only.  It adds no upper side, exact convergence
  law, non-diagonal two-sided-minor transfer, row-Gram result for \(r>0\), or
  condition-number-only covariance claim.

## Files changed

- `parts/ensembles.tex`: added
  `cor:fixed-excess-fixed-k-transfer`.
- `STATE.md`: broadened row `V.B` and added the R39 round log.
- `PLAN.md`: recorded the fixed-excess fixed-\(k\) deterministic transfer under
  V.B.
- `extremal_hard_edge.tex`: updated the abstract summary.
- `master/chO_phase_retrieval_rmt.tex`: added the compact master transfer
  statement inside `laneO:cor:conditioning-variants`.
- `MASTER_STATE.md`: recorded the master integration.

## Build verification

Standalone:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  after the final display cleanup.
- Output: `extremal_hard_edge.pdf` has 55 pages and 813,196 bytes.
- Targeted log scan matched only:
  `Output written on extremal_hard_edge.pdf (55 pages, 813196 bytes).`

Master:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` twice.
- Output: `master.pdf` has 856 pages and 7,775,708 bytes.
- Copied to `~/Downloads/master.pdf`.
- Targeted log scan matched only:
  `Output written on master.pdf (856 pages, 7775708 bytes).`

Known residual diagnostics are unchanged in kind: the standalone keeps the
pre-existing `\theHfootnote` warning and known layout warnings; the master keeps
its large pre-existing warning/overfull-box background.
