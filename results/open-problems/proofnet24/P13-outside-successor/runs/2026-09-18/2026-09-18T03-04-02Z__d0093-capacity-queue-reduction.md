Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no authenticated runtime model-family or reasoning-effort selector is exposed, so this was not a verified GPT-6/maximum run and I do not claim otherwise. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `1 -> 2`; methods actually tried: B3 PROVE SOMETHING STRONGER, B12 FIND WHAT IS CONSERVED, B30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# P13 — D0093 second research run: replace all-block success by negative-drift capacity flow

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, second open problem after Theorem 6.1 / estimate (6.3).  
Status after this run: **OPEN / PARTIAL**.

## 1. Continuity and frozen metric

The retired P13 Aldous--Janson I0051 clade-covariance target remains retired and was not reopened. The handed-off P0082 WARM target also remains handed off. The current exclusive P13 claim is D0093, owned by native slot `6aa7b253b37c8191b693d8dc79298d37` in `operations/claims/D0093.md`.

The controlling predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T02-23-34Z__d0093-admission-first-research.md`.

That run froze the source-faithful metric

\[
\beta_{\rm fast}:=\inf\left\{\beta\ge0:\exists\kappa<\infty,\delta>0,
\ \mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)\ge1-n^{-\delta}
\text{ for all large }n\right\},
\]

under exactly the source finite-cycle, i.i.d.-Poisson initial law and fast-regime hypotheses. The certified source frontier is `beta_fast = 2`; the source target is `0`. Auxiliary block lemmas, infinite-line results, Bernoulli initial laws, open-boundary estimates, or conditional reductions do not move this metric.

This run does not complete the missing ARW block-transfer theorem below. Therefore

\[
\boxed{\beta_{\rm fast}:2\to2.}
\]

No metric rename or narrower subdomain is used to manufacture movement.

## 2. Source and current-literature reread

I reread the current canonical claim, the owner/new-method directives, campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the newest P13 report, D0093 intake/attempt material, the current claim surface, and the latest visible P14 state. There is no P14 `runs/2026-09-18/` directory on current master; the latest visible P14 research remains the 2026-09-17 G0007 work, so there was no new P14 theorem requiring a duplicate directed audit in this invocation.

The exact source proof was reread at the mechanism that creates `log^2 n`:

- source sites are spaced at radius `r=K log n`;
- Stage 1 sends particles by lazy random walk to neighboring sources;
- the number arriving at a fixed source is Poisson with parameter below `2 zeta r+2`, and overload beyond `2 zeta' r` has probability `e^{-cr}`;
- Proposition 6.5 says that, for `zeta' < p := lambda/(1+lambda)`, a centered pile of at most `2 zeta' r` particles can be trapped inside `[-r,r]` except with probability `e^{-cr}`;
- the published proof then demands that **every** one of order `n/r` source blocks succeed, so the union bound forces `r` of order `log n`;
- the random-walk work at radius `r` is then charged at order `r^2` per particle, producing `n r^2 = n log^2 n`.

The source's trap construction is stronger than a black-box success probability: Section 4 shows that successive trap-barrier increments are i.i.d. geometric with parameter `p=lambda/(1+lambda)`, and Section 6.2 couples the two-sided confinement process to two such geometric sequences plus an urn controlling which side is used.

A fresh bounded literature search on 18 September 2026 used variants of

- `activated random walk cycle topplings linear log^2 2025 2026`,
- `activated random walk torus odometer subcritical 2025 2026`,
- `finite cycle odometer tightness activated random walk`,
- `Activated Random Walks on Z^d log^2 n`.

It recovered the 2025 Tobias Johnson--Jacob Richey preprint *The odometer in subcritical activated random walk* (arXiv:2510.05514v2), several 2026 ARW papers in other regimes, and the 2026 slow-phase ring paper of de Lima--Rolla--Terra. I found no later primary theorem giving the exact finite-cycle Poisson `O(n)` fast-phase bound requested by D0093. This is bounded negative evidence only, not proof of global openness or a novelty certificate.

Johnson--Richey prove a stretched-exponential one-site odometer tail on `Z` for i.i.d. Bernoulli subcritical data and finite mean odometer. Their paper explicitly says the result **should** extend nearly verbatim to other i.i.d. light-tailed laws, and that the upper-bound proof **should** work for periodic initial configurations. Those are author expectations, not source-matching Poisson finite-cycle theorems, so I did not promote them to D0093 movement. Their layer-percolation formulation is nevertheless relevant below because it parametrizes local stable odometers by a boundary net-flow variable.

