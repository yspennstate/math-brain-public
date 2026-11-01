# fleet02/B13 r26 — early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

First unpaid implication: `QFORM-STAR-COVER-TRANSVERSE-SPOKE-CLOSURE-v1` — after the exact mixed-Fresnel payment below, handle the cases where the residual three-column coupling frame is leverage-concentrated/rank-deficient, or where the leaf-curvature graph is only dominated rather than covered, without deleting nonzero curvature or rotating product coordinates.

## Exact star-cover payment

Take two original-coordinate hubs `H0={h1,h2}` and a distinguished original leaf `j*`. Assume that, after conditioning any outside coordinates, every off-diagonal leaf-leaf coefficient among the remaining leaves `L` is zero; equivalently `j*` is a vertex cover for the non-diagonal leaf curvature before moving it into the heavy set. Put `H=H0 union {j*}`, `C=A[L,H]`, `Gamma=C^T C`. If `Gamma` is invertible and every physical row `c_l` has leverage `c_l^T Gamma^{-1} c_l <=1/2`, then the proved pinned mixed-Fresnel theorem (math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, FOURIER_ROUTE_REPORT.md, Theorem MF with r=0 and |H|=3) gives

`|phi_Q(t)| <= (2*pi)^3 |t|^{-3} det(Gamma)^(-1/2)`.

Integrating `min(1,B|t|^{-3})` exactly yields

`||p_Q||_infinity <= 3 det(Gamma)^(-1/6)`.

Hence a slab witness of ratio `R` in this branch necessarily satisfies

`det(Gamma) <= (3/R)^6`.

Writing the residual two-hub coupling matrix as `Rmat=A[L,H0]` and the curvature-spoke column as `c=A[L,{j*}]`, the Gram Schur identity gives, whenever `Rmat` has rank two,

`det(Gamma)=det(Rmat^T Rmat) * ||P_{col(Rmat)^perp} c||_2^2`.

If `j*` is also the determinant-star centre of the previous B13 two-hub frame `B`, with leverage `h`, then `det(Rmat^T Rmat)=(1-h)det(BB^T)`. Thus every high-density balanced star-cover witness obeys the new target-level obstruction

`(1-h) det(BB^T) ||P_{col(Rmat)^perp} c||_2^2 <= (3/R)^6`.

No support/moment assumption, spectral rotation, or perturbative deletion is used; all heavy/leaf coordinates are original physical coordinates. The partner fleet03/B13 local-3x3 compiler will be combined with this in the final report.
