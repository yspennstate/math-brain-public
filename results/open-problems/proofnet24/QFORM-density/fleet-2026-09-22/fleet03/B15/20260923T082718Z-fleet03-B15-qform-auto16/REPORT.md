SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T08:27:18Z.
attacking: Gaussian heat-mode Gibbs information identities and a mode-localized application of the partner one-sheet interval theorem.

# QFORM B15 — Gaussian heat-mode Gibbs information compiler

**Run:** `20260923T082718Z-fleet03-B15-qform-auto16`  
**Status:** `PROVED_SUPPORTING_REGULARITY/INFORMATION_LEMMAS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source state

The owner target is unchanged: for independent real coordinates with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, support, log-concavity, Gaussian, connected-support, or post-rotation independence assumption is made.

Fresh owner control is revision `2026-09-22.15`. I explicitly avoid the live refuted interfaces: law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive moments of worst conditional projection caps, generic X-ray control of the two-sheet trace, post-rotation independence, and uniform matrix-perturbation continuity.

The completed partner result applied below is fleet04/B15 r5:

`yspennstate/math-open-problems@728598f48c29cbf4f15e04312727663abeccb0af`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T232152Z-fleet04-B15-ruled-trace-regularity-r5/REPORT.md`.

For the exact rank-three form

`Q=lambda_1 Y_1^2+lambda_2 Y_2^2-mu Y_3^2`,

with `lambda_1,lambda_2,mu>0`, that report proves domination of the positive one-sheet submeasure by `C_lambda dx`, where

`C_lambda=(lambda_1 lambda_2 mu)^(-1/2) integral_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`.

If `s=min(lambda_1,lambda_2,mu)`, scaling its displayed estimate gives

`C_lambda <= pi sqrt(2)/s`.                                      (1.1)

The opposite two-sheet side is not controlled by that theorem.

## 2. Heat modes and their Gibbs posterior

Let `P` be any probability law on a source space, let `Z` be any real measurable random variable, and for `epsilon>0` define

`gamma_epsilon(u)=(sqrt(2pi) epsilon)^(-1) exp(-u^2/(2 epsilon^2))`,

`H_epsilon(y)=E_P gamma_epsilon(Z-y)`.

Because `H_epsilon` is continuous and tends to zero at infinity, it has a global maximizer `y_*`. Put

`M_epsilon=H_epsilon(y_*)`,

and define the Gaussian Gibbs posterior `nu_*` on the original source space by

`d nu_*/dP = gamma_epsilon(Z-y_*)/M_epsilon`.                     (2.1)

Let

`U=(Z-y_*)/epsilon`.                                               (2.2)

The previous fleet03/B15 mode theorem gives, and the one-line proof is repeated for completeness,

`H_epsilon(y_*+epsilon v)/H_epsilon(y_*)`
` = E_(nu_*) exp(vU-v^2/2) <=1`

for every real `v`. Hence

`boxed(E_(nu_*) exp(vU) <= exp(v^2/2) for all v in R.)`            (2.3)

In particular

`E_(nu_*) U=0`, `E_(nu_*) U^2<=1`.                                (2.4)

No moment of the original law `P` is used.

## 3. Exact inverse-weight and entropy identities

The normalization (2.1) can be inverted exactly. Since

`dP/dnu_* = M_epsilon/gamma_epsilon(Z-y_*)`
` = sqrt(2pi) epsilon M_epsilon exp(U^2/2)`,

integrating with respect to `nu_*` gives

`boxed(1=sqrt(2pi) epsilon M_epsilon E_(nu_*) exp(U^2/2).)`        (3.1)

Therefore

`boxed(M_epsilon = [sqrt(2pi) epsilon E_(nu_*) exp(U^2/2)]^(-1).)` (3.2)

This is an exact height identity, not an estimate.

The relative entropy of the Gibbs posterior is also exact:

`D(nu_*||P)`
`=E_(nu_*) log(gamma_epsilon(Z-y_*)/M_epsilon)`
`=-log(sqrt(2pi) epsilon M_epsilon)-(1/2)E_(nu_*)U^2`.

Using (3.1),

`boxed(D(nu_*||P)=log E_(nu_*) exp(U^2/2)-(1/2)E_(nu_*)U^2.)`       (3.3)

Equivalently,

`boxed(epsilon M_epsilon=(2pi)^(-1/2)`
`       * exp[-D(nu_*||P)-(1/2)E_(nu_*)U^2].)`                    (3.4)

The right side is finite automatically. At a heat mode the second moment in (3.4) is a variance by (2.4), and it lies in `[0,1]`.

### Product-source decomposition

For the QFORM source law `P=product_i P_i` on the original independent coordinates, the entropy chain rule gives

`boxed(D(nu_*||P)=I_(nu_*)(X_1;...;X_n)+sum_i D((nu_*)_i||P_i),)` (3.5)

where

`I_(nu_*)=D(nu_*||product_i (nu_*)_i)>=0`.

Thus the quadratic Gibbs tilt pays its height through an exact combination of marginal information cost and dependence created from the original product source. This keeps product provenance in the original coordinates; no spectral rotation is made.

## 4. Exact spectral-scale information criterion for the full conjecture

Let `s_3(A)` be the third largest singular value of `A`, and let `C_*` denote the optimal universal density-height constant for the owner target, interpreted in the extended sense through Gaussian heat height if bounded density has not yet been established.

The completed heat-height theorem used in the preceding B15 work says for every probability law `mu`,

`sup_(epsilon>0,y) (mu*gamma_epsilon)(y)`

equals its bounded-density norm, with value `+infinity` if it has no bounded density.

Scalar homogeneity and heat-semigroup monotonicity give the exact one-scale form

