SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T15:36:26Z.
attacking: diffuse-eigenvector aggregate passage — derive an exact squared-energy child/cross ledger and use it to strengthen the live k=1 collective-tail branch without deleting any spectral remainder.

# fleet01/B08 — squared-energy child/cross ledger

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / analytic derivation and exact structural identities  
**Classification:** `PROVED SUPPORTING STRUCTURAL THEOREM + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains **OPEN**. Global continuity remains **OPEN**. Every statement below keeps the original-coordinate product structure and the complete literal matrix. No moment, support, Gaussian, log-concavity, iid, post-rotation independence, pointwise law-uniform quadratic-phase decay, arbitrary-joint coarea estimate, worst-fiber supremum, or perturbative deletion of a matrix tail is used.

## 1. First missing implication attacked

The current diffuse spectral gate starts with three genuine eigenvectors

`A R = R Lambda`, `R^T R=I_3`, `min_j |lambda_j|>=L`,

and a balanced ORIGINAL-coordinate cut `I|J`. Previous work transferred missing principal curvature to the true cross block, but with the quantitative floor

`beta L = (3/16)sqrt(3/5) L = 0.14523687548...L`.

This run proves a sharper exact identity by squaring the **full** matrix first. It yields the cross floor

`delta L = (3/sqrt(40))L = 0.4743416490...L`

on every non-three-child branch of the current gate, an improvement by the exact factor

`delta/beta=sqrt(32/3)=3.2659863237...`.

The point is that `A^2` is positive semidefinite on every spectral direction, so the arbitrary complementary spectrum can help but cannot cancel the selected three large directions. This avoids the principal-block cancellation issue that forces weaker first-order transfer estimates.

## 2. Exact squared-energy ledger

Write the physical block decomposition

`A = [[C,B],[B^T,D]]`,

where `C=A[I,I]`, `D=A[J,J]`, and `B=A[I,J]`. Put

`G_I=R_I^T R_I`, `G_J=R_J^T R_J`.

### Theorem 2.1 — `QFORM-SQUARED-ENERGY-CHILD-CROSS-LEDGER-v1`

Assume

`G_I >= alpha I_3`, `G_J >= alpha I_3`

for some `alpha>0`. Then, for each `k=0,1,2`,

`boxed: s_{k+1}(C)^2 + s_{3-k}(B)^2 >= alpha L^2,`        (2.1)

and simultaneously

`boxed: s_{k+1}(D)^2 + s_{3-k}(B)^2 >= alpha L^2.`        (2.2)

Here singular values are in decreasing order. In particular, for either physical side `K`, if

`s_{k+1}(A[K,K]) < cL`

with `0<=c<sqrt(alpha)`, then

`boxed: s_{3-k}(B) > sqrt(alpha-c^2) L.`                 (2.3)

The theorem is sign-free and remains valid with repeated eigenvalues and arbitrary extra nonzero spectrum.

### Proof

Extend the three selected eigenvectors to an orthonormal eigenbasis of the real symmetric matrix `A`. Since the selected eigenvalues satisfy `Lambda^2>=L^2 I_3`, spectral calculus gives

`A^2 - R Lambda^2 R^T >=0`.                                  (2.4)

Taking the `I x I` principal block and using the literal block-square identity gives

`C^2 + B B^T = (A^2)[I,I]
               >= R_I Lambda^2 R_I^T
               >= L^2 R_I R_I^T`.                            (2.5)

The three nonzero eigenvalues of `R_I R_I^T` equal the three eigenvalues of `G_I=R_I^T R_I`, hence each is at least `alpha`. Therefore

`lambda_3(C^2+B B^T) >= alpha L^2`.                           (2.6)

For positive semidefinite matrices, Weyl's upper inequality says

`lambda_{i+j-1}(X+Y) <= lambda_i(X)+lambda_j(Y)`              (2.7)

whenever `i+j-1` is in range. Apply (2.7) to `X=C^2`, `Y=BB^T` with

`(i,j)=(1,3),(2,2),(3,1)`.

Because `C` is symmetric,

`lambda_i(C^2)=s_i(C)^2`,

and because `lambda_j(BB^T)=s_j(B)^2`, (2.6)-(2.7) give (2.1). The identical argument on the `J x J` principal block,

`D^2+B^T B=(A^2)[J,J] >= L^2 R_JR_J^T`,

gives (2.2). Finally (2.3) follows by subtraction. QED.

### Why this is safe under the current correction set

The proof is entirely deterministic matrix algebra in the original coordinate decomposition. It never rotates the random variables. It does not replace `A` by the selected rank-three component: the complementary spectrum is retained inside `A^2`, and its squared spectral contribution is positive semidefinite. Thus there is no small-tail/random-perturbation step and no sign restriction.

## 3. Actual application to the completed fleet02/B08 spectral gate

The completed fleet02/B08 r18 source is

`yspennstate/math-open-problems@9fb59f9549a85af6173ade505fd53bc035c611ba`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T004036Z-fleet02-B08-qform-diffuse-r18/REPORT.md`.

