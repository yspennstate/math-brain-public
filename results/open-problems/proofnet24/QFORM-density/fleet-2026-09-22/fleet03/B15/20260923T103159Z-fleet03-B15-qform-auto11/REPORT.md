SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T10:31:59Z.
attacking: balanced Laplace-mode excision of every already-paid one-sheet submeasure, with a two-sided local packing certificate for the remaining two-sheet mass.

# QFORM B15 — balanced Laplace paid-submeasure excision

**Run:** `20260923T103159Z-fleet03-B15-qform-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / LAPLACE_PAID_SUBMEASURE_EXCISION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope

The owner target remains the unrestricted statement: independent real coordinates with probability densities `0<=f_i<=1`, arbitrary real symmetric `A`, and at least three eigenvalues of `A` of modulus at least one. No moments, support assumptions, log-concavity, Gaussianity, connectedness, or independence after a spectral rotation are assumed.

The full universal height conjecture remains open. This report isolates a new exact regularity/anti-concentration interface. It does not use the refuted law-uniform pointwise van-der-Corput route, an arbitrary-joint coarea bound, a fiber supremum, or a single tiny physical minor.

The completed partner results actually used are fleet04/B15:

1. heat-height closure, `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`;
2. rough one-sheet trace domination, `yspennstate/math-open-problems@728598f48c29cbf4f15e04312727663abeccb0af`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T232152Z-fleet04-B15-ruled-trace-regularity-r5/REPORT.md`.

The second theorem says, for the exact rank-three form

`Q=lambda_1 Y_1^2+lambda_2 Y_2^2-mu Y_3^2`, `lambda_1,lambda_2,mu>0`,

the positive one-sheet submeasure is dominated by `C_lambda dx`, where

`C_lambda=(lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta`

and if `s=min(lambda_1,lambda_2,mu)`, then `C_lambda<=pi sqrt(2)/s`.

## 2. Atomlessness and the scaled Laplace mode balance

Every target QFORM law is atomless before any density-height theorem is used. Indeed the joint input law is absolutely continuous on `R^n`, while for nonzero `A` each level set

`{x: x^T A x=t}`

is the zero set of a nonzero polynomial and hence is Lebesgue-null.

For an arbitrary atomless probability law `mu` on `R`, define the scaled Laplace kernel and its smoothing by

`ell_epsilon(u)=(2 epsilon)^(-1) exp(-|u|/epsilon)`,

`L_epsilon(y)=int ell_epsilon(q-y) dmu(q)`.

The function `L_epsilon` is continuous, vanishes at infinity, and therefore has a global maximizer `y_*`. Put

`I_+(y)=int_{q>y} exp(-(q-y)/epsilon)dmu(q)`,

`I_-(y)=int_{q<y} exp(-(y-q)/epsilon)dmu(q)`.

Atomlessness justifies differentiation through the cusp and gives

`L_epsilon'(y)=[I_+(y)-I_-(y)]/(2 epsilon^2)`.

At every global mode `y_*`,

`I_+(y_*)=I_-(y_*)`.

Since

`L_epsilon(y_*)=[I_+(y_*)+I_-(y_*)]/(2 epsilon)`,

we obtain the exact balance

`boxed(I_+(y_*)=I_-(y_*)=epsilon L_epsilon(y_*)).`       (2.1)

Thus a Laplace mode carries two equal one-sided positive budgets. This is the feature exploited below.

## 3. Paid-submeasure excision lemma

Let `G` be any event on the original source space and let

`mu_G(E)=P(Q in E, G)`

be its output submeasure. Assume only

`mu_G <= B dx`                                                (3.1)

for some finite `B`. No support relation between `G` and the mode is assumed.

At a global Laplace mode `y_*`, write `L=L_epsilon(y_*)`. Define the two half-posteriors

`dnu_+ = [exp(-(Q-y_*)/epsilon) 1_{Q>y_*}/(epsilon L)] dP`,

`dnu_- = [exp(-(y_*-Q)/epsilon) 1_{Q<y_*}/(epsilon L)] dP`.

By (2.1), both are probability measures.

Because (3.1) implies

`int_{q>y_*} exp(-(q-y_*)/epsilon)dmu_G(q) <= B epsilon`,

and similarly on the left, we get the exact one-sided excision bounds

`boxed(nu_+(G)<=B/L,  nu_-(G)<=B/L.)`                            (3.2)

Hence, whenever `L>B`,

