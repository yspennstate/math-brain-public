Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `epsilon_bridge: 1/14,469,504 -> 1/14,469,504`; supported unchanged count `4 -> 5`; **STUCK_RECOVERY_2 / thinking-only**. Methods actually tried: **#11 DUALIZE, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: stuck recovery 2, transport duality and the alternating-flow lift that a successful switching proof would need

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`. Source-level status: **PARTIAL / OPEN in the current repository scope**. This report makes **no new source-level theorem claim**, does not improve the frozen bridge exponent, and intentionally creates no checker-only artifact. It executes the second and final hard-target recovery allowed on I0036.

## 1. Continuity, mandatory repository read, source status, and ownership

I continued from the newest immutable R16 report

`runs/R16/2026-09-17T15-47-43Z_i0036-rank-only-random-switching-no-go_7c4e.md`,

which preserved

\[
B_T\le 1000\,T^{-1/14,469,504}\qquad(T\ge1)
\]

and advanced the supported unchanged streak to `4`. That report explicitly required the **next** R16 invocation to be `STUCK_RECOVERY_2 / thinking-only` and recommended the non-immediate triple `#11,#14,#25`. I follow that instruction here; this is not another opportunistic lemma run.

Before research I recovered/read the current control and research state required by the owner:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- exclusive create-only claim `operations/claims/I0036.md`;
- the newest R16 report and the preceding R16 recurrence, weighted-pigeonhole, renewal, phase/Fourier, `n->0`, and first-stuck-recovery reports;
- the neighboring planar-SAW R11 stuck report and its Krachun--Panagiotis comparison;
- current R13/R12/P26 records around the now-claimed Guo--Fang--Lu Boolean Komlos theorem.

The large intake JSONL corpus cannot be rendered byte-for-byte in one connector response. I used the repository search surface to recover the exact I0036 source/claim and relevant neighboring history and do not pretend connector truncation is a literal reread of every historical intake row.

I0036 remains **R16 exclusive / ADMITTED_ACTIVE / HARD_OUTSIDE**. Its source is Oded Schramm, ICM 2006, Problem 2.1, arXiv:math/0602151: for the infinite half-plane SAW obtained from the `n -> infinity` limit of uniform `n`-step SAWs, prove that the law of `s gamma` has a limit as `s downarrow 0` and that the limit is `SLE_{8/3}`. Schramm explicitly notes that the hexagonal lattice may be easier.

Fresh dated source navigation again found Krachun--Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, **Annals of Probability 54(3) (2026), 1109--1125**, published 31 May 2026, DOI `10.1214/24-AOP1730`, as the directly relevant peer-reviewed quantitative fixed-lattice baseline: `O(n/log n)` sub-ballisticity with high probability and polynomial critical bridge decay. A bounded search did not locate a later source-matching proof of Schramm Problem 2.1. That negative search is not a worldwide openness or novelty certificate.

## 2. Frozen metric and second stuck trigger

The R16 metric remains

`epsilon_bridge` = the largest explicit `epsilon>0` for which R16 has a complete proof in the Krachun--Panagiotis critical honeycomb normalization that

\[
B_T\le C_\varepsilon T^{-\varepsilon}
\qquad\text{for every integer }T\ge1
\]

with explicit finite `C_epsilon`.

Before:

\[
\varepsilon_{\rm bridge}=\frac1{14,469,504}.
\]

After:

\[
\boxed{\varepsilon_{\rm bridge}=\frac1{14,469,504}.}
\]

There is **no movement**. The supported consecutive unchanged count is now `5`. The first hard-target recovery was the Fomin-style switching recovery at count `3`; the intervening substantive attack eliminated every rank-only randomized switch rule while leaving geometry-dependent switching alive. Therefore this report is the required **second and final** recovery on I0036.

All thirty Section-B labels have already appeared somewhere in the I0036 history, so a literally never-before-used label is impossible. The present triple `#11,#14,#25` does not repeat the immediately preceding `#7,#9,#19`, and the mathematical route below is genuinely different.

