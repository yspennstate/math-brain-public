SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T06:25:49Z.
attacking: a product-preserving grouped-coordinate reduction for indefinite rank three: three disjoint original-coordinate banks, with an aligned-Schur corollary that isolates the genuinely hard same-bank transverse overlap.

# account01/B11 — three disjoint product banks and the aligned-Schur compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T062549Z-account01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** only essential boundedness is proved here.

## 1. Source boundary and dependencies

The full owner target remains open: arbitrary independent real coordinates with density caps one, arbitrary symmetric ambient matrix with at least three eigenvalues of modulus at least one, with no moment, support, Gaussian, log-concavity, connected-support, or post-rotation-independence assumptions.

This run uses three completed inputs at their exact scopes.

1. The preceding account01/B11 scalar-Schur theorem, `QFORM-CROSSCOUPLED-SCALAR-SCHUR-HALF-RIESZ-v1`, source
   `yspennstate/math-open-problems@1d7b9757303be54c58e44e18e6c962c4f1f9b293`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T051701Z-account01-B11-QFORM-auto11/REPORT.md`.
   For three independent cap-one variables and a nonzero scalar physical pivot `d`, it gives
   
   `||p_Q||_inf <= 16 sqrt(30) (|d| |det H|)^(-1/4)`.

2. The completed physical-pair logarithmic theorem, source
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   For an exact-rank-three original-coordinate block whose eigenvalue magnitudes are at least `s`, and an invertible indefinite physical pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`, it gives
   
   `||p_Q||_inf <= 8 sqrt(5) (D*kappa*s)^(-1/4)`.

3. The designated partner account02/B11 theorem `QFORM-INDEFINITE-PAIR-DIFFUSE-SQUARE-v1`, source
   `yspennstate/math-open-problems@f2835c54b9f384f8f83e34c46bef5c40953e32a7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T042112Z-account02-B11-QFORM-2f47d35a/REPORT.md`.
   If `U=(X1,X2)` are independent cap-one, `B` is invertible symmetric, `W` is independent with density cap `L`, and `d!=0`, then
   
   `||p_(U^T B U + affine(U) + dW^2+2rW+q)||_inf
      <= 16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2)`.

The standard sharp product-marginal theorem used by the partner report is also used below: every normalized linear form of independent cap-one coordinates has density at most `sqrt(2)`.

No arbitrary-joint coarea estimate, positive conditional-projection moment, pointwise law-uniform quadratic-phase decay, or post-rotation independence is used.

## 2. A complete three-independent-variable compiler

### Lemma 2.1 — `QFORM-3PHYS-INDEFINITE-COMPILER-v1`

Let `Y1,Y2,Y3` be independent real variables with probability densities bounded by one. Let `H` be a real symmetric `3x3` matrix with

`min_j |lambda_j(H)| >= s > 0`.

For arbitrary affine terms `ell^T Y+q`, the law of

`F=Y^T H Y+ell^T Y+q`

has an essentially bounded density and

`boxed:
 ||p_F||_inf <= C3/s,
 C3 = 16 sqrt(30) 2^(1/4) < 104.217.`                         (2.1)

This holds for both indefinite signatures `(2,1)` and `(1,2)` (and in fact also for definite `H`).

### Proof

There are two exhaustive cases.

**Case A: a scalar physical pivot is visible.** Suppose `|h_ii|>=s/2` for some `i`. Apply the scalar-Schur theorem with `d=h_ii`. Since

`|det H| = product_j |lambda_j(H)| >= s^3`,                         (2.2)

we obtain

`||p_F||_inf
 <=16 sqrt(30)(|h_ii||det H|)^(-1/4)
 <=16 sqrt(30) 2^(1/4) s^(-1).`                                  (2.3)

**Case B: all three scalar pivots are small.** Suppose `|h_ii|<s/2` for every `i`. Since

`||H||_F^2 = sum_j lambda_j(H)^2 >=3s^2`,                         (2.4)

we have

`2 sum_(i<j) h_ij^2
 = ||H||_F^2-sum_i h_ii^2
 > 3s^2-3s^2/4 = 9s^2/4`.                                       (2.5)

Hence some pair, relabelled `(1,2)`, satisfies