`boxed(nu_+(G^c)>=1-B/L,  nu_-(G^c)>=1-B/L.)`                    (3.3)

This is stronger than merely saying that the full smoothed value has a large unpaid contribution: **both balanced sides of the mode must be supplied by the unpaid event**.

The full Laplace Gibbs posterior is

`dnu_L = ell_epsilon(Q-y_*) dP / L = (nu_+ + nu_-)/2`.

Therefore also `nu_L(G)<=B/L`, but (3.2) retains the additional two-sided information.

### Compact local form

For every `r>0`, the far right tail contributes at most `exp(-r)`, because on `Q>=y_*+r epsilon` the exponential weight is at most `exp(-r)` and the total probability is at most one. The same holds on the left. Combining this with (3.2) gives

`boxed(P(G^c, y_*<Q<y_*+r epsilon)`
`       >= [epsilon(L-B)-exp(-r)]_+),`                           (3.4)

`boxed(P(G^c, y_*-r epsilon<Q<y_*)`
`       >= [epsilon(L-B)-exp(-r)]_+).`                           (3.5)

If `L>B`, then `epsilon(L-B)<=epsilon L=I_+<=1`. Taking

`r_*=log[2/(epsilon(L-B))] >= log 2`

gives the symmetric local certificate

`boxed(P(G^c, y_*<Q<y_*+r_* epsilon)>=epsilon(L-B)/2,)`          (3.6)

`boxed(P(G^c, y_*-r_* epsilon<Q<y_*)>=epsilon(L-B)/2.)`          (3.7)

Thus any large mode above a paid density level `B` forces **two adjacent output intervals**, one on each side of the mode, to contain quantitatively comparable unpaid mass. This conclusion uses no continuity of the raw density.

## 4. Harmonic bank compiler

The preceding lemma aggregates cleanly across a bank of already-paid events.

Suppose events `G_1,...,G_N` satisfy

`mu_{G_j} <= C_j dx`, `C_j>0`.

Define harmonic capacities and weights

`h_j=1/C_j`, `H=sum_j h_j`, `w_j=h_j/H`,

and the weighted coverage random variable

`W=sum_j w_j 1_{G_j}`.

Applying (3.2) term-by-term gives, for each balanced half-posterior,

`E_{nu_+} W <= sum_j w_j C_j/L = N/(H L)`,

`E_{nu_-} W <= N/(H L)`.                                       (4.1)

Therefore any structural lower bound

`E_{nu_+}W >= delta`  or  `E_{nu_-}W >= delta`                   (4.2)

immediately yields

`boxed(L <= N/(H delta).)`                                      (4.3)

In particular, if a completed structural branch supplies

`H/N >= c s_3(A)`,                                              (4.4)

then (4.2) gives the target-scale estimate

`boxed(s_3(A) L <= 1/(c delta).)`                               (4.5)

This is a conditional compiler, not a claim that (4.2) or (4.4) always holds. Its value is that a putative high-height mode must make **both** balanced half-posteriors simultaneously avoid the harmonic collection of already-paid one-sheet events. This converts the obstruction from a scalar random-critical-value shadowing statement into a two-sided multi-block coverage problem.

## 5. Actual application of fleet04/B15: exact rank three

Take the completed partner form

`Q=lambda_1 Y_1^2+lambda_2 Y_2^2-mu Y_3^2`

and let

`G={Q>=0}`.

The fleet04/B15 rough trace theorem gives

`mu_G <= C_lambda dx`, `C_lambda<=pi sqrt(2)/s`,

where `s=min(lambda_1,lambda_2,mu)`.

### Majority-side Laplace modes are paid with zero loss

Let `y_*` be a global mode of `L_epsilon`. If `y_*>=0`, then the entire right half `{Q>y_*}` lies in `G`. Hence `nu_+(G)=1`. Applying (3.2) gives

`boxed(L_epsilon(y_*) <= C_lambda <= pi sqrt(2)/s.)`             (5.1)

This includes the cone vertex `y_*=0`; there is no critical-window loss and no limiting argument at the vertex.

Therefore, if an exact-rank-three instance has

`L_epsilon(y_*) > C_lambda`,

then necessarily `y_*<0`, and (3.3) says

`boxed(nu_+(Q<0)>=1-C_lambda/L,`
`       nu_-(Q<0)>=1-C_lambda/L.)`                              (5.2)

Moreover (3.4)-(3.7) show that the two-sheet side `Q<0` must place quantitative mass in adjacent intervals on **both** sides of the mode. For the optimized radius

