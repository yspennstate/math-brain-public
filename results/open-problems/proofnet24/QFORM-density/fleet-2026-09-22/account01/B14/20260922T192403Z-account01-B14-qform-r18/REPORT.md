SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-22T19:24:03Z.
attacking: exact no-tax translation/localization through range-aligned active blocks, then aggregate the canonical diffuse three-bank obstruction before determinant inversion.

# account01/B14 — exact extreme-product localization and range-aligned bank aggregation

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization  
**Run:** `20260922T192403Z-account01-B14-qform-r18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM`  
**Full QFORM:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The source control was read first at `yspennstate/math-research-brain@09c86b976b555738450505507b0a2bca107a535c`; immediately before publication it had advanced to owner-control revision `2026-09-22.14`. The sole target remains:

> for every dimension, every product law with independent real coordinates of densities at most one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal output-density bound for `X^T A X`, or give a valid counterexample.

The live correction set is respected. In particular this report does not use the false arbitrary-joint 3D coarea lemma, the false positive conditional-projection moment, post-rotation independence, a universal physical minor, a bounded-diameter reduction, or law-uniform pointwise quadratic Fourier decay.

## 1. Completed named partner result actually consumed

Assigned partner `account02/B14`, run `20260922T191035Z-account02-B14-QFORM-r17`, canonical proof

`yspennstate/math-open-problems@51c319713bf7b8f8bff3c08e8b6bae462fc5b9fd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T191035Z-account02-B14-QFORM-r17/REPORT.md`.

