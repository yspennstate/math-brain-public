# account02/B16 — projection-product interaction: curved-shell copula obstruction and integrated weighted-Wiener criterion

Status: **SUPPORTING THEOREMS PROVED / FULL TARGET OPEN**

Programme: `QFORM-DENSITY-3EIG-20260922`

Run: `20260922T115600Z-account02-B16-qform-projprod`

Execution: `WITHOUT_VERIFIED_BRAIN`; no native learned-memory receiver was used.

## 1. Source pins and live assignment

Fresh owner controls were read from `yspennstate/math-research-brain` main commit `00bd16396410aae9a7bc394e03e733be30a801a6`, control revision `2026-09-22.5`. This later owner order supersedes the stale FEI text attached to the scheduler: all workers are on the quadratic-form bounded-density conjecture.


The scientific source repository was resolved at `yspennstate/math-open-problems` master commit `92717ee3ab720389cb84a8941c62810b5a2fd605` before the derivation.

Named completed other-account result actually used: account03/B05, run `20260922T113800Z-account03-B05-qform-r11`, report blob `6e4da2dbfb380b2b0d1ff2a9723ec7b4422942ca`. That theorem proves the full-density bound for a full nonzero small-leverage spectral support from a Fourier–Brascamp–Lieb `L^1` bound, and identifies the exact unpaid interface when only three large eigenvalues are selected: the complementary quadratic phase turns the projected density into a phase-weighted complex density, for which ordinary projection `L^infinity` control does not preserve the Wiener norm. The assigned account03/B16 partner had no completed current-qform artifact visible at the pinned master, so no stale artifact was substituted.

