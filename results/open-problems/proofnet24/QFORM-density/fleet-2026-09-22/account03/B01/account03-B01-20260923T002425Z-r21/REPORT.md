SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T00:24:25Z.
attacking: overlapping grouped-square innovations — replace disjointness between the two same-sign grouped directions by a two-dimensional product-projection/area bound, then transfer it to the exact signed-Fejer interface.

# account03/B01 r21 — overlapping definite grouped pair and aggregate Pluecker payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement / FOURIER  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and live correction boundary

The owner target remains the unrestricted statement: for independent real original-coordinate inputs with probability densities at most one and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one, prove one dimension-free bound for the essential supremum of the density of `Q=X^T A X`, or produce a genuine target counterexample. No moment, compact-support, log-concavity, connected-support, Gaussian, centering, or post-rotation independence assumption is introduced.

Fresh control at the beginning of this run was `yspennstate/math-research-brain@57f48e76948c8b179017113c686a18674d1d8351`, OWNER CONTROL revision `2026-09-22.15`. The current `CURRENT_RESEARCH.md` still marks the full conjecture OPEN.

The following corrections are retained throughout:

* bounded input density does **not** imply a law-uniform pointwise quadratic-phase decay;
* arbitrary joint three-dimensional density caps do **not** imply the formerly proposed rank-three coarea bound;
* conditional density caps do **not** substitute for genuine independence;
* taking unrestricted fiber suprema can lose dimension;
* a fixed uniformly good physical minor or fixed cross-rank-three cut is not forced by the spectral hypothesis;
* absolute Wiener / coordinatewise absolute-value routes can fail even when the quadratic output density is bounded.

In particular, fix `s!=0` and `delta>0`. The set

