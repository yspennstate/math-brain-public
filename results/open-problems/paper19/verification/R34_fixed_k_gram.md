# R34 verification - fixed-k Gram eigenvalue lower side

Date: 2026-06-28.

Target: transfer the proved fixed-\(k\) singular-value lower side to the
\(k\)-th smallest eigenvalue of normalized Gram matrices, without promoting the
missing exact fixed-\(k\) law.

Five tool-managed audit agents were launched and completed:

- algebra/order (`019f0d05-9827-7743-938d-e1a2902861d6`): use ascending
  eigenvalues \(\lambda_{(1)}\le\cdots\le\lambda_{(m)}\), so
  \(\lambda_{(k)}(A_T^*A_T)=\sigma_{m-k+1}(A_T)^2\);
- corollary wording (`019f0d05-b6c9-73c3-b045-17450955795f`): place the formal
  finite-budget corollary immediately after `kth:lower`;
- notation (`019f0d05-f3d7-7120-a1a3-4531f7b01230`): add no new macros; use raw
  `\lambda_{(k)}` notation;
- master integration (`019f0d06-7055-7833-8ca1-c404741124f3`): add only a
  compact `\tagSYNTH` Lane O paragraph, and do not include quaternion fixed-\(k\);
- status transfer (`019f0d07-9db4-7363-8dbf-8977364c02a1`): finite-budget,
  fixed-aspect lower side, and a.s. lower envelope are proved; exact convergence
  remains equivalent to the missing codimension-\(k\) pair-correlation theorem.

Implemented:

- `parts/geometric.tex` now has `kth:gram-lower`, defining
  \[
    \Lambda_m[k]=\min_{|T|=m}
    \lambda_{(k)}(m^{-1}A_{m,T}^*A_{m,T})
    =m^{-1}M_m[k]^2
  \]
  pathwise;
- the finite-budget lower side is the squared `kth:lower` threshold, with the
  extra \(m^{-1}\) sample-covariance normalization;
- the fixed-aspect lower base is
  \[
    \liminf m^{-1}\log\Lambda_m[k]\ge
    -2h(\gamma)/(d_\mathbb F k^2)
  \]
  in probability;
- `cor:as-geometric-lower-envelopes` now includes the fixed-\(k\) singular-value
  and fixed-\(k\) normalized Gram a.s. lower envelopes;
- `master/chO_phase_retrieval_rmt.tex` now contains
  `laneO:par:fixed-k-gram-lower`.

Guardrails:

- Scope is iid Gaussian over \(\mathbb R,\mathbb C\), matching the existing
  fixed-\(k\) Laguerre tail.
- No quaternion fixed-\(k\) claim was added.
- No exact fixed-\(k\) Gram law was claimed; exact convergence remains
  conjectural with the singular-value fixed-\(k\) law.
- No proportional Wishart-edge claim was added.

Build:

- Standalone `pdflatex` passed twice after the fixed-\(k\) Gram and
  finite-alphabet edits.
- Final standalone PDF: 52 pages, 794,348 bytes.
- Master `pdflatex` passed twice and was copied to
  `~/Downloads/master.pdf`.
- Final master PDF: 855 pages, 7,770,973 bytes.
- Targeted standalone log scan found no undefined citations/references and no
  rerun request. Remaining standalone diagnostics are the known
  `\theHfootnote` warning, the pre-existing overfull hbox in `parts/ldp.tex`,
  and an underfull vbox on the numerics figure page.
- No `pdflatex`, `bibtex`, `lean`, `lake`, or `elan` processes remained after
  the final check.
