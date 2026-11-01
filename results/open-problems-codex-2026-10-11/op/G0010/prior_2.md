Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum. NO MOVEMENT: `C_sub: 0 -> 0`; supported unchanged count `5 -> 6`; **STUCK RECOVERY 2 / thinking-only**; methods B15/B23/B29.

# G0010 — STUCK RECOVERY 2: from finite type kernels to a Perron-profile extremal problem

## 1. Source / exact target / status

**Native task.** `6aa7eca50c1c8191b3c26254b14d65fd`.

**Target.** G0010, HARD OUTSIDE.

**Primary source.** Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 2026-08-19, concluding tight-subcritical question (repository intake G0010; current web mirror labels the displayed question `question:tight subcritical`).

**Exact frozen source target.** For arbitrary finite `G`, with maximum degree `Delta(G)` and adjacency spectral radius `lambda(G)`, determine the tight typical all-regime upper scale of the largest component of Bernoulli bond percolation `G_p` under

\[
p\le \frac{1-\varepsilon}{\lambda(G)}
\]

for fixed `epsilon>0`, preserving the source's graph class, probability convention and all `(Delta,lambda)` regimes.

**Frozen metric.** `C_sub in {0,1}`. Before `0`; after `0`. It becomes `1` only after a source-valid matching theorem/counterexample settles the full all-regime question.

**Status after this run.** **OPEN / PARTIAL / STUCK RECOVERY 2 COMPLETE.** No theorem-sized claim is promoted in this report and no checker/artifact was manufactured. This run is deliberately the second and final thinking-only HARD recovery cycle.

## 2. Snapshot, continuity, ownership and history

Captured current `master` immediately before delivery:

`681ec029d4523a3b3fee34d97ee8a104ef2c4be9`.

Canonical exclusive claim:

`operations/claims/G0010.md`, blob `b62a5a64b2fde8f44efde5c3350452ebe83be0a2`.

Previous current-target report:

`proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T21-18-47Z__report.md`

creation commit

`4284d7910025b416c9e284ad9d9b92bdb3cdf41c`

readback blob

`b199296d65ca09ba7256680483bd2501dfef20e9`.

Path-scoped Git history at this run recovered the current G0010 chain and confirms there is no later G0010 report before this one:

1. `5f2f46d...` — refuted the static induced-spectrum envelope; finite trees isolate transient branching;
2. `fb35a76...` — sharp pointwise finite-horizon nonbacktracking growth bound and near-regular logarithmic wedge;
3. `5e5f0f8...` — exceptional-root `L^2` budget and overlap obstruction;
4. `f798506...` — STUCK RECOVERY 1, selected arbitrary biregular bipartite special case;
5. `4284d79...` — proved the selected biregular weighted two-type branching upper-tail theorem.

