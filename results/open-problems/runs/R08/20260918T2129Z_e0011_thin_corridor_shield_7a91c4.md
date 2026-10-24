Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b8 -> B_cat >= b9`, exact `b9>b8`; diagnostic `log10(b9/b8)=38.842224585252836`. Unchanged count remains `0`. Methods actually used: B9, B20, B28.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: thin-corridor regeneration with a generated terminal shield

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active source target: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, **without added stirring**.

## 1. Continuity, exclusions, ownership, and current-source check

I did **not** reopen the native-title Hasebe--Ueda Problem 3.11 (`I0082`). Its controlling R08 handoff froze the explicit-candidate metric at `2/3` after six unchanged supported runs; `operations/claims/E0011.md` records I0082 as `RETIRED/FROZEN`. The old R08 FPP strict-convexity line remains retired from this slot as well.

The active exclusive claim is still `E0011`, owned by R08. Its frozen metric is

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite 1-dependent two-child Harris-block certificates at the rational anchor `p=1/2`, and `b(C)` is a rigorous lower bound on the good-block probability. The current sufficient closure threshold for this track remains `>63/64`, followed by the written oriented-percolation comparison and continuity in `p`.

Before new research I refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the controlling owner directive, `operations/claims/I0082.md` and `operations/claims/E0011.md`, the newest complete R08 report, and the newest neighboring R07/R09 reports. I also target-searched the intake/attempt material and repository for `I0082`, `E0011`, Durrett Problem 5, no-stirring catalyst/ZGB, and duplicate ownership. The very large intake mirrors were queried by exact target rather than literally rendered line-by-line through the connector; I do not claim a byte-for-byte reread of every unrelated intake row.

The immediately preceding R08 report is

`runs/R08/20260918T2029Z_e0011_asymmetric_regeneration_b4e7c1.md`,

which proved

\[
B_{\rm cat}\ge b_8,
\qquad
\log_{10} b_8\approx -99.23646137647626,
\]

using B3/B15/B24. The present triple B9/B20/B28 is different.

I refreshed the primary/current literature screen on 2026-09-18. Durrett's 2009 source still presents nine challenging open problems. Current searches for the exact no-stirring catalyst/ZGB coexistence target, later rigorous catalyst results, and 2025--2026 ZGB work recovered the source and modified/simulation literature but no later primary theorem closing this exact Problem 5. This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Idea before code

The previous certificate already removed the eraser and one planter, but it still paid eighteen local vacancy-expander successes because it transported a **four-row** empty corridor. The new idea is more structural:

> Transport only a two-row vacancy cursor. Preserve the parent species as the left child. Near the right endpoint, create only the four extra guard vacancies actually needed by the child planter, using two rotated local expanders. Then plant only the new right child.

This reduces the repeated-expander count from eighteen to eleven. The same run also replaces repeated worst-case conditioning by a generated shield condition: after the first successful horizontal stage, two cells behind the cursor are known vacant from the block's own history, so later stages need not minimize over boundary states that are no longer reachable.

## 3. B20 — identify the exact algorithmic waste

Normalize the new parent seed to

\[
C_0=\{(0,0),(0,1),(1,0),(1,1)\}
\]

vacant, together with

\[
O:\ (-3,0),(-2,0),
\qquad
CO:\ (-4,1).
\]

The occupied roots are stable: the CO root is not adjacent to either oxygen root. The occupied parent lies outside every horizontal expander's accepted read/write support and is included in every local protected set, so it survives on the good event and becomes the left child.

For horizontal propagation use the exact seven-label `2 x 2 -> 2 x 3` vacancy expander from the preceding R08 chain. Nine horizontal advances grow the two-row empty corridor from columns `0,1` through columns `9,10`.

The child translated by `L=9` should have

\[
O:\ (6,0),(7,0),
\qquad
CO:\ (5,1),
\qquad
C_9=\{9,10\}\times\{0,1\}.
\]

The two-row corridor alone does not leave the complete final planter support vacant. Exactly four additional guard cells are needed:

\[
G=\{(6,-1),(7,-1),(5,2),(6,2)\}.
\]

After the horizontal corridor has been generated, one downward and one upward rotated `2 x 2 -> 2 x 3` expander create these four guard vacancies. The final O2 and CO adsorption marks then have fully vacant support buffers and do not react with each other because the child CO root is not adjacent to either child oxygen root.

Thus eleven local expander stages replace the previous eighteen.

### Terminal support trimming

The remaining geometric obstruction was the final horizontal expander's forward causal reach. Delete only the local label `CO(1,0)` from the seven-label alphabet in this **terminal** stage. Its deletion removes exactly the read cells

\[
(1,-1),\qquad(2,0)
\]

from that stage's union of read supports.

This is not assumed harmless: the exact all-history recursion was recomputed. Over the generated-shield descriptor class of Section 4,

\[
\min_\eta A^{(6)}_4(\eta)=0,
\qquad
\boxed{\min_\eta A^{(6)}_5(\eta)=5,724,131,328>0},
\]

so the six-label terminal automaton still has a uniform finite successful history family.

## 4. B28 — replace repeated worst-case boundaries by a generated shield

The old local state enumeration fixed only the incoming `2 x 2` vacancy cursor. It contains

\[
50,785
\]

stable full boundary states and exactly

\[
12,201
\]

projected descriptors relevant to the seven-label automaton.

But after the first successful horizontal advance, every subsequent horizontal stage inherits two additional vacant cells immediately behind its incoming cursor. In local coordinates these are

\[
(-2,0),(-2,1).
\]

They are not a probabilistic guess about a "typical" exterior: they are deterministic consequences of the preceding successful stage. Freezing them to zero reduces the exact state family to

\[
7,255\text{ stable full states}
\quad\longrightarrow\quad
\boxed{1,743\text{ projected descriptors}}.
\]

Hence later horizontal stages may be certified uniformly over this smaller **reachable** descriptor family without weakening source validity. This is a stronger, deterministic version of the B28 idea.

The first horizontal stage still uses all `12,201` descriptors; later horizontal stages use the `1,743` generated-shield descriptors; the terminal stage uses the six-label automaton on those `1,743` descriptors; the two rotated guard stages are conservatively certified against the full base descriptor family.

## 5. B9 — randomization attempt and the exact part that survives

I first tried to sum many competing spatial growth fronts. That is not yet a certificate: spatial front events share protected clocks, so naive addition would require an inclusion-exclusion or disjointification argument that this run did not obtain. I therefore do **not** count that proposed union toward the metric.

A smaller exact B9 gain does survive at the planter. Once its buffer is empty, both two-arrival orders

\[
O_2\ \hbox{then}\ CO,
\qquad
CO\ \hbox{then}\ O_2
\]

produce the same stable child because the roots are nonadjacent. The two embedded-label histories are disjoint and may be added exactly.

For the selected final protected set the exact clock counts are

\[
(D,N_{CO},N_{O_2})=(249,55,139).
\]

Using a Poisson window of mean two and the already certified rational bound `e^{-1}>32/87`, the two-order planter probability is bounded below by

\[
\boxed{
P_{\rm plant}
=
\left(\frac{32}{87}\right)^2\frac{8}{249^2}
=
\frac{8192}{469285569}.
}
\]

## 6. Deterministic two-child implication and 1-dependence

Let the parent seed be as in Section 3. On the good event:

1. the nine horizontal expander windows successively clear the two-row corridor through columns `9,10` while every parent occupied root is protected;
2. the downward rotated expander clears `(6,-1),(7,-1)`;
3. the upward rotated expander clears `(5,2),(6,2)`;
4. the final two adsorption marks, in either allowed order, create O at `(6,0),(7,0)` and CO at `(5,1)` while leaving columns `9,10` vacant.

The unchanged original seed is therefore a left child at offset zero, and the newly constructed seed is the same cylinder translated by nine:

\[
\boxed{
\text{one seed occurrence}
\Longrightarrow
\text{two seed occurrences at offsets }0\text{ and }9.
}
\]

The exact local interference units for the eleven expander stages are

\[
\boxed{
157,167,184,201,212,221,231,248,252,269,273.
}
\]

The union of protected CO-site clock identities has x-span `[-5,11]`. Exact enumeration of site and O2-edge clock identities shows that a translation by `2L=18` makes the full protected clock families disjoint. Therefore spatially distance-two block events are independent, yielding the same 1-dependent oriented block field required by the frozen metric. Successive time generations are placed in disjoint deterministic slabs as before.

A finite spacing scan in this frozen thin-corridor family gives distance-two disjointness

\[
L=6:\text{false},\quad
L=7:\text{false},\quad
L=8:\text{false},\quad
L=9:\text{true}.
\]

At `L=8` the site-clock families are already disjoint; the sole remaining collision is the O2 edge clock on `((10,1),(11,1))`. Thus the exact reason the inherited 1-dependence test fails at eight is localized to one edge. This is only a statement about the frozen family, not a global minimum-spacing theorem.

## 7. Exact probability certificate and metric movement

For a protected interference unit `D`, let `c_7(D;S)` denote the exact finite-horizon all-history lower bound obtained by uniformization of the seven-label local chain, summing accepted histories through eight arrivals, scanning Poisson means `1,...,8`, and minimizing over descriptor family `S`. Let `c_6` be the identical construction for the terminal six-label chain. The exact checker uses integer transition weights and a common factorial denominator; every stage used here again has Poisson mean `2` as the maximizing scanned value.

Writing `S_0` for the `12,201` base descriptors and `S_-` for the `1,743` generated-shield descriptors, the new certificate is

\[
\boxed{
\begin{aligned}
b_9={}&P_{\rm plant}\,
 c_7(157;S_0)
 c_7(167;S_-)
 c_7(184;S_-)
 c_7(201;S_-)\\
&\times c_7(212;S_-)
 c_7(221;S_-)
 c_7(231;S_-)
 c_7(248;S_-)
 c_6(252;S_-)\\
&\times c_7(269;S_0)
 c_7(273;S_0).
\end{aligned}
}
\]

The checker independently reconstructs the preceding `b8` and proves by exact rational arithmetic

\[
\boxed{b_9>b_8}.
\]

The diagnostic decimal scales are

\[
\log_{10}b_8\approx-99.23646137647626,
\]

\[
\boxed{\log_{10}b_9\approx-60.39423679122342},
\]

hence

\[
\boxed{
\log_{10}(b_9/b_8)
\approx38.842224585252836.
}
\]

Thus the frozen metric genuinely moves:

\[
\boxed{B_{\rm cat}\ge b_9>b_8.}
\]

The exact rational value certified for `b9` is

\[
\frac{
49758751590609051187887185208379138807823429264095370066434964403353208971099519799693681156860304609113002503554608176465376237651698685408038394666707178631344307935987065689140994581377056768
}{
123340659688289101634946769293098440881907977113663846535768332653492071563721468731551222445072065426905185448951138883719595772619646194678452859062844709240984346079818361719084716487325065471465233987730480822292749046956561059490797036221695958984375
}.
\]

## 8. Status and what the three methods taught

Status remains **PARTIAL / OPEN_CURRENT_BOUNDED**. The source problem is not closed: `b9` is still of order `10^-60`, enormously below the sufficient `63/64` block threshold. No independent closure audit is requested.

**B20 FIND WHY THE ALGORITHM FAILS.** The four-row corridor, not the species planter, was the main artificial cost. The exact L=8 failure also collapses to one shared O2 edge, which identifies the present geometry/dependence bottleneck precisely.

**B28 REPLACE FOR ALL WITH TYPICAL.** A probabilistic typical-boundary argument was unnecessary. The previous stage itself creates a deterministic two-cell vacancy shield, shrinking the exact adversarial descriptor set from `12,201` to `1,743` for all later horizontal stages.

**B9 RANDOMIZE.** The large multi-front union remains uncertified because of shared-clock dependence. The safe disjoint part gives two planter histories instead of one. The failed larger B9 route is recorded rather than counted.

The next nonrepeating methods are **B11/B19/B27**:

- B11: solve the exact absorbing-chain/Dirichlet hitting probabilities for the local expander instead of truncating accepted histories at eight arrivals;
- B19: turn the block construction into a multi-type seed-propagation algorithm whose states are relaxed seed classes rather than complete vacancy cylinders;
- B27: swap the remaining universal quantifier by seeking a finite family of seed types such that every stable exterior is handled by at least one type, then compare the resulting multitype block process directly with supercritical oriented percolation.

Those routes can change the per-stage exponential loss; further small reductions of a single `D` cannot plausibly bridge the remaining gap.

## 9. Exact artifacts

Self-check, not an independent audit:

- `artifacts/R08/20260918T2129Z_e0011_thin_corridor_shield_check.py`
- `artifacts/R08/20260918T2129Z_e0011_thin_corridor_shield_check.out`

The checker verifies exactly:

1. base boundary count `50,785 -> 12,201` projected descriptors;
2. generated-shield count `7,255 -> 1,743` projected descriptors;
3. six-label terminal minima `A4=0`, `A5=5,724,131,328>0`;
4. distance-two disjointness fails for `L=6,7,8` and succeeds for `L=9`, with the unique `L=8` shared edge identified;
5. the selected parent/child seed geometry and all guard cells;
6. exact eleven-stage `D` sequence and final `(249,55,139)` count;
7. distance-two site/edge clock disjointness at shift 18;
8. exact two-order planter factor `8192/469285569`;
9. reconstruction of `b8`, construction of `b9`, and exact `b9>b8`.

Artifact creation commits:

- checker: `71a6439c430ee5e75b8a573345cf26ee46b6efbc`;
- archived output: `fa962cd9bc7c65621af03083daf503e6cf5381a1`.

## 10. Model / scheduler / denied-task status

The prompt requests GPT-6 with maximum reasoning, but this run actually identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long runtime.

The exposed task control surface still has no binding model-family selector and no binding reasoning-effort selector; GPT-6/maximum can therefore be requested in prompt text but not enforced or authenticated here. Repository deployment evidence also records that the historical P26 `You cannot modify this task` failure was authorization-context-specific: P26 later accepted its full update from an authorized P/C context, while R-series edits were denied in that P/C context. A task that still rejects modification requires its authorized owning context, a supported owner/admin transfer, or platform support; there is no repository or duplicate-task workaround. No scheduler change was attempted in this run.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  lane: CLOSABLE_OUTSIDE
  target: E0011
  source: "Durrett 2009, Problem 5, original no-stirring catalyst/ZGB"
  status_before: PARTIAL
  status_after: PARTIAL
  source_resolution: OPEN_CURRENT_BOUNDED
  metric: B_cat
  before: ">= b8"
  after: ">= b9"
  exact_relation: "b9 > b8"
  diagnostic_log10_before: -99.23646137647626
  diagnostic_log10_after: -60.39423679122342
  diagnostic_log10_gain: 38.842224585252836
  unchanged_before: 0
  unchanged_after: 0
  methods: [9, 20, 28]
  next_methods: [11, 19, 27]
  closure_threshold_reached: false
  closure_audits_requested: 0
  predecessor_I0082: "RETIRED/FROZEN at 2/3"
```
