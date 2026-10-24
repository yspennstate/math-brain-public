Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model/reasoning telemetry, so GPT-6 maximum is not claimed. F0097 NO MOVEMENT on the frozen source metric: `Omega_3 <= 0.9698` remains the best fully source-backed bound; F0097 unchanged count `0 -> 1`. Methods: #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R03 run43 — F0097 random k-SAT: fractional cavity-energy budget and overlap-scale reformulation

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0097 OPEN / R03 PARTIAL.** F0001 / sharp iid Rademacher singularity remains handed off after run41's third stuck episode and is **not reopened**. The current canonical R03 claim is `operations/claims/F0097.md`; returning to F0001 without an explicit reassignment would violate the owner's stuck/rotation rule.

## 1. Continuity, source, and current literature

Before new mathematics I recovered/read the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the F0097 ownership claim, newest own report `runs/R03/20260917T2008Z_42_f0097_cavity_slice.md`, neighboring R02's current F0097 source screen, and the intake history including `F0097-A001`. The prior attempt's Ding--Sly--Sun sufficiently-large-`k` result is preserved; it is not reset or relabeled as new work.

The outside source remains Alan Frieze, *Random Structures and Algorithms*, ICM 2014, asking for a fixed-
`k` satisfiability threshold. The current source-matching target is existence of a uniform threshold for every fixed `k>=3`; a result for `k=3` alone is PARTIAL relative to the source.

Fresh primary/later-source check dated 2026-09-17:

1. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (2026), published online 27 March 2026, explicitly states that the threshold is known precisely for `k=2` and for all sufficiently large `k`, while for `3<=k<k_0` even existence of a uniform threshold remains open. It proves the replica-symmetric formula for the actual number of satisfying assignments only up to the Gibbs uniqueness threshold, far below the conjectural small-`k` satisfiability threshold.

2. Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, 12/16 August 2026, proves for every fixed `k>=3` a central clause window

   `W_{eta,k}(n) = O(n/log n)`.

   Its Section 10 records the decisive current barrier: Abbe--Montanari show that a bound `O(n/log^{1+delta} n)` for any fixed `delta>0` would imply the satisfiability conjecture. Carenini reaches exactly the boundary `n/log n`; the generic Bourgain/replacement mechanism has booster strength `exp(-O(K))`, replacement cost `exp(O(K))`, and a Boolean-layer `1/sqrt(V)` loss, forcing only `K=Omega(log V)`. The paper says an improvement needs a larger booster, subexponential simulation of clean boosters, or a model-specific replacement using more geometry than monotonicity.

A bounded fresh search found no later accepted theorem closing the small-fixed-`k` threshold-existence problem. This is dated negative search evidence, not a worldwide novelty certificate.

## 2. Frozen metric

Run42 fixed

\[
\theta_{k,n}=\frac1n\min\{m:\Pr(F_k(n,m)\text{ SAT})\le1/2\},
\qquad
\Omega_k=\limsup_n\theta_{k,n}-\liminf_n\theta_{k,n}.
\]

For the first unresolved case, R03 tracks

\[
\boxed{\Omega_3},\qquad \text{target }0.
\]

The fully source-backed lower/upper threshold bounds `3.52` and `4.4898` still give

\[
\boxed{0\le\Omega_3\le0.9698.}
\]

Carenini's `O(n/log n)` window is a major structural improvement but does **not** reduce this limsup-minus-liminf interval by itself; her paper explicitly explains why the extra positive power of `log n` is the threshold-convergence frontier. Therefore the frozen metric has **no movement** this run and the F0097 unchanged count becomes `1`.

## 3. Method #1 — CHANGE THE CATEGORY: from SAT probability to a partition-function martingale

Work in the standard proper-clause model. Fix `n,k`, let `F_t` contain `t` independent uniform proper `k`-clauses, and let

\[
Z_t=|\mathrm{SAT}(F_t)|,
\qquad
a_k=1-2^{-k},
\qquad
W_t=\frac{Z_t}{2^n a_k^t}.
\]

The key category change is to stop tracking the Boolean event `Z_t>0` directly and instead track the normalized partition function `W_t`, together with the local geometry of the uniform measure on its solutions.

If `Z_t>0`, let `\mu_t` be uniform on `SAT(F_t)`. For a `k`-set `S` and local pattern `tau in {+-1}^S`, write

\[
p_{S,t}(\tau)=\mu_t(\sigma_S=\tau).
\]

Define the average local `L^2` defect

\[
\boxed{
D_t:=\mathbb E_{S}\sum_{\tau\in\{\pm1\}^S}
\bigl(p_{S,t}(\tau)-2^{-k}\bigr)^2,
}
\tag{3.1}
\]

