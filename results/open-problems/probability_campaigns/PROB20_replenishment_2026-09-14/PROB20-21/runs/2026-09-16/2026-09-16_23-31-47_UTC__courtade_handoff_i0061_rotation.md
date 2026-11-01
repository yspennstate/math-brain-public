Model actually exposed: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested, but the exposed scheduler/runtime provides no model selector, reasoning-effort selector, or authenticated effort telemetry. Courtade frozen metric: **6 -> 6, NO MOVEMENT**; mandatory hard-target handoff after two completed recovery cycles. Successor I0061 metric: **0/2 -> 0/2, NO MOVEMENT**. Methods this run: **B2 attack the negation first, B18 say it in another language, B20 find why the obvious algorithm fails**.

# PROB20-21 handoff and same-slot rotation admission

## 0. Executive status

The Courtade--Kumar source remains **OPEN / PARTIAL**. This slot has now exhausted the two owner-authorized stuck-recovery cycles without moving the frozen all-functions/full-noise dimension beyond `n=6`, so this run does **not** manufacture a third special-case Courtade lemma. It preserves a source-exact handoff and passes the rotation gate.

The successor selected from the outside queue is **I0061**, Auffinger--Damron--Hanson, *50 years of first passage percolation*, Question 18: upper-tail large-deviation rate existence for bounded nondegenerate passage times. A bounded current-status and ownership admission was completed at the captured repository snapshot. The exact intended problem remains open after Basu--Ganguly--Sly's substantial regularity-class result. This report also finds a literal sign/domain defect in the printed survey wording; that defect is **not** promoted as a refutation of the intended open problem.

Captured repository snapshot before new research:

`master @ eebef8cea0615b116ea78d6cd393077fab8f91bd`.

---

# 1. Courtade--Kumar: final handoff from this slot

Outside source: Thomas A. Courtade and Gowtham R. Kumar (2013), *Which Boolean Functions are Most Informative?*, arXiv:1302.2512, Conjecture 1.

For uniform `X in {0,1}^n` and `Y=X xor Z` with iid `Bernoulli(alpha)` noise, the source target is

\[
I(b(X);Y)\le 1-h_2(\alpha)
\qquad
\text{for every Boolean }b\text{ and }0\le\alpha\le\tfrac12.
\]