It works under selected-three leverage `<=1/48` and, using its designated partition theorem, supplies an ORIGINAL-coordinate cut with

`G_I >= (3/8)I_3`, `G_J >= (3/8)I_3`.                          (3.1)

It defines the child threshold

`c=(1/2)sqrt(3/5)=sqrt(3/20)`                                  (3.2)

and child counts `k_I,k_J` equal to the number of physical-child eigenvalues of modulus at least `cL`. Let `k=min(k_I,k_J)` and orient the cut so the `I` child realizes that minimum. If `k<3`, then by definition

`s_{k+1}(C)<cL`.                                                (3.3)

Apply Theorem 2.1 with `alpha=3/8`. Since

`3/8 - c^2 = 3/8-3/20=9/40`,                                  (3.4)

we obtain the sharpened actual spectral gate

`boxed: k=0 => s_3(B) > (3/sqrt40)L,`

`boxed: k=1 => s_2(B) > (3/sqrt40)L,`

`boxed: k=2 => s_1(B) > (3/sqrt40)L.`                          (3.5)

The old partner threshold was

`beta=(3/16)sqrt(3/5)`,

so (3.5) improves it by

`(3/sqrt40)/beta = sqrt(32/3)`.                                (3.6)

This is an application to the partner's **actual physical cut and actual child count**, not to a rank-three surrogate.

## 4. k=0 branch: immediate stronger full-form payment or bilateral stars

A completed earlier B08 theorem is

