# Independent audit of the Gaussian calibration transfer theorem

Date: 2026-10-24. Reviewer: B02. No frozen source or author proof was edited.

**Verdict: PASS for Theorem 2.1, Corollary 3.1, and the exact first-GD-step calibration transfer in Sections 4.1–4.3.** I independently checked the determinant concentration, cutoff vector fields, Gaussian divergence estimate, translation-in-TV argument, weak-to-TV passage, random-environment localization, coefficient normalization and the first-step imported replica theorem. No fatal mathematical gap was found. Two minor formulation improvements are recorded below; neither affects the Gaussian first-step conclusion.

This is not a vote for full T357 closure. The proof establishes an exact calibration theorem for the first actual GD step and a conditional structural transfer theorem for subsequent readouts. Later deterministic overlaps, positive-time nondegeneracy, and a trajectory/early-stopping theorem remain independent obligations.

## 1. Version and imported result

The reviewed file is `fullproof/b04_calibration_transfer.md`, 879 lines, SHA-256:

`1021b43f533f10d3c5bcd574433c141d64ae50f72f6329ed8b3307961987afcd`.

The first-step probabilistic result it imports is pinned by:

| Source | SHA-256 |
|---|---|
| `followup/T357_gaussian_first_step_attempt.md` | `1469aad3c34b902a363fe66d32eff199c451adc28d2ae5ae4de6cbb716fd630b` |
| `followup/T357_gaussian_first_step_independent_review.md` | `7c9b8412cc8d38e184972b9256773d7854cf7878b2bb2e1df5a8eafda80fc73f` |

I checked the statements and replica-to-conditional-law transfer in those files. I did not redo every line of the earlier model-specific first-step CLT; that theorem is an explicit previously audited input, not hidden in the analytic argument.

## 2. Determinant concentration: verified

Let `g=grad f`, `J=Hess f`, `a=theta.g`, and `q=(I-theta theta^T)g`. The derivative Gram determinant of `(theta.X,f(X))` is

\[
\Delta=\|g\|^2-a^2=\|q\|^2.
\]

Since `E a=E[Z f]=A`, Gaussian Poincaré and the uniform Hessian operator bound imply

\[
\operatorname{Var}(a)\leq\varepsilon^2,
\qquad
\mathbb E\Delta\geq Q-A^2-\varepsilon^2.
\]

Also `grad Delta=2Jq`, so

\[
\operatorname{Var}(\Delta)\leq4L^2\varepsilon^2.
\]

Thus `Q-A^2>=delta_*` forces the probability of `Delta<=delta_*/4` to vanish. The displayed numerical constant `16 L^2 epsilon^2/delta_*^2` is valid when `epsilon^2<=delta_*/4`.

The direction of the Poincaré inequality is correct: it supplies a lower bound on the mean derivative energy from the variance of `f`, rather than an unjustified upper bound. No inverse determinant moments are assumed. This is the crucial protection against degeneracy.

## 3. Localized Gaussian integration by parts: verified

On `Delta>0`, the proposed dual vector fields

\[
v_2=q/\Delta,\qquad v_1=\theta-a v_2
\]

satisfy `D(Z,f)v_i=e_i`. A smooth cutoff vanishing for `Delta<=delta_*/8` makes `V_i=chi(Delta)v_i` globally smooth, including the extension by zero. Because the cutoff is identically zero on a full interval, its derivatives vanish at the joining boundary.

I independently obtain

\[
\|v_2\|=\Delta^{-1/2},\qquad
\|Dv_2\|_{\mathrm{HS}}
\leq\frac{\|J\|_{\mathrm{HS}}}{\Delta}
 +\frac{\|q\|\,2\|Jq\|}{\Delta^2}
\leq\frac{3H}{\Delta}.
\]

For `v_1`, differentiate `theta-a v_2`; the new outer-product term has Hilbert–Schmidt norm at most `||grad a|| ||v_2||`, and `||grad a||<=H`. The derivatives of the cutoff add a term bounded by `||chi'|| ||grad Delta|| ||v_i||`. All of these are bounded by a constant depending only on `L,H,delta_*`, independent of input dimension.

