# R14 verification - supercritical phase retrieval reduction killed

## Scope

Round R14 tested whether the real supercritical Balan--Wang singular-value
statistic at \(N=2m-1+r\), \(r>0\), reduces to the fixed-excess row-submatrix
minimum
\[
  \min_{|T|=m+r}\sigma_{\min}(A_T).
\]

## Five-agent audit

Exactly five read-only agents were launched and then closed.

1. `019f0a35-e0a5-7011-9716-ec92ebd3ebfc` checked the proposed deterministic reduction.
2. `019f0a35-ffe0-76d3-8d08-29dbda320a37` checked the fixed-excess lower-side consequence if the reduction were valid.
3. `019f0a36-132c-72f2-9908-ad03496d6de7` checked normalization/preconditioning transfers.
4. `019f0a36-27ac-7c02-8a85-43df00df17ef` checked integration placement and guardrails.
5. `019f0a36-44bb-70f1-b26b-914456d326d9` adversarially checked counterexamples.

## Outcome

The proposed supercritical reduction is false for \(r>0\) under the
Balan--Wang partition/minimum convention.  For full-spark \(A\), the
fixed-excess statistic equals the branch where the complementary side has at
most \(m-1\) rows and therefore fails to span.  But for \(N=2m-1+r\), \(r>0\),
there are also partitions with both sides spanning:
\[
  m\le |S|\le m+r-1.
\]
These both-spanning partitions can control the Balan--Wang minimum.

The correct schematic decomposition is
\[
  \omega(A)=
  \min\left\{
    \min_{|T|=m+r}\sigma_{\min}(A_T),
    \min_{m\le |S|\le m+r-1}
      \max(\sigma_{\min}(A_S),\sigma_{\min}(A_{S^c}))
  \right\},
\]
up to the exact convention used for \(\omega\).

The adversarial audit supplied a concrete \(m=2,r=1,N=4\) full-spark family in
which a two-versus-two partition makes the Balan--Wang statistic arbitrarily
small while every three-row submatrix remains well conditioned.  Therefore no
supercritical Balan--Wang lower-side corollary was added.

## Manuscript changes

The existing supercritical warning in `parts/phaseretrieval.tex` and the R13
verification note were corrected: fixed-excess tall submatrices are now stated
to be only one branch of the supercritical partition problem, not an exact
supercritical Balan--Wang reduction.  The diagonal preconditioning wording was
also corrected from "subexponential condition number" to "subexponential
logarithmic extrema"; a scalar factor \(e^m I\) has condition number one but
changes the absolute singular-value exponent.

## Build verification

After these corrections, the standalone manuscript compiled to
`extremal_hard_edge.pdf` with 29 pages and 525354 bytes.  The fleet master
compiled to `master.pdf` with 852 pages and 7752261 bytes, and the same file was
copied to `~/Downloads/master.pdf`.  Targeted log scans showed no
LaTeX errors, undefined references/citations, or rerun requests.