`|h_12| > sqrt(3/8) s`.                                           (2.6)

For its physical block

`B=[[h_11,h_12],[h_12,h_22]]`,                                   (2.7)

we get

`det B = h_11 h_22-h_12^2 < s^2/4-3s^2/8 = -s^2/8`,              (2.8)

so the pair is indefinite and

`D=|det B| > s^2/8`.                                              (2.9)

Compare `B` with `B0=[[0,h_12],[h_12,0]]`. Since

`||B-B0||_op = max(|h_11|,|h_22|)<s/2`,                           (2.10)

singular-value perturbation gives

`kappa=sigma_min(B)
 >= |h_12|-s/2
 > (sqrt(3/8)-1/2)s`.                                             (2.11)

The physical-pair logarithmic theorem therefore gives

`||p_F||_inf
 <=8sqrt(5)[(1/8)(sqrt(3/8)-1/2)]^(-1/4)s^(-1)
 <51.962 s^(-1),`                                                 (2.12)

which is smaller than the Case-A constant in (2.1). This proves the lemma. QED.

The point of Case B is sign-specific: when all physical squares are near-null, spectral nondegeneracy forces a quantitatively indefinite original-coordinate pair, and its true logarithmic singularity is paid by the third rank-one remainder rather than falsely discarded.

## 3. Main theorem: arbitrary indefinite coupling of three disjoint product banks

### Theorem 3.1 — `QFORM-THREE-DISJOINT-BANKS-INDEFINITE-v1`

Let `X_1,...,X_n` be independent, each with density at most one. Let `S1,S2,S3` be pairwise disjoint coordinate sets and let `u_k` be a unit vector supported on `S_k`. Put

`U=[u_1,u_2,u_3]`,                                                (3.1)

so `U^T U=I_3` automatically. Let `H` be any real symmetric `3x3` matrix with

`min_j |lambda_j(H)| >= s>0`,                                    (3.2)

and define the exact-rank-three ambient form

`A=U H U^T`.                                                      (3.3)

Then, for **arbitrary** cap-one product input laws,

`boxed:
 ||p_(X^T A X)||_inf
 <= 2 C3/s
 <208.434/s.`                                                     (3.4)

In particular this holds uniformly for genuinely rotated signatures `(2,1)` and `(1,2)` and allows all six entries of `H`, including arbitrary cross-couplings between the three banks.

### Proof

Set

`Y_k=u_k^T X`.                                                    (3.5)

Because the supports `S1,S2,S3` are disjoint, the three variables `Y_1,Y_2,Y_3` are genuinely independent. No spectral rotation is being used to create independence.

By the sharp one-dimensional product-marginal theorem,

`||p_(Y_k)||_inf <=sqrt(2)` for each `k`.                         (3.6)

Define `Z_k=sqrt(2)Y_k`. Then the `Z_k` remain independent and satisfy density caps one. Moreover

`X^TAX = Y^T H Y = Z^T (H/2) Z`.                                 (3.7)

The eigenvalue magnitudes of `H/2` are at least `s/2`. Applying Lemma 2.1 at scale `s/2` gives

`||p_(X^TAX)||_inf <= C3/(s/2)=2C3/s`,                            (3.8)

which is (3.4). QED.

This is the product-preserving aggregation that local-minor strategies miss: an entire diffuse bank is collapsed to its normalized linear statistic **before** any reciprocal pivot or determinant is paid.

## 4. Exact aligned-Schur corollary

The three-bank theorem closes a concrete part of the B11 overlap problem that is not visible from a single physical third coordinate.

Partition the coordinates as `I={i,j}` and `J=I^c`, and write an exact-rank-three symmetric matrix as

`A=[[B,C],[C^T,D]]`,                                              (4.1)

with `B=A_II` invertible. Since `rank A=3` and `rank B=2`, its Schur complement

`S=D-C^T B^(-1) C`                                                (4.2)

has rank exactly one. Write

`S=sigma v v^T`, `||v||=1`, `sigma!=0`.                           (4.3)

Assume the cross block is aligned with that same residual direction:

`boxed: C=c v^T for some c in R^2.`                               (4.4)

Then

`D=(c^T B^(-1)c+sigma)vv^T`,                                     (4.5)

and with the orthonormal, disjoint-support frame

