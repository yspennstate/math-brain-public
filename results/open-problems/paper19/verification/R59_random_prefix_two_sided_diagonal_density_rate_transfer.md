# R59 verification -- random-prefix two-sided diagonal density-rate transfer

## Scope

Added `two:random-prefix-diagonal-conditioning-transfer` in
`parts/geometric.tex`, immediately after the R58 random-prefix two-sided
density-rate lower side.

For `F in {R,C}`, start with the R58 independent-entry random-prefix base array.
Positive real row and column weights over the realized ordered prefixes may be
random and dependent on the entries and prefix counts.  If

```text
Delta_k^{twodiag}
 = max_{i<=N_k^R}|log d_{i,k}| + max_{j<=N_k^C}|log e_{j,k}| = o_P(k),
```

then the lower threshold for the minimum over weighted `k x k` two-sided minors
is unchanged:

```text
(h(gamma_R) + h(gamma_C) + kappa)/d_F.
```

A.s. prefix-count convergence plus `Delta_k^{twodiag}=o(k)` a.s. gives the
same lower envelope.

## Audit

Five read-only audit agents were launched and closed.

- Copernicus `019f0ec4-49e4-7811-af85-682b1486960f`: checked the pathwise
  diagonal sandwich and confirmed that the density contribution remains one
  `kappa`, not two.
- Sagan `019f0ec4-712f-7001-a6db-8b0a1ff3e001`: checked placement after R58,
  label style, and the `epsilon k/2` split when `Delta` is the sum of row and
  column log-extrema.
- Beauvoir `019f0ec4-855b-7d52-82e2-014724ff241b`: stress-tested guardrails:
  positive finite weights only, no non-diagonal covariance/right-factor
  transfer, no selected-submatrix normalization, and no upper/exact law.
- Meitner `019f0ec4-ab98-7f61-b5f9-cbf17b97b475`: checked the a.s. lower
  envelope and confirmed that no extra summability or independence is needed
  once the R58 a.s. base and `Delta=o(k)` a.s. are assumed.
- Darwin `019f0ec4-c69c-7242-b59d-8a829c810d17`: checked ledger placement
  (`III.C-rc-diag`), R58 guardrail softening, verification filename, PLAN
  wording, and the compact master paragraph.

## Proof Check

For every feasible selected pair `(R,C)`,

```text
s_min(diag(d_i:i in R) A_{R,C} diag(e_j:j in C))
 >= exp(-Delta_k^{twodiag}) s_min(A_{R,C}).
```

Taking minima gives

```text
M_B >= exp(-Delta_k^{twodiag}) M_A.
```

With

```text
c = (h(gamma_R)+h(gamma_C)+kappa)/d_F,
```

the event split is

```text
P{M_B <= exp(-(c+eps)k)}
 <= P{Delta_k^{twodiag}>eps k/2}
  + P{M_A <= exp(-(c+eps/2)k)} -> 0.
```

The first term is the conditioning hypothesis; the second is R58.  The a.s.
statement follows from the same pathwise inequality and R58's a.s. lower
envelope.

## Guardrails

This is only a pathwise lower-side transfer from the unweighted
independent-entry base array.  It does not assert that the weighted matrix
satisfies the density hypothesis.

Weights are finite positive real scalars, one global row weight per realized
prefix row and one global column weight per realized prefix column.  Zero
weights are excluded.

No non-diagonal column covariance/right-factor transfer, selected-column
covariance theorem, selected-submatrix renormalization theorem,
condition-number-only scale control, value-dependent thinning or reindexing,
upper side, exact two-sided law, pair-correlation theorem, quaternion extension,
upper/exact Gram/sample-covariance law, or Wishart-edge/LDP law is claimed.
R61 separately records the deterministic selected-minor normalized Gram
lower-side transfer.

## Integration

- `parts/geometric.tex`: added
  `two:random-prefix-diagonal-conditioning-transfer` after R58.
- `STATE.md`: added row `III.C-rc-diag`, softened the R58 guardrail, and added
  the R59 round log.
- `PLAN.md`: recorded random-prefix two-sided diagonal row/column transfers.
- Fleet master: added paragraph
  `laneO:par:random-prefix-two-sided-diagonal-transfer`.
- `MASTER_STATE.md`: added the Lane O R59 integration note and softened the R58
  caveat.

## Build Verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error
  extremal_hard_edge.tex` run twice.  Final output:
  `extremal_hard_edge.pdf`, 76 pages, 965,364 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice.  Final output: `master.pdf`, 861 pages, 7,803,713 bytes.
- Copied `math-open-problems-fleet/master/master.pdf` to
  `~/Downloads/master.pdf`.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined references, undefined citations, multiply-defined labels, or rerun
  requests; only the final `Output written` lines matched.
