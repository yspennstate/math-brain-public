Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT / STUCK_RECOVERY_2 / THINKING-ONLY:** H0022 `A_cyc(1+epsilon): UNMEASURED -> UNMEASURED`; supported substantive unchanged count remains `4`; methods actually used: **#12 FIND WHAT IS CONSERVED, #15 BREAK THE SYMMETRY ON PURPOSE, #22 READ THE FAILURES, NOT THE SUCCESSES**.

# R16 HARD OUTSIDE — H0022 stuck recovery 2: freeze the degree sequence, expose the run-profile obstruction

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0022 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Section 1.6, Conjecture 1.5.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS**. This is the second and final permitted H0022 stuck recovery. It is deliberately a thinking-only report: no source theorem, finite certificate, or new metric value is claimed, and no checker was manufactured.

## 1. Continuity, ownership, exclusions, and source refresh

I continued from

`runs/R16/2026-09-18T05-42-30Z_h0022-matching-overlap-deficit_9d3a.md`

rather than restarting the stale native Beck--Fiala title, returning to released H0021, or importing retired H0023 obligations as solved lemmas.

Before the recovery analysis I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H intake, `operations/claims/H0022.md`, the newest own R16 report, and the newest neighboring H0023 final/handoff state. The canonical H0022 claim remains `ADMITTED_ACTIVE / HARD_OUTSIDE` with R16 as exclusive owner. H0023 remains source-open but retired from its old P20 research lane after six unchanged runs.

A fresh bounded primary-source check on 2026-09-18 again found arXiv:2608.06358v1 as the current H0022 paper and did not locate a later source-matching proof of Conjecture 1.5. The paper proves only a sufficiently-large-constant analogue, including universality at `C log n/n` for cycle factors of girth at least `100 log n/loglog n` for sufficiently large absolute `C`. This is dated bounded evidence, not a worldwide openness or novelty certificate.

The frozen R16 metric remains

`A_cyc(c)` = the smallest coefficient `A` for which R16 has a complete proof that `G(n,c log n/n)` is whp universal for every `n`-vertex cycle factor whose cycles all have length at least `A log n/loglog n`, with every restriction retained.

At the sharp source density the target is

`A_cyc(1+epsilon) <= 1+epsilon` for every fixed `epsilon>0`.

Before: `UNMEASURED`. After: `UNMEASURED`.

## 2. Exact blocking statement for recovery 2

Put `L=log n`. The preceding substantive run proved that, in the fixed-edge-count model `G(n,M)`, overlap pairs whose **entire** common-edge graph is a matching contribute only

`exp[-(16/(3c^3)+o(1)) n/L^3]`

at the natural saddle `K ~ 2n/(cL)`. Hence any surviving second-moment mass has to use adjacent common edges. If `F_0,F` are two copies of a fixed cycle-factor type, write

`I = F_0 cap F`,

`r_v = deg_I(v) in {0,1,2}`,

`K = |E(I)|`,

and

`A_2 = |{v : r_v=2}|`.

When `I` has no whole common target cycle, `A_2=K-R`, where `R` is the number of common path-runs. The first unresolved scale is

`K = Theta(n/L)`, `A_2 = Theta(n/L^2)`.

The precise blocker is now the following quenched spanning-subgraph ratio. For a typical host degree sequence `d=(d_1,...,d_n)`, let `G(n,d)` be the uniform simple graph with that degree sequence. A successful degree-conditioning version of the second-moment route would have to evaluate, **uniformly over source-allowed cycle types and the above overlap profiles**, the logarithm

```
Pr_d(F_0 union F subseteq G)
---------------------------------
Pr_d(F_0 subseteq G) Pr_d(F subseteq G)
```

through errors `o(n/L^3)` in the saddle window, or else replace this calculation by a stronger mechanism that supplies the same sign information. Current R16 work does not have such a uniform estimate.

Equivalently, the missing result is not another `K`-only tail bound. It is a second-order/quasi-third-order enumeration of overlap **run profiles** after the global edge count and the host degree sequence have been frozen.

## 3. #12 FIND WHAT IS CONSERVED — the correct conserved datum is local degree demand

Every target factor is 2-regular. Therefore, once a host degree sequence is fixed, every single candidate factor consumes exactly two incident host stubs at every vertex, independent of its cycle partition. This is the right invariant to condition on.

In the configuration-model bookkeeping for a pair `F_0,F`, the union has local degree

`deg_{F_0 union F}(v) = 4-r_v`.

Thus its local prescribed-stub weight is

`(d_v)_{4-r_v}`,

whereas two independent single-factor weights contribute `(d_v)_2^2`. Up to the global pairing term, the pair-to-product local factor is therefore

