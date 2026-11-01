# R54 verification -- random-prefix all-column fixed-excess fixed-k lower sides

Date: 2026-06-28.

## Scope

This round adds `cor:random-prefix-right-factor-fixed-excess-fixed-k-lower`.
It packages the R51 random-prefix fixed-excess fixed-`k` lower side with one
global all-column right factor over `F in {R,C,H}`.  The proposed result was
audited as the next round, but is recorded as R54 because the existing R53 file
already covers the all-field square random-prefix diagonal exact transfer.

For an infinite iid Gaussian row array, possibly dependent prefix counts
`N_m/m -> gamma>1`, fixed `r>=0,k>=1`, positive real row weights over the
realized prefix, and one global invertible `S_m in F^{m x m}`, assume

```text
Delta_m^rpcond =
max_{i<=N_m}|log d_im| + |log smin(S_m)| + |log opnorm(S_m)| = o_P(m).
```

Then the singular lower base remains `h(gamma)/(d_F k(k+r))`, and the
normalized column-Gram lower base remains `2h(gamma)/(d_F k(k+r))`.  A.s. count
convergence plus `Delta_m^rpcond=o(m)` transfers lower envelopes.

The result is lower-side only.  It does not claim an upper side, an exact
fixed-excess law, a row-Gram theorem for `r>0`, condition-number-only covariance
transfer, selected-column covariance, value-dependent row selection,
selected-submatrix column normalization, proportional Wishart-edge behavior, or
a Balan-Wang/supercritical phase-retrieval conclusion.

## Agent audits

Exactly five read-only agents were launched and all completed.

- Mendel (`019f0e9b-340f-7d41-9a83-400e9c6ba4c9`) passed the singular-value
  transfer.  The pathwise lower sandwich is uniform in the selected row set and
  uses no independence.
- Hilbert (`019f0e9b-349e-7022-85ef-f616750cff7e`) passed the normalized
  column-Gram transfer.  The normalization is `(m+r)^-1`, and the right-factor
  error doubles at the Gram level.
- Lorentz (`019f0e9b-3516-7851-9c8f-843384853ca0`) checked examples and
  exclusions.  Positive column diagonals, full-column covariance/whitening
  factors with absolute singular-scale control, row normalization, and
  full-prefix column normalization are safe examples.
- Pauli (`019f0e9b-357d-7243-889f-2d7f2a605982`) checked probability and a.s.
  logic.  The singular split uses `Delta <= eps m/2`; the Gram split uses
  `Delta <= eps m/4` because the Gram sandwich has doubled error.
- McClintock (`019f0e9b-35e7-7701-8b4f-5f9a19617e4a`) checked integration,
  placement, labels, and the R54 numbering to avoid conflict with existing R53.

## Proof audit

On `{N_m>=m+r}`, for every selected `T` with `|T|=m+r`,

```text
B_T = diag(d_im : i in T) G_T S_m
```

and the min-max singular-value inequality gives

```text
sigma_{m-k+1}(B_T) >= exp(-Delta_m^rpcond) sigma_{m-k+1}(G_T).
```

Taking minima over `T` gives the random-prefix singular lower sandwich.  For
`c=h(gamma)/(d_F k(k+r))`,

```text
P{M_B <= exp(-(c+eps)m)}
 <= P{Delta_m^rpcond > eps m/2}
  + P{M_G(N_m) <= exp(-(c+eps/2)m)}.
```

The first term vanishes by the conditioning hypothesis and the second by R51.
No independence between count, rows, row weights, or right factor is used.

For the normalized column Gram,

```text
lambda_(k)((m+r)^-1 B_T^* B_T)
 = (m+r)^-1 sigma_{m-k+1}(B_T)^2,
```

so `Lambda_B >= exp(-2 Delta_m^rpcond) Lambda_G(N_m)`.  The lower-tail split is

```text
P{Lambda_B <= exp(-(2c+eps)m)}
 <= P{Delta_m^rpcond > eps m/4}
  + P{Lambda_G(N_m) <= exp(-(2c+eps/2)m)}.
```

For `F=H`, positive real row weights are central and the right factor is one
global quaternionic right multiplication; the same singular-value sandwich
applies.  The `+infty` convention on `{N_m<m+r}` is used only for the extended
statistics, and the sandwich is stated on the feasible event.

## Build

Standalone build from `paper19`:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Result: `extremal_hard_edge.pdf`, 72 pages, 936,170 bytes.

Master build from `math-open-problems-fleet/master`:

```text
pdflatex -interaction=nonstopmode -halt-on-error master.tex
pdflatex -interaction=nonstopmode -halt-on-error master.tex
```

Result: `master.pdf`, 859 pages, 7,795,044 bytes.  The rebuilt master PDF was
copied to `~/Downloads/master.pdf` with the same byte size.

Targeted log scans found no undefined citations, undefined references,
multiply-defined labels, or rerun requests; the scans only returned the
expected `Output written` lines.  No `pdflatex`, `bibtex`, `lean`, `lake`, or
`elan` process remained after verification.