## 3. Idea before proof/code

The previous run tried to make each failed block rare enough that adaptive merging would repair only exponentially little total length. Its blocker was that a merged region contains a distributed, history-dependent configuration, whereas Rolla Proposition 6.5 begins from one centered pile.

The new idea is to avoid that large-region restart entirely.

At **one fixed large constant scale** `r`, a source block already has a positive *mean service surplus*: it receives about `2 zeta r` particles, while on the Proposition 6.5 good event it can trap `2 zeta' r` particles, with `zeta<zeta'<p`, and the bad event has probability `e^{-cr}`. Thus one should not require every block to be good. Treat bad/overloaded blocks as temporary service deficits, transport only their excess to neighboring blocks, and use the negative drift of cumulative `arrival - capacity`.

The source proof pays a maximum-block penalty. The proposed replacement pays a **queue-area** penalty. A negative-drift queue has linear total area with polynomially high probability even though a positive fraction of blocks may individually fail.

That observation is independent of the unresolved ARW implementation. I therefore first prove the queue theorem exactly, then isolate the one local ARW flux gadget still missing.

## 4. B3 — stronger theorem: a cyclic negative-drift queue has linear total workload with polynomially high probability

### Theorem P13-D0093-CYCLIC-QUEUE-AREA-03

Let `(X_i)_{i=0}^{K-1}` be i.i.d. real random variables such that

\[
\mathbb E X_0<0
\]

and

\[
\mathbb E e^{\theta_0|X_0|}<\infty
\]

for some `theta_0>0`. Extend the length-`K` sample periodically. On the event `S_K:=sum_{i=0}^{K-1}X_i<0`, define the minimal periodic Lindley workload

\[
Q_i:=\left(\max_{1\le \ell\le K}\sum_{j=1}^{\ell}X_{i-j}\right)_+,
\qquad i\in\mathbb Z/K\mathbb Z,
\]

with indices modulo `K`. Then

\[
Q_{i+1}=(Q_i+X_i)_+
\]

for every `i`. Moreover, for every `delta>0` there is a finite constant `C_delta` such that for all sufficiently large `K`,

\[
\boxed{
\mathbb P\left(S_K<0\ \text{and}\ \sum_{i=0}^{K-1}Q_i\le C_\delta K\right)
\ge1-K^{-\delta}.
}
\]

In fact the same proof gives

\[
\max_i Q_i=O(\log K)
\]

with arbitrarily high polynomial probability.

#### Proof

Because `E X_0<0` and the moment generating function is finite near zero, choose `theta in (0,theta_0)` so small that

\[
\rho:=\mathbb E e^{\theta X_0}<1.
\]

For any fixed segment of length `ell`, exponential Markov gives

\[
\mathbb P\left(\sum_{j=1}^{\ell}X_j\ge t\right)
\le e^{-\theta t}\rho^{\ell}.
\tag{4.1}
\]

Choose

\[
h=\lceil B\log K\rceil
\]

with `B` so large that

\[
K\sum_{\ell\ge h}\rho^\ell\le K^{-\delta-4}.
\]

There are at most `K` cyclic segments of each length. Hence, outside an event of probability at most `K^{-delta-4}`, **no cyclic segment of length at least `h` has nonnegative sum**. In particular the full length-`K` sum is negative, and every maximizing segment in the definition of `Q_i` has length `<h`. Thus on this event

\[
Q_i=\widetilde Q_i:=
\left(\max_{1\le\ell<h}\sum_{j=1}^{\ell}X_{i-j}\right)_+.
\tag{4.2}
\]

From (4.1), uniformly in `i,K,h`,

\[
\mathbb P(\widetilde Q_i\ge t)
\le e^{-\theta t}\sum_{\ell\ge1}\rho^\ell
\le C e^{-\theta t}.
\tag{4.3}
\]

Consequently, for any fixed `alpha in (0,theta)`,

\[
\sup_{i,K}\mathbb E e^{\alpha\widetilde Q_i}<\infty.
\tag{4.4}
\]

Ignore for the moment the at most `h` indices whose length-`h` backward window wraps around the chosen cut of the cycle. For the remaining indices, group them by residue modulo `h`. Inside one residue class the windows of `X` used to define the corresponding `widetilde Q_i` are disjoint. Therefore those `widetilde Q_i` are independent. By (4.4) and an ordinary Chernoff bound, there are constants `a,c>0`, independent of `K`, such that for every residue class containing `m` indices,

