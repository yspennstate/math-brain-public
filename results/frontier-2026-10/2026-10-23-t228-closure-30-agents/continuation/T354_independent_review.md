# T354 independent audit: slow-step reshuffling counterexample

23 October 2026. A28. Independent reconstruction of A29's argument; no new agents and no changes to the frozen campaign.

**Verdict: PASS for the corrected version pinned below.** The construction proves that, for each fixed `q=β₂∈(0,1)` and `η₀∈(0,1]`, the specified bias-corrected, unprojected recursion with `β₁=0` has two distinct nonzero accumulation points almost surely. The stationary random-reshuffling averaged drift has its unique zero at zero and attracts the invariant interval exponentially. Therefore the interpolation is not an almost-sure asymptotic pseudotrajectory (APT) of that drift.

**A genuine gap was found and corrected during this review.** The original §7 invoked the tracking lemma on `[0,4H+4]` for a successful block only known to last at least `H`. An upper bound on a block's duration does not authorize tracking beyond its end. The corrected proof evaluates the interpolation at the fixed interior time `H`, then takes a neighboring actual slot. This proves the stated accumulation-point conclusion without an endpoint claim. I checked A29's revised paragraph, including its error budget, rather than treating the proposed correction as automatically incorporated.

The result refutes the unrestricted tracking step in local Theorem 2. It does **not** refute that theorem's weaker residual-liminf conclusion, its separately audited Theorem 3 at `η/√k`, or a claim that some suitably restricted decaying schedule converges. This review makes no novelty claim and does not close registry T354 or T357.

## 1. Exact artifacts and target

| Artifact | SHA256 |
|---|---|
| Corrected `followup/T354_T357_attempt.md` audited here | `f8475d6d92fabd7ba4c370cb7cc010d6786691d647661b4151f776bd3bc1c1e3` |
| Original, preserved at `followup/history/T354_T357_attempt_pre_tracking_horizon_fix.md` | `1ff5cd3dedf7a61f4047b96b47aca374d23df78bd74271e417f859b5c4ad9fdb` |
| Target `a03/T354_theorem.md` | `fbf6011a14d439eff8208fa14c6a0625cc66aca91eebe09b19fb0b4c4bd59f28` |
| Prior audit `a03/T354_independent_prior_audit.md` | `f5ccf97da806793c0937d77100d2f92d86ca1aa992749c8a27b86a5105034559` |

The target theorem explicitly permits `β₁=0`, assumes compact iterates, positive `B₂`, positive steps tending to zero with divergent sum, and positive epsilon or a denominator floor. Its proof step (i) asserts almost-sure APT tracking under those hypotheses. The prior audit's final section expressly leaves this tracking sketch unaudited; its acceptance concerns Theorem 3. Thus this counterexample does not overturn a tracking result previously certified by that audit.

## 2. Model and assumption check

Let `c=(-2,-1,1,2)`, `f_i(x)=(x+c_i)²/2`, and

\[
f(x)=\tfrac12x^2+\tfrac54,\qquad f'(x)=x.
\]

Epochs are independent uniform permutations of the four components. At slot `k`, with epoch `e=ceil(k/4)`, the recursion is

\[
g_k=x_{k-1}+C_k,\quad
v_k=qv_{k-1}+(1-q)g_k^2,\quad
\widehat v_k=v_k/(1-q^k),\quad
x_k=x_{k-1}-\eta_e\frac{g_k}{5+\sqrt{\widehat v_k}},
\]

with `x₀=v₀=0` and `η_e=η₀/log log(e+exp(euler's number))`.