`boxed(C_*=sup_(s_3(A)>=1, product P) s_3(A) max_y E gamma_1(X^TAX-y).)` (4.1)

For completeness: scale `A` to `B=A/s_3(A)`, so `s_3(B)=1`. For `0<epsilon<=1`, the target matrix `B/epsilon` satisfies

`s_3(B/epsilon) max_y E gamma_1(Q_B/epsilon-y)`
`=max_y E gamma_epsilon(Q_B-y)`.

For `epsilon>1`, the heat maximum is no larger than its value at scale one. Taking the supremum over scales recovers the heat-height theorem exactly.

Now take a global **unit** heat mode `y_*` for each target instance and its Gibbs posterior `nu_*`. Equations (3.2)-(3.4) yield

`boxed(C_*=(2pi)^(-1/2) sup s_3(A)/E_(nu_*) exp((Q-y_*)^2/2).)`     (4.2)

and

`boxed(C_*=(2pi)^(-1/2) sup s_3(A)`
` * exp[-D(nu_*||P)-(1/2)Var_(nu_*)(Q-y_*)].)`                    (4.3)

Consequently the full bounded-density conjecture is equivalent to a logarithmic Gibbs-information lower bound. Precisely, `C_*<infinity` iff there is a finite `K` such that every target instance and every global unit heat mode satisfy

`boxed(D(nu_*||P)+(1/2)Var_(nu_*)(Q-y_*) >= log s_3(A)-K.)`        (4.4)

The sharp additive constant is

`K_*=log(sqrt(2pi) C_*)`.                                        (4.5)

Since the mode posterior obeys `Var_(nu_*)(Q-y_*)<=1`, finiteness is equivalently reduced, up to only an additive `1/2`, to

`D(nu_*||P) >= log s_3(A)-O(1)`.                                 (4.6)

Indeed, (4.6) with constant `K` gives `C_*<=e^K/sqrt(2pi)`, while `C_*<=C` implies

`D(nu_*||P) >= log s_3(A)-log(sqrt(2pi)C)-1/2`.                  (4.7)

Combining (3.5) with (4.6) identifies the remaining product-preserving obligation: show that the unit Gaussian quadratic tilt necessarily creates `log s_3(A)-O(1)` total marginal KL plus multi-information. This is a reformulation, not yet the missing lower bound.

## 5. Actual application of the completed fleet04/B15 one-sheet result

The preceding exact information criterion becomes quantitative on the partner's ruled one-sheet branch.

Consider the exact rank-three signature `(+,+,-)` and let

`s=min(lambda_1,lambda_2,mu)`.

Let `mu_+` be the restriction of the law of `Q` to `[0,infinity)`. The partner theorem and (1.1) give

`mu_+ <= B dx`, `B<=pi sqrt(2)/s`.                                (5.1)

Fix any heat scale `epsilon`, let `y_*` be a global heat mode, and let `nu_*` be its posterior. If `y_*>0`, then on `{Q<0}`,

`U=(Q-y_*)/epsilon <= -y_*/epsilon`.

The 1-subgaussian posterior bound (2.3) therefore gives

`nu_*(Q<0) <= exp[-y_*^2/(2epsilon^2)]`.                          (5.2)

But by the definition of the posterior,

`(mu_+*gamma_epsilon)(y_*)`
`=M_epsilon nu_*(Q>=0)`,                                         (5.3)

while (5.1) implies

`(mu_+*gamma_epsilon)(y_*)<=B`.                                  (5.4)

Hence the completed partner result yields the new mode-localized inequality

`boxed(M_epsilon <= [pi sqrt(2)/s]`
`       / [1-exp(-y_*^2/(2epsilon^2))])`                          (5.5)

for every positive global mode. In particular, if

`y_*/epsilon >= sqrt(2 log 2)=1.177410...`,                       (5.6)

then

`boxed(M_epsilon <= 2pi sqrt(2)/s = 8.885766.../s.)`              (5.7)

For signature `(+,-,-)`, reflect `Q` and the identical assertion holds on the negative majority-sign side. Thus any exact-rank-three obstruction not already paid by (5.7) must have all maximizing heat centers either on the minority-sign side or inside the critical window of width `sqrt(2log2) epsilon` around the cone vertex.

At unit scale, combining (5.7) with the exact entropy identity gives, on every such deep majority-sign heat mode,

`boxed(D(nu_*||P)+(1/2)Var_(nu_*)(Q-y_*)`
`       >= log s-log(4pi sqrt(pi)).)`                             (5.8)

Here `log(4pi sqrt(pi))=3.103389...`. Equation (5.8) is an actual spectral-scale information payment derived from the completed partner theorem, not merely a restatement of it.

## 6. What this does and does not prove

1. The identities (3.1)-(3.5) are exact for arbitrary probability laws and require no input moments.
2. The criterion (4.4) is target-level and matches all owner quantifiers; proving its right side uniformly would prove the full universal `L^infinity` conjecture.
3. Equation (5.5) applies the completed fleet04/B15 theorem to a new inequality and removes all deep majority-sign heat modes from the unresolved exact-rank-three geometry.
4. The hard endpoint remains: prove the logarithmic information cost, or the corresponding heat/small-ball estimate, for minority-sign/near-vertex modes and then for arbitrary additional spectral directions while retaining original-coordinate product structure.
5. This report does **not** prove a new continuity theorem. Essential boundedness and continuity remain logically separate. The shared claim file still marks the full continuous-representative assertion open. Existing source reports contain fixed-instance `C_0` statements, but they are not promoted here beyond their stated scope.
6. Nothing here uses a law-uniform pointwise oscillatory decay, arbitrary-joint coarea, fiber supremum, bounded conditional-cap moment, bounded fragment count, or matrix-norm genericization.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.
