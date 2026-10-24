Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on P0157: `Q_m -> 0` before and after. STUCK-RECOVERY-1/2, THINKING-ONLY; methods actually used: #11 DUALIZE, #25 COUNT THE SAME THING TWICE, #30 ONE SCALE AT A TIME.**

# R14 HARD OUTSIDE — P0157 STUCK-RECOVERY-1/2: clean-path Poissonization route

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / STUCK-RECOVERY-1 OF AT MOST 2.** This execution intentionally introduces **no new theorem claim, no new finite certificate, and no checker-only artifact**. The purpose is the mandatory Section-I five-part stuck analysis after three consecutive R14 P0157 runs left the frozen metric unchanged.

The negative-margin spherical perceptron and H0008 remain terminally handed off. R14 continues only the exclusive P0157 assignment recorded in `operations/claims/P0157.md`.

## 1. Continuity, repository state, and ownership

Before this thinking run I recovered/read the current campaign and ownership state rather than restarting:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical `operations/claims/P0157.md`, which still records **Owner: R14** and the frozen metric `Q_n`;
- newest own checkpoint `runs/R14/2026-09-19T13-50-48Z_p0157_dyadic_steiner_stuck_trigger_b61e.md`;
- the preceding R14 staircase and matched-pair reports;
- the relevant HARD7-04 P0157 chain, including both of its consumed stuck recoveries, the marked-hub kernel, three-hub skeleton theorem, compensated-queue mass theorem, and terminal handoff;
- the neighboring R17/R19/R20 admission/wait records that all recognize P0157 as R14-owned rather than unassigned;
- the intake alias `P0157|3|two competing scales, barely subcritical CM` and the indexed intake/ranking records.

No competing live owner, release, posting exclusion, or source closure surfaced. I did not edit a shared root ledger or a peer track.

## 2. Fresh source and literature check

### 2.1 Primary source

I reopened the author's current primary source directly:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF page 254,

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The text still says, in the finite-third-moment configuration-model setting, that the barely subcritical behavior is “one interesting open problem.” It recalls the strictly subcritical high-degree law, predicts persistence of a `d_max/(1-nu)` scale sufficiently far below criticality when `d_max` is large, contrasts this with the Erdős--Rényi barely-subcritical scale `delta^{-2} log(n delta^3)` near the critical window, and says this suggests a phase transition within the subcritical regime.

Thus the source status used by this track remains correct: it is a **prose open problem / predicted crossover**, not a fully quantified theorem statement that our stress families could literally refute.

### 2.2 Current nearby literature, bounded search dated 2026-09-19

I rechecked the closest references and looked for a later source-matching closure.

1. **Coulson--Perarnau**, *Largest component of subcritical random graphs with given degree sequence*, arXiv:2111.11780 / EJP 28 (2023): strong configuration-model upper bounds in the (barely) subcritical regime, asymptotically tight for certain degree sequences, but not a complete finite-third-moment two-scale crossover theorem.

2. **Lienau--Schulte**, *Large components in the subcritical Norros--Reittu model*, arXiv:2311.17606 / *Extremes* 28 (2025): point-process convergence for subcritical component statistics in an independent-edge rank-one model. This is structurally close to the marked-tail graph suggested by R14, but its exact Poisson-edge independence is precisely what the configuration model lacks.

3. **Yiming Chen**, *Sharp Asymptotics for the Largest Component in the Subcritical Regime of Preferential Attachment Without Vertex Growth*, arXiv:2607.00731 (1 July 2026): a different model, but methodologically relevant because the upper bound is routed through the configuration model after conditioning on the degree sequence and the lower bound uses tree-component asymptotics plus a second moment.

4. **Janson**, *Random graphs with given vertex degrees and switchings* (2020): switchings can transfer statements from the configuration-model multigraph to the uniform simple graph under appropriate moment assumptions. This does not provide the missing induced-tail-graph coupling, but it confirms that switching counts are a natural exact language for pairing-law comparisons.

I did **not** locate a 2026 paper in this bounded search that closes the exact deterministic-degree finite-third-moment crossover retained by the August 2026 monograph. This is bounded negative evidence only, not a worldwide novelty certificate.

## 3. Frozen metric: no movement

The canonical P0157 metric remains

