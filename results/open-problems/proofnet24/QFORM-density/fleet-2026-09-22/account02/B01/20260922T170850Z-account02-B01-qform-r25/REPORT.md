# QFORM account02/B01 r25 — physical three-coordinate determinant theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T170850Z-account02-B01-qform-r25`  
Assignment: Oscillatory replacement  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Full target and contribution

The full target remains open: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample.

This run proves a new product-preserving three-coordinate theorem. It closes the zero/near-zero *physical diagonal* difficulty whenever one has a quantitatively nonsingular physical principal triple, while keeping arbitrary affine leakage created by conditioning all other coordinates.

### Theorem — `QFORM-PHYSICAL-TRIPLE-DET-v1`

Let `B` be any invertible real symmetric `3 x 3` matrix. Let `X_1,X_2,X_3` be independent real random variables with probability densities at most one. For arbitrary `ell in R^3` and `c in R`,

`Q_B = X^T B X + ell^T X + c`

has an essentially bounded density and

`||p_{Q_B}||_infinity <= 216 |det B|^(-1/3).`                (1.1)

Consequently, for the full ambient target form `Q=X^T A X`, if some original-coordinate triple `I` satisfies `D=|det A[I,I]|>0`, then after conditioning on every coordinate outside `I`,

`||p_Q||_infinity <= 216 D^(-1/3).`                          (1.2)

All outside quadratic coefficients and cross couplings are retained: they become an arbitrary affine term in the conditioned physical triple. No rotated coordinates are declared independent.

The theorem is not a full solution because the three-large-eigenvalue hypothesis does not force one physical principal `3 x 3` determinant bounded below by a universal constant. Known diffuse/bank stress families have all fixed physical minors tending to zero. Thus the remaining task is genuinely to aggregate many small physical certificates or combine this theorem with the ridge/grouped-coordinate branches.

## 2. Source-pinned dependencies and corrections


The completed compatible partner theorem actually applied is the arbitrary-orientation rank-two/three Schur fusion at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Its rank-three consequence states: for an invertible original-coordinate rank-three principal block `B=VMV^T`, a nonzero physical diagonal `a=B_ii`, and spectral row leverage `c_i`, the full ambient form (including arbitrary outside-induced affine terms) satisfies

`||p||_infinity <= 128 [c_i |a| |det M|]^(-1/4).`            (2.1)

For a full `3 x 3` block, `V` is orthogonal, so `c_i=1` and `|det M|=|det B|`.

The named partner account03/B01 also independently supplied the preceding arbitrary-orientation half-Riesz proof at commit `76fd4f9ccae2e422498fec6d4156bfd64775c8e4`; that report identifies the zero/near-zero outer pivot as the remaining branch. This run uses the later fused constant (2.1) and supplies a different product-coordinate treatment of the complementary small-diagonal branch.

Live corrections consumed include: law-uniform pointwise quadratic-phase decay is false; post-rotation independence is forbidden; direct absolute-value ambiguity/Hölder aggregation can lose a logarithm; one fixed physical triple is not guaranteed quantitatively by the spectral hypothesis. None of those refuted premises is used below.

## 3. A near-identity product density lemma

The key new replacement is distributional, not pointwise in frequency.

### Lemma 3.1 — product after a small shear

Let `X,Y` be independent with probability densities at most one. Let

`U=X+lambda Y+alpha`, `V=Y+mu X+beta`,

where `|lambda|,|mu|<=1/4`; the translations `alpha,beta` are arbitrary. Put `D=1-lambda mu`, so `D>=15/16`. If `H` is the density of `UV`, then for every `r!=0`,

`H(r) <= 16/3 + (32/15) log(1/|r|)` for `0<|r|<1`,          (3.1)

and

`H(r) <= 16/(3 sqrt(|r|))` for `|r|>=1`.                    (3.2)

In particular,

`H(r) <= 16/3 + (32/15) log_+(1/|r|).`                       (3.3)

#### Proof

Translations do not affect Jacobians, so suppress them in the notation. The map `(x,y)->(u,v)` has determinant `D`; its joint density is

`rho(u,v)=D^(-1) f(x(u,v)) g(y(u,v))`.

For `r!=0`, the product-density formula is

`H(r)=int_R rho(u,r/u) du/|u|`.                              (3.4)

First suppose `0<|r|<1`. On `|u|>=1`, use `g<=1` and `|u|^(-1)<=1`. Along `v=r/u`,

`x(u)=(u-lambda r/u)/D`,
`dx/du=(1+lambda r/u^2)/D`.

Hence `|dx/du| >= (1-|lambda|)/D >= (3/4)/D`. Each of the two tails therefore contributes at most `1/(1-1/4)=4/3`, so together they contribute at most `8/3`.