For Gaussian divergence `d(V)=X.V-div V`, the exact identity used is

\[
\mathbb E[d(V)^2]
=\mathbb E\|V\|^2
 +\mathbb E\sum_{i,j}(\partial_iV_j)(\partial_jV_i).
\]

The second term need not be nonnegative, but its upper bound by `E||DV||_HS^2` is valid. The argument uses this upper bound, not a mistaken equality with the Hilbert–Schmidt square. Smooth truncation followed by Gaussian Sobolev approximation justifies the identity under the given bounds. The resulting estimate is dimension-free even though separately bounding `X.V` by `||X|| ||V||` would not be.

Consequently, for smooth compactly supported `psi`,

\[
\mathbb E[\chi(\Delta)\partial_i\psi(Z,f)]
=\mathbb E[\psi(Z,f)d(V_i)]
\]

is correct, with uniformly bounded right-hand signed measure.

## 4. The smoothing argument actually gives joint total variation

Let `eta` be the cutoff-weighted pushforward subprobability measure. For any translation vector `h`, apply the previous IBP identity to `psi(.-t h)` or `psi(.+t h)` and integrate over `0<=t<=1`. The result is

\[
|\langle\tau_h\eta-\eta,\psi\rangle|
\leq C\|h\|\|\psi\|_\infty.
\]

Smooth compactly supported tests determine the total variation norm of finite regular Borel measures on `R^2`. Therefore this is the claimed TV translation bound, not merely a bound in a weaker metric.

Because `mu-eta` is positive, its TV norm in the author's convention equals its mass `E[1-chi(Delta)]`. Convolution contracts TV. Hence

\[
\|\mu-\mu*\rho_r\|_{\mathrm{TV}}
\leq2\mathbb E[1-\chi(\Delta)]+Cr.
\]

The factor two is correct: one copy is needed before convolution and one after it. This avoids requiring a density for the original joint law at finite dimension.

At fixed smoothing radius, weak convergence yields pointwise convergence of the convolution densities, since a translated smooth compactly supported mollifier is a bounded continuous test. Those densities have mass one. Scheffé's lemma therefore gives `L1` convergence. Removing the mollifier after taking the dimension limit proves joint TV convergence. The order of limits is correct; the proof does not choose a shrinking smoothing radius without control.

The Gaussian covariance parameters lie in a compact set because `Q<=L^2` and `|A|<=L`. The fixed residual-variance bound keeps every limiting covariance nonsingular. The subsequence argument therefore proves approximation by the Gaussian with each dimension's own covariance, even when those covariances do not converge.

I also checked the scalar OU/characteristic-function argument in Section 2.1. Its variance identity and the constant in the characteristic-function estimate are consistent. Thus the weak Gaussian premise used by the TV argument is actually established.

## 5. Corollary 3.1: random environments and covariance convergence

The deterministic derivative inequalities for a tanh readout are valid for arbitrary training-dependent coefficients:

\[
\|\nabla f\|\leq\|F\|_{op}\|b\|_2,
\quad
\|\nabla^2f\|_{op}\leq2\|F\|_{op}^2\|b\|_\infty,
\quad
\|\nabla^2f\|_{HS}\leq2\|F\|_{op}^2\|b\|_2.
\]

No independence between `b,F` is used. The only required independence is the fresh test input from the environment.

The passage from deterministic to random environments is sound. Fix bounds on `||F||op`, `||b||2`, and the inverse residual variance. Within that bounded class, failure of uniform convergence as the Hessian operator bound tends to zero would supply a deterministic violating sequence, contradicting Theorem 2.1. Tightness makes the excluded environments arbitrarily unlikely. This is a valid localization argument; it does not require almost-sure bounds along the entire random sequence.

The variant starting from conditional weak convergence to a fixed nonsingular Gaussian is also sound. To make its covariance step explicit, on `||F||op ||b||2<=M`,

\[
\mathbb E_X S^4\leq5M^4,
\qquad \mathbb E_X Z^4=3.
\]

Thus `S^2` and `ZS` are uniformly integrable conditionally on every fixed bounded environment class. Bounded continuous truncations, conditional weak convergence in probability, and localization give `Q_d->Q`, `A_d->A` in probability. In particular `Q_d-A_d^2` is eventually bounded away from zero in probability. Gaussian covariance continuity in TV then identifies the deterministic target.

