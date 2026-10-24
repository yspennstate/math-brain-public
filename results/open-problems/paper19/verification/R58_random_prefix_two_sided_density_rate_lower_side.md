# R58 verification -- random-prefix two-sided density-rate lower side

## Scope

Added `two:random-prefix-density-rate-lower` in `parts/geometric.tex`, after
the deterministic two-sided density-rate and smoothed lower-side results.

For `F in {R,C}`, an infinite independent-entry array with scalar density
bound

```text
K_k = exp((kappa+o(1))k)
```

and possibly dependent ordered prefix counts

```text
N_k^R/k -> gamma_R > 1,   N_k^C/k -> gamma_C > 1
```

has the lower-side threshold

```text
(h(gamma_R) + h(gamma_C) + kappa)/d_F.
```

The statistic is the minimum singular value over all `k x k` row/column minors
inside the realized ordered prefixes, with value `+infty` when a prefix is
smaller than `k`.  A.s. count convergence gives the corresponding liminf lower
envelope.

## Audit

Five read-only audit agents were launched and closed.

- Peirce `019f0eb8-aa6c-7623-a0be-1a864a8996ed`: checked that random ordered
  prefixes reduce to deterministic upper brackets and that the theorem should
  remain lower-side only.
- Epicurus `019f0eb8-e7cb-77b0-92df-c53e02332d7f`: checked the two-sided
  entropy constant `h(gamma_R)+h(gamma_C)` and the single density-rate
  contribution `kappa`.
- Heisenberg `019f0eb9-0abc-7140-84e6-662457961cc6`: checked the probability
  argument when the two prefix counts may depend on the entries and on each
  other.
- Anscombe `019f0eb9-3d8e-7070-945b-13ae79ff57b5`: checked the almost-sure
  lower envelope using countable deterministic brackets and the finite-budget
  result.
- Plato `019f0eb9-56ea-7203-91e2-097a0ffedb5d`: checked placement, labels,
  ledger row id, master paragraph, and guardrail wording.

## Proof Check

For deterministic brackets `gamma_R^+ > gamma_R` and
`gamma_C^+ > gamma_C`, set

```text
N_k^+ = ceil(gamma_R^+ k),   n_k^+ = ceil(gamma_C^+ k).
```

On `{N_k^R <= N_k^+, N_k^C <= n_k^+}`, the realized-prefix family is a
subfamily of the deterministic-prefix family, so

```text
M_k^{rpref,two} >= M_k^{two}(N_k^+, n_k^+).
```

The complementary count event has probability tending to zero.  The
deterministic two-sided density-rate lower theorem gives the lower side for
each fixed pair of brackets.  Sending `gamma_R^+ down to gamma_R` and
`gamma_C^+ down to gamma_C` gives the stated probability limit by continuity
of `h`.

For the a.s. statement, use countable decreasing bracket sequences and the
summable-error finite-budget lower side `two:finite-entropy`; after the prefix
counts are eventually inside every fixed bracket, intersect the full-measure
events and let the brackets decrease.

## Guardrails

This is an ordered-prefix lower-side transfer only.  It does not assert an
upper side, exact two-sided law, pair-correlation theorem, quaternion
extension, value-dependent thinning or reindexing theorem, selected-column
covariance transfer, non-diagonal right-factor transfer, or
upper/exact Gram/sample-covariance law.  R59 separately records the pathwise
diagonal row/column weighting transfer.  R61 separately records the
deterministic selected-minor normalized Gram lower-side transfer.

## Integration

- `STATE.md`: added row `III.C-rc` and the R58 round log.
- `PLAN.md`: recorded random-prefix two-sided lower sides among completed
  Phase V.E items.
- Fleet master: added paragraph
  `laneO:par:random-prefix-two-sided-density-rate`.
- `MASTER_STATE.md`: added the Lane O R58 integration note.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 75 pages, 960,682 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 860 pages, 7,801,521 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