For

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`

it proves exactly:

1. `spec_nonzero(A_m)={1,1,-1}`;
2. every physical active set `S` of size `k` has
   `s_3(A_m[S,S]) <= (k-1)/(2m)`;
3. every nonzero physical principal `3x3` determinant has magnitude `m^(-2)`, so every randomized principal-triple selector obeys
   `E |det A_m[S,S]|^(-1/3)=m^(2/3)`;
4. nevertheless the full third-compound squared-minor mass is one and asymptotically all of it lies in overlap-one cross minors:
   `M_1=((m-1)/m)^2 ->1`.

Thus selecting a local determinant and then inverting it is provably the wrong order on this target-valid family. Section 5 below applies the partner result to an actual uniform density inequality and pays the same family by aggregating the two coordinate banks first.

## 2. Exact extreme-product localization with no support tax

Let

`D={f:R-> [0,1] measurable : integral f =1}`.

For any bounded measurable payoff `0<=Phi<=1`, define

`S(Phi)=sup_(f_1,...,f_n in D) integral Phi(x) prod_i f_i(x_i) dx`.

### Theorem 2.1 — `QFORM-EXACT-EXTREME-PRODUCT-LOCALIZATION-v1`

One has the exact equality

`S(Phi)=sup_(|E_i|=1) integral_(E_1 x ... x E_n) Phi(x) dx`.      (2.1)

Moreover the same supremum is obtained if every `E_i` is required to be a bounded finite union of intervals of total length exactly one. No uniform bound on the number of intervals or on their diameter is asserted or needed.

#### Proof

Fix all coordinates except coordinate `i`. The functional in `f_i` is

`integral g_i(x_i) f_i(x_i) dx_i`,

where `0<=g_i<=1`. By the bathtub principle,

`sup_(f in D) integral g_i f = sup_(|E|=1) integral_E g_i`.      (2.2)

Indeed, writing `g_i^*` for the decreasing rearrangement, every `f in D` satisfies

`integral g_i f <= integral_0^1 g_i^*(s) ds`,

and superlevel sets, with an arbitrary measurable subset of the threshold level if necessary, realize or arbitrarily approximate the right side. Sequentially replacing `f_1,...,f_n` by indicators cannot lower the value, up to an arbitrarily small total error. The reverse inequality is immediate because `1_E in D` when `|E|=1`. This proves (2.1).

Now let `E` have measure one. By regularity of Lebesgue measure, for every `delta>0` there is a bounded finite union of intervals `F` with `|F|=1` and

`|E triangle F|<delta`.                                      (2.3)

For products, telescope the difference:

`|prod_i 1_(E_i)-prod_i 1_(F_i)|`

and integrate one coordinate at a time. Since every other factor has integral one,

`| integral Phi prod_i1_(E_i)- integral Phi prod_i1_(F_i) |`
` <= sum_i |E_i triangle F_i|`.                              (2.4)

Taking all symmetric differences arbitrarily small proves the finite-fragment statement.

QED.

### Corollary 2.2 — exact preservation of the QFORM density constant

For a fixed quadratic-affine polynomial

`q(x)=x^T A x + ell^T x + c`,

put

`K(q)=sup_(f_i in D) sup_(t in R,h>0) h^(-1) P{q(X) in [t,t+h]}`.

Then `K(q)` is unchanged if the outer supremum over product laws is restricted to independent uniforms on arbitrary measurable unit-measure sets, or further to bounded finite unions of intervals of total length one.

Therefore any small-ball estimate with constant `C` proved uniformly on the finite-fragment indicator subclass transfers to **all** independent cap-one laws with exactly the same `C`. This is the requested no-moment/no-diameter/no-fragment-count localization statement. It also preserves arbitrary translations because `ell,c` were never restricted.

This does not contradict the live bounded-diameter and fixed-fragment-count falsifiers: the approximating unions may have arbitrarily many components at arbitrarily distant locations.

## 3. Exact affine quotient: only kernel leakage survives outside conditioning

Let a physical coordinate set `S` be active and write, after reordering coordinates,

`A=[[B,C],[C^T,D]]`,

where `B=A_SS`. Condition on all outside original coordinates `Z=z`. The active polynomial is

`q_z(x)=x^T B x +2(Cz)^T x + z^T D z`.                       (3.1)

Let `B^dagger` be the Moore-Penrose pseudoinverse and let

`P_R=BB^dagger`, `P_K=I-P_R`,
`h(z)=B^dagger C z`, `r(z)=P_K C z`.

Since `B` is symmetric, `Ran(B)` is orthogonal to `Ker(B)`. With `y=x+h(z)`, direct expansion gives the **exact identity**

`q_z(x)= y^T B y +2 r(z)^T y + c(z)`,                       (3.2)

where

`c(z)= z^T D z - h(z)^T B h(z)`.                            (3.3)

The shift `x -> y=x+h(z)` is coordinatewise deterministic after conditioning, hence it preserves independence and every density cap. Thus every outside-induced affine term in `Ran(B)` is free; the only possible translation obstruction is the component injected into `Ker(B)`.

### Theorem 3.1 — `QFORM-RANGE-ALIGNED-NO-TAX-LOCALIZATION-v1`

Assume

`Ran(C) subset Ran(B)`, equivalently `P_K C=0`.                (3.4)

Suppose the pure active quadratic form `Y^T B Y` has density at most `K_B` for **every** independent cap-one law on the active original coordinates. Then the full form `X^T A X` has density at most the same `K_B`, with no loss whatever from:

- the number of outside coordinates;
- the outside block `D`;
- the size of the cross coupling `C`;
- translations generated by conditioning;
- unbounded supports, moments, tails, support diameter, or fragment count.

#### Proof

Under (3.4), `r(z)=0`. Conditional on each deterministic `z`, (3.2) is a coordinatewise translate of the pure form plus a scalar output shift, so its conditional density is at most `K_B`. Averaging the conditional densities over the arbitrary outside product law preserves the same essential-supremum bound.

QED.

This theorem is useful even when `B` is singular. It identifies the exact unpaid localization object in the general singular case as the kernel-leakage map

`P_(Ker B) C`.                                               (3.5)

No norm of the range-aligned part of `C` matters.

## 4. Three disjoint rank-one banks: a target-level full-matrix branch

Partition the active original coordinates into disjoint nonempty banks

`S=I_1 disjoint_union ... disjoint_union I_R`.

Assume

`B= direct_sum_(r=1)^R lambda_r u_r u_r^T`,                  (4.1)

where each `u_r` is a unit vector supported on `I_r`. Suppose at least three coefficients satisfy `|lambda_r|>=1`. Assume the outside coupling is range-aligned:

`Ran(C) subset Ran(B)=span{u_1,...,u_R}`.                    (4.2)

We use the standard sharp Rogozin-Ball scalar projection bound:

> if `Y=sum_i a_i X_i`, the `X_i` are independent with densities at most one, and `sum_i a_i^2=1`, then `Y` has density at most `sqrt(2)`.

This is exactly the cap-one bank-compression mechanism also used in the current rank-three fleet work.

### Theorem 4.1 — `QFORM-RANGE-ALIGNED-DISJOINT-BANK-v1`

Under (4.1)-(4.2),

`||p_(X^T A X)||_infinity <= 2 pi`.                          (4.3)

If one of the two same-sign large banks can be chosen to be a singleton original coordinate, the bound improves to

`pi sqrt(2)`.                                                 (4.4)

#### Proof

By Theorem 3.1 it suffices to bound the pure active form. Put

`Y_r=u_r^T X_(I_r)`.

Because the banks use disjoint original coordinates, the `Y_r` are independent. Each has density cap

`M_r<=sqrt(2)`,                                               (4.5)

and if `I_r` is a singleton then `M_r<=1`.

Among any three real `lambda_r` with `|lambda_r|>=1`, two have the same sign. Choose such `r,s`. A deterministic translation of `Y_r` does not change `M_r`; for completeness, if `lambda>0` and `W=lambda(Y+a)^2`, then for `w>0`

`p_W(w)`
`=[p_Y(-a+sqrt(w/lambda))+p_Y(-a-sqrt(w/lambda))]`
` /(2 sqrt(lambda w))`
`<= M / sqrt(lambda w)`.                                    (4.6)

For `lambda<0`, reflect the output. Therefore the convolution of the two same-sign square terms obeys

`||p_(lambda_r(Y_r+a_r)^2 + lambda_s(Y_s+a_s)^2)||_infinity`
`<= (M_r M_s)/sqrt(|lambda_r lambda_s|)`
`   * integral_0^t [u(t-u)]^(-1/2) du`
`= pi M_r M_s / sqrt(|lambda_r lambda_s|)`
`<= 2 pi`.                                                    (4.7)

All remaining bank terms are independent of this pair. Convolution with any probability law cannot increase an `L^infinity` density norm, so (4.3) follows. If one selected member is a singleton, `M_r M_s<=sqrt(2)`, giving (4.4). Range-aligned outside variables are then restored by Theorem 3.1 with exactly zero loss.

QED.

This is a genuine full-matrix theorem: the outside block `D` may have arbitrary rank, signs and magnitudes, and `C` may be arbitrarily large. The only structural condition is that the outside linear forcing lands in the already-paid rank-one bank span.

## 5. Partner obstruction paid by an actual aggregate inequality

Return to the assigned partner's canonical diffuse family

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`.

