# account01/B05 — two-coordinate hyperbolic coarea and the distributed wedge-mass obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T155803Z-account01-B05-qform13`  
**Assignment:** quadratic coarea bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval occurred, but no native learned-memory ingestion was observed.

## 1. Exact target and conditional end-to-end route

The full conjecture remains open. The target is: for every dimension, every independent real input vector with coordinate densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `Q=X^T A X`, or give a valid counterexample. No moment, compact-support, log-concavity, sign, connected-support, diagonal-basis, or post-rotation-independence assumption is used below. Continuity is tracked separately and is **not** proved by the new coarea statements in this report.

The previous B05 result proved a universal determinant-scale half-Riesz estimate for every exact rank-two product quadratic form, closing the localized rank-two residual after a nonzero scalar pivot. The present run deliberately changes mechanism: instead of a one-coordinate square pivot, it uses a **two-coordinate hyperbolic pivot**. This attacks the zero/near-isotropic diagonal geometry where scalar Schur completion is unavailable or expensive.

A compact conditional route is now:

1. a nonzero well-sized physical scalar pivot is handled by the existing scalar-Schur coarea inequality plus the universal rank-two half-Riesz theorem in rank exactly three;
2. an exact zero-diagonal physical pair with nonzero cross coefficient admits the new hyperbolic coarea inequality below;
3. if its Schur residual has a suitable product-coordinate cross certificate, the completed account02/B05 fractional-Riesz theorem closes the density bound even with arbitrary additional spectrum;
4. in exact rank three, the zero-diagonal pair has a rank-one residual and an exact determinant/wedge identity, giving a direct bound `36 (|det Lambda| delta_ij)^(-1/3)`;
5. the first unpaid geometric factor is now explicit: a heavy isotropic row carries total wedge mass `sum_j delta_ij=2 ell_i`, but that mass can be distributed over arbitrarily many physical rows. A universal proof must aggregate this mass before paying a reciprocal `delta_ij^(-1/3)` cost, or convert it to another existing ridge/cross-bank certificate.

## 2. Dependencies actually consumed

### Assigned partner account02/B05

Canonical report:

