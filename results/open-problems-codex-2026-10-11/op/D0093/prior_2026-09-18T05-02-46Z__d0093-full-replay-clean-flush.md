Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime does not authenticate a GPT-6 model-family or maximum-reasoning selector, so I do not claim that configuration. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `3 -> 4`; methods actually tried: B6 DEFORM TO A POINT YOU CAN SOLVE, B16 COMPUTE EVERY SMALL CASE, B25 COUNT THE SAME THING TWICE. STUCK RECOVERY 1 continues.**

# P13 — D0093 fourth research run: chronological full replay removes the two-sided corruption obstruction

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, second Open Problem after Theorem 6.1 / equation (6.3).  
Status after this run: **OPEN / PARTIAL / STUCK RECOVERY 1**.

## 1. Continuity, exclusions, ownership, and frozen metric

The former P13 I0051 Aldous--Janson clade-covariance target remains RETIRED and was not reopened. P0082 remains handed off after its six-run CLOSABLE rotation and was not reopened. The current exclusive P13 claim remains D0093, owned by native slot `6aa7b253b37c8191b693d8dc79298d37`.

The controlling predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T04-19-16Z__d0093-stuck-recovery-01-static-capacity-obstruction.md`.

That report triggered STUCK RECOVERY 1 after three unchanged D0093 runs and selected exactly one recovery: **port the analogous Section 4 corrupted-instruction shielding/unwind technique to the two-sided Proposition 6.5 geometry**. It scheduled B6/B16/B25 for the present run.

The source-faithful metric remains

\[
\beta_{\rm fast}:=\inf\left\{\beta\ge0:\exists\kappa<\infty,\delta>0,
\ \mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)\ge1-n^{-\delta}
\text{ for all large }n\right\},
\]

under exactly the source finite cycle, i.i.d.-Poisson initial law, symmetric nearest-neighbor jumps, and fast-regime hypotheses used for (6.3). The certified source frontier is `beta_fast=2`; the requested source conclusion is the order-`n` bound.

This run proves a source-native clean-flush theorem for the local two-sided exploration and removes the previous freshness/corruption obstruction, but it does not yet yield a finite-cycle bound with exponent below 2. Hence

\[
\boxed{\beta_{\rm fast}:2\to2}
\]

and the no-movement count is four. The local theorem is recorded as auxiliary progress only.

## 2. Required repository/source/current-status reread

Before new research I reread the controlling owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current D0093 claim, the newest P13 report, D0093 intake and attempt-ledger hits, and neighboring ownership/admission material. The root `RESULTS.md` P13 row is historical/stale relative to the create-only D0093 claim and immutable P13 D0093 reports; I did not reset to it. Repository-wide current search still shows D0093 exclusively owned by this P13 slot and no later P13 D0093 report beyond the 04:19:16Z predecessor at the start of research.

The source PDF was rechecked directly. Section 6.2 fixes the ring `Z_n`, i.i.d. Poisson initial counts of mean `zeta`, symmetric nearest-neighbor jumps, and total topplings `T`. Theorem 6.1 gives the fast estimate

\[
\mathbb P(T\le \kappa n\log^2n)\ge1-n^{-\delta},
\]

and the next explicit Open Problem asks to improve (6.3) to one without the `log^2 n` term. The proof chooses

\[
\frac{\lambda}{1+\lambda}>\zeta'>\zeta,
\qquad r=\lfloor K\log n\rfloor,
\]

routes particles to sources by acceptable topplings, and then invokes Proposition 6.5, whose local input is at most `2 zeta' r` particles concentrated at one source and whose local failure probability is exponentially small in `r`.

The source also explicitly says that Section 4's exploration is non-Markovian: it reveals instructions to choose a trap, and sites containing revealed-but-unused instructions are `corrupted`. Section 4 emphasizes acceptable topplings as a way to enforce activity. In the site-wise representation a toppling is acceptable whenever the site contains any particle at all, including one sleeper; operationally one may force that sleeper active and topple it. Those exact conventions are what make the replay below valid.

A fresh bounded literature pass dated 2026-09-18 used variants of

- `"Removing the log^2 n factor" activated random walks`,
- `activated random walk cycle topplings linear bound 2026`,
- `fast phase activated random walk finite cycle Poisson O(n)`,
- `"The odometer in subcritical activated random walk"`,
- `activated random walk ring slow phase 2026`.