Repository-wide entrypoints read or reconciled this run: `operations/VISIBLE_FLEET_2026-09-16.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, the G0010 claim and path history, G-intake/source-verification material, and a neighboring current report from the same source (`G0011`, R7-07), which concerns the distinct long-cycle question and does not conflict with this claim.

`HISTORY_GAP`: none material for the present G0010 sequence. Shared ledgers remain coordinator-owned and were not edited.

## 3. Why STUCK RECOVERY 2 is binding

The source metric has remained `0` through five supported current-target runs. Recovery cycle 1 was already consumed at `f798506...`; its selected action was then executed successfully in the biregular class at `4284d79...`, but the full all-graph source obligation remained unchanged. Under the controlling HARD protocol this invocation must therefore be **STUCK RECOVERY 2 / thinking-only**. There is no recovery 3.

The exact source blocker is no longer a missing pointwise path count, a missing exceptional-root count, or a missing two-type branching estimate. It is:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
Control the extreme total progeny / component tail for every deterministic finite host from only `(n,Delta,lambda)`, while allowing an adversarial multiscale distribution of Perron weights and degree amplifications whose depth may grow with `n`.
\end{minipage}}
\tag{BLOCK-G0010}
\]

Equivalently: the proof needs a source-parameter extremal principle over **all feasible multiscale type profiles**, not a canonical finite-type kernel inferred from `(Delta,lambda)`.

## 4. Inventory of routes already tried and the precise failure of each

This section is an inventory, not new claims.

### Route A — static induced-subgraph adjacency spectra

A natural candidate was to optimize logarithmic subcritical scales over induced subgraphs using `p lambda(H)`. Finite regular rooted trees kill this route: all induced adjacency spectra can stay uniformly below the source threshold while a root-to-leaf percolation process remains supercritical for `Theta(log n)` generations and creates a polynomial-size component. The failure is **finite-horizon transient branching**.

### Route B — one finite Hashimoto/nonbacktracking spectral radius

For every finite tree the Hashimoto matrix is nilpotent, hence its spectral radius is zero, despite large nonbacktracking growth for `Theta(log n)` generations. The failure is again **finite horizon versus asymptotic spectral radius**.

### Route C — pointwise finite-horizon nonbacktracking growth

The exact recovered bound

\[
N_k^{\rm NB}(v)\le
\min\!\left\{
\Delta(\Delta-1)^{k-1},
\frac{\lambda^{2k}}{4^{k-1}}
\right\}
\]

solves the rootwise extremal growth problem up to the proved sharp prefactor. It does **not** solve the source because `C_max` is an extreme over many roots and because path mass may either spread through new vertices (tree mechanism) or collide repeatedly onto a small high-degree population (complete-bipartite mechanism).

### Route D — marginal exceptional-root tails

The spectral budgets

\[
\sum_v N_k(v)^2\le n\lambda^{2k}
\]

and their Markov tail bounds sharply control how many roots can have large one-horizon path mass. Stars, regular graphs and complete bipartite graphs already nearly saturate different portions of these inequalities. The failure is that a one-time marginal tail does not encode **transitions between exceptional sets at successive scales**.

### Route E — one collision/endpoint statistic

The endpoint effective count `E_k=N_k^2/Q_k` separates tree-like low-collision growth from complete-bipartite high-collision growth. But it remains a one-horizon statistic; it does not determine how a component moves from one amplification layer to another. The failure is **missing multiscale transition structure**.

### Route F — a universal two-type kernel

STUCK RECOVERY 1 selected arbitrary connected biregular bipartite hosts. That route succeeded completely inside the class: a collision-blind two-type Galton-Watson process with Perron weighting gives an explicit tail whose scale contains the correct high-degree burst `Delta/lambda` and high-side population `n/(1+(Delta/lambda)^2)`. The failure is not in the two-type proof. The failure is that a general graph has no source-controlled two-type partition and may have `Theta(log n)` materially different Perron scales, as finite trees already demonstrate.

### Route G — import known multitype/inhomogeneous-random-graph results verbatim

Turova's subcritical inhomogeneous-random-graph work and the 2026 Mörters--Schleicher preferential-attachment-kernel result can identify sharp largest-component scales because the type kernel / branching-random-walk geometry is **part of the model input**. G0010 is the adversarial inverse problem: only `(n,Delta,lambda)` is supplied, and the type geometry must be controlled uniformly over all deterministic hosts. The missing ingredient is exactly the kernel/profile extremal principle.

## 5. B15 — BREAK THE SYMMETRY: the minimal genuine three-type laboratory

The biregular proof has only two Perron/degree types. The first place where a new obstruction can occur is an equitable three-type chain

\[
V_0\longleftrightarrow V_1\longleftrightarrow V_2,
\]

with no `V_0--V_2` edges. If the cross-degrees are `r_{01},r_{10},r_{12},r_{21}`, edge balance gives

\[
|V_0|r_{01}=|V_1|r_{10},\qquad
|V_1|r_{12}=|V_2|r_{21}.
\]

After the standard population symmetrization, the type quotient has the Jacobi form

\[
J=\begin{pmatrix}
0&a&0\\
a&0&b\\
0&b&0
\end{pmatrix},
\qquad
a=\sqrt{r_{01}r_{10}},\quad
b=\sqrt{r_{12}r_{21}},
\]

and hence

\[
\lambda(J)^2=a^2+b^2.
\]

I am **not** promoting a new theorem here; this is the exact elementary quotient calculation used as a thinking device.

### Outcome of B15

The spectral budget is already not a scalar `worst type` budget: it can be split between two consecutive amplification channels. In a longer equitable chain, the corresponding symmetrized quotient is a weighted Jacobi path. This directly echoes the earlier finite-horizon nonbacktracking extremal calculation, where a one-dimensional weighted path was the sharp object.

This changes the target of the next proof attempt. A successful all-graph argument cannot merely find the single largest degree/Perron ratio and attach a multiplicity to it. It must prevent a **hierarchy of moderate amplifications** from compounding across many scales.

The simplest still-unproved special case is therefore:

> arbitrary finite connected equitable **three-type** hosts, with no randomness/pseudorandomness/girth assumptions, under the source subcritical condition, with an upper tail expressed only through the resulting global `(n,Delta,lambda)` rather than the hidden quotient parameters.

Two-type/biregular is solved internally; three types are the first genuine asymmetry.

## 6. B23 — assume the proposer did not give enough information for a canonical kernel

I deliberately assumed the opposite of the previous recovery plan: suppose there is **no canonical coarse transition kernel determined by `(n,Delta,lambda)`**.

That assumption is strongly supported by the existing exact calibration construction. For integer-admissible parameter pairs one can take a disjoint union of:

- a core carrying the mechanism of interest;
- a spectral calibration component fixing the global top eigenvalue;
- a maximum-degree calibration star fixing the global `Delta`;
- isolated vertices padding the order.

The first G0010 run already used this architecture to put finite-tree mechanisms at prescribed global `(Delta,lambda)`. The same calibration can coexist with a high-overlap/bipartite-style core whenever that core stays below the same caps. Therefore hosts with the same global source parameters can have radically different local transition geometries.

### Outcome of B23

This does **not** refute Question 5.2; the source asks for a tight **upper envelope** over such hosts. It refutes only a proof architecture that tries to reconstruct a unique multitype kernel from `(Delta,lambda)`.

The correct category is an adversarial extremal problem:

\[
\boxed{
\text{maximize the subcritical cluster extreme over all feasible type/profile geometries subject to the source caps.}
}
\]

Thus the unknown object is not `the kernel`; it is the **extremal feasible kernel/profile**.

## 7. B29 — add the zero-Perron boundary and compactify to a reversible profile

Let `A` be the adjacency matrix of a connected component with top eigenvalue `lambda`, and let `x>0` be a Perron vector. Define the Perron `h`-transform

\[
P(v,u)=\frac{A_{vu}x_u}{\lambda x_v}.
\]

The Perron equation makes `P` stochastic. It is reversible with stationary weights proportional to `x_v^2` because

\[
x_v^2P(v,u)=\frac{A_{vu}x_vx_u}{\lambda}
=x_u^2P(u,v).
\]

Define the local degree amplification

\[
a(v)=\frac{d(v)}{\lambda}.
\]

Then the elementary identity

\[
a(v)
=
\sum_u P(v,u)\frac{x_v}{x_u}
\tag{7.1}
\]

rewrites degree amplification as an exponential moment of the Perron-coordinate increment. If

\[
q(v)=\log\frac{x_{\max}}{x_v},
\]

then (7.1) is

\[
a(v)=\mathbb E_v^P\exp(q(X_1)-q(v)).
\tag{7.2}
\]

At the same time, at the source boundary `p=(1-epsilon)/lambda`, expected **Perron mass** of the children of a particle at `v` contracts exactly by `1-epsilon`:

\[
p\sum_{u\sim v}x_u=(1-\varepsilon)x_v.
\tag{7.3}
\]

Again, these are algebraic reparameterizations, not a promoted source theorem.

### Why this is the right compactification

- In a biregular graph, `q` has two levels and the previous two-type proof closes.
- In a complete bipartite graph, the two levels can be extremely separated, producing the burst/multiplicity mechanism.
- In a deep finite tree, `q` varies across many depth levels, producing the transient polynomial mechanism.
- If `G` is disconnected, a Perron vector for the top component is zero on lower-spectral components. In the `q` coordinate these vertices naturally sit at the added boundary point `q=+infinity`; one must then optimize componentwise over spectral levels `lambda_i<=lambda` rather than pretend one positive global Perron vector exists.

The minimal compact object is therefore not merely the empirical distribution of `(q,a)`. It must include the **reversible edge coupling** induced by `P`, because transition geometry matters. A candidate state variable is a probability law of

\[
(q(X_0),a(X_0),q(X_1),a(X_1))
\]

under stationary oriented Perron-edge sampling, with `q=+infinity` admitted as a boundary type for lower-spectral components in a global mixture.

### Outcome of B29

The source problem has been converted conceptually into a constrained variational problem over reversible multiscale environments. What remains missing is the inequality that turns the available constraints

- reversibility,
- `a(v)<=Delta/lambda`,
- the exponential-moment identity (7.2),
- finite population `n`,
- component spectral levels at most `lambda`,

into a sharp extreme total-progeny tail.

No existing G0010 route supplies that inequality.

## 8. A concrete refutation target distilled from the two known extremal mechanisms

The recovery must select a route for the next ordinary run. To make that route falsifiable rather than vague, I distilled the existing tree and hub mechanisms into one **candidate envelope**. This is explicitly **NOT A CLAIM** and must be attacked before any proof attempt.

Put

\[
c=1-\varepsilon,\qquad
w=\frac{\Delta}{\lambda},
\]

and use the already-proved finite-horizon exponential base

\[
b:=\min\left\{\Delta-1,\frac{\lambda^2}{4}\right\}.
\]

When `b>1`, define

\[
\alpha:=
\max\left\{0,
\frac{\log(cb/\lambda)}{\log b}
\right\};
\]

set `alpha=0` when `b<=1`.

The **refutation target** is the scale

\[
F_\varepsilon(n,\Delta,\lambda)
:=
\frac{\Delta}{\lambda}
\log\!\left(e+\frac{n\lambda^2}{\Delta^2}\right)
+
n^{\alpha}.
\tag{8.1}
\]

Why this is worth trying to break:

- the first term is the two-type/hub heuristic: burst scale `w=Delta/lambda`, with at most order `n/w^2` genuinely high-amplification launch sites according to the earlier spectral degree budget;
- the second term is the deep-tree heuristic: host volume grows at the sharp nonbacktracking base `b`, while an open tree frontier grows at base `cb/lambda`, giving exponent `log_b(cb/lambda)` when that base exceeds one;
- regular graphs have `w=1` and `alpha=0`, leaving a logarithmic scale;
- stars give the expected square-root burst order;
- the source benchmark `K_{s,s^3}` gives a hub term of order `s log s`, while the tree term is only order `s`;
- finite regular-tree calibrations produce the polynomial `n^alpha` term;
- both pieces are consistent with, but much more structured than, the source's unconditional `O(sqrt(n))` ceiling.

These checks are **diagnostics only**. A three-type or longer hierarchical host may beat (8.1) by chaining moderate amplifications in a way neither primitive term captures. That is exactly what the next run must test.

## 9. What a full proof would need that no route currently contains

A source-closing proof must provide all of the following simultaneously:

1. **A multiscale extremal principle.** Show that any deterministic host profile consistent with `(n,Delta,lambda)` is dominated, for the relevant cluster extreme, by an explicit extremal profile or by a computable envelope.
2. **Depth and overlap in one inequality.** The inequality must reduce to transient tree growth when endpoint collisions are negligible and to hub multiplicity when many paths reuse a small low-side population.
3. **Extreme-value accounting.** It must control not merely one root or a uniform root, but the maximum over all launch vertices with the correct multiplicity penalty.
4. **No hidden kernel assumption.** The construction cannot assume a bounded number of types, degree regularity, expansion, girth, or a supplied inhomogeneous-random-graph kernel.
5. **Matching lower families.** Once an upper scale is proposed, explicit graph sequences must match it throughout the parameter regimes required by the source, not only at the regular/tree/bipartite corners.

No route so far contains item 1; all earlier failures are manifestations of that absence.

## 10. Nearest solved analogues and the missing ingredient

### Turova — subcritical inhomogeneous random graphs

Tatyana Turova, *The Largest Component in Subcritical Inhomogeneous Random Graphs*, CPC 20 (2011), and her later general inhomogeneous work derive exact logarithmic largest-component asymptotics through the branching process associated with a **known type kernel**. The kernel specifies the type transition law and makes the progeny large-deviation problem explicit.

### Mörters--Schleicher — preferential-attachment-type kernel

Peter Mörters and Nick Schleicher, *The largest subcritical component in inhomogeneous random graphs of preferential attachment type*, published online 2026-03-04, obtain a polynomial largest-component exponent via a killed branching-random-walk approximation. Again, the spatial/type kernel and its geometry are given as part of the model.

### What G0010 lacks

G0010 supplies only a deterministic host through `(n,Delta,lambda)`. The type law, Perron profile, overlap geometry and finite-horizon transition structure are adversarial. The missing ingredient is therefore an **extremal theorem over kernels/profiles**, not another application of a known-kernel branching theorem.

## 11. Section-I choice after STUCK RECOVERY 2

Exactly one recovery action is selected:

### **REFUTE INSTEAD OF PROVE**

The next ordinary G0010 run must attack the candidate envelope (8.1) before trying to prove it. The primary counterexample laboratory is the smallest genuinely irregular hierarchy:

- equitable three-type chains and forks;
- then `k`-layer weighted/Jacobi-type block graphs with `k` allowed to grow slowly with `n`;
- calibrate global `(n,Delta,lambda)` exactly or asymptotically without changing the percolation mechanism;
- test whether chained moderate amplifications can exceed both the hub term and the tree term in (8.1).

If a counterexample exists, the run should identify the missing third mechanism rather than patch constants. If the candidate survives an honest adversarial search, only then should the same run attempt to identify the inequality needed for an upper bound.

The next three Section-B methods are deliberately unused on G0010 so far:

- **B16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE:** enumerate small symmetrizable/equitable quotient matrices analytically or exactly enough to see whether three-type hierarchies beat the two-mechanism envelope;
- **B5 — ADD A PARAMETER AND DIFFERENTIATE:** introduce a continuous spectral-budget split parameter between consecutive amplification channels and determine whether the worst case sits at a tree endpoint, a bipartite endpoint, or an interior hierarchy;
- **B26 — HUNT THE SPORADIC CASE:** search for a non-monotone three/four-type pattern that defeats both obvious extremizers.

Recovery cycles consumed after this report: **2 of 2**. There is **no STUCK RECOVERY 3**. After the selected refutation action, the next qualifying stuck event with unchanged `C_sub`/remaining obligation requires a preserved terminal handoff and in-place successor rotation under the controlling protocol.

## 12. Dated source / current / later / citing checks

Checks performed 2026-09-17 UTC / 2026-09-18 Asia/Jerusalem:

1. **Original/current source.** arXiv `2608.19145` still presents v1 by Christoph--Morawski--Wigderson, submitted 2026-08-19. The abstract still states the general subcritical `O(sqrt(|G|))` result.
2. **Exact open question.** A current open-problem mirror reproduces the tight-subcritical question: for prescribed `Delta(G)` and `lambda(G)`, determine the tight typical largest-component upper bound under `p <= (1-epsilon)/lambda(G)` across all regimes.
3. **Later title/author/follow-up searches.** Bounded searches for the exact title, arXiv ID, authors plus `tight subcritical`, and later 2026 follow-up did not recover a later source-matching resolution. This is negative evidence only, not an openness/novelty certificate.
4. **Nearest literature.** Turova's 2011 rank-one result and later general inhomogeneous work solve known-kernel analogues; Mörters--Schleicher (CPC 2026) solve a preferential-attachment-type kernel with polynomial subcritical components using killed branching random walks. These do not settle the deterministic all-host `(Delta,lambda)` extremal problem.
5. **Neighbor same-source track.** R7-07/G0011 works the distinct long-cycle question from the same paper and has no ownership overlap with G0010.

Search phrases included exact title / arXiv ID, `tight subcritical percolation spectral radius maximum degree largest component`, and `largest subcritical component multitype branching kernel`.

No novelty claim is made for any algebraic reparameterization or candidate envelope in this report.

## 13. Model / scheduler interface status

The exposed scheduler/task-update interface still provides task title, prompt, schedule/timing mode and enabled state, but no authenticated model-family field and no reasoning-effort field. Therefore `GPT-6 / maximum` remains a prompt request only; this run must and does report the actual exposed model as GPT-5.6 Sol with reasoning level UNVERIFIED.

Changing this requires a platform/product surface that exposes an owner-authorized model selector and reasoning-effort selector for scheduled tasks, or platform support changing the scheduler capability. Prompt text alone cannot authenticate the runtime choice.

The repository also preserves the distinction between historical `You cannot modify this task` denials in one context and successful updates from other authorized contexts. The only valid workaround for a genuine modification denial is the task's owning authorized context or platform/admin support. Do not duplicate the schedule, change access, or bypass permissions.

## 14. Artifacts / checks

No new artifact and no checker were created. This is intentional: STUCK RECOVERY 2 is a thinking-only run, and no finite claim here warranted certification. The only new file is this immutable report.

## 15. `ledger_delta`

```yaml
ledger_delta:
  native_task_id: 6aa7eca50c1c8191b3c26254b14d65fd
  target_id: G0010
  report_kind: STUCK_RECOVERY_2_THINKING_ONLY
  input_snapshot_sha: 681ec029d4523a3b3fee34d97ee8a104ef2c4be9
  previous_report_path: proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T21-18-47Z__report.md
  previous_report_commit: 4284d7910025b416c9e284ad9d9b92bdb3cdf41c
  exact_source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 tight-subcritical question
  metric: C_sub
  metric_before: 0
  metric_after: 0
  supported_unchanged_count_before: 5
  supported_unchanged_count_after: 6
  hard_recovery_cycle: 2_of_2
  methods:
    - B15: three-type/Jacobi laboratory shows spectral budget can split across consecutive amplification channels; finite two-type summaries are structurally insufficient
    - B23: same global source parameters can support incompatible local mechanisms after calibration; abandon canonical-kernel reconstruction in favor of an extremal envelope
    - B29: Perron h-transform/reversible profile exposes the missing multiscale environment and the zero-Perron boundary for lower-spectral components
  exact_blocker: extremal total-progeny/component tail over all multiscale Perron/degree profiles consistent with n, Delta, lambda
  selected_section_I_action: REFUTE_INSTEAD_OF_PROVE
  next_refutation_target: F_epsilon(n,Delta,lambda) = (Delta/lambda) log(e+n lambda^2/Delta^2) + n^alpha, with alpha=[log((1-epsilon)b/lambda)/log b]_+ and b=min{Delta-1,lambda^2/4}; CANDIDATE ONLY
  next_methods: [B16, B5, B26]
  mathematical_status: PARTIAL_SOURCE_OPEN
  source_closed: false
  audit_refs: []
  artifact_refs: []
  shared_ledgers_edited: false
  email_drive_public_posting: false
  note: No recovery 3. After the selected refutation action, the next qualifying stuck event requires terminal handoff and in-place successor rotation.
```