\[
\mathbb P\left(\sum \widetilde Q_i>a m\right)\le e^{-cm}.
\]

There are only `h=O(log K)` residue classes, and each has order `K/h` terms. Hence

\[
\mathbb P\left(\sum_{\text{nonwrapping }i}\widetilde Q_i>aK\right)
\le h e^{-cK/h},
\tag{4.5}
\]

which is smaller than `K^{-delta-3}` for all sufficiently large `K`.

For the at most `h` wrapping indices, (4.3) and a union bound show that

\[
\max_i\widetilde Q_i\le D\log K
\]

with probability at least `1-K^{-delta-3}` after taking `D` large enough. Their total contribution is then at most

\[
Dh\log K=O((\log K)^2)=o(K).
\]

Combining this with (4.5) and the no-long-nonnegative-segment event proves

\[
\sum_iQ_i\le C_\delta K
\]

with probability at least `1-K^{-delta}` for all large `K`. The recursion

\[
Q_{i+1}=(Q_i+X_i)_+
\]

is the standard backward-supremum identity; because the total period sum is negative, adding a full period can only decrease a backward partial sum, so the supremum is attained within one period. This completes the proof. `square`

### Corollary: arrivals and capacities

Let `(A_i,C_i)` be i.i.d. nonnegative arrival/capacity pairs with an exponential moment, and suppose

\[
\mathbb E A_i<\mathbb E C_i.
\]

Take `X_i=A_i-C_i`. Then the theorem gives a periodic overflow process

\[
Q_{i+1}=(Q_i+A_i-C_i)_+
\]

whose total backlog satisfies

\[
\sum_iQ_i=O(K)
\]

with arbitrarily high polynomial probability. Since `sum_i A_i=O(K)` with exponentially high probability, any local processor whose work is bounded by

\[
K_0(1+A_i+Q_i)
\]

at block `i` has total work `O(K)` with polynomially high probability.

This theorem is not ARW-specific. Its role is to show that constant-scale local failures do **not** force a logarithm if the dynamics can pass excess mass between blocks while preserving a negative mean service deficit.

## 5. B12 — the conserved quantity is total unused trap capacity

For the capacity queue, define the unused service at block `i` by

\[
U_i:=(C_i-Q_i-A_i)_+.
\]

The Lindley recursion can be written exactly as

\[
Q_{i+1}=Q_i+A_i-C_i+U_i.
\]

Summing around the cycle cancels the workload telescopically and gives the exact conservation law

\[
\boxed{
\sum_i U_i=\sum_i(C_i-A_i).
}
\tag{5.1}
\]

Thus the global quantity that matters is not `min_i C_i` and not the largest failed block. It is the **aggregate capacity surplus**. The published one-scale proof throws this conservation away by requiring every local deficit to be zero.

The source constants already make the mean surplus positive at one fixed scale. Put

\[
p=\frac{\lambda}{1+\lambda},
\qquad \zeta<\zeta'<p.
\]

For a large integer radius `r`, let

\[
B_r:=\lfloor2\zeta' r\rfloor.
\]

Proposition 6.5 supplies `c>0` such that a centered `B_r`-particle source has a confinement/trapping certificate in `[-r,r]` except with probability at most `e^{-cr}`. Define the **formal local service capacity**

\[
C_r:=B_r\,\mathbf 1_{G_r},
\]

where `G_r` is that good event. Then

