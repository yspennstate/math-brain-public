# R52 verification -- random-prefix diagonal/normalized fixed-excess fixed-k lower sides

Date: 2026-06-28.

## Scope

This round adds `cor:random-prefix-diagonal-fixed-excess-fixed-k` to
package the R51 random-prefix fixed-excess fixed-`k` lower side with positive
real diagonal row/column factors over the realized prefix.

For `F in {R,C,H}`, fixed `r>=0,k>=1`, possibly dependent prefix counts
`N_m/m -> gamma>1`, and realized-prefix diagonal log-extreme
`Delta_m^rpdiag=o_P(m)`, the singular lower base remains
`h(gamma)/(d_F k(k+r))`, and the normalized column-Gram lower base remains
`2h(gamma)/(d_F k(k+r))`.  A.s. count convergence plus
`Delta_m^rpdiag=o(m)` transfers lower envelopes.  Row-normalized random-prefix
Gaussian rows and full-prefix column-normalized Gaussian columns are included.

The result is intentionally lower-side only.  It does not claim an upper side,
an exact fixed-excess law, a row-Gram theorem for `r>0`, value-dependent row
selection, selected-submatrix column normalization, non-diagonal covariance
transfer, beta interpolation, proportional Wishart-edge behavior, or a
Balan-Wang/supercritical phase-retrieval conclusion.

## Agent audits

Exactly five read-only agents were launched for this active R52 pass and all
completed.

- Dirac (`019f0e8c-27f3-7792-b0bf-dce66d534379`) passed the singular-value
  lower-side transfer by the uniform diagonal sandwich, with no independence
  needed between `N_m`, the rows, or the weights.
- Godel (`019f0e8c-2873-7cb2-bff0-f4b18a4d0148`) checked the normalized
  column-Gram side: the normalization is `(m+r)^-1`, and diagonal factors
  double the logarithmic error.
- Pascal (`019f0e8c-28e2-74c2-a0b3-ed09f495b92c`) checked row-normalized
  random-prefix rows and full-prefix column normalization using deterministic
  prefix brackets and Gaussian norm extrema.
- Gibbs (`019f0e8c-2943-7c81-bbba-9c6ab12cc2df`) checked the probability and
  a.s. logic, including the `+infty` convention on `{N_m<m+r}` and avoiding
  any invalid `+infty - +infty` log comparison.
- Kepler (`019f0e8c-29c4-7c30-b279-a9643a92b301`) checked integration, labels,
  state-row wording, master placement, and guardrails against non-diagonal or
  exact-law overclaims.

## Proof audit

On the feasible event `{N_m>=m+r}`, for every selected `T` with `|T|=m+r`,

```text
sigma_{m-k+1}(D_T G_T E) >= exp(-Delta_m^rpdiag) sigma_{m-k+1}(G_T).
```

Taking minima gives the random-prefix singular-value lower sandwich.  For the
normalized column Gram, the identity

```text
lambda_(k)((m+r)^-1 B_T^* B_T) = (m+r)^-1 sigma_{m-k+1}(B_T)^2
```

gives the same lower sandwich with doubled logarithmic error.  Therefore the
weighted lower-tail event is contained in the union of
`{Delta_m^rpdiag > eps m/2}` and the R51 unweighted random-prefix lower-tail
event with slack `eps/2`; the Gram case uses the same split with the doubled
error.  The a.s. envelope follows from the pathwise inequalities and the a.s.
part of R51.

For row normalization, the row-norm extrema over the realized prefix are
bounded by deterministic-prefix extrema on `{N_m<=ceil(gamma_+ m)}`.  For
full-prefix column normalization, each column norm is bracketed between
deterministic-prefix column norms on
`{floor(gamma_- m)<=N_m<=ceil(gamma_+ m)}`.  Gaussian norm upper tails and
ball-volume lower tails give the required `o_P(m)` and a.s. `o(m)` extrema.

## Build

Standalone build from `paper19`:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Result: `extremal_hard_edge.pdf`, 69 pages, 917,919 bytes.

Master build from `math-open-problems-fleet/master`:

```text
pdflatex -interaction=nonstopmode -halt-on-error master.tex
pdflatex -interaction=nonstopmode -halt-on-error master.tex
```

Result: `master.pdf`, 859 pages, 7,794,073 bytes.  The rebuilt master PDF was
copied to `~/Downloads/master.pdf` with the same byte size.

Targeted log scans found no undefined citations, undefined references,
multiply-defined labels, or rerun requests; the scans only returned the
expected `Output written` lines.  No `pdflatex`, `bibtex`, `lean`, `lake`, or
`elan` process remained after verification.
