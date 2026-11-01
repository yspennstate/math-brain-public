SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T22:05:07Z.

attacking: quantitative output regularity on the live product-preserving Fourier/decoupling branches, and its exact connection to the fleet04/B15 heat-height normal form.

# fleet03/B15 r19 — endpoint Hölder regularity and quantitative heat recovery

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_REGULARITY_LEMMA`. The full QFORM universal constant remains OPEN. Execution is `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and scope

The owner target is unchanged: independent real coordinates with densities `0<=f_i<=1`, real symmetric `A`, and at least three eigenvalues of absolute value at least one. The central unpaid statement is one dimension- and matrix-independent bound on `||p_{X^TAX}||_infinity`. Continuity is separate.

This report does **not** claim the universal height theorem. It proves a quantitative regularity upgrade on every branch for which the current product-preserving arguments give an absolute Fourier tail of order `|t|^{-3/2}`. In particular it applies to the completed decoupling/Brascamp-Lieb Theorem D and Fresnel/Brascamp-Lieb Theorem F below, while preserving arbitrary measurable cap-one input densities.

Corrections respected: no law-uniform one-dimensional pointwise van-der-Corput estimate is used; no arbitrary-joint coarea bound is used; no conditional projection-density positive moment is used; no rotation is declared to preserve independence; no reciprocal physical minor is introduced.

## 2. Dependency actually used: current product-preserving Fourier branches

Source: `yspennstate/math-open-problems@1b86f205262fdfdba6fd1f1166fcc9f7ea75828c`, path
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Its Theorem D states the following. For a physical coordinate cut `I,J`, put `M=A_IJ`,

`Z=e_3(M^T M)=sum_{|S|=|T|=3} det(M_ST)^2`,

and use the volume-sampling weights `w_ST=det(M_ST)^2/Z`, with row marginals `alpha_i=P_w(i in S)`. If every `alpha_i<=1/2`, then the **full** quadratic form, with arbitrary diagonal blocks and affine terms, satisfies

`|phi_Q(t)| <= K_D |t|^{-3/2}`,

where

`K_D=(2*pi)^(3/2) exp(3/4) Z^(-1/4)`,

and the source also proves

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)`.

The same source's Theorem F gives, on its stated diffuse three-square-plus-diagonal branch,

`|phi_Q(t)| <= K_F |t|^{-3/2}`

with

`K_F=(4*pi)^(3/2) Delta^(-1/2)`,

`Delta=|lambda_1 lambda_2 lambda_3| det(G_I)`,

and `||p_Q||_infinity<=12 Delta^(-1/3)`.

These source theorems are used only in their exact scopes.

## 3. New analytic lemma: `|t|^{-1-alpha}` gives endpoint `C^{0,alpha}`

Let `mu` be a probability law on `R` with characteristic function `phi`, and suppose that for some `0<alpha<1` and `K<infinity`,

`|phi(t)| <= K |t|^(-1-alpha)` for every `t!=0`.

Then `phi in L^1`, because also `|phi|<=1`. Hence Fourier inversion gives a representative `p in C_0(R)`. More quantitatively,

`[p]_{C^{0,alpha}} <= (2^(1-alpha) K)/(pi alpha(1-alpha))`.

### Proof

For `h!=0`, Fourier inversion and `|e^{-ith}-1|<=min(2,|h t|)` give

`|p(x+h)-p(x)|`
` <= (1/pi) int_0^infinity min(2,|h|t) K t^(-1-alpha) dt`.

Split at `T=2/|h|`. The first part is

`K |h| int_0^T t^(-alpha) dt = K 2^(1-alpha)|h|^alpha/(1-alpha)`,

and the second is

`2K int_T^infinity t^(-1-alpha) dt = K 2^(1-alpha)|h|^alpha/alpha`.

After the prefactor `1/pi`, this is exactly

`(2^(1-alpha)K)/(pi alpha(1-alpha)) |h|^alpha`.

No continuity of any input density is assumed.

At the live exponent `alpha=1/2`,

`[p]_{C^{0,1/2}} <= (4 sqrt(2)/pi) K`.          (3.1)

## 4. New Theorem D regularity corollary

Under the exact hypotheses of source Theorem D,

`p_Q in C_0(R) cap C^{0,1/2}(R)`

and

`[p_Q]_{C^{0,1/2}} <= 16 sqrt(pi) exp(3/4) Z^(-1/4)`.       (4.1)

Indeed substitute `K_D` into (3.1):

`(4sqrt(2)/pi)(2pi)^(3/2)=16sqrt(pi)`.

If `sigma=s_3(M)>0`, then

`Z=e_3(M^TM) >= s_1(M)^2 s_2(M)^2 s_3(M)^2 >= sigma^6`,

so the completely explicit singular-value form is

`||p_Q||_infinity <= 6 sqrt(e)/sigma`,

`[p_Q]_{C^{0,1/2}} <= 16 sqrt(pi) exp(3/4) sigma^(-3/2)`.    (4.2)

Thus this branch gives not merely an essentially bounded output but a quantitative rough-input continuous representative. The conclusion is uniform over every allowed choice of the one-dimensional measurable densities once the displayed cross-block parameter is fixed.

Numerically the two universal prefactors in (4.2) are

`6 sqrt(e) = 9.89232762420077`,

`16 sqrt(pi) exp(3/4) = 60.03655730899482`.

## 5. Assigned partner application: quantitative Gaussian heat recovery

Completed partner: `fleet04/B15`, `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

