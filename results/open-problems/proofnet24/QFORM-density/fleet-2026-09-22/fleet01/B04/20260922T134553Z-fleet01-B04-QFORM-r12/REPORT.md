# fleet01/B04 — zero-principal-minor product rearrangement and spectral closure

Run: `20260922T134553Z-fleet01-B04-QFORM-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and conditional route

The target remains the full arbitrary-dimensional statement: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density with one universal `L^infinity` bound, or give a genuine counterexample. Continuity of the density is a separate stronger owner goal.

This report does **not** assume post-rotation independence, moments, compact support, connected support, log-concavity, or a law-uniform pointwise oscillatory decay. It uses original-coordinate conditioning and decreasing-rearrangement/bathtub inequalities only.

The present run closes a new exact local branch:

> every three-dimensional target matrix whose one physical `2x2` principal minor vanishes has a universal density bound `4*2^(1/4)<4.757`.

The result survives arbitrary affine terms and therefore applies uniformly after conditioning on all coordinates outside such a physical principal triple in an ambient form.

What remains unpaid is global: the three-large-eigenvalue hypothesis does not force one exact zero principal minor, nor one uniformly good fixed minor. The next useful implication is a stable or aggregated replacement for the exact-zero-minor hypothesis.

## 2. Fresh controls, corrections, and named partner result

Fresh control immediately before publication retained owner revision `2026-09-22.5`, QFORM as the sole research target, and no later stop. The live correction inbox was reread and includes the known failures of law-uniform pointwise decay, one-cross-minor extraction, conditional density-cap substitution for independence, bounded-diameter localization, local fixed-block dichotomies, and fiberwise trace-mass control. None is used here.

Named OTHER-account result actually applied:

- `fleet02/B04`, canonical report `yspennstate/math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T122057Z-01c809a1/REPORT.md`, blob `fa94d255369a9ad6475ebc66b2f158066e588a8b`.
- Its theorem `QFORM-SHIFTED-SQUARE-PRODUCT-REARRANGEMENT-v1` proves, for independent density-`<=1` `U,V,W`, nonzero `a,gamma`, and arbitrary constants `alpha,beta`,

  `||p_{a(W-alpha U-beta V)^2-gamma UV}||_infinity <= 4 sqrt(2)/sqrt(|a gamma|)`.

- The key exact ingredient used below is its one-sided bathtub inequality: if `H` is a probability density with `0<=H<=M`, then

  `integral_0^infinity s^(-1/2) H(s) ds <= 2 sqrt(M)`.

The present run first proves that the partner estimate is unchanged by an **arbitrary one-factor perturbation**. That extension is then applied to a Schur form with one vanishing diagonal entry.

## 3. Arbitrary one-factor perturbations cost nothing

### Lemma 3.1 — `QFORM-SHIFTED-SQUARE-ONE-FACTOR-v1`

Let `U,V,W` be independent real random variables with densities bounded by one. Let `a,gamma` be nonzero, `alpha,beta` be arbitrary real constants, and let `h:R->R` be measurable and finite almost surely under `U`. Then

`T = a(W-alpha U-beta V)^2 - gamma U V + h(U)`

has an essentially bounded density satisfying

`boxed( ||p_T||_infinity <= 4 sqrt(2)/sqrt(|a gamma|). )`       (3.1)

The same statement allows arbitrary affine terms, because constants translate the output and a linear term in `V` can be removed by translating `U`, while linear terms in `U` can be absorbed into `h`.

#### Proof

Reflect the output if necessary and assume `a>0`. Condition on `(U,V)=(u,v)`. Translation of `W` preserves the density cap. The pushforward of a density-`<=1` variable by `a w^2` has a density bounded by

`a^(-1/2) s^(-1/2) 1_{s>0}`.                                  (3.2)

Hence a density version of `T` obeys, for every `t`,

`p_T(t)
 <= a^(-1/2) integral f_U(u) f_V(v)
      (t-h(u)+gamma u v)_+^(-1/2) du dv`.                       (3.3)

Fix `u!=0`. The random variable

`t-h(u)+gamma u V`

has density bounded by

`M_u=1/(|gamma u|)`.                                            (3.4)

The important point is that the arbitrary quantity `h(u)` is only a level translation and does not change this cap. Applying the partner's exact one-sided bathtub inequality to the inner integral gives

`int f_V(v)(t-h(u)+gamma u v)_+^(-1/2)dv
 <=2/sqrt(|gamma u|)`.                                         (3.5)

Therefore

`p_T(t)
 <= 2/sqrt(|a gamma|) integral f_U(u)|u|^(-1/2)du`.             (3.6)

Among all probability densities bounded by one, the last integral is maximized by filling the unit-measure set nearest zero. Thus

`int f_U(u)|u|^(-1/2)du
 <= int_{-1/2}^{1/2}|u|^(-1/2)du
 =2 sqrt(2)`.                                                   (3.7)

Equations (3.6)-(3.7) give (3.1). The null set `u=0` causes no issue. The displayed conditional density bound also proves absolute continuity. QED.

### Why this is a genuine extension of the partner theorem

The extra term `h(U)` may be quadratic, discontinuous, or otherwise arbitrary; no derivative or Fourier decay of `h` is used. The reason is structural: the product variable `V` remains affine with slope `gamma u` after `U=u` is fixed. This is exactly what fails once independent self-terms are placed on **both** product factors.

## 4. One vanishing Schur diagonal: exact determinant identity

Let

`B = [[a,u,v],
      [u,b,c],
      [v,c,d]]`                                                (4.1)

be a real symmetric invertible `3x3` matrix and suppose the first `2x2` principal minor vanishes:

`Delta_12 := ab-u^2 =0`.                                       (4.2)

Assume first `a!=0`; the `a=0` boundary is handled below. Define

`kappa = c-uv/a`,
`tau   = d-v^2/a`.                                              (4.3)

Completing the square in the first original coordinate gives the exact identity

`[X,Y,Z] B [X,Y,Z]^T
 = a(X+(u/a)Y+(v/a)Z)^2
   +2 kappa YZ + tau Z^2`,                                     (4.4)

because the `Y^2` coefficient in the Schur complement is

`b-u^2/a=0`.                                                    (4.5)

Moreover

`det B
 = a det([[0,kappa],[kappa,tau]])
 = -a kappa^2`.                                                 (4.6)

Thus invertibility forces `kappa!=0`.

Arbitrary affine terms do not spoil (4.4). After the first completion they leave only affine terms in `Y,Z`; since `kappa!=0`, separate constant translations of `Y` and `Z` remove those terms while preserving independence and the density caps. The completed-square center changes only by affine constants. Equivalently, one may absorb the `Z`-only terms into the function `h` in Lemma 3.1.

## 5. Deterministic coefficient bound on the zero-minor surface

### Theorem 5.1 — `QFORM-ZERO-PRINCIPAL-MINOR-COEFFICIENT-v1`

Let `X,Y,Z` be independent with densities bounded by one, let `B` be invertible and symmetric, and assume some physical `2x2` principal minor of `B` is zero. If for that pair the first nonzero endpoint diagonal is `a` and `kappa` is defined by (4.3), then for the corresponding quadratic polynomial, including arbitrary affine terms,

`boxed( ||p_Q||_infinity <= 4/sqrt(|a kappa|). )`               (5.1)

Equivalently, using (4.6),

`boxed( ||p_Q||_infinity <=4 (|a det B|)^(-1/4). )`             (5.2)

If both endpoint diagonals are nonzero, one may take the better endpoint. In the notation (4.1), pivoting instead on `b` gives

`kappa_2 = v-u c/b`,                                           (5.3)

and the two pivot parameters satisfy

`|a kappa| = sqrt(|a det B|)`,
`|b kappa_2| = |u kappa| = sqrt(|b det B|)`.                    (5.4)

Hence

`boxed(
 ||p_Q||_infinity
 <=4 ( |det B| max(|a|,|b|) )^(-1/4)
)`                                                              (5.5)

whenever both endpoints are available.

#### Proof

Use (4.4) and apply Lemma 3.1 with

`W=X`, `U=Z`, `V=Y`, `gamma=-2 kappa`,
`h(Z)=tau Z^2`                                                  (5.6)

(after the harmless coordinate translations needed for affine terms). Then

`4 sqrt(2)/sqrt(|a(-2 kappa)|)=4/sqrt(|a kappa|)`,              (5.7)

which is (5.1). Formula (5.2) follows from (4.6).

For the second endpoint, (4.2) gives `b=u^2/a`; hence

`b kappa_2=bv-u c
            =-(u/a)(a c-u v)
            =-u kappa`,                                        (5.8)

which proves (5.4)-(5.5). QED.

### Ambient conditioning

If `B` is a physical principal triple of a larger symmetric matrix `A`, condition on every coordinate outside this triple. Outside couplings create only affine terms in the selected variables. The bound above is uniform in those affine coefficients, so averaging over the outside variables preserves it. No independence after a spectral rotation is asserted.

## 6. Spectral threshold closes the entire exact-zero-minor 3D class

The preceding coefficient estimate still appears to depend on a physical coefficient. Under the **three-dimensional target spectral hypothesis**, that dependence can be eliminated exactly by looking at both endpoints of the zero minor.

### Theorem 6.1 — `QFORM-ZERO-PRINCIPAL-MINOR-UNIVERSAL-v1`

Let `B` be a real symmetric `3x3` matrix whose three eigenvalues satisfy

`|lambda_1(B)|,|lambda_2(B)|,|lambda_3(B)| >=1`.                (6.1)

Assume at least one physical `2x2` principal minor of `B` vanishes. Then for every independent real `X,Y,Z` with densities bounded by one,

`boxed(
 ||p_{[X,Y,Z]B[X,Y,Z]^T}||_infinity
 <=4*2^(1/4)
 <4.757.
)`                                                              (6.2)

The same bound holds with arbitrary affine terms. Only existence of an essentially bounded density is claimed; continuity is not established by this proof.

#### Proof

Relabel so that `Delta_12=0`. If `a=0`, then (4.2) forces `u=0`; invertibility forces `b!=0`, so interchange indices `1,2`. Thus assume `a!=0`.

Put

`M=B^{-1}`.                                                     (6.3)

By Cramer's rule and (4.2),

`M_33=Delta_12/det B=0`.                                       (6.4)

Using (4.3)-(4.6), direct cofactor calculation gives

`M_23=1/kappa`,
`M_13=-u/(a kappa)`,
`det M=-1/(a kappa^2)`.                                        (6.5)

Write

`C=M_13`, `E=M_23`.                                             (6.6)

The spectral assumption (6.1) says every singular value of the symmetric matrix `M` is at most one. If

`sigma_1(M)>=sigma_2(M)>=sigma_3(M)>0`,

then

`|det M|=sigma_1 sigma_2 sigma_3 <=sigma_3`.                    (6.7)

For every unit vector, and in particular `e_3`,

`||M e_3||_2 >=sigma_3 >=|det M|`.                              (6.8)

By (6.4),

`M e_3=(C,E,0)^T`,

so (6.8) yields

`max(|C|,|E|)
 >= ||M e_3||_2/sqrt(2)
 >= |det M|/sqrt(2)`.                                          (6.9)

Now (6.5) converts the inverse entries into the **two exact pivot parameters**:

`|E|/|det M| = |a kappa|`,
`|C|/|det M| = |u kappa|`.                                     (6.10)

Consequently

`max(|a kappa|,|u kappa|) >=1/sqrt(2)`.                         (6.11)

If `b!=0`, the second quantity is exactly `|b kappa_2|` by (5.8), so choose the endpoint with the larger parameter and apply Theorem 5.1. If `b=0`, then `u=0`, the second quantity vanishes, and (6.9) in fact gives `|a kappa|>=1`, so the first endpoint alone is even stronger. In every case an available endpoint satisfies

`|pivot * cross|>=1/sqrt(2)`.                                  (6.12)

Substituting (6.12) into (5.1) gives

`||p_Q||_infinity
 <=4/sqrt(1/sqrt(2))
 =4*2^(1/4)`,                                                   (6.13)

which proves the theorem. QED.

## 7. The `1/sqrt(2)` structural constant is sharp for this argument

The matrix

`M_* = [[1/2,-1/2,1/sqrt(2)],
        [-1/2,1/2,1/sqrt(2)],
        [1/sqrt(2),1/sqrt(2),0]]`                               (7.1)

satisfies

`M_*^2=I`, `det M_*=-1`, `spec(M_*)={1,1,-1}`,                  (7.2)

and its upper-left principal `2x2` determinant is zero. Since `M_*^{-1}=M_*`, we may take `B=M_*`. For the first endpoint,

`a=1/2`, `u=-1/2`, `kappa=sqrt(2)`,                             (7.3)

so

`|a kappa|=1/sqrt(2)`,                                         (7.4)

and symmetry gives the same value at the second endpoint. Thus (6.11) is sharp if one uses only contraction of `B^{-1}` plus the vanishing-minor identity. Improving the final numerical constant requires more information about the input laws or the quadratic geometry, not merely a stronger version of (6.9).

## 8. Explicit genuinely rotated indefinite target with a nonzero residual self-term

Consider

`B_0 = [[1,-1,2],
        [-1,1,2],
        [2,2,0]]`.                                              (8.1)

Its first principal `2x2` minor is zero. The spectrum is exactly

`spec(B_0)={2, 2 sqrt(2), -2 sqrt(2)}`,                         (8.2)

so all three eigenvalues have modulus at least two and the form is genuinely indefinite and non-diagonal. The quadratic form is

`Q_0=X^2+Y^2-2XY+4XZ+4YZ`.                                    (8.3)

Here

`a=1`, `u=-1`, `v=2`, `c=2`, `d=0`,
`kappa=4`, `tau=-4`,                                            (8.4)

and the exact decomposition is

`boxed(
 Q_0=(X-Y+2Z)^2+8YZ-4Z^2.
)`                                                              (8.5)

The `-4Z^2` term is precisely an extra one-factor perturbation not present in the partner's original shifted-square/product theorem. Lemma 3.1 pays it with no cost. The coefficient bound therefore gives the explicit estimate

`boxed( ||p_{Q_0}||_infinity <=2. )`                            (8.6)

for **every** independent choice of the three input laws with densities bounded by one.

A direct exact check gives `det B_0=-16`; the eigenvalue decomposition in (8.2) follows because `(1,-1,0)` is an eigenvector of eigenvalue `2`, while on the span of `(1,1,0)/sqrt(2)` and `(0,0,1)` the matrix is `[[0,2sqrt(2)],[2sqrt(2),0]]`.

## 9. First essential missing implication

The exact zero-minor surface is now paid. The next local/global bridge is:

> **`QFORM-NEAR-ZERO-PRINCIPAL-MINOR-STABILITY-v1`.** Starting from
> `Q=aW^2+sY^2+2kappa YZ+tau Z^2` with `s=Delta_12/a`, derive a product-preserving estimate that remains bounded as `s->0` and then aggregate such near-zero-minor information over original-coordinate pairs without paying the inverse of one tiny physical minor.

The obstacle is precise. Lemma 3.1 allows arbitrary self-interaction on one product factor, but when `s!=0` both product factors carry self-quadratics. A naive scalar-pivot Schur estimate reintroduces a factor `(|a det B|)^(-1/4)`, which can diverge even while the three spectral eigenvalues remain large; fleet02/B04's Fourier-frame family gives an explicit version of that obstruction. A fixed-principal-block dichotomy is also disallowed by the live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` correction. The required next step must therefore be a stable rearrangement or an aggregate bank/wedge inequality, not selection of one tiny pivot.

