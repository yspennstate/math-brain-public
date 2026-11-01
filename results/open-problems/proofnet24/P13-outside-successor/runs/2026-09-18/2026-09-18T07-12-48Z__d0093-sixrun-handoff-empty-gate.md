Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime does not authenticate GPT-6 or a maximum-reasoning selector, so I do not claim that configuration. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `5 -> 6`; methods actually tried: B4 PROVE SOMETHING WEAKER COMPLETELY, B16 COMPUTE EVERY SMALL CASE, B30 ONE SCALE / ONE DIRECTION AT A TIME. SIX-RUN CLOSABLE HANDOFF IS NOW MANDATORY.**

# P13 — D0093 sixth research run and mandatory handoff: exact empty-corridor transfer, a reactivation counterexample, and the cyclic direction-bias obstruction

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, second Open Problem after Theorem 6.1 / (6.3).  
Status after this run: **OPEN / PARTIAL / SIX-RUN HANDOFF / SUCCESSOR ADMISSION_PENDING**.

## 1. Continuity, source, ownership, and frozen metric

The former P13 I0051 Aldous--Janson Open Problem 9 clade-covariance project remains **RETIRED** and was not reopened. P0082 remains handed off after its own six-run CLOSABLE rotation and was not reopened. The active P13 source entering this invocation was D0093, whose canonical claim still identifies this native slot and whose source-faithful frozen metric is

\[
\beta_{\rm fast}:=\inf\left\{\beta\ge0:\exists\kappa<\infty,\delta>0,\ 
\mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)\ge1-n^{-\delta}
\text{ for all sufficiently large }n\right\}
\]

under the exact source finite cycle, i.i.d.-Poisson initial law, symmetric nearest-neighbor walks, and the fast-regime parameter domain of (6.3).

The controlling predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T06-07-09Z__d0093-periodic-regenerative-queue.md`.

That report left the source metric at `beta_fast=2`, giving five consecutive unchanged D0093 runs. It proved an auxiliary periodic negative-drift queue theorem in which the sum of cubic busy-cell lengths is `O(n)` with polynomially high probability, but it isolated one source-native realization problem (`REG-CELL`) and explicitly stated that **one further unchanged source-metric run would force handoff rather than a seventh D0093 research run**.

Rolla's source was rechecked directly. Section 6.2 fixes the ring `Z_n`, fair nearest-neighbor jumps, i.i.d. Poisson initial counts of mean `zeta`, and total number `T` of topplings. Theorem 6.1 gives

\[
\mathbb P(T\le \kappa n\log^2 n)\ge1-n^{-\delta},
\]

and the next Open Problem asks to improve (6.3) to one **without the `log^2 n` term**. The proof chooses

\[
p:=\frac{\lambda}{1+\lambda}>\zeta'>\zeta,
\qquad r=\lfloor K\log n\rfloor,
\]

routes particles to sources by acceptable topplings, and applies Proposition 6.5, which confines at most `2 zeta' r` particles started at one source with failure probability `e^{-cr}`. The global union bound over the order-`n/r` source blocks is exactly where the deterministic logarithmic block scale enters; the source then pays diffusive `r^2` work.

A fresh bounded literature check dated 2026-09-18 again recovered the original cycle theorem of Basu--Ganguly--Hoffman--Richey, whose abstract describes the fast behavior as linear only up to polylogarithmic factors; Johnson--Richey (2025), which proves stretched-exponential subcritical one-site odometer tails on `Z` for i.i.d. **Bernoulli** initial data; and de Lima--Rolla--Terra (published online 17 April 2026), which treats the opposite slow/high-density finite-ring phase. No checked primary source in this bounded search states the exact finite-cycle i.i.d.-Poisson order-`n` estimate asked by D0093. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

The arXiv PDF text was readable. Required screenshot attempts on the Section 6 pages failed again with a cache-miss error; I record `PDF_VISUAL_ACCESS_FAILURE`. No argument below depends on a figure.