| Requirement or possible obstruction | Independent check |
|---|---|
| Allowed moment parameters | `β₁=0` is explicitly allowed by the target theorem; `β₂=q∈(0,1)` and `β₁<√β₂`. No extension to positive `β₁` is proved. |
| Actual initialized bias correction | The first correction is trivial; the second correction is retained throughout the finite-run proof. |
| Smooth finite sum | The four losses are `C∞`, individually bounded below, and have globally 1-Lipschitz gradients. The mean is strongly convex. |
| Genuine fresh reshuffling | Each epoch uses each component once; epochs are independent. No within-epoch martingale-difference assumption is used. |
| Positive vanishing steps | The denominator is greater than one, increases to infinity, and grows slower than any positive power of the epoch index. Thus `0<η_e<1`, `η_e→0`, and `Σ_eη_e=∞`. Repeating each step four times preserves these facts. |
| Compactness without projection | Set `a_k=η_e/(5+√v̂_k)`. Then `0<a_k≤1/5` and `x_k=(1−a_k)x_{k−1}+a_k(−C_k)`. Induction gives `x_k∈[−2,2]` for every sample path. |
| Moment and movement bounds | `|g_k|≤4`; `v̂_k` is a weighted average of the first `k` squared gradients, so `v̂_k≤16`; `|x_k−x_{k−1}|≤Uη_e`, `U=4/5`. |
| Nondegenerate frozen second moment | `B₂(x)=x²+5/2≥5/2` globally. |
| Epsilon condition | `ε=5>0`; no argument divides by a potentially zero RMS. |
| Objective/noise symmetry | Uniform offsets have mean zero and variance `5/2`. This symmetry is used for the stationary averaged drift, not as conditional slotwise independence. |
| Stationary frozen law | A two-sided sequence of independent permutation epochs with a uniform phase yields the phase-averaged stationary law; the exponentially weighted filter is a well-defined measurable function of this bounded past. |
| Time convention | A slot has duration `η_e`; an epoch has duration `4η_e`. The periodic vector field is the average of four phase directions, so its Euler increment is `−4η_e h_π`, not `−η_e h_π`. The attempt uses the correct factor. |

The quadratic gradients are not globally bounded, but global boundedness is not a hypothesis of target Theorem 2. The optional modification in §8 of the attempt supplies it without changing the trajectory; see §8 below.

## 3. Averaged drift and periodic roots

For every allowed frozen past define

\[
R(x)=\Big((1-q)\sum_{j\ge0}q^j(x+C_{-j})^2\Big)^{1/2},
\qquad u(x)=\frac{x+C_0}{5+R(x)}.
\]

The weighted norm is 1-Lipschitz in `x`. It is strictly positive because some complete epoch of distinct offsets occurs in the past with positive weights. On the invariant interval, `R≤4` and Cauchy–Schwarz gives `|R'|≤1`. Therefore

\[
u'(x)=\frac{5+R(x)-(x+C_0)R'(x)}{(5+R(x))^2}
\ge\frac1{81}=:\kappa,
\quad
|u(x)-u(y)|\le\frac9{25}|x-y|=:L|x-y|.
\]

The lower bound is conservative but valid: the numerator is at least `5−4=1`, while the squared denominator is at most `81`. These pathwise bounds pass to phase averages and expectations, either by integrating the derivative inequality or directly by differences; no unjustified interchange of a singular derivative and expectation is required.

Negating every offset is a probability-preserving bijection of the permutation stream and gives `h(−x)=−h(x)`. Thus `h(0)=0`, `(h(x)−h(y))(x−y)≥κ(x−y)²` on the interval, and

\[
|\Phi_t(x)|\le e^{-\kappa t}|x|.
\]

No zero occurs outside the interval either: all phase numerators are positive for `x>2` and negative for `x<−2`. The use of “unique zero” is consequently valid globally, although only the invariant-interval contraction is needed.

For repeated order `π₋=(-2,-1,1,2)`, summing the infinite geometric past yields exactly

\[
v_i(x)=\frac{\sum_{j=0}^3q^j(x+c_{i-j})^2}{1+q+q^2+q^3},
\qquad h_-(x)=\frac14\sum_i\frac{x+c_i}{5+\sqrt{v_i(x)}}.
\]

The four numerators at zero in the attempt are correct. In particular

\[
v_1-v_4=v_2-v_3=
\frac{3q(1-q^2)}{1+q+q^2+q^3}
=\frac{3q(1-q)}{1+q^2}=:\Delta_q>0.
\]

Pairing offsets `−2,+2` and `−1,+1` then gives

\[
4h_-(0)=2\left(\frac1{5+\sqrt{v_4}}-\frac1{5+\sqrt{v_1}}\right)
+\left(\frac1{5+\sqrt{v_3}}-\frac1{5+\sqrt{v_2}}\right)>0.
\]

This sign is not a floating-point observation and persists for every fixed `q∈(0,1)`. Since `h_-(-2)<0` and `h_-'≥κ`, there is exactly one root `x_-=-a_q∈(-2,0)`. Reflection gives `h_+(x)=−h_-(-x)` and root `x_+=a_q` for `π₊=(2,1,−1,−2)`. Both flows remain in the invariant interval and satisfy

\[
|z_\pm(t)-x_\pm|\le e^{-\kappa t}|z_\pm(0)-x_\pm|
\le4e^{-\kappa t}.
\]

At zero, `1≤v_i≤4`. For `b>a` in that range,

\[
\frac1{5+\sqrt a}-\frac1{5+\sqrt b}
=\frac{b-a}{(\sqrt a+\sqrt b)(5+\sqrt a)(5+\sqrt b)}
\ge\frac{b-a}{196}.
\]

