SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B16, 2026-09-22T19:04:33Z.
attacking: projection-product interaction at a singular physical pair, retaining the unnormalized original-product weight instead of a normalized conditional supremum.

# Rank-one physical-pair aggregate smoothing

Run: `20260922T190433Z-account01-B16-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING FULL-MATRIX BRANCH PROVED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Fresh control used before the main write: `yspennstate/math-research-brain@22540f97867e35d0e2ef3976586c6770d0238210`, OWNER CONTROL revision `2026-09-22.13`. The mathematical corrections in CURRENT_RESEARCH / CORRECTION_INBOX override the refuted rank-three arbitrary-joint coarea and normalized conditional-supremum claims still present in owner-message prose.

## 1. Target and source-corrected first implication

The owner target remains: for arbitrary independent real coordinates with densities at most one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `Q=X^TAX`; continuity is separate.

The designated partner `account02/B16`, run `20260922T181706Z-account02-B16-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@1dd4fc6bb98e57eed6a5a4e77273193cacea77a4`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T181706Z-account02-B16-QFORM-auto11/REPORT.md`

proved that the proposed scalar-rest interface

`sup_b ||p_(Q3 | Q'=b)||_infinity <= C`

is false even for a four-dimensional target matrix. Its exact endpoint calculation exhibits the repair principle: the normalized conditional peak can diverge, but the *unnormalized scalar-rest weight* vanishes strongly enough to compensate. The present run applies that correction directly: no supremum over a conditioned scalar is taken. Instead a singular pair produces an inverse fractional power of a random physical linear coefficient, and that inverse power is integrated against its actual product-source law.

A second completed partner result, `account02/B16` run `20260922T163840Z-account02-B16-qform-r13`, canonical mathematics

`yspennstate/math-open-problems@d2e3dd1587a3fa93707631ea847c48279f3dc6dc`,

proves the complementary invertible-indefinite projected-pair half-Riesz bridge. The new theorem below treats a determinant-zero rank-one physical pair and does not invert that pair.

## 2. Product rank-one pair lemma

### Lemma 2.1 — `QFORM-RANK1-PAIR-TRANSVERSE-AFFINE-v1`

Let `X_1,X_2` be independent real random variables with densities bounded by one. Let

`B=lambda u u^T`,

where `lambda !=0` and `u in R^2` is a unit vector. Let `n` be a unit vector orthogonal to `u`. For any `b in R^2`, `c in R`, put

`P(X)=X^T B X+b^T X+c`

and write

`delta=n^T b`.

If `delta !=0`, then `P(X)` is absolutely continuous and

`boxed( ||p_P||_infinity <= 6 |lambda|^(-1/3)|delta|^(-2/3). )`       (2.1)

No independence is asserted after rotating the pair coordinates. The proof uses the original product density pointwise.

### Proof

Use deterministic orthonormal coordinates

`r=u^T x`, `s=n^T x`.

Writing `b=alpha u+delta n`,

`P=lambda r^2+alpha r+delta s+c`.

The original product density in these coordinates is

`h(r,s)=f_1(u_1r+n_1s) f_2(u_2r+n_2s)`,

which is generally not a product in `(r,s)`, but still satisfies the exact product representation above and `0<=h<=1`.

For fixed output value `t`, solve

`s=phi_t(r):=(t-c-lambda r^2-alpha r)/delta`.

The change of variables `(r,s)->(r,P)` has Jacobian `|delta|`, hence for a.e. `t`

`p_P(t)=|delta|^(-1) int_R f_1(F(r)) f_2(G(r)) dr`,                  (2.2)

where

`F(r)=u_1r+n_1 phi_t(r)`, `G(r)=u_2r+n_2 phi_t(r)`.

Both `F,G` are quadratic. Put

`W:=|F'G''-G'F''|`.

Since `(F',G')=u+n phi_t'` and `(F'',G'')=n phi_t''`,

`boxed( W=|phi_t''|=2|lambda|/|delta|. )`                             (2.3)

Fix `a>0` and partition the real line into

`E_F={|F'|>=a}`,

`E_G={|F'|<a, |G'|>=a}`,

`E_0={|F'|<a, |G'|<a}`.

On `E_F`, discard the second density factor and use the one-dimensional area formula. Because a quadratic has multiplicity at most two,

`int_(E_F) f_1(F(r))f_2(G(r))dr <=2/a`.                              (2.4)

The same argument gives at most `2/a` on `E_G`.

For `E_0`, the derivative vector