\[
Q_n
:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the inherited stress/staircase families,

\[
Q_m\sim m^{-1}\to0.
\]

This thinking-only recovery does not change that scalar:

\[
\boxed{Q_m:0\text{ in the limit}\longrightarrow0\text{ in the limit}.}
\]

No movement. I do not relabel the route correction below as movement in the frozen quantity.

---

# Section-I stuck report

## (a) Exact statement that blocks

The previous R14 run reduced the marked-tail route to two missing ingredients. The first is a two-sided approximation of top-band connectivity by the rank-one kernel

\[
\kappa_{ij}^{(a)}\approx \frac{d_i d_j}{\ell\delta_a},
\qquad
\delta_a
=1-\frac1\ell\sum_{v:\,d_v<a}d_v(d_v-1),
\]

and the second is transfer from marked-degree mass to total component size.

The strongest form written in the previous report was

\[
\Pr(A\text{ tail-exact connected})
\stackrel{?}{\sim}
\sum_{T\in\mathcal T(A)}
\prod_{\{i,j\}\in E(T)}
\frac{d_i d_j}{\ell\delta_a}.
\tag{S1}
\]

The present thinking run identifies an important **route correction**: `(S1)` should not be demanded uniformly whenever its right-hand side is not a rare-event quantity. In an actual rank-one graph, once several tree witnesses have non-negligible probability, different trees can coexist and cycles can occur; a raw tree sum can exceed one and therefore cannot remain asymptotic to a probability. This is not a new theorem claim; it is a correction to the target formulation of the missing lower bound.

The more robust blocker is therefore the distributional one:

\[
\boxed{
\text{Construct a source-valid asymptotic coupling/contiguity of the}\
\text{single-band tail connectivity process to a rank-one Poisson graph,}
}
\tag{B1}
\]

at least on the exploration sizes relevant to the largest marked component, and then prove the mass map

\[
\boxed{
|C|\approx \frac1{\delta_n}
\sum_{i\in C\cap H_a}d_i
}
\tag{B2}
\]

uniformly enough to survive post-selection of the largest component.

The previous dyadic Steiner theorem supplies only the one-sided tree-dominance / overlap-penalty structure needed for `(B1)`; it does not supply a coupling or matching lower law.

## (b) Routes tried and the precise reason each failed

The complete P0157 history is long; only routes relevant to the present blocker are grouped here.

### Local one-root branching / frozen scalar

`Q_n` measures self-averaging of the ideal root branching forest. It correctly diagnoses fixed-root fluctuations but cannot encode how many comparable high-degree roots merge. The stress and staircase families made this failure decisive: `Q_m -> 0` while multi-hub coalescence changes the largest-component constant, even by a diverging factor along the growing staircase.

### Fixed-root exploration and compensated queue

These routes proved sharp mass laws for a preselected hub and later for the explicit three-hub conditioned stress family. They fail as a general crossover mechanism because the largest component is selected after the graph is revealed, and arbitrary upper-degree tails can contain many potential marked seeds.

### Marked pair kernel

The bulk Green-function calculation produced the pair scale

\[
\kappa_{ij}\approx d_i d_j/(\ell\delta_H).
\]

It is only a marginal. Pairwise probabilities do not imply joint edge independence. The missing dependence lives in shared bulk paths, path intersections, half-edge depletion, and components with unlisted high-degree vertices.

### Exact skeleton counting

Finite core enumeration and second moments settled the special three-hub skeleton and excluded four hubs in the stress family. This does not generalize automatically to a growing arbitrary tail because enumerating every core topology is exactly the combinatorial explosion the rank-one reduction is supposed to avoid.

### Matched-tail pair and growing staircase

These showed that `H_n`, `E_n`, `Q_n`, and limiting low moments do not determine the largest-component scale. They are diagnostic counterexamples to scalar-only routes, not a positive characterization theorem.

### Dyadic Steiner penalty

The newest theorem suppresses an unmarked bulk branch-point defect `t`: every extra Steiner branch pays a factor of order `r/(a delta_a)` on a dyadic band. The `t=0` contribution equals the weighted Cayley tree sum of the rank-one kernel. This is strong one-sided structure, but it does **not** prove that disjoint path witnesses occur with the needed approximately independent law.

### Why a direct lower-tree bound is the wrong universal target

The previous target `(S1)` treats the sum over spanning trees as if it were a probability. That is only plausible in a rare-event regime where the total witness intensity tends to zero. In the transition regime, an independent rank-one comparison object itself has multiple tree witnesses and cycle corrections. Therefore the right positive theorem should approximate the **edge/path witness process**, not force one particular first-moment tree expansion to remain exact everywhere.

## (c) What a proof must contain that no route so far contains

A successful route needs a genuine process-level approximation, not another scalar or another family.

### C1. Define clean bulk-path counts

For one dyadic tail band

\[
B_a=\{i:a\le d_i<2a\},
\]

define for each unordered pair `{i,j}` a count `N_ij` of **clean bulk paths** joining `i` and `j`: internal vertices have degree `<a`, no other marked tail vertex is visited, and path length is truncated before the long-exploration scale already controlled in the preceding theorem.

The target comparison law is not a Bernoulli graph at first. It is a family of approximately independent Poisson path counts with means near

\[
\mu_{ij}\approx\frac{d_i d_j}{\ell\delta_a}.
\]

Only after that step should the induced simple tail graph use edge probability `1-exp(-mu_ij)`.

### C2. Factorial moments for disjoint path systems

For a fixed collection of vertex-disjoint clean path witnesses, the exact pairing probability is a falling-product of reciprocal remaining-half-edge counts. The required proof has to show that the depletion correction is `1+o(1)` over the total exploration budget relevant to the largest tail component.

This is where a direct exact pairing count and a sequential exploration count should agree.

### C3. Overlap systems must be negligible for a structural reason

Whenever two nominal pair paths overlap in the bulk, suppressing degree-two bulk vertices creates a positive Steiner defect or another explicit collision defect. The previous dyadic theorem suggests that these configurations should inherit a factor like

\[
O\!\left(\frac{r}{a\delta_a}\right)^t,
\qquad t\ge1,
\]

plus the already isolated long-path error. A process-level proof must promote that one-sided core penalty into factorial-moment control for *systems* of pair witnesses.

### C4. A Poisson-approximation criterion with a growing index set

Classical finite-dimensional method of moments is not enough if the marked component size `r=r_n` grows. One needs either:

- a Stein--Chen / dependency-graph error bound for all relevant `N_ij`;
- a total-variation coupling on a truncated set of marked vertices;
- or a switching ratio strong enough to produce the same conclusion.

The error must remain `o(1)` on the scale used to locate the largest marked component.

### C5. Only then transfer to component mass

Even a perfect tail-graph coupling does not by itself prove the source theorem. One still needs the bulk-mass map `(B2)` with a selection-safe tail. The existing compensated-queue theorem shows this mechanism on the explicit stress family; a general theorem needs a version uniform over the random marked component selected by the tail graph.

This two-layer decomposition is what no previous P0157 route has yet contained:

\[
\text{CM pairing}
\to
\text{Poisson clean-path process}
\to
\text{rank-one tail component}
\to
\text{bulk-mass map}.
\]

## (d) Simplest special case still unproved

The smallest useful target is deliberately narrower than the full source problem but broad enough to exercise the missing dependence mechanism.

Take a **single dyadic band** `B_a` with all marked degrees in `[a,2a)`. Write

\[
S_a=\sum_{i\in B_a}d_i,
\qquad
\lambda_a:=\frac{aS_a}{\ell\delta_a}.
\]

The special case is the very sparse marked regime

\[
\lambda_a\to0,
\qquad
\max_{i,j\in B_a}\frac{d_i d_j}{\ell\delta_a}\to0,
\]

with marked component sizes restricted to the largest scale predicted by the corresponding sparse rank-one graph and with the preceding long-path/Steiner errors tending to zero.

**Special-case target for a future proof run:** show that the joint clean-path counts on this one band are asymptotically distributed like independent Poisson variables with means `mu_ij`, uniformly on the finite/growing marked subgraphs needed to determine the largest marked component.

This is not claimed here. It is the simplest unproved case because:

1. it keeps the actual configuration-model pairing law;
2. it keeps a growing high-degree population;
3. pair intensities are individually rare, so Poissonization is meaningful;
4. the induced rank-one graph can still have nontrivial extreme components;
5. it avoids multi-scale gluing until the dependence problem is solved once.

A proof of this special case would remain **PARTIAL**, not closure of P0157.

## (e) Nearest solved problem and what its proof has that P0157 lacks

The nearest positive comparison object is **Lienau--Schulte's subcritical Norros--Reittu model**. There, conditional on weights, edge counts are independent Poisson random variables from the start. That exact product structure permits component point-process arguments without having to prove that different high-weight connections are asymptotically independent.

For the actual configuration model, the desired rank-one structure is only emergent after summing over bulk paths. The missing ingredient is exactly an **independence manufacture theorem**: disjoint pairing witnesses must asymptotically factor, and overlapping witnesses must be shown negligible uniformly on the extreme-component scale.

Chen's 2026 paper supplies the complementary lesson for lower bounds: count full tree components before selecting the largest one, and use a second moment. Coulson--Perarnau supplies the closest configuration-model upper-bound architecture. Neither paper gives the marked-tail Poisson path-process coupling required here.

Janson's switching paper shows that exact pairing-law switchings can successfully compare nearby graph laws, but its target is simplicity/uniformity rather than an induced high-degree tail graph. Thus the technical gap is not the existence of switching methodology; it is designing a switching or factorial-moment scheme whose **defect parameter is the same overlap/Steiner defect already isolated by R14**.

---

# Method outcomes in this recovery

## #11 DUALIZE — outcome: route reformulated, not solved

I tried to dualize the missing lower bound from “prove a connectedness probability” to “compare two probability laws.” The natural object is the path-count process `N=(N_ij)`, and the comparison law is independent Poisson counts.

A direct switching between “no witness” and “one witness” pairings is not yet enough: a pairing can carry several witnesses, one switching may create/destroy multiple paths, and reverse multiplicities depend on overlaps. This is exactly why the overlap defect must be part of the state.

**Outcome:** useful reformulation. The hard direction should be attacked as Poissonization / Radon--Nikodym control of witness counts, not a raw lower bound on a single connectedness event.

## #25 COUNT THE SAME THING TWICE — outcome: identifies the missing error terms

The same clean path system can be counted in two languages:

1. exact random-pairing witness counts, using falling products of available half-edges;
2. sequential bulk exploration, where each step sees the size-biased bulk offspring law until collision or marked-tail absorption.

For disjoint witness systems these descriptions should differ only by depletion. For overlapping witness systems they differ because one bulk structure can realize several nominal marked edges at once. Suppressing degree-two pieces turns that discrepancy into the Steiner/collision cores already identified in the previous theorem.

**Outcome:** this suggests a concrete factorial-moment proof architecture, but no uniform error estimate is proved in this thinking run.

## #30 ONE SCALE AT A TIME — outcome: chooses the correct proving ground

Trying to couple the full upper tail across all degree scales immediately mixes three difficulties: varying pair intensity, cross-scale absorption, and post-selection of the largest component.

The one-band sparse regime isolates only the dependence question. Once that is solved, cross-scale gluing can be formulated as a separate inhomogeneous rank-one problem rather than entangled with the configuration-model pairing law.

**Outcome:** the next admissible positive route should be one dyadic band first. No multi-scale theorem should be attempted until the single-band Poissonization error is explicit.

# Exactly one recovery choice

Per Section I, I choose exactly one action:

> **PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d): single-dyadic-band clean-path Poissonization in the very sparse marked regime.**

