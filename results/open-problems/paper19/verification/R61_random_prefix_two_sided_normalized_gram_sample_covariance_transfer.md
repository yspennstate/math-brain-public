# R61 verification -- random-prefix two-sided normalized Gram/sample-covariance transfer

## Scope

Added `two:random-prefix-normalized-gram-transfer` in `parts/geometric.tex`,
immediately after the R60 full-prefix normalization corollary.

In the R59 diagonal-transfer setting, define the selected-minor normalized
column-Gram statistic

```text
Lambda_{k,B}^{rpref,twodiag}
 = min lambda_min(k^{-1} (B_{R,C}^{(k)})^* B_{R,C}^{(k)})
```

over `R subset [N_k^R]`, `C subset [N_k^C]`, `|R|=|C|=k`, with value
`+infty` if either prefix is infeasible.  The lower threshold is

```text
2(h(gamma_R) + h(gamma_C) + kappa)/d_F.
```

A.s. prefix-count convergence plus `Delta_k^{twodiag}=o(k)` a.s. gives the
corresponding lower envelope.  The R60 Gaussian full-prefix-normalized matrices
are included with `kappa=0`.

## Audit

Five read-only audit agents were launched and closed.

- Noether `019f0ed4-b49a-7af0-b2df-f1ddcd0c73d3`: checked the doubled constant
  and the harmless `log k/k` normalization loss.
- Parfit `019f0ed4-d08d-7c30-8334-919d4843d96c`: checked placement after R60,
  label `two:random-prefix-normalized-gram-transfer`, row id
  `III.C-rc-gram`, verification filename, and master label
  `laneO:par:random-prefix-two-sided-normalized-gram-transfer`.
- Euclid `019f0ed4-e634-72c2-8a8e-aad78509eb99`: checked guardrails limiting
  the statement to selected `k x k` column-Gram matrices with selected-minor
  normalization `k^{-1}`.
- Laplace `019f0ed4-ff3e-7f91-9bd5-0fdb27cdaef7`: checked that the R58--R60
  caveats were softened only for this deterministic selected-minor Gram
  transfer.
- James `019f0ed5-2422-7800-a327-15d13c8a0c6d`: checked the compact fleet
  master paragraph and the density-rate notation alignment in the R58--R61
  master-state area.

## Proof Check

For every feasible selected minor,

```text
lambda_min(k^{-1} B_{R,C}^* B_{R,C}) = k^{-1} s_min(B_{R,C})^2.
```

Taking minima over exactly the same feasible family gives

```text
Lambda_{k,B}^{rpref,twodiag}
 = k^{-1} (M_{k,B}^{rpref,twodiag})^2.
```

If `c=(h(gamma_R)+h(gamma_C)+kappa)/d_F` and
`Lambda <= exp(-(2c+eps)k)`, then

```text
M <= k^{1/2} exp(-(c+eps/2)k) <= exp(-(c+eps/4)k)
```

for all large `k`.  The probability statement follows from R59.  The a.s.
lower envelope follows from

```text
k^{-1} log Lambda = 2 k^{-1} log M - (log k)/k.
```

## Guardrails

This is only deterministic squaring for already selected square minors with
the selected-minor normalization `k^{-1}`.  It is not an upper or exact
two-sided Gram/sample-covariance law, a Wishart-edge or LDP theorem, a
pair-correlation theorem, a non-diagonal covariance or right-factor transfer, a
row-Gram result for rectangular matrices, a per-minor normalization theorem, a
value-dependent selection theorem, or a quaternion statement.

## Integration

- `parts/geometric.tex`: added
  `two:random-prefix-normalized-gram-transfer` after R60.
- `STATE.md`: added row `III.C-rc-gram`, softened the R58--R60 guardrails, and
  added the R61 round log.
- `PLAN.md`: recorded the selected-minor normalized Gram transfer in the
  III.C, V.C, and V.E summaries.
- Fleet master: added paragraph
  `laneO:par:random-prefix-two-sided-normalized-gram-transfer`.
- `MASTER_STATE.md`: softened the R58--R60 caveats and added the Lane O R61
  integration note.
- R58--R60 verification files: softened the older hard Gram exclusions to
  point at this R61 lower-side transfer.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 80 pages, 1,000,502 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 861 pages, 7,806,351 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
