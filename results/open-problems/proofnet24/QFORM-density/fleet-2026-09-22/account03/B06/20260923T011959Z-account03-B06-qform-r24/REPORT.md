# account03/B06 r24 — Fractional curved-fiber payment with retained cross tail

**Run:** `20260923T011959Z-account03-B06-qform-r24`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** supporting target-relevant theorems proved; full QFORM conjecture remains OPEN; continuity is not proved by the outer-square conclusions below.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and scope

The owner target is unchanged: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `Q=X^TAX`, or give a valid counterexample. No moments, support regularity, log-concavity, Gaussianity, diagonal-basis independence, or sign assumption is used here.

This run addresses a specific B06 debt left by the exact-rank-two cross-bank arguments: extra cross singular directions must not be discarded merely to recover an exact rank-two normal form. The mechanism below keeps the full cross block, aggregates its curved two-dimensional volume before any reciprocal payment, and only then spends a genuine original-coordinate square.

Fresh corrections used throughout include: law-uniform pointwise quadratic-phase decay is false; unrestricted spectral-fiber suprema can lose dimension; arbitrary-joint coarea and positive conditional-projection moments are false; a single tiny physical minor cannot be selected before aggregation; and extra cross curvature cannot simply be deleted from the phase.

## 2. Source-valid analytic inputs

Two completed inputs are used at their proved scopes.

1. **Regularized determinant / fractional graph estimate.** From
   `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`,
   `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`:
   for a full quadratic form with an original-coordinate cross block `B=A[I,J]`, arbitrary self blocks and outside couplings, and `1<=q<2`, if the coordinate leverage of the projection onto `range(B)` on one side is at most `q/2`, then

   `|phi_R(t)| <= det(I + 2q t^2 BB^T/(pi^2 e^2))^(-1/(4q)).`       (2.1)

   The same source, together with the one-scale refinement at
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   gives for any `rho>0`

   `K_rho=BB^T(rho^2 I+BB^T)^(-1)`, `theta=tr K_rho`, `D=det(I+BB^T/rho^2)`,

   and, whenever `max_i(K_rho)_ii<=q/2`,

   `|phi_R(t)| <= D^(-1/(4q)) [L_q/(2 rho |t|)]^(theta/(2q)),`

   where `L_q=pi e sqrt(2/q)`. This pointwise envelope is a consequence of the product-space graph argument, not the refuted one-dimensional law-uniform Fresnel estimate.