The newest own report was recovered by path-scoped commit history, not by filename guessing:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/runs/2026-09-16/2026-09-16_22-00-03_UTC__report.md`

creation commit

`920dd2e025410296cc30bfbb673d89d9740149b4`.

That report is `STUCK_RECOVERY_2_SPECIAL_CASE_SUCCESS`. It retains:

- complete exact all-function/all-noise certification through `n=6`;
- all-function `n=7` coverage on
  \[
  [0,1/5000]\cup[67/135,1/2];
  \]
- unresolved all-function middle interval
  \[
  [1/5000,67/135];
  \]
- full-noise certification of the one-point dictator perturbation orbit;
- full-noise certification of the balanced antipodal two-point dictator perturbation orbit represented by mask
  `15555555555555555555555555555557`.

The fixed fleet metric therefore remains

\[
\boxed{n_{\rm full}=6.}
\]

The source itself still says the conjecture remains open. The current Javanmard--Woodruff arXiv:2601.09679 record (submitted 14 January 2026) proves the arbitrary-bias **coordinate-wise sum** inequality and improves the high-noise regime, not the full-vector theorem. Chen--Watanabe--Yu arXiv:2607.28162 (30 July 2026) studies a divergence analogue, not this BSC mutual-information target. A dated bounded check on 16 September 2026 found no accepted source-valid full proof or counterexample.

### Handoff obstruction ledger

The exact remaining obligation is

\[
\boxed{
\forall f\in\mathcal S_7,\quad
\forall\alpha\in[1/5000,67/135],\quad
\log2-h(\alpha)-I(f(X);Y)\ge0.
}
\]

Courtade--Kumar two-coordinate compression reduces the seven-bit search to the source compressed family; the internal complement/antipodal symmetry further reduces the exact finite family, but that does not itself settle the continuous middle interval.

Routes already tried and why they did not close the source target:

1. exact full enumeration works through `n=6` but the direct all-`n=7` transcendental interval solver timed out;
2. high-noise Fourier/entropy expansions are perturbative and do not cover the middle interval;
3. exact-past / scalar bias recursions discard selector-recovery information; a scalar Bellman route has a recorded obstruction;
4. the full information-defect derivative is not sign-monotone even for the nearest one-point dictator perturbation;
5. low-noise sensitive-degree bounds reach `alpha=1/5000` but not the middle;
6. two stuck-recovery cycles solved the two most dangerous near-dictator special orbits but did not move the all-function metric.

A fresh neighboring FEI history read at the captured snapshot shows its newest report commit `8b4905bbba70396f7c6ab83139f20426b0c87e61` is itself a defect-two stuck analysis. No FEI theorem is imported into the Courtade handoff.

Audits for a full Courtade claim: `P26 = NONE`, distinct `OTHER = NONE`, because there is no full claim to audit.

**Courtade slot disposition:** source remains open and is handed off for future reassignment with a fresh route. The research recurrence is not disabled.

---

# 2. Rotation admission: I0061 / Auffinger--Damron--Hanson Question 18

## 2.1 Exact outside source

Source: Antonio Auffinger, Michael Damron, Jack Hanson, *50 years of first passage percolation*, arXiv:1511.03262 / AMS University Lecture Series 68, Question 18.

For iid nonnegative passage times `tau_e` on nearest-neighbor edges of `Z^d`, define

\[
p_n^u(\epsilon)
=
\Pr\!\left(T(0,ne_1)>n(\mu(e_1)+\epsilon)\right).
\]

The printed Question 18 says: assuming passage times are bounded and not concentrated at one point, show there exists a convex function `I^u(epsilon)` such that

\[
\lim_{n\to\infty}\frac1{n^d}\log p_n^u(\epsilon)=I^u(\epsilon).
\tag{2.1}
\]

Immediately before the question the survey records Kesten's volume-speed upper bound for bounded weights and says existence of the corresponding rate limit is open.

## 2.2 Current-status check

Basu--Ganguly--Sly, *Upper Tail Large Deviations in First Passage Percolation*, arXiv:1712.01255 / CPAM 74 (2021), proves rate-function existence for compactly supported laws having a continuous density on `[0,b]`. Their paper explicitly says this assumption is not optimal, states the result for `zeta in (0,b-mu)`, and formulates the rate with the standard positive sign

\[
-\frac1{n^2}\log\Pr(T_n\ge(\mu+\zeta)n)\to r(\nu,\zeta)>0.
\tag{2.2}
\]

They note their method extends to higher dimensions. This is a major partial answer but is **not** the full bounded-nondegenerate class in Question 18.

Later relevant work found in the dated check:

- Shuta Nakajima (2019/2021 line) treats other tail classes and even constructs an unbounded continuous finite-exponential-moment law with no rate function; it does not refute the bounded source class.
- Cosco--Nakajima (2023) gives variational formulas under explicit stretched/exponential tail assumptions, a different regime.
- Wai-Kit Lam--Shuta Nakajima, *Moderate deviations in first-passage percolation for bounded weights*, Journal of Mathematical Physics 67 (2026), 073302, studies moderate/near-large deviations under fluctuation hypotheses and does not supply the missing unrestricted bounded-law rate-limit theorem.

A bounded search through 16 September 2026 found no later theorem removing all distributional regularity from the bounded nondegenerate source class.

## 2.3 Ownership / duplication check at the captured snapshot

`QUEUE.md` lists I0061 as the Question-18 bounded-passage large-deviation problem. Root `POSTED.md` does not list I0061 as excluded/closed. Exact fetch of

`operations/claims/I0061.md`

at snapshot `eebef8...` returned `404 Not Found`. A bounded repository search for `I0061` returned the queue/intake records but no owner report or claim; commit search for the literal ID returned no commits. By contrast, adjacent I0060 is explicitly claimed by R12, so it was rejected as a successor.

Thus I0061 is source-verified and unassigned **at the captured snapshot under the repository evidence available to this worker**. Canonical shared claim insertion is left to the coordinator/main-agent ledger merge; this worker does not edit shared root/peer files.

## 2.4 New fixed metric; no inherited Courtade number

Successor metric:

`Q18_full_clauses = number of the two intended source obligations {rate-limit existence; convexity of the positive rate} proved for the ENTIRE class of bounded non-point-mass passage-time laws (all source dimensions/feasible epsilons)`.

Goal: `2/2`.

Baseline before this run: `0/2`.

After this run: `0/2`.

The Basu--Ganguly--Sly regularity-class theorem does not count as full-class movement. Courtade's `n=6` is not inherited by this successor.

---

# 3. B2 — attack the source statement literally before proving it

There is a genuine wording defect in the printed Question 18.

Assume the passage times are supported in `[0,M]`. Deterministically, the straight coordinate path from `0` to `ne_1` contains exactly `n` edges, each of weight at most `M`. Hence

\[
T(0,ne_1)\le nM.
\tag{3.1}
\]

For every

\[
\epsilon>M-\mu(e_1),
\]
we have `n(mu+epsilon)>nM`, so

\[
p_n^u(\epsilon)=0
\qquad\text{for every }n.
\tag{3.2}
\]

Therefore

\[
\frac1{n^d}\log p_n^u(\epsilon)=-\infty.
\tag{3.3}
\]

Consequently no ordinary real-valued convex function on all positive `epsilon` can satisfy (2.1) as printed.

There is also an internal sign mismatch in the survey. Its preceding heuristic writes

\[
p_n^u(\epsilon)\approx\exp(-n^d I^u(\epsilon)),
\]

which corresponds to

\[
-\frac1{n^d}\log p_n^u(\epsilon)\to I^u(\epsilon),
\]
not (2.1). Basu--Ganguly--Sly use exactly this corrected positive-rate sign and explicitly restrict to the feasible interval `0<zeta<b-mu`.

**Verdict on this observation:** `LITERAL_SOURCE_WORDING_DEFECT`, not a refutation of the intended open mathematical problem. If Question 18 is read with the standard feasible domain and the positive rate `R=-lim n^{-d} log p`, the trivial contradiction disappears. The successor research target is that corrected intended formulation.

This distinction is essential: the source's intended rate-existence problem remains open for arbitrary bounded nondegenerate laws.

---

# 4. B18 — rewrite the missing regularity step as an atom-safe change of measure

The Basu--Ganguly--Sly theorem assumes a continuous density. A natural obstacle to extending geometric dilation arguments is that literal dilation of edge weights can be singular for atomic passage-time laws. The following elementary reparameterization avoids that problem completely.

Let `F` be any nondegenerate probability law supported in `[0,M]`. Define the log moment generating function

\[
\Lambda(\theta)=\log\int e^{\theta x}\,dF(x),
\qquad \theta\ge0,
\]

and the exponentially tilted law

\[
\boxed{
\frac{dF_\theta}{dF}(x)=e^{\theta x-\Lambda(\theta)}.
}
\tag{4.1}
\]

This is well-defined for every bounded law, including purely atomic laws.

## Lemma 4.1 — atom-safe monotone volume tilt

For every bounded nondegenerate `F` and every `theta>0`:

1. `F_theta` is mutually absolutely continuous with `F` on the same support;
2. `F_theta` first-order stochastically dominates `F`;
3. its mean is strictly larger than the mean of `F`;
4. for `N` independent edges,
   \[
   D(F_\theta^{\otimes N}\|F^{\otimes N})
   =N\,[\theta\Lambda'(\theta)-\Lambda(\theta)].
   \tag{4.2}
   \]

### Proof

(1) follows immediately because the density in (4.1) is strictly positive and finite on `[0,M]`.

For (2), if `theta_2>theta_1`, then

\[
\frac{dF_{\theta_2}}{dF_{\theta_1}}(x)
=C e^{(\theta_2-\theta_1)x},
\]

which is increasing in `x`. Thus the family has monotone likelihood ratio, implying first-order stochastic dominance. Equivalently, for every bounded increasing `phi`,

\[
\frac{d}{d\theta}\mathbb E_{F_\theta}[\phi(X)]
=\operatorname{Cov}_{F_\theta}(\phi(X),X)\ge0,
\]

because two increasing functions of one random variable have nonnegative covariance.

Taking `phi(x)=x`,

\[
\frac{d}{d\theta}\mathbb E_{F_\theta}X
=\Lambda''(\theta)
=\operatorname{Var}_{F_\theta}(X)>0
\]

for a nondegenerate law, proving (3).

Finally,

\[
D(F_\theta\|F)
=\int(\theta x-\Lambda(\theta))\,dF_\theta(x)
=\theta\Lambda'(\theta)-\Lambda(\theta),
\]

and relative entropy tensorizes, proving (4.2). QED.

### Why this is potentially useful

Equation (4.2) gives exactly a **volume-order** entropy cost when a box containing `Theta(n^d)` edges is tilted upward. Unlike weight dilation, it does not require a density and does not break on atoms. Thus the regularity gap can be moved from measure theory to geometry: can an upward tilt be converted into the required deterministic/typical metric slowdown strongly enough to compare scales?

This lemma is not a proof of Question 18. It is a candidate replacement for one density-sensitive ingredient.

---

# 5. B20 — locate the precise failure of naive block subadditivity

A first attempt at Question 18 is to tile a large box by independent `n`-boxes and invoke a Fekete-type argument on

\[
a_n(\epsilon)=-\log p_n^u(\epsilon).
\]

The obstruction is structural, not bookkeeping.

The event

\[
T(0,ne_1)>n(\mu+\epsilon)
\]

is a **minimum over all paths**. Making the designated point-to-point crossing slow in each tile does not force a larger-scale point-to-point crossing to be slow: a global geodesic may leave the prescribed crossing geometry, enter neighboring tiles through different faces, backtrack, or bypass the local bad endpoints. Therefore there is no direct implication of the form

\[
\bigcap_j\{T_j>n(\mu+\epsilon)\}
\subseteq
\{T_{\rm large}>kn(\mu+\epsilon-o(1))\}
\]

for a simple collection of endpoint events.

What does glue is not a scalar passage time but an **entire boundary-to-boundary random metric profile**. This explains both the metric-dilation architecture of Basu--Ganguly--Sly and why a generic Fekete argument has resisted the full bounded-law problem.

The atom-safe tilt of Section 4 suggests a concrete new route:

> Replace geometric weight dilation by exponential tilting inside finite boxes; prove a scale-comparison theorem for the induced boundary metric profiles, with error `o(n)` and entropy cost `O(n^d)`, uniformly over arbitrary bounded `F`.

The first genuinely missing statement is therefore not another tail estimate. It is a **strict metric-uplift lemma**: for a suitable `theta=theta(epsilon,F)>0`, the tilted law must make the relevant finite-box boundary metric uniformly slower than the original time constant by the target epsilon, up to controllable boundary error, in a form stable under gluing.

The stochastic-order statement `F_theta >=_st F` alone is insufficient: first-order domination does not automatically quantify a strict increase of every relevant finite-volume boundary distance or the infinite-volume time constant, especially near atomic/percolative regimes. That is the precise place the next run should attack.

---

# 6. Proved / conditional / open ledger for the successor

## PROVED this run

- The printed Question 18 has a literal sign/domain defect: outside the feasible epsilon range the event is impossible, while the displayed limit is written with the opposite sign from the preceding positive-rate heuristic.
- Lemma 4.1: exponential tilting gives an atom-safe, stochastically increasing change of measure with exact volume-order relative entropy cost for every bounded nondegenerate law.
- Naive scalar endpoint-event block subadditivity does not furnish a valid gluing implication; a boundary metric profile is required.

## KNOWN / imported

- Kesten gives volume-speed upper-tail bounds for bounded passage times.
- Basu--Ganguly--Sly prove rate existence under compact-support continuous-density regularity and describe the metric-dilation route; their theorem is a partial answer to the intended Question 18.

## OPEN

- Full rate-limit existence for every bounded non-point-mass law under the corrected feasible-domain/positive-rate formulation.
- Convexity of the resulting full-class rate.
- A strict quantitative metric-uplift/gluing lemma for arbitrary bounded laws, particularly atomic laws.

No finite enumeration claim was promoted in this run, so no checker artifact was manufactured merely for bookkeeping.

---

# 7. Next attack after rotation

The next run should remain on I0061, not return to Courtade absent reassignment. It should use three methods not equal to this run's triple. Highest-value target:

\[
\boxed{
\text{prove or refute a uniform strict increase of the FPP time constant / box metric under }F\mapsto F_\theta.
}
\]

A useful split is:

1. atomic two-point laws, especially Bernoulli `{0,1}` on both sides of the percolation threshold;
2. laws with minimum atom below `p_c`, where strict comparison theorems may apply;
3. the percolating-minimum regime, where the time constant can be zero and the correct uplift statement may require choosing `theta` past a threshold rather than infinitesimal differentiation.

Suggested next methods: **B21 ask who else has this shape, B23 assume the opposite, B27 swap the quantifiers**.

---

# 8. ledger_delta for coordinator

```yaml
native_task_id: 6aa7ebbe26308191a40003a950a2307a
predecessor_target_id: PROB20-21 / Courtade-Kumar-2013-Conjecture-1
report_kind: HARD_HANDOFF_AND_SUCCESSOR_ADMISSION
input_snapshot_sha: eebef8cea0615b116ea78d6cd393077fab8f91bd
previous_report:
  path: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/runs/2026-09-16/2026-09-16_22-00-03_UTC__report.md
  commit: 920dd2e025410296cc30bfbb673d89d9740149b4