It recovered the original cycle work of Basu--Ganguly--Hoffman--Richey, Tobias Johnson--Jacob Richey (2025), *The odometer in subcritical activated random walk* (stretched-exponential subcritical one-site odometer tails on `Z` for i.i.d. Bernoulli initial data), and the April 2026 de Lima--Rolla--Terra slow-phase ring paper. I found no checked primary source stating the exact finite-cycle i.i.d.-Poisson order-`n` fast estimate asked here. This is **bounded negative evidence only**, not proof of global openness or publication novelty.

PDF text extraction from the arXiv source was available. Required PDF screenshot attempts on the relevant Section 4 and Section 6 pages failed with a cache-miss error in the screenshot service. I therefore record a **PDF_VISUAL_ACCESS_FAILURE** for this run; no mathematical claim below depends on interpreting a figure or an unreadable visual element.

No new P14 theorem/report dated 2026-09-18 was found that would justify repeating P13's already-completed directed P14 audits. Prior completed P14 audit work is retained rather than duplicated.

## 3. Idea before code

The previous blocker was sharper than `failed blocks are history-dependent`: a two-sided Proposition 6.5 trap attempt may have **peeked** at instructions it does not consume, so after a failure one cannot simply call the residual stacks fresh. The previous report tried to imitate Section 4 by reverse-unwinding abandoned trap plans.

B6 suggested a simpler deformation: forget the traps entirely after deciding to sacrifice an attempt. Every virtual explorer already recorded a complete lazy-walk path from the source `0` to the current barrier it first hit. Instead of replaying only to its selected trap, replay the explorers **chronologically all the way to their hit barriers**. A sleep instruction merely leaves the explorer in place; acceptable toppling lets the physical replay consume that instruction and continue. If chronological full replay works, every instruction that was ever revealed is consumed, so corruption disappears by construction.

The crucial point is that this is not just a heuristic about paths. There are two exact equalities:

1. sitewise, the replay odometer equals the virtual reveal-count vector;
2. globally, jump-flow telescopes so that replaying `q` explorers changes the particle-count vector by
   \[
   -q\delta_0+\sum_{k=1}^q\delta_{b_k},
   \]
   where `b_k` is the barrier hit by explorer `k`.

Thus the sacrificed block automatically ends with all mass at the source and hit barriers, and with no revealed instruction left unused. This is the B25 double count. B16 then stress-tests the construction on every small source-shaped transcript in a finite radius-two model.

## 4. B6 — two-sided chronological full replay

### Theorem P13-D0093-TWO-SIDED-FULL-REPLAY-FLUSH-07

Fix `r` and a finite ARW instruction field on `[-r,r]` with the usual independent stack law. Start with `m` active particles at `0` and no particles elsewhere. Run any finite prefix of the two-sided virtual exploration used in the proof of Proposition 6.5, including a prefix ending at the first failed trap search. Suppose `q<=m` explorers have been launched. For explorer `k`, let

- `E_k=((x_{k,1},I_{k,1}),...,(x_{k,tau_k},I_{k,tau_k}))` be the chronological list of site/instruction pairs it revealed;
- `b_k` be the current left or right barrier first hit by that explorer;
- `R_x` be the total number of instructions revealed at site `x` over all `q` records.

The virtual rule is only the source rule that each explorer starts at `0`, always reads the **next previously-unexplored** instruction at its present site, stays put on a sleep instruction, moves one lattice step on a jump instruction, and stops on first hitting its current barrier. The particular trap-selection rule after the path has been exposed is irrelevant to the statement.

Then there exists an acceptable toppling sequence `alpha`, contained in `[-r,r]`, obtained by replaying `E_1,E_2,...,E_q` in chronological order all the way to their hit barriers, such that

\[
\boxed{m_\alpha(x)=R_x\quad\text{for every }x.}
\tag{4.1}
\]

If `N(eta)` denotes the ordinary particle-count vector, forgetting active versus sleeping state, then the final configuration satisfies

\[
\boxed{
N(\Phi_\alpha\eta_0)
=(m-q)\delta_0+\sum_{k=1}^q\delta_{b_k}.
}
\tag{4.2}
\]

Consequently every instruction inspected by the sacrificed exploration has been consumed, every remaining stack tail is untouched, no particle has left `[-r,r]`, and the residual mass is supported only at the source and the barriers actually hit by the virtual explorers.

Moreover the reveal-count vector `R=(R_x)` is a stopping line for the independent stacks. Hence, conditional on the full explored history, the shifted tails