Since the TV norm is bounded by two, convergence in probability upgrades to convergence in every finite `Lp` over the environment. No unconditional fourth-moment bound is needed for this bounded output quantity.

## 6. Exact first-step transfer: verified

The author's coefficient

\[
b_j=\frac{cd}{nm}\sum_i(Y_i-1/2)\tanh(W_j^TX_i)
\]

reconstructs exactly the frozen first-step score

\[
S_{1,d}(X)=\frac{cd}{n}\sum_i(Y_i-1/2)
\left[\frac1m\sum_j\tanh(W_j^TX_i)\tanh(W_j^TX)\right].
\]

There is no missing factor of `sqrt(m)`. The distinction between the raw readout coefficient and the alternative normalized network parameter is handled correctly.

For fixed `W_j`, conditional independence across training examples permits Hoeffding. A union bound over `m=O(d)` features does not need independence across the feature coordinates. Gaussian interpolation gives

\[
|\mathbb E[(\sigma(\beta Z)-1/2)\tanh(W_j^TX)]|
\leq(\beta/4)|\theta^TW_j|.
\]

Together with `max_j |theta.W_j|=O_P(sqrt(log(d)/d))`, this proves the displayed infinity-norm decay. The second-moment calculation proves `||b||2=O_P(1)`, with the normalization in Section 4.1 intact.

The imported two-test replica theorem really supplies convergence in `L2` over the environment for each fixed bounded continuous test. A countable convergence-determining class, or the finite compact-net argument stated in the proof, converts this into conditional weak convergence in probability. It is stronger than a one-test annealed CLT, and it is the correct imported result here.

The target covariance

\[
A=ca_1^2\kappa,\qquad Q=A^2+c^2\tau^2,
\]

uses the same three variance contributions as the frozen theorem. For fixed `c>0`, finite positive aspect ratios, `tau^2>0` even if `beta=0`. Hence the nonsingularity needed by the transfer theorem holds.

Finally, exact unbinned calibration is TV-Lipschitz. The signed score measure with density `E[p(Z)|S]-sigma(S)` has variation norm equal to the calibration error; bounded multiplication and measurable pushforward contract TV. This proves the matching upper bound that weak convergence alone could not provide. The first-step CE and integrated curve limits therefore follow, and the environment `Lp` upgrades are valid because both errors are bounded.

## 7. Minor formulation improvements

1. In the completely general statement (1.4), explicitly choose an everywhere `[0,1]`-valued version of `g_nu`. A regular conditional expectation of a Bernoulli mean has such a version, but an arbitrary extension off the score marginal's support could be unbounded and invalidate the written inequality. The Gaussian calibration curve used in the theorem is already continuous and `[0,1]`-valued, so the application is unaffected.
2. The scale-free alternative (3.8) should explicitly retain `||F_d||op=O_P(1)` or say that the Gaussian-row hypothesis in its subsection supplies it. The surrounding text does supply this assumption; making it explicit would prevent misreading (3.8) as sufficient for arbitrary feature matrices.

These are clarification requests, not missing lemmas for the reviewed conclusion.

## 8. Exact acceptance boundary

| Claim | Independent review result |
|---|---|
| Dimension-free localized IBP bounds | Verified. |
| Joint weak-to-TV upgrade | Verified. |
| Conditional matched-covariance Gaussian TV for arbitrary delocalized readouts | Verified under all conditions (3.4). |
| Random-environment convergence in probability and finite `Lp` | Verified. |
| First-step coefficient delocalization and norm control | Verified. |
| Exact first-step model-conditional calibration error and integrated curve | Verified using the explicitly imported replica theorem. |
| Deterministic overlaps at all fixed GD times | Not proved by this file. |
| Nondegeneracy at every positive GD time | Requires a separate argument; an upper norm bound alone does not imply it. |
| Whole-row T357 time-dependent calibration and early stopping | Not certified by this audit. |

The proof now closes a real analytic gap for the Gaussian model. Its scope must remain distinct from the still-needed dynamics theorem.