It follows that `h_-(0)≥3Δ_q/784` and, by `L=9/25`,

\[
a_q\ge\frac{h_-(0)}L\ge
\frac{25q(1-q)}{784(1+q^2)}>0.
\]

All signs, factors of four, the cancellation in `Δ_q`, and the stated lower bound check out.

## 4. Finite-run tracking with memory and bias correction

This is a deterministic lemma conditional on a repeated-order block, uniform over every earlier history. It does not reuse the disputed random-averaging assertion.

Let `a=η_N≤1`, the largest step in a block starting at epoch `N`. At its slot age `j≥0`, use a weighted Hilbert norm with weights `(1−q)q^s`. Extend actual gradients by zero before initialization. For `s≤j`, actual and frozen periodic offsets agree, so the gradient difference is at most `Uas`. For older lags both gradients are bounded by four in magnitude, giving difference at most eight. Consequently

\[
\begin{aligned}
|\sqrt{v_k}-\sqrt{v_i(x_{k-1})}|
&\le Ua\Big((1-q)\sum_{s\ge0}q^ss^2\Big)^{1/2}
+8\Big((1-q)\sum_{s>j}q^s\Big)^{1/2}\\
&=UaM_q+8q^{(j+1)/2},\qquad
M_q=\frac{\sqrt{q(1+q)}}{1-q}.
\end{aligned}
\]

The correction from `v_k` to `v̂_k` is bounded without differentiating a square root near zero:

\[
0\le\sqrt{\widehat v_k}-\sqrt{v_k}
=\sqrt{\widehat v_k}\,(1-\sqrt{1-q^k})\le4q^k.
\]

Denominators at least five and numerator magnitude at most four now give the attempt's normalized-direction error `(4/25)(UaM_q+8q^{(j+1)/2}+4q^k)`.

Writing `z_p` for the state at epoch `N+p` and `η_p^*=η_{N+p}`, the four equal steps in that epoch give

\[
z_{p+1}=z_p-4\eta_p^*h_-(z_p)+r_p,
\]

\[
|r_p|\le C_q\eta_p^*a+
\frac{128}{25}\eta_p^*q^{2p}+
\frac{64}{25}\eta_p^*q^{4p},
\qquad
C_q=\frac{16U}{25}M_q+12LU
\]

as one explicit valid choice. The first constant includes the movement of the phase arguments back to the epoch start. Since `j≥4p` and the global slot `k≥4p+1`, both displayed geometric bounds are conservative in the correct direction.

For epoch times through a fixed horizon `H`, including at most one covering epoch, `4Ση_p^*≤H+4a`. Thus

\[
\sum_p|r_p|\le a\left[
\frac{C_q(H+4a)}4+
\frac{128}{25(1-q^2)}+
\frac{64}{25(1-q^4)}\right].
\]

The Euler time steps are `b_p=4η_p^*≤4a`. Since `|h_-|≤U` and `h_-` is `L`-Lipschitz, the sum of ODE local errors is at most

\[
\frac{LU}{2}\sum_pb_p^2\le2LUa(H+4a).
\]

Discrete Gronwall gives an epochwise error bounded by the sum of these two quantities times `exp(L(H+4a))`. Between neighboring epoch times, the actual interpolation and the ODE each have speed at most `U`; allowing `8Ua` covers the remaining interpolation error. In particular a possible constant in (10) is

\[
C_{q,H}=e^{L(H+4)}\left[
\frac{C_q(H+4)}4+
\frac{128}{25(1-q^2)}+
\frac{64}{25(1-q^4)}+2LU(H+4)
\right]+8U.
\]

This verifies the asserted `O_{q,H}(η_N)` bound for the initialized, bias-corrected recursion. Uniformity over the earlier random history is genuine. The constant can grow when `q→1`; the proof fixes `q` before taking `N→∞` and makes no uniform claim in that limit. No stochastic concentration theorem is hidden in this step.

## 5. Independent long-run events and the corrected accumulation step

For fixed `H>0`, set `N_j=j²` and `m_j=ceil(H/η_{N_j})`. These lengths are deterministic and `O_H(log log j)`, whereas consecutive starts differ by `2j+1`. Therefore the blocks are eventually disjoint. Moreover

\[
\frac{\eta_{N_j+m_j}}{\eta_{N_j}}\longrightarrow1.
\]

If `D_j=4Σ_{e=N_j}^{N_j+m_j-1}η_e` is the block duration, monotonicity gives

