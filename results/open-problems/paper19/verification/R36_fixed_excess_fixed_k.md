# R36 verification - fixed-excess fixed-k lower side

Date: 2026-06-28.

## Scope

Promote the existing fixed-excess/fixed-k exponent remark into a theorem-quality
lower-side result for iid real/complex Gaussian \((m+r)\times m\) matrices, with
fixed \(r\ge0\) and fixed \(k\ge1\).

## Agent audit

Launched exactly five read-only audit agents for the active round.  All five
agreed that the exponent is \(d_\F k(k+r)\) and that theorem-quality use needs
an explicit finite-\(m\) rectangular Laguerre--Selberg tail with constants
\(C_{\F,r,k},B_{\F,r,k}\).  They also flagged the required guardrails:
real/complex Gaussian only, fixed \(r,k\), lower side only, no quaternion variant,
no proportional-excess Wishart-edge statement, and no exact law.

## Mathematical checks

- In the ordered Laguerre density for \(G^*G\), \(G\in\F^{(m+r)\times m}\), the
  hard-edge weight parameter is \(q=d_\F(r+1)/2\).
- On \(\lambda_k\le\delta\), scaling the \(k\) smallest eigenvalues gives
  \[
    \delta^{kq+d_\F\binom{k}{2}}
    = \delta^{d_\F k(k+r)/2}.
  \]
- With \(\delta=t^2\), the singular-value tail exponent is
  \(t^{d_\F k(k+r)}\).
- The cross terms are bounded by
  \[
    \prod_{i\le k<j}(\lambda_j-\lambda_i)^{d_\F}
    \le \prod_{j=1}^{m-k} y_j^{d_\F k},
  \]
  shifting the remaining Laguerre parameter from \(q\) to \(q+d_\F k\).
- The ordered-density normalization ratio
  \[
    \frac{m!}{(m-k)!}\frac{Z_{m-k}(q+d_\F k)}{Z_m(q)}
  \]
  is polynomial in \(m\) for fixed \(r,k\), by the Laguerre--Selberg product and
  Stirling's formula.
- Union bounding over \(\binom{N_m}{m+r}\) row sets gives the finite-budget
  threshold with denominator \(d_\F k(k+r)\).
- For \(N_m/m\to\gamma>1\),
  \(m^{-1}\log\binom{N_m}{m+r}\to h(\gamma)\), so the fixed-aspect lower base is
  \(h(\gamma)/(d_\F k(k+r))\).

## Files changed

- `parts/geometric.tex`: added `rect-kth:laguerre-tail`,
  `rect-kth:lower`, `rect-kth:fixed-aspect-lower`, the lower-side guardrail,
  and the almost-sure lower envelope.
- `STATE.md`: added ledger row `III.B-rect-lower` and R36 round log.
- `PLAN.md`: recorded the fixed-excess fixed-\(k\) budget under III.B.
- `extremal_hard_edge.tex`: updated the abstract summary.
- `master/chO_phase_retrieval_rmt.tex`: added compact paragraph
  `laneO:par:rect-fixed-k-lower`.
- `MASTER_STATE.md`: recorded the master integration.

## Build verification

Standalone:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  twice.
- Output: `extremal_hard_edge.pdf` has 54 pages and 802,418 bytes.
- Targeted log scan matched only:
  `Output written on extremal_hard_edge.pdf (54 pages, 802418 bytes).`

Master:

- Command: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` twice.
- Output: `master.pdf` has 856 pages and 7,773,478 bytes.
- Copied to `~/Downloads/master.pdf`.
- Targeted log scan matched only:
  `Output written on master.pdf (856 pages, 7773478 bytes).`

Known residual diagnostics are unchanged in kind: the standalone keeps the
pre-existing `\theHfootnote` warning and the known `parts/ldp.tex` overfull box;
the master retains its large pre-existing warning/overfull-box background.
