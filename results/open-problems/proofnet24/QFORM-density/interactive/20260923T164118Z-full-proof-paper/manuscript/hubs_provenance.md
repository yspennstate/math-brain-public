# Hub chapter: provenance, scope and checks

## Files

- `hubs.tex` is the professional manuscript chapter. It includes complete proofs of all results stated there, with external theorems cited at their uses.
- `../research_work/hub_new.md` records the new symmetric-window recovery estimate and its implications.
- `../research_work/adapted_attack.md` gives complete independent derivations of the conditional Gaussian theorem, fixed-dimensional frame partition, Gaussian scale-mixture theorem, and conditional-information obstruction.

## Source record

The existing results were consolidated from the snapshot `20c8f358318f0753d3fbe1f59c04b8391c1bcb92` of `yspennstate/math-open-problems`:

- `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`;
- sibling `counterexample_search/REPORT.md`, `degenerate_hub/REPORT.md`;
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

These are source provenance, not independent publications and not earlier public preprints. They are not cited in the manuscript as such.

Additional existing proofs use the sibling multiscale_fourier/REPORT.md and hub_with_diagonal/REPORT.md source files.

A later pinned supplement of single_hub_core/REPORT.md is saved under ../source_snapshot/additional_claude/. Its exact source commit is 37489065b13869b622e5eedab7ab253de46eb154, blob SHA d75613751b4bedd98959abae4eb065b82518f49b, fetched at 2026-09-23 17:08:02 UTC. ADDITIONAL_SOURCE.json records the permanent source URL and confirms that the initial snapshot was not altered.

## Consolidated known results

The chapter proves the modulated frame lemma; frozen-slice Fourier and interval estimates; profile criterion; interval-supported hub theorem; pure hub/transverse-square bound; nonzero-leakage Fourier bound; double-logarithmic small-ball estimate; localized leakage, independent square, partner-only block and bounded-variation bounds; maximal-projection criterion and bounded/window light laws; multihub Plancherel; two-hub square and interval-profile estimates; one-/two-hub projected-crossing decoupling; logarithmic hub-diagonal interpolation; and spread linear hubs.

The general arbitrary-rank projected-crossing extension is proved in `structure.tex` and referenced by `thm:grouped-crossing`; it is not duplicated here. Convex-superlevel, full interval-law rank-three and ruled-surface results belong to `geometry.tex`. Some weaker or specialized variants of the source record are subsumed by these statements or retained in the complete source archive rather than repeated.

## New proved refinements and subclass results

1. **Symmetric-window recovery**, `lem:hub-window-recovery`, with the exact constant `2 sqrt(2pi)/(3pi)`.
2. **Improved leakage interpolation**, `cor:hub-loglog-density`, replacing the previous multiple of the window density by coefficient one and improving the error to `16pi/(3sqrt(|lambda|))` at h=eps. The endpoint remains logarithmically nonuniform.
3. **Exact large-lambda pure-hub branch**, `(192/|lambda|)^(1/3)`, obtained by evaluating the existing bathtub optimizer rather than rounding that branch to `2sqrt2`.
4. **Conditional Gaussian covariance theorem**, `lem:hub-gaussian`, with a covariance-floor bound of three, allowing an adapted hub depending on P.
5. **Fixed-dimensional frame partition**, `lem:hub-frame-partition`: Parseval frames with each vector norm squared at most one half split into two uniformly nondegenerate parts, with a nonexplicit dimension-dependent constant. Uses the published matroid base-packing criterion and a complete compactness/diffuse-tail proof.
6. **Gaussian component-mixture adapted-hub theorem**, `thm:hub-gaussian-mixtures`. This handles the bare entangled core uniformly in leakage size (and an arbitrary hub diagonal), for independent Gaussian mixtures with `E T_i^(-1/2)<=sqrt(2pi)`. In the centered scale-mixture class this condition is precisely the density cap. No positive lower bound on component variances is required.
7. **Explicit translated Laplace case**, constant below 19, without spread assumptions.
8. **Conditional-information obstruction**, `prop:hub-cap-obstruction`: all coordinate marginals and the joint density of an abstract (L,V,P) vector can have cap one while an adapted hub produces a logarithmically unbounded density. The example is explicitly not claimed to come from projections of a cap-one product law.

The Gaussian-mixture theorem does not cover arbitrary separated narrow-component mixtures whose marginal cap results from separation in location. It also does not settle all light diagonals or arbitrary q0L²/LV terms. The general QFORM and unrestricted adapted-hub conjectures remain open.

9. **Scalar SQ kernel improvement**, lem:hub-sq-scalar: the exact elementary sublevel estimate gives 2^(7/4) in place of 9.05. Consequently thm:hub-sq-composition gives 2^(13/4) in place of 25.6. The new scalar bound was independently re-derived by the project lead.
10. **Explicit scale joining for the zero-diagonal degenerate hub**, thm:hub-degenerate-uniform: symmetric-window recovery and a two-sided dyadic sum replace the unspecified smoothing constant by a displayed finite one.

The final chapter also includes full proofs of shell-collision L2 bounds, the sqrt(log K) improvement for bounded light supports, the conditional weighted-collision criterion, the elementary L6 parabola estimate, degenerate-hub Strichartz and its normalized bound below 18, joint SQ composition, randomness at the degenerate center, and an independent-square consequence. The support proof supplies an explicit concave majorant. The logarithmic SQ estimate uses slightly coarser constants than its source and a complete direct interval-kernel proof.

## Verification

- The principal existing analytic arguments were re-derived from their stated hypotheses; slice parameter exceptional sets are handled by an explicit freezing procedure.
- The exact nonzero-leakage constant is `4sqrt(2)pi^(3/2)`, so the density constant is `3*2^(5/3)`.
- The exact two-hub-square density constant is `5*2^(6/5)`; no extra pi factor occurs.
- The bounded-support tilt constant uses its exact integral `2^(3/2)(6+sqrt(pi/2))`; the displayed coarse bound is rounded upward to 52.
- For the interval-slice-profile theorem, an initial restriction to bounded partner-density levels makes collision measures finite and is removed by monotone convergence.
- The Gaussian-mixture theorem and frame partition received two additional independent proof checks before inclusion. The hub is explicitly generated by fresh auxiliary randomness after X, so its kernel survives conditioning on latent mixture variables.
- A standalone pdflatex/bibtex build of the complete chapter, including all final requested additions, passed. It has 26 text pages plus bibliography and no overfull boxes. The final combined manuscript resolves the single external reference to thm:grouped-crossing and undergoes visual review separately.
