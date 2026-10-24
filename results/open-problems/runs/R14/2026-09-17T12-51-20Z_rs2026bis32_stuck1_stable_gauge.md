Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `D_bis: 2 -> 2`; unchanged count `3 -> 4`; `STUCK-RECOVERY-1/2`. Methods actually tried: #7 TAKE THE LIMIT, #21 ASK WHO ELSE HAS THIS SHAPE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# R14 — RS-2026-BIS32 STUCK-RECOVERY-1: where fixed-degree bisection symmetry actually breaks, and a local-stable-gauge handoff

Status: **OPEN / PARTIAL**. The active exclusive R14 target remains `RS-2026-BIS32`, Afonso S. Bandeira's Randomstrasse 101 Conjecture 32 (Min and Max Bisections), tracing to Zdeborova--Boettcher. The original negative-margin spherical-perceptron target remains handed off and is **not reopened**; its last supported rigorous bracket remains

\[
6.30297437506\le \alpha_c(-1)\le 12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

The intervening I0089 Riesz target also remains handed off. This run continues the current `RS-2026-BIS32` state from `runs/R14/2026-09-17T11-51-30Z_rs2026bis32_cutspace_gauge_decorrelation.md` and obeys its mandatory `STUCK-RECOVERY-1` instruction. This is a thinking run: I did **not** manufacture a new theorem label or checker merely because the fixed metric stayed unchanged.

## 1. Repository continuity, ownership, and current source status

At run start I reread the controlling campaign material (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`), the canonical claim `operations/claims/RS-2026-BIS32.md`, and the newest complete R14 report. I also checked current neighboring R13/R15 report evidence. The intake collection is too large to render safely as one connector response, so I used targeted repository searches for the exact source/target/ownership rather than claiming a complete row-by-row intake rendering.

The live Randomstrasse page was checked again on 2026-09-17. It still states Conjecture 32 for a uniformly random **simple** fixed-`d` regular graph on even `n`:

\[
\frac{\mathbf E\,\mathrm{MinBis}(G_d)+\mathbf E\,\mathrm{MaxBis}(G_d)}{n}
=\frac d2+o(1),\qquad n\to\infty,
\tag{BIS32}
\]

with `d>=3` fixed. A fresh bounded search of primary literature did not find a 2025--2026 theorem closing (BIS32) at any fixed `d>=3`. In particular:

- Gheissari--Perkins--Yap, arXiv:2511.16620, proves a **positive-temperature** Zdeborova--Boettcher relation only below the tree reconstruction threshold, with the antiferromagnetic side **unconstrained MaxCut** and the ferromagnetic side zero-magnetization MinBis; it does not give balanced MaxBis and it does not reach zero temperature.
- Dembo--Montanari--Sen, arXiv:1503.03923, gives the zero-temperature symmetry to leading order only in the further `d -> infinity` asymptotic.
- Coja-Oghlan--Loick--Mezei--Sorkin, arXiv:2009.10483, rigorously identifies an antiferromagnetic replica-symmetry-breaking transition and gives MaxCut bounds, not the balanced MinBis/MaxBis equality.
- Csoka--Fekete--Nagy--Szemeredi, arXiv:2509.08531, improves finite-degree bisection/max-cut bounds (notably at degree five) but does not prove Conjecture 32.

This is bounded negative evidence, not a novelty certificate.

The fixed metric remains

\[
D_{\rm bis}:=\sup\{D\ge2:\text{(BIS32) is rigorously proved for every fixed }3\le d\le D\}=2.
\]

## 2. (a) Exact statement that blocks

The source-level blocker is

\[
\boxed{
B_{n,3}:=
\mathbf E\big[\mathrm{MinBis}(G_3)+\mathrm{MaxBis}(G_3)\big]
-\frac{3n^2}{2(n-1)}
=o(n).
}
\tag{S0}
\]

The `3n^2/[2(n-1)]` center differs from `3n/2` by only `O(1)`, so (S0) is exactly the fixed-degree `d=3` movement obligation in the current metric.

The strongest current route-specific sufficient condition is the previous report's deterministic max-cut-gauge reduction. For a balanced bisection spin `sigma`, and a maximum-cut gauge `eta`, the previous report defined

\[
\Phi_G(\sigma)=
\min_{\eta\in\operatorname{ArgMaxCut}(G)}
\left(
|R_\eta(\sigma)|+\frac32|\langle\sigma,\eta\rangle|
\right),
\]

with `R_eta(sigma)` the signed contribution from the frustration matching. The exact blocker on that route is

\[
\boxed{
\mathbf E\max\{\Phi_-(G_3),\Phi_+(G_3)\}=o(n).
}
\tag{S1}
\]

No known argument in the material I found controls the joint zero-temperature correlation in (S1). The rest of this report explains why this is not merely a missing local lemma.

## 3. (b) Routes tried so far, and the precise failure of each

### Route 1 — exact finite-`n` enumeration

The first `RS-2026-BIS32` run exhaustively tested the smallest simple regular graphs. It refuted the tempting stronger statement that `MinBis+MaxBis=dn/2` at every finite `n`, while leaving the asymptotic source conjecture untouched.

**Failure:** finite exact data identifies the sign/size of the correction at small `n`, but provides no monotone quantity or recurrence that controls the `n -> infinity` correction.

### Route 2 — balanced Ising pressure and temperature deformation

Writing the bisections as extrema of the zero-magnetization Ising Hamiltonian gives an exact soft-max route: if the odd part of the balanced quenched pressure is sublinear uniformly as `beta -> infinity`, then (BIS32) follows.

**Failure:** the rigorous fixed-magnetization theorem of Gheissari--Perkins--Yap stops at `beta < beta_r`, the tree reconstruction threshold. Their application relates unconstrained antiferromagnetic MaxCut to ferromagnetic zero-magnetization MinBis, not balanced antiferromagnetic MaxBis. The exact missing regime is therefore both **beyond reconstruction** and **balanced on the antiferromagnetic side**. Taking `beta -> infinity` is not justified by their theorem.

### Route 3 — configuration-model reflection and transfer to simple graphs

The balanced cut-counting function in the configuration model has an exact reflection at exponential scale, and the previous run transferred the same leading annealed complexity to the uniform simple model.

**Failure:** this proves the correct symmetry only for the **annealed** enumerator. Extremal cut values depend on the quenched edge of the support. The first moment can be dominated by atypical graph/configuration pairs, and no edge-uniform quenched concentration theorem was obtained.

### Route 4 — planted/reverse-KL duality

The annealing gap was rewritten exactly as a reverse KL divergence between the null random-regular law and a balanced Ising planted mixture. Conjecture 32 becomes equality of the positive- and negative-temperature zero-temperature reverse-information slopes.

**Failure:** this is an exact dual reformulation, not a contraction estimate. Above reconstruction the relevant models have nontrivial glassy structure; there is no rigorous reason found for the two reverse-KL slopes to agree at fixed `d=3`.

### Route 5 — graph complementation

The centered finite-`n` defect satisfies an exact antisymmetry under graph complement.

**Failure:** complement sends degree `d` to degree `n-1-d`. It therefore exchanges a sparse fixed-degree problem with a dense one instead of remaining in the fixed-`d=3` source regime.

### Route 6 — LDGM/cut-code shell spectrum

The balanced cut problem can be expressed as the output-weight edge of a column-weight-two LDGM-type map restricted to a constant input-weight shell. The annealed shell spectrum again has the required reflection symmetry.

**Failure:** available enumerator machinery controls average shell weights rather than the quenched smallest/largest nonempty shell support. The problem is precisely the support edge, not its mean multiplicity.

### Route 7 — local balanced swaps

For equal-size vertex swaps, the cut increment has an exact decomposition. If the swapped induced subgraph is empty, min and max local optimality have perfectly reflected inequalities.

**Failure:** a typical fixed small swap set is almost edge-free, but an extremizer can choose among exponentially many swap sets. The signed induced-edge correction is therefore an adversarial extreme-value term; a typical-set estimate cannot control it.

### Route 8 — affine cut-code / maximum-cut gauge

The newest route makes MaxBis an orthogonality-constrained nearest-codeword problem. In cubic graphs, the frustration set of a maximum cut is a matching, yielding the exact deterministic reduction (S1).

**Failure:** global maximum-cut gauges and global minimum/maximum-bisection optimizers may remain extensively correlated. The matching property controls the geometry of the residual but not its **sign cancellation**, and it gives no sublinear control of the overlap `|<sigma,eta>|`. Neither current fixed-temperature results nor cavity heuristics provide a rigorous quenched estimate for this joint global-optimum correlation.

## 4. Method #7 — TAKE THE LIMIT: the zero-temperature limit is exactly where the theorem stops

The natural hope was to start from the 2025 fixed-magnetization positive-temperature theorem and take `beta -> infinity`. The fresh source check shows that this is not a technical afterthought.

Gheissari--Perkins--Yap prove, for each fixed `d>=3`, convergence of fixed-magnetization **ferromagnetic** free energy to its annealed/Bethe value only below reconstruction. Their abstract already isolates the obstruction: the theorem is `beta < beta_r`, and the application to Zdeborova--Boettcher is correspondingly positive-temperature and below reconstruction.

The R14 soft-max estimate itself is harmless: for a finite graph the error between `beta^{-1} log Z` and a ground-state extremum is `O(n/beta)`. What is missing is a source-valid control of the **odd balanced quenched pressure** through the entire low-temperature interval. A theorem only on every compact interval below `beta_r` cannot be diagonalized to `beta=infinity`; the obstruction is a genuine phase transition, not a bookkeeping limit.

Conclusion of #7: **the direct positive-temperature-to-zero-temperature deformation is exhausted unless one first proves a new beyond-reconstruction balanced-antiferromagnetic theorem.** That is at least as hard as the present source problem and is not a useful next lemma.

## 5. Method #21 — ASK WHO ELSE HAS THIS SHAPE: local stable states are the closest structural analogue

The closest object I found to the C205 gauge residual is not another global optimization problem. It is the ensemble of **single-spin-flip-stable** (disassortative) cuts studied by Behrens--Arpino--Kivva--Zdeborova, arXiv:2202.10379.

Their paper explicitly relates assortative/disassortative partitions to single-spin-flip-stable states and, using the cavity method, argues for an asymptotic relation between the two families. This is nonrigorous for our source purpose, but it suggests a materially different way to use the existing cubic matching observation.

The one-vertex proof behind R14-C204 never used the full global maximality of the cut except to guarantee that no single vertex flip can increase it. Thus the **route**, without promoting a new theorem in this thinking run, can be relaxed from the small set `ArgMaxCut(G)` to the much larger set of one-flip-stable disassortative cuts. For every such candidate gauge the same frustration geometry is expected to be a matching; the exact gauge identity itself already holds for any spin gauge.

This changes the probabilistic problem qualitatively. Instead of asking whether two separately chosen global optima decorrelate, ask whether among an exponentially large family of local stable gauges there exists **one** gauge with small overlap and small signed matching residual against the chosen extremal bisection. Entropy may help an existence statement even when two global optima remain correlated.

What is missing is a rigorous quenched existence theorem conditioned on the extremal bisection. A stable gauge chosen independently of `sigma_-(G)` is not enough, because `sigma_-` is itself an adversarial function of the same graph.

## 6. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

The literature failures line up around one boundary.

1. **Below reconstruction:** rigorous replica-symmetric fixed-magnetization control exists (Gheissari--Perkins--Yap).
2. **Above reconstruction / low temperature:** Coja-Oghlan--Loick--Mezei--Sorkin rigorously identify a replica-symmetry-breaking transition for the antiferromagnetic model and obtain MaxCut bounds, but not a balanced extremal symmetry.
3. **At zero temperature with another asymptotic parameter:** Dembo--Montanari--Sen recover the symmetric `+/- P_* sqrt(d)` corrections only after `d -> infinity`; their error is not a fixed-`d` closure mechanism.
4. **Single-spin-flip-stable states:** Behrens--Arpino--Kivva--Zdeborova obtain the right qualitative symmetry by cavity/BP reasoning, but this is precisely the point where a rigorous quenched conditional-counting theorem is absent.

The common failure is therefore not “we have not optimized the constant.” It is:

\[
\boxed{
\text{no rigorous fixed-}d\text{ theorem controls the joint low-temperature / zero-temperature overlap geometry}
}
\]

of the balanced ferro/antiferro extremal states needed here.

That diagnosis also explains why the annealed, coding, local-swap, and planted-duality formulations all stall at the same point: each loses the correlation structure of the **typical graph's extremizers**.

## 7. (c) What a proof must contain that no route so far contains

A source-closing proof at `d=3` needs one ingredient absent from every route tried so far:

> **A quenched, zero-temperature correlation principle that survives beyond reconstruction.**

It can take several forms, but it must imply a sublinear relation between the actual extremal balanced states on the **same** random cubic graph. Annealed enumeration, marginal local weak convergence, a typical fixed swap, or an independently sampled stable state cannot substitute for this.

For the current gauge route, the minimum sufficient content would be a theorem that supplies, for the actual extremal bisection(s), a gauge whose magnetization overlap and signed frustration residual are both `o(n)` in expectation. A graph-by-graph involution would be even stronger, but no such involution has emerged from the cut-space formulation.

## 8. (d) Simplest special case still unproved

The simplest source-relevant special case I can isolate is **one-sided and local-stable**, not the full two-extremizer statement.

Let `sigma_-(G)` be one measurable minimum-bisection optimizer of a random cubic graph. Let `L(G)` denote the set of cuts that are stable under every one-vertex cut-improving flip. For `eta in L(G)`, use the same exact gauge residual `R_eta(sigma)` as in the preceding report.

The special case is to prove

\[
\boxed{
\mathbf E\min_{\eta\in L(G_3)}
\left(
|R_\eta(\sigma_-)|+\frac32|\langle\sigma_-,\eta\rangle|
\right)
=o(n).
}
\tag{SC}
\]

I am **not** claiming (SC) here. It is deliberately weaker than (S1): it treats one extremal bisection instead of both, and replaces a global maximum-cut gauge by a one-flip-stable gauge. It preserves the exact source graph and balance convention and is the smallest case I found that still tests the missing quenched correlation mechanism rather than another annealed surrogate.

The reason this special case is worth trying is structural: one-flip-stable cubic cuts have the same local matching-type frustration geometry that made C205 possible, but there can be vastly more of them than global maximum cuts. If that entropy can be converted into conditional anti-concentration against `sigma_-`, the route changes category from “correlate two global optima” to “find one good witness in a large stable-state family.”

## 9. (e) Nearest solved problems and what they possess that this problem lacks

### Nearest fixed-`d` rigorous result

**Gheissari--Perkins--Yap (2025), fixed-magnetization Ising below reconstruction.** Their proof has rigorous quenched free-energy control and local weak convergence in a replica-symmetric temperature regime. The current problem lacks exactly the extension of that control through reconstruction and to zero temperature on the balanced antiferromagnetic side.

### Nearest zero-temperature result

**Dembo--Montanari--Sen (2017), large-degree extremal cuts.** Their interpolation to the Sherrington--Kirkpatrick model produces the symmetric leading min/max corrections at zero temperature. The current problem lacks a fixed-degree error theory: `d -> infinity` is an essential asymptotic in their conclusion, so it does not move `D_bis` from 2 to 3.

### Nearest structural analogue, but not a solved rigorous substitute

**Behrens--Arpino--Kivva--Zdeborova (2022), (dis)assortative partitions.** Their cavity analysis has the right local-stability state space and argues for an assortative/disassortative symmetry. What it lacks for this campaign is a rigorous quenched theorem, especially one conditioned on an extremal bisection.

## 10. Section-I choice — exactly one recovery action

I choose exactly one of the allowed Section-I actions:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d).**

The next recovery attempt is therefore (SC), not another lemma about global `ArgMaxCut` gauges and not another annealed enumerator. If (SC) itself has no viable mechanism after the next allowed recovery, the max-cut/local-stable-gauge family should be handed off rather than extended indefinitely.

The next methods are deliberately different from the current triple:

- **#15 BREAK THE SYMMETRY ON PURPOSE:** target only the minimum-bisection optimizer `sigma_-` first, not both extrema.
- **#9 RANDOMIZE:** investigate whether a randomized one-flip-stabilization / stable-state sampling construction can supply many candidate gauges and an anti-concentration mechanism conditional on the graph.
- **#19 MAKE IT AN ALGORITHM:** turn the witness search in (SC) into an explicit local-improvement procedure with a secondary overlap/residual objective, so the exact failure point is testable rather than hidden in an existential cavity ansatz.

No numerical simulation from that future route will count as movement. Movement remains only a rigorous proof of (BIS32) at `d=3`, i.e. `D_bis:2->3`.

## 11. No checker this run

This was the mandatory thinking run. I made no new finite claim needing an exact certificate and therefore did not spend the run creating a redundant checker or receipt artifact. The earlier C203/C205 exact outputs remain self-checks only, with `0/2` external audits for those claims.

## 12. Model / reasoning and scheduler-control status

The model-control limitation is still true in the interface exposed to this runtime. Task editing exposes title/prompt, schedule or relative start, enablement, and timing mode. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains request text only here; I cannot truthfully report it as enforced.

Changing that would require an authorized scheduler/product/API surface that exposes model and reasoning fields and reports the model actually used on the completed run, or a platform-side change adding those controls. Prompt text alone is not enforcement.

For tasks that return `You cannot modify this task`, repository history shows the result is authorization/context dependent: some task edits that failed in one context later succeeded in another authorized owning context. The valid workaround is to edit from the owning account/workspace/authorized scheduler context or escalate to platform support. Duplicating the task or bypassing permissions is not a valid workaround. No scheduler change was attempted in this run, as required by the owner instruction.

```yaml
ledger_delta:
  track: R14
  target: RS-2026-BIS32
  source: "Randomstrasse 101, Conjecture 32 (Min and Max Bisections), 2026-02-16"
  status: OPEN/PARTIAL
  metric: D_bis
  before: 2
  after: 2
  moved: false
  unchanged_count_before: 3
  unchanged_count_after: 4
  stuck_recovery: "1/2"
  methods_actual: [7, 21, 22]
  new_theorem_claims: []
  new_checker: none
  exact_blocker_source: "B_n,3 = o(n)"
  exact_blocker_current_route: "E max(Phi_-,Phi_+) = o(n)"
  stuck_analysis:
    simplest_unproved_special_case: "one minimum-bisection optimizer plus one-flip-stable gauge with sublinear overlap/residual cost"
    nearest_fixed_d_solved: "Gheissari-Perkins-Yap 2025 below reconstruction"
    nearest_zero_temperature_solved: "Dembo-Montanari-Sen 2017 in the further d->infinity asymptotic"
    missing_ingredient: "quenched zero-temperature extremal-overlap control beyond reconstruction"
  section_I_choice: "prove the simplest unproved special case from (d)"
  next_methods: [15, 9, 19]
  next_obligation: "attempt (SC); if the second hard recovery also cannot produce movement or a certified obstruction, prepare the mandatory handoff/rotation rather than another global-gauge lemma"
  external_audits: "0/2 for current R14 C203/C205 line; this thinking run creates no closure claim"
```