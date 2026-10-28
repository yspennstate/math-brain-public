SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-22T22:33:02Z.
attacking: the two-star near-leaf branch — absorb arbitrary residual curvature at a strong physical star before any reciprocal tiny-minor extraction, and identify the exact obstruction when the star coordinate has nonzero self-curvature.

# account02/B07 — random-shift L3 payment for zero-self physical stars

**Run:** `20260922T223302Z-account02-B07-QFORM-ddc6a5`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Classification:** **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED (intermediate arbitrary-self one-star extension); FULL TARGET OPEN**.

## 1. First unpaid implication and what is changed here

The previous B07 run reduced the bi-heavy O0 two-star survivor to a genuine physical near-leaf geometry. In its notation, two physical anchors carry a source-valid reserve

`P=||r||_2^2 ||c||_2^2 > 1/200`,

and either the complete checkerboard two-row second compound is at least `P/16`, in which case the completed two-cross theorem pays the full residual, or the two outside coupling rows are within relative norm `<1/4` of proportionality. The remaining implication was `QFORM-O0-NEARLEAF-OR-EDGEBANK-PAYMENT-v1`.

The designated partner account03/B07 r18 then proved `QFORM-PRODUCT-L2-v1` and paid the **clean** two-star endpoint, but explicitly left arbitrary same-bank quadratic curvature, residual cross-core curvature, and own-side anchor couplings unpaid.

This run proves a curvature-robust replacement at one physical star. The key point is that if the chosen physical coordinate has **zero diagonal coefficient**, all other terms—however complicated—are a random shift once that coordinate is exposed linearly. A third-power density estimate survives that arbitrary random shift. This gives exactly the half-Riesz quantity needed by the existing outer physical-square transducer.

The remaining near-leaf debt is therefore narrowed to the case in which every quantitatively strong star anchor has nonzero physical self-curvature. A two-variable exact square construction below proves that one cannot extend the one-star half-Riesz lemma through an arbitrary nonzero self coefficient without using additional spectral/product structure.

## 2. Source-pinned inputs actually consumed

### 2.1 Previous own B07 near-leaf theorem

Complete source:

`yspennstate/math-open-problems@d4afa77929c3a9b5322f451c6d470fcfe519f01b`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T213439Z-account02-B07-QFORM-e7b269/REPORT.md`.

It proves, after applying account03/B07 r17 and account01/B07's compound transfer, that the current O0 two-star branch has `P>1/200`; it also proves the checkerboard wedge payment and the quantitative near-proportional alternative. No single coordinate minor is selected.

### 2.2 Designated partner account03/B07 r18

Complete source:

`yspennstate/math-open-problems@816c00139a183545a0f85c5b4a939eb52cabcfac`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T221112Z-account03-B07-qform-r18/REPORT.md`.

The partner proves that for independent `X,Y` with density caps `M,N`,

`||p_(kappa X Y)||_2 <= 2 sqrt(MN/|kappa|)`,

and hence two genuinely disjoint product terms have a bounded continuous density. It applies this to the curvature-free two-star endpoint. I use that result as the already-paid clean endpoint and extend the same product-kernel mechanism to an arbitrary shift depending on the entire complementary product block.

### 2.3 Product-projection density cap

The partner's application uses the completed sharp product-projection transfer from account04/B18:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

In the form needed here: for independent cap-one original coordinates and a nonzero coefficient vector `ell`, the normalized linear form `<ell,Y>/||ell||_2` has density at most `sqrt(2)`. Thus

`||p_(<ell,Y>)||_infinity <= sqrt(2)/||ell||_2`.                 (2.1)

This is an original-coordinate product statement; no independence after rotation is asserted.

## 3. Random-shift L3 theorem for one product

### Theorem 3.1 — `QFORM-RANDOMSHIFT-PRODUCT-L3-v1`

Let `X` be independent of a random element `Y`. Assume `X` has probability density `f` with `||f||_infinity<=N`. Let `U=U(Y)` be a real random variable with probability density bounded by `M`, and let `H=H(Y)` be an arbitrary measurable real function. For `kappa!=0`, put

`Z=kappa X U + H`.

Then `Z` has an `L^3` density and

`boxed:
||p_Z||_3^3 <= 24 N^2 M^2 / |kappa|^2,
`

or equivalently

`boxed:
||p_Z||_3 <= 24^(1/3) (NM/|kappa|)^(2/3).
`                                                               (3.1)

No moment, support, centering, continuity, log-concavity, or independence between `U` and `H` is assumed. The random shift `H(Y)` may contain arbitrary quadratic curvature and arbitrary couplings among the coordinates in `Y`.

### Proof

Because `U` has a density, `P(U=0)=0`. Conditioning on `Y` gives the density

`p_Z(z)=E[ f((z-H)/(kappa U)) / (|kappa U|) ].`                 (3.2)

Take three independent copies `Y_1,Y_2,Y_3` of `Y`, and write `U_a=U(Y_a)`, `H_a=H(Y_a)`. Tonelli gives

`||p_Z||_3^3
 = E int_R prod_(a=1)^3
   f((z-H_a)/(kappa U_a))/(|kappa U_a|) dz.`                    (3.3)