On `|u|<=|r|`, change from `u` to `v=r/u`; the symmetric argument using `f<=1` and the derivative of `y(v)` gives another at most `8/3`. On the middle region `|r|<|u|<1`, simply use `rho<=D^(-1)<=16/15`; since

`int_{|r|<|u|<1} du/|u|=2 log(1/|r|)`,

the middle contributes at most `(32/15)log(1/|r|)`. This proves (3.1).

If `|r|>=1`, split at `|u|=sqrt(|r|)`. On the outer part use the preceding `x` change of variables and `|u|^(-1)<=|r|^(-1/2)`; on the inner part switch to `v=r/u`, where `|v|>=sqrt(|r|)`, and use the symmetric `y` change of variables. The two contributions total at most

`4/(1-1/4) |r|^(-1/2)=16/(3sqrt(|r|))`,

proving (3.2). QED.

The logarithm at the product singularity is expected: it is exactly the rank-two opposite-sign obstruction. The next lemma shows that one genuine transverse square averages it integrably.

## 4. Uniform logarithmic averaging through a square

### Lemma 4.1

If `Z` has a probability density at most one, then for every `L>0` and every real `c`,

`E log_+( L/|Z^2+c| ) <= 2 + log(1+8L).`                     (4.1)

#### Proof

For every `epsilon>0` and every real `c`, elementary interval geometry gives

`Leb{z: |z^2+c|<epsilon} <= 2 sqrt(2 epsilon).`               (4.2)

Indeed, if `c>=0`, the set is empty unless `c<epsilon` and then lies in an interval of length at most `2sqrt(epsilon)`. If `c<0`, write `a=-c`; for `a>=epsilon` it is the union of two intervals with total length

`2[sqrt(a+epsilon)-sqrt(a-epsilon)] <= 2sqrt(2epsilon)`,

with the maximum attained at `a=epsilon`; if `a<epsilon` the same bound is immediate. Since the density of `Z` is at most one,

`P(|Z^2+c|<epsilon) <= min(1,2sqrt(2epsilon)).`               (4.3)

Layer cake gives

`E log_+(L/|Z^2+c|)`
` = int_0^infinity P(|Z^2+c|<L e^{-s}) ds`
` <= int_0^infinity min(1,2sqrt(2L)e^{-s/2}) ds`.             (4.4)

If `L>=1/8`, the last integral equals `2+log(8L)`; if `L<1/8`, it equals `4sqrt(2L)<2`. Both cases are bounded by (4.1). QED.

This is a direct averaged/distributional replacement for the false scalar pointwise Fresnel bound: the logarithmic product singularity is not suppressed pointwise, but it is uniformly integrable against any third cap-one coordinate through a nonzero quadratic coefficient.

## 5. Proof of the physical-triple determinant theorem

By scaling the entire polynomial, it is enough to prove (1.1) under

`|det B|=1`.                                                 (5.1)

Write `d_i=B_ii`, and write the off-diagonal entries as `a_12,a_13,a_23`. Fix

`delta=1/8`.                                                 (5.2)

### Case A: one physical diagonal is not small

If some `|d_i|>=delta`, apply the source-pinned rank-three Schur theorem (2.1). For a full three-coordinate block, `c_i=1` and `|det B|=1`, hence

`||p||_infinity <=128 delta^(-1/4)=128*8^(1/4)`
`                    <215.270<216`.                          (5.3)

Arbitrary affine terms are allowed by the source theorem.

### Case B: all three physical diagonals are small

Assume `|d_i|<delta` for all `i`. Since the eigenvalues `lambda_1,lambda_2,lambda_3` of `B` have product of absolute value one,

`||B||_F^2=sum lambda_i^2 >=3`                               (5.4)

by AM-GM. Therefore

`2 sum_{i<j} a_ij^2 = ||B||_F^2-sum_i d_i^2 >3(1-delta^2)`,

so for at least one pair, relabeled `(1,2)`,

`A:=|a_12| >= a_0:=sqrt((1-delta^2)/2)=sqrt(63/128)`.        (5.5)

Set `a=a_12` and

`Delta=a^2-d_1d_2>0`.

Choose the root

`K=a+sgn(a)sqrt(Delta)`,                                    (5.6)

and put

`lambda=d_2/K`, `mu=d_1/K`.                                 (5.7)

Because `K^2-2aK+d_1d_2=0`, one has the exact factorization

`d_1 x^2+2axy+d_2y^2`
`   =K(x+lambda y)(y+mu x).`                                (5.8)

Moreover `|K|>=A`, so by (5.5)

`|lambda|,|mu| <=delta/A <=delta/a_0<1/4`.                  (5.9)

Now condition on the third coordinate `Z=z`. Include all affine terms. After the invertible near-identity change

`u=x+lambda y`, `v=y+mu x`,