\[
4m_j\eta_{N_j+m_j}\le D_j\le4m_j\eta_{N_j},
\qquad D_j\longrightarrow4H.
\]

Thus `D_j≥H` eventually and `D_j≤4H+4`, exactly as needed for fixed-time evaluation. The factor four makes the lower bound especially safe.

The probability that all `m_j` permutations are a specified order is exactly `24^{-m_j}`. The ceiling inequality yields

\[
\Pr(E_j^-)\ge\frac1{24}
[\log(N_j+\exp(\mathrm e))]^{-H\log(24)/\eta_0}.
\]

This has divergent sum. For example, for any fixed exponent `p>0`, `j/(log j)^p→∞`, so eventually an inverse power of `log j` dominates a positive multiple of `1/j`. The events for disjoint epoch blocks are independent. Their states at block starts need not be independent; the deterministic tracking lemma is uniform over those states and memories, so that dependence causes no gap. Second Borel–Cantelli gives infinitely many successful blocks for each specified sign. Taking the intersection of the two probability-one events is valid; the plus and minus events inside the same block need not be independent.

**Original gap and repair.** The original proof's invocation of horizon `4H+4` did not follow from `D_j≥H`. The revised proof instead chooses `H` with `4e^{-κH}<δ/3`, uses the lemma on `[0,H]`, and obtains

\[
|X_{N_j}(H)-x_-|<\delta/3+C_{q,H}\eta_{N_j}.
\]

Take the last actual slot time `τ≤H` in the block. Its distance in time from `H` is at most `η_{N_j}`, and the interpolation has speed at most `U`. Hence

\[
|x_{\mathrm{slot}}-x_-|
<\delta/3+(C_{q,H}+U)\eta_{N_j}<\delta
\]

for all sufficiently late successes. If `H` happens to equal a slot time, the additional error is zero. For large starts the chosen time is genuinely within the block. The reflected proof gives the same assertion for `x_+`.

For each `δ=1/n`, the horizon is fixed and the event has probability one. Their countable intersection still has probability one; recursively choose a successful slot later than the previously chosen one to get the two convergent subsequences. No uncountable intersection or limit of probabilities is invoked. This establishes the claimed two accumulation points.

## 6. Non-APT conclusion and limits of what is contradicted

If the interpolation were an APT of `x'=−h(x)`, then for every fixed `T>0`,

\[
|X(t+T)|\le e^{-\kappa T}|X(t)|+o(1).
\]

Its bounded continuous-time limsup `L_*` is unchanged by shifting time by `T`, so `L_*≤e^{-κT}L_*` forces `L_*=0`. But the actual slot subsequences give `L_*≥a_q>0`. This contradiction is rigorous. The construction proves bounded nonconvergence, not escape to infinity.

Conversely, the two opposite-sign accumulation points and vanishing increments force infinitely many arbitrarily small crossings of zero. For any sufficiently late transition from one sign neighborhood to the other, a crossing step has size at most `Uη_e→0`. Therefore

\[
\liminf_k|f'(x_k)|=0,\qquad
\limsup_k|f'(x_k)|\ge a_q>0
\quad\text{almost surely}.
\]

| Possible claim | What this audit establishes |
|---|---|
| Theorem 2's stated assumptions imply almost-sure APT tracking | False; the corrected example satisfies them and violates tracking. |
| Theorem 2's residual-liminf inequality | Not refuted. This example has an even smaller liminf, namely zero. Its former proof route is unavailable under the stated schedule generality. |
| Local Theorem 3's expected-rate bound for `η/√k` | Unaffected. It fixes a different schedule and has a separate coupling proof, which this audit does not re-audit. |
| Convergence for every arbitrary positive vanishing step schedule | False for this recursion and parameter class. |
| Convergence for some appropriate decaying schedule, or for practical positive `β₁` | Not decided by the present example. |
| Fixed small constant steps, exact criticality under interpolation, or transformer advantage | Not settled. The proof uses vanishing steps and nonzero component gradients at the minimizer. |
| Registry T357 calibration question | No result supplied. |

## 7. Primary-source checks

The following were opened independently on 23 October 2026. Relevant mathematical PDF pages were visually inspected, not inferred only from search snippets. These references contextualize the result; the counterexample proof above is self-contained.

Downloaded primary-source byte hashes (the arXiv downloads used the explicit `v1` URLs) are:

