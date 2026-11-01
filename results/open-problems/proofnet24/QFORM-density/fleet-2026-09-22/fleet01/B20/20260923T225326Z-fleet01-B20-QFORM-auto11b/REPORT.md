SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T22:53:26Z.
attacking: the unresolved finite-collar bridge after fleet02/B20's exact common-Gram third-mode escape.

# fleet01/B20 — finite-collar common-Gram robustification

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read: revision `2026-09-22.15` / programme revision `2026-09-22.5`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## Result

This run proves `QFORM-R37-FINITE-COLLAR-ABSOLUTE-BRIDGE-v1` and the sharper collective-tail localization in the sibling files `FINITE_COLLAR_BRIDGE.md` and `TAIL_AGGREGATION_STRENGTHENING.md`.

The completed designated partner is fleet02/B20 run `20260923T200300Z-fleet02-B20-QFORM-auto11`, canonical package `math-open-problems@edefefbd4d25c1c870330eb976e47a9356f7f4a0`. Its exact common-Gram theorem says that for a five-node exact rank-at-most-two symmetric common-Gram P-network with `s_3(A)>=sigma`,

`max{||PAQ||_op, max_i||Delta_i||_op, ||QAQ||_op} >= sigma/2`.

The later fleet02/B20 `e6fb033...` artifact is explicitly an EARLY calculation from an unfinished run and was not substituted for the completed result.

In the canonical r37 diffuse collar, write

`S_ab=B_a-D_ab A_b^{-1} C`,

with `s_2(A_b),s_2(B_b)>a`,

`a=0.002408434254376076...`,

and `D_ba=D_ab^T` in the common canonical physical frames. The source-valid mixed-fan identity and marginal-free physical E3 receiver give

`e_3(M_ab M_ab^T) >= det(A_b)^2 ||S_ab||_F^2 > a^4||S_ab||_F^2`,

`||p_Q||_infinity <= C_3 e_3(M_abM_ab^T)^(-1/6)`,

`C_3=10.5501688311648...`,

for the full ambient law on the paid branch.

Fix `c,M>0` and suppose

`s_2(C)>=c`, `max_b||A_b||<=M`, `||C||<=M`.

Set

`delta_*=c/[8(21M^2/a+2M)]`.

If some `||S_ab||_F>=delta_*`, the full law is paid continuously by

`||p_Q||_infinity <= C_3 a^(-2/3) delta_*^(-1/3)`.

Otherwise define

`F_b=A_b^{-T}B_bC^{-1}`.

The six Schur equations plus physical symmetry give the exact transpose-cocycle identity

`F_b-F_a^T
 =A_b^{-T}S_ba C^{-1}-(A_a^{-T}S_ab C^{-1})^T`,

hence

`||F_b-F_a^T||<2delta_*/(ac)`.

The odd three-cycle forces all three `F_b` within `7delta_*/(ac)` of one symmetric matrix `F`. Perturb `F` arbitrarily slightly to an invertible symmetric `F'`, and build the exact rank-two common-Gram model with kernel `(F')^{-1}` and node maps

`G_D1=I`, `G_Kb=F'A_b`, `G_D2=F'C`.

The off-diagonal error matrix `T` then obeys

`||T||
 <= delta_*/c (21M^2/a+2M)+3M^2||F'-F||
 <1/4`.

Replace only these P-off-diagonal blocks of `A` by the exact common-Gram blocks, obtaining `A'`. Then

`||A-A'||<1/4`,
`s_3(A')>3/4`.

This is the required equation-level consumption of fleet02/B20: applying its completed theorem to `A'` gives

`boxed: max{||PAQ||, max_i||Delta_i||, ||QAQ||}>3/8.`

The nonzero source tail is not discarded. Spending its full Frobenius budget collectively shows that the six strong source arms contribute operator norm `<sqrt(2)epsilon`, where

`epsilon=0.0023595307563857772`.

Thus, unless a same-node Gram self defect exceeds `3/8`, the forced third mode localizes to a NON-ARM physical interaction with

`boxed: ||P_i A Q_r|| >0.0876018373961`

or

`boxed: ||Q_r A Q_s|| >0.0758654166033`.

Here non-arm means it is not one of the already-controlled `D_1-K_b` or `K_b-D_2` source arms. The interaction can be same-node, `D_1-D_2`, `K_a-K_b`, or involve the exterior node according to its block type.

For the fixed universal subbranch `c=a`, `M=1`,

`delta_*=3.45191985840904e-8`,

and any Schur defect at this scale pays the full law with

`boxed: ||p_Q||_infinity <180337`,

with a continuous C0 density.

Therefore every still-unpaid state in this fixed moderate-scale nondegenerate collar is reduced to one of:

- `s_2(C)<a`;
- `||C||>1` or some `||A_b||>1`;
- a same-node common-Gram self defect `>3/8`;
- a non-arm physical plane/complement interaction `>0.08760`;
- a non-arm physical complement/complement interaction `>0.07586`.

The former undifferentiated finite relative-collar gap is therefore gone on the quantitative moderate-scale/nondegenerate branch. The next implication is

`QFORM-R37-C-SMALL-OR-HIGHSCALE-OR-NONARM-THIRDMODE-PAYMENT-v1`.

It must pay the displayed residual packets without rotating the product law or deleting the retained source tail. The full unrestricted theorem remains OPEN.

## Correction audit

No law-uniform pointwise quadratic oscillatory decay; no dimension-free worst-fibre cap; no arbitrary-joint coarea replacement; no conditional-cap-as-independence shortcut; no independence after spectral rotation; no deletion of a small nonzero random quadratic tail; no inference of one uniformly good physical minor from aggregate volume. Same-bank curvature, affine terms, exterior coordinates/couplings and all additional spectrum remain present in the full-law E3 payment.

## Keeper

Fresh native fleet01 inventory contained exactly the same twenty QFORM tasks B01-B20, each present once, enabled, hourly-valid and quiet; no B21/B22 and no repairable prompt/state defect were found, so **zero scheduler mutations** were made. The actual 22Z login directory contains B01 through B20; this is worker check-in evidence only, separate from native assignment and substantive-result state. The existing same-hour B20 canonical login and exclusive keeper lease belonged to the earlier same-hour B20 invocation and were preserved without overwrite or lease theft.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider reasoning/thinking usage: `UNKNOWN/null` (not zero).