## 3. (a) Exact blocking statement — bounded-congestion geometry-aware transport

The preceding run sharpened the surviving route to geometry-dependent switching. I now state the blocker in the form that exposes exactly what must be proved.

Fix a finite simply connected honeycomb domain `D` with cyclic pendant boundary terminals `a,b,c,d`. Let `S` be the finite set of ordered **opposite-connectivity** source pairs

\[
s=(P,Q),\qquad P:a\to c,\quad Q:b\to d,
\]

where both paths are SAWs. Let `T` be the union of the two **adjacent-connectivity** target-pair sets

\[
(a\to b,c\to d)\qquad\text{and}\qquad(a\to d,b\to c).
\]

For each source `s`, let `A(s)` be the allowed geometry-aware switch-and-loop-erase actions. An action `u in A(s)` produces a target pair `f(s,u) in T` and never increases total length. Write

\[
r(s,u)
:=x_c^{\,|s|-|f(s,u)|}\in(0,1],
\qquad
x_c=\frac1{\sqrt{2+\sqrt2}}.
\]

A fractional geometry-aware selector chooses `p_{s,u}>=0` with `sum_{u in A(s)} p_{s,u}=1`. Its normalized load on target `t` is

\[
L_t(p)
=
\sum_{s\in S}\sum_{u\in A(s):f(s,u)=t}
 p_{s,u}\,r(s,u).
\]

Define the optimal congestion

\[
\boxed{
C_D^*
:=
\inf_p\ \max_{t\in T}L_t(p).
}
\tag{BLOCK}
\]

The exact missing statement is

\[
\boxed{\sup_D C_D^*<\infty,}
\tag{3.1}
\]

ideally with `C_D^*<=1` for every `D`.

Why this is the right blocker: multiplying the capacity inequality for each target by its critical weight and summing over all targets would give

\[
S_{ac}(x_c)S_{bd}(x_c)
\le C\Bigl(
S_{ab}(x_c)S_{cd}(x_c)
+S_{ad}(x_c)S_{bc}(x_c)
\Bigr).
\tag{3.2}
\]

Thus bounded congestion is precisely the geometry-aware transport statement needed by the current four-terminal gluing route. Conversely, the earlier rank-only obstruction shows that `p` cannot depend only on the number/rank of intersections.

This report does **not** claim (3.1) or (3.2).

## 4. (b) Every substantive I0036 route tried so far, and why it stops

### Route 1 — published fifth-power bridge recurrence

The first I0036 run repaired the statement/application mismatch around the Krachun--Panagiotis recurrence and improved the published explicit exponent `10^-10` to `9*10^-10`.

**What it taught:** there was real slack in the published constants.

**Why it stops:** it is still a vertical bridge-partition estimate. It does not control lateral excursions or annulus crossings.

### Route 2 — retain the original quadratic/cubic dichotomy

Instead of collapsing the source inequalities into the coarser fifth-power recurrence, R16 retained the denominator ratios in the original alternatives. Large denominator drop or small-ratio recurrence both close the induction. This moved the exponent to `1/42,000,000`.

**Why it stops:** the method still only changes the bridge-height exponent; the constants are tiny and there is no new geometric observable.

### Route 3 — threshold invariant / one-threshold block optimization

R16 introduced the invariant `theta=M epsilon` and a free ratio threshold `lambda`, moving the exponent to `1/18,817,988`. The same analysis showed the one-threshold architecture has an internal ceiling of order `5.6*10^-8`, and that the then-current exponent was already close to that ceiling.

**Why it stops:** tuning that architecture cannot produce a qualitative change, and even a larger vertical exponent would not itself imply tightness or conformal invariance.

### Route 4 — weighted logarithmic-scale pigeonhole

A nonuniform distribution over the logarithmic bands exploited scale-dependent slack and moved the frozen metric again to

\[
\boxed{\varepsilon_{\rm bridge}=1/14,469,504.}
\]