| Primary PDF | SHA256 |
|---|---|
| Benaïm 1999 | `8cac79a286f670b26626a4373dfec0a89633323ace40e5ed72edf74da50ff45a` |
| Zhang et al. `2603.02092v1` | `b2510f48b9ecb9b93462d06097bf76f40e4b939e31af10d7575a35fab5f825d7` |
| Heilman–Mohanty `2607.03519v1` | `05b827ddccba2ae01fea6b660d4eaf5bd855a5997240c3390e03ce94891c4d43` |

1. **Michel Benaïm, *Dynamics of stochastic approximation algorithms*, Séminaire de Probabilités XXXIII (1999), pp. 1–68.** [Numdam primary PDF](https://www.numdam.org/item/SPS_1999__33__1_0.pdf). Proposition 4.4, printed p. 16, assumes summability of `Σ_n exp(−c/γ_n)` for every `c>0` in its subgaussian Robbins–Monro APT result. Section 10, printed p. 60 and its footnote, distinguishes slower-step nonconvergence from the previous fast-decay APT setting. Proposition 10.3, p. 64, supplies a weak-APT statement under its own Robbins–Monro conditions. Our schedule fails the displayed exponential summability. These statements do not by themselves prove anything about the reshuffling filter; they confirm why geometric forgetting plus a frozen ergodic average is insufficient to cite as a sample-path averaging proof. PDF indices 16, 60, 64 correspond to these printed pages because of the front cover.

2. **Yushun Zhang et al., *Adam Converges Without Any Modification On Update Rules*, arXiv:2603.02092v1, 2 March 2026.** [Primary PDF](https://arxiv.org/pdf/2603.02092). The retrieved PDF's title page identifies v1 and states that it extends the NeurIPS 2022 paper. Theorem 3.3, printed p. 11 (PDF index 10), fixes `η_k=η₀/√k`, random shuffling, and a problem-dependent large-`β₂` threshold; its conclusion is an expectation bound on a minimum of gradient residual measures. It is not a theorem for all vanishing schedules or almost-sure pointwise convergence. The versioned `/pdf/2603.02092v1` endpoint was unavailable to this browser retrieval, so the unversioned PDF was used only after verifying its printed version label. [Original arXiv:2208.09632v5](https://arxiv.org/html/2208.09632v5), 13 January 2023, likewise distinguishes a neighborhood guarantee from the extra strong-growth setting.

3. **Steven Heilman and Sampad Mohanty, *On the Convergence of Adam, Revisited*, arXiv:2607.03519v1, submitted 3 July 2026; displayed manuscript date 7 July 2026.** [Versioned primary PDF](https://arxiv.org/pdf/2607.03519v1). Definition 1.1, pp. 1–2, uses projection onto `[−1,1]`; Theorem 1.5, p. 3, concerns online periodic linear losses; Theorem 1.7, p. 4, states an iid extension for `α_t=α/√t`. That is a different model and convergence quantity from the bounded, unprojected, fixed finite-sum reshuffling construction here. These distinctions support the narrow comparison, not a priority claim or a finding that the construction is new.

## 8. Optional modifications and arithmetic checks

The epsilon scaling is exact. With `a=ε₀/5>0`, replacing every loss by `a f_i` multiplies `g`, `m̂`, and `√v̂` by `a`; using epsilon `ε₀=5a` leaves the normalized update unchanged. This handles any prescribed positive epsilon, but makes no assertion at epsilon zero.

The proposed smooth cutoff also works. For even `χ` equal to one on `[−2,2]`, positive on `(2,3)`, zero outside `[−3,3]`, and at most one, `b(x)=∫₀ˣχ(s)ds` is odd, bounded, and Lipschitz, with limits `±B` where `B>2`. The new gradients `b(x)+c_i` equal the original ones on the invariant interval. Their losses tend to positive infinity at both ends because their limiting slopes are strictly positive at `+∞` and strictly negative at `−∞`. Adding a common smooth compactly supported loss perturbation outside the invariant interval can make the mean nonconvex while preserving all actual iterates, global boundedness of gradients, and the lower bound `B₂=(b+perturbation derivative)²+5/2`.

Independent `fractions.Fraction` checks verified the two exact variance differences at `q=1/1000,1/4,9/10,99/100,999/1000`; at `q=1/4` they return `(65,29,20,56)/17` and difference `9/17`. Separate floating-point bisection reproduced the four illustrative roots in the attempt to the shown precision. These finite checks are only arithmetic sanity checks. The exact inequalities in §§3–5, not numerical simulation, prove the sign for every fixed `q` and the almost-sure rare-run assertion.

**Final disposition:** the original horizon misuse is resolved in the pinned corrected version. No remaining gap was found in the claimed counterexample, its initialized-filter treatment, its use of Borel–Cantelli, or its explicitly limited conclusion.
