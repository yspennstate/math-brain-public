# fleet01/B19 — universal proof assembly: one-sided scalar-curvature repair of the rank-two mixed-Hessian endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T141737Z-b19-qform-r11`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and correction discipline

The full target remains: for every dimension, every independent real coordinate law with one-dimensional probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `Q=X^T A X`. A continuous representative is a separate stronger conclusion.

This report keeps arbitrary signs, repeated eigenvalues, arbitrary extra spectrum and arbitrary fragmented bounded densities. It does not use law-uniform pointwise one-dimensional Fresnel decay, post-rotation independence, an unrestricted fiber supremum, bounded-diameter localization, a conditional-density substitute for independence, or a single-minor extraction as a universal structural bridge. The live corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1` are all respected.

The preceding B19 run proved a cancellation-resistant balanced-cut resource theorem. If a selected three-eigenvector frame is balanced across an original-coordinate cut `H,L` with both partial Gram matrices at least `delta I_3`, and

`A=[[C,B],[B^T,D]]`,

then

`delta <= s_1(C)^2+s_3(B)^2`,
`delta <= s_2(C)^2+s_2(B)^2`,
`delta <= s_3(C)^2+s_1(B)^2`,

and likewise with `C` replaced by `D`. Thus the only genuinely new analytic difficulty after that algebra is the mixed `1 self + 2 cross` / `2 self + 1 cross` regime. The present run attacks the sharpest borderline piece: two mixed directions give only `|t|^{-1}` and are not integrable; one genuine scalar curvature can repair exactly that endpoint if its coupling is product-compatible.

## 2. Completed peer mathematics used

Two immutable peer results are used at their exact scopes.

1. **Designated partner fleet02/B19**, canonical package `yspennstate/math-open-problems@23b520c19dd0e43cbff0fc0514a4dbfcd637b0f4`, report blob `802371834ddf9f3ad03d4db1875058c2a266d1b9`, proves `QFORM-RECTANGULAR-MULTIPIVOT-SINGULAR-v1`: if an original-coordinate pivot side has zero self block and a rectangular cross block `B` has `s_2(B)>0`, then

   `||p_Q||_infinity <= 2 sqrt(pi)/sqrt(s_1(B)s_2(B))`.

   This is the paid zero-self endpoint of the present mixed phase diagram and avoids selecting a coordinate minor.

2. **fleet03/B09**, canonical report `yspennstate/math-open-problems@446d0a33ef626b11ed5da529f2cec821732e97e9`, report blob `193f3f41acb6bbf7fa4a3edfd9eb918489b51ded`, proves the exact mixed-Hessian Plancherel estimate. In mixed dimension two, for arbitrary unit-modulus same-side phases and an invertible physical `2x2` cross block `B`, the same calculation gives

   `|psi(t)| <= pi |t|^{-1}|det B|^{-1/2} ||F_t||_2 ||G_t||_2`.    (2.1)

   In dimension three this is integrable and yields their full block theorem. In dimension two it is only logarithmically nonintegrable, and the fleet02/B09 counterexample `Q=(X_1+Y_1)^2-(X_2+Y_2)^2` shows that an arbitrary `2x2` cross block plus unrestricted curvature really can have an unbounded logarithmic density.

The new theorem below inserts the missing scalar curvature into (2.1) **without** replacing it by a false pointwise Fresnel estimate. The curvature is spent through an averaged `L^4(dt)` estimate and a vector-valued Minkowski step.

## 3. Scalar averaged-curvature lemma

### Lemma 3.1 (`L^4` shifted-square transform)

Let `X` have probability density `0<=f<=1`. For `a!=0` and arbitrary `b in R`, define

`K_b(t)=E exp(i t (a X^2+2bX))`.

Then

`||K_b||_{L^4(R_t)} <= 2 sqrt(2) (2 pi)^(1/4) |a|^(-1/4)`.       (3.1)

The bound is uniform in `b` and in the law of `X`.

### Proof

Completing the square changes only an overall unimodular factor and translates the input density:

`aX^2+2bX = a(X+b/a)^2-b^2/a`.

Translations preserve the density cap one. It therefore suffices to study `W=aY^2` with `p_Y<=1`.

For `a=1`, the density `g` of `Y^2` obeys for `y>0`

`g(y)=[p_Y(sqrt(y))+p_Y(-sqrt(y))]/(2sqrt(y)) <= y^(-1/2)`,

and `int g=1`. Hence

`int_0^1 g(y)^(4/3)dy <= int_0^1 y^(-2/3)dy=3`,

while for `y>=1` we have `g(y)<=1`, so

`int_1^infinity g(y)^(4/3)dy <= int_1^infinity g(y)dy <=1`.

Thus `||g||_(4/3)<=4^(3/4)=2sqrt(2)`. Scaling by `a` gives

`||p_{aY^2}||_(4/3) <= 2sqrt(2)|a|^(-1/4)`.                    (3.2)

For the Fourier convention `hat g(t)=int exp(itx)g(x)dx`, the elementary Riesz--Thorin Hausdorff--Young bound obtained from `L^1->L^infinity` norm one and Plancherel `L^2->L^2` norm `sqrt(2pi)` gives

`||hat g||_4 <= (2pi)^(1/4)||g||_(4/3)`.

Combining with (3.2) proves (3.1). QED.

This is deliberately an **integrated** time estimate. It is compatible with the live phase-aligned-density correction, which refutes any positive law-uniform pointwise power decay for `K_b(t)`.

## 4. Main theorem — one-sided scalar curvature repairs the `2x2` logarithmic endpoint

Let `x,u_1,u_2,v_1,v_2` be five distinct original coordinates. Write `u=(u_1,u_2)` and `v=(v_1,v_2)`. Condition on every remaining original coordinate. Suppose the resulting quadratic polynomial has the form

`q(x,u,v)= a x^2 + 2x(beta+r^T u)
          + F(u) + 2u^T Bv + G(v) + c`,                         (4.1)

where

- `a!=0`;
- `B` is an invertible real `2x2` matrix;
- `r,beta,c` are arbitrary and may depend on the conditioned outside coordinates;
- `F,G` are arbitrary real quadratic-affine functions and may depend on the conditioned outside coordinates.

Equivalently, in matrix language the only structural restriction besides the invertible `2x2` cross packet is the **one-sided compatibility**

`A[x,{v_1,v_2}]=0`;                                             (4.2)

coupling of `x` to the `u` side is completely unrestricted. There is no condition on the two same-side principal blocks, on signs, or on outside couplings.

### Theorem 4.1 (`QFORM-ONE-SIDED-MIXED-2PLUS1-v1`)

Under (4.1), for arbitrary independent original-coordinate densities bounded by one, the conditional and unconditional laws of `Q` have bounded continuous densities vanishing at infinity, and

`||p_Q||_infinity
 <= C_* |a|^(-1/5)|det B|^(-2/5)`,                              (4.3)

where

`C_* = 5 * 3^(3/5) * 2^(-2/5) < 7.326`.                         (4.4)

The same result holds with the roles of `u` and `v` reversed.

### Proof

Fix the outside coordinates. Let `f_x`, `f_U=f_{u_1}f_{u_2}`, and `f_V=f_{v_1}f_{v_2}` denote the three independent product densities. Define

`K_t(u)=int f_x(x) exp(i t[a x^2+2x(beta+r^T u)]) dx`,           (4.5)

`F_t(u)=f_U(u) exp(i t F(u)) K_t(u)`,
`G_t(v)=f_V(v) exp(i t G(v))`.

Then, up to an irrelevant unimodular constant, the conditional characteristic function is

`psi(t)=int F_t(u) exp(i2t u^T Bv) G_t(v) du dv`.               (4.6)

Apply the exact `m=2` mixed-Hessian Plancherel calculation from fleet03/B09 to these actual amplitudes. For `t!=0`,

`|psi(t)| <= pi |t|^(-1)|det B|^(-1/2)
              ||F_t||_2 ||G_t||_2`.                             (4.7)

Since each coordinate density is at most one,

`||G_t||_2<=1`,

and, writing

`h(t)^2 = int f_U(u)|K_t(u)|^2 du`,                             (4.8)

we have

`||F_t||_2^2
 = int f_U(u)^2|K_t(u)|^2du
 <= int f_U(u)|K_t(u)|^2du
 = h(t)^2`.                                                      (4.9)

For every fixed `u`, Lemma 3.1 applies to `K_t(u)` because the coefficient `beta+r^Tu` merely changes the linear shift. Therefore

`||K_.(u)||_4 <= C_a`,
`C_a=2sqrt(2)(2pi)^(1/4)|a|^(-1/4)`.                            (4.10)

Now use Minkowski on the **square** of `h`:

`||h||_4^2
 = ||h^2||_2
 = || int f_U(u)|K_.(u)|^2du ||_2`

`<= int f_U(u) || |K_.(u)|^2 ||_2 du`
`= int f_U(u)||K_.(u)||_4^2 du`
`<= C_a^2`.                                                      (4.11)

Hence

`||h||_4 <= C_a`.                                               (4.12)

This is the essential missing inequality: the scalar curvature supplies a law-uniform **time-averaged** gain while the two mixed directions supply the exact `|t|^{-1}` Plancherel factor.

Put

`K_B=pi |det B|^(-1/2)`.

Together with the trivial `|psi(t)|<=1`, equations (4.7)--(4.12) imply for every `T>0`

`int_R |psi(t)|dt
 <= 2T + K_B int_{|t|>T}|t|^(-1)h(t)dt`

`<=2T + K_B C_a
       (int_{|t|>T}|t|^(-4/3)dt)^(3/4)`

`=2T + K_B C_a 6^(3/4) T^(-1/4)`.                               (4.13)

Let

`D=K_B C_a 6^(3/4)`.

The right side is minimized at `T=(D/8)^(4/5)`, where its value is `10(D/8)^(4/5)`. Thus Fourier inversion gives

`||p_Q||_infinity
 <= (1/(2pi)) 10(D/8)^(4/5)`

`=5*3^(3/5)*2^(-2/5)
  |a|^(-1/5)|det B|^(-2/5)`.                                   (4.14)

The same `L^1(dt)` majorant is uniform in all conditioned outside coordinates. Averaging the conditional characteristic functions therefore preserves the bound. Since the unconditional characteristic function is in `L^1`, Fourier inversion supplies a bounded continuous density vanishing at infinity. QED.

### Why the one-sided condition is real

If `x` couples to both `u` and `v`, then after integrating `x` the factor `K_t(u,v)` is no longer an amplitude on just one side of the bilinear Fourier operator. The Plancherel step (4.7) can no longer insert its `L^4_t` gain through a single `L^2` amplitude. Taking only `sup|K_t|` would discard the new curvature and return the nonintegrable `|t|^{-1}` endpoint. Thus (4.2) is not cosmetic; removing it is a genuine next analytic problem rather than an omitted line.

## 5. Direct target-level example

The theorem is not restricted to a diagonal additive square. Consider five independent admissible coordinates and

`Q=x^2+2xu_1+2u_1v_1+2u_2v_2`.                                 (5.1)

Here `a=1`, `B=I_2`, and the scalar coordinate is genuinely coupled to the `u` side. The symmetric matrix has eigenvalues approximately

`-1.2469796, -1, 0.4450419, 1, 1.8019377`,

so it lies inside the owner's target class (indeed four eigenvalues have modulus at least one). Theorem 4.1 gives for **every** admissible product input law

`||p_Q||_infinity <= C_* <7.326`,                               (5.2)

with a continuous representative.

This example is a literal mixed `1 self + 2 cross` configuration and is not covered merely by saying that an independent square was convolved onto the fleet02/B09 logarithmic control example.

## 6. Application of the designated partner to the same phase diagram

The preceding B19 balanced-cut theorem already supplies an actual inequality for the zero-self endpoint. If a balanced cut has `C=0`, then

`s_3(B)>=sqrt(delta)`,

so in particular `s_1(B),s_2(B)>=sqrt(delta)`. Applying the completed **fleet02/B19** rectangular singular-spectrum theorem gives

`||p_Q||_infinity
 <= 2sqrt(pi)/sqrt(s_1(B)s_2(B))
 <= 2sqrt(pi)/sqrt(delta)`.                                    (6.1)

For the selected-frame MSS value `delta=7/32`,

`||p_Q||_infinity <= 8sqrt(2pi/7)<7.58`.                        (6.2)

Thus the designated partner pays the pure two-cross packet without any local determinant extraction; Theorem 4.1 proves that a compatible scalar self-curvature repairs the otherwise logarithmic mixed-dimension-two endpoint. These are complementary, not competing, branches.

## 7. Compact conditional end-to-end assembly

The current source-valid architecture is now:

1. diagonal / near-diagonal forms are already paid;
2. diffuse rank-three and localized-pivot/diffuse-residual branches are paid by the completed diffuse and critical `L^3` results;
3. entire-range diffuse matrices, including arbitrary extra small eigenvalues of any sign, are paid by the regularized-determinant/MSS theorem;
4. for a diffuse **selected** three-eigenspace with arbitrary extra spectrum, the preceding B19 theorem gives a balanced physical cut and the exact cancellation-resistant self/cross rank budget;
5. the pure zero-self two-cross endpoint is paid by fleet02/B19 through (6.1);
6. arbitrary `3x3` mixed Hessians are paid by fleet03/B09;
7. the present theorem pays the first genuine `1 self + 2 cross` borderline whenever one scalar curvature has a one-sided product-compatible placement.

Consequently a full proof would follow from an exhaustive, quantitative **product-compatible mixed-profile extraction theorem** that routes every remaining balanced mixed profile to one of those paid configurations (or to the already-paid localized/hyperbolic aggregate branches), with parameters bounded below by universal functions of the fixed balanced-cut constant. No step in that conditional assembly treats a rotated input as independent or discards arbitrary extra spectrum.

## 8. First essential missing implication after this run

The remaining mixed-profile debt is now narrower:

### `QFORM-TWOSIDED-MIXED-AGGREGATE-EXTRACTION-v1` (OPEN)

Starting from the balanced-cut inequalities

`delta <= s_1(C)^2+s_3(B)^2`,
`delta <= s_2(C)^2+s_2(B)^2`,
`delta <= s_3(C)^2+s_1(B)^2`,

prove that every `1 self + 2 cross` or `2 self + 1 cross` configuration with fixed `delta>0` admits, before paying a vanishing coordinate minor, at least one of:

- the fleet02/B19 zero-self rectangular packet;
- an fleet03/B09 three-dimensional mixed Hessian;
- a scalar-curvature / rank-two-cross packet satisfying the one-sided compatibility of Theorem 4.1 with quantitative `|a|` and determinant/aggregate cross resource;
- the completed dependent hyperbolic-square aggregate of fleet02/B19;
- a localized-pivot / diffuse-residual branch already paid by fleet03/B19;
- or another dimension-free aggregate smoother.

The new analytic obstruction is specifically **two-sided recycling of the scalar curvature into both sides of a rank-two mixed packet**, together with the known need to aggregate cross singular resource before selecting physical minors. The six-dimensional mixed-profile family from the preceding B19 run proves that these regimes cannot be deleted by a stronger self-or-cross rank-three dichotomy.

## 9. Status

**Proved in this run:** Lemma 3.1 and `QFORM-ONE-SIDED-MIXED-2PLUS1-v1`, including an explicit constant `<7.326`, arbitrary independent density-one inputs, arbitrary signs and outside couplings, and continuity in this branch.

**Named OTHER-account mathematics actually applied:** fleet03/B09's immutable mixed-Hessian Plancherel identity is inserted into the proof at (4.7); designated partner fleet02/B19 is applied quantitatively at (6.1)--(6.2).

**Not proved:** the two-sided/aggregate extraction implication in Section 8; the unrestricted full QFORM conjecture; universal continuity outside branches with an `L^1` characteristic-function proof.

No full-solution claim is made.