\[
(I_{x,R_x+1},I_{x,R_x+2},\ldots)_x
\]

are mutually independent and have the original ARW stack law.

#### Proof

We replay the explorer records one at a time.

At the start of explorer `k`, the first `k-1` records have already been fully replayed. We prove inductively that one particle is available at `0` for record `k` and that, at every step of the record, the current recorded site contains at least one particle. For `k=1` this is immediate from the initial `m` particles at `0`.

Suppose the record is currently at site `x`. If the next recorded instruction is a sleep instruction, the virtual explorer stays at `x`. In the physical configuration, if there is more than one active particle at `x`, the sleep attempt has no effect. If there is exactly one active particle, it becomes a sleeper. If there is already one sleeper, the source's acceptable-toppling convention permits us to force it active and topple it; a sleep instruction leaves it sleeping. In every case at least one particle remains at `x`, so the next recorded instruction at that same site can be consumed acceptably.

If the next recorded instruction is a jump from `x` to the neighboring site `y`, an acceptable toppling removes one particle from `x` and puts one active particle at `y` (waking a sleeper there if one was present). Therefore the next recorded site, which is exactly `y`, contains a particle. We continue until the jump that first reaches the recorded barrier `b_k`; the virtual record stops there, so no instruction at the barrier need be consumed merely to terminate the replay.

It remains to check that the instruction indices line up. Before record `k` was created, the virtual exploration skipped every instruction already revealed by records `1,...,k-1` and read the next unexplored instruction. By the induction hypothesis, full replay of those previous records has consumed **exactly** all of those previously revealed instructions. Therefore the next instruction required by record `k` is physically the next unconsumed stack entry at every visited site. Thus every step above uses the correct instruction. Summing over records proves (4.1).

For the particle-count identity, ignore active/sleeping labels. A sleep instruction changes no particle count. A jump instruction from `x` to `y` changes the count vector by `-delta_x+delta_y`. Along explorer `k`, the jump edges form a nearest-neighbor path starting at `0` and ending at `b_k`; all intermediate increments telescope, so the net count change for that whole record is

\[
-\delta_0+\delta_{b_k}.
\]

Adding the `q` records to the initial vector `m delta_0` gives (4.2). In particular, after the first `k-1` records there are exactly `m-k+1` particles at `0`, validating the availability claim used by the induction.

Finally, the virtual reveal algorithm is adaptive but online with respect to **revealed** instructions: the decision whether and where to reveal the next instruction and whether the prefix has stopped is determined entirely by the entries already revealed. Therefore, for every deterministic vector `r=(r_x)`, the event `{R=r}` is measurable with respect to the sigma-field generated by the first `r_x` stack entries at each site. This is precisely the stopping-line condition proved sufficient in Lemma P13-D0093-STOPPING-LINE-FRESH-TAILS-04 of the preceding report. Applying that lemma at `R` proves conditional freshness and independence of the unused tails. `square`

### Why this is stronger than the previous unwind formulation

The proof does not require reverse processing, side-by-side disjointness of corrupted slabs, or any special ordering of left and right trap placements. It uses only the chronological virtual records and the source's `next unexplored instruction` rule. It therefore applies verbatim to the two-sided Proposition 6.5 exploration, including the first explorer on which the trap search fails.

This is the main successful port of the recovery episode: the **fresh-tail part of the two-sided clean-attempt/flush interface is now proved**, not conjectured.

## 5. Quantitative work tail for the clean flush

The previous stuck report also required the flush not to cost more than the natural `O(r^3)` scale. The same replay gives this without an additional construction.

### Theorem P13-D0093-FULL-REPLAY-WORK-TAIL-08

Fix `lambda<infinity` and `zeta_1>0`. In the setting of Theorem 07, assume

\[
m\le 2\zeta_1 r.
\]

There exist constants `K<infinity` and `c>0`, depending only on `lambda,zeta_1`, such that for every `r>=1`, the total number

\[
W:=\sum_x R_x=\sum_{k=1}^q\tau_k
\]

of instructions revealed, hence also the number of acceptable topplings in the full replay, obeys

\[
\boxed{\mathbb P(W>K r^3)\le e^{-cr}.}
\tag{5.1}
\]

The estimate holds conditionally on any pre-attempt history for which the unused instruction tails at the start of the attempt are fresh.

#### Proof

Condition on the history before explorer `k` begins. If it is launched, its current left and right barriers are `a<0<b` with `b-a<=2r`. Because it always takes the next previously-unexplored instruction, its position evolves as a lazy symmetric walk until hitting `{a,b}`: at each revealed instruction it stays in place with probability

