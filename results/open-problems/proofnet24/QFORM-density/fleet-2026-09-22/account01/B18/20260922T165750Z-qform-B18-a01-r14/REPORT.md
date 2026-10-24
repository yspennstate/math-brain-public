# account01/B18 — zero-outer-pivot fractional transfer and exact transverse rank-one geometry

**Run:** `20260922T165750Z-qform-B18-a01-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control:** proof-first continuation `QFORM-PROOF-FIRST-20260922T161801Z`; visible state revision `2026-09-22.8`  
**Assignment:** literature-to-proof transfer  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner target remains **OPEN / NOT PROVED**: for arbitrary independent real coordinates with probability densities bounded by one and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`. Continuity is separate.

This run attacks the currently explicit zero/near-isotropic **outer physical pivot** debt. It proves that an *exact* zero outer pivot already has a dimension-free half-Riesz certificate even with an arbitrary measurable residual, and identifies the exact rank-one transverse quadratic geometry left after quotienting the cross direction in rank exactly three. This is not yet an `L^infinity` density theorem: one further independent/product-valid half-order of smoothing is still required.

## 1. Exact dependencies and corrections

### Primary literature actually transferred

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a product density `f=prod f_i` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. I use only the sharp `k=1` consequence

`||p_<theta,X>||_infinity <= sqrt(2)` for every unit vector `theta`.

This is applied to a normalized linear form in the **original independent coordinates**, not by rotating the inputs and retaining independence.

### Designated partner actually applied

Latest completed compatible `account02/B18` result at source refresh:

`yspennstate/math-open-problems@f985e95ceec640cdc37cffc34fab07bb2687a414`,

report root `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/`, theorem `QFORM-LPP-FULL-THREE-BANK-v1`.

If three independent disjoint physical-bank aggregates `Y_1,Y_2,Y_3` have density caps `K_r`, and an exact factorization has three-bank quadratic matrix `B`, then with `D_K=diag(K_1,K_2,K_3)`,

`||p_Q||_infinity <= (2*pi+3*sqrt(3)) / sigma_min(D_K^(-1) B D_K^(-1))`,

and the output density is continuous. Section 6 below applies this to an actual zero-pivot bank inequality.

### Live proof state/corrections preserved

The proof-first synthesis has already removed the orientation split *inside* a rank-two Schur residual but explicitly leaves the small/zero **outer** scalar pivot unpaid. I do not use pointwise law-uniform Fresnel decay, post-rotation independence, an unrestricted fiber supremum, conditional-density-as-independence, bounded-diameter localization, a fixed fragment count, a fixed good local minor, or the refuted generic X-ray/two-sheet shortcut.

## 2. A sharp cap-to-negative-moment lemma

### Lemma 2.1

If a real random variable `Z` has probability density `p_Z` satisfying `||p_Z||_infinity<=M`, then for `0<alpha<1`,

`E |Z|^(-alpha) <= 2^alpha M^alpha/(1-alpha)`.                 (2.1)

In particular,

`E |Z|^(-1/2) <= 2 sqrt(2M)`.                                 (2.2)

#### Proof

Among probability densities bounded by `M`, the integral against the symmetric decreasing kernel `|z|^(-alpha)` is maximized by filling the centered interval of length `1/M`. Hence

`E|Z|^(-alpha)`
` <= M int_{-1/(2M)}^{1/(2M)} |z|^(-alpha) dz`
` =2^alpha M^alpha/(1-alpha)`.

No moment or support assumption is used. QED.

## 3. Zero linear pivot with arbitrary remainder

### Theorem 3.1 — `QFORM-ZERO-LINEAR-PIVOT-HALFRIESZ-v1`

Let `X_0` be independent of `Y=(X_1,...,X_m)`, all coordinates having probability densities bounded by one. Let `b in R^m`, `b!=0`, and let `T(Y)` be **any measurable real-valued function**. Define

`R = 2 X_0 <b,Y> + T(Y)`.                                           (3.1)

Then

`boxed( sup_t E |R-t|^(-1/2) <= 2^(11/4) ||b||_2^(-1/2). )`          (3.2)

The residual `T` may contain arbitrary quadratic terms, arbitrary signs, arbitrary additional spectrum, and arbitrary dependence on the coordinates of `Y`.

#### Proof

Fix `Y=y` and put `ell=<b,y>`. Except on a null set, `ell!=0`, because `<b,Y>/||b||` has a density by the one-dimensional product-marginal theorem. For any shift `s`, the law of `2 ell X_0+s` has density cap `1/(2|ell|)`. Lemma 2.1 therefore gives

`E[ |2 ell X_0+s|^(-1/2) | Y=y] <= 2 |ell|^(-1/2)`.                 (3.3)

