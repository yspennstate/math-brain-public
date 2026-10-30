# Fresh dependency addendum — B09 r15

After the primary report was committed, fresh programme main exposed two later same-role results. Neither contradicts `QFORM-ONE-SIDED-SEPARABLE-CROSS-DIFFUSE-v1`; both sharpen the routing boundary.

## 1. Latest assigned partner fleet02/B09

Source: `yspennstate/math-open-problems@caa2cef304844e9d6f841acaf2e003f0bc1c24b5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T183809Z-fleet02-B09-QFORM-r7/REPORT.md`, theorem `QFORM-RANK3-BILINEAR-SCHUR-BANK-v1`.

For an exact-rank-three zero-diagonal form and any nonzero physical edge `(i,j)`, put

`R_ij = |A_ij|^2 sum_{k!=i,j} |A_ik A_jk|`.

The partner theorem proves

`||p_Q||_infinity <= 2^(5/4) sqrt(15) R_ij^(-1/4).`                  (1.1)

This is applied here as an explicit routing inequality: whenever `R_ij>=1/16`,

`||p_Q||_infinity <= 2^(9/4) sqrt(15) <18.424.`                      (1.2)

Thus the exact-rank-three zero-diagonal branch with a quantitatively nontrivial aggregate pair bank is removed from B09's remaining debt. On the partner's clone-bank stress family `R_12=1`, (1.1) gives the sharper `<9.212` bound. This application is complementary to the primary report's use of the partner's previous exact-zero-bank theorem: the new r7 theorem pays a rank-one Schur bank that the previous rank-two flat-bank theorem does not.

## 2. Fresh fleet03/B09 Schur half-Riesz result

Source: `yspennstate/math-open-problems@2589a6230149bd8c3b4b2a0aad6f404bc7ab034a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T184648Z-fleet03-B09-QFORM-r15/REPORT.md`.

That run proves two translation-uniform half-Riesz exits for a residual quadratic form `F` with `s_2(S)>=1`:

- if a second physical diagonal satisfies `|S_kk|>=1/2`, then `sup_w E|F-w|^(-1/2)<25.095`;
- if some original-coordinate cross cut has two singular values at least `beta`, then `sup_w E|F-w|^(-1/2)<=8 beta^(-1/2)`.

Its remaining Schur geometry is therefore a one-strong-cross regime: all physical diagonals below `1/2`, one cross singular value bounded below, but the second can be arbitrarily small.

The primary B09 theorem is compatible with this split. It gives a full continuous-density endpoint when a rank-two cross block has a diffuse singular frame and a coordinate-separable self side, but its constant contains `(s_1 s_2)^(-1/2)` at rank two and hence does not uniformly pay an arbitrarily small `s_2`. The combined first unpaid geometry is consequently sharper:

`QFORM-ONE-STRONG-CROSS-NONSEPARABLE-HEAVY-v1`: pay the branch where there is one strong original-coordinate cross singular direction, every candidate second cross direction is quantitatively weak, no second physical pivot is large enough, and the self-curvature on the potentially diffuse coefficient bank is genuinely nonseparable/heavy so that the new separable-phase theorem cannot be invoked at a uniform product scale.

This is a routing refinement only; the full QFORM conjecture remains open.