\[
s=\frac{\lambda}{1+\lambda}
\]

and jumps left or right with probability `1/(2(1+lambda))` each.

For the embedded non-lazy simple random walk, the expected number of jumps to hit `{a,b}` from a site `z` is `(z-a)(b-z)`, at most `(b-a)^2/4<=r^2`. One jump occurs after a geometric number of revealed instructions of mean `1+lambda`. Hence from **every** current interior position the expected remaining number of revealed instructions is at most

\[
\mu:=(1+\lambda)r^2.
\]

Markov's inequality gives probability at most `1/2` of surviving another `2 mu` revealed instructions. Reapply this after each such block using the strong Markov property and fresh unused stack entries. Thus, with `X=tau_k/r^2` and

\[
A:=2(1+\lambda),
\]

we have uniformly in the past

\[
\mathbb P(X>A j\mid\text{past})\le2^{-j},\qquad j=0,1,2,\ldots.
\tag{5.2}
\]

Choose

\[
\theta:=\frac{\log2}{4(1+\lambda)},
\qquad e^{\theta A}=\sqrt2.
\]

Partitioning according to the intervals `(Aj,A(j+1)]` and using (5.2),

\[
\mathbb E[e^{\theta X}\mid\text{past}]
\le \frac{e^{\theta A}}{1-e^{\theta A}/2}
=:C_0
=2(1+\sqrt2).
\tag{5.3}
\]

If the exploration has already stopped, set later `tau_k=0`; (5.3) remains true. Iterating conditional expectations through at most `m` explorers yields

\[
\mathbb E\exp\left(\theta\frac{W}{r^2}\right)
\le C_0^m
\le \exp\bigl(2\zeta_1 r\log C_0\bigr).
\]

Therefore for any

\[
K>\frac{2\zeta_1\log C_0}{\theta}
\]

Chernoff's inequality gives

\[
\mathbb P(W>K r^3)
\le\exp\left[-\bigl(\theta K-2\zeta_1\log C_0\bigr)r\right].
\]

Taking `c=theta K-2 zeta_1 log C_0>0` proves (5.1). `square`

### Consequence

A failed Proposition-6.5-style attempt can now be treated as follows: expose the attempt exactly as in the source; if it is to be sacrificed, full-replay every exposed explorer to its hit barrier. With exponentially high probability the cleanup costs only `O(r^3)` topplings, all peeks become consumed history, no particle exits the interval, the particle count is concentrated on the source plus hit barriers, and all stack tails after the consumed odometer are fresh.

This discharges the exact single-block `failure -> clean state + fresh tails + O(r^3) work` obligation that triggered STUCK RECOVERY 1.

## 6. B25 — count the same process twice: reveal odometer and mass flux

Theorem 07 contains two distinct double counts, both useful for the next stage.

First,

\[
\boxed{\text{reveal count at }x=R_x=m_\alpha(x)=\text{physical replay topplings at }x.}
\]

The virtual algorithm's information boundary is therefore exactly the physical odometer boundary after full replay. There is no hidden class of `examined but not consumed` instructions after cleanup.

Second, write `J_k` for the oriented jump edges in explorer record `k`. Counting mass change instruction-by-instruction gives

\[
N_{\rm out}-N_{\rm in}
=\sum_{k=1}^q\sum_{(x\to y)\in J_k}(-\delta_x+\delta_y).
\]

Counting the same edges as paths makes every interior vertex cancel, leaving

\[
\boxed{N_{\rm out}-N_{\rm in}
=\sum_{k=1}^q(-\delta_0+\delta_{b_k}).}
\]

This identifies the exact residual object after a failure: **clean boundary flux**, not a mysterious history-dependent configuration.

For the simplest two-adjacent-block case from the previous stuck report, sacrificing and chronologically replaying both plans therefore produces, block by block, a state with

- no revealed-but-unused instructions;
- fresh independent shifted stack tails;
- no particle outside the two original intervals due to the replay itself;
- all mass at the two sources and the barrier sites hit by the sacrificed explorers;
- an `O(r^3)` exponential-tail cleanup budget per block.

So the previous two-block *freshness* obstruction is gone. What remains is a genuinely different gluing question: how to turn these **clean but distributed barrier loads** into the centered source piles required by the next Proposition 6.5 application, without making a successful neighboring block absorb uncontrolled incoming particles or paying a global diffusive cost.