and set `D_t=0` when `Z_t=0`.

A new random proper clause is equivalently a random pair `(S,tau)` and forbids the local assignment `tau`. Conditional on `F_t`, put

\[
q=p_{S,t}(\tau).
\]

Then

\[
\frac{Z_{t+1}}{Z_t}=1-q,
\qquad
\mathbb E[q\mid F_t]=2^{-k}.
\tag{3.2}
\]

Hence

\[
\boxed{\mathbb E[W_{t+1}\mid F_t]=W_t.}
\tag{3.3}
\]

Thus `W_t` is a nonnegative martingale. This elementary conservation law is standard/folkloric in random-CSP and planted-model language; I make no novelty claim for the martingale itself.

There is also an exact planted interpretation. In the ordered-clause model let `P_0` be the null formula law, and let `P_pl` choose a uniform planted assignment first and then choose every clause uniformly among clauses satisfied by it. Direct counting gives

\[
\boxed{
\frac{dP_{pl}}{dP_0}(F_t)=W_t(F_t).
}
\tag{3.4}
\]

So fractional moments of `W_t` are Renyi/Hellinger affinities between planted and null ensembles. Quiet planting and the general planted/null connection are well established in the CSP literature; again, the category change is used here as a route, not claimed as new prior art.

## 4. Method #12 — FIND WHAT IS CONSERVED: an exact cavity-energy budget

The conservation (3.3) has a quantitative refinement. First compute the variance of the fraction `q` of current solutions killed by one random clause. Since `tau` is uniform on `2^k` patterns,

\[
\begin{aligned}
\operatorname{Var}(q\mid F_t)
&=2^{-k}\,\mathbb E_S\sum_{\tau}p_{S,t}(\tau)^2-2^{-2k}\\
&=2^{-k}D_t.
\end{aligned}
\tag{4.1}
\]

Therefore the one-step quadratic variation of the normalized solution-count martingale is exactly

\[
\boxed{
\mathbb E[(W_{t+1}-W_t)^2\mid F_t]
=\frac{2^{-k}}{a_k^2}\,W_t^2D_t.
}
\tag{C299a}
\]

This identifies `D_t` as the exact cavity energy seen by a fresh random clause.

The useful robust version uses a fractional moment. Fix `0<alpha<1` and set

\[
\gamma_{\alpha,k}
:=\frac{\alpha(1-\alpha)2^{-k-1}}{a_k^\alpha}.
\tag{4.2}
\]

Then

\[
\boxed{
\mathbb E[W_{t+1}^\alpha\mid F_t]
\le
W_t^\alpha\bigl(1-\gamma_{\alpha,k}D_t\bigr).
}
\tag{C299b}
\]

Consequently, for every `m`,

\[
\boxed{
\gamma_{\alpha,k}
\sum_{t=0}^{m-1}\mathbb E[W_t^\alpha D_t]
\le1-\mathbb E[W_m^\alpha]\le1.
}
\tag{C299c}
\]

### Proof of C299b--c

On `Z_t>0`, from (3.2),

\[
\frac{W_{t+1}}{W_t}=\frac{1-q}{a_k}.
\]

Let

\[
h(q)=\left(\frac{1-q}{a_k}\right)^\alpha.
\]

Since

\[
h''(q)=-\alpha(1-\alpha)a_k^{-\alpha}(1-q)^{\alpha-2}
\le-\alpha(1-\alpha)a_k^{-\alpha},
\]

`h` is uniformly strongly concave on `[0,1]`. With `p=E q=2^{-k}` and `h(p)=1`, Taylor's inequality for a strongly concave function gives

\[
\mathbb E h(q)
\le
1-\frac{\alpha(1-\alpha)}{2a_k^\alpha}\operatorname{Var}(q).
\]

Insert (4.1) to get C299b. When `W_t=0`, both sides vanish by convention. Taking expectation and telescoping over `t` gives C299c because `W_0=1`. QED.

For `k=3`, `alpha=1/2`,

\[
\gamma_{1/2,3}=\frac{\sqrt{8/7}}{64},
\qquad
\sum_t\mathbb E[\sqrt{W_t}\,D_t]
\le64\sqrt{7/8}.
\tag{4.3}
\]

Thus, in the Hellinger interpolation between null and planted formulas, the **total weighted local-correlation energy over all clause-exposure times has an absolute finite budget**. This is the concrete invariant/monovariant produced by method #12.