That theorem proves for every probability law `mu`, with

`gamma_epsilon(u)=exp(-u^2/(2 epsilon^2))/(sqrt(2pi) epsilon)`,

that

`sup_{epsilon>0,y} (mu*gamma_epsilon)(y)=||p_mu||_infinity`

(with `+infinity` if no bounded density exists), and if `p in C_0`, the heat maxima increase to `max p` as `epsilon downarrow0`.

I apply this partner theorem to (4.1), obtaining an explicit **rate**, not merely convergence. Let `G~N(0,1)` and

`m_{1/2}=E|G|^(1/2)=2^(1/4) Gamma(3/4)/sqrt(pi)`.

For every `y`,

`|(p_Q*gamma_epsilon)(y)-p_Q(y)|`
` <= [p_Q]_{C^{0,1/2}} E|epsilon G|^(1/2)`
` <= 16 sqrt(pi) exp(3/4) Z^(-1/4) m_{1/2} sqrt(epsilon)`.

Since `p_Q in C_0` attains its maximum, the partner heat maximum

`H_epsilon=sup_y E gamma_epsilon(Q-y)`

therefore obeys the actual inequality

`0 <= ||p_Q||_infinity-H_epsilon`
` <= 16*2^(1/4)*exp(3/4)*Gamma(3/4) Z^(-1/4) sqrt(epsilon)`.   (5.1)

The universal prefactor is

`16*2^(1/4)*exp(3/4)*Gamma(3/4)=49.3607941699884`.

Using `Z>=sigma^6`,

`0 <= ||p_Q||_infinity-H_epsilon <= 49.3607941699884 sigma^(-3/2) sqrt(epsilon)`.   (5.2)

This is a direct quantitative application of the assigned partner result to the live QFORM inequality.

## 6. Fresnel branch corollary

Under the exact hypotheses of source Theorem F,

`p_Q in C_0 cap C^{0,1/2}` and

`[p_Q]_{C^{0,1/2}} <= 32 sqrt(2pi) Delta^(-1/2)`.            (6.1)

Applying the same fleet04/B15 heat theorem gives

`0<=||p_Q||_infinity-H_epsilon`
` <= 32*2^(3/4)*Gamma(3/4) Delta^(-1/2) sqrt(epsilon)`.       (6.2)

Again this uses the full product-preserving Fourier estimate before taking absolute Fourier values; it does not invoke the refuted one-dimensional phase decay claim.

## 7. Relation to the exact full target

The previous B15 run proved the exact single-scale normal form

`C_* = sup_{s_3(A)>0,f,y} s_3(A) E gamma_1(X^TAX-y)`.

On the Theorem D branch, (4.2) and the partner heat theorem immediately give

`s_3(A) sup_y E gamma_1(Q-y) <= 6 sqrt(e) s_3(A)/s_3(A_IJ)`

whenever the source volume-sampling leverage hypothesis holds. Thus any product-preserving cut satisfying

`s_3(A_IJ) >= eta s_3(A)`

with the same leverage condition closes that instance with the universal branch constant

`6 sqrt(e)/eta`.

The missing implication is structural, not regularity: the bare three-large-eigenvalue hypothesis does **not** currently force such a cross cut with universal `eta`, and the live correction ledger contains families defeating several one-block/one-minor substitutes. Consequently (4.1)-(6.2) are supporting regularity theorems, not a solution of full QFORM.

## 8. Exact status ledger

- Absolute continuity for every nonzero quadratic polynomial under an absolutely continuous joint input: already proved qualitatively.
- Every fixed rank-`>=3` product target: independently reviewed as having a matrix-dependent bounded `C_0` density; see fleet02/B15 r11.
- New here: any current `|t|^{-3/2}` product-preserving QFORM branch automatically has a **quantitative `1/2`-Hölder density**, with explicit constants, plus an explicit `O(sqrt(epsilon))` rate from Gaussian heat height to the true peak.
- Full dimension- and matrix-independent height constant: **OPEN**.

The next B15 implication is to look for a similarly quantitative regularity/heat estimate on the residual near-degenerate grouped-bank branch where no single physical cross block retains a universal third singular value. The useful interface is now exact: any branch giving a tail `K|t|^{-1-alpha}` yields both `C^{0,alpha}` output regularity and a partner-compatible heat recovery rate.
