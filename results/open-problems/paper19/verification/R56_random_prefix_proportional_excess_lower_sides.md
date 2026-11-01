# R56 verification -- random-prefix proportional-excess lower sides

## Scope

Added `rect:random-prefix-proportional-density-rate` in `parts/geometric.tex`
after `rect:moving-excess-finite-budget` and before the proportional
Wishart-edge remark.  The result is real/complex only.

For an infinite ordered row array with independent scalar entries and
density bound `K_m=exp((kappa+o(1))m)`, deterministic
`ell_m/m -> zeta in (1,gamma)`, and possibly dependent prefix counts
`N_m/m -> gamma>1`, the lower side transfers by monotonicity:

```text
P{ min_{T subset [N_m], |T|=ell_m} s_min(A_T)
    <= exp[-(kappa/d_F+eps)m] } -> 0.
```

The selected-row normalized column-Gram statistic
`lambda_min(ell_m^{-1} A_T^* A_T)` has the doubled lower threshold
`2 kappa/d_F`.  A.s. prefix-count convergence gives the corresponding
lower envelopes on common couplings.  For `K_m=e^{o(m)}` the
exponential-scale lower base is `0`.

## Audit

Five read-only audit agents were launched and closed.

- Harvey `019f0ea5-0a5d-7f22-8f46-94b995f9a101`: confirmed the Gaussian
  random-prefix proportional-excess transfer and the trivial fixed-block
  upper exponential scale.
- Arendt `019f0ea5-0ab5-7ba1-bdfe-964b0119a669`: confirmed the density-rate
  lower-side transfer and dependence caveats for prefix counts.
- Descartes `019f0ea5-0b0e-70b2-a066-da3a02e093e4`: confirmed the
  selected-row normalized column-Gram threshold is doubled and uses
  `ell_m^{-1}`, not `N_m^{-1}`.
- Volta `019f0ea5-0b66-7eb0-a6d4-cd3d7d187e65`: checked the probability and
  a.s. upper-bracket monotonicity skeleton with the `+infty` convention.
- Anscombe `019f0ea5-0baf-7be0-a7b5-20f62f4b8631`: checked placement and
  identified that the new round must be R56 because R55 is already occupied.

The proof does not condition on `N_m`; it uses only the pathwise comparison
with a deterministic prefix `ceil(gamma_+ m)`.  Therefore `N_m` may depend on
the row array, but value-dependent thinning, filtering, or reordering is not
covered.

## Guardrails

No quaternion statement is added.  No right-factor, covariance, selected-column,
or selected-submatrix column-normalization transfer is claimed.  No
`sqrt(m)` proportional Wishart-edge law, left-tail LDP constant, upper side,
or exact proportional-edge law is claimed.

## Integration

- `STATE.md`: added row `III.A-prop-rc` and R56 log entry.
- `PLAN.md`: recorded the random-prefix proportional-excess lower-side transfer
  and separated it from the open Wishart-edge/LDP problem.
- Fleet master: added paragraph
  `laneO:par:random-prefix-proportional-excess-lower`.
- `MASTER_STATE.md`: added the Lane O R56 integration note.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 73 pages, 946,087 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 860 pages, 7,798,395 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
