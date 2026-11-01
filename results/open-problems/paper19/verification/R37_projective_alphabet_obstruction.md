# R37 verification - finite alphabet projective-pair obstruction

Date: 2026-06-28.

Target: extend the R35 nonzero-alphabet quotient obstruction to finite alphabets
that may contain zero, without claiming random atomic thresholds or touching
the sign-case Lean certificate.

Five tool-managed audit agents were launched.  All five completed.  The
consensus statement is the projective-pair theorem over \(\R\) and \(\C\),
with the all-zero alphabet handled separately.

Verified statement:

Let \(S\subset\mathbb K\) be finite and nonempty for
\(\mathbb K\in\{\R,\C\}\), and let
\[
  \Pi(S)=\{[a:b]\in\mathbb P^1(\mathbb K):a,b\in S,\ (a,b)\ne(0,0)\}.
\]
For \(m\ge2\), if either \(S=\{0\}\) and \(N\ge m\), or \(S\ne\{0\}\) and
\[
  N\ge |\Pi(S)|(m-1)+1,
\]
then every matrix in \(S^{N\times m}\) has a singular \(m\times m\) row
submatrix.

Proof audit:

- A nonzero first-two-entry pair determines a projective class \([u:v]\).
- A row with first two entries \((0,0)\) is not a projective point, but it is
  compatible with every projective class because it satisfies
  \(vA_{i1}-uA_{i2}=0\) for all \([u:v]\).
- If \(z\) is the number of zero-zero rows and \(n_\pi\) is the number of
  nonzero rows in class \(\pi\), then \(z+n_\pi\ge m\) gives \(m\) rows on
  which the first two columns satisfy one nontrivial linear relation.
- If all \(z+n_\pi\le m-1\), then with \(L=|\Pi(S)|\),
  \[
    N=z+\sum_\pi n_\pi
    \le z+L(m-1-z)
    =L(m-1)-(L-1)z
    \le L(m-1),
  \]
  contradicting \(N\ge L(m-1)+1\).
- If \(S=\{0\}\), every selected \(m\)-row submatrix is zero once \(N\ge m\).
- When \(0\notin S\), the map \([a:b]\mapsto ab^{-1}\) identifies
  \(\Pi(S)\) with \(S/S\), recovering R35.

Guardrails:

- The \(+1\) is necessary.  For \(S=\{0,1\}\), \(m=2\), the three rows
  \((1,0),(0,1),(1,1)\) represent the three projective classes and have no
  singular two-row submatrix.
- This is deterministic and does not prove a high-probability singular-minor
  threshold below the projective-pair row count.
- The theorem is over \(\R\) and \(\C\).  Quaternion/right-ratio variants were
  not integrated.
- No Lean change was made.  `lean/SignCritical.lean` remains a certificate for
  the real sign case.
- The atomic numerics remain a nonzero-alphabet quotient specialization; the
  manuscript language was softened so sampled below-threshold behavior is only
  illustrative.

Build verification:

- `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  passed twice after the edits.
- Final `extremal_hard_edge.pdf`: 55 pages, 809,343 bytes, last written
  2026-06-28 10:47:07 local time.
- Targeted standalone log scan found no undefined citations/references and no
  rerun request. Remaining diagnostics are the known `\theHfootnote` warning,
  the pre-existing overfull hbox in `parts/ldp.tex`, and an underfull vbox on
  the numerics figure page.
- No `pdflatex`, `bibtex`, `lean`, `lake`, or `elan` processes remained after
  the final check.