Let `T_(1)<=T_(2)<=T_(3)` be the increasing rearrangement of `|U_1|,|U_2|,|U_3|`. In the inner integral, retain the factor corresponding to `T_(1)` and bound the other two copies of `f` by `N`. Since the retained scaled density integrates to one before its Jacobian denominator is removed,

`int prod_(a=1)^3
   f((z-H_a)/(kappa U_a))/(|kappa U_a|) dz
 <= N^2 / (|kappa|^2 T_(2) T_(3)).`                            (3.4)

The shifts `H_a` have disappeared completely from the upper bound.

Let `T=|U|` and `F(t)=P(T<=t)`. The density cap on `U` gives

`F(t)<=min(1,2Mt).`                                             (3.5)

For three iid copies, symmetry and conditioning on the two copies not declared smallest give

`E[1/(T_(2)T_(3))]
 <= 3 E[ F(min(T_2,T_3))/(T_2T_3) ]`
` <= 6M E[1/max(T_2,T_3)].`                                    (3.6)

The remaining expectation is exactly

`E[1/max(T_2,T_3)]
 = int_0^infinity F(t)^2 t^(-2) dt.`                            (3.7)

Split at `t_0=(2M)^(-1)`. Using (3.5),

`int_0^t0 F(t)^2 t^(-2)dt <= int_0^t0 4M^2 dt = 2M`,

and

`int_t0^infinity F(t)^2 t^(-2)dt <= int_t0^infinity t^(-2)dt = 2M`.

Therefore

`E[1/(T_(2)T_(3))] <= 6M(4M)=24M^2`.                           (3.8)

Combining (3.3), (3.4), and (3.8) proves (3.1). QED.

### Why this is stronger than the clean-product endpoint

The partner's `L^2` theorem is optimal for a single unshifted product but cannot by itself absorb a shift depending on the same bank as the product factor. The third-copy argument above is deliberately arranged so that the arbitrary `H_a` never needs a density or an independence property. Thus this theorem preserves all complementary quadratic curvature instead of conditioning it away.

## 4. Half-Riesz consequence

For a probability density `h` with `L=||h||_3`, split at radius `R>0`. Hölder with exponents `3` and `3/2` gives, uniformly in the center `y`,

`int_(|z-y|<=R) |z-y|^(-1/2) h(z) dz
 <= L (int_(|u|<=R)|u|^(-3/4)du)^(2/3)
 =4 L R^(1/6).`                                                  (4.1)

The complement is at most `R^(-1/2)`. Optimizing

`4LR^(1/6)+R^(-1/2)`

at `R^(2/3)=3/(4L)` gives

`sup_y E|Z-y|^(-1/2)
 <= 4^(7/4)3^(-3/4) L^(3/4).`                                  (4.2)

Using (3.1),

`boxed:
H_(1/2)(Z):=sup_y E|Z-y|^(-1/2)
 <= [2^(17/4)/sqrt(3)] sqrt(NM/|kappa|).
`                                                               (4.3)

Numerically the universal coefficient in (4.3) is

`2^(17/4)/sqrt(3)=10.985424767504629...`.

## 5. Curvature-robust zero-self theorem in original coordinates

### Corollary 5.1 — `QFORM-ZEROSELF-RANDOMSHIFT-HALFRIESZ-v1`

Let `S` be any real symmetric matrix and let the independent original coordinates have densities at most one. Fix a physical coordinate `i` satisfying

`S_ii=0`,

and let `ell=(S_ij)_(j!=i)` be its full off-diagonal row. If `ell!=0`, then for

`R=X^T S X`

one has

`boxed:
||p_R||_3 <= 12^(1/3) ||ell||_2^(-2/3),
`                                                               (5.1)

and

`boxed:
H_(1/2)(R) <= (16/sqrt(3)) ||ell||_2^(-1/2).
`                                                               (5.2)

All other diagonal terms, same-bank quadratic terms, cross-core terms, affine shifts arising from earlier conditioning, and additional spectral directions are allowed.

### Proof

Write `Y=(X_j)_(j!=i)`. Then exactly

`R=2 X_i <ell,Y> + H(Y)`                                       (5.3)

for an arbitrary quadratic `H`. The scalar `X_i` is independent of the entire original-coordinate block `Y`. By the source-pinned product-projection theorem (2.1),

`M:=||p_(<ell,Y>)||_infinity <= sqrt(2)/||ell||_2`.             (5.4)

Apply Theorem 3.1 with `N=1`, `kappa=2`. Equation (3.1) becomes

`||p_R||_3 <= 12^(1/3)||ell||_2^(-2/3)`,

and (4.3) simplifies exactly to

`[2^(17/4)/sqrt(3)] sqrt((sqrt(2)/||ell||_2)/2)
 = (16/sqrt(3))||ell||_2^(-1/2)`.

QED.

This is an independence-safe physical-coordinate statement. In particular, there is no conditioning on a rotated complement and no arbitrary-joint coarea step.

## 6. Application to the current O0 two-star reserve

In the current B07 two-star branch,

