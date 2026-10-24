SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-22T20:02:41Z.
attacking: two-plane spectral compression — turn angular escape from a heavy near-isotropic cascade into a quantitative physical-pair certificate, and isolate the surviving near-ray multiscale bank.

# account01/B10 r17 — two-plane escape versus projective cascade

**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Live owner control:** revision `2026-09-22.15`; QFORM is the sole research target.  
**Continuity:** not proved by the new branch below; only an essentially bounded density is obtained where the pair-log theorem fires.

## 1. Conditional end-to-end argument and the first unpaid step

Work in the exact-rank-three target

`A = U M U^T`, `U^T U = I_3`, `sigma_min(M)>=1`,

with independent original physical coordinates having densities at most one. Let `u_i` denote the physical rows of `U` and let

`c_i=||u_i||^2`, `a_i=A_ii=u_i^T M u_i`.

The completed partner reduction account02/B10 r13 gives the following quantitative hard state. Choose a maximum-leverage row `i`, put

`c=||u_i||^2=1-rho`.

Outside already-paid diffuse/nonisotropic branches, and provided `rho>=1/64`, one reaches

`c>1/2`, `|a_i|<1/64`,

and there is a second original physical row `j` such that, writing `d=||u_j||^2` and `q=u_i dot u_j`,

`d + q^2/rho > 1/2`, `d>rho/2>=1/128`, `|a_j|<rho/8`.            (1.1)

The partner's exact isotropic-ray construction also proves that no fixed number of deletion/whitening steps can terminate the argument: arbitrarily many heavy zero-pivot rows can lie on one isotropic spectral ray. Thus the first missing implication is not another bounded-depth peel. It is:

> **Angular escape or bank compression.** Show that a second hard row which genuinely leaves the first projective ray creates a paid physical pair; consequently every unpaid continuation is quantitatively projectively clustered and must be aggregated as a bank before reciprocal local-minor payment.

This run proves the angular-escape half exactly. More precisely, in the partner hard state (1.1), if the normalized row directions have projective overlap at most `5/8`, then an invertible indefinite physical pair with explicit determinant and least-singular-value bounds is forced, and the completed pair-log theorem yields a universal density bound `<2131`. Therefore every unpaid second step has projective overlap `>5/8`; moreover its original leverage is of order `rho` and conditioning on both rows cuts the residual frame determinant by a factor greater than two. This turns the remaining cascade into a precise multiscale near-ray object rather than a generic heavy-row obstruction.

## 2. Source-pinned inputs actually consumed

### 2.1 Designated partner account02/B10 r13

Canonical source:

