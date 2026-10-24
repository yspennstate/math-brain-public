# account03/B08 handoff — fractional ridge diffuse spectral-gap branch

Run: `20260922T154922Z-account03-B08-qform-diffuse-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

Canonical proof bundle: `yspennstate/math-open-problems@cf67f10cc3b6687e6c1bcd1a6f8075adb1057924`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T154922Z-account03-B08-qform-diffuse-r12/REPORT.md`. Arithmetic checker/output are beside it.

## New theorem

`QFORM-FRACTIONAL-RIDGE-DIFFUSE-SPECTRAL-GAP-v1`.

Let `A=R Lambda R^T+E`, `R^T R=I_r`, `r>=3`, every singular value of `Lambda` at least one, and `||E||op<=eta`. Put

`mu=max_i ||r_i||^2`, `alpha=(1-sqrt(r mu))/2`, `sigma=alpha-eta`,

`kappa=[sqrt(mu/alpha)+sqrt(6) eta/sigma]^2`.

If `r mu<1`, `sigma>0`, and for some `q in [1,2]`

`kappa<=q/2`, `6r/7>2q`,

then for every independent cap-one product input law, `X^TAX` has a continuous `C_0` density and

`||p||_infinity <= [3r/(3r-7q)] sqrt(3e/q)/sigma`.

The proof uses an original-coordinate Rademacher partition, lower-bounds the selected cross singular values, controls range leverage, and applies the completed one-scale ridge theorem at `gamma=sigma/sqrt(6)`. No post-rotation independence, law-uniform pointwise quadratic decay, or fiber supremum is used.

## Explicit new branch

For `r=3`, `||E||op<=1/64`, and `max_i||r_i||^2<=169/1875`, choose `q=5/4`. Exact arithmetic gives

`alpha>=6/25`, `sigma>=359/1600`, `kappa<5/8`, `theta>=18/7>5/2`,

hence

`||p||_infinity <= (57600/359) sqrt(12e/5) <410`,

with continuity. The same worst-case endpoint is not certified by the corresponding `q=1` perturbative criterion: its best limiting leverage square-root exceeds `1/sqrt(2)` by the exact positive amount induced by `13/30+25/359=1/2+16/5385`. Thus the fractional-exponent mechanism strictly enlarges the prior perturbative diffuse branch.

## Dependencies actually applied

1. `QFORM-RIDGE-DENSITY-v1`, full proof `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
2. Compatible completed account04 mathematics: account04/B16 `QFORM-CONDITIONAL-HEAVY-RAYLEIGH-HALF-v1`, source `yspennstate/math-open-problems@d6150b6de22e898de442e821e42c2ddc09604a0d`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T151616Z-account04-B16-QFORM-r1/REPORT.md`. It gives `||p||_infinity<15.69` for the complementary exact-rank-three branch with a unique leverage `>1/2` row and `|A_ii|>=1/4`; essential boundedness only, continuity not asserted there.

The designated assignment partner `account04/B08` had no completed current-QFORM handoff on the fresh shared path during this run, so no result was fabricated or attributed to it.

## Remaining implication

The unrestricted spectral complement can have arbitrarily large operator norm, so a small-remainder theorem is not the full conjecture. Next target: `QFORM-LARGE-DEFECT-RIDGE-CHARGE-v1` — charge a large remainder to the ridge effective dimension of the actual cross block; if the ridge certificate fails, extract a quantitatively low-effective-dimension remainder suitable for an existing bank/star/localized mechanism.

Full QFORM remains OPEN.