Write

`U_m=m^(-1/2) sum_(i=1)^m X_i`,
`V_m=m^(-1/2) sum_(j=1)^m Y_j`.

The three coordinate groups are disjoint, so `X_0,U_m,V_m` are independent. Rogozin-Ball gives

`||p_(U_m)||_infinity, ||p_(V_m)||_infinity <=sqrt(2)`        (5.1)

for every cap-one product input, independently of `m`, support location, fragmentation or moments. The quadratic form is exactly

`Q_m=X_0^2+U_m^2-V_m^2`.                                    (5.2)

The positive same-sign pair is `X_0^2+U_m^2`. Since `X_0` itself has density cap one, (4.7) sharpens to

`||p_(X_0^2+U_m^2)||_infinity <= pi sqrt(2)`.                (5.3)

Convolving with the independent law of `-V_m^2` gives

`boxed{ ||p_(Q_m)||_infinity <= pi sqrt(2) <4.443 }`          (5.4)

for every `m` and every admissible product law.

This is the requested substantive application of the partner result. The same family simultaneously satisfies the partner's exact obstruction

`E_selector |det A_m[S,S]|^(-1/3)=m^(2/3) ->infinity`,       (5.5)

while its true density is uniformly bounded by (5.4). Thus this is an explicit mathematical proof that, on the canonical diffuse obstruction, **bank aggregation before reciprocal determinant payment is not merely a slogan: it converts a diverging local-minor cost into a universal density constant.**

The partner's overlap-one compound packet `M_1=((m-1)/m)^2 ->1` is exactly the matrix signature of this situation: the order-one curvature is spread among many tiny physical minors, while the product law is naturally compressed into the two normalized bank sums before squaring.

## 6. Arbitrary-rank extension of the partner family

Let `B=A_m` on the singleton/positive/negative active banks, and append any number of outside coordinates. Take any symmetric outside block `D` and any cross block `C` satisfying

`Ran(C) subset Ran(B)`.

Equivalently every outside column couples to the active coordinates only through the three bank directions

`e_0`, `m^(-1/2)1_(positive bank)`, `m^(-1/2)1_(negative bank)`.

Then Theorem 3.1 followed by (5.4) gives

`boxed{ ||p_(X^T A X)||_infinity <= pi sqrt(2) }`             (6.1)

for every cap-one product law, uniformly in `m`, the number of outside variables, all entries of `C,D`, and all support geometry.

This enlarged matrix is automatically in the target class: the principal block `B` has eigenvalues `1,1,-1` (and zeros), so Cauchy interlacing forces the full symmetric matrix to have at least two eigenvalues `>=1` and one eigenvalue `<=-1`.

Thus (6.1) closes a nontrivial arbitrary-rank target family that still exhibits the partner's complete failure of bounded-size principal localization.

## 7. What remains unpaid

The full theorem is not proved. The new exact translation identity shows that the translation/localization part itself has a precise boundary:

- range-aligned outside forcing is completely free;
- arbitrary support geometry is completely free through Theorem 2.1;
- diffuse collinear banks can be aggregated before squaring with universal scalar projection caps;
- the remaining local obstruction for a singular active Hessian is **kernel leakage** `P_(Ker B) C` together with the absence, in a general target matrix, of a guaranteed decomposition into disjoint rank-one banks.

A highest-value next implication is therefore an aggregate-before-inversion theorem that either

1. decomposes an order-one third-compound packet into a bounded number of disjoint/range-aligned product-linear banks, or
2. proves directly that substantial kernel leakage supplies an alternative hyperbolic/linear smoother,

without selecting one tiny physical determinant first.

No full-solution claim is made. No finite numerical sweep or unreviewed coarea premise is used.
