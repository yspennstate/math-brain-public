# R38 verification - fixed-excess fixed-k Gram transfer

Date: 2026-06-28.

## Scope

Add the normalized column-Gram transfer of the R36 fixed-excess fixed-\(k\)
singular-value lower side.

## Agent audit

Launched exactly five read-only audit agents for the active round.  All five
approved the transfer with these guardrails: use the column Gram
\(A_{m,T}^*A_{m,T}\), normalize by \(m+r\), keep \(r,k\) fixed, use row sets
\(|T|=m+r\), and state only a lower-side result.  No row-Gram statement for
\(r>0\), quaternion variant, upper side, exact law, or proportional-excess
Wishart-edge statement is justified.

## Mathematical checks

- For \(A_{m,T}\in\F^{(m+r)\times m}\), the nonzero singular values satisfy
  \[
    \lambda_{(k)}(A_{m,T}^*A_{m,T})
    =
    \sigma_{m-k+1}(A_{m,T})^2
  \]
  when eigenvalues are ordered increasingly and singular values decreasingly.
- The normalized statistic is
  \[
    \Lambda_m^{(r)}[k]
    =
    \min_{|T|=m+r}
    \lambda_{(k)}((m+r)^{-1}A_{m,T}^*A_{m,T})
    =
    (m+r)^{-1}(M_m^{(r)}[k])^2 .
  \]
- Therefore the finite-budget threshold is the squared R36 singular-value
  threshold multiplied by \((m+r)^{-1}\):
  \[
    (m+r)^{-1}
    \exp\left[
      -{2\bigl(\log\binom{N_m}{m+r}+B\log m+\log C+u_m\bigr)
      \over d_\F k(k+r)}
    \right].
  \]
- The factor \((m+r)^{-1}\) contributes only \(-\log(m+r)\) to the log scale, so
  for fixed \(r\) it does not affect the \(m^{-1}\log\) lower base.
- If \(N_m/m\to\gamma>1\), the fixed-aspect lower base is
  \(2h(\gamma)/(d_\F k(k+r))\).
- Edge cases are consistent: \(r=0\) recovers the square fixed-\(k\) Gram lower
  side; \(k=1\) recovers the fixed-excess minimum-eigenvalue column-Gram
  transfer.

## Files changed

- `parts/geometric.tex`: added `rect-kth:gram-lower` and the corresponding
  almost-sure lower envelope.
- `STATE.md`: added ledger row `III.B-rect-gram` and R38 round log.
- `PLAN.md`: recorded both square and fixed-excess fixed-\(k\) Gram lower bases.
- `extremal_hard_edge.tex`: updated the abstract phrase to plural Gram transfers.
- `master/chO_phase_retrieval_rmt.tex`: added compact paragraph
  `laneO:par:rect-fixed-k-gram-lower`.
- `MASTER_STATE.md`: recorded the master integration.

## Build verification

Standalone:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  twice.
- Output: `extremal_hard_edge.pdf` has 54 pages and 807,346 bytes.
- Targeted log scan matched only:
  `Output written on extremal_hard_edge.pdf (54 pages, 807346 bytes).`

Master:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` twice.
- Output: `master.pdf` has 856 pages and 7,774,714 bytes.
- Copied to `~/Downloads/master.pdf`.
- Targeted log scan matched only:
  `Output written on master.pdf (856 pages, 7774714 bytes).`

Known residual diagnostics are unchanged in kind: the standalone keeps the
pre-existing `\theHfootnote` warning and known layout warnings; the master keeps
its large pre-existing warning/overfull-box background.
