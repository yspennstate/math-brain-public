# account03/B19 — universal proof assembly: localized spectral-Schur smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T120353Z-account03-B19-qform-r11`  
**Assignment:** Universal proof assembly  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Target, corrections, and proof assembly

The target remains the full arbitrary-law statement: for independent real `X_i` with densities `0<=f_i<=1` and a real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `Q=X^TAX`, or produce a valid counterexample. Continuity is a separate stronger request.

This run uses the current correction set. In particular it does not use law-uniform pointwise quadratic-phase decay, does not assume independence after spectral rotation, does not take an unrestricted spectral-fiber supremum, and does not infer a full theorem from one coordinate minor. The later correction `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH` is also respected: `C=pi` is not a valid universal target constant; the full conjecture itself remains open.

The named partner `account04/B19` had no completed current-QFORM artifact at the final pre-publication snapshot, so no partner result is fabricated. A compatible completed other-account theorem is applied substantively: `account04/B18`, report `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`, proves dependent square smoothing. I also use the completed `account03/B08` diffuse-frame theorem and the sharp product-marginal theorem of Livshyts--Paouris--Pivovarov (arXiv:1507.07949), which gives density at most `2` for every two-dimensional orthogonal marginal of a product density with one-dimensional factors bounded by one.

The compact assembly is now:

1. **rank-exactly-three diffuse spectral frame:** closed by account03/B08, with density at most `3e` when all three nonzero eigenvalues have magnitude at least one;
2. **rank-exactly-three localized definite frame:** closed below, with density at most `4 sqrt(pi)` in the localized branch, hence at most `3e` after combining with (1);
3. **rank-exactly-three localized indefinite frame:** partially closed below when a localized physical row has minority-sign Rayleigh pivot; the unresolved subcase is a majority-sign or near-isotropic localized pivot;
4. **additional spectral remainder:** still requires a truncation/interaction theorem; no remainder is silently discarded.

Thus the first unpaid implication already occurs in pure rank three, before the extra-spectrum problem: close the localized indefinite majority-pivot/near-isotropic branch without selecting a dimension-losing physical minor.

## 2. One-coordinate spectral decomposition

Let `R` be an `n x 3` matrix with orthonormal columns and let `Lambda` be an invertible real symmetric `3 x 3` matrix. Put

`A0 = R Lambda R^T`,  `Q0 = X^T A0 X`.

Fix a physical coordinate `i`. Write `v in R^3` for row `i` of `R`,

`c=|v|^2`,  `a=v^T Lambda v`.

Assume first `0<c<1` and `a!=0`. Let `L` denote all coordinates except `i` and set

`M=I-vv^T=R_L^T R_L`.

Then `M` is positive definite. Define

`W=R_L M^(-1/2)`.

Its columns are orthonormal because `W^T W=I`. If

`Y=W^T X_L`,

then `Y` is independent of `x=X_i`, and

`R^T X = v x + M^(1/2)Y`.

Completing the square in the independent scalar `x` gives the exact identity

`Q0 = a (x + m(Y))^2 + Y^T T Y`,

where

`m(Y)=a^(-1) v^T Lambda M^(1/2)Y`,

`T=M^(1/2) S M^(1/2)`,

`S=Lambda - (Lambda v v^T Lambda)/a`.

The matrix `S` has rank two and kernel containing `v`. Standard Schur-inertia additivity shows that the two nonzero signs of `S` are the signs remaining after removing `sign(a)` from the inertia of `Lambda`. Hence:

- if `Lambda` is definite, `T` is definite;
- if `Lambda` has inertia `(2,1)` or `(1,2)` and `a` has the minority sign, `T` is definite;
- if `a` has the majority sign in an indefinite form, `T` is rank-two indefinite.

This is precisely the sign boundary relevant to the remaining localized branch.

## 3. Exact pseudodeterminant identity

### Lemma 3.1 — `QFORM-SPECTRAL-SCHUR-PDET-v1`

With the notation above,

`pdet(T) = c det(Lambda)/a`,

where `pdet` is the signed product of the two nonzero eigenvalues. In particular

`|pdet(T)| = c |det Lambda|/|a|`.

### Proof

Put `u=Lambda v`. For an invertible matrix `B` and a rank-one update, the adjugate identity gives

`adj(B+xy^T)=det(B)[(1+y^T B^(-1)x)B^(-1)-B^(-1)x y^T B^(-1)]`.

Apply it to `B=Lambda`, `x=-u/a`, `y=u`. Since

`u^T Lambda^(-1)u = v^T Lambda v = a`,

the first term vanishes and

`adj(S) = (det Lambda/a) vv^T`.

Because `S` is symmetric rank two with kernel `span(v)`,

`adj(S)=pdet(S) vv^T/c`,

so `pdet(S)=c det(Lambda)/a`.

It remains to check the congruence by `M^(1/2)`. For invertible `M`,

`adj(T)=det(M) M^(-1/2) adj(S) M^(-1/2)`.

Here `det(M)=1-c`, while Sherman--Morrison gives

`v^T M^(-1)v = c/(1-c)`.

The kernel of `T` is generated by `M^(-1/2)v`; comparing the rank-one adjugate with the normalized kernel therefore gives

`pdet(T)=det(M) [v^T M^(-1)v] det(Lambda)/a = c det(Lambda)/a`.

QED.

For `c=1`, the same formula follows by restricting directly to `v^perp`; this is the nonsingular two-dimensional residual version of the same calculation.

## 4. Localized spectral-Schur smoothing theorem

### Theorem 4.1 — `QFORM-LOCALIZED-SPECTRAL-SCHUR-v1`