**Why it stops:** it improves the scalar bridge observable but still does not control a single irreducible bridge's horizontal shape.

### Route 5 — renewal-height / SLE dictionary

The bridge bound was converted into renewal-height information for the irreducible-bridge process, and the conjectural SLE bridge exponent was matched to the stable-subordinator picture.

**Why it stops:** renewal points constrain vertical progress. A single irreducible bridge can make many lateral excursions between successive renewal heights.

### Route 6 — finite-strip transfer operator and parafermionic phase sectors

For a fixed strip, transfer-matrix rationality gives exponential tails below the strip radius. The missing quantitative object is a width-uniform critical spectral gap. The parafermionic winding phase lives in a nontrivial Fourier sector of `Z/48Z`.

**Why it stops:** an exact finite obstruction shows that nontrivial Fourier modes cannot control the positive invariant `k=0` mass. Indeed, even all 47 nontrivial sectors are blind to adding a uniform phase component; the corresponding all-ones-matrix model changes the Perron root while leaving every nontrivial block unchanged.

### Route 7 — `n -> 0` two-defect O(n) deformation

R16 identified the two-defect ratio as the correct `n -> 0` object and differentiated it. The derivative is a positive weighted mass of closed loops intersecting the open SAW, hence a genuine `k=0` geometric observable.

**Why it stops:** the established `O(n)` box-crossing/gluing route uses FKG in the `n>=1` regime. The required lattice condition fails below that threshold, and a fixed local multiplicative quasi-FKG defect tensorizes exponentially, so there is no scale-uniform continuation to `n=0` by merely paying a constant slack.

### Route 8 — same-total-length four-terminal switching

`STUCK_RECOVERY_1` attacked a direct Ptolemy-type switching inequality. Exact enumeration on a seven-vertex planar subcubic witness showed that the opposite-pair coefficient at total length 15 is nonzero while the adjacent-pair coefficient at that same total length vanishes.

**Why it stops:** no universal coefficientwise / total-length-preserving injection exists. Shortening has to be allowed.

### Route 9 — Fomin-style loop erasure with rank-only randomization

The post-recovery attack allowed shortening, randomized the chosen intersection, and solved the entire rank-only rule class on the same witness. Every rule depending only on `(number of intersections, rank)` has a target fiber of load at least

\[
\frac{6-\sqrt2}{4}>1,
\]

and independent iteration of that fixed defect blows up exponentially. On the same finite witness, however, a geometry-dependent deterministic selector achieves max load at most one.

**Why it stops:** the finite success has no known scale-uniform extension. The surviving question is exactly (BLOCK).

These routes collectively show that the remaining problem is not another scalar constant optimization. It is the absence of a **positive, geometry-sensitive, scale-stable switching/transport mechanism**.

## 5. #11 DUALIZE — replace selector construction by a target-price adversary

For each fixed finite domain `D`, (BLOCK) is a finite linear program. Standard finite LP duality rewrites it in the following working form. Let `Delta(T)` be the simplex of nonnegative target prices `beta_t` with `sum_t beta_t=1`. Then

\[
C_D^*
=
\max_{\beta\in\Delta(T)}
\sum_{s\in S}
\min_{u\in A(s)}
\beta_{f(s,u)}\,r(s,u).
\tag{5.1}
\]

This is an exact reformulation of the finite selector problem, not a new source-level theorem.

The value of (5.1) is conceptual. A direct proof tries to coordinate all source choices simultaneously so that no target is overloaded. The dual instead says: **give an adversary any distribution of prices on adjacent-pair targets; for each source pair, use its actual planar geometry to choose a cheap switch; then bound the total cheapest price.**

This is the first formulation in the R16 history where erased-loop reconstruction does not have to be controlled one target fiber at a time. A successful proof can attack arbitrary `beta` by a geometric charging argument.

It also exposes a falsification route for the next ordinary run: finite exact LPs on growing honeycomb domains can search directly for dual price vectors whose value grows with scale. If such prices are found, the current transport architecture dies without spending more runs on ad hoc selectors. If the extremal prices localize on a small number of alternating bottlenecks, that localization points to the missing combinatorial inequality.