`yspennstate/math-open-problems@0a9b587adf257c8983f8351de2670006c75e02fe`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260923T063906Z-fleet01-B08-qform-r24/REPORT.md`,

Theorem `QFORM-S3-VOLUME-OR-BILATERAL-STAR-v1`. At `q=1`, if an ORIGINAL-coordinate cross block has `s_3(B)>=sigma`, then either the full ambient quadratic form has a continuous `C_0` density with

`||p_Q||_infinity <= 6sqrt(e)/sigma`,                           (4.1)

or there are an original physical row and column with star norms each `>sigma/sqrt6`.

Insert `sigma=delta L`, `delta=3/sqrt40` from (3.5). The entire k=0 branch therefore satisfies the exhaustive alternative

`boxed: ||p_Q||_infinity < 4sqrt(10e)/L
       =20.8548577688.../L`                                    (4.2)

with a continuous `C_0` density, or there are opposite-side physical stars each exceeding

`boxed: (sqrt15/20)L =0.19364916731...L.`                       (4.3)

This is a substantial strengthening of the preceding k=0 constants and retains arbitrary same-bank blocks and all extra spectrum.

## 5. k=1 branch: energy-upgraded collective-tail router

The completed designated-partner r27 report is

`yspennstate/math-open-problems@41ee49f6e9c3383e4c3a322bdc52779768a17eb7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T130941Z-fleet02-B08-qform-diffuse-r27/REPORT.md`.

Its source-pinned collective-tail theorem uses, for the ACTUAL cross block,

`T_2=sum_{nu>=3}s_nu(B)^2`,

and the top-two left singular projector `P_2`. When

`max_i(P_2)_{ii}<=1/2`, `T_2/s_3(B)^2>=225`,                  (5.1)

it proves for the full ambient form

`||p_Q||_infinity
 <=(9sqrt(3)e/2)[s_1(B)^2s_2(B)^2T_2]^(-1/6)`,                 (5.2)

continuously.

Rerun that exact partner argument with the now-proved

`s_2(B)>delta L`, `delta=3/sqrt40`,                            (5.3)

instead of the old `beta L`. Set

`gamma=delta/64 = 3/(64sqrt40)=0.007411588266...`.             (5.4)

Then at least one of the following holds.

**(V) Collective-tail payment:**

`boxed: ||p_Q||_infinity < (12sqrt30 e)/L
       =178.663713012.../L`,                                   (5.5)

with a continuous `C_0` density.

**(R2) Genuine Frobenius rank-two tube:**

`boxed: dist_F(B,{rank<=2}) < gamma L
       =0.007411588266...L.`                                   (5.6)

**(SR) Low stable-rank tail:** if `s_3(B)>0`,

`boxed: T_2/s_3(B)^2 <225.`                                    (5.7)

**(H) Heavy top-two physical row:** there is an original physical row `i` with

`(P_2)_{ii}>1/2`,                                               (5.8)

and then the actual cross row `g=B^Te_i` obeys

`boxed: ||g|| > delta L/sqrt2
       =3L/sqrt80
       =(3sqrt5/20)L
       =0.335410196625...L > L/4.`                              (5.9)

### Proof of the upgraded constants

If (R2) fails, `T_2>=gamma^2L^2`. If (SR) and (H) also fail, (5.1) holds and (5.2) applies. Since `s_1,s_2>=delta L`,

`s_1^2s_2^2T_2 >= delta^4 gamma^2 L^6`.

With `gamma=delta/64`, the sixth root of the reciprocal currency is `4/(delta L)`. Hence

`||p_Q||_infinity
 <=(18sqrt3 e/delta)L^(-1)
 =12sqrt30 e L^(-1)`,

which is (5.5). In branch (H), the exact SVD row-energy identity gives

`||g||^2=sum_nu s_nu^2u_nu(i)^2
        >=s_2^2[(P_2)_{ii}]
        >delta^2L^2/2`,

which is (5.9). QED.

Compared with partner r27, the continuous collective-tail constant drops from `<584/L` to `<179/L`, while its high-row survivor is upgraded from a `0.1027L` star to a literal `>0.3354L` star. Thus the r27 child-aligned/transverse split is unnecessary on this heavy-row branch: it already lands beyond the live quarter-star threshold.

## 6. What remains unpaid

This does **not** prove full QFORM. The first B08 implication after this run is narrower:

`QFORM-ENERGY-GATE-LOWRANK-OR-QUARTERSTAR-RECEIVER-v1`:

> In the k=1 state, pay the genuine Frobenius rank-two tube (5.6), the low-stable-rank tail (5.7), or the literal `>L/4` physical star (5.9), while retaining arbitrary same-bank curvature, all unused couplings, arbitrary complementary spectrum and conditioning-generated affine terms. In the k=0 state, pay the bilateral-star survivor (4.3). The k=2 state now has the stronger actual cross direction `s_1(B)>0.47434L` but still needs a product-preserving receiver combining it with its two child directions.

A bare `ell^2` star is not silently promoted to a density theorem. The Hadamard hybrid from fleet02/B08 remains a valid warning that bounded physical-pivot selection can lose dimension; the compiler must aggregate before inversion when the star/cross mass is delocalized.

## 7. Finite sanity checks

A deterministic-seed numerical checker was run on random symmetric matrices with three marked eigenvalues, searching for cuts satisfying the theorem's Gram hypothesis. Across 434 accepted balanced cuts (2604 side/index inequalities), there were zero violations of (2.1)-(2.2). The checker is only a sanity test; the proof is the spectral/Weyl argument above.

No full-solution review is claimed. Two independent end-to-end reviews would still be required for a full candidate.
