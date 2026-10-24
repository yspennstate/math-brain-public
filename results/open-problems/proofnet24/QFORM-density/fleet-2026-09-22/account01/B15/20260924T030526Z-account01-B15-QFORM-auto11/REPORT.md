SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T03:05:26Z.
attacking: absolute-continuity/regularity closure for the first genuinely two-nonzero-diagonal Schur remainder, and a same-height continuity compiler compatible with original-coordinate product structure.

# account01/B15 — log-envelope self-convolution and a nested indefinite-pair regularity receiver

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW_SUPPORTING_THEOREM / PARTNER_APPLIED / FULL_QFORM_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and corrections

The unrestricted owner target remains OPEN. This run preserves all live corrections: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no projection/X-ray-only shortcut, no arbitrary-joint rank-three coarea height theorem, and no positive conditional projection-density moment shortcut.

The new result stays in original independent coordinates and fills the local gap explicitly identified by the latest designated partner `account02/B15`: an invertible indefinite physical pair whose Schur complement contains a genuinely indefinite two-coordinate quadratic remainder with **both Schur diagonal coefficients nonzero**. The result is matrix-dependent; it does not solve the global aggregate-before-inversion problem.

Source-pinned inputs used at exact scope:

1. account03/B15 physical-pair logarithmic density envelope, `math-open-problems@2f36eb6204ac8598eaf63faed15f9fa7fddffd0c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T222614Z-account03-B15-qform-auto27/REPORT.md`;
2. designated partner account02/B15 one-null-diagonal Schur theorem, `math-open-problems@1205ce188002747c102b80c97d0493985fa6fe34`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T023639Z-account02-B15-qform-auto11/REPORT.md`;
3. account04/B15 same-constant `C_0` compiler, `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

## 2. Qualitative absolute continuity is much easier than height

Let the joint law of `X in R^n` be absolutely continuous and let `A != 0` be symmetric. Then

`Q=X^TAX`

is absolutely continuous. Indeed, for every null Borel set `N`, coarea gives

`int_{Q^{-1}(N)} |grad Q(x)| dx = 0`.

Since `grad Q(x)=2Ax` vanishes only on the proper subspace `ker A`, the set `Q^{-1}(N)` is Lebesgue-null. Hence every absolutely continuous input law assigns it probability zero.

This uses neither rank three nor the density cap and gives no quantitative `L^infinity` information.

## 3. A target-level logarithmic-potential compiler

For `L>0`, write

`K_L(x)=log_+(L/|x|)`.

Then exactly

`||K_L||_1=2L`,

and

`||K_L||_2^2=2 int_0^L log^2(L/x) dx =4L`,

so

`||K_L||_2=2 sqrt(L)`.

Therefore, for every `L,M>0` and every shift `c`, Cauchy-Schwarz gives

`boxed( sup_t int K_L(t-x) K_M(x-c) dx <=4 sqrt(LM). )`     (3.1)

Consequently, if a probability density `g` satisfies

`g(x) <= A + B K_M(x-c)`

almost everywhere, then

`boxed( sup_t int K_L(t-x) g(x) dx <=2AL+4B sqrt(LM). )`     (3.2)

No smoothness or pointwise decay of a characteristic function is used. The statement is purely a positive-kernel estimate.

## 4. Uniform logarithmic potential of an arbitrary affine indefinite pair

Let `U,V` be independent cap-one random variables and let

`R(U,V)=aU^2+2sUV+bV^2+alpha U+beta V+gamma`,

where

`E=[[a,s],[s,b]]`

is invertible and indefinite. Put

`delta=|det E|`, `nu=sigma_min(E)`.

The completed physical-pair logarithmic envelope gives, for every `rho>0`, a center `c` depending on the affine coefficients such that

`p_R(x) <= 2sqrt(2)/rho + delta^(-1/2) K_{2rho^2/nu}(x-c).`     (4.1)

Apply (3.2). For every `L>0`,

`sup_t E K_L(t-R)`

`<=4sqrt(2)L/rho +4delta^(-1/2) sqrt( L * 2rho^2/nu )`

`=4sqrt(2) [ L/rho + rho sqrt(L)/sqrt(delta nu) ].`          (4.2)

The two terms balance at

`rho=(L delta nu)^(1/4)`.

Hence

`boxed( sup_t E log_+(L/|R-t|)
        <=8sqrt(2) L^(3/4) (delta nu)^(-1/4). )`               (4.3)

This is the new regularity lemma. It says that the logarithmic singularity of one indefinite physical pair is itself sufficiently square-integrable to average a second logarithmic singularity. In particular, no exact zero diagonal is needed in the inner pair.

## 5. Nested indefinite-pair theorem

Split ORIGINAL coordinates as `X=(P,Z)`, with `P=(X_1,X_2)`, and write

`A=[[D,B],[B^T,C]]`,

where `D` is an invertible indefinite physical `2x2` principal block. Define

`Delta=|det D|`, `kappa=sigma_min(D)`,

`S=C-B^T D^(-1) B`.

Assume that among the remaining ORIGINAL coordinates there are two, `U,V`, such that the physical `2x2` principal block

`E=S[{U,V},{U,V}]`

is invertible and indefinite. Put

`delta=|det E|`, `nu=sigma_min(E)`.

All other Schur coefficients and every outside coupling are arbitrary.

### Theorem 5.1 — `QFORM-NESTED-INDEFINITE-PAIR-LOGLOG-v1`

