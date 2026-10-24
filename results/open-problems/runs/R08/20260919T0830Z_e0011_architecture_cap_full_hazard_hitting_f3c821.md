Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b17_rob -> B_cat >= b17_rob`, with `log10(b17_rob) ~= -50.09882171767006`; unchanged count `0 -> 1`. Methods actually used: #2 ATTACK THE NEGATION FIRST, #10 DERANDOMIZE, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R08 CLOSABLE OUTSIDE — exact architecture cap and the full-hazard robust-hitting route

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / OPEN_CURRENT_BOUNDED**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and fresh source checks

I continued from

`runs/R08/20260919T0736Z_e0011_adversarial_boundary_b17rob_a61d4c.md`

and did not restart from the stale native title. The controlling current exclusive claim is `operations/claims/E0011.md`. It records that the predecessor Hasebe--Ueda Problem 3.11 / `I0082` is **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. The older `operations/claims/I0082.md` remains part of history, but the later E0011 claim and R08 handoff govern this slot. The old R08 FPP strict-convexity route also remains retired.

At run start I reread/refreshed campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the owner directive and `operations/NEW_METHODS_2026-09-16.md`, the I0082/E0011 claim files, the latest R08 report and exact artifacts, and current neighboring R07/R09 status. E0011 remains exclusively owned by R08; the newest visible R07 work is on a different periodic-boundary target and R09 is in successor admission, with no E0011 conflict.

Fresh current-literature checks on 2026-09-19 found:

- Hasebe--Ueda's ALEA source still states Problem 3.11 exactly as the existence question for a non-delta freely strongly unimodal law. A September 7, 2026 unrefereed candidate on **symmetric** unimodality under free additive convolution explicitly says that free strong unimodality is not established; it therefore does not resolve I0082 and does not reopen the retired predecessor.
- Durrett's 2009 source, arXiv:0906.2293 / Ann. Appl. Probab. 19 (2009), remains the source for E0011. A current Durrett slide deck still literally says `Problem 5: Prove coexistence.`
- Recent ZGB papers found in the bounded search are modified models: e.g. Fernandes--da Silva (Phys. Rev. E 111, 044101, 2025) allows CO desorption, and de Andrade--Girardi (Phys. Rev. E 114, 024136, published 18 August 2026) adds reactive sulfur. I found no later primary theorem in this bounded search settling the exact original no-stirring source target. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

All thirty Section-B methods had already appeared at least once on E0011 before the previous cycle, so the established R08 method catalog may restart; this run does not repeat the immediately preceding `B11/B19/B27` triple.

## 2. B2 — attack the current architecture, not another terminal constant

The sound `b17_rob` certificate has the form

\[
 b_{17,\rm rob}=K_{\rm up}\,p_{\rm rob},
\]

where `p_rob` is the new adversarial-boundary terminal factor and `K_up` is the product of every already-certified upstream bootstrap, corridor, guard, and planter factor. I reconstructed `K_up` from the exact factors in the sound `b14` metric checker, **without** using the withdrawn `b15/b16` halo increments.

The exact rational is archived in the checker. Numerically only for scale,

\[
\boxed{K_{\rm up}\approx 3.514426670110799\times10^{-46}},
\qquad
\boxed{\log_{10}K_{\rm up}\approx-45.45414551397732}.
\tag{2.1}
\]

This yields a rigorous restricted obstruction:

> **Fixed-upstream architecture cap.** Keep every upstream event in the present `L=8` certificate unchanged, but replace the entire terminal stage by an arbitrary event of probability at most one. Then the resulting block probability is at most `K_up < 4*10^-46`.

The proof is one line: the upstream event has probability `K_up`, and intersecting it with any terminal event has probability at most `K_up`. No independence assumption is needed for this upper bound.

Consequently **no terminal-only improvement of the present architecture can possibly reach `63/64`**. Even a magical terminal stage that succeeds with probability one leaves a gap of approximately

\[
\log_{10}\frac{63/64}{K_{\rm up}}\approx45.44730608944701
\]

decimal orders. This is not an upper bound on `B_cat`; it is an exact obstruction only for the subfamily that freezes the current upstream rare-cylinder factors.

This result changes the research allocation: further terminal-alphabet or terminal-window tuning is no longer a plausible closure route.

## 3. B21 — the eight-arrival truncation is already saturated in the current killed event

Before abandoning the current Bellman terminal event I also checked whether the proposed infinite-horizon continuation could hide a large amount of mass.

The 17 accepted terminal clocks have exact reaction-weight total

\[
8\cdot72+9\cdot36=900,
\]

inside the owned hazard

\[
36\cdot214=7704.
\]

Hence the accepted fraction is

\[
\boxed{a=\frac{900}{7704}=\frac{25}{214}}.
\]

At the current rational Poisson mean `lambda=429/200`, the effective accepted-arrival mean is

\[
\boxed{x=a\lambda=\frac{429}{1712}\approx0.2505841121}.
\]

The preceding certificate sums all accepted histories through `n=8`. Even under the impossible optimistic assumption that **every** accepted history of length `n>=9` succeeds, its omitted polynomial mass is at most

\[
R_9:=\sum_{n\ge9}\frac{x^n}{n!}
<\frac{x^9/9!}{1-x/10}
=
\frac{6076179719018640351549}
{551811127381208040112134425673728}.
\tag{3.1}
\]

The inequality uses `t_{n+1}/t_n=x/(n+1)<=x/10` for `n>=9`. Exact arithmetic gives

\[
\boxed{R_9<\frac1{90,000,000,000}},
\qquad
R_9\approx1.10113\times10^{-11}.
\tag{3.2}
\]

The sound robust terminal factor is `p_rob≈2.26633*10^-5`, so

\[
\boxed{\frac{R_9}{p_{\rm rob}}<\frac1{2,050,000}}
\tag{3.3}
\]

(the displayed bound is conservative because it even omits the global `e^{-lambda}` factor). Thus extending **this same suppress-all-other-owned-clocks terminal event** from eight arrivals to infinitely many can improve its terminal factor by less than about five parts in ten million. It cannot change scale.

So the earlier idea “use an infinite-horizon solver on the existing killed alphabet” is now retired. The infinite-horizon machinery is useful only if we first stop killing ordinary owned Harris marks.

## 4. B10 — why terminal derandomization is the wrong place to derandomize

The preceding exact Bellman output has `MINS[2]=4320`. Since the total accepted branch weight is 900 per accepted mark, every generated-shield entrance descriptor has, conditionally on two accepted marks in the present robust game, success probability at least

\[
\boxed{\frac{4320}{900^2}=\frac2{375}}.
\tag{4.1}
\]

This is a useful reachability diagnostic: the six-vacancy target is uniformly reachable in only two accepted steps from the entrance class. But it is **not** yet an amplifiable regeneration theorem, because after a failed two-step attempt the projected core state need not return to the entrance class.

I tried the B10 interpretation “extract a compact deterministic robust terminal word/policy from the Bellman mass.” It fails as a closure route for two independent reasons:

1. a deterministic terminal word throws away the all-history mass that the Bellman recursion recovered; the earlier `L=7` robust 21-mark word demonstrated how severe that loss can be;
2. much more decisively, Section 2 proves that **even a perfect deterministic terminal policy with probability one cannot overcome the fixed upstream cap**.

So the useful derandomization target is not a successful terminal word. It is the *adversary*: after constructing the full-hazard lower transition operator, extract the finite set of extremal boundary rows / worst states that attain its minima. That can turn a large robust stochastic calculation into a small symbolic obstruction or minorization proof.

## 5. B21 — the matching external machinery: imprecise Markov-chain hitting probabilities

The previous Bellman recursion has exactly the shape studied in the imprecise-Markov-chain literature: each protected core state has a family of transition rows induced by legal exterior boundary states, and the exterior can choose the hostile row state by state.

A particularly direct current reference is:

- Marco Sangalli, Rick M. H. J. Reubsaet, Erik Quaeghebeur and Thomas E. Krak, **“Computing lower and upper hitting probabilities for imprecise Markov chains,”** *International Journal of Approximate Reasoning* 194 (July 2026), 109671, DOI `10.1016/j.ijar.2026.109671`. The paper characterizes lower hitting probabilities by nonlinear fixed-point equations and gives computational algorithms based on extreme transition matrices.
- Sangalli--Quaeghebeur--Krak, **“Relation between Hitting Times and Probabilities for Imprecise Markov Chains,”** arXiv:2603.16675 (17 March 2026), treats compact convex transition sets with separately specified rows and relates lower hitting probability one to finite upper expected hitting time.
- Krak--De Bock--Siebes, **“Imprecise Continuous-Time Markov Chains,”** *IJAR* 88 (2017), 452--528, develops the lower-transition-operator formalism in continuous time.

This is not being cited as a solution to E0011. It identifies the right computational category for the exterior-adversarial local dynamics.

### Robust finite-horizon minorization lemma

Here is the exact theorem the next construction should try to satisfy.

Let `S` be a finite state set, `A subset S` the regeneration target, and for each `s notin A` let `P(s)` be a nonempty finite (or compact) set of admissible one-step transition rows. An adversary may select a row from `P(s)` after seeing the current state and all past history. Keep `A` absorbing for the hitting calculation and define

\[
h_0=\mathbf 1_A,
\]

and, for `n>=0`,

\[
h_{n+1}(s)=
\begin{cases}
1,&s\in A,\\
\inf_{p\in P(s)}\sum_{y\in S}p(y)h_n(y),&s\notin A.
\end{cases}
\tag{5.1}
\]

**Claim.** `h_n(s)` is exactly the worst-adversary probability of hitting `A` within `n` steps. If for some `m` there is an `eta>0` such that

\[
\eta:=\min_{s\in S}h_m(s)>0,
\tag{5.2}
\]

then uniformly over every adaptive exterior strategy,

\[
\Pr_s(\tau_A>jm)\le(1-\eta)^j,
\qquad
\Pr_s(\tau_A\le jm)\ge1-(1-\eta)^j.
\tag{5.3}
\]

**Proof.** The first statement is induction on `n`. At the first step the adversary chooses a row `p in P(s)`; after the realized next state `y`, its optimal continuation has value `h_n(y)` by the induction hypothesis. Taking the infimum over the first row gives (5.1). For (5.3), condition at each time `km` on the event that `A` has not yet been hit. The current state still lies in `S`, so (5.2) gives conditional failure probability at most `1-eta` during the next `m` steps, regardless of the past or the future adaptive choices. Iterating the conditional inequality gives `(1-eta)^j`. QED.

This lemma is elementary; the external IMC papers supply the larger fixed-point/algorithmic framework. Its significance here is scale: **a full-hazard closed state set with any certified uniform `eta>0` can be amplified arbitrarily close to one without multiplying nine unrelated rare-cylinder probabilities.** That is the first route in this R08 sequence that can plausibly bridge dozens of decimal orders rather than improve a constant.

## 6. The exact next finite problem

The next object is no longer the 17-label killed terminal chain. Build the finite protected-core state graph under **all owned Harris clocks that can affect the core**, with the four halo coordinates treated as adversarially refreshed boundary variables exactly as in `b17_rob`.

Then do one of two things:

1. **positive route:** find a closed safe set `S` containing every generated-shield entrance state and an `m` for which the exact lower recursion (5.1) has `eta=min_S h_m>0`; then (5.3) gives a near-one regeneration event after finitely many blocks of `m` transitions;
2. **negative route:** exhibit an exact adversarial trap/recurrent class disjoint from the target. That proves this seed/core architecture cannot have uniform lower hitting probability one and forces a seed redesign rather than more probability tuning.

The current `2/375` two-accepted-mark floor is **not** yet enough for route (1), precisely because closure of the entrance class after failure is unproved. This is the cleanest remaining finite obligation.

## 7. What each method did

**B2 ATTACK THE NEGATION FIRST — succeeded.** The exact `K_up` calculation proves a strong restricted negative result: terminal-only optimization of the current fixed-upstream construction can never close the source.

**B10 DERANDOMIZE — failed in its naive terminal form, and redirected.** Extracting a deterministic terminal word cannot beat the architecture cap. The useful deterministic extraction will be the extremal hostile rows/trap states of the full-hazard lower operator.

**B21 ASK WHO ELSE HAS THIS SHAPE — succeeded.** The exterior-refresh Bellman problem is a separately-specified-row imprecise Markov hitting problem. Recent 2026 work gives exactly the nonlinear fixed-point/hitting framework needed; the route must be applied to the full hazard, not the already saturated killed alphabet.

## 8. Exact self-check

Idea-before-code note:

`artifacts/R08/20260919T0830Z_e0011_full_hazard_hitting_idea.md`

Executed exact-arithmetic checker/output:

`artifacts/R08/20260919T0830Z_e0011_architecture_cap_check.py`  
`artifacts/R08/20260919T0830Z_e0011_architecture_cap_check.out`

The output reports `PASS exact R08/E0011 architecture-cap and tail certificate` and checks:

- the exact upstream product and `K_up<4*10^-46`;
- the sound `b17_rob` scale;
- accepted fraction `25/214` and effective mean `429/1712`;
- the exact `n>=9` tail bound and its ratio to `p_rob`;
- the `2/375` robust two-accepted-mark reachability floor.

This is a **self-check**, not an independent OTHER-track audit. No audit credit is claimed.

## 9. Status, stuck counter, and next methods

The frozen metric does **not** move this run:

\[
\boxed{B_{\rm cat}\ge b_{17,\rm rob}\quad\text{before and after}.}
\]

The unchanged count is therefore `0 -> 1`. This is not yet a Section-I stuck run. The substantive gain is an exact route-killing theorem plus a replacement route capable in principle of changing scale.

All thirty methods were previously exhausted once on E0011, so the catalog is already in its permitted restart cycle. Do not repeat `B2/B10/B21` next. The next triple is **B3 / B6 / B24**:

- **B3 PROVE SOMETHING STRONGER:** seek the uniform full-hazard minorization (5.2) on a closed safe set, which is stronger than a one-shot block lower bound but self-amplifies once proved;
- **B6 DEFORM TO A POINT YOU CAN SOLVE:** compute the lower hitting operator first with frozen-empty exterior, then add adversarial halo freedoms one coordinate at a time and identify the first deformation at which `eta` collapses;
- **B24 FIND THE EXTREMAL OBJECT:** extract the exact worst core state and extremal boundary row. If they form a target-avoiding recurrent class, certify the obstruction; if not, they should reveal the smallest state set on which a positive minorization can be proved.

## 10. Model / scheduler-control status

The requested GPT-6/maximum setting is still **not bindable through the exposed scheduler interface**. The update surface available to this worker exposes prompt/title, schedule or relative start, enabled state, and timing mode; it exposes no model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model/effort telemetry. Therefore GPT-6/maximum remains prompt text only, and this report truthfully records GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository now records that the historical P26 `You cannot modify this task` response was context-specific: a later full P26 prompt update succeeded from an authorized context. For any task that still rejects modification, the legitimate workaround is its authorized owning context, a supported ownership/admin transfer, or platform support. There is no repository-side bypass. In accordance with the current owner directive, **no scheduler modification was attempted this run**.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  lane: CLOSABLE_OUTSIDE
  active_claim: E0011
  source: "Durrett 2009 Problem 5 — original no-stirring catalyst/ZGB coexistence"
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric_name: B_cat
  sound_before: ">= b17_rob; log10 ~= -50.09882171767006"
  sound_after: ">= b17_rob; log10 ~= -50.09882171767006"
  movement: "NO"
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: PARTIAL
  restricted_obstruction: "with all present upstream factors frozen, even a probability-one terminal stage leaves the block probability K_up < 4e-46"
  killed_terminal_saturation: "at lambda=429/200, the complete omitted n>=9 accepted-history tail is <1/90,000,000,000 and <p_rob/2,050,000"
  new_route: "full-hazard separately-specified-row lower hitting operator; seek a closed safe set with uniform finite-horizon minorization eta>0 or certify an adversarial target-avoiding recurrent class"
  artifacts:
    - "artifacts/R08/20260919T0830Z_e0011_full_hazard_hitting_idea.md"
    - "artifacts/R08/20260919T0830Z_e0011_architecture_cap_check.py"
    - "artifacts/R08/20260919T0830Z_e0011_architecture_cap_check.out"
  self_check_only: true
  independent_audits_new: 0
  shared_root_modified: false
  next_methods: [3, 6, 24]
```