2. **Dependence-safe square kernel.** From account04/B18,
   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`:
   after completing a square in an ORIGINAL independent coordinate with coefficient `a!=0`,

   `Q=R+a V_R^2`,

   the conditional density of `V_R` remains bounded by one and the proof gives the domination

   `p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du.`   (2.2)

   No independence between `R` and `V_R` is asserted or needed.

The designated partner `account04/B06` had no completed current-QFORM canonical artifact at the fresh lookup, so none is fabricated. The compatible completed account04/B18 result is applied below to an actual displayed inequality.

## 3. Aggregate two-curvature receiver in L3

For a real cross block `B`, define

`Delta_2(B)=e_2(BB^T)=sum_(r<s) sigma_r(B)^2 sigma_s(B)^2.`

By Cauchy--Binet this is also the sum of the squares of **all physical 2x2 minors** of `B`. Thus `Delta_2` is exactly an aggregate curved two-volume currency; no individual minor is chosen.

### Theorem 3.1 — `QFORM-CROSS-E2-FRACTIONAL-L3-v1`

Let `R` be an arbitrary quadratic form in independent cap-one original coordinates. Suppose it has an original-coordinate cross block `B` between disjoint coordinate banks. Let `1<=q<3/2`, and suppose the coordinate leverage of `range(B)` on one side is at most `q/2`. If `Delta_2=Delta_2(B)>0`, then `R` has an `L^3` density and

`||p_R||_3 <= [3^(1/6)e^(2/3)/(4 q^(1/3))]
               BETA(1/4, 3/(8q)-1/4)^(2/3) Delta_2^(-1/6).`    (3.1)

All additional cross singular values, self quadratic terms, affine terms, signs, and outside couplings are retained.

#### Proof

From (2.1), with

`c_q=2q/(pi^2 e^2)`,

we have

`|phi_R(t)| <= det(I+c_q t^2 BB^T)^(-1/(4q)).`

For nonnegative eigenvalues `x_r=sigma_r(B)^2`, the determinant expansion gives

`det(I+c_q t^2 BB^T)
 >= 1 + c_q^2 t^4 sum_(r<s) x_r x_s
 = 1+c_q^2 Delta_2 t^4.`

Hence

`|phi_R(t)|^(3/2)
 <= (1+c_q^2 Delta_2 t^4)^(-3/(8q)).`

Because `q<3/2`, the exponent `3/(8q)` is strictly larger than `1/4`. The beta integral yields

`int_R |phi_R(t)|^(3/2) dt
 <= [pi e/(2 sqrt(2q))]
    BETA(1/4,3/(8q)-1/4) Delta_2^(-1/4).`                    (3.2)

With the convention `hat f(t)=int e^(itx)f(x)dx`, inverse sharp Hausdorff--Young at exponent `3/2` gives

`||p_R||_3
 <= [3^(1/6)/(2 pi^(2/3))]
    (int |phi_R|^(3/2))^(2/3).`

Substitution of (3.2) simplifies exactly to (3.1). QED.

At `q=1`, the numerical coefficient in (3.1) is finite. The theorem is tail-monotone: adding extra singular values to `B` only increases the regularized determinant and `Delta_2`; no exact-rank-two reduction is used.

## 4. Fractional ridge receiver without an ordinary range-leverage gate

The one-scale regularized estimate also gives a tail-stable version useful when the ordinary range projection is localized.

### Theorem 4.1 — `QFORM-RIDGE-FRACTIONAL-L3-v1`

Fix `1<=q<=2` and `rho>0`. Put

`K=BB^T(rho^2I+BB^T)^(-1)`, `theta=tr K`, `D=det(I+BB^T/rho^2)`.

Assume

`max_i K_ii <= q/2`,   and   `theta > 4q/3`.                    (4.1)

Then `R` has an `L^3` density with

`||p_R||_3
 <= [3^(1/6)e^(2/3)/(2^(2/3) q^(1/3))]
    [3theta/(3theta-4q)]^(2/3)
    D^(-1/(3theta)) rho^(-2/3).`                              (4.2)

#### Proof

The source-valid ridge envelope can be written

`|phi_R(t)| <= min(1,(t_0/|t|)^beta)`,

where

`beta=theta/(2q)`,
`t_0=L_q/(2rho) D^(-1/(2theta))`.

Raising to `3/2` gives an integrable tail precisely when

`(3/2)beta=3theta/(4q)>1`,

which is the second condition in (4.1). Therefore

`int |phi_R|^(3/2)
 <= 2 t_0 * [3theta/(3theta-4q)]
 = [L_q/rho] D^(-1/(2theta)) [3theta/(3theta-4q)].`

Apply inverse Hausdorff--Young exactly as in Section 3 and simplify. QED.

This is the fractional analogue of the source's `theta>2q` `L^1`-Fourier density criterion: an outer square only needs `L^3`, so the effective-dimension threshold drops from `2q` to `4q/3`.

## 5. The L3-to-square transducer

The account04/B18 kernel (2.2) combines with any `L^3` base density.

### Lemma 5.1 — `QFORM-L3-HALF-RIESZ-TO-LINFINITY-v1`

If `p` is a probability density with `||p||_3=M`, then

`sup_t int_0^infinity p(t-u)u^(-1/2)du
 <= [8/3^(3/4)] M^(3/4).`                                    (5.1)

#### Proof

Split at `U>0`. Holder with exponents `3` and `3/2` gives

`int_0^U p(t-u)u^(-1/2)du <= 4^(2/3) M U^(1/6)`.

The far part is at most `U^(-1/2)` because `p` has mass one. Optimizing

`4^(2/3) M U^(1/6)+U^(-1/2)`

gives `U^(2/3)=3/(4^(2/3)M)` and exactly (5.1). QED.

Combining (2.2) and (5.1) is a genuine application of the completed account04 result:

`||p_Q||_infinity <= [8/3^(3/4)] |a|^(-1/2) ||p_R||_3^(3/4).` (5.2)

No post-completion independence is introduced.

## 6. Main B06 endpoint: aggregate e2 before the reciprocal power

### Theorem 6.1 — `QFORM-CROSS-E2-OUTER-SQUARE-v1`

Under the hypotheses of Theorem 3.1, suppose `R` is the Schur residual obtained by completing a square in an original coordinate with coefficient `a!=0`. Then

`||p_Q||_infinity
 <= C_q |a|^(-1/2) Delta_2(B)^(-1/8),`                         (6.1)

where

`C_q = 2^(3/2)e^(1/2)3^(-5/8) q^(-1/4)
       BETA(1/4,3/(8q)-1/4)^(1/2).`                           (6.2)

For `q=1`,

`C_1 = 7.9667094489... < 7.967.`                              (6.3)

Thus the complete sum of squared physical `2x2` minors is paid **before** the reciprocal exponent `-1/8` is taken. This is a weighted replacement for the invalid strategy of selecting one minor or integrating an unrestricted fiber supremum.

#### Proof

Insert (3.1) into (5.2). The powers simplify to `Delta_2^(-1/8)` and the scalar coefficient to (6.2). QED.

### Concrete splice with the preceding B06 transverse currency

In the preceding B06 transverse state the residual cross block `H` satisfies

`h_1 h_2 > (4/5) G^2`

for the inherited curvature scale `G`. Hence, without deleting any extra singular directions,

`Delta_2(H) >= h_1^2 h_2^2 > (16/25)G^4.`

If one side's cross-range leverage is at most `1/2`, Theorem 6.1 with `q=1` gives

`boxed( ||p_Q||_infinity < 8.424 / sqrt(|a|G) ).`              (6.4)

The bicolooop survivor has deliberately failed this ordinary leverage gate; (6.4) closes the complementary aggregate-e2 chamber and shows exactly where the remaining geometry begins.

## 7. Arbitrary extra spectrum: a three-cross-singular-value endpoint below 25

The ridge theorem gives a leverage-free payment as soon as a genuine third cross singular value is quantitatively present.

### Corollary 7.1 — `QFORM-THIRD-CROSS-SINGULAR-SQUARE-v1`

Suppose the Schur residual has an original-coordinate cross block `B` with

`sigma_3(B) >= s >0`.

Then

`boxed( ||p_Q||_infinity
       <= 12 sqrt(2) 3^(1/8) e^(1/4) / sqrt(|a|s)
       < 25 / sqrt(|a|s). )`                                 (7.1)

There is no leverage hypothesis and no bound on the number, size, or signs of the remaining spectral directions.

#### Proof

Use Theorem 4.1 with `q=2` and

`rho=s/sqrt(24)`.

The leverage condition is automatic because `K<=I=qI/2`. Each of the first three ridge eigenvalues is at least `24/25`, so

`theta >= 72/25 > 8/3 =4q/3.`

Since `log D>=theta`, (4.2) followed by (5.2) gives

`||p_Q||_infinity
 <= [4 sqrt(2)e^(1/4)3^(-5/8)q^(-1/4)]
    sqrt(3theta/(3theta-4q)) / sqrt(|a|rho).`

The right side decreases with `theta`, so insert `q=2`, `theta=72/25`, `rho=s/sqrt(24)`. Exact simplification gives

`12 sqrt(2)3^(1/8)e^(1/4)/sqrt(|a|s)=24.99827384.../sqrt(|a|s)`.

QED.

For the surviving B06 higher-rank cross block, this gives a clean fixed-scale dichotomy for any inherited curvature scale `G`: either

`sigma_3(B) >= G/64`,

in which case

`||p_Q||_infinity < 200/sqrt(|a|G)`,

or

`||B-B_(2)||_op=sigma_3(B)<G/64`,

where `B_(2)` is the best rank-two approximation. Thus the unpaid branch can be confined to an explicit operator-norm tube around rank two without ever pretending that the tail is zero.

## 8. Why this is compatible with the live corrections

* No spectral rotation is used to claim independence. All banks and the outer square are original-coordinate objects.
* The proof does not use law-uniform scalar van der Corput/Fresnel decay. The characteristic estimates come from the source-valid product-space regularized determinant theorem.
* `Delta_2` is an aggregate Cauchy--Binet currency. No largest local minor is selected before taking a reciprocal power.
* Extra cross singular values are retained throughout. In Sections 3 and 6 they can only help the determinant and `Delta_2`; in Section 7 they are explicitly included in the ridge trace.
* No unrestricted fiber maximum, arbitrary-joint coarea bound, or conditional projection-density moment is used.
* The square step is dependence-safe by the account04/B18 conditional-mixture argument.

## 9. Remaining implication

The full target is still OPEN. The current B06 debt is now narrower:

`QFORM-DOUBLE-WEDGE-DIFFUSE-RANK2-TUBE-STABILITY-v1`.

After the previous bicolooop/star squeeze, the hard chamber has two-sided diffuse incident exterior directions. By Corollary 7.1 one may additionally assume, at a fixed universal cost, that the retained cross block lies in an explicit operator-norm tube around rank two. The next step is to combine those two facts **before inversion**: construct a physical/grouped product packet whose aggregate `Delta_2` has one-side range/ridge leverage below the fractional threshold, or prove a perturbative version of Theorem 6.1 in which the small nonzero tail is absorbed without fragment-count or conditional-density losses.

Zero/near-zero outer pivots and the eventual payment of the scale `|a|G` across all chambers remain separate target-level debts. A complete QFORM proof also requires arbitrary higher-rank matrices and two independent end-to-end reviews. Universal continuity is not established by the outer-square conclusions above.
