# R33 verification - Gram and sample-covariance transfer

Date: 2026-06-28.

Target: close the V.C sample-covariance row as a deterministic transfer, while
leaving the proportional Wishart edge as an open problem.

Five tool-managed audit agents were launched and completed:

- algebra/constants (`019f0cb6-0af5-7f50-8ec9-6733e00413ad`);
- scope/integration (`019f0cb6-302e-7051-840d-8c828b9086c7`);
- notation (`019f0cb6-49ec-7730-92d5-2e4923193931`);
- master integration (`019f0cb6-6396-7d53-8139-14bc84814156`);
- stronger-consequence guardrails (`019f0cb6-7cc0-7371-9c72-14a7793d87d7`).

Verified content:

- For every selected \(q\times n\) matrix \(B\),
  \[
    \lambda_{\min}(q^{-1}B^*B)=q^{-1}\smin(B)^2.
  \]
  Hence minima over fixed-cardinality row families satisfy the same identity.
- On an \(m^{-1}\log\) scale, \(\log q=o(m)\) in the square, fixed-excess, and
  proportional row-excess regimes, so singular-value bases double for
  sample-covariance lower edges.
- Square Gaussian row submatrices give
  \[
    m^{-1}\log\min_{|T|=m}\lambda_{\min}(m^{-1}A_T^*A_T)
    \to -2h(\gamma)/d_\F
  \]
  over \(\R,\C\), and the quaternion Gaussian base gives \(-h(\gamma)/2\).
- Fixed-excess covariance statements inherit only the lower-side or conditional
  status of the underlying singular-value fixed-excess statements.
- For \(A=G\Sigma^{1/2}\), the covariance lower-edge sandwich needs
  subexponential absolute extreme eigenvalues of \(\Sigma\); a small condition
  number alone is insufficient because \(e^{cm}I\) shifts the log edge.
- For proportional excess, the exponential scale is zero, but the constant
  normalized Wishart edge remains open.

No Lean or numerical changes were made.  The identity is deterministic spectral
bookkeeping, and existing SVD-based numerics already support the singular-value
side.

Master integration:

- `master/chO_phase_retrieval_rmt.tex` now contains
  `laneO:cor:square-row-gram-transfer`;
- the master corollary records the real, complex, and quaternion square-row
  constants and explicitly excludes the proportional-excess Wishart-edge law.

Build verification:

- `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  passed twice after the edits.
- Final `extremal_hard_edge.pdf`: 50 pages, 696,452 bytes.
- Master `pdflatex` passed twice and was copied to
  `~/Downloads/master.pdf`.
- Final `master.pdf`: 855 pages, 7,769,954 bytes.
- Targeted final log scans found no undefined citations/references, no rerun
  request, and no fatal/package/LaTeX errors; each scan reported only its
  `Output written` line.
