# account02/B04 — QFORM product Fourier rearrangement handoff

Status: `ESSENTIAL_STEP_APPLIED`; `QFORM-FULL` remains OPEN; execution `WITHOUT_VERIFIED_BRAIN`.

Primary immutable mathematics: `yspennstate/math-open-problems@4b3710c4cb26b29e3f80ac4069d731baa6fc4af0`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T114427Z-qform-product-rearrange-r1/REPORT.md`, blob `7cc2a250ef49ef0edd745be69caa8f5da39a08b4`.

New theorem `QFORM-PRIVATE-BLOCK-FOURIER-v1`: if, after conditioning a shared physical-coordinate block `T`, the form is

`Q=R(X_T)+sum_{j=1}^3 lambda_j(a_j·X_{S_j}+b_j(X_T))^2`

on disjoint private blocks `S_1,S_2,S_3`, with `alpha_j=||a_j||_2>0`, then

`||phi_Q||_1 <= 32 pi / ((alpha_1 alpha_2 alpha_3)^(2/3)|lambda_1 lambda_2 lambda_3|^(1/3))`

and therefore the law has a continuous density with

`||p_Q||_inf <= 16 / ((alpha_1 alpha_2 alpha_3)^(2/3)|lambda_1 lambda_2 lambda_3|^(1/3))`.

The proof uses the sharp one-dimensional product-marginal bound `sqrt(2)` from Livshyts–Paouris–Pivovarov (arXiv:1507.07949), a self-contained decreasing-rearrangement estimate `||p_{lambda(Y+c)^2}||_{3/2}<=2K^(2/3)|lambda|^(-1/3)`, Hausdorff–Young to `L^3`, and Hölder across the three private product blocks. No law-uniform pointwise Fourier decay is used.

If two `lambda`s have the same sign, the same conditioning gives the sharper density-only bound

`||p_Q||_inf <= 2 pi /(alpha_i alpha_j sqrt(|lambda_i lambda_j|))`.

Explicit genuinely rotated indefinite instance: six coordinates, three orthonormal eigenvectors each with private mass `1/sqrt(2)` and overlapping a shared 3-coordinate block, eigenvalues `(2,-1,-1)`. The theorem gives a continuous density and the same-sign pair improves the universal bound for this instance to `4 pi` for arbitrary independent input densities <=1.

OTHER-account result actually applied: account01/B05 handoff at brain commit `5f703e4c639acefc3f33aa4d149fe5ff85814622`, blob `028e99f4705e07fac0fb369efb7ed63ec8927c35`. Its flat-Walsh minor calculation rules out treating this theorem as a generic chart argument: best-chart / naive Cauchy–Binet reciprocal-Jacobian averaging loses a polynomial factor. Named partner account03/B04 had started but had no completed qform handoff on the fresh read, so no peer PASS was inferred and the run did not wait.

First unpaid implication: a `soft-private-block / averaged rearrangement` theorem for arbitrary overlapping orthonormal large-eigenvalue triples that preserves the three `L^{3/2}` square budgets without paying reciprocal-minor or fiber-volume loss. The flat-Walsh family is the mandatory stress case.

Required corrections consumed: `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`. Fresh correction inbox before publication was empty at main `00bd16396410aae9a7bc394e03e733be30a801a6`.