The intake history `probability_1000_intake_D_20260908/batches/b08.json` was also reread. Its old D0093 attempt identifies the odometer-tail issue but predates Johnson--Richey and does not contain the regenerative-cell route developed here. Missing values were not reset.

Because the theorem proved below is only a local source-stack interface and does not produce an exact finite-cycle bound with exponent below `2`, the frozen metric remains

\[
\boxed{\beta_{\rm fast}:2\to2}.
\]

This is the **sixth** consecutive unchanged source-metric run. The owner rule therefore forces D0093 handoff/rotation at the end of this report.

## 2. Idea before code

The previous run's `REG-CELL` blocker was deliberately reduced to its smallest useful piece: one unit of overflow crossing one interface between two clean cells, with fresh stack tails. Before attempting a large two-sided cell construction, B4 asks whether this one-particle interface is itself genuinely difficult.

It is not, provided the corridor is empty. Acceptable topplings turn the ARW instruction sequence for a single carrier into a lazy symmetric walk; after ignoring sleep holds, the jump skeleton is ordinary gambler's ruin. This gives an exact, composable transfer kernel with a stopping-line fresh-tail property.

But that kernel exposes two separate obstructions to a full source proof:

1. **occupied-background reactivation:** if the carrier encounters an existing sleeper, `A+S -> 2A`, so a one-particle transfer can leave an active particle behind; the scalar queue state is then false;
2. **cyclic directional geometry:** to imitate a one-sided queue one may try to bias each symmetric carrier toward a chosen neighboring source by making the opposite buffer longer. The exact gambler's-ruin formula shows how much geometry is required. On a cycle, however, every source cannot simultaneously have its counter-clockwise gap larger than its clockwise gap by the fixed ratio needed when `zeta` is close to `p=lambda/(1+lambda)`. Multiplying the inequalities around the cycle gives a contradiction.

This explains, in exact finite geometry, why the source itself needs a genuinely **two-sided** Proposition-6.5 urn argument for arbitrary `zeta<1`: the easy one-sided reduction works only when the available service can afford the factor `1/2` from symmetry.

Only after the mathematical statement was fixed did I execute the B16 exact checker.

## 3. B4 — an exact empty-corridor transfer theorem

### Theorem P13-D0093-EMPTY-GATE-11

Fix integers `a,b>=1`. Consider symmetric nearest-neighbor ARW instruction stacks on the finite interval

\[
[-a,b]\cap\mathbb Z,
\]

with fresh unused tails. Put one active particle at `0` and no other particles at the interior sites. Repeatedly use **acceptable** topplings at the carrier's current site until the carrier first reaches either `-a` or `b`. A sleep instruction leaves the carrier in place; if it is alone it becomes sleeping, and the next acceptable toppling forces it active and continues the same procedure.

Let `W` be the number of instructions consumed before the first boundary hit. Then:

1. every consumed instruction belongs to an online stopping line; at the stopping time all open-interval sites are empty and the single particle is at one of the two boundary sites;
2. the unused stack tails are conditionally independent fresh ARW stacks;
3. the exact exit probabilities are
   \[
   \boxed{\mathbb P_0(X_\tau=b)=\frac{a}{a+b},\qquad
   \mathbb P_0(X_\tau=-a)=\frac{b}{a+b};}
   \tag{3.1}
   \]
4. the exact mean instruction cost is
   \[
   \boxed{\mathbb E W=(1+\lambda)ab;}
   \tag{3.2}
   \]
5. writing
   \[
   M_{a,b}:=\frac{1+\lambda}{4}(a+b)^2,
   \]
   there is the uniform block tail
   \[
   \boxed{
   \mathbb P\!\left(W>k\left\lceil2M_{a,b}\right\rceil\right)\le2^{-k}
   \quad(k\ge1).
   }
   \tag{3.3}
   \]

In particular, if `a+b=O(L)`, then the empty-gate work is at most `C L^3` except with probability `e^{-cL}`.

#### Proof