I did a bounded prior-art search for the exact `W^alpha D` form. The normalized-solution martingale, planted likelihood ratio, fractional moments, and Fourier/correlation techniques all have extensive antecedents; I did not locate this exact displayed identity as a named theorem. That is not a novelty certificate, and C299 is recorded only as a proved route lemma.

## 5. Method #30 — ONE SCALE AT A TIME: exact Fourier and overlap decompositions

The point of C299 is not another one-step coupling lemma. Its energy has an exact multiscale interpretation.

### 5.1 One-clause scale = low-degree Fourier energy

Let

\[
f_t(\sigma)=2^n\mu_t(\sigma)
\]

be the solution-measure density relative to the uniform cube measure, and let

\[
\widehat f_t(A)=\mathbb E_{\mu_t}\chi_A
\]

be its Walsh coefficients. Parseval on a random `k`-coordinate marginal gives

\[
\boxed{
D_t
=2^{-k}\sum_{j=1}^{k}
\frac{\binom{n-j}{k-j}}{\binom nk}
\sum_{|A|=j}\widehat f_t(A)^2.
}
\tag{C299d}
\]

Proof: for a fixed `S`, the marginal density is `f_S(tau)=2^k p_S(tau)`. Parseval gives

\[
2^k\sum_\tau(p_S(\tau)-2^{-k})^2
=
\sum_{\varnothing\ne A\subseteq S}\widehat f_t(A)^2.
\]

Average over uniform `S` and note that a fixed `j`-set belongs to `S` with probability `binom(n-j,k-j)/binom(n,k)`. QED.

For `k=3`, writing `E_j=\sum_{|A|=j}\widehat f_t(A)^2`,

\[
\boxed{
D_t=\frac18\left[
\frac3n E_1
+\frac{6}{n(n-1)}E_2
+\frac{6}{n(n-1)(n-2)}E_3
\right].
}
\tag{5.1}
\]

So a fresh 3-SAT clause only sees the first three Fourier levels of the **current solution measure**, and C299c gives an exact global budget for those levels under fractional planting.

### 5.2 `ell`-clause scale = an overlap moment

Now expose a block `C_1,...,C_ell` of independent fresh proper `k`-clauses. For a fixed satisfiable `F`, define

\[
R_\ell
:=\frac{|\mathrm{SAT}(F\wedge C_1\wedge\cdots\wedge C_\ell)|}
{|\mathrm{SAT}(F)|a_k^\ell}.
\]

Let `A(sigma,tau)` be the number of coordinates on which two assignments agree. Then

\[
\boxed{
\mathbb E[R_\ell\mid F]=1,
}
\tag{5.2}
\]

and the exact second moment is

\[
\boxed{
\mathbb E[R_\ell^2\mid F]
=
\mathbb E_{\sigma,\tau\sim\mu_F}
\left[r_{n,k}(A(\sigma,\tau))^\ell\right],
}
\tag{C300}
\]

where

\[
\boxed{
r_{n,k}(a)
=
\frac{1-2^{1-k}+2^{-k}\binom{a}{k}/\binom nk}{(1-2^{-k})^2}.
}
\tag{5.3}
\]

### Proof of C300

For one random proper clause, a fixed assignment falsifies it with probability `2^{-k}`. Two fixed assignments both falsify it iff all `k` selected variables lie among their `a` agreement coordinates and the signs choose the common forbidden local pattern. Therefore

\[
\Pr(C\text{ satisfied by both }\sigma,\tau)
=1-2^{1-k}+2^{-k}\frac{\binom ak}{\binom nk}.
\]

Square the solution-count average, average over the two independent `mu_F` samples, and use independence of the `ell` new clauses. Dividing by `a_k^{2ell}` gives C300. QED.

Paley--Zygmund now gives the exact model-specific block-survival lower bound

\[
\boxed{
\Pr(F\wedge C_1\wedge\cdots\wedge C_\ell\text{ SAT}\mid F)
\ge
\left(
\mathbb E_{\sigma,\tau\sim\mu_F}
 r_{n,k}(A(\sigma,\tau))^\ell
\right)^{-1}.
}
\tag{5.4}
\]

At `ell=1`, C300 reduces to C299a:

\[
\mathbb E[R_1^2\mid F]
=1+\frac{2^{-k}}{a_k^2}D(F).
\tag{5.5}
\]

For `k=3`,

\[
r_{n,3}(a)=\frac{48+8\binom a3/\binom n3}{49},
\qquad
1\le r_{n,3}(n)=\frac87,
\]

with `r` asymptotically `1` at independent-overlap scale `a/n=1/2`. Thus the entire cost of sprinkling a logarithmic block can be read directly from the overlap distribution of two uniform satisfying assignments.

