# Late-source addendum: exact rank-three cross-volume / basis localization identity

A later compatible result arrived after the main report was committed: account01/B01 `QFORM-RANDOM-SLOPE-CROSSMINOR-v1`, canonical report `yspennstate/math-open-problems@508b0985ba8bb658a7f6a935af5138a195cb89de`, proves that a physical triple `I` with cross-volume

`s_I = sqrt(det(A[I,I^c] A[I,I^c]^T))`

gives the continuous-density bound `||p_Q||_infinity <= 3 C_RV s_I^(-1/3)`, where `C_RV` is the absolute bounded-density projection constant. This addendum applies that result exactly to the pure rank-three residual.

## Exact identity

Let `A=U Lambda U^T` have rank exactly three, with `U^T U=I_3` and `|det Lambda|>=1`. For a physical triple `I`, put

`G_I=U_I^T U_I`,
`p_I=det(G_I)=det(U_I)^2`,
`q_I=det(I-G_I)`.

Then

`s_I^2 = det(A[I,I^c]A[I,I^c]^T)
       = det(Lambda)^2 p_I q_I`.                                      (A.1)

Indeed

`A[I,I^c]A[I,I^c]^T
 = U_I Lambda (U_{I^c}^T U_{I^c}) Lambda U_I^T
 = U_I Lambda (I-G_I) Lambda U_I^T`,

and taking determinants gives (A.1).

Cauchy--Binet also gives the exact complementary-basis interpretation

`q_I = det(U_{I^c}^T U_{I^c})
     = sum_{J subset I^c, |J|=3} det(U_J)^2`.                          (A.2)

Thus `{p_I}` is the projection-DPP basis mass of the rank-three frame and `q_I` is exactly the total basis mass on triples disjoint from `I`.

## Quantitative cross-volume-or-localization consequence

Fix `eta,tau in (0,1)`. If some physical triple `I` satisfies `p_I>=eta`, then exactly one of the following useful branches holds:

1. `q_I>=tau`. Then (A.1) gives
   `s_I >= |det Lambda| sqrt(eta tau)`,
   so account01/B01 yields
   `||p_Q||_infinity <= 3 C_RV |det Lambda|^(-1/3) (eta tau)^(-1/6)
                       <= 3 C_RV (eta tau)^(-1/6)`.
2. `q_I<tau`. Since the eigenvalues `gamma_1,gamma_2,gamma_3` of `G_I` lie in `[0,1]` and `q_I=prod_k(1-gamma_k)`, some `gamma_k>1-tau^(1/3)`. Therefore there is a unit spectral vector `w in R^3` such that
   `||U_I w||_2^2 > 1-tau^(1/3)`.
   Equivalently, one spectral direction is quantitatively concentrated on the three original coordinates in `I`.

This is an exact deterministic reduction, not a probabilistic approximation. It converts failure of the new cross-volume packet on any triple carrying nonnegligible rank-three basis mass into explicit three-coordinate spectral localization.

## Consequence for the unresolved extraction problem

Combine this with the main report and the named partner account03/B19. The unresolved rank-three hard branch can now be partitioned more sharply:

- diffuse original frame: already paid by the diffuse theorem;
- localized pivot with diffuse Schur residual: paid by account03/B19;
- a triple with nonnegligible basis mass and nonnegligible disjoint basis mass: paid by account01/B01 through (A.1);
- otherwise, every nonnegligible basis triple has a nearly supported spectral direction, so the residual task is a genuinely localized finite-coordinate / second-level aggregation problem rather than generic determinant spread.

What is still missing is a dimension-free argument that the partner's second-level localized hard branch must enter one of these paid alternatives (or the rectangular two-channel / dependent hyperbolic-square alternatives proved in the main report). No full-target proof is claimed.
