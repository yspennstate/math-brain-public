# account03/B04 — independent determinant review and sharpened diffuse-range Fourier theorem

Run: `B04-20260922T135303Z-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `INDEPENDENT_SCOPE_PASS / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and later owner instruction

The target remains: for every dimension `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a universally bounded density, or give a valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, or eigen-coordinate-independence hypothesis is added. Continuity is tracked separately.

Fresh control additionally assigns `account03/B04` an independent review of the regularized-determinant proof at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

The exact assigned partner `account04/B04` had no completed QFORM handoff/report in the fresh shared handoff tree, so no partner result is fabricated. The owner-specified completed interactive determinant proof is the mathematical dependency actually applied below.

Live corrections consumed before publication include the false pointwise scalar oscillatory-decay route, the cross-minor-only obstruction, the false single-Schur-rank-two extraction, the local-cross-rank-three dichotomy obstruction, and the fiberwise-trace obstruction. None is used as a positive premise.

## 2. Independent check of the graph Brascamp--Lieb normalization

I re-derived the scaling in Section 4 of the source report rather than accepting it by name.

Let `R` be an `m x k` real matrix with columns `r_j`; let `D_i` be independent with difference densities `g_i=f_i*tilde(f_i)`; put `h_j=|hat f_j|^q`, `1<=q<=2`; and define

`M = alpha I_m + a^2 R R^T`,
`c_i = alpha e_i^T M^{-1}e_i`,
`d_j = a^2 r_j^T M^{-1}r_j`.

Set

`v_i=sqrt(alpha)M^{-1/2}e_i`, `w_j=aM^{-1/2}r_j`.

Then

`sum_i v_iv_i^T + sum_j w_jw_j^T = I_m`,
`||v_i||^2=c_i`, `||w_j||^2=d_j`.

After `x=M^{-1/2}z`,

`g_i(x_i)=g_i((sqrt(c_i)/sqrt(alpha)) <v_i/sqrt(c_i),z>)`,
`h_j(a r_j.x)=h_j(sqrt(d_j)<w_j/sqrt(d_j),z>)`.

Applying geometric rank-one Brascamp--Lieb to the normalized directions therefore contributes exactly

`alpha^(c_i/2)c_i^(-c_i/2)||g_i||_(1/c_i)`

for each `g_i`, and

`d_j^(-d_j/2)||h_j||_(1/d_j)`

for each nonzero `w_j`, together with `det(M)^(-1/2)`. This matches equation (4.2) of the source report; in particular the `alpha^(c_i/2)c_i^(-c_i/2)` factor is necessary and is present.

Using the source scalar inequalities

`||g_i||_(1/c) <= 2^c c^(c/2)(1+c)^(-(1+c)/2)`,

and, when `d<=q/2`,

`|| |hat f|^q ||_(1/d)
 <= (2pi)^d q^(q/2-d)(q-d)^(-(q-d)/2)d^(d/2)`,

the powers `c_i^(c_i/2)` and `d_j^(d_j/2)` cancel the Brascamp--Lieb normalization factors. If `theta=sum_j d_j=sum_i(1-c_i)`, the remaining scalar multiplier is

`det(M)^(-1/2) alpha^((m-theta)/2)(2pi)^theta
 exp{[1-(log(2q))/2]theta}`.

For

`L_q=pi e sqrt(2/q)`, `alpha=L_q^2`,

the bracket after factoring `alpha^m` from `det(M)` is exactly one:

`2pi exp(1-(log(2q))/2)/sqrt(alpha)=1`.

Hence the reviewed graph estimate is correctly normalized:

`E prod_j |hat f_j(a r_j.D)|^q
 <= det(I+a^2RR^T/L_q^2)^(-1/2)`.

I find no missing determinant power or row-scaling factor in this step.

## 3. Independent check of the quadratic-form decoupling orientation

For disjoint original-coordinate sets `I,J` and `B=A[I,J]`, condition on all coordinates outside `I union J`. Write the conditional phase as

`q_I(X_I)+q_J(X_J)+2X_I^TBX_J+c`.

Cauchy--Schwarz in `X_I` removes the arbitrary self phase `q_I`. Expanding the square with two independent copies `Y,Y'` of `X_J` and then taking absolute values removes the `q_J(Y)-q_J(Y')` phase and yields

`|phi(t)|^2
 <= E_(Y,Y') prod_(i in I) |hat f_i(2t[B(Y-Y')]_i)|`.

For `q>=1`, Jensen gives

`|phi(t)|^(2q)
 <= E_(Y,Y') prod_(i in I)|hat f_i(2t[B(Y-Y')]_i)|^q`.

Applying the reviewed graph estimate with `R=B^T` and `a=2t` therefore gives

`|phi(t)|
 <= det(I+2q t^2 BB^T/(pi^2e^2))^(-1/(4q))`,

provided the diagonal of the projection onto `range(B)` on the `I` side is at most `q/2`. The orientation is correct: the columns of `R=B^T` are indexed by `I`, and `range(R^T)=range(B) subset R^I`.

This step never declares rotated eigen-coordinates independent and permits arbitrary self blocks, outside couplings, and coordinate-separable measurable phases.

## 4. Independent check of the MSS/full-spectrum passage

Assume

`A=U Lambda U^T`,

where the columns of `U` are orthonormal and span the **entire range** of `A`; `Lambda` is invertible on that range; and at least three eigenvalues of `Lambda` have modulus at least one. Let

`epsilon=max_i ||u_i||^2`.

MSS Corollary 1.5, specialized to two parts, gives a partition of the original coordinates into `I,J` such that

`M_I=U_I^TU_I <= beta I`, `M_J=U_J^TU_J <= beta I`,

where

`beta=(1/sqrt(2)+sqrt(epsilon))^2`.

Since `M_I+M_J=I`, both parts also satisfy

`M_I,M_J >= delta I`,

with

`delta=1-beta = 1/2-sqrt(2epsilon)-epsilon`.

For the cross block

`B=A[I,J]=U_I Lambda U_J^T`,

polar factorization of the restricted frames shows that its nonzero singular values are exactly those of

`M_I^(1/2) Lambda M_J^(1/2)`.

Consequently

`s_j(B)>=delta s_j(Lambda)`

for every nonzero singular-value index `j`: each square-root factor has least singular value at least `sqrt(delta)`. Thus the three target eigenvalues produce three cross singular values at least `delta`.

Because `Lambda` is invertible on the entire range and `U_J` has full column rank, `range(B)=range(U_I)`. Hence its projection is

`P_B=U_I M_I^(-1)U_I^T`,

and for each `i in I`,

`(P_B)_(ii)=u_i^TM_I^(-1)u_i <= epsilon/delta`.

This verifies the direction of the projection and shows why all additional nonzero eigenvalues, however small and of either sign, are harmless: they are retained in `Lambda`, while the regularized determinant bound may discard their factors after the three large singular values have been secured.

For the source value `epsilon=1/32`, `delta=7/32` and the leverage bound is `1/7<1/2`, so `q=1` is valid. I therefore independently PASS the source theorem on its stated scope. The unrestricted QFORM conjecture remains open because the entire-range leverage hypothesis is extra and fails, for example, for every invertible matrix.

The MSS constant was also checked against the published two-part formula `||(sum_{i in S_k}u_iu_i^*)|| <= (1/sqrt(2)+sqrt(epsilon))^2`.

## 5. New strengthening: the `1/32` threshold is not intrinsic

The source chose `epsilon=1/32`, but the reviewed fractional determinant estimate allows a wider diffuse-range regime.

### Theorem 5.1 — parameterized full-spectrum diffuse-range branch

Let the hypotheses of Section 4 hold. Define

`delta_epsilon = 1/2-sqrt(2epsilon)-epsilon`.

Suppose there exists `q` with

`1<=q<3/2`,

`epsilon/delta_epsilon <= q/2`.

Then `Q=X^TAX` has a bounded **continuous** density and

`||p_Q||_infinity
 <= [e sqrt(pi)/(2 sqrt(2q) delta_epsilon)]
    Gamma(3/(4q)-1/2)/Gamma(3/(4q)).`                         (5.1)

The same conclusion holds after adding any coordinate-separable measurable real phase `sum_i V_i(X_i)` finite almost surely.

### Proof

The MSS partition gives three cross singular values at least `delta_epsilon`, while the cross-range leverage is at most `epsilon/delta_epsilon<=q/2`. The reviewed determinant estimate gives

`|phi(t)|
 <= (1+2q delta_epsilon^2 t^2/(pi^2e^2))^(-3/(4q)).`          (5.2)

Since `q<3/2`, the exponent at infinity is `3/(2q)>1`, so (5.2) is integrable. Fourier inversion gives a continuous density vanishing at infinity. The exact beta integral

`int_R (1+beta^2t^2)^(-a)dt
 = sqrt(pi) beta^(-1) Gamma(a-1/2)/Gamma(a)`

with `a=3/(4q)` and `beta=sqrt(2q)delta_epsilon/(pi e)` gives (5.1). QED.

A convenient explicit choice is

`q(epsilon)=max(1,2epsilon/delta_epsilon)`.

Such a `q<3/2` exists exactly throughout

`epsilon < epsilon_* := (39-6sqrt(30))/98 = 0.0626188423...`.

Indeed the endpoint condition is `delta_epsilon>4epsilon/3`.

### Clean corollary with q=1

The simpler `q=1` condition is

`delta_epsilon>=2epsilon`,

which is equivalent to

`epsilon<=1/18`.

Therefore the source theorem can be strengthened from entire-range leverage `<=1/32` to

`boxed(max_i ||u_i||^2 <= 1/18)`

without changing mechanism. In this regime `delta_epsilon>=1/9`, and hence

`|phi(t)| <= (1+2t^2/(81pi^2e^2))^(-3/4)`

and

`boxed(||p_Q||_infinity
 <= [9e sqrt(pi)/(2sqrt(2))] Gamma(1/4)/Gamma(3/4)
 <45.360.)`                                                    (5.3)

At the source point `epsilon=1/32`, using the exact gamma integral rather than the crude tail split sharpens its reported `96e/(7sqrt(2))<27` to

`[16e sqrt(pi)/(7sqrt(2))] Gamma(1/4)/Gamma(3/4)
 =23.03953145...`.

These are supporting theorems, not a solution of the arbitrary heavy-coordinate case.

## 6. Explicit genuinely rotated indefinite form with constant 10.08

To instantiate the reviewed inequality without any eigen-coordinate independence, index 64 original coordinates by `x in {0,1}^6` and define three orthonormal vectors by

`U_x = (1, (-1)^{x_1}, (-1)^{x_2})/8`.

Equivalently, `U` consists of three Walsh columns. Every entry of every eigenvector is nonzero and every row leverage is `3/64`. Let

`Lambda=diag(1,1,-1)`, `A=U Lambda U^T`.

Then `A` is a genuinely rotated indefinite rank-three matrix with spectrum

`{1,1,-1,0,...,0}`.

Partition by the unused Walsh bit:

`I={x:x_3=0}`, `J={x:x_3=1}`.

Because the three chosen Walsh columns do not depend on `x_3`,

`U_I^TU_I=U_J^TU_J=(1/2)I_3`.

Thus the cross block `B=A[I,J]` has exactly three nonzero singular values, all equal to `1/2`, and

`(P_range(B))_(xx)=2||U_x||^2=3/32<1/2`.

The `q=1` determinant estimate therefore gives the explicit product-space inequality

`boxed(|E exp(itX^TAX)|
 <= (1+t^2/(2pi^2e^2))^(-3/4))`                               (6.1)

for **every** independent input law with coordinate densities bounded by one. No support, moment, or log-concavity condition appears.

Consequently `Q` has a continuous density and

`boxed(||p_Q||_infinity
 <= e sqrt(pi/2) Gamma(1/4)/Gamma(3/4)
 =10.07979501... .)`                                          (6.2)

This is an explicit genuinely rotated indefinite estimate with all constants tracked.

## 7. Remaining full-target obstruction

This review does not supply an exhaustive reduction from three large eigenvalues to a diffuse entire-range frame or to a good cross cut. The live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` correction shows that a uniformly good small principal block / rank-three-cross-cut dichotomy is false. The remaining product-Fourier task is therefore to aggregate heavy original coordinates or independent coordinate banks *before* paying a reciprocal minor/cross singular value, while preserving the regularized determinant gain on the diffuse remainder.

A concrete next implication is:

`QFORM-HEAVY-DIFFUSE-REGDET-BRIDGE-v1` — prove that every target matrix either admits a cross block satisfying a parameter pair `(sigma,q)` with `3>2q` and universal `sigma>0`, or has a heavy-coordinate/bank decomposition whose heavy part can be conditioned/aggregated into an already controlled hyperbolic or principal-block mechanism without losing dimension-free constants.

The corrections show that this cannot be reduced to choosing one scalar Schur pivot, one small principal minor, or one fiberwise trace bound.

## 8. Review verdict

**PASS on the stated supporting scope.** I found no defect in the graph Brascamp--Lieb normalization, the cross-block orientation, the MSS two-part passage, the singular-value comparison, or the claim that arbitrary additional *small nonzero* eigenvalues are retained without reciprocal determinant loss under the entire-range leverage hypothesis.

The pass does not promote the result to the unrestricted conjecture. The new mathematical delta is the parameterized leverage theorem (5.1), its clean `1/18` corollary (5.3), and the explicit Walsh-rotated indefinite bound (6.2).