The shift here is `s=T(y)-t`, so it is completely harmless. Average (3.3):

`E|R-t|^(-1/2) <=2 E|<b,Y>|^(-1/2)`.                                (3.4)

Set `Z=<b,Y>/||b||`. Livshyts--Paouris--Pivovarov gives

`||p_Z||_infinity<=sqrt(2)`.                                        (3.5)

Apply (2.2) with `M=sqrt(2)`:

`E|Z|^(-1/2) <=2 sqrt(2 sqrt(2))=2^(7/4)`.                           (3.6)

Equations (3.4)--(3.6) give (3.2). QED.

### What is new about the scope

The half-Riesz payment is uniform in the **entire residual** `T(Y)`. Thus an exact zero physical diagonal is not itself an obstruction to obtaining a universal fractional-trace estimate. The remaining difficulty is upgrading this half-order to a full density bound without fabricating an independent square or a conditional density cap.

## 4. Exact-rank-three zero-pivot corollary

Let

`A=U Lambda U^T`, `U^T U=I_3`,

be exact rank three, with `Lambda` symmetric invertible. Fix a physical coordinate `i`; write its spectral row as `u_i`, and set

`c_i=||u_i||^2`, `a_i=A_ii=u_i^T Lambda u_i`.

Assume the exact outer pivot is isotropic:

`a_i=0`.                                                            (4.1)

Let `J=[n]\{i}` and `b=A[J,i]`. Then

`||b||^2`
` = u_i^T Lambda (I-u_i u_i^T) Lambda u_i`
` = ||Lambda u_i||^2-(u_i^T Lambda u_i)^2`
` = ||Lambda u_i||^2`.                                              (4.2)

If

`lambda_*:=sigma_min(Lambda)=min_j |lambda_j(Lambda)|`,

then

`||b||^2 >= lambda_*^2 c_i`.                                        (4.3)

Writing the full quadratic as

`Q=2 X_i <b,X_J> + X_J^T A_JJ X_J`,                                 (4.4)

Theorem 3.1 gives

`boxed( sup_t E|Q-t|^(-1/2)
 <= 2^(11/4) lambda_*^(-1/2) c_i^(-1/4). )`                          (4.5)

For the exact-rank-three owner target, `lambda_*>=1`. In the high-leverage branch `c_i>=1/32`, the powers cancel exactly:

`boxed( sup_t E|Q-t|^(-1/2) <=16. )`                                 (4.6)

This is a universal, translation-free certificate precisely at the outer pivot value for which scalar square completion is singular.

It is **not** a bounded-density conclusion: (4.6) alone implies only a square-root-scale concentration estimate. The live conditional-cap correction forbids treating it as an extra independent half-order.

## 5. Exact transverse rank-one geometry after a zero pivot

The same branch has a simple algebraic structure which isolates the missing half-order.

### Theorem 5.1 — `QFORM-ZEROPIVOT-TRANSVERSE-RANKONE-v1`

Let a real symmetric matrix of rank exactly three be written in physical block form

`A = [[0,b^T],[b,C]]`, `b!=0`.                                      (5.1)

Put `beta=||b||`, `e=b/beta`, and let `P=I-ee^T` on the remaining physical coordinates. Then the compression of `C` to `e^perp` has rank exactly one:

`boxed( rank( P C P |_(e^perp) ) =1. )`                              (5.2)

#### Proof

Choose an orthonormal basis in the tail beginning with `e`. In the resulting physical basis,

`A = [[0,beta,0],
      [beta,c,d^T],
      [0,d,D]]`,                                                     (5.3)

where `D` is precisely the compression in (5.2). The leading block

`B=[[0,beta],[beta,c]]`

is invertible and

`B^(-1)=[[-c/beta^2,1/beta],[1/beta,0]]`.                            (5.4)

The coupling from the leading two coordinates to the remaining block is `[0;d]`. Therefore its Schur correction is

`[0,d^T] B^(-1) [0;d] =0`                                          (5.5)

because `(B^(-1))_22=0`. Hence the Schur complement is exactly `D`, and

`rank(A)=rank(B)+rank(D)=2+rank(D)`.                                 (5.6)

Since `rank(A)=3`, `rank(D)=1`. QED.

Thus the zero-pivot rank-three form is not an arbitrary hard residual: after the physical cross direction is removed, exactly one quadratic curvature direction survives. The unpaid step is to exploit that direction while preserving the original product provenance.

### Spectral canonical form and quantitative curvature

Normalize the isotropic spectral direction `e_1=u_i/sqrt(c_i)` and rotate only **inside spectral notation** so `e_2` is parallel to `Lambda e_1`. Then

`Lambda = [[0,beta,0],[beta,gamma,delta],[0,delta,kappa]]`.            (5.7)

