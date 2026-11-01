# R12 verification - random column preconditioning

## Scope

Round R12 adds:

- a pathwise random positive column-diagonal transfer theorem;
- Gaussian column-normalized row-submatrix matrices;
- diagonal coordinate preconditioning for real critical Gaussian phase-retrieval frames;
- the corresponding compact Lane O master entry.

## Five-agent audit

Exactly five read-only agents were launched and then closed.

1. `019f0a22-7232-7ba3-be29-abe49dd518ee` checked the pathwise column-weight theorem.
2. `019f0a22-8ded-7ad1-ad35-45ae95918270` checked Gaussian column normalization and the column-norm tails.
3. `019f0a22-a021-7653-8711-cd336a760c18` checked phase-retrieval/full-spark implications.
4. `019f0a22-b164-7fa0-bd02-8210a7b5906d` checked almost-sure lower-envelope transfer.
5. `019f0a22-c714-7ee1-967c-4c8ea62e44c3` checked integration with the two-sided diagonal caveat and Lane O notation.

## Audit conclusions

The theorem is pathwise: for \(B=A E\), with \(E\) positive diagonal,
\[
  (B)_{R,C}=A_{R,C}E_C,
\]
so every selected singular value is sandwiched by the minimum and maximum
selected column weights.  No independence between \(E\) and \(A\) is required.

Required hypotheses were added: the selected family is nonempty, the diagonal
entries are strictly positive and finite, and logarithms are only taken on
\(\{M(A)>0\}\).  Convergence transfer requires \(M(A)>0\) with high probability
and subexponential logarithmic extrema.  Almost-sure transfer requires
subexponential extrema almost surely or summable tails.

For Gaussian column normalization, if \(R_{jm}=\|G_me_j\|_2\), then
\[
  \max_{j\le m}|\log R_{jm}|=o(m)
\]
almost surely.  The upper tail is summable by Markov's inequality, while the
lower tail is summable by a ball-volume bound in real dimension \(d_\F N_m\).

For phase retrieval, right multiplication by an invertible diagonal matrix
preserves full spark and the complement property.  This is coordinate
preconditioning of the unknown signal, not measurement-vector normalization.
It preserves the Balan--Wang exponential base when the diagonal entries have
subexponential logarithmic extrema, \(\max_j|\log e_j|=o_P(m)\).  It preserves
almost-sure lower envelopes only under the corresponding almost-sure
subexponential extrema condition.

The two-sided caveat remains: diagonal column scaling commutes with column
selection, but non-diagonal column covariance does not.

## Build verification

After integration:

- `paper19/extremal_hard_edge.pdf`: 27 pages, 512048 bytes.
- `master/master.pdf`: 852 pages, 7751921 bytes.
- `master/master.pdf` was copied to `~/Downloads/master.pdf`.

Targeted log scans found no undefined references or citations, no rerun request,
and no LaTeX error/fatal/emergency stop.  Remaining diagnostics are the existing
`\theHfootnote` warning and legacy box/hyperref warnings.
