# account02/B14 proof-first addendum handoff — arbitrary-offset graphical localization

Run `20260922T160911Z-b14-qform-localization-r15`; full QFORM remains OPEN.

Canonical addendum: `yspennstate/math-open-problems@b157d48994785c3224d2fdf9e694396548f9b347`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T160911Z-b14-qform-localization-r15/PROOF_FIRST_ADDENDUM.md`.

Later owner continuation applied: `QFORM-PROOF-FIRST-20260922T161801Z` (`yspennstate/math-research-brain@10695e7784b41c0a2bf1a5e61a93cbc8cfc66564`). Completed peers consumed: assigned partner account03/B14 global convex-mixture localization `yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`; account01/B14 arbitrary-offset triangle `@2ad67886f215eff6f3daed247871a882a6f0314b`; account01/B06 curved coarea `@1bc95193312b70572b2765529ac3b6d98e3fe754`.

**Theorem.** For any fixed finite simple graph `G` with exponents `theta_e>=0`, the moment

`E prod_{e={i,j}} |X_i-X_j-d_e|^-theta_e`

is uniformly finite over every choice of real edge offsets `d_e` and all independent cap-one input densities iff every vertex cluster `S`, `|S|>=2`, satisfies

`sum_{e subset S} theta_e < |S|-1`.

Sufficiency uses the graphic-matroid forest polytope. With strict cluster slack choose `epsilon>0` so `x_e=theta_e/(1-epsilon)` lies in the forest polytope and decompose `x` as a convex mixture of forest indicators. Dominate each edge kernel by `max(1,|gap-d_e|^{-(1-epsilon)})^{x_e}`, apply Hölder across the forest mixture, and eliminate forest leaves. Each leaf costs at most `1+2/epsilon`, uniformly in the parent and arbitrary edge offset. Thus `C_off <= (1+2/epsilon)^{m-1}`. Necessity follows at zero offsets from iid `Uniform[0,1]` and the collision-cluster radial integral; equality gives logarithmic divergence.

This removes cycle consistency from the localization debt. Combined with account03/B14, a bounded-size subcritical graph certificate may be chosen separately for each compact extreme-product mixture component and may have arbitrary outside-dependent edge offsets; convex mixing and TV passage preserve one universal constant. It does not assert those certificates exist for every target matrix.

**First unpaid implication after the proof-first continuation:** retain the determinant/Pluecker weights in account01/B06's translation-uniform curved-coarea reciprocal kernel before scalar collapse and reorganize the kernel into uniformly bounded-size subcritical pair-gap graphs, or prove an unavoidable critical cluster. A critical cluster rules out raw absolute graph integration even for iid uniforms and forces cancellation/operator aggregation.

Correction snapshot before the addendum: `yspennstate/math-research-brain@29e91087236ca7ebeaa5d6b64e42adc450cba975`; no listed correction conflicts with this theorem.
