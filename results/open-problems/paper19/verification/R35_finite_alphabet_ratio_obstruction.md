# R35 verification - finite alphabet quotient obstruction

Date: 2026-06-28.

Target: generalize the deterministic sign obstruction to finite nonzero
alphabets, while preserving the PARTIAL status of random atomic thresholds.

Five tool-managed audit agents were launched.  All five completed.  The
consensus conservative statement is the nonzero alphabet quotient theorem over
\(\R\) or \(\C\); zero-containing alphabets and quaternion/projective variants
were left out to avoid side-convention and projective-pair bookkeeping.

Verified statement:

Let \(S\subset\mathbb K^\times\) be finite and nonempty for
\(\mathbb K\in\{\R,\C\}\), and let \(q=|S/S|\).  For \(m\ge2\), if
\(N\ge q(m-1)+1\), then every matrix in \(S^{N\times m}\) has a singular
\(m\times m\) row submatrix.

Proof audit:

- Use only columns 1 and 2.
- Each row has quotient \(A_{i1}A_{i2}^{-1}\in S/S\).
- Pigeonhole gives at least \(m\) rows with the same quotient.
- On those rows, column 1 is a scalar multiple of column 2, so the selected
  square row submatrix is singular.
- For signs, \(S=\{\pm1\}\) gives \(|S/S|=2\), recovering \(N\ge2m-1\).

Guardrails:

- The alphabet is required to be nonzero.  Zero-containing alphabets need
  projective-pair bookkeeping and are not claimed.
- The statement is over \(\R\) and \(\C\).  Quaternion versions require
  right-ratio conventions and were not integrated.
- This is deterministic and does not prove a high-probability singular-minor
  threshold below \(q(m-1)+1\).
- `II.C` remains PARTIAL; the new theorem is a PROVEN deterministic subresult.
- No Toeplitz, Hankel, circulant, or structured-symbol matrix scope is involved.
- No new bibliography, numerics, or Lean changes were made.  The existing Lean
  file remains a certificate for the sign case only.

Supersession note:

- R37 extends this nonzero-alphabet quotient theorem to finite alphabets that
  may contain zero, using projective first-two-coordinate classes.  This R35
  note remains the audit record for the nonzero quotient specialization.

Build verification:

- `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  passed twice after the edits.
- Final `extremal_hard_edge.pdf`: 52 pages, 794,348 bytes, last written
  2026-06-28 10:10:18 local time.
- Targeted standalone log scan found no undefined citations/references and no
  rerun request. Remaining diagnostics are the known `\theHfootnote` warning,
  the pre-existing overfull hbox in `parts/ldp.tex`, and an underfull vbox on
  the numerics figure page.
- No `pdflatex`, `bibtex`, `lean`, `lake`, or `elan` processes remained after
  the final check.
