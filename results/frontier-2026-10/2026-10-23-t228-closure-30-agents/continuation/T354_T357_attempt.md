# T354/T357 follow-up: a counterexample to unrestricted almost-sure tracking

23 October 2026. A29. No new agents. The frozen `campaign/` was not modified. A26 was told the selected target before the derivation was completed.

**Result:** an explicit, bounded, unprojected, bias-corrected Adam/RMSProp example disproves the almost-sure asymptotic-pseudotrajectory claim in the still-sketched tracking step of `a03/T354_theorem.md`, Theorem 2, under its stated unrestricted vanishing-step assumptions. The example has a smooth strongly convex four-term objective, fresh uniform random reshuffling, symmetric gradient offsets, and any fixed `β₂∈(0,1)`, including values arbitrarily close to one. Its iterates have two distinct nonzero accumulation points almost surely.

**Honest status:** the mathematical counterexample is proved below, but has not received an independent audit. This refutes that tracking step and a stronger assertion of almost-sure convergence under arbitrary vanishing steps. It does **not** refute Theorem 2's weaker residual-liminf conclusion, the audited `η/√k` expected-rate theorem, or every possible decaying-step convergence theorem. No first-in-literature priority or closure of T354/T357 is claimed.

## 1. Target selection and source versions

| Local item inspected | SHA256 |
|---|---|
| `a03/T354_independent_prior_audit.md` | `f5ccf97da806793c0937d77100d2f92d86ca1aa992749c8a27b86a5105034559` |
| `a03/T354_next.md` | `e92496a9053aeb0e195ab32ecee5b67a2cb0b1faf1a481850b95ee0944213f5a` |
| `a03/T354_theorem.md` | `fbf6011a14d439eff8208fa14c6a0625cc66aca91eebe09b19fb0b4c4bd59f28` |
| `a03/rows_T357_DOSSIER.md` | `4f150d1a55209ed37d8b1c6bca8e6ed85b9b4b50dbac24e616b5126791fb5ff9` |
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |

The exact registry rows are JSONL line 354, problem `T354`, rank 332, “Convergence of Adam with the hyperparameters used in practice”; and line 357, problem `T357`, rank 335, “Overconfidence of overparameterized classifiers.” T354 asks about convergence with problem-independent fixed betas and decaying or small constant steps, plus a separate transformer-advantage model. T357 asks for calibration along training of a two-layer model, including sample ratio, width, and time dependence.

The local T354 scalar residual law and corrected Theorem 3 are already established partial results. The independent prior audit explicitly excludes Theorem 2's tracking sketch from its acceptance. That sketch claims that compactness, `η_k→0`, and `Ση_k=∞` suffice to make the interpolation an almost-sure asymptotic pseudotrajectory of the averaged frozen drift. This is the selected unresolved gap.

I also read the T357 dossier and continuation notes. Their late entries already resolve several earlier ridge fixed-point and spectral-moment items, so those are unsuitable targets for a fresh claim. The actual gradient-flow/GD transfer and proportional finite-time calibration remain outside this attempt; I do not infer present literature-wide openness from the dossier's stale status lines.

## 2. Primary-source check and current-status limits

Primary sources were opened directly on 23 October 2026:

