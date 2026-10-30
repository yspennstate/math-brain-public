# fleet02/B11 early checkpoint — overlap-safe logarithmic-pair smoothing

Programme `QFORM-DENSITY-3EIG-20260922`. Full conjecture OPEN.

First unpaid implication attacked: the opposite-sign exact-rank-three branch in which an invertible indefinite ORIGINAL-coordinate pair is available, but the rank-one third Schur direction overlaps the same residual coordinates that translate the pair. The preceding disjoint-bank square argument did not cover that overlap.

## New calculation

Let the original independent cap-one variables split as `X=(U,Z)`, `U=(X_i,X_j)`, and write

`A = [[B,C],[C^T,D0]]`

with `B` invertible indefinite. For an exact-rank-three form, Schur completion gives

`Q=(U+B^{-1}CZ)^T B (U+B^{-1}CZ)+Z^T S Z`,
`S=D0-C^T B^{-1}C=sigma vv^T`, `||v||_2=1`.

The pair shift `B^{-1}CZ` may depend on the SAME scalar `W=v.Z`; no independence between the translating pair and `W` is assumed.

Use the source-pinned pair logarithmic envelope

`p_pair(t) <= 2sqrt(2)/r + |det B|^{-1/2} log_+(2r^2/(kappa |t-t0|))`,

`kappa=sigma_min(B)`, uniformly over all deterministic shifts of the two original pair coordinates. Conditional on `Z=z`, the critical value is exactly `sigma(v.z)^2`. Hence after averaging,

`p_Q(t) <= 2sqrt(2)/r + |det B|^{-1/2} E log_+(2r^2/(kappa |t-sigma W^2|))`.

A normalized product projection has `||p_W||_infinity<=sqrt(2)`. More generally, if `||p_W||_infinity<=L`, then for all `rho>0,t`,

`P(|sigma W^2-t|<rho) <= H sqrt(rho)`,
`H=2sqrt(2)L/|sigma|^{1/2}`,

because the preimage of an interval of radius `rho` under `w -> sigma w^2` has total length at most `2sqrt(2rho/|sigma|)`.

Layer cake gives, for every `a>0`,

`E log_+(a/|t-sigma W^2|) <= 2H sqrt(a)`.

Optimizing `r` therefore yields

`||p_Q||_infinity <= 4 sqrt(2H) (|det B| kappa)^(-1/4)`
`                  = 2^(13/4) L^(1/2) (|det B| kappa |sigma|)^(-1/4)`.

For product inputs, `L<=sqrt(2)`, so

`boxed: ||p_Q||_infinity <= 8sqrt(2) (|det B| kappa |sigma|)^(-1/4).`

For exact rank three with all three nonzero eigenvalue magnitudes at least `s`, the Schur-complement inverse identity gives `|sigma|>=s`, hence

`boxed: ||p_Q||_infinity <= 8sqrt(2) (|det B| kappa s)^(-1/4).`

This sharpens the earlier `8sqrt(5)` exact-rank-three physical-pair constant in the pure quadratic/no-outside-affine setting and, more importantly for this slot, explicitly permits the third square to overlap the coordinates that translate the pair.

Mandatory rank-two control remains intact: the pair itself need not have bounded density; for centered unit uniforms `2X_1X_2` has the genuine logarithmic singularity `log(1/(2|t|))`. The third direction removes it by the square small-ball exponent `1/2`, not by a false bounded pair-density claim.

## Required source applications

1. Pair envelope and moving-centre averaging framework: `math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
2. Pinned Claude ruled theorem: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `.../COUNTEREXAMPLE_SEARCH.md`, Theorem C. For signature `(+,+,-)`, it gives `p_Q(t)<=pi sqrt(2)` on the one-sheet side `t>=0`; reflection gives the corresponding majority-sign side for `(+,-,-)`.
3. Designated partner fleet03/B11 latest compatible report: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T061800Z-fleet03-B11-QFORM-r24/REPORT.md`. In the balanced pair-PSD complement at `s_3(A)>=1`, its Theorem 1 forces either a defect star of squared mass at least `1/4` or a disjoint defect cross-block with second exterior volume at least `1/32`.

## First remaining implication

`QFORM-BALANCED-STAR-CROSS-TWOSHEET-v1`: once every quantitative indefinite pair exit is unavailable, convert the partner's STAR/CROSS-2VOL alternative into a uniform two-sheet density bound while retaining the full original-coordinate product law and arbitrary within-bank curvature. The pure-star leverage-gated endpoint is paid by the partner mixed-Fresnel theorem; the missing part is the leverage-free/collective STAR and the aligned CROSS-2VOL branch without asserting a uniformly good local pair or a rank-three cross block.