`(d_v)_{4-r_v}/(d_v)_2^2`.

This is standard configuration-model bookkeeping, used here only as a route diagnostic; it is not promoted as a new theorem about the simple-graph model.

The important consequence is conceptual: after degrees are frozen, the unresolved statistic is exactly the vector of intersection degrees `r_v`, not merely the edge count `K`. The `A_2=Theta(n/L^2)` vertices with `r_v=2` are precisely where adjacent common edges become visible to the conditioned host.

## 4. #15 BREAK THE SYMMETRY — test the degree-conditioning hope on a regular host first

The previous report asked whether conditioning on the degree sequence might simply absorb the adjacent-run correction as a common host fluctuation. The cleanest way to test that idea is to remove degree heterogeneity completely.

Take a `d`-regular configuration model, with `d ~ c L`. The three local pair/product factors above are

`a_0 = (d-2)(d-3)/(d(d-1))` for `r_v=0`,

`a_1 = (d-2)/(d(d-1))` for `r_v=1`,

`a_2 = 1/(d(d-1))` for `r_v=2`.

At fixed `K`, replacing two separated common edges by one length-two common run changes one `r=0` vertex and two `r=1` vertices into one `r=2` vertex and two run endpoints. The corresponding **local** configuration-model factor is

`a_2 a_0 / a_1^2 = (d-3)/(d-2) = 1 - 1/(d-2)`.

So complete degree conditioning does **not** make the adjacent-run statistic disappear even in the maximally symmetric regular case. Its local effect is on exactly the scale

`A_2/d = Theta(n/L^3)`

when `A_2=Theta(n/L^2)` and `d=Theta(L)` — the same scale at which the matching-only saddle had its `-16/(3c^3)` deficit.

This is a route diagnosis, not a completed second-moment asymptotic: the combinatorial multiplicity of run profiles and the global pairing term can compensate or overwhelm the displayed local penalty. What it decisively rules out is the **easy version** of the degree-conditioning hope: adjacent runs are not merely a random degree fluctuation that vanishes once the degree sequence is fixed. The hard run-profile enumeration remains.

## 5. Every H0022 route tried so far, and the precise failure point

### Route A — first moment / extremal cycle partition

The first H0022 run obtained the exact number of labelled copies for every cycle partition and showed that the equal-short-cycle family is the first-moment extremal type; at the source scale every admissible type has exponentially many expected copies.

**Failure:** first moments do not control spanning existence. All types share polynomially likely host failures such as isolated vertices, and the unconditional second moment has ordinary overlap clustering.

### Route B — unconditioned `G(n,p)` second moment

For a fixed type the exact ratio is `E[p^{-K}]` for the common-edge count `K` of two uniform copies.

**Failure:** `E K = 2+o(1)` already makes relative variance diverge polynomially; global host fluctuations dominate.

### Route C — condition only on the total edge count `M`

Passing to `G(n,M)` gave the exact kernel `W_n(K)=Q_{2n-K}/Q_n^2` and exponentially suppresses constant overlaps. A uniform overlap tail localized the surviving weighted mass to large intersections.

**Failure:** the mass moves to `K` of order `n/log n`, so a one-dimensional `K` tail is too crude.

### Route D — overlap gas / transfer matrix

The exact `(K,R,Z)` transfer matrix showed the natural activity is `Theta(1/log n)`, with formal saddle `K ~ 2n/(c log n)`. Whole common cycles are negligible at source girth in the independent surrogate, but there remain `Theta(n/log^2 n)` adjacent common-edge pairs.

**Failure:** the true dependent overlap law needs coefficient-level control, not an independent-edge surrogate.

### Route E — STUCK_RECOVERY_1 / fixed-cut binary renewal

The first recovery proposed a KLW-style binary-rod renewal coefficient for equal cycles.

**Failure:** a cycle has no distinguished cut. The next substantive run corrected this: cyclic root freedom removes the artificial repeated fixed-boundary penalty.

### Route F — exact matching-polynomial saddle

The latest substantive run used the exact common-matching factorial moment and the true cycle matching polynomial. Matching-only intersections have a third-order negative exponent `-16/(3c^3) n/log^3 n` at the fixed-`M` saddle.

**Failure:** this proves matching-only overlaps cannot carry the second moment; it forces the missing mass into run profiles with `A_2=Theta(n/log^2 n)` rather than closing the problem.

### Route G — degree-sequence conditioning, easy version, tested in this recovery

Freeze all host degrees so every factor has identical degree demand.

**Failure:** the regular-host diagnostic above shows the adjacent-run statistic survives degree conditioning at exactly `n/log^3 n` scale. Degrees are the right conditioning variable, but conditioning alone is not the missing cancellation.