## 6. What this says about the 2026 `n/log n` barrier

Carenini's Section 10 says the generic replacement step pays an `exp(O(K))` simulation cost for a clean booster of scale `K`; this is what prevents any positive extra power of `log n`.

C300 gives a model-specific way to see the same obstruction in solution-space geometry. Since

\[
1\le r_{n,k}(a)\le a_k^{-1},
\]

the worst-case overlap moment obeys only

\[
\mathbb E_{\mu_F^2}r_{n,k}(A)^K\le a_k^{-K}=\exp(O(K)),
\tag{6.1}
\]

which exactly reproduces an exponential-in-`K` cost. To beat that cost by this route, one would need a **near-critical model-specific overlap theorem** strong enough to replace (6.1) by a subexponential bound

\[
\boxed{
\mathbb E_{\mu_F^2}r_{n,k}(A)^K=\exp(o(K))
\quad\text{for }K\asymp c\log n
}
\tag{6.2}
\]

on the relevant satisfiable formulas, or a different inequality that extracts the same saving without full overlap concentration.

This is not asserted to imply the Abbe--Montanari window bound by itself; a deterministic-booster-to-random-block comparison still has to be proved. The point is narrower and rigorous: **the missing exponential factor has been relocated to a concrete overlap moment of the near-critical solution measure**, rather than left as a generic local-to-random replacement loss.

That diagnosis is consistent with the current literature. Chatterjee et al. rigorously control the partition function only through the Gibbs-uniqueness regime; their paper explicitly says that extending actual-solution control substantially further would likely resolve the uniform-threshold problem. No source found in the bounded search supplies (6.2) near the small-`k` satisfiability threshold.

## 7. Why this is not metric movement

C299--C300 are exact source-relevant structural identities, but they do **not** prove `Omega_3<0.9698`, let alone `Omega_3=0`. The fixed metric is therefore unchanged.

The concrete remaining obligation is now one of the following source-scale statements:

1. improve the scaling window from `O(n/log n)` to `O(n/log^{1+delta} n)` for some `delta>0`; or
2. directly prove convergence of `theta_{3,n}` by a mechanism not reducible to adjacent-size continuity; or
3. establish a model-specific replacement theorem at `K~log n`, plausibly through a subexponential overlap-moment or an equally strong solution-geometry input.

The next run should **not** manufacture another one-variable cavity bound. The planned new triple is **#9 RANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT**. A concrete target is to test whether a clean `K`-clause booster forces a lower bound on the overlap moment in C300, or to construct an exact counterexample showing that overlap alone cannot replace Carenini's generic simulation step.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD OUTSIDE
  active_source: F0097
  source_target: "uniform random-k-SAT satisfiability threshold for every fixed k>=3"
  first_unresolved_case: k=3
  status: PARTIAL
  source_status: OPEN_CURRENT
  metric: "Omega_3 = limsup theta_{3,n} - liminf theta_{3,n}"
  before: "Omega_3 <= 0.9698"
  after: "Omega_3 <= 0.9698"
  movement: NO_MOVEMENT
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods: [1, 12, 30]
  new_claims:
    - "C299a exact quadratic-variation/local-L2 identity"
    - "C299b-c fractional-moment cavity-energy budget"
    - "C299d exact Fourier localization of cavity energy"
    - "C300 exact block second moment in terms of solution overlap"
  claim_scope: "structural route lemmas only; no source closure and no metric improvement"
  finite_claims: 0
  checker: none
  prior_art_note: "martingale/planted/quiet-planting ingredients are established; no novelty certificate claimed for C299-C300"
  retained_handoff:
    F0001: "OPEN/PARTIAL, handed off after third stuck episode; not reopened"
  next_methods: [9, 20, 24]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 9. Model / scheduler escalation

The product limitation is still real. The exposed automation/task control schema permits prompt/title/schedule/timing/enabled state (and notifications where available), but **no model-family field and no reasoning-effort field**, and it returns no authenticated applied-runtime telemetry. `GPT-6 / maximum` is therefore a prompt request only in this environment.

The current repository reconciliation adds an important nuance to the old P26 denial: `RESULTS.md` records that P26's full prompt update later **succeeded from a different authorized context**, while all R-series edits were denied in another reconciliation context. This is consistent with an account/workspace/ownership boundary, not with a repository workaround. The lawful way to repair a task that returns `You cannot modify this task` is to use the authorized owning context or platform support. Enforcing GPT-6/maximum additionally requires a product/backend surface that exposes explicit model/reasoning selectors and authenticated applied-runtime metadata. I made no scheduler or permission change in this run.