At each site the next fresh instruction is sleep with probability

\[
\frac{\lambda}{1+\lambda}
\]

and is a left or right jump with probability

\[
\frac{1}{2(1+\lambda)}
\]

each. An acceptable toppling is allowed whenever there is a particle at the site, including one sleeping particle after forcing it active. Thus sleep instructions act only as holding times for this one-carrier procedure. If we retain only jump instructions, the embedded position process is a simple symmetric random walk started at `0` and killed on hitting `{-a,b}`.

The harmonic function for that jump chain is

\[
h(x)=\frac{x+a}{a+b},
\]

with `h(-a)=0` and `h(b)=1`. Optional stopping at the finite absorption time gives (3.1).

For the jump skeleton, the standard quadratic solution of

\[
e(x)=1+\frac12e(x-1)+\frac12e(x+1),\qquad e(-a)=e(b)=0,
\]

is

\[
e(x)=(x+a)(b-x),
\]

so `e(0)=ab`. Between successive jumps, the number of revealed instructions has a geometric law with success probability `1/(1+lambda)` and mean `1+lambda`. Conditioning on the number of jumps and using Wald's identity gives (3.2).

More generally, from any current interior position `x`, the expected remaining number of jump steps is

\[
(x+a)(b-x)\le\frac{(a+b)^2}{4},
\]

so the expected remaining number of instructions is at most `M_{a,b}`. Markov's inequality gives conditional probability at most `1/2` of surviving another `ceil(2M_{a,b})` instructions from **any** current state. Iterating with the strong Markov property at these deterministic blocks proves (3.3).

Finally, the procedure reveals only the next unused stack entry at the currently occupied site and stops according to the revealed history. Hence its reveal-count vector is a stopping line in the sense already proved in `P13-D0093-STOPPING-LINE-FRESH-TAILS-04`. Every revealed instruction has actually been consumed by the acceptable toppling procedure. Independence of the original stacks therefore gives conditional freshness and independence of all shifted tails. Because there is only one particle, no interior residue can remain after its first boundary hit. This proves all five assertions. `square`

### What B4 solves and what it does not

This theorem **does solve the literal one-carrier / empty-corridor transfer problem** left by the previous report. It is source-native: it uses the actual ARW stacks and acceptable-toppling convention, not an auxiliary directed walk. It also has exactly the `O(L^3)` / `e^{-cL}` cost envelope that the regenerative accounting can afford.

It does **not** solve `REG-CELL`. A real regenerated cell may contain already sleeping particles unless all touched plans have first been sacrificed and fully flushed, and the global cycle still needs a coherent two-sided flow rule. Those are the issues tested next.

## 4. B16 — exact smallest reactivation counterexample

The tempting extrapolation from Theorem 11 is false: an empty-corridor transfer is not automatically a transfer through an already stabilized ARW background.

Take sites `-1,0,1`. Initially place one active carrier at `0` and one sleeper at `-1`. Use the three jump instructions

\[
0\to-1,\qquad -1\to0,\qquad 0\to1.
\]

The first jump activates the sleeper, giving two active particles at `-1`. The second sends one active particle back to `0` but leaves one active at `-1`. The third reaches the intended right boundary. The final configuration therefore contains one active particle at `1` **and one active particle left behind at `-1`**.

Thus a transfer state described by one scalar `q` is not closed under passage through occupied stable cells. The exact local reaction responsible is

\[
\boxed{A+S\longrightarrow 2A.}
\tag{4.1}
\]

A future cell processor must either ensure that every routing corridor has first been cleaned by the full-replay flush, or explicitly track and dissipate this reactivation debt.

After writing this witness and Theorem 11, I executed the exact self-check

`proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T07-10-46Z__d0093_empty_gate_and_reactivation_check.py`.

It uses exact `Fraction` Gaussian elimination, independently of the closed-form proof, to solve the gambler's-ruin linear systems for `L=1,...,8`, checking

