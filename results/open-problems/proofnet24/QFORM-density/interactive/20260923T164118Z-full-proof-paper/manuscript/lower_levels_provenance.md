# Lower-level chapter: source and verification

The chapter `lower_levels.tex` adapts the full proofs from
`source_snapshot/interactive/20260922T231000Z-semidefinite-and-hub-reduction/lower_levels/REPORT.md`.

## Included results

- One large eigenvalue and no `c`-pivot, `c <= 2e-6`: concentration at most `25 sqrt(u)`, with the heavy/light random-partition proof.
- Coordinate discriminant: exact minors matrix, conditional sublevel formula, quarter-power and logarithmic transition bounds, uniform half-power potential.
- Two tests for sufficient discriminant norm.
- Exact second-volume marginal formulas and their row and residual consequences.
- Both random-partition expansions, all sign second moments, comparable and dominant eigenvalue cases, and the final two-eigenvalue half-Riesz estimate `10^6` at `c_*=1e-15`.

## Corrections and conservative constants

1. The source's proof of Theorem B first proves a global bound `5+12 K_Delta` and then unnecessarily adds a second estimate on a subset. The chapter retains the already sufficient global bound, giving the stronger displayed constant `5+40(16.92/nu)^(1/3)` instead of `5+69(16.92/nu)^(1/3)`.
2. The Fejer coefficient `3/kappa0` is `3.2630139745...`, so the chapter uses `3.264`, not the slightly downward-rounded `3.263`.
3. At `q=6/5`, the exact characteristic-function coefficient is `6.5029997689...`; the chapter uses `6.51`. It uses the safe concentration coefficient `85`, and the half-power bound remains below `129`.
4. The eigenvector perturbation quotient at `sigma0=4996` is `2.00100112... / sigma0`; the source's `2.001/sigma0` is marginally too small. The chapter uses `2.01/sigma0`, preserving comfortable margins in all residual estimates. The residual entry cap used is `0.003`, row norm cap `1.001`, and top-vector coordinate-square cap `3e-7`.
5. Direct integration with the source Fejer normalization in the balanced case gives `7912.0162...`, not `7500`. The chapter uses `8000`.
6. Under scaling `r=|mu_2|>=1`, the correct comparison is `H(Q)<=r^(-1/2) H(Q/r)`. The source's verbal monotonicity claim is replaced by this inequality and its event inclusion.
7. The source's first discriminant branch using its own constant gives about `796940`, slightly greater than its displayed `7.9e5`. The improved discriminant proof gives about `461996`, and the chapter uses `4.7e5`. The final `10^6` theorem is unchanged.
8. The logarithmic transition estimate is proved by separate cases `V0<=A0` and `V0>A0`, so no integration interval is inadvertently reversed.

All these changes repair constants or simplify a proof. No unresolved step in the stated lower-level theorems was identified during this verification.

## Compilation check

Compiled the chapter twice with the current master preamble using `pdflatex -interaction=nonstopmode -halt-on-error`. The standalone chapter is nine pages. There are no overfull or underfull boxes. Its internal references resolve; the only standalone unresolved references are the five intended cross-chapter labels:

`sec:structure`, `four:volume`, `four:quarter`, `geom:square`, `lem:schur-count`.

The final manuscript must resolve these through the included companion chapters. No bibliography keys were added by this chapter.
