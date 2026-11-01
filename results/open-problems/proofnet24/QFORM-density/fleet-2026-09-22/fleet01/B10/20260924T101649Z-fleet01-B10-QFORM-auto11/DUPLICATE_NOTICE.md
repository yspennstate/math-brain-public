# Duplicate-scope correction for fleet01/B10 run 20260924T101649Z

## Corrected classification

**DUPLICATE REDISCOVERY / EXISTING THEOREM RECONFIRMED / NO NEW CLAIM / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN.**

The immutable `REPORT.md` in this run re-derived a leverage-`1/2` Fourier–Brascamp–Lieb / sharp Hausdorff–Young / Fresnel theorem and initially described it as new to this run. A post-publication repository source-match found that this scope had already been proved in the QFORM corpus on 2026-09-22. The original report is intentionally preserved rather than rewritten; this notice supersedes its novelty classification.

## Exact pre-existing sources

1. **fleet02/B08 diffuse-rank3 theorem** — `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T113624Z-qform11/REPORT.md`.

   It already proves for exact rank three, with physical row leverages `c_i<=1/2`,

   `||hat p_{U^T X}||_1 <= (2*pi)^3 e^(3/2)`

   and

   `||p_{X^T U Lambda U^T X}||_infinity <=3e`,

   with a bounded continuous density. Its proof is the same sharp Hausdorff–Young + geometric Brascamp–Lieb cancellation followed by a Gaussian-regularized Fresnel integral.

2. **Broader separable-perturbation theorem** — repository snapshot `yspennstate/math-open-problems@500a7ee6eb5422b311fbda3a61f10a1cd619343a`, path
   `proofnet24/QFORM-density/interactive/20260922T193503Z-conversation-sync/initial_note/PROOF_NOTE.md`.

   Its Theorem 3 covers every `r>=3`, arbitrary coordinatewise measurable perturbations, and gives

   `||p_T||_infinity <= [r/(r-2)] B(U)^(2/r) |det Lambda|^(-1/r) <= e r/(r-2)|det Lambda|^(-1/r)`.

   For `r=3` this is exactly the `3e |det Lambda|^(-1/3)` compiler re-derived in this run, and it already includes arbitrary linear terms as a special case.

3. **Whitened/conditional physical-block theorem** — repository snapshot `yspennstate/math-open-problems@500a7ee6eb5422b311fbda3a61f10a1cd619343a`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T124007Z-r11/REPORT.md`.

   Its Theorem 3.1 already proves the conditional/whitened extension used in this run. In particular, for one conditioned physical row of leverage `c<1`, residual covariance `M=I-u_hu_h^T`, and whitened residual leverages at most `1/2`, it gives

   `||p_Q||_infinity <=3e[(1-c)|det Lambda|]^(-1/3)`.

   Thus the run's `3e[D(1-h)]^(-1/3)` one-hub estimate is also pre-existing.

4. This slot's own earlier report `yspennstate/math-open-problems@500a7ee6eb5422b311fbda3a61f10a1cd619343a`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260922T115451Z-b10-qform-r12/REPORT.md`, explicitly cites and consumes the fleet02/B08 diffuse theorem. This confirms that the present re-derivation is not a new fleet result.

## Partner result remains validly applied

The designated current partner source remains `yspennstate/math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T094654Z-fleet02-B10-QFORM-r13/REPORT.md`.

At the exact-coloop/null-hub endpoint it yields the actual inequality

`||p_Q||_infinity <= 6*2^(2/3) < 9.525`.

That application is correct but does not create a new bridge between the punctured collar and the endpoint.

## Corrected frontier and proposed successor

No new theorem from this run should be promoted into `CLAIMS.json`. The source match terminates this duplicate mechanism.

The current unresolved rank-three frontier remains the punctured near-coloop/shared-source gluing problem already identified before this run: one must bridge the small-`D(1-h)` collar to the finite exact-coloop endpoint without treating small coefficients as small random perturbations and without replacing original-product provenance by bounded compressed marginals.

For owner approval, the proposed successor is:

`QFORM-HEAVY-ROW-TO-EXACT-COLOOP-PRODUCT-PROVENANCE-GLUING-v1` — work directly at source level in the punctured heavy-row collar, using the exact endpoint receiver from fleet02/B10 and retaining the shared original-coordinate product structure. Do **not** repeat the leverage-`1/2` Wiener compiler or its whitened conditional version.

Full exact rank three remains **OPEN / NOT PROVED / NOT DISPROVED**. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open.
