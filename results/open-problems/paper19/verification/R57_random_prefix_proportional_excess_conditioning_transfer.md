# R57 verification -- random-prefix proportional-excess conditioning transfer

## Scope

Added `rect:random-prefix-proportional-conditioning-transfer` in
`parts/geometric.tex`, immediately after the R56 random-prefix
proportional-excess lower-side corollary.

The result is a real/complex pathwise lower-side transfer from the R56
independent-entry base array.  For

```text
B_T = diag(d_im : i in T) A_T S_m,
Delta = max_{i<=N_m}|log d_im| + |log smin(S_m)| + |log opnorm(S_m)|,
```

with `Delta=o_P(m)`, the R56 lower thresholds are preserved:

- singular values: `kappa/d_F`;
- selected-row normalized column Gram `ell_m^{-1}B_T^*B_T`: `2 kappa/d_F`.

A.s. prefix convergence plus `Delta=o(m)` a.s. gives the corresponding lower
envelopes.

## Audit

Five read-only audit agents were launched and closed.

- Plato `019f0eaf-ba9c-7f12-843c-15c2a32e91c4`: confirmed the row/right-factor
  singular-value sandwich and warned not to restate this as a density theorem
  for the conditioned matrix.
- Feynman `019f0eaf-d505-7860-8a61-d2075f1c9904`: checked the positive
  diagonal specialization, Gaussian row normalization, full-prefix Gaussian
  column normalization, and the non-Gaussian row-normalization caveat.
- Schrodinger `019f0eaf-f417-7111-a17d-b7edad27eb7a`: checked the normalized
  column-Gram sandwich, confirming `ell_m^{-1}` normalization and the
  `epsilon m/4` split.
- Ampere `019f0eb0-0a93-7bc0-a1e0-b41f0a363b64`: checked placement, labels,
  state row id, verification filename, and R56/R57 caveat coordination.
- Turing `019f0eb0-40d6-7cf3-b2e0-3a618e33da40`: checked the probability and
  a.s. composition, including the deterministic upper prefix bracket.

## Proof Check

For `c=kappa/d_F` and `n_m^+=ceil(gamma_+m)`, on
`{N_m<=n_m^+}` the pathwise sandwich gives

```text
M_B(N_m) >= exp(-Delta_m) M_A(n_m^+).
```

Therefore

```text
P{M_B <= exp(-(c+eps)m)}
 <= P{Delta_m>eps m/2}
  + P{N_m>n_m^+}
  + P{M_A(n_m^+) <= exp(-(c+eps/2)m)} -> 0.
```

The Gram statistic satisfies

```text
Lambda_B(N_m) >= exp(-2 Delta_m) Lambda_A(n_m^+),
```

so the same proof uses `Delta_m>eps m/4` and the doubled R56 threshold.

No independence between the prefix count, row weights, right factor, and row
array is used.

## Guardrails

This is lower-side/exponential-scale only.  It does not assert that the
conditioned matrix satisfies the independent-entry density hypothesis.
Condition number alone is insufficient because scalar rescaling shifts the
exponential scale.

No quaternion extension, selected-column covariance theorem,
selected-submatrix column normalization, value-dependent row selection,
row-Gram result, proportional Wishart-edge/LDP constant, upper side, or exact
proportional-edge law is claimed.

## Integration

- `STATE.md`: added row `III.A-prop-rc-cond`, updated the R56 caveat, and added
  the R57 round log.
- `PLAN.md`: recorded the pathwise conditioning transfer separately from the
  open proportional Wishart-edge problem.
- Fleet master: added paragraph
  `laneO:par:random-prefix-proportional-conditioning-transfer`.
- `MASTER_STATE.md`: added the Lane O R57 integration note and adjusted the
  R56 caveat.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 74 pages, 953,556 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 860 pages, 7,799,977 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