`d(r)=(F'(r),G'(r))`

runs on an affine line with constant velocity `v=(F'',G'')`. Its Euclidean distance from the origin is exactly `W/|v|`. If `E_0` is nonempty, that line meets the square `[-a,a]^2`, so

`|v|>=W/(sqrt(2)a)`.

The Euclidean length of any chord of that square is at most `2sqrt(2)a`. Therefore the corresponding parameter interval has length

`|E_0|<=4a^2/W`.                                                     (2.5)

Since both density factors are at most one,

`int_R f_1(F(r))f_2(G(r))dr <=4/a+4a^2/W`.                           (2.6)

Choose `a=(W/2)^(1/3)`. Then

`4/a+4a^2/W =12*2^(-2/3)W^(-1/3)`.

Insert (2.3) into (2.2):

`p_P(t)<=|delta|^(-1) 12*2^(-2/3)(2|lambda|/|delta|)^(-1/3)`

`=6|lambda|^(-1/3)|delta|^(-2/3)`.

This proves (2.1). The same majorant gives absolute continuity by disintegration. QED.

## 3. Keep the random transverse coefficient weighted

The previous lemma is deliberately not followed by `sup |delta|^(-2/3)`. This is where the latest account02/B16 correction is applied.

### Lemma 3.1 — capped scalar inverse moment

If a real random variable `Y` has density bounded by `K`, then

`boxed( E|Y|^(-2/3) <= 3(2K)^(2/3). )`                               (3.1)

The bound is translation-uniform. Indeed the rearrangement/bathtub extremizer for the even decreasing kernel `|y|^(-2/3)` is density `K` on the centered interval of length `1/K`, and

`K int_(-1/(2K))^(1/(2K)) |y|^(-2/3)dy =3(2K)^(2/3)`.

This is the exact analogue of the partner's endpoint compensation: a potentially divergent normalized conditional peak is integrated against the actual scalar source density before any supremum is taken.

## 4. Full-matrix theorem for a rank-one physical pair

### Theorem 4.1 — `QFORM-RANK1-PAIR-AGGREGATE-SMOOTHER-v1`

Let `X=(X_1,...,X_n)` have independent coordinate densities bounded by one, and let `A` be any real symmetric matrix. Choose an original-coordinate pair `I={i,j}`. Write

`P=A[I,I]`, `C=A[I,I^c]`.

Assume `P` has rank one and nonzero eigenvalue `lambda`. Let `n_I` be a unit null vector of `P`, and put

`eta=||C^T n_I||_2`.

