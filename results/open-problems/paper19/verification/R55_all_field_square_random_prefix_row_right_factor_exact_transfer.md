# R55 verification -- all-field square random-prefix row/right-factor exact transfer

Date: 2026-06-28.

## Scope

This round upgrades the R53 all-field square diagonal transfer into
`cor:random-prefix-square-row-right-factor-exact`.  The theorem now allows
positive real prefix row weights and one global all-column right factor
`S_m in GL_m(F)` over `F in {R,C,H}`.  Positive column diagonals, row
normalization, and full-prefix column normalization remain included as special
cases.  The old diagonal label is kept as an alias on the same corollary.

The result is square row-submatrix only.  It does not cover selected-column or
two-sided non-diagonal covariance, selected-submatrix column normalization,
fixed-excess exact laws, row-Gram statements for `r>0`, value-dependent row
selection, condition-number-only covariance control, or almost-sure exact laws.

## Agent audits

Exactly five read-only agents were launched and all completed.

- Euclid (`019f0e9d-1e0e-74f3-a1b3-432b3325af73`) passed the statement as a
  direct pathwise transfer, with constants `-h(gamma)/d_F` and
  `-2h(gamma)/d_F`.
- Euler (`019f0e9d-34db-7121-962e-da931790ed76`) verified the row-only
  singular-value bounds and explained why a global right factor is safe for row
  selection but not for selected-column or two-sided minors.
- Hilbert (`019f0e9d-49f2-7162-a9d2-ca3927f902c7`) recommended upgrading the
  existing R53 diagonal corollary rather than adding a redundant parallel
  theorem.
- Feynman (`019f0e9d-5dc0-71f0-b991-8d88f1c9ab39`) checked the probability
  proof and the a.s. lower-envelope sources for `R,C,H`.
- Dewey (`019f0e9d-73cb-7e61-8f14-4be275cc61f7`) stress-tested the theorem and
  emphasized absolute scale control; condition number alone fails by
  `S_m=e^{cm}I`.

## Proof audit

On `{N_m>=m}`, for every `T subset [N_m]` with `|T|=m`,

```text
B_T = D_T G_T S_m
```

and

```text
exp(-Delta_m) smin(G_T) <= smin(B_T) <= exp(Delta_m) smin(G_T),
```

where

```text
Delta_m=max_{i<=N_m}|log d_i|+|log smin(S_m)|+|log ||S_m|||.
```

Taking minima gives a two-sided logarithmic comparison to the unweighted
random-prefix statistic.  The unweighted exact laws are
`thm:random-row-count-gaussian` for `R,C` and
`thm:quat-random-row-count-gaussian` for `H`.  The Gram base doubles by the
identity `lambda_min(m^{-1}B_T^*B_T)=m^{-1}smin(B_T)^2`.

For a.s. lower envelopes, only the lower sandwich is used.  The sources are
`cor:random-row-count-bd` at `kappa=0` for `R,C`, and the a.s. part of
`thm:quat-random-row-count-gaussian` for `H`.

## Build

Standalone build from `paper19`:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Result: `extremal_hard_edge.pdf`, 72 pages, 936,978 bytes, last written
2026-06-28 17:33:22.

Targeted log scan: no undefined citations, no undefined references, and no
rerun request.  Remaining diagnostics are the existing `\theHfootnote` warning,
the known overfull hbox in `parts/ldp.tex` lines 81--89, and the known underfull
vbox on the numerics figure page.

No standalone `pdflatex`, `bibtex`, `lean`, `lake`, or `elan` process remained
after verification.