1. Benaïm, [*Dynamics of stochastic approximation algorithms* (1999)](https://www.numdam.org/item/SPS_1999__33__1_0.pdf), Proposition 4.4, printed p. 16; Section 10 opening, p. 60; Proposition 10.3, p. 64. The paper distinguishes almost-sure APT results with sufficiently fast decay from weak APT results for slow decay. Section 10 explicitly discusses nonconvergence for slow steps. Thus geometric forgetting of a frozen filter alone does not supply the missing sample-path averaging hypothesis. The phenomenon is known in general stochastic approximation; the derivation below specializes it to the actual Adam recursion in the local claim.
2. Zhang et al., [arXiv:2603.02092v1](https://arxiv.org/pdf/2603.02092v1), the March 2026 extended version of the registry's 2022 paper. Theorem 3.3, printed p. 11, states the random-shuffling expected residual bound with `η_k=η₀/√k` and a problem-dependent large-`β₂` threshold. This is not a theorem for all vanishing steps. The original record [2208.09632v5](https://arxiv.org/abs/2208.09632v5) also distinguishes a neighborhood result from exact criticality under an extra growth assumption.
3. Heilman–Mohanty, [arXiv:2607.03519v1](https://arxiv.org/pdf/2607.03519v1), Theorems 1.5 and 1.7, printed pp. 3–4; Appendix A, pp. 18–20. Their projected online periodic/iid linear-loss counterexamples and stationary-drift transfer are relevant prior work. The iid theorem uses `α/√t`. The present construction concerns fresh reshuffling of a fixed smooth finite sum, no projection, symmetric offsets, and much slower steps. These differences explain the local target; they do not establish novelty.

## 3. Model and statement

Fix any `q∈(0,1)` and any step amplitude `η₀∈(0,1]`. Set

\[
c=(-2,-1,1,2),\quad f_i(x)=\tfrac12(x+c_i)^2,
\quad f(x)=\tfrac14\sum_{i=1}^4 f_i(x)=\tfrac12x^2+\tfrac54.
\]

At each epoch independently draw a uniform permutation of the four components and process all four once. Put `β₁=0`, `β₂=q`, `ε=5`, `m₀=v₀=0`, and `x₀=0`. At slot `k` of epoch `e=ceil(k/4)`, run the standard bias-corrected update

\[
g_k=x_{k-1}+C_k,\qquad
v_k=qv_{k-1}+(1-q)g_k^2,\qquad
\widehat v_k=\frac{v_k}{1-q^k},\qquad
x_k=x_{k-1}-\eta_e\frac{g_k}{5+\sqrt{\widehat v_k}},
\tag{1}
\]

where

\[
\eta_e=\frac{\eta_0}{\log\log(e+\exp(\mathrm e))}.
\tag{2}
\]

Here `e` in the argument is the integer epoch; `\mathrm e` is Euler's number. The step is constant within each epoch, is positive and less than one, tends to zero, and has divergent sum. Its initial amplitude can be arbitrarily small. The first-moment bias correction is trivial because `β₁=0`. In particular `β₁<√β₂` holds.

Let `h(x)` be the phase-averaged stationary frozen drift under iid uniform reshuffling, exactly as in the local theorem. Then there is a number `a_q>0` such that, almost surely,

\[
-a_q\text{ and }a_q\text{ are accumulation points of }(x_k),
\qquad
\limsup_{k\to\infty}|x_k|\ge a_q>0.
\tag{3}
\]

Nevertheless `h` has the unique zero `0`, and its ODE `\dot x=-h(x)` attracts the entire interval `[-2,2]` to zero exponentially. Consequently the ordinary continuous-time interpolation of (1), at times `t_k=Σ_{s≤k}η_{ceil(s/4)}`, is almost surely **not** an APT of this ODE.

## 4. Compactness, noise, and regularity hold

If `x_{k−1}∈[-2,2]`, write

\[
a_k=\frac{\eta_e}{5+\sqrt{\widehat v_k}}\in[0,1/5],
\qquad x_k=(1-a_k)x_{k-1}+a_k(-C_k).
\]

Both endpoints of this convex combination lie in `[-2,2]`. Thus the interval is invariant for every permutation realization; no projection has been added. In it,

\[
|g_k|\le4,\quad 0\le\widehat v_k\le16,
\quad |x_k-x_{k-1}|\le U\eta_e,\quad U=4/5.
\tag{4}
\]

The objective is bounded below, the components are globally smooth with Lipschitz gradients, and

\[
B_2(x)=\tfrac14\sum_i(x+c_i)^2=x^2+5/2\ge5/2.
\]

The uniformly sampled gradient oracle has mean `x` and variance `5/2`; its offsets are symmetric. The actual sampling is fresh reshuffling, with its usual conditional dependence within an epoch. No martingale-difference property is falsely asserted for an individual reshuffled slot.

For any allowed infinite frozen history, set

\[
R(x)=\left((1-q)\sum_{j\ge0}q^j(x+C_{-j})^2\right)^{1/2}.
\]

On `[-2,2]`, `R≤4` and `|R'|≤1`, by Cauchy–Schwarz. Also `R>0`: a full epoch of distinct offsets occurs in the frozen past and its weights are positive. For the current offset `C_0`, define `u(x)=(x+C_0)/(5+R(x))`. Then

\[
u'(x)=\frac{5+R(x)-(x+C_0)R'(x)}{(5+R(x))^2}
\ge\frac1{81}=:\kappa.
\tag{5}
\]

Furthermore `u` is `L=9/25` Lipschitz: its numerator is 1-Lipschitz, its denominator is at least five, `|x+C_0|≤4`, and `R` is 1-Lipschitz. These bounds hold for every history, so they pass to expectations and phase averages.

Negating every offset preserves the law of the random permutation stream and sends `u(x)` to `−u(−x)`. Hence `h` is odd, `h(0)=0`, and (5) makes it strictly increasing, with unique zero zero. Its flow satisfies

\[
|\Phi_t(x)|\le e^{-\kappa t}|x|,\qquad x\in[-2,2].
\tag{6}
\]

This is not a nonzero frozen-bias example: the random-reshuffling averaged drift is exactly zero at the population minimizer.

## 5. A repeated permutation has a different exact drift

Consider the deterministic permutation `π₋=(-2,-1,1,2)` repeated forever. Its frozen second moments at phase `i` are

\[
v_i(x)=\frac{\sum_{j=0}^3q^j(x+c_{i-j})^2}{D},
\qquad D=1+q+q^2+q^3,
\]

with cyclic indexing. Define

\[
h_-(x)=\frac14\sum_{i=1}^4\frac{x+c_i}{5+\sqrt{v_i(x)}}.
\]

The same bounds (5) and `L=9/25` apply to `h_-`. At zero its second moments are exactly

\[
\begin{aligned}
Dv_1&=4+4q+q^2+q^3,& Dv_2&=1+4q+4q^2+q^3,\\
Dv_3&=1+q+4q^2+4q^3,& Dv_4&=4+q+q^2+4q^3.
\end{aligned}
\]

In particular,

\[
v_1-v_4=v_2-v_3=\Delta_q
=\frac{3q(1-q)}{1+q^2}>0.
\tag{7}
\]

Pairing the equal-magnitude gradients gives

\[
4h_-(0)=
2\left(\frac1{5+\sqrt{v_4}}-\frac1{5+\sqrt{v_1}}\right)
+\left(\frac1{5+\sqrt{v_3}}-\frac1{5+\sqrt{v_2}}\right)>0.
\tag{8}
\]

At `x=−2`, all four numerators are nonpositive and three are negative, so `h_-(−2)<0`. Strict monotonicity proves a unique root `x_-=−a_q∈(−2,0)`. The reflected repeated order `π₊=(2,1,−1,−2)` has drift `h_+(x)=−h_-(−x)` and root `x_+=a_q>0`.

An explicit positive separation is available. At zero, each `v_i∈[1,4]`. Rationalizing each difference in (8) bounds its denominator by `4·7²=196`, giving

\[
h_-(0)\ge\frac{3\Delta_q}{784},\qquad
a_q\ge\frac{h_-(0)}L
\ge\frac{25q(1-q)}{784(1+q^2)}>0.
\tag{9}
\]

Thus the construction works for every fixed `q<1`, with no numerical sign test and no exclusion of `q` close to one.

## 6. Finite-run tracking lemma, proved for the actual initialized recursion

**Lemma.** Suppose epochs starting at `N` repeat `π₋` for a block whose algorithmic duration is at least a fixed `H`. Let `X_N(t)` be the actual slot interpolation starting at the block's initial state, and let `z` solve `\dot z=-h_-(z)` from that same state. Uniformly over the entire preceding history,

\[
\sup_{0\le t\le H}|X_N(t)-z(t)|
\le C_{q,H}\eta_N\longrightarrow0.
\tag{10}
\]

The same holds for `π₊`. Constants may depend on the fixed `q,H`; uniformity as `q→1` is not claimed.

**Proof.** Put `a=η_N`, the largest step in the block. At a slot `k` with block age `j≥0`, compare `√v_k` with the periodic frozen RMS `√v_i(x_{k−1})`. Regard both as weighted Hilbert-space norms with weights `(1−q)q^s`; extend the actual gradient history by zero before initialization. Within the block the gradient difference at lag `s≤j` is just an iterate difference, at most `Uas`. At older lags the difference is at most eight. The reverse triangle inequality therefore gives

\[
\left|\sqrt{v_k}-\sqrt{v_i(x_{k-1})}\right|
\le UaM_q+8q^{(j+1)/2},\qquad
M_q=\frac{\sqrt{q(1+q)}}{1-q}.
\tag{11}
\]

The bias correction is controlled exactly, using `√v̂_k≤4`:

\[
0\le\sqrt{\widehat v_k}-\sqrt{v_k}
=\sqrt{\widehat v_k}(1-\sqrt{1-q^k})\le4q^k.
\tag{12}
\]

The two denominators are at least five. Hence the difference between the actual normalized direction and the periodic frozen direction at the current iterate is at most

\[
\frac4{25}\left(UaM_q+8q^{(j+1)/2}+4q^k\right).
\tag{13}
\]

Let `z_p` be the actual state at the start of the block's `p`th epoch. Moving a phase's argument back to `z_p` costs at most `3LUa`, by (4) and the Lipschitz bound. Summing the four slot updates gives

\[
z_{p+1}=z_p-4\eta_{N+p}h_-(z_p)+r_p,
\]

where, for constants depending only on `q`,

\[
|r_p|\le C_q\eta_{N+p}a
 +\frac{128}{25}\eta_{N+p}q^{2p}
 +\frac{64}{25}\eta_{N+p}q^{4p}.
\tag{14}
\]

The last bound conservatively drops the extra decay from the global starting time in the bias-correction term. On any fixed algorithmic horizon, summing (14) gives `O_{q,H}(a)`: the first term uses `4Ση≤H+4a`, and the other two are geometric series multiplied by at most `a`. Euler truncation for the Lipschitz bounded vector field also sums to `O_H(a)`, since `Ση²≤aΣη`. Discrete Gronwall yields (10) at epoch times. Within an epoch, both trajectories move by `O(a)`, proving the interpolation bound. This proves the lemma without invoking the disputed stochastic averaging step. □

## 7. Long exceptional runs occur infinitely often

Fix a finite `H>0`. Let `N_j=j²` and

\[
m_j=\left\lceil\frac H{\eta_{N_j}}\right\rceil.
\]

These are deterministic block lengths. They are `O_H(log log j)`, so the epoch blocks `[N_j,N_j+m_j−1]` are disjoint for all sufficiently large `j`. Slow variation gives `η_(N_j+m_j)/η_(N_j)→1`; therefore their algorithmic durations are at least `H` for large `j` and at most `4H+4`.

Let `E_j^-` be the event that every permutation in this block equals `π₋`. Its exact probability and a useful lower bound are

\[
P(E_j^-)=24^{-m_j}
\ge\frac1{24}\,[\log(N_j+\exp(\mathrm e))]^{-H\log24/\eta_0}.
\tag{15}
\]

The series of these probabilities diverges; every fixed negative power of `log j` has divergent sum over integers. The block events are independent. The second Borel–Cantelli lemma proves that `E_j^-` occurs infinitely often almost surely. The same argument separately proves infinitely many all-`π₊` blocks, on the same probability-one event.

For a fixed accuracy `δ>0`, choose a finite `H` such that `4exp(−κH)<δ/3`, using the contraction rate `κ=1/81`. The `h_-` flow starting anywhere in `[-2,2]` is then within `δ/3` of `x_-` at time `H`. Every sufficiently late successful block has algorithmic duration at least `H`, so (10) applies on `[0,H]` and gives `|X_N(H)−x_-|<δ/3+C_{q,H}η_N`. Take the last actual slot time `τ≤H` inside that block. Since each slot has duration at most `η_N` and the interpolation has speed at most `U`, its iterate satisfies `|x_slot−X_N(H)|≤Uη_N`. For sufficiently late successes, `(C_{q,H}+U)η_N<2δ/3`, so this actual interior slot is within `δ` of `x_-`. The reflected statement holds for `x_+`. Intersect these probability-one assertions over `δ=1,1/2,1/3,...`, and extract increasing interior-slot subsequences. Both `x_-` and `x_+` are accumulation points, proving (3). No approximation beyond the successful block or claim about its endpoint is needed.

If the interpolation were an APT of `\dot x=-h(x)`, then for every fixed `T>0`, (6) and the APT property would imply

\[
|X(t+T)|\le e^{-\kappa T}|X(t)|+o(1).
\]

Writing `L_*=limsup_(t→∞)|X(t)|≤2` gives `L_*≤e^{-κT}L_*`, hence `L_*=0`. This contradicts (3). The claimed almost-sure tracking is false.

There is also an informative limit to the counterexample. Since the sequence has accumulation points on both sides of zero and its increments tend to zero, it crosses arbitrarily close to zero infinitely often. Thus

\[
\liminf_k|f'(x_k)|=0,
\qquad \limsup_k|f'(x_k)|\ge a_q>0
\quad\text{almost surely}.
\tag{16}
\]

Equation (16) is why this is not a refutation of the residual-liminf conclusion.

## 8. Robustness and numerical checks

The large displayed epsilon is removable by exact scaling. For any prescribed `ε₀>0`, replace each loss by `(ε₀/5)f_i` and use epsilon `ε₀`. Both first and RMS second moments scale by `ε₀/5`, so the normalized update is exactly (1). The iterates and counterexample are unchanged.

If globally bounded gradients are desired, choose an even smooth cutoff `χ`, equal to one on `[-2,2]`, positive on `(2,3)`, zero outside `[-3,3]`, and bounded by one. Put `b(x)=∫₀ˣχ(s)ds` and replace the gradients by `b(x)+c_i`. These are globally bounded and Lipschitz, agree with the construction throughout its invariant interval, and have `B₂=b(x)²+5/2`. Their component losses are bounded below because the limits of `b` have magnitude strictly greater than two. A common compactly supported perturbation outside `[-2,2]` can make the objective genuinely nonconvex without changing any iterate. Convexity was therefore not the source of the obstruction.

Independent arithmetic sanity checks used `fractions.Fraction`. At `q=1/4`,

\[
(v_1,v_2,v_3,v_4)=(65/17,29/17,20/17,56/17),
\]

and both differences in (7) equal `9/17`. Floating-point bisection, used only as an illustration, gave:

| `q` | `h_-(0)` | Negative root `x_-` |
|---|---:|---:|
| 0.25 | 0.002923932625 | −0.022501824462 |
| 0.9 | 0.000810846557 | −0.005406622994 |
| 0.99 | 0.000082074228 | −0.000540796811 |
| 0.999 | 0.000008213307 | −0.000054059412 |

Direct deterministic-order, bias-corrected runs at `q=.999`, algorithmic time 180, and steps `10⁻³`, `2·10⁻⁴`, `4·10⁻⁵` ended at `−0.000319999`, `−0.000107245`, `−0.0000646964`, respectively, approaching the frozen periodic root as the step decreases. These checks do not demonstrate the rare-event statement numerically; (15) and Borel–Cantelli prove it.

## 9. What has advanced and what remains

The previously missing tracking argument cannot be supplied under the exact general step assumptions currently written. A repair must either restrict the schedule and prove a sample-path noise estimate, or use an appropriate weak-tracking/occupation argument for the weaker liminf claim. Simply citing geometric forgetting and frozen ergodicity is insufficient: rare long runs are the obstruction.

The audited `η/√k` Theorem 3 remains separate. This attempt supplies neither a new proof nor a counterexample for that schedule, and proves nothing about practical nonzero momentum such as `β₁=.9`. The original T354 transformer-advantage clause and T357's proportional neural-feature calibration dynamics remain unaddressed.

**Disposition:** proved explicit counterexample to the local unrestricted almost-sure APT step; no blanket T354/T357 closure; independent audit still needed for this new derivation.