\[
\Pr_0(\tau_{+1}<\tau_{-L})=\frac{L}{L+1},\qquad
\mathbb E_0[\#\text{ jumps}]=L,
\]

and then executes the three-jump sleeper witness exactly. Its archived output is

`proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T07-10-46Z__d0093_empty_gate_and_reactivation_check.out`

with terminal line

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check only**, not a universal proof or an independent audit.

## 5. B30 — exact direction-bias tradeoff and the cyclic obstruction

The empty-gate formula quantifies exactly how geometry can bias a symmetric carrier.

Suppose the desired exit is `b>0` sites clockwise and the undesired exit is `a>0` sites counter-clockwise. Theorem 11 gives

\[
q_{\rightarrow}=\frac{a}{a+b},
\qquad
\mathbb EW=(1+\lambda)ab.
\tag{5.1}
\]

This has an initially encouraging consequence. If a genuine trap opportunity has density

\[
p=\frac{\lambda}{1+\lambda}
\]

and source arrivals have density `zeta<p`, then any fixed target service density `theta` satisfying

\[
\zeta<\theta<p
\]

could in principle tolerate a constant routing-success factor `q` as long as

\[
pq>\zeta.
\]

By (5.1), this asks only for the fixed aspect ratio

\[
\boxed{
\frac{a}{b}>\frac{\zeta}{p-\zeta}.
}
\tag{5.2}
\]

Because the source has strict slack `zeta<p`, this ratio is finite; no exponentially long corridor is required merely to obtain negative mean drift.

However, using **static neighboring source gaps** to enforce this bias everywhere on a cycle is impossible in the high-density part of the source domain. Let clockwise source gaps be `d_1,...,d_K>0`. At source `i`, the gambler's-ruin probability of reaching the clockwise neighboring source before the counter-clockwise neighboring source is

\[
q_i=\frac{d_{i-1}}{d_{i-1}+d_i}.
\tag{5.3}
\]

To have `p q_i>zeta` for every `i` would require

\[
\frac{d_{i-1}}{d_i}>\rho,
\qquad
\rho:=\frac{\zeta}{p-\zeta}.
\tag{5.4}
\]

If `zeta>p/2`, then `rho>1`. Multiplying (5.4) over all `i` around the cycle yields

\[
1=\prod_i\frac{d_{i-1}}{d_i}>\rho^K>1,
\]

a contradiction. Therefore

\[
\boxed{
\zeta>\frac p2
\Longrightarrow
\text{no static cyclic source-spacing scheme can make every block a clockwise scalar service queue with }pq_i>\zeta.
}
\tag{5.5}
\]

This is not a counterexample to D0093. It is a counterexample to the **one-direction-at-a-time repair algorithm**.

It also matches the exact shape of Rolla's source proof. Immediately before the urn argument for Proposition 6.5, the source notes that if `zeta<1/2` one could choose `p>2zeta'` and the one-sided Section-4 analysis would suffice; arbitrary `zeta<1` requires a more delicate two-sided argument because roughly half the explorers choose each side and the choices reinforce. The obstruction (5.5) is the finite-cycle geometric version of the same phenomenon.

So B30 succeeds by ruling out the wrong simplification. The remaining cell interface must be genuinely **two-sided**; it cannot be reduced to one globally oriented Lindley queue in the full source regime.

## 6. Full six-run STUCK / handoff diagnosis

The source metric never moved during the six D0093 runs, even though the local obstruction was repeatedly narrowed. Under the owner rule this section records the entire route rather than renaming a metric or manufacturing a seventh run.

### Run 1 — B26 / B18 / B25

- attacked the apparent `log^2 n` obstruction directly;
- proved that polynomial functions of the i.i.d.-Poisson source piles have linear aggregate size with arbitrarily high polynomial probability, so the maximum initial pile is not itself the logarithmic obstruction;
- identified adaptive multiscale repair as the natural replacement for the source's all-block-success union bound;
- proved an abstract accounting lemma: if length `U_j` is repaired at scale `L_j` with `U_j` decaying exponentially in `L_j`, then `sum_j U_j L_j^2=O(n)`.

**Failure:** no history-robust local ARW repair lemma.

### Run 2 — B3 / B12 / B30

- changed the repair accounting to a negative-drift queue;
- proved a periodic Lindley workload theorem and the exact aggregate capacity-surplus identity;
- observed that Rolla's own `zeta<zeta'<p` gives positive mean local surplus at a sufficiently large fixed scale.

**Failure:** the proposed static block capacity was not an ARW state variable after particles traverse a block.

### Run 3 — B11 / B19 / B20

- rewrote the source block as its true two-sided response functions rather than a fake scalar capacity;
- proved stopping-line fresh-tail regeneration for actually consumed stack prefixes;
- gave the one-site `SJJ` counterexample showing that “this stack can trap one particle” is not a persistent resource when another particle arrives;
- isolated corrupted revealed-but-unused instructions as the apparent blocker.

**Failure:** a failed virtual trap plan did not yet have a proved clean restart.

### Run 4 — B6 / B16 / B25

- solved that blocker with chronological full replay;
- proved exactly that replay consumes every instruction revealed by a sacrificed two-sided exploration, leaves residual mass only at the source and hit barriers, restores fresh tails at a stopping line, and costs `O(r^3)` with exponentially high probability;
- exact bounded enumeration found no replay or mass-transport defect.

**Failure:** clean mass at left/right barriers still did not implement a chosen scalar queue direction.

### Run 5 — B1 / B9 / B27

- abandoned the maximum block scale and proved the periodic negative-drift regenerative theorem
  \[
  \sum_j L_j^3=O(n)
  \]
  with polynomially high probability for the surrogate busy-cell lengths;
- thinned the source trap opportunity parameter `p` to any `theta in (zeta,p)` to expose strict queue drift;
- swapped “one `K log n` radius works everywhere” for “random cell sizes whose aggregate cubic cost is linear.”

**Failure:** `REG-CELL` remained unproved: the surrogate Bernoulli service process had not been realized online in symmetric ARW.

### Run 6 — B4 / B16 / B30 (this report)

- proved the exact empty-corridor ARW transfer kernel, including hit law, exact mean work, exponential block tail, stopping-line freshness and no residue;
- gave the exact three-jump reactivation witness showing why occupied backgrounds are not scalar transfer states;
- proved the static cyclic direction-bias obstruction (5.5), showing that a globally oriented scalar queue cannot cover the source regime `zeta>p/2`.

**Failure:** the required local processor must retain genuinely two-sided flow while ensuring that any touched occupied cells are either shielded or sacrificed/flushed before transfer.

### Exact blocking formula

The surviving obstruction can now be stated without vague words such as “history dependence.” For a one-carrier transfer through an **empty** corridor, the exact kernel is

\[
\Pr(\text{right})=\frac a{a+b},
\quad
\Pr(\text{left})=\frac b{a+b},
\quad
\mathbb EW=(1+\lambda)ab.
\tag{6.1}
\]

But if the path hits a sleeper, the state transition contains

\[
A+S\to2A,
\tag{6.2}
\]

so the scalar number of transported particles is not closed. And if one tries to avoid the two-sided state by globally orienting the scalar queue, the necessary inequalities around the cycle are

\[
\frac{d_{i-1}}{d_i}>\frac{\zeta}{p-\zeta},
\tag{6.3}
\]

which are mutually impossible whenever `zeta>p/2`.

### Missing ingredient

A **two-sided regenerative cell processor** on a flushed/cleaned cluster: after the constituent failed/sacrificed plans have been fully replayed, it must accept active mass supported at finitely many internal sources/barriers, use only source-valid acceptable/legal topplings and fresh stack tails, create genuine traps, export any residual mass through **both** outer boundaries in a state that concatenates with adjacent cells, and have a uniform `O(L^3)` work / exponentially summable failure bound. The state must retain both left and right boundary flux; a scalar globally oriented queue is insufficient.

### Simplest unproved case after this run

Two adjacent flushed source intervals, with empty interiors and fresh tails, carrying one unit of excess active mass at their common internal interface plus source piles satisfying the source slack. The one-particle empty transfer is now solved by Theorem 11. What remains is to process that transfer **together with the two-sided trap service of the source piles** and finish with only outer-boundary flux, without touching an occupied neighboring cell or losing stopping-line freshness.

### Nearest solved analogue

Rolla's own Proposition 6.5 is the nearest source-native solved analogue: for at most `2 zeta' r` particles concentrated at one source, the two-barrier exploration is successful with probability `1-e^{-cr}`. Its proof keeps both directions and represents barrier depletion by an urn with two colors; the source explicitly explains why the simpler one-sided argument would only cover the regime where the symmetry factor `1/2` leaves enough trap capacity. Section 4's one-sided trap construction supplies the shielding/freshness mechanism, while the present P13 full-replay theorem supplies a clean way to abandon a failed plan. What is still missing is their **composable multi-cell interface**, not another one-source confinement estimate.

### Recovery decision

The selected recovery episode was “port the analogous technique.” It has now run through the full allowed CLOSABLE horizon and produced the clean-flush, regenerative-accounting, and empty-gate package, but not a source-domain exponent below `2`. The owner rule leaves no discretion here:

\[
\boxed{\text{HAND OFF D0093 AND ROTATE AFTER SIX UNCHANGED RUNS.}}
\]

D0093 remains mathematically **OPEN / PARTIAL**. This operational handoff is not a theorem that the route cannot work, and it is not closure.

## 7. Successor gate after D0093 handoff

The required first successor lead I0054 was not available to P13. Its canonical claim `operations/claims/I0054.md` belongs to **R11**, native task `6aa7b68c70c481919b1a131eb67b6b24`. More importantly, the newest R11 report found in this run is

`runs/R11/2026-09-18T06-42-15Z_i0054-unicyclic-pseudoforest-c038-5f8c.md`,

which continues active I0054 research and reports its own metric movement `37 -> 38`. P13 therefore does not collide with, audit-steal, or restart I0054.

I then reconciled the highest visible CLOSABLE queue front against current claims and recent admission screens rather than trusting stale `QUEUE.md` labels:

- I0011 is exclusively claimed by P16;
- I0035 is claimed in the current fleet;
- I0054 is owned and actively researched by R11;
- I0055's corrected Kahn question is literature-resolved by the recorded Tang result;
- I0070 is reserved to R10;
- I0068 and I0066 are claimed;
- I0077 is reserved to R07;
- I0082 is actively claimed by R08;
- I0095 is reserved to R02;
- I0004 is claimed by P21;
- I0075 is claimed by another native slot;
- D0007--D0010, which were once a READY complete-mixability batch, have since acquired owners.

The apparently unclaimed I0087 was already adjudicated by a recent successor screen: its highlighted `H^2 x R` example is covered by the later 2026 D'Achille--Khezeli product-convergence work, so it is not a lawful fresh-open CLOSABLE replacement in that scope. The newest coordinator screen read here, `operations/task_health/runs/2026-09-17T235200Z/queue_screening.md`, places D0012 on `HOLD_SCOPE / PENDING` and certifies **no new READY + CLOSABLE OUTSIDE + UNASSIGNED successor** in that bounded cursor.

Therefore no new canonical claim is created in this run. P13 exits D0093 into

\[
\boxed{\text{CLOSABLE OUTSIDE / ROTATION HOLD / SUCCESSOR ADMISSION_PENDING}.}
\]

The successor metric is **UNMEASURED**, not zero. Future P13 invocations must continue the admission cursor rather than revive D0093, I0051, or P0082, and must create a successor claim only after the full source/current-status/ownership gate passes.

The existing D0093 claim file is preserved as historical admission/ownership evidence; it is not overwritten or deleted by this worker report. The immutable handoff here is the operational record that P13 no longer performs D0093 research absent an explicit owner-side reassignment.

## 8. P14 directed audit duty and closure gates

P13's secondary directed-audit duty remains P14. No new P14 theorem package dated 2026-09-18 was found that would justify repeating already completed P13->P14 component audits, so no duplicate audit artifact was manufactured.

D0093 never reached the source conclusion, so closure machinery is not invoked. In particular there is no paper package, no closure claim, and no fabricated audit vote. A future genuine D0093 closure would still require the exact finite-cycle Poisson order-`n` proof, a prior-art review with limitations, one P26 end-to-end audit, and one distinct OTHER-track end-to-end audit.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  root: proofnet24/P13-outside-successor
  category: CLOSABLE_OUTSIDE
  source:
    problem_id: D0093
    author: Leonardo_T_Rolla
    title: Activated_Random_Walks_on_Zd
    locator: Section_6_2_second_open_problem_after_Theorem_6_1_equation_6_3
    exact_target: remove_log_squared_n_from_fast_phase_finite_cycle_Poisson_total_toppling_bound
  frozen_metric:
    name: beta_fast
    before: 2
    after: 2
    target: 0
    movement: none
    unchanged_count_before: 5
    unchanged_count_after: 6
  methods_tried:
    - B4_PROVE_SOMETHING_WEAKER_COMPLETELY
    - B16_COMPUTE_EVERY_SMALL_CASE
    - B30_ONE_SCALE_ONE_DIRECTION_AT_A_TIME
  new_author_side_results:
    - id: P13-D0093-EMPTY-GATE-11
      scope: one_active_carrier_empty_interval_fresh_ARW_tails_acceptable_topplings
      statement: "P(right)=a/(a+b), E[instructions]=(1+lambda)ab, stopping-line fresh tails, geometric-block work tail"
      metric_credit: 0
    - id: P13-D0093-CYCLIC-DIRECTION-OBSTRUCTION-12
      scope: static_neighbor_source_spacing_one_direction_scalar_queue
      statement: "if zeta>p/2, p=lambda/(1+lambda), no cyclic gaps can satisfy p*d_{i-1}/(d_{i-1}+d_i)>zeta for every source"
      metric_credit: 0
    - id: P13-D0093-REACTIVATION-WITNESS-13
      scope: three_site_ARW_local_transcript
      statement: "0->-1, -1->0, 0->1 with a sleeper initially at -1 reaches +1 while leaving one active particle at -1"
      metric_credit: 0
  exact_self_check:
    script: proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T07-10-46Z__d0093_empty_gate_and_reactivation_check.py
    output: proofnet24/P13-outside-successor/artifacts/2026-09-18/2026-09-18T07-10-46Z__d0093_empty_gate_and_reactivation_check.out
    terminal: ALL_EXACT_CHECKS_PASS
    label: SELF_CHECK_NOT_AUDIT
  exact_blocker: "two-sided regenerative cell processor after full-replay cleanup; scalar oriented queue is invalid on occupied backgrounds and cannot be globally geometrically biased across the full zeta<p domain"
  recovery_episode: port_analogous_technique
  recovery_status: exhausted_by_six_run_CLOSABLE_limit
  handoff:
    status: OPEN_PARTIAL_SIX_RUN_HANDOFF
    reason: six_consecutive_source_metric_nonmovement_runs
    do_not_restart_without_explicit_reassignment: true
  successor_screen:
    I0054: "SKIP_OWNED_R11_ACTIVE; newest found report moves its metric 37->38"
    current_ready_closable_unassigned_found: false
    successor_state: ADMISSION_PENDING
    successor_metric: UNMEASURED
  closure:
    claimed: false
    P26_end_to_end_audit: missing_not_applicable_yet
    other_track_end_to_end_audit: missing_not_applicable_yet
```

No shared root ledger, historical report, peer file, public post, email/Gmail item, Drive item, workflow, credential, permission, schedule, or retired target was modified.

END OF IMMUTABLE P13 REPORT
