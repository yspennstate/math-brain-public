# R20 verification - square row-wise heterogeneous-density budget

## Scope

Round R20 checked whether the concrete square row-submatrix lower side can keep
row-dependent scalar density bounds, instead of using one global \(K_m\).  This
is a reader-facing application of the R19 nonuniform finite-budget corollary.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0c55-0223-7c60-bb56-c7e0e6e2f105` checked the distance-to-hyperplane
   proof and confirmed the one-row constants \(C_\R=2\), \(C_\C=\pi\).
2. `019f0c55-2283-7a72-86a9-0adbe81a6482` checked the finite-family budget and
   the identity
   \[
     \sum_{|T|=m}\sum_{i\in T}\kappa_i
     =\binom{N-1}{m-1}\sum_i\kappa_i .
   \]
3. `019f0c55-3bb6-73b0-b4c8-7eecfba7cb0b` checked manuscript placement and
   recommended a corollary after the square finite-entropy result.
4. `019f0c55-51d3-7e02-b4d8-e3b818cd4017` red-teamed random budgets, singular
   parts, complex-density assumptions, nonuniform exponents, and value-dependent
   row families.
5. `019f0c55-6df4-7ed1-bf34-5f98556ab61d` checked ledger/master updates and
   noted that the result is expository relative to R19, but useful as a concrete
   square-row formula.

## Result

For a fixed \(m\)-row set \(T\), if row \(i\) has scalar density bound
\(K_{m,i}\) uniformly over columns, then
\[
  \PP\{\smin(A_{m,T})\le t\}
  \le C_\F m^{d_\F}t^{d_\F}\sum_{i\in T}K_{m,i},\qquad 0<t\le1.
\]
Summing this over all \(m\)-row sets and applying
Corollary~\(\ref{cor:nonuniform-finite-budget}\) gives the budget
\[
  \Lambda_m^{\rm row}
  =
  \log\binom{N_m-1}{m-1}
  +\log\sum_{i=1}^{N_m}K_{m,i}.
\]
The finite threshold has numerator
\[
  \Lambda_m^{\rm row}+d_\F\log m+O_\F(1)+u_m.
\]
If \(K_{m,i}=K_m\) for all rows, this recovers the existing uniform budget
\(\log\binom{N_m}{m}+\log K_m+(d_\F+1)\log m+O_\F(1)+u_m\).

## Guardrails

The row bounds are deterministic and uniform over columns.  More general
coordinate-wise bounds are safe only after replacing \(K_{m,i}\) by the row
maximum.  The complex case requires genuine two-real-dimensional densities on
\(\C\simeq\R^2\).  Singular or atomic components, random/value-dependent
budgets, nonuniform exponents, and matching upper/exact-base claims are not
covered.

## Manuscript changes

- `parts/universality.tex`: added `cor:rowwise-heterogeneous-square`.
- `master/chO_phase_retrieval_rmt.tex`: added a compact row-wise heterogeneous
  budget sentence in Lane O's finite-entropy paragraph.
- `PLAN.md`, `STATE.md`, and `MASTER_STATE.md` were updated.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
was run twice from `paper19/`; the final standalone PDF is 34 pages /
569,034 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` was run twice
from `math-open-problems-fleet/master/`; the final master PDF is 853 pages /
7,757,924 bytes and was copied to `~/Downloads/master.pdf`.

Targeted log scans found no LaTeX errors, undefined control sequences,
undefined references, undefined citations, fatal stops, emergency stops, or
rerun requests.  The only targeted matches were the two expected
`Output written` lines.
