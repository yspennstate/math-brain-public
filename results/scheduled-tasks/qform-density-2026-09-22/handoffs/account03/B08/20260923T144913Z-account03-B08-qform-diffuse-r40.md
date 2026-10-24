SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T14:49:13Z.
attacking: localized-triangle plus second-arm receiver: convert Schur-cancellation packet into a physical 3x3 determinant or a two-bank fractional smoothing inequality while retaining arbitrary curvature.

# account03/B08 r40 handoff — triangle rank-one escape + cancellation-stable pair receiver

Full mathematics: `yspennstate/math-open-problems@b7556cdf6324f77477282920e1905de61003e86a:proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T144913Z-account03-B08-qform-diffuse-r40/REPORT.md`.

Status: new supporting structural router and proved scoped target family; full conjecture OPEN; independent review pending; execution `WITHOUT_VERIFIED_BRAIN`.

## New structural theorem

For a physical triangle

`T=[[a,u,v],[u,b,h],[v,h,c]]`, `a!=0`,

put

`d1=ab-u^2`, `d2=ac-v^2`, `k=ah-uv`,

`Delta_T=sqrt(d1^2+d2^2+2k^2)/|a|`.

If the full matrix is `A=[[T,C],[C^T,D]]`, then

`boxed: s3(A)<=s1(C)+||D||op+Delta_T`.

Hence, if `s3(A)>=L`, for every `0<rho<1` either

`max{|d1|,|d2|,|k|}>(rho/2)|a|L`

or

`max{s1(C),||D||op}>=(1-rho)L/2`.

At `rho=1/4`, this is physical minor scale `>|a|L/8` or outside scale `>=3L/8`.

The exact obstruction to the naive r38 implication is important: taking `b=u^2/a`, `c=v^2/a`, `h=uv/a` makes the triangle rank one and gives `d1=d2=k=det T=0` while `uv=ah`. Therefore the localized product packet alone does NOT force an invertible physical pair or nonzero triangle determinant.

## Actual newest-volume application

On the near-rank-one branch `Delta_T<=L/4`, if `||D||op<3L/8`, then `s1(C)>3L/8`. Orient `M=C^T`. If `s3(C)>=L/16` and the row-range projection of `C^T` has maximum physical-coordinate leverage at most `1/2`, apply the current `c2414ef...` volume-stability theorem with `M0=M`, error zero, and scale `L/16`. The FULL ambient form then has a continuous `C_0` density with

`boxed: ||p_Q||infinity<368/L`.

Failure is now explicitly either `dist_op(C,rank<=2)<L/16` or a physical outside coordinate of leverage `>1/2`. This is the requested quantitative join from diffuse volume to low-cross-rank/high-leverage survivors, with the full spectrum retained.

## New analytic endpoint

If three physical coordinates have rank-one principal block `sigma c c^T`, two disjoint physical coordinates have an invertible symmetric pair block `B`, and the five-coordinate principal block is their block direct sum (outside couplings arbitrary), then conditioning only original coordinates and applying the orientation-free rank-two half-Riesz theorem gives

`boxed: ||p_Q||infinity <=128 sqrt(3)||c||^{-1}|det B|^{-1/4}`.

If `h` is an off-diagonal coefficient of the rank-one triangle,

`boxed: ||p_Q||infinity <=128 sqrt(3/2)|h|^{-1/2}|det B|^{-1/4}`.

Essential boundedness is proved; continuity is not claimed.

For the exact maximally-cancelled target family

`c=(sqrt(L),sqrt(L/R),sqrt(L/R))`, `T=cc^T`, `B=[[0,LR],[LR,0]]`,

the spectrum is `{L(1+2/R),+LR,-LR,0,0}`, hence target-valid for `L>=1,R>=1`; scalar Schur completion of the small arm cancels exactly. The clean direct-sum refinement gives

`boxed: ||p_Q||infinity<=128/L` uniformly in `R`.

The designated account04/B08 result was applied separately to the non-cancelled companion family

`L X0^2+2LR U1V1+2L R^{-1}U2V2`,

giving its completed inequality `||p_Q||infinity<7.251/L`. Thus the partner theorem and the new receiver pay opposite anisotropic endpoints.

Checks: committed `CHECKS.py`/`CHECKS.txt`; 5,000 seeded tests verify the exact triangle identity/decomposition and the singular-value router; the checker ends `QFORM_B08_R40_CHECK_PASS`.

Remaining first B08 debt: `QFORM-LOWRANK-HIGHLEVERAGE-TWOARM-INTERPOLATION-v1` — handle near-rank-one triangle states where the outside cross block is rank-two/high-leverage and the second arm is not a separated invertible pair because arbitrary within-bank curvature/couplings interact with it. Complementary curvature `||D||op>=3L/8` must also be integrated with the global high-spectral-leverage/ridge router. Global continuity remains OPEN.