\[
\mathbb E C_r\ge(2\zeta' r-1)(1-e^{-cr}).
\tag{5.2}
\]

Meanwhile the source Stage-1 arrival at a source is Poisson with mean at most

\[
2\zeta r+2.
\tag{5.3}
\]

Therefore, because `zeta'<p` and `zeta<zeta'`, for all sufficiently large **fixed** `r`,

\[
(2\zeta' r-1)(1-e^{-cr})>2\zeta r+2,
\]

so the idealized block increment satisfies

\[
\boxed{
\mathbb E(A_r-C_r)<0.
}
\tag{5.4}
\]

This is the main conceptual movement of the run: one does **not** need `r` to grow like `log n` in order to have enough capacity. A large constant `r=r(zeta,lambda)` already has a strict service surplus in expectation. The logarithm is introduced solely by converting a negative-drift aggregate problem into an all-blocks-good event.

Equation (5.4) is an exact inequality from the source overload mean and Proposition 6.5 failure bound. It is **not yet** a statement that the actual ARW dynamics realize the capacities `C_i` as a directed queue. That realization is the remaining theorem below.

## 6. B30 — localize the source problem to one constant-width flux gadget

The previous run's missing statement was a large, history-robust distributed repair lemma. The queue theorem shows that this was stronger than necessary.

A source-exact proof would follow from the following one-scale interface.

### Remaining local obligation P13-D0093-BLOCK-FLUX

Fix source parameters and then one sufficiently large constant radius `r` satisfying (5.4). Construct, from the actual unused ARW instruction stacks in a source cell, a local stable-odometer/acceptable-toppling processor with these properties:

1. it receives an integer incoming overflow `q>=0` plus the Stage-1 source load `A`;
2. on its local good stack event it can absorb at least `B_r` particles, and on a bad event it may absorb fewer;
3. it exports exactly
   \[
   q'=(q+A-C)_+
   \]
   particles through a specified neighboring interface (or an equivalent two-sided flux rule reducible to a negative-drift one-dimensional workload);
4. its local toppling cost is at most a constant depending on `r` times `1+q+A` with an exponential-moment domination;
5. after concatenating processors, matching boundary fluxes gives a genuine nonnegative stable odometer on the cycle, so the least-action principle bounds the true stabilization odometer;
6. the capacity/arrival sequence has enough finite-range or renewal independence for Theorem P13-D0093-CYCLIC-QUEUE-AREA-03 (or its routine finite-range variant).

If this block-flux statement holds, then (5.4) and the queue theorem give

\[
T=O(n)
\]

with probability at least `1-n^{-delta}` for some `delta>0`, i.e. the exact source target `beta_fast=0`.

### Why this is now a genuinely local problem

The width `r` is fixed after `(zeta,lambda)` are fixed. There is no `log n`, no growing merged region, and no need to condition a Proposition 6.5 restart on an arbitrarily complicated large-scale history. The unresolved mathematics is confined to how a **single constant-width ARW block transmits excess boundary flux**.

That is precisely the language in which the 2025 layer-percolation machinery is organized. Johnson--Richey recall the classes

\[
\mathcal O_n(\sigma,u_0,f_0)
\]

of local stable odometers with a specified boundary net flow `f_0`, and the HJJ correspondence maps these to infection paths. Thus `f_0` is a natural candidate for the queue variable `q`: instead of literally forcing particles to walk clockwise, one can try to concatenate **stable odometers with matching fluxes** and invoke least action. This avoids inventing a nonphysical directed random-walk routing rule.

I did not claim this final interface theorem. The checked Johnson--Richey result is infinite-line/Bernoulli and their comments about light-tailed and periodic extensions are not the needed finite-cycle Poisson block statement.

### A second useful observation from the source exploration rules

Section 4 explicitly says that an explorer examines the next unused instruction at its current position, a sleep instruction simply leaves the explorer in place, and on a successful trap plan the path can later be replayed by acceptable topplings even if the physical particle temporarily sleeps. This suggests a possible restart mechanism for a failed block: discard the planned traps and **burn the revealed prefixes** by acceptable topplings so that only fresh stack tails remain before a coarser transfer step.

However, the source proves this replay/legalization carefully only for the ordered successful trap construction. I have not proved that a failed two-sided exploration can always be burned and concatenated without waking a previously finalized neighboring trap. Therefore this is recorded as a route, not as a theorem.

## 7. What the three methods did

**B3 — PROVE SOMETHING STRONGER.** Instead of another ARW-specific tail estimate, I proved the stronger abstract statement that any exponentially light negative-drift cyclic service network has linear total queue area with polynomially high probability. This succeeds mathematically and removes the need for an all-block success event. It does not itself move `beta_fast` because an ARW flux realization is still missing.

**B12 — FIND WHAT IS CONSERVED.** The exact invariant is (5.1): total unused service equals total capacity minus total arrivals. Combining the source's Poisson load estimate and Proposition 6.5 shows a strict **constant-scale mean capacity surplus** (5.4). This identifies the published union bound, not capacity itself, as the logarithmic bottleneck.

**B30 — ONE SCALE / ONE DIRECTION AT A TIME.** The remaining proof obligation has been reduced from a growing distributed-repair theorem to one fixed-width boundary-flux gadget. The layer-percolation boundary-flow parameter `f_0` is the most natural language for the next attack. The attempt does not yet prove the required nonnegative stable-odometer concatenation, so the source metric remains unchanged.

## 8. Counterexample pressure and why this does not overclaim

The first D0093 run already attacked the negation and ruled out the simplest Poisson-pile obstruction: any fixed polynomial local pile cost has linear aggregate budget with arbitrarily high polynomial probability. This run exposes an additional reason a genuine counterexample would need a more global mechanism: at constant scale the source itself gives mean trap capacity strictly larger than mean arrival load.

That still does not prove the source statement. A model can have positive mean service surplus and yet fail to admit the directed/flux-local decomposition needed by the queue theorem. The exact possible obstruction is dynamical: trap certificates use the same instruction stacks as the eventual transfer, and failed explorations may corrupt precisely the local information needed by a naive retry. The next run must either construct the flux interface or exhibit a concrete stack-history obstruction to it.

No finite counterexample candidate was produced, so no exact-arithmetic checker was warranted. The new theorem is analytic and its proof is on this page; I did not spend the run manufacturing a redundant checker.

## 9. Status, stagnation, next methods

Frozen source metric:

`beta_fast: 2 -> 2`.

D0093 unchanged-run count:

`1 -> 2`.

This is not yet a three-run stuck trigger. Status remains **OPEN / PARTIAL**. No source closure, audit vote, or novelty certificate is claimed.

If no intervening source resolution or peer result changes the state, the next unused method triple should be:

- **B11 DUALIZE:** treat the block transfer through the stable-odometer / boundary-flux dual language and the layer-percolation infection path;
- **B19 MAKE IT AN ALGORITHM:** write the exact constant-width processor and the gluing rule that turns local fluxes into a periodic stable odometer;
- **B20 FIND WHY THE ALGORITHM FAILS:** if concatenation breaks, isolate whether the obstruction is nonnegativity, stack-history dependence, or a boundary-flux mismatch.

## 10. P14 directed-audit duty

P13's directed secondary audit duty remains P14. Current master has no `proofnet24/P14-probability-correlation/runs/2026-09-18/` directory. The latest visible P14 research is the existing 2026-09-17 G0007 line. Prior completed P13->P14 component audits are retained; I did not repeat them merely to create an audit artifact.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  root: proofnet24/P13-outside-successor
  category: CLOSABLE_OUTSIDE
  target: D0093
  source: "Leonardo T. Rolla, Activated Random Walks on Z^d, Probab. Surveys 17 (2020), Section 6.2, second open problem after Theorem 6.1 / (6.3)"
  claim: operations/claims/D0093.md
  metric: beta_fast
  metric_domain: "finite cycle; iid Poisson(zeta) active initial law; symmetric nearest-neighbor ARW; exact source fast-regime hypotheses"
  before: 2
  after: 2
  movement: false
  no_movement_count_before: 1
  no_movement_count_after: 2
  status: OPEN_PARTIAL
  methods: [3, 12, 30]
  new_math:
    - "P13-D0093-CYCLIC-QUEUE-AREA-03: negative-drift exponentially-light cyclic Lindley queue has total workload O(K) with arbitrarily high polynomial probability"
    - "exact conserved slack identity sum unused_capacity = sum(capacity-arrival)"
    - "source Proposition 6.5 plus Stage-1 Poisson mean imply strict positive mean service surplus at one sufficiently large fixed constant scale"
    - "source target conditionally reduces to one constant-width ARW boundary-flux / stable-odometer interface"
  source_metric_credit_for_auxiliary_results: 0
  literature_check_date: 2026-09-18
  literature_limit: "bounded search; no global openness or novelty claim"
  closure_authorized: false
  p26_end_to_end_audit: missing
  second_other_track_end_to_end_audit: missing
  p14_directed_audit_this_run: none_new_to_audit
  next_methods: [11, 19, 20]
  next_exact_obligation: "construct or refute the fixed-width block-flux stable-odometer interface realizing negative-drift capacity flow on the actual ARW stacks"
  retired_targets_reopened: false
```

## 12. Delivery statement

This report is the sole intended immutable run report for this invocation. No shared root ledger, peer file, historical report, claim ownership, email/Gmail item, Drive item, public post, permission, workflow, or schedule is modified by this worker. The original I0051 retirement and P0082 handoff are preserved.
