# account03/B08 handoff — diffuse block remainder + rank-three definite closure

**Run:** `20260922T122924Z-account03-B08-qform-diffuse-v2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
**Status:** `TARGET_SUPPORTING_THEOREMS`; full conjecture `OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

Canonical report: `yspennstate/math-open-problems@55d185b63ba44f172d9342b5d89e0875e850e17a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T122924Z-account03-B08-qform-diffuse-v2/REPORT.md`.

## New result 1: block-remainder diffuse theorem

If `A=R Lambda R^T+C`, `R^TR=I_r`, `r>2`, and the original coordinates split into blocks `G_k` across which `C` has no cross terms, put `M_k=R_{G_k}^TR_{G_k}` and `mu=max_k ||M_k||op`. If `r mu<1`, then a deterministic union-of-blocks cut exists with both selected-frame Gram matrices at least

`alpha I`, `alpha=(1-sqrt(r mu))/2`.

The actual full-matrix cross block is then `R_I Lambda R_J^T`, whose nonzero singular-value product is at least `|det Lambda| alpha^r`. Applying the completed rank-`r` cross-block Fourier theorem gives

`||p_Q||infinity <= [4r/((r-2)(1-sqrt(r mu)))] |det Lambda|^(-1/r)`

and a continuous density. This permits arbitrary dense off-diagonal remainder couplings inside each physical component, so it is a genuine extension of the previous coordinatewise-remainder theorem.

## New result 2: all rank-three definite leverage regimes

For every rank-exactly-three definite form `A=R Lambda R^T` with all three nonzero eigenvalue magnitudes at least one, every admissible product input law has

`||p_Q||infinity <= 3e`.

If all row leverages are at most `1/2`, this is the previous B08 Fourier–Brascamp–Lieb theorem. Otherwise choose a row `v` with `c=||v||^2>1/2`, put `a=v^T Lambda v`, and complete the square in that **original coordinate**. For positive definite `Lambda`, `a>=c`; the residual is a positive rank-two Schur complement. Its two-dimensional projection law has density at most `2`, yielding residual quadratic density

`M <= 2 pi sqrt(a/(c det Lambda))`.

Account04/B18's dependent square-smoothing lemma then gives

`||p_Q||infinity <= 2 sqrt(2 pi)(a c det Lambda)^(-1/4) < 4 sqrt(pi) < 3e`.

Reflection handles negative definite `Lambda`. The localized proof establishes essential boundedness; continuity is not promoted on that branch.

## Peer mathematics actually applied

- cross-block Fourier theorem: `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`;
- account04/B18 dependent square smoothing: `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

The designated partner `account04/B08` still had no completed current-QFORM handoff at the final source check, so no result was fabricated or attributed to it.

## First unpaid implication / next mechanism

The pure rank-three residue is now the localized indefinite near-isotropic/majority-pivot branch: `max_i ||v_i||^2>1/2` but a heavy physical row can have `|v_i^T Lambda v_i|` arbitrarily small by sign cancellation. The next mechanism is `QFORM-LOCALIZED-INDEFINITE-NEAR-NULL-v1`: exploit the necessarily strong orthogonal coupling `P^T Lambda v` and interpolate between square smoothing for a large pivot and a bilinear/cross-block payment for a near-null pivot. For general higher-rank targets, the arbitrary dense spectral remainder is still unpaid.

Correction inbox consumed through blob `1681679e291cfd73917b46a25dc5bc8584d40bec`, including the two-sheet X-ray-only refutation. The owner check-in request `QFORM-CHECKIN-20260922T120815Z` was acknowledged during this run.