`yspennstate/math-open-problems@d88444f6ee8744b72a46448734db26349baabdd7`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T142748Z-b05-qform-f7a2e3e0/REPORT.md`.

The completed theorem used below is: if `R=Y^T S Y` in independent original coordinates and a physical cross block of `S` has two positive singular values `sigma_1,sigma_2` with range leverage at most `1/2`, then

`sup_t E |t-R|^(-1/2) <= C_1 (sigma_1 sigma_2)^(-1/4)`,

where `C_1=7.270461147134126...`. The source allows arbitrary residual self blocks, outside couplings, signs, and extra spectrum.

### Regularized determinant theorem

Canonical source:

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

path

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For a residual quadratic form and a physical cross block `C`, at `q=1` and range leverage at most `1/2`,

`|phi_R(s)| <= det(I+2s^2 CC^T/(pi^2 e^2))^(-1/4)`.

This retains arbitrary self blocks and extra spectrum. I use it only to derive a one-cross **third-Riesz** bound; no law-uniform pointwise scalar van-der-Corput estimate is used.

### One-dimensional product marginal theorem

For independent coordinates of density cap one, every unit one-dimensional linear projection has density cap at most `sqrt(2)`. This is the `k=1` case of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949. It is applied only to an original-coordinate linear form, not by declaring rotated coordinates independent.

## 3. Product kernel for a hyperbolic pivot

### Lemma 3.1 — fractional density of a product

Let `U,V` be independent real random variables with probability densities bounded by one and put `W=UV`. For `w!=0`,

`p_W(w)=int f(u) g(w/u) du/|u|`.

If `|w|<=1`, split the integral into `|u|<|w|`, `|w|<=|u|<=1`, and `|u|>1`. In the first region substitute `v=w/u`; it is at most `int_{|v|>1}g(v)dv<=1`. The middle region is at most `2 log(1/|w|)`, and the last is at most `1`. Hence

`p_W(w) <= 2+2 log(1/|w|)` for `0<|w|<=1`.                 (3.1)

If `|w|>=1`, split at `|u|=sqrt(|w|)`. The large-`u` part is at most `|w|^(-1/2) int f`, and after the same substitution the small-`u` part is at most `|w|^(-1/2) int g`. Thus

`p_W(w) <= 2 |w|^(-1/2)` for `|w|>=1`.                    (3.2)

For every `0<alpha<=1/2`, (3.1)--(3.2) imply the uniform power majorant

`p_W(w) <= (2/alpha)|w|^(-alpha)`.                         (3.3)

Indeed, for `|w|=e^{-L}<=1`, `1+L <= alpha^(-1)e^(alpha L)`, while for `|w|>=1`, `|w|^(-1/2)<=|w|^(-alpha)`.

Therefore the density of `T=2bUV`, `b!=0`, obeys

`p_T(s) <= (2^alpha/alpha)|b|^(alpha-1)|s|^(-alpha)`.     (3.4)

At `alpha=1/3`,

`p_T(s) <= K_0 |b|^(-2/3)|s|^(-1/3)`,
`K_0=3*2^(1/3)=3.779763149684619...`.                     (3.5)

The logarithmic singularity of a pure indefinite rank-two product is visible in (3.1); the fractional majorant is deliberately weaker but can be smoothed by the remaining curvature.

## 4. Two-coordinate hyperbolic coarea theorem

### Theorem 4.1 — `QFORM-ZEROPAIR-THIRD-RIESZ-COAREA-v1`

Let `Q=X^T A X`, with independent original coordinates of density cap one. Suppose two physical coordinates `i,j` satisfy

`A_ii=A_jj=0`, `b=A_ij!=0`.

Let `K` denote the other coordinates. Write the cross rows to `K` as `r^T,s^T`, so the relevant block decomposition is

`A = [[0,b,r^T],[b,0,s^T],[r,s,D]]`.

Define the exact two-coordinate Schur residual

`S = D - C^T B_0^(-1) C`,

where `B_0=[[0,b],[b,0]]` and `C=[r^T;s^T]`, and put `R(Z)=Z^T S Z`.

Completing the two original coordinates gives the identity

`Q = 2b U_Z V_Z + R(Z)`,                                  (4.1)

with

`U_Z=X_i+(s^T Z)/b`, `V_Z=X_j+(r^T Z)/b`.                (4.2)

Conditioned on `Z`, `U_Z,V_Z` remain independent translations of the original independent coordinates, with density caps one. Hence for every `0<alpha<=1/2`, Lemma 3.1 gives an actual mixture density satisfying

`p_Q(t) <= (2^alpha/alpha)|b|^(alpha-1)
           E |t-R|^(-alpha)`.                             (4.3)

In particular,

`p_Q(t) <= K_0 |b|^(-2/3) E|t-R|^(-1/3)`.                (4.4)

This is an original-coordinate coarea inequality. It does not rotate the product source and does not take an unrestricted fiber supremum.

## 5. Direct application of the assigned partner result

Assume in addition that the post-pair Schur residual `S` has an original-coordinate cross block with two positive singular values `sigma_1,sigma_2` and range leverage at most `1/2`. The assigned account02/B05 theorem gives

`M_(1/2):=sup_t E|t-R|^(-1/2)
 <= C_1 (sigma_1 sigma_2)^(-1/4)`.                         (5.1)

By Lyapunov/Jensen,

`E|t-R|^(-1/3)
 <= (E|t-R|^(-1/2))^(2/3)`,                               (5.2)

so (4.4) becomes

`||p_Q||_infinity
 <= K_0 C_1^(2/3) |b|^(-2/3)(sigma_1 sigma_2)^(-1/6)`
` = 14.18532287264322...
    (|b|^4 sigma_1 sigma_2)^(-1/6)`.                       (5.3)

Thus `|b|^4 sigma_1 sigma_2>=1` implies `||p_Q||_infinity<14.186`. This is a genuine application of the completed assigned-partner theorem to a new inequality. It permits arbitrary extra residual spectrum and arbitrary residual self blocks/couplings within the partner theorem's stated cross-certificate scope.

## 6. One cross direction suffices for the third-Riesz potential

The two-coordinate pivot consumes only a `1/3`-order Riesz singularity, so its residual requires less smoothing than the scalar-square pivot.

### Theorem 6.1 — `QFORM-CROSS1-THIRD-RIESZ-v1`

Let `R=Y^T S Y` in independent original coordinates of density cap one. Suppose a physical cross block `C=S[I,J]` has at least one positive singular value `sigma`, and its range projection on the controlled side has maximum diagonal at most `1/2`. Then

`sup_t E|t-R|^(-1/3) <= C_(1/3) sigma^(-1/3)`,             (6.1)

where

`C_(1/3)
 = [1/(sqrt(3) Gamma(1/3))]
   [2/(pi^2 e^2)]^(-1/6)
   B(1/6,1/12)
 = 6.928662978258370...`.                                  (6.2)

**Proof.** The regularized-determinant theorem at `q=1`, discarding every singular factor except one, gives

`|phi_R(s)| <= (1+c s^2 sigma^2)^(-1/4)`,
`c=2/(pi^2 e^2)`.                                         (6.3)

For `alpha=1/3`, the Riesz Fourier identity in the convention `hat f(s)=int e^(isx)f(x)dx` is

`|x|^(-1/3)
 = [1/(sqrt(3) Gamma(1/3))]
   int_R e^(-isx)|s|^(-2/3) ds`,                           (6.4)

under the usual positive regularization/Fatou limiting argument. The weighted integral is finite by (6.3). After `u=s sqrt(c) sigma`,

`int_R |u|^(-2/3)(1+u^2)^(-1/4)du
 = B(1/6,1/12)`.                                           (6.5)

Equations (6.3)--(6.5) prove (6.1). QED.

Combining Theorems 4.1 and 6.1 yields

`||p_Q||_infinity
 <= 26.1887050018051...
    (|b|^2 sigma)^(-1/3)`.                                 (6.6)

Thus the pair pivot lowers the residual cross-direction requirement: **one** diffuse residual cross singular direction is enough for a bounded density at this interface.

## 7. Exact rank-three zero-pair determinant identity

Now assume `rank(A)=3` and write the active spectral representation

`A=U Lambda U^T`, `U^T U=I_3`,

with `Lambda` invertible. Let `u_i,u_j in R^3` be the two physical spectral rows and define their squared area

`delta_ij
 = det [[||u_i||^2,<u_i,u_j>],[<u_i,u_j>,||u_j||^2]]
 = ||u_i wedge u_j||^2`.                                  (7.1)

Assume again `A_ii=A_jj=0` and `b=A_ij!=0`. Then the pair Schur residual in Theorem 4.1 has rank one. Let `nu` be its nonzero eigenvalue. The exact identity is

`b^2 |nu| = |det Lambda| delta_ij`.                        (7.2)

**Proof.** Put `W=[u_i,u_j]`. Since `b!=0`, its two columns are independent and the physical pivot block is

`B_0=W^T Lambda W=[[0,b],[b,0]]`,
`det B_0=-b^2`.                                            (7.3)

Choose an orthonormal two-frame `V` spanning `W` and write `W=V R`; then `det(R)^2=delta_ij`. In the orthogonal basis `[V,n]`, with `n` normal to `span(W)`, write

`Lambda_tilde=[[M,g],[g^T,d]]`.

The spectral Schur complement against `W` is rank one in direction `n`, with coefficient

`nu = d-g^T M^(-1)g = det(Lambda)/det(M)`.                 (7.4)

There is no additional norm factor when returning to the physical residual: `W^T n=0` and `U_K^T U_K=I-WW^T`, so `||U_K n||=1`. Also

`det B_0=det(R)^2 det(M)=delta_ij det(M)`.                 (7.5)

Multiplying (7.4)--(7.5) and taking absolute values proves (7.2). QED.

## 8. Rank-three zero-pair density bound

The rank-one residual is `R=nu L^2`, where `L` is a unit original-coordinate linear projection and therefore has density cap `M<=sqrt(2)` by the product-marginal theorem.

For completeness, if a real `W` has density cap `M`, `nu!=0`, and `0<alpha<1/2`, then

`P(|t-nu W^2|<r) <= min(1,4M sqrt(r/|nu|))`.              (8.1)

Layer cake gives

`sup_t E|t-nu W^2|^(-alpha)
 <= (16M^2)^alpha/(1-2alpha) |nu|^(-alpha)`.              (8.2)

At `alpha=1/3`, `M=sqrt(2)`, this is

`sup_t E|t-R|^(-1/3)
 <= 3*32^(1/3)|nu|^(-1/3)`.                               (8.3)

Combining (4.4), (7.2), and (8.3), the constants simplify exactly:

`K_0 * 3*32^(1/3)=36`.

Therefore

`boxed: ||p_Q||_infinity
 <= 36 (|det Lambda| delta_ij)^(-1/3).`                   (8.4)

If this is an exact-rank-three target form with all three active eigenvalues of modulus at least one, then `|det Lambda|>=1`, hence

`||p_Q||_infinity <= 36 delta_ij^(-1/3)`.                 (8.5)

For example, `delta_ij>=1/8` gives `||p_Q||_infinity<=72`.

The sign of `Lambda` is unrestricted. In a nondegenerate three-dimensional indefinite form the Witt index is one, so two linearly independent null spectral rows cannot also be mutually `Lambda`-orthogonal. Consequently, whenever `A_ii=A_jj=0` and `delta_ij>0`, automatically `b=A_ij!=0`; the hyperbolic pivot is legitimate.

## 9. Exact wedge-mass identity and the remaining factor

Let `ell_i=||u_i||^2`. Parseval for the three-column frame gives

`sum_j ell_j=3`,
`sum_j <u_i,u_j>^2=ell_i`.

Therefore

`sum_{j!=i} delta_ij
 = sum_{j!=i}[ell_i ell_j-<u_i,u_j>^2]
 = ell_i(3-ell_i)-(ell_i-ell_i^2)
 = 2 ell_i`.                                               (9.1)

This identity is exact. In particular, a heavy spectral row with `ell_i>1/4` carries total wedge mass greater than `1/2` against the other physical rows.

However, (9.1) does **not** force one pair with `delta_ij` bounded below independently of dimension: the mass can be spread over arbitrarily many rows. Applying (8.4) one pair at a time then pays the uncontrolled reciprocal factor `delta_ij^(-1/3)`. This is the precise missing geometric factor left by the present coarea mechanism.

Accordingly, the first unpaid implication is:

**`QFORM-DISTRIBUTED-WEDGE-AGGREGATION-v1`.** In the heavy near-isotropic branch, turn the total area identity `sum_j delta_ij=2ell_i` (and the corresponding cross coefficients) into either (a) a collective two-coordinate coarea estimate that pays an aggregate area rather than `max_j delta_ij`, (b) a post-Schur cross/ridge certificate to which the completed partner theorems apply, or (c) another product-preserving bank/hyperbolic-square smoothing certificate. The aggregation must occur before reciprocal pair-minor payment.

The same issue persists for small nonzero diagonal entries: the exact zero-pair theorem identifies the limiting geometry, but a perturbative near-zero-diagonal argument still has to be made uniform.

## 10. Scope and regularity

What is proved in this report:

- the product fractional kernel (3.3)--(3.5);
- the exact two-coordinate hyperbolic coarea inequality (4.3)--(4.4), preserving arbitrary product densities;
- the partner-applied two-cross density bound (5.3), allowing arbitrary additional residual spectrum in the partner's scope;
- the one-cross third-Riesz theorem (6.1) and density consequence (6.6);
- the exact rank-three determinant/wedge identity (7.2);
- the exact-rank-three zero-pair density bound (8.4);
- the exact wedge-mass identity (9.1), which identifies the remaining dimension-loss factor.

What is **not** proved:

- the unrestricted three-large-eigenvalue conjecture;
- a universal extraction/aggregation theorem from `sum delta_ij=2ell_i`;
- a uniform perturbation from exact zero diagonals to all near-isotropic heavy rows;
- the arbitrary-extra-spectrum theorem without one of the stated residual cross certificates;
- continuity of the density in these new coarea branches.

The conclusions here are absolute continuity plus an essentially bounded density in the stated branches. Continuity remains a separate open regularity question for this mechanism.

## 11. Corrections respected

The proof does not use the refuted law-uniform pointwise quadratic oscillatory decay, does not rotate and retain independence, does not take a dimension-growing unrestricted fiber supremum, does not replace independence by a bounded conditional density, and does not assume a single uniformly good physical minor exists. In particular it is consistent with the live corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`.