## 6. #14 FIND THE GROUP ACTING — why a pure switching group is insufficient, and what must be lifted

A pair of colored paths naturally suggests toggling colors along alternating pieces of their union. In random-current and planar-flow proofs this produces a genuine switching group. Here the previous exact obstruction already tells us something stronger:

> Any **pure** recoloring group that preserves the same underlying edge multiset also preserves total path length, and therefore cannot by itself establish the desired SAW inequality in all domains, because the coefficientwise same-length switching statement is already false.

So the right algebraic object cannot be a group acting only on undecorated SAW pairs.

The useful lift is instead:

\[
\boxed{\text{SAW pair}\quad\longrightarrow\quad
\text{adjacent-pair skeleton + explicit erased/reconstruction decoration}.}
\tag{6.1}
\]

On the **decorated** state space, one can hope that alternating-component toggles become invertible, exactly as loop-erased switching is invertible only when the pre-erasure walk information is retained. Projection back to a pure SAW pair then forgets decoration and gains critical weight because erased edges disappear.

This clarifies the real obstacle: the group action is not the hard part. The hard part is to prove a **uniform bound on the total critical weight of decorations above one undecorated target**, or an equivalent dual-price bound. At criticality arbitrary loop decorations cannot simply be assumed summable; their multiplicity is precisely the information that ordinary SAW throws away.

The honeycomb degree-three geometry suggests using the alternating decomposition of the two-color union/symmetric difference as the state variable, but I do **not** claim here that this decomposition already yields a closed switching identity. The next attack has to verify the exact boundary pairing, common-edge bookkeeping, and decoration multiplicity in the intended domain class before promoting any such statement.

## 7. #25 COUNT THE SAME THING TWICE — the Pluecker/alternating-flow shape and the missing projection estimate

The desired four-terminal inequality (3.2) has the same **shape** as a positive Pluecker/Ptolemy relation. This is not enough by itself: the products `S_{uv}S_{rs}` count two SAWs that may intersect, while planar-network Pluecker identities normally arise from an ensemble whose switching state space is already closed.

The nearest useful double-counting template is therefore:

1. lift an opposite-connectivity SAW pair to a decorated alternating object;
2. count/recolor the same decorated object in the adjacent pairing;
3. project away the decoration;
4. pay a controlled factor for all decorations that project to the same target pair.

At the level of critical weights the hoped-for estimate has the schematic form

\[
\sum_{\mathcal E:\,\pi(t,\mathcal E)=t}
 x_c^{\,|\mathcal E|}
\le C
\tag{7.1}
\]

for the **actual admissible erased/reconstruction data**, uniformly in domain and scale. Equation (7.1) is schematic, not a proved bound; the exact decoration variable has not yet been defined.

This perspective also explains why the preceding pure-group idea cannot be enough. A same-union/same-length double count would contradict the finite coefficientwise obstruction. Some monotone simplification—loop erasure, deletion of doubled segments, or another weight-gaining projection—must accompany the alternating switch.

## 8. (c) What a proof must contain that no route so far contains

A successful source-relevant route now needs **all three** of the following in the same argument:

1. **positivity in the trivial sector:** the mechanism must act directly on positive SAW mass, not infer it from winding Fourier modes;
2. **geometry-aware switching:** the choice must see the actual alternating path/domain structure, not only intersection count or rank;
3. **scale-stable closure:** erased/reconstruction data must have a uniformly bounded total critical weight, or the LP dual must be bounded uniformly over all target price vectors and all scales.

Fomin-style walk switching has (2) and an enlarged state that remembers erased information. The planar Ising/random-current setting has (1)--(3) through double currents and alternating flows. Ordinary critical SAW has neither a Markovian walk reservoir nor current multiplicities available for free. That is the missing ingredient.

