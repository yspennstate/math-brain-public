SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T02:44:34Z.
attacking: strict-N3 exact global star survivor; combine the two-hub physical-star Fourier theorem with a spectral perturbation argument to eliminate both exact alignment and high row leverage.

# account03/B09 r22 — strict-N3 global physical star is fully paid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **NEW TARGET-LEVEL STRUCTURAL EXIT / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a complete bounded-continuous-density exit for the global physical-star branch of the current strict no-pivot class `N3(1/128)`. It does not claim that every target matrix has this geometry.

No Gaussianity, moments, compact support, connected support, log-concavity, identical laws, or independence after a spectral rotation is used. The proof stays in original physical coordinates. It does not use law-uniform pointwise van-der-Corput decay, arbitrary-joint rank-three coarea, a worst conditional projection-density supremum, or a single-good-minor assertion.

## 1. Source theorem actually applied

The predecessor is account01/B09's completed two-hub star theorem, canonical source

`yspennstate/math-open-problems@344963502d821945c7af02ab8d7272536dab8e5c`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T021354Z-account01-B09-QFORM-auto11/REPORT.md`,

with the subsequent global-scope clarification at commit

`aa3a9fa9f63baf640ff8707925851928debb73af`.

Its theorem `QFORM-TWOHUB-PHYSICAL-STAR-DIFFUSE-v1` says the following. Let `{h,s}` be two ORIGINAL physical coordinates and let `I` be a disjoint physical leaf bank such that `A_II` is diagonal. Define

`rho_i=(A_ih,A_is) in R^2`,

`G=sum_(i in I) rho_i rho_i^T`.

If `G` is nonsingular and every normalized row leverage obeys

`rho_i^T G^(-1) rho_i <= 1/2`,

then, uniformly under all coefficients involving an additionally conditioned outside bank,

`||p_Q||_infinity <= 4 det(G)^(-1/4)`,                         (1.1)

and the characteristic function is integrable. Therefore the density is continuous and

`P{Q in L} <= 4 det(G)^(-1/4) |L|`                             (1.2)

for every interval `L`.

Below I prove that, in the strict-N3 **global star** chamber at the current threshold, the two hypotheses that were left open in that theorem — nonalignment and the leverage gate — are automatic, quantitatively.

## 2. Strict-N3 global star setup

Fix `tau>0`. Assume the target spectral condition

`s_3(A) >= 1`,                                                   (2.1)

where `s_3` is the third singular value of the real symmetric matrix `A`, together with the strict no-pivot inequalities

`|A_ii| < tau` for every `i`,                                    (2.2)

`|det A[{i,j},{i,j}]| < tau` for every `i != j`.                (2.3)

Fix one physical hub `h`. Assume the off-diagonal support on its **entire physical complement** is a star centered at one coordinate `s`. Put

`I={1,...,n}\{h,s}`.

Then `A_II` is diagonal. Define the two leaf-to-hub vectors

`c_i=A_ih`, `b_i=A_is`, `i in I`,

and the rectangular mixed-frame matrix

`C=[c,b] in R^(|I| x 2)`.                                       (2.4)

The source theorem from Section 1 is exactly adapted to this geometry. The issue is to prove, from (2.1)--(2.3) alone, that `C` has two quantitative singular directions and no row carries excessive leverage.

## 3. Pair determinants force every physical edge to be small

For `i != j`,

`det A[{i,j},{i,j}] = A_ii A_jj - A_ij^2`.

Hence (2.2)--(2.3) imply

`|A_ij|^2
 <= |A_ii A_jj| + |det A[{i,j},{i,j}]|
 < tau^2+tau`.                                                   (3.1)

Set

`q=sqrt(tau+tau^2)`.                                             (3.2)

Thus every off-diagonal physical coefficient satisfies

`|A_ij|<q`.                                                      (3.3)

In particular every row of `C` satisfies

`||rho_i||_2^2=c_i^2+b_i^2<2q^2`.                              (3.4)

## 4. Spectral forcing of a two-dimensional mixed frame

In the splitting `{h,s} union I`, define

`A0 = [[0_(2x2), C^T],
       [C,        0   ]]`.                                      (4.1)

Because the leaf off-diagonal support is globally a star centered at `s`, the difference

`E=A-A0`                                                        (4.2)

is block diagonal: one block is the physical `2 x 2` hub block `A[{h,s},{h,s}]`, and the other is the diagonal matrix `diag(A_ii : i in I)`.

The latter has operator norm `<tau`. For the hub block, (2.2) and (3.3) give maximum absolute row sum `<tau+q`, hence

`||A[{h,s},{h,s}]||_op < tau+q`.

Therefore

`||E||_op < delta := tau+q`.                                    (4.3)

The nonzero eigenvalues of `A0` are

`+sigma_1(C), -sigma_1(C), +sigma_2(C), -sigma_2(C)`,           (4.4)

with zeros thereafter. Equivalently its singular values are

`sigma_1(C),sigma_1(C),sigma_2(C),sigma_2(C),0,...`.

By the 1-Lipschitz perturbation inequality for singular values,

`sigma_2(C)=s_3(A0)
 >= s_3(A)-||A-A0||_op
 > 1-delta`.                                                     (4.5)

Put

`mu=1-tau-sqrt(tau+tau^2)`.                                     (4.6)

Whenever `mu>0`, (4.5) gives

`sigma_2(C) >= mu`.                                              (4.7)

This is the first essential implication: **exact alignment is impossible** in the strict-N3 global-star chamber. In particular `G=C^T C` is positive definite and

`lambda_min(G)=sigma_2(C)^2 >= mu^2`,                           (4.8)

`det G=sigma_1(C)^2 sigma_2(C)^2 >= mu^4`.                      (4.9)

No individual minor was selected; the full two-column frame is paid before inversion.

## 5. The same spectral gap forces the row-leverage gate

For every `i in I`, using (3.4) and (4.8),

`ell_i := rho_i^T G^(-1)rho_i
 <= ||rho_i||_2^2 / lambda_min(G)
 < 2q^2/mu^2`.                                                   (5.1)

Consequently, if

`2(tau+tau^2)/[1-tau-sqrt(tau+tau^2)]^2 <= 1/2`,               (5.2)

the exact source theorem (1.1) applies to the full ambient quadratic form.

Combining (1.1) and (4.9) yields

`boxed: ||p_Q||_infinity <= 4/mu`                               (5.3)

and, for every interval `L`,

`boxed: P{X^T A X in L} <= (4/mu)|L|.`                          (5.4)

Because the source characteristic-function estimate is `L^1`, this branch has a **continuous density**, not merely an essentially bounded one.

Thus the former `high-row-leverage` exception is also impossible once the strict-N3 spectral hypothesis is imposed at a threshold satisfying (5.2).

## 6. Current threshold tau=1/128

At the strict threshold used by the current N3 compiler,

`tau=1/128`,

`q=sqrt(129)/128 = 0.088732942903129...`,

`mu=(127-sqrt(129))/128 = 0.903454557096871...`.

The leverage estimate is

`2q^2/mu^2 = 0.019292439232164... < 1/2`,                        (6.1)

and therefore

`boxed: ||p_Q||_infinity
 <= 512/(127-sqrt(129))
 = 4.427450134131218... < 4.428.`                                (6.2)

This is dimension-free and law-uniform under the full cap-one product hypothesis.

The arithmetic is reproduced in `CHECK.py`; the recorded output is `CHECK_OUTPUT.txt` in this run directory.

## 7. What this changes in the proof map

Account01/B09's global exact-cut-rank-one compiler left, after excluding the triangle case, two possible obstructions in the star or clique-factor geometry:

1. exact alignment of the mixed hub/curvature frame;
2. concentration of its transverse wedge on a high-leverage physical row.

For the **global star branch**, Sections 3--6 remove both possibilities directly from strict N3. Therefore:

### Theorem `QFORM-STRICTN3-GLOBAL-STAR-CLOSED-v1`

Under (2.1)--(2.3) with `tau=1/128`, if for some physical hub `h` the off-diagonal graph on its entire physical complement is a star, then `Q=X^TAX` has a continuous density satisfying

`||p_Q||_infinity < 4.428`                                      (7.1)

for every independent cap-one input law.

Equivalently every interval obeys

`P{Q in L}<4.428 |L|`.                                          (7.2)

This is a genuine target-level exit for one complete structural chamber; no extra assumption on the input laws is present.

Together with the already-recorded triangle exclusion in the same global cut-rank-one compiler, the remaining exact global cut-rank-one N3 geometry is now reduced to the **clique-factor branch**. The same perturbation proof cannot simply be copied there: writing the physical clique block as `D+lambda vv^T` may involve large diagonal entries in `D` cancelling the rank-one diagonal, even though the actual physical diagonal entries of `A` are small. Treating that algebraic `D` as a small matrix perturbation would be invalid.

The next B09 implication is therefore:

`QFORM-STRICTN3-GLOBAL-CLIQUE-ALIGNED-OR-HEAVYROW-v1`:

> preserve the clique-factor product geometry and either pay the aligned/high-leverage mixed frame directly, or route it quantitatively to an already-paid physical-pair, ridge, volume, or multi-hub exit, without declaring the cancelling diagonal twist small.

## 8. Partner and review status

The designated partner `account04/B09` still had no completed current-QFORM canonical handoff or math archive at the fresh checks in this run, so no result was fabricated or attributed to that slot. Work continued asynchronously as instructed.

A completed compatible B09 theorem from `account01/B09` was applied at the actual inequality (5.3), with its full source/commit/path stated in Section 1. This report has **not** received the two independent end-to-end reviews required of a full candidate. It is a supporting target-level branch theorem only.

Full QFORM status: **OPEN**.  
Full-target continuity: **OPEN**.  
This branch: **bounded continuous density proved**.  
Native-brain status: **WITHOUT_VERIFIED_BRAIN**.