Let `X_1,...,X_n` be independent with densities bounded by one. Let `A0=R Lambda R^T` have rank exactly three, with `R^T R=I_3` and every eigenvalue of `Lambda` having magnitude at least one. Fix a physical row `v` of `R`, set `c=|v|^2>0` and `a=v^T Lambda v!=0`.

Assume that the rank-two residual `T` above is definite; equivalently, this holds automatically when `Lambda` is definite, and in the indefinite `(2,1)` or `(1,2)` case when `a` has the minority sign. Then `Q0=X^T A0 X` has an essentially bounded density and

`||p_Q0||_infinity <= 2 sqrt(2 pi) ( |a| c |det Lambda| )^(-1/4).`   (4.1)

### Proof

Diagonalize the definite rank-two form `T` on its range. Let `U` be a `3 x 2` matrix with orthonormal columns spanning that range, and let the two nonzero eigenvalues be `mu_1,mu_2` of the same sign. Put

`Z=U^T Y=(WU)^T X_L`.

Because `WU` has orthonormal columns, `Z` is a two-dimensional orthogonal projection of the original product law on `X_L`. The Livshyts--Paouris--Pivovarov product-marginal theorem gives

`||p_Z||_infinity <= 2`.

Therefore the coarea formula for the definite ellipse gives the density bound

`||p_R0||_infinity <= 2 pi / sqrt(|mu_1 mu_2|)
                    = 2 pi / sqrt(|pdet T|)`,

where `R0=Y^T T Y`.

Now condition on the value `R0=r`. Since `x=X_i` is independent of all of `Y`, the conditional law of

`V_r = x + m(Y)`

is a mixture of translations of the density of `x`; hence its conditional density is still bounded by one. The dependent square-smoothing lemma of account04/B18 applies to

`Q0=R0+aV_R0^2`

and yields

`||p_Q0||_infinity
 <= 2 sqrt( [2 pi/sqrt(|pdet T|)] / |a| ).`

Using Lemma 3.1,

`|pdet T|=c|det Lambda|/|a|`,

so this becomes exactly (4.1):

`2 sqrt(2 pi) (|a| c |det Lambda|)^(-1/4)`.

No independence of spectral coordinates was assumed. QED.

## 5. A complete new assembled branch: all rank-three definite forms

### Corollary 5.1 — `QFORM-RANK3-DEFINITE-UNIVERSAL-v1`

Let `A0` have rank exactly three and all three nonzero eigenvalues have the same sign and magnitude at least one. For every admissible independent input law,

`||p_X^T A0 X||_infinity <= 3e`.

### Proof

Use a rank-three spectral frame `R`.

If every row leverage `c_i=|R_{i,*}|^2` is at most `1/2`, the account03/B08 diffuse-frame theorem gives the bound `3e` (and in fact a continuous representative).

Otherwise choose a row with `c>1/2`. Since `Lambda` is definite and its eigenvalues have magnitude at least one,

`|a|=|v^T Lambda v| >= |v|^2=c`.

Also `|det Lambda|>=1`. Theorem 4.1 therefore gives

`||p_Q0||_infinity
 <=2 sqrt(2 pi)(c^2)^(-1/4)
 < =4 sqrt(pi) < 3e`.

Thus `3e` is a universal essential-density bound on the entire rank-exactly-three definite branch, with arbitrary rotation and arbitrary independent coordinate densities bounded by one. QED.

This is not the full owner conjecture: indefinite rank-three localized frames and additional spectral directions remain.

## 6. Quantitative shape of the remaining pure-rank-three obstruction

The new theorem also isolates the hard localized indefinite branch. Suppose `c>1/2`. The cross energy from coordinate `i` into the remaining spectral coordinates is exactly

`sum_{j!=i} (A0)_{ij}^2
 = v^T Lambda (I-vv^T) Lambda v
 = |Lambda v|^2-a^2`.

Because all singular values of `Lambda` are at least one,

`|Lambda v|^2 >= c`,

hence

`sum_{j!=i}(A0)_{ij}^2 >= c-a^2`.   (6.1)

Thus a localized row whose Rayleigh pivot is near the isotropic cone cannot be weakly coupled: for example, if `c>1/2` and `|a|<=1/2`, the total squared cross coupling is at least `1/4`.

Consequently the unresolved pure-rank-three branch is not a vague localization problem. It is:

> **`QFORM-LOCALIZED-INDEFINITE-CROSS-AGGREGATION-v1` (OPEN):** in an indefinite rank-three spectral frame, when a row has `c>1/2` but its pivot has majority sign or lies close to zero, exploit the dimension-free cross-energy lower bound (6.1) to aggregate the distributed bilinear coupling without selecting one small physical coefficient, and obtain a universal density bound.

This branch must include matrices such as the majority-pivot Hadamard-type examples identified by account04/B18. Once it is paid, rank-exactly-three would be closed; only then does the separate extra-spectrum interaction/truncation debt remain.

## 7. Status and provenance

**PROVED in this run**

- `QFORM-SPECTRAL-SCHUR-PDET-v1`;
- `QFORM-LOCALIZED-SPECTRAL-SCHUR-v1`;
- `QFORM-RANK3-DEFINITE-UNIVERSAL-v1`, with universal bound `3e`;
- the exact localized near-isotropic cross-energy identity/lower bound (6.1).

**APPLIED completed mathematics**

- account03/B08 diffuse spectral-frame theorem;
- account04/B18 dependent square-smoothing theorem;
- Livshyts--Paouris--Pivovarov two-dimensional product-marginal bound.

**OPEN**

- `QFORM-LOCALIZED-INDEFINITE-CROSS-AGGREGATION-v1`;
- interaction with arbitrary additional spectral directions;
- full target and the full continuous-representative conclusion.

No claim of a complete proof or counterexample is made.