For arbitrary independent cap-one marginals, the full quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= C_nested
    Delta^(-1/5) kappa^(-3/10)
    (delta nu)^(-1/10),
)`                                                                  (5.1)

where

`C_nested =5 * 2^(11/5) * 3^(-3/5)
          =11.8840163864... .`

Moreover, because the Schur rank is at least two,

`rank(A)=2+rank(S)>=4`.

Thus the completed fixed-matrix same-constant regularity compiler upgrades (5.1), after the height has been paid, to

`boxed( p_Q in C_0(R) )`                                           (5.2)

with exactly the same pointwise height constant.

### Proof

Complete the outer physical pair in the original coordinates. For every fixed value of the remaining coordinates `Z=z`, the completed pair envelope gives

`p_(Q|Z=z)(t)
 <=2sqrt(2)/r
   +Delta^(-1/2)
    K_{2r^2/kappa}(t-R(z)),`                                      (5.3)

where `R(z)=z^T S z+ell^Tz+c`.

Now condition on all Schur coordinates except `U,V`. The resulting polynomial in `U,V` has quadratic matrix exactly `E` and arbitrary affine coefficients. Applying (4.3), uniformly in the conditioned outside variables, with

`L=2r^2/kappa`,

gives

`E K_{2r^2/kappa}(t-R(Z))`

`<=8sqrt(2)(2r^2/kappa)^(3/4)(delta nu)^(-1/4)`

`=2^(17/4) r^(3/2) kappa^(-3/4)(delta nu)^(-1/4).`              (5.4)

Average (5.3):

`p_Q(t)
 <=2sqrt(2)/r
   +2^(17/4) Delta^(-1/2) kappa^(-3/4)
      (delta nu)^(-1/4) r^(3/2).`                                (5.5)

Write the second coefficient as `B0`. For `a/r+B0 r^(3/2)`, with `a=2sqrt(2)`, the minimizing radius satisfies

`r^(5/2)=2a/(3B0)`.

At that point the second term equals `(2/3)` of the first, so the minimum is `(5/3)` times the first term. Direct simplification yields exactly (5.1).

Every conditioning step is on original coordinates only. No spectral rotation is used to preserve independence. Continuity enters only after (5.1), through the same-constant rank-at-least-three compiler. QED.

## 6. Exact target family crossing the partner's one-null endpoint

Let

`Q_theta=4XY+U^2+2UV+theta V^2`,

for independent cap-one `X,Y,U,V` and `0<=theta<1`.

The matrix is block diagonal with

`D=[[0,2],[2,0]]`

and

`E_theta=[[1,1],[1,theta]].`

The outer eigenvalues are `2,-2`. The inner eigenvalues are

`lambda_+- = (1+theta +- sqrt((1-theta)^2+4))/2`.

For every `0<=theta<1`, `lambda_+>1`. Hence every `Q_theta` lies in the exact owner target: at least three eigenvalues have modulus at least one.

For `0<theta<1`, both Schur diagonal coefficients are nonzero and

`delta_theta=1-theta`,

`nu_theta=( sqrt((1-theta)^2+4)-(1+theta) )/2.`

The new theorem gives

`boxed(
 ||p_(Q_theta)||_infinity
 <=5*2^(3/2)*3^(-3/5)
   [ (1-theta) nu_theta ]^(-1/10),
 p_(Q_theta) in C_0.
)`                                                                  (6.1)

For the concrete range `0<theta<=1/2`, `nu_theta` decreases in `theta`, so

`(1-theta)nu_theta >= (sqrt(17)-3)/8`.

Therefore

`boxed(
 sup_{0<theta<=1/2} ||p_(Q_theta)||_infinity
 <8.903,
)`                                                                  (6.2)

with a `C_0` representative for every member of the family.

This is a genuine both-nonzero-diagonal extension of the designated partner's newest chamber.

## 7. Designated partner account02/B15 applied at an actual inequality

At the endpoint `theta=0`, the newest completed account02/B15 theorem applies directly. It gives

`boxed(
 ||p_(Q_0)||_infinity
 <=2+2log2
 =3.3862943611...,
)`                                                                  (7.1)

for

`Q_0=4XY+U^2+2UV`.

The same source also records the majority-sheet interval estimate

`Pr{Q_0 in I, Q_0>=-V^2} <= pi |I|.`                              (7.2)

Since `rank(Q_0)=4`, the same-constant `C_0` compiler yields

`p_(Q_0) in C_0`

without changing (7.1). Thus the exact family `Q_theta` is now quantitatively paid on the partner's one-null endpoint and on a full open collar of genuinely two-nonzero-diagonal Schur remainders.

## 8. Boundedness versus continuity

The logical hierarchy is now explicit.

1. `A!=0` plus an absolutely continuous joint input law implies qualitative absolute continuity of `X^TAX`.
2. The interval/height estimate is a separate problem. The new nested-pair theorem pays it directly in the stated chamber.
3. For the cap-one product problem with `rank(A)>=3`, the completed fixed-matrix theorem supplies a `C_0` representative. Hence any independently proved interval domination `P(Q in I)<=M|I|` transfers to that representative with the identical constant `M`.
4. No target-uniform modulus of continuity follows; earlier source-pinned phase-aligned constructions already rule out such a class-uniform modulus.

## 9. Remaining connection to full QFORM

The new theorem removes one local regularity/height gap: after paying an outer indefinite physical pair, a genuinely indefinite Schur pair with both diagonal coefficients nonzero is now controlled by log-envelope self-convolution.

The global conjecture is still OPEN because `s_3(A)>=1` does not force one outer physical pair and one nested Schur pair with the four reciprocal parameters in (5.1) uniformly nondegenerate. The remaining work is still aggregate-before-inversion: convert diffuse/high-dimensional spectral mass into a grouped, ridge, crossing, or other product-preserving receiver before paying reciprocal local minors.