I tested the most obvious immediate restart and it fails for a structural reason. A particle sitting at an outer hit barrier can be moved by acceptable topplings until it next reaches a source, and the shifted tails stay fresh because this routing is online. But the first source it reaches can be the neighboring source on the *outside* of the repair cluster. Thus a local failure naturally exports random mass across the cluster boundary. Forcing all such particles to one prescribed repair source would require controlling random-walk direction, which acceptable topplings alone do not provide. The clean-flush theorem therefore converts the blocker from `biased stack tails` into a source-lattice **stochastic boundary-flow/gluing** problem; it does not solve that flow problem by sleight of hand.

This is a useful failure: the next proof must control exported clean mass, not invent a static capacity or pretend routing direction is deterministic.

## 7. B16 — exhaustive small source-shaped histories

Only after the replay theorem was written did I build a finite exact self-check. It is deliberately bounded and is labelled a **self-check**, not an outside audit or a proof of Proposition 6.5.

The checker uses radius `r=2`, two source particles, at most six revealed instructions per explorer, and exhausts all

\[
3^{10}=59049
\]

global instruction-choice streams over `{L,R,S}`. It implements the structural source rules needed here: next-unexplored site instruction, sleep-as-hold, nearest-neighbor jumps, first-hit stopping at the current barrier, and a source-shaped inward trap update. It then performs the physical ARW replay with the exact acceptable-toppling sleep convention and checks both equalities of Section 6.

Executed output:

```text
radius=2
particles=2
max_steps_per_explorer=6
global_choice_length=10
choice_strings=59049
completed_choice_strings=38346
timeout_choice_strings=19999
insufficient_choice_strings=704
distinct_completed_histories=1106
replay_failures=0
PASS: every completed source-shaped history has acceptable chronological full replay, consumed_count == revealed_count sitewise, and the exact source-to-hit-barrier mass-transport identity.
```

Artifacts:

- `proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T05-02-46Z__d0093_two_sided_full_replay_check.py`
- `proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T05-02-46Z__d0093_two_sided_full_replay_check.out`

The script was created at commit `8d10659ccc0f1afe2addb22eb2303d35bedf4cce` and read back there; its blob is `ec0d05ad1b45971e95d26bd913702016917fe733`. The archived output was created at `1cbf97d506cf111f0f4b65cb70a399d29ac069c9` and read back there; its blob is `5ff697bfe83382b84ed680e5a76bb58908a65634`.

The enumeration is not extrapolated to an infinite or universal claim. The theorem is supplied by the analytic induction; the enumeration only stress-tests the finite mechanics and caught no counterexample.

## 8. What each method accomplished

### B6 — DEFORM TO A POINT YOU CAN SOLVE

I deformed the source's partial replay-to-trap procedure into the more wasteful `sacrifice everything and replay the complete virtual path` procedure. That deformation **worked**: the two-sided corruption/freshness obstruction disappears exactly, and the natural `O(r^3)` work tail can be proved.

### B16 — COMPUTE EVERY SMALL CASE

I exhaustively enumerated a bounded source-shaped radius-two model after the theorem was formulated. Among 1,106 distinct completed histories there were zero replay/odometer/mass-transport failures. This **worked as a self-check** but earns no source-metric credit and is not used as evidence beyond its finite scope.

### B25 — COUNT THE SAME THING TWICE

I counted the exploration once as information (`R_x`) and once as physical odometer (`m_alpha(x)`), obtaining exact equality, then counted jump flow once instruction-by-instruction and once as path divergence, obtaining the source-to-hit-barrier mass identity. This **worked** and is the reason the failed state is now a clean flux object rather than an arbitrary distributed history.

## 9. Updated stuck diagnosis

The no-movement counter is now four, so the CLOSABLE six-run rotation clock continues. The selected recovery episode made genuine auxiliary progress but did not move `beta_fast`.

### Old exact blocker — now discharged locally

The previous report required a two-sided clean attempt/flush interface that consumes peeks, stays inside the block, has `O(r^3)` work with exponential tail, and restores fresh unused tails. Theorems 07--08 supply that interface for any finite prefix of the source two-sided exploration, including a first failed trap search.

### New exact blocker

After a sacrificed failure, the mass is clean but can sit on **both left and right hit barriers**. To resume the fixed-scale or multiscale program one must prove a source-valid stochastic gluing theorem of the following type:

> Starting from a collection of adjacent clean failed blocks whose particles lie only at their sources and hit barriers, use fresh tails and acceptable topplings to redistribute/absorb the exported barrier mass so that subsequent local attempts again satisfy a centered-load condition with density strictly below `lambda/(1+lambda)`, while preserving an exponentially decaying repair-cluster law and an aggregate `O(n)` work budget.

The immediate deterministic one-way Lindley recursion remains invalid because a barrier particle cannot be commanded to choose a prescribed neighboring source; its source-to-source routing direction is random. Conversely, the old objection `the routing has biased the trap stacks` is no longer valid after the clean flush, because the post-flush tails are a genuine stopping line.

### Simplest remaining case

Take two adjacent source intervals at fixed scale `r`, each initially loaded below a stricter threshold `2 zeta_1 r`, where

\[
\zeta<\zeta_1<\zeta_2<\frac{\lambda}{1+\lambda}.
\]

Sacrifice both local plans and apply full replay. The remaining finite problem is to route the resulting source/barrier mass using fresh tails so that either

1. both source loads become at most `2 zeta_2 r` and can be retried independently, or
2. any excess is represented as explicit clean outward flux to a neighboring repair block,

with an exponential tail uniform over every input satisfying the `zeta_1` load cap. This is now the smallest source-relevant gluing case; there is no longer any peeking/freshness ambiguity inside it.

### Next methods

If D0093 remains active next run, the next nonrepeating triple is **B1** (change category: cleaned failures as a random source-lattice flow network), **B9** (randomize the coarser source offset to reduce adversarial alignment of barrier mass), and **B27** (swap quantifiers: seek one routing/offset rule that handles every load vector satisfying a strict aggregate-slack condition). Any route that silently assumes a barrier particle can be sent in a prescribed direction is rejected at formulation time.

## 10. Closure/audit status

D0093 remains **OPEN / PARTIAL**. No source-domain exponent below 2 has been proved. There is no paper package and no closure request. A future closure would still require the exact finite-cycle Poisson order-`n` argument, a bounded-prior-art review with its limitations made explicit, a P26 end-to-end audit, and a second distinct OTHER-track end-to-end audit.

The finite enumeration above is a self-check only. No audit vote was fabricated. No claim of worldwide openness or publication novelty is made from the bounded literature search.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  root: proofnet24/P13-outside-successor
  category: CLOSABLE_OUTSIDE
  target: D0093
  canonical_claim: operations/claims/D0093.md
  source: Rolla_2020_Activated_Random_Walks_on_Zd
  locator: Section_6_2_second_open_problem_after_Theorem_6_1_equation_6_3
  metric: beta_fast
  metric_domain: exact_source_finite_cycle_iid_Poisson_symmetric_fast_regime
  value_before: 2
  value_after: 2
  movement: false
  unchanged_runs_before: 3
  unchanged_runs_after: 4
  status: OPEN_PARTIAL_STUCK_RECOVERY_1
  methods:
    - B6_DEFORM_TO_A_POINT_YOU_CAN_SOLVE
    - B16_COMPUTE_EVERY_SMALL_CASE
    - B25_COUNT_THE_SAME_THING_TWICE
  selected_recovery: PORT_THE_ANALOGOUS_TECHNIQUE
  recovery_progress:
    old_blocker: two_sided_failed_attempt_peeks_prevent_fresh_retry
    old_blocker_status: DISCHARGED_FOR_SINGLE_BLOCK_BY_FULL_REPLAY
    new_claims:
      - P13-D0093-TWO-SIDED-FULL-REPLAY-FLUSH-07
      - P13-D0093-FULL-REPLAY-WORK-TAIL-08
    exact_finite_self_check: PASS_1106_distinct_completed_histories
  residual_blocker: clean_distributed_barrier_flux_to_centered_source_load_gluing
  simplest_remaining_case: two_adjacent_blocks_with_zeta1_to_zeta2_slack
  literature_screen_date: 2026-09-18
  literature_screen_result: bounded_no_source_matching_linear_cycle_Poisson_theorem_found
  pdf_visual_access: FAILED_CACHE_MISS_screenshots_requested_for_source_pages
  p14_directed_audit: no_new_2026_09_18_P14_theorem_found_previous_audits_retained
  closure_authorized: false
  source_metric_claim: no_change
  retired_targets_reopened: false
```

No shared root ledger, peer file, historical report, canonical ownership file, schedule, workflow, public post, email/Gmail item, Drive item, credential, permission, or retired target was modified.