`{x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure, so one may choose a measurable subset of measure one and use its indicator as an admissible density. Then

`Re E exp(i s X^2) >= cos(delta)`.

This phase-aligned counterexample remains intact. Nothing below asserts a pointwise Fresnel estimate or absolute Fourier integrability.

## 2. Source-valid ingredients actually used

### 2.1 Weighted product-projection density

I use account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an `m x k` matrix `R` with orthonormal columns and independent cap-one original coordinates `X`, the projected vector `R^T X` has a density bounded by `exp(k/2)`. For `k=2` the bound is `e`. The proof is an affine-fiber Brascamp--Lieb integral in the original product coordinates; it makes no independence claim after rotation.

### 2.2 Assigned partner account04/B01

The latest compatible partner report is account04/B01 `QFORM-GROUPED-SQUARE-INNOVATIONS-v1`, canonical source

`yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T234537Z-account04-B01-grouped-square-fejer-r2/REPORT.md`.

For three **disjoint** original-coordinate innovation banks, two same-sign shifted squares give

`||p_Q||_infinity <= 2 pi / (sigma_j sigma_k sqrt(|lambda_j lambda_k|))`,

with continuity. That report explicitly leaves mutually overlapping innovation maps as an unpaid interface.

I also use the same partner slot's completed exact signed-Fejer theorem, canonical

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`:

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`

for every law with bounded density, where `D_T` is the signed triangular Fejer average. This is the exact averaged-in-frequency interface and is strictly weaker than absolute Fourier integrability.

## 3. A two-dimensional overlapping-source projection lemma

Let `B` be a set of original coordinates and let

`M in R^(2 x |B|)`, `rank M=2`.

Put

`Y=M X_B in R^2`,
`G=M M^T`.

Then `G` is positive definite.

### Lemma 3.1 — `QFORM-OVERLAP-PROJECTION-CAP-v1`

The random vector `Y` has a density `g_Y` satisfying

`boxed: ||g_Y||_infinity <= e / sqrt(det G).`                  (3.1)

No disjointness of the two rows of `M` is required; they may use exactly the same original coordinates.

### Proof

Define

`R=M^T G^(-1/2)`.

Then `R` is a `|B| x 2` matrix with orthonormal columns because

`R^T R = G^(-1/2) M M^T G^(-1/2)=I_2`.

Set

`Z=R^T X_B=G^(-1/2)Y`.

The account02/B06 theorem gives `||g_Z||_infinity<=e`. Since `Y=G^(1/2)Z`, the change of variables gives

`g_Y(y)=g_Z(G^(-1/2)y)/sqrt(det G)`

for almost every `y`, proving (3.1). `QED`

The quantity in (3.1) is an aggregate source-area quantity. If the two rows of `M` are `a,b in R^|B|`, Cauchy--Binet gives the exact identity

`boxed: det G = ||a||^2 ||b||^2-(a dot b)^2
                = sum_(r<s) (a_r b_s-a_s b_r)^2.}`             (3.2)

Thus the theorem sums all physical two-coordinate Pluecker minors **before** paying an inverse determinant. No single good coordinate pair is selected.

## 4. Definite quadratic pushforward of the overlapping pair

Let `H` be any real symmetric definite `2 x 2` matrix, positive or negative definite, and let `h in R^2` be arbitrary.

### Lemma 4.1 — `QFORM-DEFINITE-OVERLAP-AREA-v1`

If `Y` has density cap `M_0`, then

`U=(Y+h)^T H (Y+h)`

has a density `q_h` satisfying, uniformly in `h`,

`boxed: ||q_h||_infinity <= pi M_0 / sqrt(|det H|).}`           (4.1)

### Proof

It suffices by reflection to take `H>0`. For an interval `I`, make the affine change

`u=H^(1/2)(y+h)`.

The Jacobian is `dy=du/sqrt(det H)`. Therefore

`P(U in I)
 <= M_0/sqrt(det H) * |{u: |u|^2 in I}|`.

In two dimensions

`|{u: |u|^2 in I}| <= pi |I|`,

because the Lebesgue pushforward of `u -> |u|^2` is exactly `pi ds` on `(0,infinity)`. Hence

`P(U in I) <= [pi M_0/sqrt(det H)] |I|`.

Interval domination implies absolute continuity and (4.1). `QED`

Combining Lemmas 3.1 and 4.1 yields

`boxed:
 ||q_h||_infinity
 <= pi e / [sqrt(det(MM^T)) sqrt(|det H|)].}`                   (4.2)

This is the central new analytic estimate.

## 5. Main theorem: two overlapping grouped innovations plus an independent remainder

Partition the original coordinates into disjoint sets

`C, B, D`.

Let `M in R^(2 x |B|)` have rank two, let `H` be definite, and let `h:R^C -> R^2`, `R_0:R^C->R` and `S:R^D x R^C->R` be arbitrary measurable functions for which the displayed expression is defined. Put

`Q = R_0(X_C)
    + (M X_B+h(X_C))^T H (M X_B+h(X_C))
    + S(X_D,X_C).`                                             (5.1)

### Theorem 5.1 — `QFORM-OVERLAPPING-DEFINITE-PAIR-INNOVATIONS-v1`

Under the full cap-one product-input assumptions,

`boxed:
 ||p_Q||_infinity
 <= K(M,H)
 := pi e / [sqrt(det(MM^T)) sqrt(|det H|)].}`                  (5.2)

This proves an essentially bounded density. It does **not** require the two grouped linear forms in `M X_B` to be independent or to have disjoint supports.

If, additionally, for almost every `X_C=c` the conditional remainder `S(X_D,c)` has an `L^1` density, then `p_Q` has a representative in `C_0(R)`. In particular this continuity conclusion holds when

`S(X_D,c)=lambda (d^T X_D+t(c))^2`

with `lambda!=0` and `d!=0`.

### Proof

Condition on `X_C=c`. The original banks `B` and `D` remain independent. By (4.2), the definite pair term

`U_c=(M X_B+h(c))^T H(M X_B+h(c))`

has a probability density `q_c` with the uniform cap `K(M,H)`, independent of `c`.

Let `mu_c` be the conditional probability law of `S(X_D,c)`. Independence of the original banks gives the conditional output density

`p_(Q|c)(t)
  = (q_c * mu_c)(t-R_0(c))`

in the measure-convolution sense. Hence

`||p_(Q|c)||_infinity <= ||q_c||_infinity <= K(M,H)`.

Averaging the conditional interval inequality over `c` proves absolute continuity and (5.2).

For the continuity statement, suppose `mu_c` has an `L^1` density `w_c`. Both `q_c` and `w_c` lie in `L^1`, so `q_c*w_c in C_0(R)` for almost every `c`. The conditional densities are uniformly dominated by `K(M,H)`. Dominated convergence therefore gives continuity and vanishing at infinity after averaging over `c`. `QED`

### Aggregate Pluecker form

Writing the rows of `M` as `a,b`, define

`Omega_2(M)^2 := sum_(r<s)(a_r b_s-a_s b_r)^2 = det(MM^T)`.

Then (5.2) is

`boxed:
 ||p_Q||_infinity
 <= pi e [Omega_2(M) sqrt(|det H|)]^(-1).}`                    (5.3)

This is an aggregate-before-inversion estimate: diffuse two-dimensional source area can remain order one even when every fixed physical two-coordinate minor is small.

## 6. Actual application of the assigned partner results

### 6.1 Exact signed-Fejer inequality

Apply account04/B01's exact signed-Fejer theorem to (5.2). For every `T>0` and `y in R`,

`boxed:
 D_T law(Q)(y)
 <= pi e / [sqrt(det(MM^T)) sqrt(|det H|)].}`                  (6.1)

This is the requested averaged-in-frequency replacement. It retains the sign/time cancellation and does not assert `int |phi_Q|<infinity` or any pointwise power decay.

### 6.2 Comparison with the partner's newer disjoint-bank theorem

If the two rows of `M` are supported on disjoint original-coordinate banks with norms `sigma_1,sigma_2`, then

`det(MM^T)=sigma_1^2 sigma_2^2`.

If `H=diag(lambda_1,lambda_2)` with `lambda_1 lambda_2>0`, (5.2) becomes

`||p_Q||_infinity
 <= pi e/[sigma_1 sigma_2 sqrt(|lambda_1 lambda_2|)].`          (6.2)

The latest account04/B01 grouped-square theorem exploits the extra independence and improves the constant in this special case to

`2 pi/[sigma_1 sigma_2 sqrt(|lambda_1 lambda_2|)].`             (6.3)

Thus (5.2) is not a constant improvement over the partner result. Its gain is structural: it removes **disjointness between the two same-sign grouped innovations** at the cost of the factor `e/2`. The remaining bank `D` may still be used for the third curvature direction or any other independent remainder.

Numerically

`pi e = 8.539734222673566`, `2 pi=6.283185307179586`.

## 7. A genuinely overlapping target-valid stress family

Let `m` be even. On one original-coordinate bank `B={1,...,m}` define

`a=(1,...,1)/sqrt(m)`,
`b=(1,-1,1,-1,...)/sqrt(m)`.

Then `||a||=||b||=1`, `a dot b=0`, and both linear forms use **every** coordinate in the same bank. Let `d=m+1` be one additional original coordinate and define

`Q_m=(a^T X_B)^2+(b^T X_B)^2+X_d^2.`                          (7.1)

The matrix of (7.1) has nonzero spectrum `{1,1,1}`. The partner's disjoint-pair hypothesis does not directly represent the first two squares because their source supports completely overlap. Here `M=[a^T;b^T]`, so `MM^T=I_2`, while `H=I_2`. Theorem 5.1 gives, for **every** admissible cap-one product input law,

`boxed: ||p_(Q_m)||_infinity <= pi e <8.540,}`                  (7.2)

uniformly in `m`. Since the third square is generated by the disjoint original coordinate `X_d`, its law has an `L^1` density and the resulting density in (7.2) is continuous and vanishes at infinity.

This family is only a strict-scope witness for the new overlapping-source theorem; it is not offered as a solution of the unrestricted conjecture.

## 8. Finite algebra check

The identity (3.2) was regression-tested on `2500` random real `2 x m` matrices with `m in {2,3,5,10,30}`. The maximum relative discrepancy between

`det(MM^T)`

and

`sum_(r<s) det(M[:,{r,s}])^2`

was `4.67e-15`. This is only a floating-point check of the displayed Cauchy--Binet identity; the proof is the exact algebra above.

## 9. What this pays and the next unpaid implication

The newest account04/B01 handoff identified “overlapping grouped sources” as the obstruction after its disjoint grouped-square theorem. Theorem 5.1 pays a substantial part of that obstruction:

* the two same-sign smoothing directions may now overlap **arbitrarily** in their original-coordinate sources;
* their entire two-dimensional Pluecker mass is aggregated before any inverse-minor payment;
* arbitrary conditioning-generated translations are harmless;
* an arbitrary independent conditional remainder cannot raise the essential density cap;
* if that remainder has an `L^1` density, continuity is also obtained.

The full QFORM conjecture remains OPEN. The first unpaid implication on this route is now more precise:

`QFORM-PAIR-VS-REMAINDER-SOURCE-SEPARATION-v1` — from the bare three-large-eigenvalue hypothesis in the surviving no-pivot / near-unit / balanced-star states, either expose a source bank carrying a quantitatively nondegenerate **definite two-dimensional grouped quadratic** with

`sqrt(det(MM^T)) sqrt(|det H|) >= c_0>0`

whose source is disjoint from the remaining curvature/remainder, or route to an already-paid ridge, cross-rank, scalar-pivot, saddle-plus-clean-square, or grouped-star packet. If no such pair-vs-remainder separation exists, one still needs a genuinely three-way overlapping product-provenance inequality.

This is a structural/extraction debt, not a pointwise oscillatory-decay debt. No claim is made that the three-large-eigenvalue hypothesis automatically supplies the hypothesis of Theorem 5.1.

**Continuity status:** proved for Theorem 5.1 under the stated conditional `L^1` remainder condition and for (7.1); not proved for the full owner target.

**Full target status:** `OPEN / NOT PROVED / NOT DISPROVED`.
