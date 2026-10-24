SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-24T03:38:39Z.
attacking: a global diffuse-to-localized bridge — use the designated partner's macroscopic half-cut on the top-three spectral frame, pay a small complementary spectrum by an actual rank-three physical crossing, and route a larger complementary spectrum through the spectral-window theorem.

# account01/B08 r42 — top-three diffuse frame reduces globally to a bounded density or one localized physical row

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW EXHAUSTIVE DIFFUSE-TO-LOCALIZED ROUTER / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. The theorem below proves a complete bridge for the diffuse top-three eigenspace: either the full quadratic form already has a universal continuous density bound, or one obtains an explicit ORIGINAL-coordinate localized row/scalar witness. No moment, support, Gaussian, log-concavity, iid, post-rotation independence, or pointwise oscillatory-decay assumption is used.

## 1. Completed inputs used

### 1.1 Designated partner account02/B08: balanced physical half-cut

From account02/B08 r28,

`yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`,

if `R` is an `n x 3` orthonormal frame with

`nu := max_i ||R_{i,*}||_2^2 <= 1/48`,

there is an ORIGINAL-coordinate partition `S disjoint_union T` such that

`R_S^T R_S >= I_3/4`, `R_T^T R_T >= I_3/4`.                    (1.1)

This partner result is applied below to the actual top-three absolute-eigenvalue frame of `A`, not merely cited.

### 1.2 Literal-cross volume stability

From

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,

for an actual ORIGINAL-coordinate cross block `M=M0+E`, if

`s_3(M0)>=a`, `max_i(P_Ran(M0))_ii<=1/2`, `||E||op<=a/16`,

the full ambient quadratic-plus-affine form has a continuous `C_0` density and

`||p_Q||_infinity < 23/a`.                                      (1.2)

All within-bank curvature and outside couplings are retained.

### 1.3 Reviewed spectral-window theorem

The one-scale ridge theorem is source-pinned at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

After scaling: if a symmetric matrix has at least three eigenvalues of absolute value at least `sigma>0`, and `P_sigma` denotes the full spectral projection onto

`{|lambda(A)| >= sigma/64}`,

then

`max_i (P_sigma)_{ii} <=1/32`

implies a continuous `C_0` density with

`||p_Q||_infinity <= C_RW/sigma`,
`C_RW = 288 sqrt(3e)/13 = 63.26405187778285...`.                 (1.3)

Arbitrary smaller nonzero eigenvalues of either sign are allowed.

The newest account02/B08 r31 handoff was also read. Its exact rank-one resonant hypotheses are not forced in the present global frame argument, so they are not silently imported. The partner result actually applied at an equation here is r28, (1.1).

## 2. Main structural decomposition

Let `A=A^T` and let its absolute eigenvalues be ordered

`s_1(A)>=s_2(A)>=s_3(A)>=s_4(A)>=...`.

Fix `L>0` with

`s_3(A)>=L`.                                                     (2.1)

Choose orthonormal eigenvectors `r_1,r_2,r_3` corresponding to the three largest absolute eigenvalues and put

`R=[r_1,r_2,r_3]`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`,
`A_3=R Lambda R^T`, `E=A-A_3`.                                  (2.2)

Then

`min_j |lambda_j|>=L`, `||E||op=s_4(A)`.                        (2.3)

Write

`nu=max_i ||R_{i,*}||^2`.                                       (2.4)

The theorem separates the diffuse frame `nu<=1/48` from a literal localized row `nu>1/48`.

## 3. Diffuse frame and small complementary spectrum

Assume

`nu<=1/48`, `s_4(A)<=L/64`.                                     (3.1)

Apply the completed account02/B08 half-cut (1.1) to `R`. Let

`M0=A_3[S,T]=R_S Lambda R_T^T`.                                 (3.2)

Because both restricted Gram matrices are at least `I/4`,

`s_3(R_S)>=1/2`, `s_3(R_T)>=1/2`.                               (3.3)

Therefore the partner cut gives the actual inequality

`boxed: s_3(M0) >= (1/2) L (1/2) = L/4.`                        (3.4)

Since `Lambda` is invertible and `R_T` has full column rank,

`Ran(M0)=Ran(R_S)`.                                              (3.5)

For `i in S`, the row leverage of this range is

`(P_Ran(M0))_ii
 = R_{i,*}(R_S^T R_S)^(-1)R_{i,*}^T
 <=4 ||R_{i,*}||^2
 <=1/12 <1/2`.                                                   (3.6)

The ACTUAL physical crossing is

`M=A[S,T]=M0+E[S,T]`,                                            (3.7)

and a coordinate compression cannot increase operator norm, so

`||E[S,T]||op <= ||E||op=s_4(A)<=L/64=(L/4)/16`.                (3.8)

Thus (1.2) applies with `a=L/4` and proves

`boxed: ||p_Q||_infinity < 92/L`,                               (3.9)

with a continuous `C_0` representative.

This closes the entire diffuse-top-three / small-complementary-spectrum branch. The complementary spectrum is not treated as a small random variable; its actual cross block stays in (3.7) and is consumed by the deterministic volume-stability theorem.

## 4. Diffuse frame and large complementary spectrum

Continue to assume `nu<=1/48`, but now suppose

`sigma := s_4(A) > L/64`.                                       (4.1)

There are at least four, hence at least three, eigenvalues of absolute value at least `sigma`. Let `P` be the full spectral projection onto

`{|lambda(A)|>=sigma/64}`.                                      (4.2)

If

`max_i P_ii<=1/32`,                                             (4.3)

then the scaled spectral-window theorem (1.3) gives

`||p_Q||_infinity <= C_RW/sigma
 < 64 C_RW/L
 =4048.899320178102.../L
 <4049/L`,                                                       (4.4)

again with a continuous `C_0` representative.

It remains to understand failure of (4.3). Choose an ORIGINAL coordinate `k` with

`P_kk>1/32`.                                                     (4.5)

By the spectral theorem,

`||A e_k||_2^2
 = sum_j lambda_j^2 |<e_k,r_j>|^2
 >= (sigma/64)^2 P_kk
 > sigma^2/(64^2*32)`.                                          (4.6)

Since

`||A e_k||_2^2=A_kk^2+||A[-k,k]||_2^2`,                         (4.7)

at least one of the two terms has magnitude at least `||Ae_k||/sqrt(2)`. Hence

`boxed:
 max{|A_kk|, ||A[-k,k]||_2}
 > sigma/512
 > L/32768.