`||r||^2 ||c||^2 > 1/200`.                                     (6.1)

Hence

`max(||r||,||c||) > 200^(-1/4).`                               (6.2)

Suppose the anchor carrying the larger of these two stars has zero physical diagonal in the residual `S`. Its complete off-diagonal row norm is at least the star norm, so Corollary 5.1 gives

`boxed:
H_(1/2)(R)
 < (16/sqrt(3)) 200^(1/8)
 =17.913815821223174... .
`                                                               (6.3)

In particular, if **both** two-star anchors have zero residual diagonal, this branch is automatically paid, regardless of the checkerboard near-leaf defect and regardless of every same-bank/core quadratic term that prevented the partner's clean two-product theorem from applying.

At the exact parent scope where the already-completed outer physical-square transducer writes

`Q=a(X_0+h)^2+R`,

(6.3) yields the density estimate

`||p_Q||_infinity < 17.914 |a|^(-1/2).`                         (6.4)

I do not suppress the separate small-outer-pivot debt: (6.4) is recorded only at that transducer's exact scope.

Thus the current conditional proof map is now:

1. O0 third-compound currency transfers to `E_2>1/25`.
2. The partner's ridge theorem pays the moderate-leverage branch and otherwise yields an edge-bank or two-star reserve.
3. The previous B07 checkerboard theorem pays every two-star state whose complete two-row wedge is at least `P/16`.
4. The designated partner r18 pays the genuinely curvature-free two-product endpoint.
5. **New:** arbitrary complementary curvature is harmless whenever a quantitatively strong star sits on a zero-self physical anchor.
6. The surviving two-star debt is therefore concentrated in the near-leaf/nonzero-self geometry, plus the sibling edge-bank branch and the separate outer-small-pivot splice.

## 7. Why a nonzero self coefficient cannot be treated as a harmless perturbation

The tempting extension of Corollary 5.1 is false even for two independent cap-one variables.

Fix any `a!=0`. Let `X,Y` be independent `Uniform[-1/2,1/2]`, put `U=Y`, and choose the allowed quadratic shift

`H(Y)=Y^2/a`.

Then

`aX^2+2XY+H(Y)
 = a(X+Y/a)^2`.                                                  (7.1)

The random variable `W=X+Y/a` has a continuous density which is strictly positive at zero; in fact

`p_W(0)=min(|a|,1)>0`.                                          (7.2)

Therefore

`E |aW^2|^(-1/2)
 = |a|^(-1/2) E|W|^(-1)
 = infinity`.                                                    (7.3)

So no finite one-star estimate of the form

`H_(1/2)(aX^2+2XU+H(Y)) <= C(a, density-cap(U), coupling-size)`

can hold uniformly over arbitrary quadratic `H` merely because the linear star is nontrivial. The self-curvature can align exactly with the random shift and collapse the expression to one square.

This is a **source-valid counterexample to an intermediate proof mechanism**, not a QFORM counterexample: its two-variable quadratic matrix is rank one and therefore does not satisfy the full three-large-eigenvalue target. Its role is to show that the next near-leaf step must spend the second spectral direction / physical pair geometry rather than perturbing (5.2) across a nonzero self coefficient.

Classification: `QFORM-ONESTAR-ARBITRARY-SELF-HALFRIESZ-FALSE-v1` — **CANDIDATE_REFUTED for the intermediate extension; full QFORM not refuted.**

## 8. Exact remaining implication

The first unpaid implication is now

**`QFORM-O0-NEARLEAF-NONZEROSELF-PAIR-PAYMENT-v1` (OPEN):**

> In the surviving two-star branch with `P>1/200` and checkerboard wedge `<P/16`, assume the quantitatively strong anchor(s) have nonzero physical self coefficient. Use the physical two-anchor principal block together with the near-proportional outside rows and the residual second spectral direction to force either (i) a uniformly payable invertible physical pair, (ii) the completed pair-log/rank-two-affine half-Riesz mechanism, (iii) a grouped-coordinate/zero-pivot branch, or (iv) the sibling edge-bank resource. Do not rotate the two original anchors and then assert independence.

The exact-square construction (7.1) is a regression test: any proposed proof that uses only one strong star and treats nonzero self-curvature as an arbitrary bounded perturbation is invalid.

The edge-bank alternative `b^2||C||_F^2>1/200`, the separate small-outer-pivot splice, and non-O0 parent branches remain distinct debts. The unrestricted QFORM conjecture and global continuity remain open.

## 9. Correction and hypothesis audit

This report uses no arbitrary-joint rank-three coarea bound, no positive conditional projection-density moment, no law-uniform pointwise oscillatory decay, no fiber-supremum integration, no post-rotation independence, and no assertion that one determinant-weighted bank contains a uniformly large individual minor. The only projection cap used is source-valid for a linear form of independent original coordinates. The arbitrary shift in Theorem 3.1 is handled algebraically by the three-copy `L^3` expansion rather than by a conditional-density supremum.

No numerical experiment is a premise. A deterministic checker records only the displayed constants and the rank-one algebra of the failure example. Full target remains `OPEN / NOT PROVED / NOT DISPROVED`.