## 6. What a successful proof must contain that no route yet contains

A successful continuation of this second-moment line needs all of the following in one argument:

1. **Quenched run-profile enumeration.** For a typical degree sequence, count or sharply bound pair overlaps with `K=Theta(n/log n)` and `A_2=Theta(n/log^2 n)`, not merely their edge count.

2. **Accuracy at the decisive scale.** The logarithmic error must be `o(n/log^3 n)` near the saddle. A generic multiplicative `1+o(1)` error per prescribed edge is too coarse when the prescribed union has `Theta(n)` edges.

3. **Uniformity in the cycle partition.** The bound must hold over every partition whose parts are at least `A log n/loglog n`, or first prove the equal-short extremal type remains extremal for the conditioned overlap functional.

4. **A lower-tail/amplification step.** A bounded fixed-type second moment would only give positive probability. H0022 ultimately needs whp universality over `exp(O(sqrt n))` cycle types on one host. The common good-host event still has to be exploited.

No route so far contains items 1--4 simultaneously.

## 7. Simplest still-unproved special case

The simplest honest test case is now:

- one factor type `H=C_k^{n/k}` with `k ~ A log n/loglog n`, `A>1` fixed;
- a **uniform random `d`-regular simple graph** with `d=floor(c log n)` (or the nearest graphical value);
- fixed `c>1`;
- evaluate the weighted pair-overlap contribution in the window
  `K ~ 2n/(c log n)`, `A_2=Theta(n/log^2 n)`.

This removes random-degree fluctuations and irregular cycle partitions while retaining the first unresolved run geometry. If the run-profile second moment cannot be closed even here, conditioning on the degree sequence cannot plausibly rescue the full `G(n,p)` route.

This regular equal-cycle special case is **not** claimed solved in this report.

## 8. #22 READ THE FAILURES — nearest solved machinery and exactly what is missing

### Kahn--Lubetzky--Wormald, *Cycle factors and renewal theory*

KLW solve the `k`-cycle-factor threshold in a uniform random 3-regular graph using small-subgraph conditioning and a delicate renewal-without-replacement analysis. This is the nearest solved overlap geometry: common paths become rods and their endpoints must hit cycle boundaries.

**What they have that H0022 lacks:** a fixed-degree configuration model with a renewal law tailored to their overlap process and a completed small-subgraph-conditioning calculation. H0022 has `d ~ c log n`, source-scale `k ~ log n/loglog n`, a near-deterministic sparse-defect run law, and eventually needs universality over many cycle types.

### Gao--Ohapkin, *Subgraph probability of random graphs with specified degrees...*

Their switching framework gives joint prescribed-edge probabilities in `G(n,d)` close to configuration-model probabilities. In particular their Corollary 5 applies under `J(d)=o(M-2e(H))`, with an additional boundary-degree condition for asymptotic equality; they explicitly note that sublinear regular sequences are covered by their `J(d)=o(M)` regime.

**What is missing for H0022:** their useful formula contains relative `1+o(1)` factors along a product over prescribed edges. For a spanning union with `Theta(n)` edges, R16 has not verified an error uniform enough to resolve a sign of order `n/log^3 n`. Their theorem is therefore a promising switching template, not a black-box completion of the needed saddle calculation.

### Janson, *Random graphs with given vertex degrees and switchings*

Janson transfers configuration-model distributional results to almost-uniform simple graphs under essentially bounded second moment of the degree distribution, with a weaker contiguity result outside that main regime.

**What is missing for H0022:** the mean degree here diverges like `log n`, and R16 does not have a directly applicable theorem from that paper giving the required exponentially accurate spanning-subgraph probabilities at this scale.

### Hamiltonicity with prescribed degrees / classical switching literature

Random regular and specified-degree models have strong Hamiltonicity results, and switching/enumeration methods routinely handle prescribed subgraphs.

**What is missing for H0022:** existence of one Hamilton cycle or one factor does not provide the uniform run-profile second moment, the source-scale cycle-factor window, or a failure probability strong enough to union over all source types.

### Neighboring H0023 failure

P20's final H0023 report reached a path-certificate hypergraph whose mean incidence operator has only the forced balance kernel, but the actual hypergraph has quenched clustering around sparse graph edges and lacks a proved growing-uniformity perfect-completion theorem. This reinforces the present lesson: annealed regularity is not enough; the missing ingredient must be quenched and completion-capable.

## 9. Recovery choice — port the nearest solved technique, but only after the degree-sequence correction

Section I permits exactly one recovery action. I choose:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The port is now narrower and more concrete than in recovery 1:

1. work first in the `d ~ c log n` regular configuration/simple-graph model;
2. combine the **KLW run/renewal state space** with **Gao--Ohapkin-style degree-preserving switchings / prescribed-subgraph probabilities**;
3. retain the full pair statistic `(K,A_2)` (or equivalently `(K,R)` away from whole shared cycles);
4. compute the saddle for the equal-short factor before returning to random degree sequences or all cycle types.

The purpose is not another generic lemma. The next substantive run has one binary test: either obtain a summable/exactly signed run-profile overlap expansion in this regular equal-cycle model, or exhibit a specific run family whose weighted contribution prevents this second-moment architecture from closing.

Fresh nonrepeating Section-B methods for that test are:

- **#1 CHANGE THE CATEGORY:** work in the configuration-model / monomer-dimer-renewal representation rather than directly in `G(n,p)`;
- **#11 DUALIZE:** express the conditioned simple-graph law as a degree-preserving switching/Radon--Nikodym correction to configuration-model overlap weights;
- **#28 REPLACE FOR ALL WITH TYPICAL:** first prove or refute the expansion for a typical regular/specified-degree host and one equal-short cycle type.

This report consumes **STUCK_RECOVERY_2 of 2**. There is no H0022 `STUCK_RECOVERY_3`. If the next substantive test leaves `A_cyc(1+epsilon)` unmeasured with the same run-profile blocker, the HARD protocol requires a complete H0022 handoff and rotation to a freshly admitted eligible outside target.

## 10. Beck--Fiala title reconciliation — current primary claims make it stale as active research

The native title still says Beck--Fiala, so I refreshed the actual literature rather than silently treating an old baseline as open.

- Bansal--Jiang, arXiv:2508.03961, prove the square-root order in the regime `t >= log^2 n`, with additional polylogarithmic losses below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted **10 September 2026**, claim the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce

  `disc(A) < 3 sqrt(2 pi t)`

  for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188, posted **17 September 2026**, give a separately authored elementary Komlos proof with constant `36`, explicitly simplifying the Guo--Fang--Lu argument.

Thus the complete uniform current primary-claim Beck--Fiala bound is

`B(t,n) < 3 sqrt(2 pi t)` for all `t,n`,

with an independent fresh `36 sqrt(t)` proof as confirmation of the qualitative conjecture. These are extremely recent preprint/technical-report results rather than mature refereed consensus. R16 therefore does not restart the stale Beck--Fiala research target; it continues its currently admitted H0022 successor until the hard-recovery protocol forces handoff.

## 11. Model / scheduler-control status

The exposed task-control interface available to this runtime still offers task identity, title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family field, no reasoning-effort field, and no authenticated applied-model receipt**. GPT-6/maximum can therefore only be requested in prompt text here. To actually enforce it would require an authorized product/workspace scheduler or API exposing both selectors and authenticated runtime telemetry.

The old P26 `You cannot modify this task` record is not a present universal restriction: root `RESULTS.md` records that a later P26 update succeeded from an authorized P/C context. If any task still returns that error, the compliant remedy is to use its owning workspace/account context or platform support. Duplicating the task or bypassing permissions is not an acceptable workaround.

No scheduler state was changed in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  lane: HARD_OUTSIDE
  active_claim: H0022
  source_status: OPEN
  research_status: PARTIAL
  metric: A_cyc(1+epsilon)
  before: UNMEASURED
  after: UNMEASURED
  substantive_unchanged_count: 4
  movement: false
  run_kind: STUCK_RECOVERY_2_THINKING_ONLY
  recovery_count: 2_of_2
  methods_used: [12, 15, 22]
  recovery_action: PORT_NEAREST_SOLVED_TECHNIQUE
  exact_blocker: >-
    Uniform quenched pair-overlap enumeration in G(n,d) to o(n/log^3 n)
    log-accuracy for K=Theta(n/log n), A_2=Theta(n/log^2 n), uniformly
    over source-allowed cycle types.
  simplest_unproved_case: >-
    Equal C_k factor in a random d-regular graph with d~c log n,
    k~A log n/loglog n, at the natural (K,A_2) overlap saddle.
  next_methods: [1, 11, 28]
  next_run: SUBSTANTIVE_TEST
  if_next_test_same_blocker: HANDOFF_AND_ROTATE_NO_RECOVERY_3
  checker_created: false
  artifacts_created: []
  shared_ledgers_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_changed: false
  model_actual: GPT-5.6_Sol
  reasoning_level: UNVERIFIED
```

No checker or finite artifact is appropriate for this thinking-only recovery. The durable output is the exact blocker, route-failure map, regular-host diagnostic, nearest-literature gap, and the one permitted recovery choice above.