predecessor_metric:
  name: largest_n_all_functions_entire_noise_interval
  before: 6
  after: 6
  movement: NO_MOVEMENT
  unchanged_count_since_last_metric_move: 6
  stuck_recovery_cycles_completed: 2
  disposition: HANDOFF_OPEN_PARTIAL
predecessor_audits:
  P26_same_full_claim: NONE
  distinct_OTHER_same_full_claim: NONE
successor:
  canonical_id: I0061
  source: Auffinger-Damron-Hanson, 50 years of first passage percolation, Question 18
  category: HARD_OUTSIDE
  admission: SOURCE_CURRENT_STATUS_OWNERSHIP_CHECKED_AT_SNAPSHOT
  canonical_claim_file_at_snapshot: ABSENT_404
  posted_conflict: NONE_FOUND
  prior_id_commits: NONE_FOUND_BY_BOUNDED_SEARCH
  shared_claim_write: COORDINATOR_PENDING
successor_metric:
  name: Q18_full_clauses
  definition: count of {full-class rate-limit existence, full-class positive-rate convexity} proved for all bounded non-point-mass laws
  before: 0/2
  after: 0/2
  movement: NO_MOVEMENT
methods:
  B2: literal negation check found sign/domain defect but not an intended-problem counterexample
  B18: atom-safe exponential-tilt reformulation and entropy-cost lemma
  B20: isolated failure of scalar block subadditivity and metric-profile gluing obligation
mathematical_status: OPEN / PARTIAL LITERATURE
next_methods: [B21, B23, B27]
```

## Operational note

The scheduler/model situation is unchanged: the exposed interface does not provide a model selector or reasoning-effort selector. GPT-6/maximum is a prompt request only. No claim of full-hour execution or subagent activity is made.

This worker did not edit root ledgers, peer reports, permissions, public resources, email, or Drive, and did not create a new schedule.