If `eta>0`, then the FULL quadratic form `Q=X^TAX` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <=18*2^(1/3) (|lambda| eta^2)^(-1/3).
)`                                                                    (4.1)

Every coefficient in the complementary block `A[I^c,I^c]`, every extra eigenvalue, and every other coupling is arbitrary.

The theorem also survives an arbitrary deterministic affine term added to `Q`.

### Proof

Let `Z=X_(I^c)`. Conditional on `Z=z`,

`Q = X_I^T P X_I + 2 X_I^T C z + d(z)`.

The transverse coefficient from Lemma 2.1 is

`delta(z)=2 n_I^T C z`                                               (4.2)

(up to a harmless deterministic translation if an affine term is present). Hence for a.e. `z` with `delta(z)!=0`,

`||p_(Q|Z=z)||_infinity
 <=6|lambda|^(-1/3)|delta(z)|^(-2/3).`                                (4.3)

The coefficient vector of `delta(Z)` has Euclidean norm `2eta`. By the Rogozin--Ball one-dimensional projection theorem, a normalized linear projection of independent cap-one coordinates has density at most `sqrt(2)`. Therefore

`||p_delta||_infinity <= sqrt(2)/(2eta)=1/(sqrt(2)eta).`              (4.4)

Apply Lemma 3.1:

`E|delta|^(-2/3)
 <=3( sqrt(2)/eta )^(2/3)
 =3*2^(1/3)eta^(-2/3).`                                               (4.5)

Mixture and (4.3) now give

`||p_Q||_infinity
 <=6|lambda|^(-1/3)E|delta|^(-2/3)
 <=18*2^(1/3)|lambda|^(-1/3)eta^(-2/3),`

which is (4.1). Since the right side is integrable over the conditioning law, it also supplies absolute continuity. QED.

## 5. Exact determinant-mass form: aggregate before inversion

The quantity in (4.1) is an exact aggregate of physical principal `3x3` determinants. For `k notin I`, make a deterministic orthogonal change only inside the two-dimensional pair so that

`P=diag(lambda,0)`.

Congruence by this pair rotation does not change the determinant of the principal triple `I union {k}`. In the basis `(u,n_I,e_k)` the triple is

`[[lambda,0,a_k],
  [0,0,b_k],
  [a_k,b_k,d_k]]`,

where `b_k=n_I^T C e_k`. Thus

`det A[I union {k}] = -lambda b_k^2`.                                (5.1)

Consequently

`boxed(
 M_I:=sum_(k notin I) |det A[I union {k}]|
     =|lambda| eta^2.
)`                                                                    (5.2)

Theorem 4.1 becomes

`boxed( ||p_Q||_infinity <=18*2^(1/3) M_I^(-1/3). )`                 (5.3)

This pays the *total determinant mass before reciprocal payment*. No single well-conditioned principal triple is selected. In particular arbitrarily many individually tiny triple determinants can still give a universal bound when their total mass is bounded below.

For example, `M_I>=3/8` gives

`||p_Q||_infinity <=18(16/3)^(1/3)=31.4488967305...`.                 (5.4)

## 6. Direct payment of the singular O2 packet from the current overlap reduction

The completed account02/B07 O2 identity writes, for a shared physical pair `I`,

`G_I=det(P)B-U adj(P)V`.

When `rank(P)=1`, write `P=lambda w w^T` and let `w_perp` span its null direction. Then

`G_I=-lambda (Uw_perp)(w_perp^T V)`

and therefore

`||G_I||_F=|lambda| ||Uw_perp||_2 ||V^T w_perp||_2`.                  (6.1)

The transverse vector `C^T w_perp` from Theorem 4.1 contains both of these disjoint coordinate-bank components. Hence

`M_I=|lambda| ||C^T w_perp||_2^2`

`>=|lambda| ( ||Uw_perp||_2^2 + ||V^T w_perp||_2^2 )`

`>=2|lambda| ||Uw_perp||_2 ||V^T w_perp||_2`

`=2||G_I||_F`.                                                        (6.2)

Therefore every individual rank-one singular O2 packet satisfies the full-form bound

`boxed( ||p_Q||_infinity <=18 ||G_I||_F^(-1/3). )`                   (6.3)

This is a genuine payment, not merely a structural split. It removes the need to invert a singular physical pair and retains all additional spectrum.

It does **not** yet pay the entire O2 aggregate from only

`sum_I ||G_I||_F^2 >=1/324`,

because that mass can in principle be spread over many physical pairs. Selecting the largest packet would reintroduce a dimension tax. The next aggregate step must combine many singular packets before the reciprocal `(-1/3)` payment, or show that the complementary diffuse/ridge branch pays whenever the packet mass is too dispersed.

## 7. Relation to the designated account02/B16 results

The latest partner falsifier says that a normalized scalar conditional supremum can diverge even while the real mixture is harmless. Equations (4.3)--(4.5) implement the corrected mechanism exactly:

`false interface: sup_z |delta(z)|^(-2/3),`

`valid weighted interface: E_Z |delta(Z)|^(-2/3) <=3*2^(1/3)eta^(-2/3).`

The earlier positive account02/B16 theorem handles an invertible indefinite two-dimensional projected quadratic by a half-Riesz estimate and then a square smoother when an independent final innovation is available. Theorem 4.1 supplies a different endpoint: the physical pair itself is singular, and its null direction is smoothed by an overlapping original-product linear coefficient from all remaining coordinates. Thus no post-rotation independence and no disjoint final-square bank are asserted.

## 8. Corrections respected and exact remaining implication

This proof does not use:

* arbitrary-joint rank-three coarea;
* normalized conditional projection-density moments;
* the now-refuted scalar `Q_rest` conditional supremum;
* independence after a spectral rotation;
* one reciprocal tiny physical minor;
* pointwise law-uniform Fresnel decay.

The first unpaid implication from this B16 branch is now:

`QFORM-SINGULAR-O2-AGGREGATE-BEFORE-RECIPROCAL-v1`:

starting from the current overlap reduction's aggregate singular mass, combine many rank-one pair estimates before paying `M_I^(-1/3)`, or prove that dispersion of all `M_I` forces an already-paid diffuse/ridge branch. The analogous overlapping-innovation endpoint for invertible pairs also remains open.

The full quadratic-form conjecture is **OPEN / NOT PROVED**. Continuity is not claimed by this theorem; only existence of an essentially bounded density in its stated branch is proved.
