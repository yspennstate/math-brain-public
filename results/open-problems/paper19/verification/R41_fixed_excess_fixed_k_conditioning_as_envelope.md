# R41 verification - fixed-excess fixed-k conditioning a.s. envelope

Date: 2026-06-28.

## Scope

Add the almost-sure lower-envelope transfer for the deterministic conditioning
corollary covering fixed-excess fixed-\(k\) singular values and normalized
column-Gram statistics.

## Agent audit

Launched exactly five read-only audit agents for the active round.  All five
approved the pathwise transfer.  The shared caveats were: use the existing
Gaussian a.s. source theorem, state only a liminf lower envelope, require
deterministic or a.s. absolute \(e^{o(m)}\) conditioning factors on the common
coupling, and do not weaken covariance control to condition number control.

## Mathematical checks

- The proof of `cor:fixed-excess-fixed-k-transfer` gives, uniformly over
  \(|T|=m+r\),
  \[
    \alpha_m\sigma_{m-k+1}(G_{m,T})
    \le \sigma_{m-k+1}(A_{m,T})
    \le \beta_m\sigma_{m-k+1}(G_{m,T}),
  \]
  with
  \(\alpha_m=(\min_i d_{im})\sqrt{\lambda_{\min}(\Sigma_m)}\).
- Under the hypotheses of `prop:cov-transfer`,
  \(m^{-1}\log\alpha_m\to0\).  Hence
  \[
    M_A^{(r)}[k]\ge \alpha_m M_G^{(r)}[k]
  \]
  transfers any a.s. Gaussian liminf lower bound.
- `cor:as-geometric-lower-envelopes` already supplies
  \[
    \liminf_m m^{-1}\log M_G^{(r)}[k]
    \ge -h(\gamma)/(d_\F k(k+r))
  \]
  on common couplings.
- Squaring the same comparison transfers the normalized column-Gram statistic;
  the factor \((m+r)^{-1}\) contributes only \(o(1)\) after division by \(m\).
- No new summability is needed at the transfer stage.  Summability only belongs
  to proving the Gaussian a.s. source envelope or to proving random conditioning
  extrema are a.s. subexponential.

## Files changed

- `parts/ensembles.tex`: added a.s. lower-envelope displays to
  `cor:fixed-excess-fixed-k-transfer` and proof text citing
  `cor:as-geometric-lower-envelopes`.
- `STATE.md`: broadened row `V.B` and added the R41 round log.
- `PLAN.md`: recorded the common-coupling a.s. conditioning transfer under V.B.
- `master/chO_phase_retrieval_rmt.tex`: added the compact master sentence to
  `laneO:cor:conditioning-variants`.
- `MASTER_STATE.md`: recorded the master integration.

## Build verification

Standalone:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  twice.
- Output: `extremal_hard_edge.pdf` has 59 pages and 850,940 bytes.
- Targeted log scan matched only:
  `Output written on extremal_hard_edge.pdf (59 pages, 850940 bytes).`

Master:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` twice.
- Output: `master.pdf` has 856 pages and 7,775,984 bytes.
- Copied to `~/Downloads/master.pdf`.
- Targeted log scan matched only:
  `Output written on master.pdf (856 pages, 7775984 bytes).`

Known residual diagnostics are unchanged in kind: the standalone keeps the
pre-existing `\theHfootnote` warning and known layout warnings; the master keeps
its large pre-existing warning/overfull-box background.