the terms linear in `(u,v)` have coefficients affine in `z`; write them as `p(z)u+q(z)v`. Completing the product gives

`Kuv+p(z)u+q(z)v`
` =K[u+q(z)/K][v+p(z)/K]-p(z)q(z)/K`.                       (5.10)

Thus conditionally on `Z=z`, the first two coordinates contribute `KUV+r(z)`, where the translated pair `(U,V)` has exactly the form in Lemma 3.1 and `r` is a scalar quadratic polynomial in `z`.

The quadratic coefficient of `r` is the Schur complement of the physical pair block

`P=[[d_1,a],[a,d_2]]`.

Since `det P=d_1d_2-a^2=-Delta`, the Schur determinant identity gives

`s:=coeff_{z^2} r = det B/det P`,
`|s|=1/Delta`.                                               (5.11)

In particular `s!=0`; complete its square as

`r(z)=s(z-z_0)^2+r_0`.                                      (5.12)

Lemma 3.1 and the scaling of a product density imply, for every `t`,

`p_{Q_B|Z=z}(t)`
` <= |K|^(-1)[16/3 +(32/15) log_+(|K|/|t-r(z)|)].`          (5.13)

Average in `z` and use Lemma 4.1 after translating `z_0`. Its parameter is

`L=|K|/|s|=|K| Delta`.                                      (5.14)

Since `Delta<=A^2+delta^2`, `A>=a_0>delta`, and

`|K|=A+sqrt(Delta) <=3A`,

we have

`L<=6A^3`.                                                   (5.15)

Hence

`p_{Q_B}(t)`
` <= A^(-1){16/3 +(32/15)[2+log(1+48A^3)]}.`                (5.16)

For `c_0=48^(1/3)`,

`1+48A^3 <=(1+c_0 A)^3`,

and `A -> log(1+c_0 A)/A` is decreasing on `(0,infinity)`. Therefore the right side of (5.16) is maximized at `A=a_0` after this harmless enlargement, where it is

`<25.241<26`.                                               (5.17)

This is far below the Case-A constant. Combining (5.3) and (5.17) proves the normalized estimate `||p||_infinity<216`.

Finally, for general `D=|det B|`, put `s=D^(1/3)` and divide the entire polynomial by `s`. The normalized quadratic matrix has determinant of absolute value one, while the affine term remains arbitrary. Scaling a one-dimensional density back multiplies its supremum by `s^(-1)`. Thus

`||p_{Q_B}||_infinity <=216 D^(-1/3)`,

proving (1.1). QED.

## 6. Ambient conditioning corollary

Fix a physical triple `I` in the full matrix `A` and condition on `X_{I^c}`. Independence leaves the three coordinates in `I` independent with their original cap-one laws. Every cross term between `I` and `I^c` becomes an affine coefficient depending on the conditioning value, while the quadratic Hessian on `I` remains exactly `A[I,I]`. Theorem (1.1) is uniform over that affine term, so every conditional density is bounded by `216 |det A[I,I]|^(-1/3)`. Averaging the conditional laws proves (1.2).

This gives a clean physical-coordinate certificate that includes the exact zero and near-zero diagonal situations that were left unpaid by a one-pivot Schur argument.

## 7. Why this is not yet the full theorem

The first remaining universal implication is now:

`AGGREGATED-PRINCIPAL-TRIPLE / RIDGE-GROUPED SYNTHESIS.`

Starting only from the assumption that `A` has at least three eigenvalues of modulus at least one, either extract enough aggregate original-coordinate determinant/ridge mass to invoke a dimension-free version of (1.2), or route the matrix into an already-paid ridge/diffuse/grouped-coordinate branch, while retaining arbitrary additional spectrum and original-coordinate product provenance.

A single good physical triple cannot be demanded: the existing singleton-plus-two-banks and diffuse-frame stress families make every fixed small physical determinant tend to zero while the target law remains controllable by aggregation. Therefore (1.2) is an essential local certificate, not a disguised full reduction.

A possible next mechanism is to combine (1.2) with Cauchy-Binet mass of many physical triples before paying the negative one-third determinant power, using a signed-Fejer or ridge average rather than selecting one minor. No such aggregation is assumed here.

## 8. Exact algebra/constant regression

The accompanying `checks.py` verifies the symbolic factorization equation and the numerical constants used above. It also samples admissible small-diagonal triples to confirm only the crude inequalities used in (5.9) and (5.15). The random samples are regression evidence only; the proof is analytic.

Captured output ends `STATUS=PASS`.

## 9. Integrity

No pointwise law-uniform Fresnel decay, Gaussianity, moments, compact support, log-concavity, connected support, diagonal-basis independence, or post-rotation independence is used. No target-level truth claim is inferred from the finite checker. Full QFORM remains open and this report is not a full-proof candidate.
