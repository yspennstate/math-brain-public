# account02/B13 r30 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture OPEN.

## First unpaid implication

`QFORM-RANK2-MISALIGNMENT-CORE-GLUE-v1`: after the canonical fiber-score-core reduction, close the remaining low-spectral cross interaction once its uncontrolled part has rank at most two, without rotating the independent variables or deleting the residual quadratic curvature. If this cannot be paid, convert the canonical-core alternatives below into a genuine bounded-finite-union product-indicator counterexample.

## New reduction being proved

Let `B` be any ORIGINAL-coordinate cross block in a slab witness of ratio `rho`. Let `P` be an arbitrary orthogonal projection acting on its column space; later `P=P_tau` is the partner account03/B13 spectral-range projection. The pinned Claude/Fourier D5 theorem at `e5f71d79eff325201dd0274053d20268ce65b837` gives

` s_5(B) <= C5/rho,   C5=5 sqrt(2e).`

Let `H` be the rank-at-most-four SVD truncation of `B`, `E=B-H`, so `||E||op<=C5/rho`. Put `H_Q=H(I-P)`. Since

`HH^T = HP(HP)^T + H_Q H_Q^T >= H_Q H_Q^T`,

Weyl monotonicity and perturbation imply

`s_3(H_Q) <= s_3(H) <= s_3(B)+||E||op`.

The pinned D' theorem at marginal threshold `h=2/3` has constant

`C3=9 sqrt(3e)`

and says that if the squared-third-minor row marginals of the physical block `B` are all at most `2/3`, then `rho<=C3/s_3(B)`. Apply it also to `B^T`. Consequently either

` s_3(B) <= C3/rho`,

or both a physical row and physical column have third-volume marginal `>2/3`; for the common squared-minor law their joint mass is `>1/3` by inclusion-exclusion.

Outside that physical third-volume bi-hub branch,

`s_3(H_Q) <= (C3+C5)/rho`.

Taking the best rank-two approximation `L` to `H_Q` gives the ORIGINAL coefficient identity

`B(I-P)=L+F,   rank(L)<=2,`

with

`||F||op <= (C3+2C5)/rho
           = 49.017460891320525.../rho.`

This is deterministic linear algebra after applying D5/D' to the genuine physical block `B`; no transformed random coordinates are introduced and no post-rotation independence is used.

The intended application to the designated partner's canonical-core compiler is: replace its rank-four low-spectral misalignment by this rank-two `L` plus an explicit `rho^{-1}` operator tail. The large-radius alternative is retained rather than suppressed, so fragmented and unbounded supports remain allowed.