Even if (3.1) were proved, a further annular iteration would be needed to get multi-crossing/tightness estimates, and then a separate identification argument would still be needed for `SLE_{8/3}`. Thus this recovery does not overstate what the switching route would accomplish.

## 9. (d) Simplest special case still unproved

The next special case should test the alternating-skeleton idea without requiring arbitrary nested decorations.

For a source pair `s=(P,Q)`, consider the mod-two symmetric-difference support of the two paths. The selected special case is:

> **Cycle-free alternating-skeleton case.** Restrict the source sum in (3.2) to opposite-connectivity pairs for which the mod-two symmetric-difference support has **no cycle component**. Prove the resulting critical four-terminal inequality with `C=1`, or equivalently construct a capacity-one geometry-aware fractional selector for this restricted class.

No such statement is claimed proved here. It is chosen because it is the first class in which alternating recoloring should have minimal decoration complexity while still testing common-edge/intersection bookkeeping. If even this restricted LP has congestion above one on a small honeycomb domain, the alternating-flow lift needs a different invariant before any full-domain attempt.

The next ordinary run should therefore either solve this restricted class or produce an exact finite dual obstruction to it; it should not optimize the bridge exponent again.

## 10. (e) Nearest solved problems and the ingredient they possess

### Fomin: loop-erased walks and total positivity

Sergey Fomin, *Loop-erased walks and total positivity*, arXiv:math/0004083 (2000), proves total nonnegativity for planar **walk** matrices and explains the positivity combinatorially using loop-erased walks. The crucial distinction from the present SAW product is that the ambient ensemble contains general walks: erased information lives in the underlying walk state, so the switching mechanism has a reservoir from which it can reconstruct multiplicity.

### Lis: planar Ising total positivity via currents / alternating flows

Marcin Lis, *The Planar Ising Model and Total Positivity*, J. Stat. Phys. 166 (2017), 72--89, proves total nonnegativity of boundary two-point correlation matrices. The proof uses a distributional relation between **double random currents** and **random alternating flows**. In other words, the model has an enlarged positive state space naturally closed under the relevant switching operation.

### Krachun--Panagiotis: nearest solved quantitative fixed-lattice SAW analogue

Krachun--Panagiotis provide the strongest source-model quantitative input currently in R16: explicit polynomial bridge decay and `O(n/log n)` sub-ballisticity on the hexagonal lattice. Their argument does not provide the four-terminal positive switching structure isolated here.

The lesson is precise: the nearest switching proofs do not avoid reconstruction multiplicity; they **encode it in a larger positive ensemble where switching is closed**. Porting that feature, rather than another particular choice of intersection, is the selected second recovery.

## 11. Exactly one recovery selected

Per the hard-task protocol, I choose exactly one recovery:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.}}
\]

Concretely, the next substantive I0036 attack should try to construct a **decorated two-color SAW / alternating-flow lift** inspired jointly by Fomin and Lis, with the LP dual (5.1) as its falsifiable target. The first milestone is the cycle-free alternating-skeleton special case from section 9, not the full scaling limit.

The next non-immediate method triple recorded for that attack is **#18 SAY IT IN ANOTHER LANGUAGE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT**:

- **#18:** rewrite the restricted four-terminal transport as a positive-network/Pluecker problem on the decorated state space;
- **#20:** identify whether projection multiplicity or critical decoration mass is the first failure;
- **#24:** use the LP dual to identify the extremal target-price vector/domain bottleneck rather than guessing a selector.

This is **STUCK_RECOVERY_2**, the second and final recovery permitted on I0036. If, after the recovery route is tested, a **third stuck episode** occurs under the owner's rule, R16 must leave an I0036 handoff and rotate to a source-checked eligible HARD outside target. There will be no `STUCK_RECOVERY_3` on I0036.

## 12. Stale Beck--Fiala title — fresh status and corrected audit count

The native task title remains Beck--Fiala, but current repository continuity has already moved R16 to I0036. The fresh source comparison is now stronger than the wording in some earlier R16 reports:

- Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` order in the regime `t>=log^2 n`, with a weaker small-`t` bound. Their result alone does **not** settle the full uniform target.
- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted **10 September 2026**, state the real Boolean Komlos theorem
  \[
  \Bigl\|\sum_j\varepsilon_jv_j\Bigr\|_\infty<3\sqrt{2\pi}
  \]
  for arbitrary Euclidean-unit real vectors, and explicitly deduce
  \[
  \operatorname{disc}(A)<3\sqrt{2\pi t}
  \qquad\text{for every integer }t\ge1,
  \]
  with no restriction on `n`.

The repository now contains **two distinct full mathematical audits of the exact universal Komlos theorem package**: R12 `R12-AUDIT-R13-KOMLOS-01 = PASS`, and P26's 17 September 2026 end-to-end audit in

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_04-57-55__run-report.md`.

P26 explicitly records the mathematical statement as a **current-literature resolution claim**, the fleet package as **2/2 independently audited**, and external maturity as **preprint v1 / not treated as refereed validation**. The Beck--Fiala bound is a scaling corollary of that audited theorem rather than a separate package.

Accordingly, R16 does not reopen the stale Beck--Fiala target. The honest current description is: **full uniform Boolean Beck--Fiala bound claimed by a 10 September 2026 primary preprint and supported by two independent fleet audits; external refereeing/mature consensus not asserted**.

## 13. Model / scheduler control and the P26 permission issue

The control limitation remains unchanged. The exposed scheduler mutation interface has prompt/title, schedule or relative start, timing mode, enablement, and task identity. It has **no model-family selector and no reasoning-effort selector**, and it provides no authenticated applied-model/applied-effort telemetry or guaranteed hour-long execution.

Therefore GPT-6/maximum can be requested only in prompt text here. Actual enforcement would require an authorized product/workspace scheduler or API exposing those selectors plus authenticated runtime telemetry.

The repository's reconciled deployment record says the earlier P26 `You cannot modify this task` failure was authorization-context-specific: a later authorized P/C context successfully updated P26, while another context denied R-series edits. The compliant workaround is the owning account/workspace context or platform support. Permission bypass and duplicate scheduling are prohibited.

No scheduler state was changed in this run.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  lane: HARD_OUTSIDE
  canonical_target: I0036
  source: "Schramm ICM 2006 Problem 2.1; fixed-lattice half-plane SAW scaling limit to SLE_8/3"
  ownership: "operations/claims/I0036.md; R16 exclusive"
  status: PARTIAL_OPEN
  metric: epsilon_bridge
  before: "1/14469504"
  after: "1/14469504"
  constant: 1000
  movement: false
  supported_unchanged_count_before: 4
  supported_unchanged_count_after: 5
  stuck_recoveries_used_before: 1
  stuck_recoveries_used_after: 2
  stuck_state: STUCK_RECOVERY_2
  run_role: "thinking-only second/final recovery"
  methods: [11, 14, 25]
  exact_blocker: "uniform bounded congestion sup_D C_D^* < infinity for geometry-aware switch-and-loop-erase transport"
  new_source_level_claims: none
  new_finite_claims: none
  checker_created: false
  recovery_choice: "port nearest solved technique: Fomin/Lis decorated alternating-flow switching"
  simplest_unproved_special_case: "cycle-free symmetric-difference source pairs; capacity-one critical four-terminal transport"
  next_methods: [18, 20, 24]
  next_protocol_action: "test recovery route; on a later third stuck episode, hand off I0036 and rotate; no third recovery"
  beck_fiala_refresh: "Guo-Fang-Lu arXiv:2609.11189v1 claims full real Boolean Komlos and disc(A)<3 sqrt(2 pi t) for all t,n; R12 and P26 distinct end-to-end audits PASS; external maturity remains preprint-v1"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
  email_or_drive: false
  closure: false
```

No shared root ledger, peer-track file, email, Drive content, public post, purchase, permission, workflow, or scheduler state was modified. This immutable R16 report is the only repository write for the run.