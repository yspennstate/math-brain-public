# account02/B04 — controlling QFORM handoff

Status: `ESSENTIAL_STEP_APPLIED`; full `QFORM-FULL` remains OPEN; `WITHOUT_VERIFIED_BRAIN`.

This handoff supersedes the narrower frontier discussion in the earlier same-run handoff while preserving it immutably.

## Canonical mathematics

Run folder: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T114427Z-qform-product-rearrange-r1/` in `yspennstate/math-open-problems`.

1. Primary report: commit `4b3710c4cb26b29e3f80ac4069d731baa6fc4af0`, blob `7cc2a250ef49ef0edd745be69caa8f5da39a08b4`. Proves `QFORM-PRIVATE-BLOCK-FOURIER-v1` by a one-square `L^(3/2)` rearrangement, Hausdorff--Young and three-factor Holder.
2. `1+2` mixed addendum: commit `637dc3db113b9824f166807066309dad3f6f4743`, blob `6eab66496fea5ef2ceaf26442ad3398985be124f`. Combines one localized square with a two-dimensional delocalized Brascamp--Lieb/Fresnel resource.
3. Large-row Schur addendum: commit `824e42064f2c3220d94b10553d4fe59565ae909e`, blob `f2d3b26d6cb6d4b6834eb1f9565183b1fd55a110`. Removes the exact zero-pattern requirement for a non-isotropic large physical row. If `A=U Lambda U^T`, row `u=u_i`, `a=u^T Lambda u !=0`, `r=||u||`, and every other row projected to `u^perp` has norm at most `1/2`, then

`||p_Q||_inf <= 4 B_RV / {pi 3^(1/4) [|a| r^2 |det Lambda|]^(1/4)}`.

The proof keeps the correlated completed-square shift, bounds the rank-two Schur residual in `L^3`, and removes the shift through a one-sided fractional integral. It supplies an explicit high-leverage, spectrally contaminated `(2,-1,-1)` example not covered by the fully delocalized theorem.
4. Isotropic-model addendum: commit `f43f0ba0be58a2f5163c4a81571bdf46c51a9496`, blob `d2b81a237ebccd3fdf6af3a30004906147509848`. For independent densities <=1,

`Q=2cXY+lambda Z^2`

obeys

`||p_Q||_inf <= |c|^(-1)+2*24^(1/3)|c|^(-2/3)|lambda|^(-1/3)`.

Hence every `|c|,|lambda|>=1` canonical isotropic `(c,-c,lambda)` form has a universal bounded density. The proof is a logarithmic product-density envelope plus the one-square `L^(3/2)` bound and Young convolution.
5. Named-partner integration: commit `4672f4054130c1d3544669abfd6c6f045a812aab`, blob `79939029a831e2550705a9782babefb14811b45b`. Applies account03/B04's completed one-square averaged-Fourier theorem to sharpen private-block constants. For a private linear form coefficient vector `a`, define

`kappa(a)=min(sqrt(2)/||a||_2,1/||a||_inf)`.

Then the three-block theorem sharpens to

`||p_Q||_inf <= 8 (kappa_1 kappa_2 kappa_3)^(2/3)|lambda_1lambda_2lambda_3|^(-1/3)`,

and a same-sign pair gives `pi kappa_i kappa_j/sqrt(|lambda_i lambda_j|)`. The six-coordinate rotated example therefore improves from the earlier valid `4pi` to the controlling `2pi` bound.

## Peer/source results actually applied

- **Named partner account03/B04**, handoff commit `9c946331d5e97e35584005a98d0e496fae7014d0`; canonical report `math-open-problems@f824ded997ee16c741468bb49860e1ccaf18d8bd`, blob `2438594f82b064359483972f59f4d061a6814ce0`. Applied to sharpen the private/mixed scalar Fourier budgets.
- account01/B05, brain handoff blob `028e99f4705e07fac0fb369efb7ed63ec8927c35` at control commit `5f703e4c639acefc3f33aa4d149fe5ff85814622`. Applied as the flat-Walsh stress test ruling out best-chart and naive reciprocal-Jacobian averaging.
- account02/B02, report commit `2d79dea715c2baa9e8ef6c0ac174eee1712d2888`, blob `d13acb61e2846ea2e1761acca18d5e4e0f124a34`. Its delocalized rank-three integrated-Fourier theorem was applied as the two-dimensional residual Fresnel resource and to identify the large-row frontier.
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949, used only for the proved product-marginal density bound.

## Later correction applied

Fresh correction inbox at control commit `e1b92e8c373113b1e2aa6420bf8652be2a3ec348` contains `QFORM-CROSSMINOR-ALONE-FALSE` (event blob `22f0079bd864c878c2133f2c50f2701a0d928783`). It refutes the claim that an invertible `2x2` cross block alone suffices. Nothing in the B04 theorems uses that false claim. The B04 isotropic theorem explicitly spends a third square direction; the B09 counterexample has only two nonzero eigenvalues. B09's safe multi-pivot theorem is an additional allowed branch when an exact physical linear-pivot packet exists.

## Updated first missing implication

For rank exactly three, the remaining hard core is now narrower:

- a large physical row that is `Lambda`-isotropic or near-isotropic **with overlapping residual physical coordinates**, so the bilinear partner and third direction are dependent projections; or
- multiple rows remain large after projection to the chosen pivot's orthogonal complement.

The next mechanism should prove a joint two-dimensional product-projection analogue of the logarithmic product envelope, or an aggregation that exposes B09's exact multi-pivot packet, while preserving the original product law. Multiplying rotated marginals, taking a spectral-fiber supremum, or selecting one reciprocal minor remains invalid.

For the full owner conjecture there is still a separate dependence problem when more than three eigendirections are present; rank-three closure alone will not justify convolving away the rest.
