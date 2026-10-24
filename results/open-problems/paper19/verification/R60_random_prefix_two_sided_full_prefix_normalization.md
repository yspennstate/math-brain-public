# R60 verification -- random-prefix two-sided full-prefix normalization

## Scope

Added `two:random-prefix-gaussian-full-prefix-normalization` in
`parts/geometric.tex`, immediately after the R59 diagonal transfer.

For `F in {R,C}`, start with an infinite iid standard Gaussian array and
possibly dependent ordered prefix counts

```text
N_k^R/k -> gamma_R > 1,   N_k^C/k -> gamma_C > 1.
```

The corollary applies one-shot full-prefix row and/or column norm factors before
selecting `R,C`:

```text
rho_{i,k} = (sum_{j<=N_k^C} |g_{ij}|^2)^{1/2},
chi_{j,k} = (sum_{i<=N_k^R} |g_{ij}|^2)^{1/2}.
```

Using either family of factors, or both, preserves the R58 Gaussian two-sided
lower threshold

```text
(h(gamma_R) + h(gamma_C))/d_F.
```

A.s. prefix-count convergence gives the corresponding lower envelope.

## Audit

Five read-only audit agents were launched and closed.

- Godel `019f0ecc-bd8d-7d42-8f6a-40705b160b9a`: checked the theorem as an R59
  specialization with `kappa=0`, including probability and a.s. norm-extrema
  bounds.
- McClintock `019f0ecc-d5be-7351-a734-c8c2aa705070`: checked that norm tails
  must be proved by deterministic prefix brackets, not by conditioning on
  possibly entry-dependent realized counts.
- Averroes `019f0ecd-016e-7900-a59d-c0ffb6701b77`: checked placement, label
  `two:random-prefix-gaussian-full-prefix-normalization`, notation
  `rho_{i,k}, chi_{j,k}`, and row id `III.C-rc-norm`.
- Cicero `019f0ecd-1ca1-78d0-be56-02df89293d8d`: checked guardrails excluding
  per-minor normalization, iterative balancing, Sinkhorn-type conclusions, and
  non-Gaussian normalization without explicit norm-tail hypotheses.
- Euler `019f0ecd-30bb-79a3-bded-0e4cdeace0f7`: returned a separate
  Gram-transfer integration sketch; it was out of R60 scope and later recorded
  in R61.

## Proof Check

The row and column factors are positive diagonal weights on feasible prefixes,
so R59 applies once

```text
Delta_k^{norm}
 = alpha_R max_i |log rho_{i,k}| + alpha_C max_j |log chi_{j,k}| = o_P(k)
```

is proved, with the a.s. analogue under common a.s. count convergence.

For `C0 > max(gamma_R,gamma_C)`, the bracket

```text
k <= N_k^R,N_k^C <= C0 k
```

has probability tending to one, and eventually holds a.s. under a.s. count
convergence.  On this bracket, realized row norms are bounded above by
deterministic-prefix Gaussian norms in `d_F ceil(C0 k)` real dimensions and
below by their first `k` coordinates.  Markov's inequality gives a summable
upper tail `O(k^2 e^{-2 delta k})`, while the ball-volume lower tail is
`exp{-d_F delta k^2 + O(k log k)}`.  The same argument with rows and columns
interchanged controls `chi_{j,k}`.

Thus the diagonal log-extrema are `o_P(k)` and `o(k)` a.s.; R59 with `kappa=0`
gives the displayed lower side and lower envelope.

## Guardrails

This is a one-shot full-prefix normalization of the raw Gaussian array.  The
factors are computed before any selected minor is chosen and then frozen.

It does not include per-minor normalization, iterative balancing,
Sinkhorn/doubly-stochastic conclusions, non-Gaussian normalized entries without
explicit norm-tail hypotheses, non-diagonal covariance/right-factor transfer,
value-dependent thinning or reindexing, selected-submatrix renormalization,
upper side, exact two-sided law, quaternion extension, upper/exact
Gram/sample-covariance law, or Wishart-edge/LDP law.  R61 separately records
the deterministic selected-minor normalized Gram lower-side transfer.

## Integration

- `parts/geometric.tex`: added
  `two:random-prefix-gaussian-full-prefix-normalization`.
- `STATE.md`: added row `III.C-rc-norm` and the R60 round log.
- `PLAN.md`: recorded Gaussian full-prefix normalization for two-sided random
  prefixes.
- Fleet master: added paragraph
  `laneO:par:random-prefix-two-sided-full-prefix-normalization`.
- `MASTER_STATE.md`: added the Lane O R60 integration note.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 78 pages, 975,139 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 861 pages, 7,804,979 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