`T=[e_i,e_j,v]`,                                                  (4.6)

we have the exact factorization

`A=T H T^T`,                                                      (4.7)

where

`H=[[B,c],[c^T,c^T B^(-1)c+sigma]].`                             (4.8)

Thus the nonzero eigenvalues of `A` are exactly the eigenvalues of `H`, and all dependence on the whole residual bank `J` occurs through the single normalized statistic

`W=v^T X_J`,                                                      (4.9)

which is independent of `X_i,X_j` and has density cap at most `sqrt(2)`.

Consequently, if the three nonzero eigenvalue magnitudes of `A` are at least `s`, then

`boxed: ||p_(X^TAX)||_inf <208.434/s.`                            (4.10)

This pays arbitrary quadratic cross-coupling `c` between the two physical coordinates and a diffuse third bank, including cases where every individual coefficient of `v` is tiny.

The exact residual obstruction is now exposed. Define

`C_perp = C(I-vv^T)`.                                             (4.11)

The present theorem pays the full chamber `C_perp=0`. The genuinely unresolved same-bank overlap starts at `C_perp!=0`: then the pair shift depends on residual linear statistics transverse to the Schur-square statistic `v^T X_J`, so conditioning those transverse statistics can destroy the scalar density cap. This is precisely where the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` matters.

## 5. Designated partner applied to an actual three-diffuse-bank inequality

The partner theorem is not merely cited. Apply it to the most transparent indefinite three-bank control.

Let `u_1,u_2,u_3` be arbitrary unit vectors on three disjoint coordinate banks and put `Y_k=u_k^T X`. Consider

`Q=2Y_1Y_2+Y_3^2`.                                                (5.1)

Its reduced matrix is

`H0=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (5.2)

with exact spectrum `{1,-1,1}`. Set `Z_k=sqrt(2)Y_k`; each `Z_k` has density cap one and the three are independent. Then

`Q=Z_1Z_2+(1/2)Z_3^2`.                                           (5.3)

In the partner notation take

`B=[[0,1/2],[1/2,0]]`, `det B=-1/4`, `W=Z_3`, `L=1`, `d=1/2`.    (5.4)

The completed account02/B11 theorem therefore gives the explicit actual inequality

`boxed:
 ||p_Q||_inf
 <=16sqrt(30)(1/4)^(-1/4)(1/2)^(-1/2)
 =32sqrt(30)
 <175.272.`                                                       (5.5)

This is uniform in all three bank sizes and all admissible fragmented cap-one input laws.

The required rank-two logarithmic obstruction is retained exactly. If the first two banks are singletons with centered unit uniforms, then

`p_(2X_1X_2)(t)=log(1/(2|t|)),  0<|t|<1/2`.                      (5.6)

Thus the two-bank opposite-sign saddle is genuinely unbounded. The third independent bank removes it only after aggregation: its square contributes the half-order kernel consumed by the partner half-Riesz estimate. Equation (5.5) is a target-valid, genuinely banked realization of that mechanism.

## 6. What this advances, and what remains unpaid

The theorem strictly extends the earlier `physical pair + one diffuse square bank` picture in one structural direction: **all three spectral coordinates may now be diffuse original-coordinate banks**, and the reduced indefinite `3x3` matrix may have arbitrary cross-couplings. The cost is only that the three one-dimensional sufficient statistics must live on disjoint original-coordinate banks.

The first B11 unpaid implication is therefore sharpened to

**`QFORM-NONDISJOINT-GROUPED-COORDINATE-COMPILER-v1`.** Starting from an arbitrary exact-rank-three Parseval frame (and ultimately an arbitrary higher-rank target), either extract three disjoint original-coordinate banks whose normalized sufficient statistics carry a uniformly nondegenerate `3x3` reduced form, or force one of the already-paid physical-pivot / indefinite-pair / ridge / volume exits. In the exact-pair Schur language, the local hard term is `C_perp!=0`: transverse statistics from the **same** residual bank are correlated with the Schur-square statistic and cannot be conditioned away using only a marginal density cap.

This is a supporting theorem, not an exhaustive structural reduction. Arbitrary extra nonseparable spectrum is also still outside this theorem. The full conjecture and the full continuity conclusion remain open.
