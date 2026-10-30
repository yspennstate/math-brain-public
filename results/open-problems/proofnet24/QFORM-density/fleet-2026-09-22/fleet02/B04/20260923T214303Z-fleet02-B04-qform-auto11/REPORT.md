SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T21:43:03Z.
attacking: rough Z-curvature aggregate routing—show that vanishing local zero-pivot determinants can coexist with target-scale optimized third-volume and ridge currency on the same physical matrix.

# fleet02/B04 — rough Z-curvature aggregate routing

Programme: `QFORM-DENSITY-3EIG-20260922`.
Owner control revision consumed: `2026-09-22.15`.
Execution status: `WITHOUT_VERIFIED_BRAIN`.
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING CONSTRUCTION / FULL TARGET OPEN`.

The unrestricted QFORM conjecture remains open. This run changes mechanism from the immediately preceding clean-bank receiver: it treats a literal rough-curvature realization of the fleet03/B04 zero-anchor star factorization and proves that aggregate physical cuts can pay it even when every useful local principal determinant vanishes like a negative power of dimension.

## 1. First unpaid implication

`QFORM-C1-ROUGH-ZCURVATURE-AGGREGATE-CUT-OR-CLEANBANK-v1`:

Starting from the fleet03/B04 star factorization

`2(b^T Y_N)(X_h+p^T Y_N)+2Y_N^T E_NZ Y_Z+Y_Z^T E_ZZ Y_Z`,

with `diag(E_ZZ)=0`, prove a dimension-free dichotomy before selecting a reciprocal local determinant:

1. some ORIGINAL-coordinate cut of the rough Z-bank exposes target-scale third-volume / determinant-retaining ridge currency; or
2. an ORIGINAL-coordinate clean or quantitatively near-clean subbank retains target-scale top-two crossing currency and the completed clean-bank rearrangement applies; or
3. route to an already completed pair / grouped-hub / D5 / projected-crossing endpoint.

The construction below proves branch (1) on a nontrivial dense rough-curvature family and simultaneously shows why local principal-triple selection is quantitatively wrong.

## 2. Exact rough-star family

Let `m=2^r>=16`. Index the Z-coordinates by bit strings `z in {0,1}^r`. Define three Walsh vectors

`u_z=m^(-1/2)`,
`r_z=m^(-1/2)(-1)^(z_1)`,
`s_z=m^(-1/2)(-1)^(z_2)`.

Then `u,r,s` are orthonormal in `R^m`.

Let `N={n_1,n_2}`, choose `0<eta<=1/2` and `0<beta<=1/8`, and define

`E = [2 r^T; 2 s^T] in R^(2 x m)`,
`G = (eta/m)(11^T-I_m)`.

In the ORIGINAL coordinate order `(h,n_1,n_2,Z)`, set

`A_(m,eta,beta) =
 [[0, beta, beta, 0],
  [beta, 0, 0, 2r^T],
  [beta, 0, 0, 2s^T],
  [0, 2r, 2s, G]].`

All `N-Z` coefficients are nonzero, all off-diagonal `Z-Z` coefficients are `eta/m`, and `G` has zero physical diagonal. No random-coordinate rotation is used.

Relative to the zero anchor `h`, the partner r41 notation has

`b=(beta,beta,0_Z)`, `p=0`, `E_NN=0`, `E_NZ=E`, `E_ZZ=G`.

Hence this is an exact realization of the previously unpaid `E_ZZ !=0` rough-curvature state.

Every principal triangle through `h` is singular. Indeed:

- on `{h,n_1,n_2}` the `n_1 n_2` edge is zero;
- on `{h,n_i,z}` the `hz` edge is zero;
- on `{h,z,z'}` both `hz` and `hz'` vanish.

Thus the newest fleet03/B04 zero-pivot 3-coordinate theorem has no `h`-anchored local determinant to invert.

## 3. Target validity

Let `A_0` be the same matrix with `beta=eta=0`. Its only nonzero block is the `N-Z` crossing `E`, whose two singular values are exactly `2,2`. Therefore

`spec(A_0)={2,2,-2,-2,0^(m-1)}`.

The perturbation consisting of the `h-N` star has operator norm `sqrt(2) beta`, while `||G||=eta(1-1/m)<eta`. Hence

`||A_(m,eta,beta)-A_0|| <= sqrt(2) beta + eta <= sqrt(2)/8 + 1/2 < 0.677`.

Weyl therefore leaves four eigenvalues of modulus at least

`2-(sqrt(2)/8+1/2) >1.32`.

So every member of this family satisfies the owner's exact spectral hypothesis and is indefinite and genuinely non-diagonal in the ORIGINAL independent coordinates.

## 4. Latest partner theorem applied: local determinant selection loses `m^(2/3)`

The newest compatible designated partner report is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T211945Z-fleet03-B04-QFORM-auto11/REPORT.md`

(blob `29ff1c0d4c7e78bcfb3b45c634df34fb1fb73058`). Its theorem says that an ORIGINAL physical principal triple with one zero diagonal and determinant magnitude `D>0` yields

`||p_Q||_infinity <= 3*2^(2/3) D^(-1/3)`.

For the present family, the largest nonzero physical principal `3x3` determinant is obtained on `{n_i,z_j,z_k}`. Since the matrix there is

`[[0,a_j,a_k],[a_j,0,g],[a_k,g,0]]`,

with `|a_j|=|a_k|=2/sqrt(m)` and `g=eta/m`,

`D_local = 2 |a_j a_k g| = 8 eta/m^2`.

All triples `{n_1,n_2,z}` are singular, and a pure-Z triple has determinant only `2 eta^3/m^3`. Thus the best certificate obtainable from the partner's local theorem on this family is exactly

`boxed:
 B_local = 3*2^(-1/3) m^(2/3) eta^(-1/3).`

This diverges with dimension although the aggregate rough curvature remains target-scale. This is an actual application of the partner theorem, not merely a qualitative citation.

## 5. Aggregate physical cut and exact optimized third-volume currency

Use the third Walsh bit to split

`L={z:z_3=0}`, `R={z:z_3=1}`,

so `|L|=|R|=m/2`. Take the ORIGINAL-coordinate cut

`I=L`, `J={n_1,n_2} union R`,

leaving only `h` outside to be conditioned.

The physical cross block is

`B=A[I,J]=[2r_L, 2s_L, (eta/m) 1_L 1_R^T].`

On `L`, the three vectors `r_L,s_L,1_L` are pairwise orthogonal. Consequently the three nonzero singular values of `B` are exactly

`sigma_1=sqrt(2), sigma_2=sqrt(2), sigma_3=eta/2`.

Therefore

`Z_3=e_3(B^T B)=sigma_1^2 sigma_2^2 sigma_3^2 = eta^2`.

For this exact-rank-three block, the canonical squared-minor volume law has row marginal equal to the rank-three leverage. Each normalized left singular vector has squared coordinate `2/m`, so every row marginal is

`alpha_z = 6/m <=3/8 <1/2`.

Thus the pinned Claude/e5 Theorem D applies.

More strongly, the admissible q=1 volume optimization is global. If `nu` is the canonical squared-minor law and `w` is any probability weight on supported physical `3x3` minors, its determinant-entropy currency satisfies the exact Gibbs identity

`log G(w)=log Z_3-D_KL(w||nu) <= log Z_3`.

Because `nu` itself already satisfies the row-marginal gate, the global optimum over every q=1 admissible physical volume weight is

`boxed: G_opt = eta^2.`

Applying the completed pinned source result at the actual inequality gives

`boxed:
 ||p_(X^T A X)||_infinity <= 6 sqrt(e) eta^(-1/3).`

No support, moment, log-concavity, diagonal-basis independence, or law-uniform pointwise oscillatory decay is used.

## 6. Determinant-retaining ridge on the identical cut

The same cut also has completely flat ridge leverage. For `gamma>0`, let

`k=2/(2+gamma^2)`,
`h=eta^2/(eta^2+4gamma^2)`,
`theta=2k+h`.

Then every physical row diagonal of

`K_gamma=B B^T(gamma^2 I+B B^T)^(-1)`

is exactly

`(K_gamma)_(zz)=2 theta/m < 6/m <=3/8 <1/2`.

For all sufficiently small `gamma`, `theta>2`, so the completed determinant-retaining q=1 ridge theorem applies:

`R_gamma = [e/(sqrt(2) gamma)] [theta/(theta-2)] D_gamma^(-1/(2theta))`,

where

`D_gamma=(1+2/gamma^2)^2(1+eta^2/(4gamma^2)).`

As `gamma ->0`,

`theta->3`,
`D_gamma ~ eta^2 gamma^(-6)`,

and therefore

`boxed:
 lim_(gamma->0) R_gamma = (3e/sqrt(2)) eta^(-1/3).`

Since every sufficiently small positive `gamma` gives a valid certificate, taking the infimum yields the rigorous bound

`boxed:
 ||p_(X^T A X)||_infinity <= (3e/sqrt(2)) eta^(-1/3).`

This ridge comparison is on exactly the same physical cut and matrix. It is stronger in constant than the pinned e5-D estimate, but both remove the spurious `m^(2/3)` local-determinant loss.

## 7. Concrete audit point

Take

`m=64`, `eta=1/2`, `beta=1/8`.

Then the target matrix has four eigenvalues of modulus greater than one. Numerically they are approximately

`-2.01167713, -2.00391006, 1.99609756, 2.00392519`,

while the rigorous Weyl lower bound is `>1.323`.

On the Walsh half-cut,

`singular values(B)=(sqrt(2),sqrt(2),1/4)`,
`Z_3=1/4`,
`alpha_z=3/32`.

The three relevant certificates are

`boxed:
 7.265141389555023...  ridge determinant limit,
 12.46355180618709... pinned e5 optimized D,
 48                 best partner local zero-pivot principal-triple bound.`

The best local principal determinant is exactly `1/1024`; every `h`-anchored principal triple is singular.

This is the quantitative point: **rough Z-curvature with tiny physical edges need not be paid by selecting one tiny local determinant. Aggregate third-volume or ridge currency can stay dimension-free.**

## 8. Source boundary and remaining debt

Pinned Claude/e5 source actually consumed:

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` re-read fresh. The full conjecture remains OPEN there; the pointwise-decay, arbitrary-joint coarea, and post-rotation-independence shortcuts remain forbidden.

Fresh designated partner actually consumed: fleet03/B04 `20260923T211945Z...`, theorem `QFORM-ZERO-PIVOT-3COORD-LINEAR-SQUARE-v1`.

The next unpaid step is no longer to handle this dense complete-graph roughness. It is to prove the aggregate-cut-or-cleanbank dichotomy for a general `E_ZZ`: extract a physical cut with determinant/ridge currency quantitatively tied to the rough C1 state, or prove that failure of every such cut leaves enough clean/near-clean Z-bank crossing to invoke the completed top-two product rearrangement. No small local coefficient may be inverted before that dichotomy.

Continuity is not promoted for the unrestricted target. Full QFORM remains OPEN.