`                                                                    (4.8)

Thus a failure of the high-window diffuse gate produces an explicit localized ORIGINAL-coordinate scalar/star witness; it does not leave an abstract spectral obstruction.

## 5. Non-diffuse top-three frame is already localized

If instead

`nu>1/48`,                                                       (5.1)

choose `k` with `||R_{k,*}||^2>1/48`. Using only the three selected eigenvectors,

`||Ae_k||_2^2 >= L^2 ||R_{k,*}||^2 > L^2/48`.                  (5.2)

Therefore

`boxed:
 max{|A_kk|,||A[-k,k]||_2}>L/sqrt(96)
 =0.1020620726... L.
`                                                                    (5.3)

This is much stronger than the witness in (4.8).

## 6. Exhaustive theorem

### Theorem 6.1 — `QFORM-TOP3-DIFFUSE-TO-LOCALIZED-ROW-v1`

Let `A=A^T` satisfy `s_3(A)>=L>0`. For independent real inputs with one-dimensional densities bounded by one, exactly one of the following conclusions is available from the preceding proof:

1. the full quadratic form `Q=X^TAX` has a continuous `C_0` density satisfying

   `boxed: ||p_Q||_infinity <4049/L`;                            (6.1)

   or

2. there is an ORIGINAL coordinate `k` satisfying

   `boxed:
   max{|A_kk|,||A[-k,k]||_2}>L/32768.
   `                                                                  (6.2)

More precisely:

- if the top-three frame is diffuse and `s_4(A)<=L/64`, the stronger bound `<92/L` holds;
- if the top-three frame is diffuse and `s_4(A)>L/64`, either `<4049/L` holds or (6.2) holds;
- if the top-three frame is not diffuse, the stronger witness (5.3) holds.

This is an exhaustive product-preserving bridge from the diffuse spectral regime to localized-coordinate currency. It does **not** assert that the single localized witness (6.2) alone already yields a universal density bound; live corrections explicitly rule out several one-pivot/one-star shortcuts. Consequently the full conjecture remains OPEN.

For the owner's target scale `L=1`, the theorem is simply:

`p_Q in C_0 and ||p_Q||_infinity<4049`

or

`exists k: max{|A_kk|,||A[-k,k]||_2}>1/32768`.

## 7. Why this changes the remaining B08 problem

The long r36--r41 deletion analysis isolated a super-aligned diffuse star with a tiny nonzero spectral-tail residual. The present theorem changes mechanism and bypasses that endpoint at the top-three-frame level. Before entering the delicate deletion geometry, the whole matrix can be routed as follows:

- small fourth singular value: the designated partner's physical half-cut plus literal-cross stability pays the full form;
- large fourth singular value: the reviewed spectral-window theorem pays the form unless it itself exposes an original-coordinate localized row;
- non-diffuse top-three frame: the localized row is immediate.

Therefore the first B08 obligation is no longer the star angle. It is now

`QFORM-LOCALIZED-ROW-COMPILER-v1`:

> starting from the explicit original-coordinate witness
> `max{|A_kk|,||A[-k,k]||_2}>L/32768`,
> combine it with the remaining three-large-eigenvalue spectral information to produce either a valid localized conditioning receiver or a further grouped-coordinate certificate, without assuming a uniformly good finite minor and without discarding arbitrary complementary spectrum or conditioning-generated affine terms.

This is exactly the intended complement between diffuse eigenvector geometry and localized-coordinate conditioning.

## 8. Corrections and scope

No use is made of:

- uniform pointwise van-der-Corput decay;
- arbitrary-joint quadratic coarea bounds;
- conditional density caps after non-product changes of variables;
- independence after a spectral rotation;
- a uniformly good single 2x2 or 3x3 physical minor;
- Monte Carlo evidence as proof.

The paid branches prove continuity because both analytic receivers used above produce `C_0` densities. The localized-witness branch has no density conclusion yet. Hence full-target continuity remains OPEN together with the full universal bound.
