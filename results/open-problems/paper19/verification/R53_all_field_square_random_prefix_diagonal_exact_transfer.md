# R53 verification -- all-field square random-prefix diagonal exact transfer

Date: 2026-06-28.

## Scope

This round adds `cor:random-prefix-square-diagonal-exact`.  It packages the
exact square random-prefix Gaussian laws over `F in {R,C,H}` with the pathwise
two-sided diagonal sandwich.

The statement is square-only.  It does not assert a fixed-excess exact law, a
row-Gram theorem for `r>0`, selected-submatrix column normalization, non-diagonal
covariance transfer, quaternionic non-real diagonal weights, condition-number
only covariance control, value-dependent row selection, or an almost-sure exact
law.

## Agent audits

Exactly five read-only agents were launched and all completed.

- Bernoulli (`019f0e95-695f-7d51-9b63-cf1ab12b0ef8`) checked constants and
  duplication.  It required a fixed positive convention on `{N_m<m}`, positive
  finite real weights, the two-sided sandwich, and a separate lower-envelope
  source for the real/complex a.s. claim.
- Confucius (`019f0e95-91c0-7462-b2c0-ebfad37f1339`) verified the linear
  algebra over `R`, `C`, and `H`, including the doubled normalized Gram base.  It
  warned to avoid Loewner-order claims when the right diagonal factor is present.
- Lorentz (`019f0e95-ae3b-7511-b482-e3acb28d7d67`) recommended a short named
  corollary after `cor:quat-random-prefix-conditioning-exact`, noting that the
  ingredients were present but not as one all-field exact diagonal statement.
- Pascal (`019f0e95-c6d4-7593-a097-aee0825b0a75`) supplied the probability
  proof skeleton: the log difference from the unweighted prefix statistic is at
  most `Delta_m/m`, so exact convergence follows by Slutsky; a.s. assumptions
  transfer lower envelopes only.
- Faraday (`019f0e95-d919-7742-a2ee-500d6a6db02b`) stress-tested the statement
  and passed it only with strict restrictions: prefix counts, global per-row and
  per-column weights, absolute scale control, positive real quaternion weights,
  full-prefix column normalization only, and no condition-number-only shortcut.

## Proof audit

On `{N_m>=m}`, for each `T subset [N_m]` with `|T|=m`,
`B_T=D_T G_T E` satisfies

```text
exp(-Delta_m) smin(G_T) <= smin(B_T) <= exp(Delta_m) smin(G_T).
```

Taking minima gives the same two-sided logarithmic comparison between the
weighted and unweighted square prefix statistics.  The unweighted source is
`thm:random-row-count-gaussian` for `R,C` and
`thm:quat-random-row-count-gaussian` for `H`.  The event `{N_m<m}` has
probability tending to zero and uses a fixed positive convention.

For normalized column Gram variables, use only
`lambda_min(m^{-1}B_T^*B_T)=m^{-1}smin(B_T)^2`, so the base doubles.  The a.s.
lower-envelope statement uses only the lower side of the sandwich, together with
`cor:random-row-count-bd` at `kappa=0` for `R,C` and the a.s. part of
`thm:quat-random-row-count-gaussian` for `H`.

## Build

Standalone build from `paper19`:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Result: `extremal_hard_edge.pdf`, 70 pages, 928,441 bytes, last written
2026-06-28 17:22:10.

Targeted log scan: no undefined citations, no undefined references, and no
rerun request.  Remaining diagnostics are the existing `\theHfootnote` warning
and the known overfull hbox in `parts/ldp.tex` lines 81--89.

No standalone `pdflatex`, `bibtex`, `lean`, `lake`, or `elan` process remained
after verification.