`r_*=log[2/(epsilon(L-C_lambda))]`,

`boxed(P(Q<0, y_*<Q<y_*+r_*epsilon)>=epsilon(L-C_lambda)/2,)`    (5.3)

`boxed(P(Q<0, y_*-r_*epsilon<Q<y_*)>=epsilon(L-C_lambda)/2.)`    (5.4)

Thus the unresolved exact-rank-three obstruction is no longer “near the cone vertex” in a Gaussian-tail sense. In the balanced Laplace formulation it is **strictly a minority-sign, two-sided two-sheet packing problem**.

For signature `(+,-,-)`, apply the identical statement after replacing `Q` by `-Q`; the majority-sign side is then the negative half-line.

## 6. Gaussian comparison: removal of the old quadratic near-vertex loss

The previous fleet03/B15 Gaussian-mode theorem gave a 1-subgaussian Gibbs posterior at every global heat mode. The partner one-sheet cap yields an additional mode-shift inequality that is useful for comparison.

Let `H_epsilon(y)=E gamma_epsilon(Q-y)`, let `y_*>0` be a global mode, put `M=H_epsilon(y_*)` and `a=y_*/epsilon`. Let `nu` be the Gaussian mode posterior and `U=(Q-y_*)/epsilon`. The mode condition gives `E_nu U=0`, so Jensen implies

`H_epsilon(y_*+epsilon v)/M`
`=exp(-v^2/2) E_nu exp(vU) >= exp(-v^2/2)`                       (6.1)

for every `v>0`.

The paid part `G={Q>=0}` has Gaussian convolution at most `B=C_lambda` at every center. Hence the unpaid part at the shifted center is at least

`M exp(-v^2/2)-B`.

In posterior form this says

`E_nu[1_{Q<0} exp(vU)] >= 1-(B/M)exp(v^2/2)`.

But `Q<0` implies `U<-a`, hence the left side is at most `exp(-av)`. Therefore

`boxed(M <= B exp(v^2/2)/(1-exp(-av)),  v>0.)`                  (6.2)

For `0<a<=1`, choosing `v=1` and using `1-exp(-a)>=a/2` yields

`boxed(M <= 2 sqrt(e) B/a < 3.298 B/a.)`                        (6.3)

The earlier Gaussian tail argument behaved like `2B/a^2` as `a->0+`; (6.3) improves the near-vertex loss from quadratic to linear. At `a=0` no Gaussian posterior bound of this form can close the mode, while the Laplace balance (5.1) pays the vertex exactly. This is the reason to change mechanism rather than iterate the previous Gaussian critical-window argument.

By the completed fleet04/B15 heat-height theorem,

`sup_{epsilon>0} max_y H_epsilon(y)=||p_Q||_infinity`

(with `+infinity` if no bounded density exists), so (6.2) is an actual density-height inequality on every majority-side Gaussian mode, not merely a formal smoothing statement.

## 7. Regularity ledger

Absolute continuity itself does not require the universal conjecture: for any nonzero symmetric `A`, the product input law is absolutely continuous and the critical set of `x^T A x` is Lebesgue-null, so the one-dimensional pushforward is absolutely continuous by local coarea/submersion arguments.

The completed B15 source chain cited by fleet04 reports the stronger fixed-instance statement `p_Q in C_0(R) cap L^infinity(R)` for every rank-`>=3` target instance, with a matrix-dependent height. The consolidated shared claim file has historically lagged this source-level closure, so this run does not alter the central shared claim ledger. In any case, no continuity assumption is used in Sections 2--6.

The central universal problem is still solely the height. The new Laplace compiler shows that any failure of a universal bound, after a one-sheet component is paid, must be carried simultaneously on both sides of a balanced mode by the complementary two-sheet event.

## 8. First unpaid implication

For an ambient bank of indefinite physical three-blocks with paid one-sheet submeasures `mu_{G_j}<=C_j dx`, prove a product-preserving alternative of the following type:

1. harmonic capacity `H/N` is of order `s_3(A)` and one of the balanced Laplace half-posteriors has a universal weighted one-sheet coverage `E W>=delta`; or
2. the simultaneous low-coverage regime forced by (4.1) enters one of the completed grouped-coordinate / ridge / determinant-volume exits.

No generic X-ray estimate for the complementary two-sheet trace is sufficient; the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` remains binding.

The full QFORM conjecture is **OPEN / NOT PROVED / NOT DISPROVED**.