Corrections consumed: `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, and `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`. No pointwise law-uniform oscillatory decay, rotation-preserves-independence, or fiber-supremum premise is used below.

## 2. Exact obstruction: even bounded 1D and 2D coordinate marginals do not control an indefinite quadratic pushforward

The known statement “a bounded joint projection density is insufficient” can be sharpened substantially. The following construction shows that even retaining all coordinate marginals of orders one and two, with the same `L^infinity` cap, still loses the curved dependence needed by the quadratic map.

### Theorem 2.1 (curved-shell copula obstruction)

For every `0<epsilon<=1/2` there exists a probability density `h_epsilon` on `R^3` such that

1. `0<=h_epsilon<=1`;
2. every one-coordinate marginal density is bounded by `1`;
3. every two-coordinate marginal density is bounded by `1`;
4. for the rank-three indefinite form

   `q(x,y,z)=x^2+y^2-z^2`,

   whose three eigenvalues have absolute value `1`, the random variable `q(Y)` for `Y~h_epsilon` is exactly uniform on `[-epsilon,epsilon]`.

Consequently

`||p_{q(Y)}||_infinity = 1/(2 epsilon) -> infinity`.

Thus no implication of the form

`bounded joint density + bounded coordinate marginals through dimension 2 => bounded quadratic pushforward density`

can be dimension-free, even in dimension three and even with the strongest unit caps. This is an obstruction to an intermediate reduction, not a counterexample to the owner conjecture, because `h_epsilon` is dependent rather than a product law.

### Proof

Let `L=log 2` and

`W = 1/(epsilon L)`.

Choose `R` so large that

`R >= 4/L`,

`R^2 >= 2(W^2+epsilon)`.

On the parameter box

`D=[R,2R] x [0,W] x [-epsilon,epsilon]`

with coordinates `(u,w,s)`, define

`v=(s-w^2)/u`,

`x=(u+v)/2`, `y=w`, `z=(u-v)/2`.

This map is injective: from `(x,y,z)` one recovers `u=x+z`, `w=y`, and `s=x^2+y^2-z^2`. Its Jacobian has absolute value

`|det d(x,y,z)/d(u,w,s)| = 1/(2u)`,

and identically

`x^2+y^2-z^2=s`.

Let `E_epsilon` be the image of `D` and set `h_epsilon=1_{E_epsilon}`. Its volume is

`|E_epsilon| = int_R^{2R} int_0^W int_{-epsilon}^{epsilon} (2u)^(-1) ds dw du`

`= epsilon W log 2 = 1`,

so `h_epsilon` is a probability density and `h_epsilon<=1`.

For fixed `s`, the pushforward density under `q` is

`int_R^{2R} int_0^W (2u)^(-1) dw du = W log 2 / 2 = 1/(2epsilon)`.

Hence `q(Y)` is exactly uniform on `[-epsilon,epsilon]`.

It remains to record the marginal caps. For `y=w`,

`p_y(w)=int_R^{2R} int_{-epsilon}^{epsilon}(2u)^(-1) ds du = epsilon log 2 <=1`.

For fixed `(w,s)`,

`partial_u x = (1+(w^2-s)/u^2)/2 >=1/4`,

`partial_u z = (1+(s-w^2)/u^2)/2 >=1/4`

by the choice of `R`. Pushing the parameter measure `(2u)^(-1)du dw ds` to `x` or `z` therefore gives

`p_x, p_z <= (2/R)(2epsilon W)=4/(R log 2)<=1`.

The same calculation without integrating in `w` gives the two-coordinate marginals

`p_{x,y}, p_{z,y} <= 4epsilon/R <=1`.

Finally, for fixed `(x,z)`, put `u=x+z`, `v=x-z`. The allowed `y=w` satisfy

`|uv+w^2|<=epsilon`, `0<=w<=W`.

The allowed interval in `w^2` has length at most `2epsilon`; therefore its interval in `w>=0` has length at most `sqrt(2epsilon)<=1`. Thus

`p_{x,z}(x,z)<=sqrt(2epsilon)<=1`.

All one- and two-coordinate marginal bounds follow. QED.

### Interpretation

The obstruction is a pure copula effect: the dependence bends a unit-height density along the indefinite cone while its low-order coordinate marginals remain harmless. Therefore a projection theorem cannot be followed by a step that forgets *how* the projected density arose from the original independent coordinates. The product remnant must survive into the nonlinear phase calculation.

## 3. A weaker sufficient interface than uniform phase-weighted Wiener control

Account03/B05 isolates the weighted-Wiener debt after selecting three large spectral directions. A useful strengthening is that **uniform-in-time** control of that Wiener norm is not necessary. A weighted time average is enough.

Let `S` be the span of three orthonormal eigenvectors of `A` with eigenvalues `lambda_1,lambda_2,lambda_3`, each satisfying `|lambda_j|>=1`. Let `R` be the `3 x n` matrix whose rows are those eigenvectors, let `Lambda=diag(lambda_1,lambda_2,lambda_3)`, and write the exact spectral split

`A = R^T Lambda R + B`,

where `B` annihilates `S`.

For independent input `X`, set `Y=RX`. For each real `t`, define the complex phase-weighted projected measure

`mu_t(E)=E[ exp(i t X^T B X) 1_{Y in E} ]`.

Whenever it has density `g_t`, its Fourier transform is the source-exact quantity

`Psi_t(xi)=E exp(i <xi,RX> + i t X^T B X)`.

Put

`W(t)=int_{R^3} |Psi_t(xi)| dxi`.

### Theorem 3.1 (integrated weighted-Wiener criterion)

Assume `W(t)<infinity` for almost every `|t|>=1` and that for one universal finite `K`,

`int_{|t|>=1} |t|^(-3/2) W(t) dt <= K`.                    (3.1)

Then the full quadratic form `Q=X^T A X` has a continuous density and

`||p_Q||_infinity <= 1/pi + K/(16 pi^(5/2))`.              (3.2)

Thus, in the three-large-eigenvalue problem, it is enough to prove the averaged weighted-Wiener estimate (3.1); one does **not** need the stronger pointwise bound `sup_t W(t)<infinity`.

### Proof

The characteristic function of `Q` is

`Phi(t)=int_{R^3} exp(i t y^T Lambda y) g_t(y) dy`.

Use the same Gaussian-regularized Fresnel pairing as in the completed account03/B05 proof, but with `g_t` in place of the ordinary projected density. Fourier inversion gives, for `t!=0`,

`|Phi(t)| <= (4 pi |t|)^(-3/2) |det Lambda|^(-1/2) W(t)`.

Since every selected eigenvalue has absolute value at least one,

`|det Lambda|^(-1/2)<=1`.

Also `|Phi(t)|<=1` for every `t`. Therefore

`int_R |Phi(t)| dt`

`<= 2 + (4 pi)^(-3/2) int_{|t|>=1}|t|^(-3/2)W(t)dt`

`<=2+(4 pi)^(-3/2)K`.

An integrable characteristic function yields a continuous density, and Fourier inversion gives

`||p_Q||_infinity <= (2pi)^(-1)||Phi||_1`

`<=1/pi + K/(16 pi^(5/2))`.

QED.

### Corollary 3.2 (sub-square-root growth is enough)

If for `|t|>=1`

`W(t)<=C_0 |t|^beta`

with universal `C_0` and any `beta<1/2`, then (3.1) holds with

`K <= 4 C_0/(1-2 beta)`.

Thus even polynomial growth of the phase-weighted Wiener norm is admissible up to, but not including, the square-root threshold. This materially weakens the first unpaid interface in account03/B05.

## 4. Exact remaining connection to the full target

Theorem 2.1 rules out a large class of projection-only closures: even a unit joint cap plus unit caps on all one- and two-coordinate marginals cannot control the indefinite quadratic pushforward. Theorem 3.1 identifies a source-valid replacement that does retain the complementary phase.

For the **delocalized selected three-eigenspace** regime, the next precise target is therefore:

`QFORM-PHASE-WIENER-AVERAGED-v1`:

prove a universal bound

`int_{|t|>=1}|t|^(-3/2) int_{R^3}|E exp(i<xi,RX>+it X^T B X)| dxi dt <= K`

under the original product-density assumptions and a suitable small-leverage hypothesis on the selected three-dimensional spectral subspace.

This is strictly weaker than the previously stated uniform weighted-Wiener norm. If it is proved, Theorem 3.1 closes the nonlinear projection-product interaction for that regime. Failure of small leverage still belongs to the localized coordinate-minor/bilinear side of the programme.

No full-target promotion is made here. In particular, the dependent density in Theorem 2.1 is not admissible as the original independent input law; it demonstrates precisely why the product structure cannot be summarized by low-order projected density caps.

## 5. Integrity / telemetry

Model self-report: `GPT-5.6 Sol`.
Requested reasoning effort: maximum actually supported by the active model.
Configured/known reasoning effort: `UNKNOWN` (not exposed).
Provider reasoning usage: `null` / not exposed.
Elapsed execution is recorded separately in the finish receipt and is not pure thinking time.

No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, email, Drive, public posting, paid API/model, remote workflow, or permission changes are included.