`yspennstate/math-open-problems@9a34dc516006d7eb417687b3d7d409f7dfaf33d9`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T154900Z-account02-B10-QFORM-r13/REPORT.md`.

I use its exact original-coordinate conditioning/whitening identities and, crucially, its hard-state implication (1.1). I also use its falsifier showing that arbitrarily long same-ray zero-pivot heavy cascades exist; this is why the present run changes mechanism from repeated peeling to two-plane compression.

### 2.2 Pair-log theorem

Canonical source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its stated scope is: for an exact-rank-three original-coordinate target with nonzero eigenvalue magnitudes at least `s`, if an original physical pair `B` is invertible indefinite, with

`D=|det B|`, `kappa=sigma_min(B)`,

then, with arbitrary outside coefficients/couplings,

`||p_Q||_infinity <= 8 sqrt(5) (D*kappa*s)^(-1/4)`.              (2.1)

This proof is supplied as a complete supporting analytic argument but is still pending the programme's independent review. Any density conclusion below that invokes (2.1) inherits that review status.

### 2.3 Corrections retained

The proof below does **not** use the refuted arbitrary-joint rank-three coarea lemma, positive conditional-projection density moments, law-uniform pointwise van-der-Corput decay, post-rotation independence, a uniformly good local `3x3/4x4` block dichotomy, fiberwise sup-density integration, or a conditional-density-cap substitute for original product provenance. The physical row pair produced below consists of two original independent coordinates.

## 3. New two-plane compression inequality

### Theorem 3.1 — `QFORM-RANK3-TWOPLANE-ESCAPE-v1`

Let `M` be a real symmetric `3x3` matrix all of whose eigenvalues have absolute value at least `s>0`. Let `e,f` be unit vectors. Set

`theta = |e dot f|`,
`alpha = e^T M e`, `beta=f^T M f`, `gamma=e^T M f`.

Then

`boxed: |gamma| >= s(1-theta) - max(|alpha|,|beta|).`             (3.1)

Equivalently, if both normalized diagonal Rayleigh coefficients are small and the mixed coefficient is also small, the two directions must be close in projective angle.

### Proof

The case `theta=1` is trivial because the right-hand side is nonpositive. Assume `theta<1`. Replacing `f` by `-f` if needed, write `tau=e dot f` with `|tau|=theta`. Let

`E=[e f]`,
`G=E^T E=[[1,tau],[tau,1]]`,
`B=E^T M E=[[alpha,gamma],[gamma,beta]]`.

The orthonormalized compression of `M` to `span{e,f}` is

`C=G^(-1/2) B G^(-1/2)`.

Let the eigenvalues of `M` be `lambda_1<=lambda_2<=lambda_3`, and those of `C` be `mu_1<=mu_2`. Cauchy interlacing gives

`lambda_1<=mu_1<=lambda_2<=mu_2<=lambda_3`.                    (3.2)

Because every `|lambda_k|>=s`, every possible signature forces at least one Ritz value to have modulus at least `s`:

- if all eigenvalues are positive, `mu_1>=lambda_1>=s`;
- if all are negative, `mu_2<=lambda_3<=-s`;
- for signature `(-,+,+)`, `mu_2>=lambda_2>=s`;
- for signature `(-,-,+)`, `mu_1<=lambda_2<=-s`.

Hence `||C||_op>=s`. On the other hand,

`||C||_op <= ||G^(-1/2)||^2 ||B||_op = ||B||_op/(1-theta)`.

Therefore

`||B||_op >= s(1-theta)`.                                      (3.3)

Finally split `B` into its diagonal and off-diagonal parts. The operator norms of those parts are respectively `max(|alpha|,|beta|)` and `|gamma|`, so

`||B||_op <= max(|alpha|,|beta|)+|gamma|`.

Combining this with (3.3) gives (3.1). QED.

## 4. Physical-row form and a near-ray certificate

For physical rows `u_i,u_j` with positive leverages

`c=||u_i||^2`, `d=||u_j||^2`,

put `e=u_i/sqrt(c)`, `f=u_j/sqrt(d)`. Then

`alpha=A_ii/c`, `beta=A_jj/d`, `gamma=A_ij/sqrt(cd)`.

Theorem 3.1 becomes

`|A_ij| >= sqrt(cd) [ s(1-|e dot f|) - max(|A_ii|/c,|A_jj|/d) ]_+`.  (4.1)

There is also an exact Parseval restriction on the projective overlap. Since `P=UU^T` is an orthogonal projection, `I-P` is positive semidefinite. Its `i,j` principal minor gives

`|u_i dot u_j|^2 <= (1-c)(1-d)`.                                (4.2)

Consequently

`|e dot f| <= sqrt((1-c)(1-d)/(cd))`.                            (4.3)

In particular, for exact null physical pivots `A_ii=A_jj=0`, if `c+d>1`, then

`|A_ij| >= s( sqrt(cd)-sqrt((1-c)(1-d)) ) >0`.                  (4.4)

Thus two large null rows cannot be spectrally separated without creating an actual original-coordinate cross coefficient.

A useful bank-level corollary is immediate. If a collection of normalized row directions `e_k` satisfies

`|e_k^T M e_k|<=epsilon`

and all its normalized pair couplings obey `|e_k^T M e_l|<=delta`, then (3.1) gives

`1-|e_k dot e_l| <= (delta+epsilon)/s`.                         (4.5)

After fixing one anchor and choosing signs relative to it,

`||sigma_k e_k-e_0||^2 <= 2(delta+epsilon)/s`.                 (4.6)

So failure to produce a mixed spectral coefficient gives a quantitative single-projective-ray certificate. This is precisely the geometry needed for a later grouped-coordinate bank compression; no distributional assertion is made by (4.6).

## 5. Application to the account02/B10 hard state

Now set `s=1` and use the partner hard state (1.1). Write

`c=1-rho`, `d=||u_j||^2`,
`e=u_i/sqrt(c)`, `f=u_j/sqrt(d)`,
`theta=|e dot f|`.

The normalized diagonal coefficients obey

`|alpha|=|a_i|/c < 1/(64c) < 1/32`,                            (5.1)

because `c>1/2`, and

`|beta|=|a_j|/d < rho/(8d) < 1/4`,                            (5.2)

because `d>rho/2`.

### 5.1 Angular escape is paid

Assume

`theta <= 5/8`.                                                 (5.3)

Theorem 3.1 and (5.1)--(5.2) give

`|gamma| > 1-5/8-1/4 = 1/8`.                                  (5.4)

Consider the normalized compressed pair

`C_0=[[alpha,gamma],[gamma,beta]]`.

Since `|alpha beta|<1/128` and `gamma^2>1/64`,

`det C_0 = alpha beta-gamma^2 < -1/128`.                        (5.5)

Thus this pair is invertible and indefinite, with

`|det C_0|>1/128`.                                              (5.6)

For the least singular value, let `x=|gamma|>=1/8`. Then

`||C_0||_op <= x+1/4`,

while

`|det C_0| >= x^2-1/128`.

Hence

`sigma_min(C_0) >= (x^2-1/128)/(x+1/4) >= 1/48`,               (5.7)

where the last function is increasing for `x>=1/8` and takes the value `1/48` at `x=1/8`.

The actual physical `2x2` principal pair is

`B_ij = diag(sqrt(c),sqrt(d)) C_0 diag(sqrt(c),sqrt(d))`.

Therefore

`|det B_ij| = cd |det C_0| > cd/128`,                          (5.8)

and

`sigma_min(B_ij) >= min(c,d) sigma_min(C_0)`.                  (5.9)

The partner inequalities give `c>1/2` and `d>1/128`, hence

`boxed: |det B_ij| > 1/32768,`                                 (5.10)

`boxed: sigma_min(B_ij) > 1/6144.`                             (5.11)

This is an original-coordinate indefinite pair, so the pair-log theorem (2.1), with `s=1`, applies to the full exact-rank-three quadratic form including all other couplings. It yields

`||p_Q||_infinity`
` < 8 sqrt(5) [ (1/32768)(1/6144) ]^(-1/4)`
` < 2131`.                                                       (5.12)

Thus **every partner hard state with projective angular escape `theta<=5/8` is paid by a universal constant**. The only external analytic dependency in (5.12) is the pair-log theorem, whose independent review is still pending as recorded above.

This is an actual application of the designated account02/B10 r13 result: r13 supplies the second original row with the quantitative conditions needed in (5.1)--(5.2), and the new theorem converts its angular departure into the physical-pair inequality (5.10)--(5.12).

### 5.2 What every unpaid second step must look like

If (5.12) does not fire, then necessarily

`theta > 5/8`.                                                  (5.13)

The Parseval inequality (4.2) now forces a scale relation. Since

`(u_i dot u_j)^2 = cd theta^2 > (25/64)cd`

and `(u_i dot u_j)^2 <= rho(1-d)`,

`d( rho + 25c/64 ) < rho`.

Using `c=1-rho`,

`boxed: rho/2 < d < 64 rho/(25+39rho) <= (64/25)rho.`          (5.14)

So an unpaid next row is not merely 'heavy after whitening': its **original** leverage is quantitatively on the same scale as the residual spectral mass `rho`.

There is a second exact invariant. After conditioning the first two physical rows, the residual spectral Gram matrix is

`G_2 = I-u_i u_i^T-u_j u_j^T`.

By the matrix determinant lemma, or directly from the `2x2` row Gram determinant,

`det G_2 = (1-c)(1-d)-(u_i dot u_j)^2`
`        = rho(1-d) - q^2`
`        = rho [1-(d+q^2/rho)]`.                               (5.15)

The partner hard-state condition says `d+q^2/rho>1/2`, hence

`boxed: det G_2 < rho/2.`                                      (5.16)

Thus every unpaid projectively aligned heavy step cuts the residual frame determinant by more than a factor two.

The partner's exact geometric-ray cascade has `theta=1` at every step and realizes precisely this multiscale fragmentation phenomenon. Equations (5.13)--(5.16) show that, after the present angular-escape theorem, that construction is no longer merely a falsifier of bounded-depth peeling: it is the canonical geometry of the surviving branch.

## 6. First remaining implication

The exact-rank-three problem is **not solved** here. The remaining implication is now narrower:

**`QFORM-PROJECTIVE-CASCADE-BANK-COMPRESSION-v1`.** Starting from a hard near-isotropic row, iterate only while every successive hard row is projectively aligned (`|e_k dot e_{k-1}|>5/8`, or a quantitatively stronger threshold obtained from (3.1)). Use the scale decay of the residual Gram determinant together with the near-ray estimate (4.6) to aggregate all such original coordinates into one product-linear bank *before* paying any reciprocal local determinant. Prove that either

1. the accumulated directions stay in one quantitative projective cone and the whole cascade compresses to a single scalar bank with two transverse bank directions; or
2. accumulated projective drift creates a pair for which Theorem 3.1 gives a determinant-scale physical-pair certificate, hence a paid pair-log branch; or
3. a diffuse/nonisotropic pivot branch from the existing programme fires.

The important new point is that alternative (2) is now quantitative and local, while every failure of it supplies the geometric data needed for alternative (1). The near-coloop case `rho<1/64`, left open in partner r13, should be handled in the same grouped-bank mechanism rather than by another finite peel.

A likely next invariant is the signed/projective path length of the normalized rows weighted by the original leverages. Equation (5.14) makes those weights comparable to the current residual scale, while (5.16) makes the number of genuinely macroscopic scales logarithmic in the residual determinant. What is still missing is a distributional theorem converting that geometric clustering into a dimension-free quadratic trace bound without taking forbidden conditional suprema.

## 7. Scope and integrity check

- Full arbitrary exact-rank-three orientation: **OPEN / NOT PROVED**.
- Full three-large-eigenvalue conjecture: **OPEN / NOT PROVED**.
- Continuity: **not proved** by this run.
- New theorem (3.1): fully elementary finite-dimensional linear algebra, no probabilistic regularity assumptions.
- Density consequence (5.12): conditional on the supplied pair-log theorem's current review status.
- No rotated coordinates are asserted independent.
- No moments, compact support, connected support, Gaussianity or log-concavity are assumed.
- No Monte Carlo or finite computation is used as proof.
- Changed-file privacy review: this report contains only mathematical statements, public programme identifiers, repository source pins and nonsecret run metadata; no credentials, scheduler IDs, machine paths, unrelated private data, email or Drive material.