This dovetails with the latest partner result `fleet02/B04 / QFORM-RANK3-PIVOT-TRANSFER-v1`, whose first unpaid implication is `QFORM-HIGH-LEVERAGE-AGGREGATION`.

## 10. Scope, checks, and honest status

Symbolic exact checks performed in this run:

- for (8.1), `det B_0=-16` and `spec(B_0)={2,2sqrt(2),-2sqrt(2)}`;
- for (7.1), `M_*^2=I`, `det M_*=-1`, and `spec(M_*)={1,1,-1}`.

These checks support the displayed algebra; the proofs above are exact and do not depend on numerics.

Proved:

1. arbitrary one-factor perturbations preserve the partner shifted-square/product rearrangement bound;
2. every invertible physical `3x3` block with one zero `2x2` principal minor obeys the explicit coefficient bounds (5.1)-(5.5);
3. if that entire `3x3` block itself satisfies the target three-eigenvalue threshold, the coefficient dependence disappears and the universal bound `4*2^(1/4)<4.757` follows;
4. the explicit rotated indefinite target (8.1) has the stronger uniform bound `2`;
5. all these local bounds survive outside conditioning and arbitrary affine terms.

Not proved:

1. the full arbitrary-dimensional QFORM conjecture;
2. a dimension-free theorem forcing or aggregating an exact/near-zero physical principal minor from the spectral hypothesis;
3. continuity of the densities in the new dependent shifted-square branches. Only existence of an essentially bounded density is established.

Honest outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`.