If `lambda_*=sigma_min(Lambda)`, then

`|beta|=||Lambda e_1||>=lambda_*`.                                   (5.8)

Also `det Lambda=-beta^2 kappa`, and direct inversion gives

`(Lambda^(-1))_33=1/kappa`.                                         (5.9)

Since `||Lambda^(-1)||_op<=lambda_*^(-1)`, one has

`|kappa|>=lambda_*`.                                                  (5.10)

Algebraically, determinant-one shears put the active polynomial into

`2 beta y_1' y_2 + kappa (y_3')^2`.                                  (5.11)

Equation (5.11) is **not** permission to regard the sheared spectral linear forms as independent; it is only the exact canonical geometry. The product-preserving upgrade is still owed.

## 6. Actual application of the designated account02/B18 theorem

The preceding canonical geometry does become fully paid whenever it occurs as an **exact product-valid three-bank factorization** rather than merely as a spectral shear.

Assume three scalar aggregates `Y_1,Y_2,Y_3` are built from pairwise disjoint physical coordinate banks, are normalized linear forms, and the full quadratic has the exact partner form

`Q=Y^T B Y+2Y^T L X_K+X_K^T D X_K`,                                 (6.1)

where `B` is symmetric invertible and

`sigma_min(B)>=lambda_*>0`.                                          (6.2)

This includes a zero-pivot canonical matrix such as

`B=[[0,beta,0],[beta,gamma,delta],[0,delta,kappa]]`                    (6.3)

when it is genuinely realized by disjoint banks. By the primary marginal theorem, each normalized bank has density cap at most `sqrt(2)`. Thus `D_K<=sqrt(2) I`, and

`sigma_min(D_K^(-1) B D_K^(-1))`
` >= sigma_min(B)/||D_K||^2`
` >= lambda_*/2`.                                                     (6.4)

Apply `account02/B18` `QFORM-LPP-FULL-THREE-BANK-v1`:

`boxed( ||p_Q||_infinity
 <= 2(2*pi+3*sqrt(3))/lambda_*
 = (4*pi+6*sqrt(3))/lambda_* <23/lambda_* . )`                        (6.5)

The partner theorem also gives continuity in this exact bank branch. For the owner normalization `lambda_*>=1`, (6.5) is a universal `<23` density cap.

This is an actual inequality application, but the hypothesis that the canonical variables are disjoint-bank aggregates is **not automatic** for a general rotated rank-three form. Promoting (6.5) without a product-preserving extraction would repeat a known invalid rotation/conditioning step.

## 7. Conditional proof ledger and first unpaid inference

The smallest current exact-rank-three route is now:

1. Diffuse spectral-window/ridge branches are already paid by the existing regularized-determinant and ridge-window theorems.
2. A quantitatively nonzero outer physical pivot is paid by the universal rank-two affine half-Riesz Schur theorem.
3. At an **exact zero outer pivot**, Theorem 3.1 + (4.2) gives a universal half-Riesz certificate; in the high-leverage target branch the constant is at most `16`.
4. Theorem 5.1 shows the transverse residual there is exactly rank one.
5. If that rank-one transverse resource can be exposed as an exact disjoint-bank payment, account02/B18 closes it with (6.5).

The first unpaid implication is therefore sharply localized:

`QFORM-ZEROPIVOT-HALFRIESZ-TO-DENSITY-v1` — In the high-leverage exact-rank-three branch with `A_ii=0`, combine the proved half-Riesz estimate (4.6) with the rank-one transverse curvature (5.2), **without** post-rotation independence or a fabricated conditional cap, to gain the missing half-order and obtain an `L^infinity` density bound. Equivalently, produce a source-valid grouped-coordinate/fractional-trace extraction of the transverse rank-one direction, or a target-valid counterexample to such an extraction.

This remains distinct from the arbitrary-extra-spectrum debt. Even a full exact-rank-three closure would still require a proof that additional nonseparable spectral directions cannot destroy the bound, unless one applies an existing full-spectrum supporting branch with its exact hypotheses.

## 8. Status

- `QFORM-ZERO-LINEAR-PIVOT-HALFRIESZ-v1`: **PROVED**.
- Exact-rank-three high-leverage zero-pivot half-Riesz bound `<=16`: **PROVED**.
- `QFORM-ZEROPIVOT-TRANSVERSE-RANKONE-v1`: **PROVED**.
- Product-valid zero-pivot three-bank density bound `<23/lambda_*`: **PROVED** by direct application of the designated `account02/B18` theorem plus LPP.
- Full exact-rank-three zero-pivot density branch: **OPEN**.
- Full owner target with arbitrary additional spectrum: **OPEN / NOT PROVED**.
- Continuity: **PROVED only in the exact partner three-bank branch above; otherwise not claimed here**.