This report does **not** execute that proof because STUCK-RECOVERY-1 is thinking-only. The next proof-capable attempt, when protocol permits it, should derive joint factorial moments / a Stein--Chen error for the clean-path counts and use the previous Steiner penalty to control overlaps.

The three fresh Section-B moves reserved for the next stuck/recovery analysis are:

- **#9 RANDOMIZE:** treat clean paths as a point process and seek a direct Poisson coupling;
- **#20 FIND WHY THE ALGORITHM FAILS:** write the sequential path-exposure/coupling algorithm and isolate the first event that breaks independence;
- **#24 FIND THE EXTREMAL OBJECT:** identify the overlap core or degree profile maximizing the Poissonization error under the finite-third-moment constraints.

Because the frozen metric and source-level obligation remain unchanged, this run consumes **STUCK-RECOVERY-1/2**. It does not authorize silently resetting the stagnation count.

## Model / scheduler capability truth

The model-control limitation remains unchanged. The exposed task-control surface provides prompt/title, schedule or relative start, timing mode, enablement, and notification controls, but **no binding model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum is still prompt text only and cannot be truthfully claimed as the applied runtime here.

The historical P26 message `You cannot modify this task` is an authorization-context boundary. Repository records indicate that P26 was later editable from another authorized context. The legitimate remedy for any currently protected task is its owning/admin-authorized account/workspace/context or platform support. No permission bypass, duplicate scheduler, scheduler mutation, email, Drive operation, public posting, purchase, or workflow execution was attempted.

## Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  target: P0157
  canonical_claim: operations/claims/P0157.md
  source_status: OPEN
  worker_status: PARTIAL

  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before: Q_m ~ m^-1 -> 0
  after: Q_m ~ m^-1 -> 0
  movement: none

  protocol_state: STUCK_RECOVERY_1_OF_2
  theorem_claims_this_run: 0
  finite_claims_this_run: 0
  checker_added: false

  methods_used:
    - 11_DUALIZE
    - 25_COUNT_THE_SAME_THING_TWICE
    - 30_ONE_SCALE_AT_A_TIME

  exact_blocker:
    - source-valid process-level approximation of single-band CM tail connectivity by a rank-one Poisson graph
    - selection-safe bulk-mass transfer after marked-component selection

  route_correction:
    old_target: raw spanning-tree probability asymptotic uniformly in growing regimes
    new_target: joint clean-path Poissonization / rank-one process coupling first

  recovery_choice: PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE
  chosen_special_case: single dyadic band, very sparse marked regime, joint clean-path Poissonization

  next_methods:
    - 9_RANDOMIZE
    - 20_FIND_WHY_THE_ALGORITHM_FAILS
    - 24_FIND_THE_EXTREMAL_OBJECT

  predecessor_reopened: false
  shared_root_modified: false
  peer_files_modified: false
  email_sent: false
  drive_used: false
  public_posting: false
  scheduler_changed: false
```
