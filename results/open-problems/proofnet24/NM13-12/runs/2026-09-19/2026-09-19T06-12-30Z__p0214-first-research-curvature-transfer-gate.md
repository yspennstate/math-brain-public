Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. P0214 is ADMITTED; frozen metric `U_T: 3/4 -> 3/4` (NO METRIC MOVEMENT). Actual Section-B methods tried this run: #2 attack the negation, #6 deform to a solved point, #30 one scale/one direction.**

# NM13-12 — P0214 first research: curvature-transfer gate for Poisson-Delaunay wandering

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `P0214` / `operations/claims/P0214.md`  
Source status: `OPEN`  
Track status: `PARTIAL` (route reduction only; no source-level exponent improvement)

## 1. Runtime truth, continuity, and admission event

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The exposed runtime provides no authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduler/task-control surface still has prompt/title, schedule/timing, enablement and update/list operations, but no bindable model-family field, no bindable reasoning-effort field, and no authenticated per-run model/effort attestation. Therefore GPT-6 / maximum remains prompt text only. Making it binding would require an authorized product/workspace/API/admin scheduler surface that persists model-family and reasoning-effort into inference routing and returns trustworthy per-run attestation. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; the lawful workaround is the owning/authorized context or an authorized platform/admin/support path, not duplication or bypass. No schedule was modified in this run.

I reread the required fleet/policy surfaces and authoritative continuity: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, later owner-authorized deployment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, probability-campaign `INDEX.md` and `RANKING.md`, the newest own NM13-12 report, neighboring NM13-11 and NM13-13 reports, the Codex campaign ledger, dedup index, prior-attempt ledger, and current claims.

The controlling predecessor report is

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T04-58-30Z__post-e0086-admission-delta-screen-15-p0219-claimed-elsewhere.md`

at creation commit

`8de06a4485443ebfe79d6553ce76e6dc8c9c7526`.

Its durable state was `ADMISSION_PENDING`, successor metric `UNMEASURED`, initial methods #2/#6/#30 unspent, P0483 and E0086 terminal and non-restartable, and P0219 excluded after another lane claimed it.

A neighboring NM13-11 report exposed a real defect in the earlier NM13 static-cursor logic: older legacy Codex P rows could have been skipped even when a worker had entered strict delta-only screening. I therefore repaired NM13-12's legacy P tranche rather than treating the old cursor as a completeness certificate. Rehashing canonical keys in P0162--P0223 recovered exactly three residue-11 rows:

| ID | canonical dedup key | SHA-256 | mod 13 | disposition |
|---|---|---|---:|---|
| P0205 | `metropolis_relaxation_for_geometric-time_cayley_targets` | `134f99e60788b624c46c0d70383afb09f26cee7a8f7dbcd983f1c05da3849781` | 11 | historical partial counterexample; not selected |
| **P0214** | `fluctuations_of_shortest_routes_in_poisson_proximity_networks` | `7707fc4888eade0e22136663abfefe5b2eddf2d482cc0bba1a943a3dcac811ff` | **11** | **selected and admitted** |
| P0219 | `high-density_oriented_percolation_flow_asymptotics` | `77b9c00d0e9ccd64917689dc1ffb6ba9918efbf2d5975a913593b39da40ac3ea` | 11 | claimed by another native lane; excluded |

The P0214 key is independently present in the F-intake dedup index, so this is the canonical identity, not an alias hash. The Codex ledger marks P0214 `attempted_unsolved`; its preserved attempt used only a deterministic Euclidean relation between detour length and transverse deviation and explicitly left the fluctuation/correlation problem unresolved.

Immediately before claiming P0214, direct fetch of `operations/claims/P0214.md` returned `404`; exact ID/title/key searches recovered only intake/campaign/dedup records and no `proofnet24` assignment, claim, handoff owner, or historical task ownership. Current `POSTED.md`, `RESULTS.md`, `QUEUE.md` and campaign ledgers contained no posted/settled/retired/paused collision. P0483/E0086 stayed terminal; P0219 stayed owned elsewhere.

The canonical create-only claim was then created and read back successfully at creation commit

`3d6afc975eef0af525062bec49b67b3918d31698`.

No overwrite semantics were used.

## 2. Frozen process and metric

The source is David Aldous's maintained open problem *Shortest routes in random proximity networks*. For a random proximity network on planar Poisson points it asks for rigorous orders of shortest-route variance and transversal deviation. The maintained page fetched in this run still says rigorous study of these questions remains open.

This HARD worker freezes the following source-valid member of that class:

- unit-intensity planar homogeneous Poisson point process;
- its Delaunay triangulation;
- each Delaunay edge weighted by Euclidean edge length;
- geodesics minimize total Euclidean edge length;
- bounded-local endpoint conventions, with start in a fixed-size box and the other endpoint at Euclidean distance `r`, matching the stationary formulation in the rigorous prior art.

Frozen metric `U_T` is the best certified polynomial upper exponent in this track for maximal transverse deviation: `a` is certified when a complete source-valid proof establishes that for every `epsilon>0`, almost surely all sufficiently long relevant geodesics satisfy

`T_r <= r^(a+epsilon)`.

The admission baseline is **`U_T=3/4`**, recovered rather than invented. Hirsch--Neuhäuser--Schmidt (ESAIM Probab. Stat. 20 (2016), 261--292) prove that for Delaunay/Voronoi/relative-neighborhood segment processes satisfying their hypotheses, passage-length deviations are controlled at every exponent `beta>1/2`; their Theorem 2.2 then gives, almost surely, all sufficiently long geodesics from a unit start box inside a tube of width `r^(3/4+epsilon)`. During this run the Numdam PDF itself was successfully parsed and visually checked at the statement page and the Section 6.2 proof page. This upgrades the claim-time access note: the earlier direct PDF route had been flaky, but the baseline is now directly source-verified.

The 2019 Kartun-Giles--Barthelemy--Dettmann simulations predict for the excluded-region class containing Delaunay approximately `xi=0.70` transverse wandering and `chi=0.40` route-length fluctuations; these are numerical predictions, not theorems and not the metric baseline.

## 3. Method #2 — attack the negation first

### 3.1 Source-valid obstruction hunt: one giant Poisson void does **not** explain `3/4`

The first negation attempt was to force an anomalously wandering Delaunay geodesic by a single macroscopic empty Poisson region. This route fails at every positive polynomial scale.

For a unit-intensity Poisson process, a fixed disk of radius `h` is empty with probability `exp(-pi h^2)`. If an empty disk of radius `h` has center in a deterministic `O(r)`-radius region, choose a unit-lattice point within distance `sqrt(2)` of its center; then a concentric disk of radius at least `h-sqrt(2)` at that lattice point is empty. There are only `O(r^2)` relevant lattice centers. Hence for `h=r^gamma`, any fixed `gamma>0`,

`P(exists such an empty disk) <= C r^2 exp(-pi (r^gamma-sqrt(2))^2)`.

The right side is summable in integer `r`. Borel--Cantelli therefore rules out infinitely many such single-hole events almost surely.

**Outcome of B2 counterexample hunt:** a lone macroscopic Poisson void cannot be the mechanism forcing a positive asymptotic wandering exponent. Any obstruction to improving `3/4` has to come from collective passage-time fluctuations / many local geometric perturbations, not one giant hole. This is a route elimination, not a source theorem about `T_r`.

### 3.2 The more important negative result: the diffusive-error + curvature architecture is locked at `3/4`

The current `3/4` proof has a clean deterministic core. I wrote it explicitly because it tells us exactly what a new route must beat.

**Curvature-transfer lemma.** Let `d_G` be a shortest-path metric obtained by summing Euclidean edge lengths in an embedded graph. Let `x,y` satisfy `|x-y|=r`, and let `z` lie on a `d_G`-geodesic from `x` to `y`. Put `h=dist(z,[x,y])` and assume `h<=r`. Suppose for some `mu>0` and error `A>=0` that all three pairs satisfy

`|d_G(x,y)-mu r| <= A`,

`|d_G(x,z)-mu |x-z|| <= A`,

`|d_G(z,y)-mu |z-y|| <= A`.

Then

`h <= sqrt(3 A r / mu)`.

**Proof.** Because `z` lies on a geodesic,

`d_G(x,y)=d_G(x,z)+d_G(z,y)`.

Therefore

`mu (|x-z|+|z-y|-r) <= 3A`.                       (1)

It remains to lower-bound the Euclidean broken-line excess. If the orthogonal projection of `z` onto the line through `x,y` lies inside `[x,y]`, convexity shows that for fixed transverse height `h` the broken length is minimized when the projection is the midpoint, so

`|x-z|+|z-y|-r >= sqrt(r^2+4h^2)-r`

`= 4h^2/(sqrt(r^2+4h^2)+r) >= h^2/r`

because `h<=r` implies `sqrt(r^2+4h^2)+r < 4r`. If the projection lies outside `[x,y]`, the excess is at least `h`, hence at least `h^2/r`. Combining either case with (1) gives `mu h^2/r <= 3A`, proving the claim. QED.

This lemma is the familiar curvature mechanism underlying the existing literature; I make **no novelty claim** for the mechanism itself. Its value here is that it turns the research target into an exact exponent equation:

if a uniform, summable passage-error estimate has scale `A(r)=O(r^chi)`, then this architecture can give at best

`T_r = O(r^((1+chi)/2))`.

At the present HNS threshold `chi=1/2+o(1)`, this is exactly `3/4+o(1)`. Therefore another lemma inside the same diffusive martingale architecture will not move `U_T`.

More sharply, to improve the transverse exponent from `3/4` to `3/4-eta` through curvature, one needs passage error on scale

`A(r) = O(r^(1/2-2 eta))`                                           (2)

with sufficient uniform tail control. The simulation pair `(chi,xi)=(2/5,7/10)` is consistent with this equation: `xi=(1+chi)/2=7/10`.

**B2 outcome:** the negation attack did not refute the source conjectural scaling. It did refute a research strategy: diffusive (`r^(1/2+o(1))`) passage-error control plus quadratic curvature is structurally incapable of improving the tracked exponent below `3/4`.

## 4. Method #6 — deform to a solved point and identify the exact transfer error

The most relevant solved deformation I found is the Howard--Newman Euclidean first-passage model on a Poisson process. Bernstein--Damron--Greenwood prove

`Var T(0,n e1) <= C n/log n`

there, using Falik--Samorodnitsky, Bernoulli encoding and greedy-lattice-animal control. That is a genuine sublinear-variance mechanism in a Poisson Euclidean setting, but it is not the Delaunay graph and it does not by itself move our polynomial exponent.

### 4.1 Why a direct import is insufficient

Even if the same `C r/log r` variance bound were proved tomorrow for Poisson-Delaunay route length, its standard deviation is still `r^(1/2)` up to logarithms. Feeding only that scale into the curvature-transfer lemma yields at most a logarithmic narrowing of the `r^(3/4)` tube, not a certified exponent `<3/4`. Thus **a bare BDG variance port is not a metric-moving target** and I will not spend the next run proving only that statement.

Also, variance alone plus Chebyshev is too weak for the uniform-over-many-potential-geodesic-points Borel--Cantelli step. The target needs polynomial improvement in the passage error and a strong enough tail.

### 4.2 Exact Delaunay transfer obstruction

The Delaunay metric is a function of the Poisson configuration in a qualitatively harder way than a fixed independent-edge environment: resampling one spatial block may change the local Delaunay adjacency through circumdisk emptiness, as well as changing which path is geodesic. HNS already built a stabilization/regularization framework sufficient for diffusive moderate deviations. The new transfer route would have to combine that geometric stabilization with low-influence/entropy technology rather than restart the martingale proof.

A useful block-resampling variable is

`Delta_Q D_r = D_r(Pi) - D_r(Pi^(Q))`,

where `Pi^(Q)` is obtained by independently resampling the Poisson points in one unit block `Q`. A metric-moving transfer must establish, uniformly in the long direction, both:

1. **localized sensitivity:** off a stabilization failure event, `Delta_Q D_r=0` unless the old or repaired geodesic comes within the stabilization neighborhood of `Q`, with a quantitative bound on `|Delta_Q D_r|` in terms of local geometry; and
2. **polynomial low influence / tail upgrade:** the aggregate block influences are small enough to give a passage-error exponent strictly below `1/2`, not merely a logarithmic correction, together with tails strong enough for the uniform geodesic-location union bound below.

The exact transfer error is therefore not “Delaunay is locally stable” in words. It is a bound on the resampling sensitivity functional strong enough to imply the `MD(eta,p)` estimate in Section 5.

**B6 outcome:** the Howard--Newman deformation identifies a plausible low-influence technology, but the currently published `n/log n` gain is quantitatively too weak for `U_T`. The only live version of this route is a genuinely polynomial Delaunay sensitivity/concentration improvement. A mere variance-log port is abandoned as a metric target.

## 5. Method #30 — one direction, one scale: the exact inequality that would move `U_T`

Fix the horizontal direction and an integer distance `r`. Let the start be in the unit box at the origin and the target in a fixed-size box near `r e1`. Existing HNS moderate deviations give a coarse linear passage bound with summable failure probability, so eventually every geodesic is confined to a deterministic `O(r)` region. Equivalently, one may use any deterministic Delaunay spanner constant only for this coarse confinement; the recent 2026 preprint improving the universal Delaunay stretch factor to `1.65` changes a constant, not the exponent argument.

An `O(r)` region contains `O(r^2)` unit boxes. Therefore the following single-scale estimate is sufficient.

### `MD(eta,p)` target

For some `eta>0` and `p>3`, uniformly over all unit boxes `Q` in that coarse `O(r)` region and all graph vertices in the relevant endpoint boxes, require

`P( one of the needed pairwise deviations |d_G(u,v)-mu|u-v|| exceeds C r^(1/2-2 eta) ) <= C r^(-p)`.

The event is required for the two legs `x--z`, `z--y` and the endpoint pair `x--y`, with the supremum taken over vertices in their unit boxes as in the HNS box-uniform formulation.

There are `O(r^2)` candidate boxes for `z`, so a union bound gives total scale-`r` failure probability

`O(r^(2-p))`.

The condition `p>3` is exactly what makes

`sum_r r^(2-p) < infinity`.

Borel--Cantelli then supplies, almost surely for all sufficiently large `r`, the simultaneous three-pair error bound for every possible geodesic junction `z`. Applying the curvature-transfer lemma with

`A(r)=C r^(1/2-2 eta)`

gives

`T_r <= C' r^(3/4-eta)`.

After absorbing constants into an arbitrary extra `epsilon`, this would certify

`U_T <= 3/4-eta`,

which is genuine movement of the frozen metric.

This is the exact one-scale quantitative gate. No multiscale induction has been assumed. If a later route needs multiple scales, it must display the induction and a summable error budget explicitly.

For comparison, a purely logarithmic passage improvement

`A(r)=r^(1/2)/(log r)^a`

would yield only

`T_r <= C r^(3/4)/(log r)^(a/2)`,

which is useful source progress but **does not move `U_T`** as currently frozen.

**B30 outcome:** the research target is now localized to one direction and one scale: prove `MD(eta,p)` for any `eta>0`, `p>3`, or find a source-valid obstruction. This is a complete quantitative implication, not an assertion that the required estimate already holds.

## 6. Fresh literature check and what changed the route

Bounded literature checks were performed on 2026-09-19 against the original author-maintained source and current primary/recent papers. Search scope included exact title/source queries and combinations of `Poisson-Delaunay`, `geodesic`, `transversal`, `wandering`, `variance`, `shortest path`, `moderate deviations`, `sublinear variance`, and 2024--2026 dates.

Recovered and checked:

- David Aldous, maintained *Shortest routes in random proximity networks*: still says rigorous study of the orders of `T_r` and `Var(D_r)` remains open.
- Hirsch--Neuhäuser--Schmidt, *Moderate deviations for shortest-path lengths on random segment processes*, ESAIM P&S 20 (2016): Theorem 2.1 gives passage deviations at arbitrary exponent `beta>1/2`; Theorem 2.2 gives the `3/4+epsilon` geodesic tube. The Numdam PDF statement and proof pages were inspected directly this run.
- Kartun-Giles--Barthelemy--Dettmann, *The shape of shortest paths in random spatial networks*, Phys. Rev. E 100 (2019): numerical Delaunay/excluded-region exponents around `xi=0.70`, `chi=0.40`; no rigorous source closure.
- Bernstein--Damron--Greenwood, *Sublinear variance in Euclidean first-passage percolation* (2019/2020): `Cn/log n` variance in the different Howard--Newman Poisson Euclidean FPP model; useful deformation technology, quantitatively insufficient by itself for polynomial movement of `U_T`.
- Malkovich--Bystrov, *Tortuosity of Delaunay Triangulations and Statistics of Shortest Paths* (published online 2024): numerical/statistical shortest-path study, not a rigorous fluctuation-order theorem for the frozen Poisson-Delaunay process.
- Marquis, *Diffusive geodesics wandering in networks of rigid chains* (2025): a different correlated spatial-network ensemble with explicit exponents; not a resolution of P0214.
- Mo--Cheng--Ding, *The Stretch Factor of Planar Delaunay Triangulations Is Less Than 1.65* (September 2026 preprint): sharpens deterministic coarse path confinement but does not address Poisson-Delaunay route fluctuation exponents.

I did **not** recover a checked 2020--2026 primary source proving the exact Aldous orders or a Poisson-Delaunay transversal upper exponent below `3/4`. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

The closest solved proof technology still lacks exactly what this source needs: a polynomial improvement below diffusive passage-error scale with uniform tails after Delaunay stabilization.

## 7. Metric accounting, stuck accounting, and next route

Frozen metric before: `U_T = 3/4`.  
Frozen metric after: `U_T = 3/4`.  
**No metric movement.**

This first admitted run nonetheless produced a source-relevant route reduction:

- eliminated single macroscopic Poisson holes as an asymptotic counterexample mechanism;
- proved on-page the exact curvature transfer inequality;
- proved that the diffusive-error architecture is exponent-locked at `3/4`;
- identified why a mere `n/log n` variance port cannot move the metric;
- reduced a genuine improvement to the explicit single-scale `MD(eta,p)` gate with `eta>0`, `p>3`.

This is not a finite claim, so no exact-arithmetic checker was manufactured. The theorem-sized deterministic implication has its full proof on the page. No source theorem is called proved/refuted.

Supported unchanged-run count after admission: **1**.  
Stuck-recovery episodes used on P0214: **0 / 2**.  
This is not yet a stuck run under the three-unchanged-run rule.

The next run must not repeat #2/#6/#30. Planned methods, not yet tried, are:

- **#11 DUALIZE:** formulate the Delaunay block-resampling problem directly in an entropy/influence inequality and isolate the dual quantity whose polynomial decay would imply `MD(eta,p)`;
- **#20 FIND WHY THE ALGORITHM FAILS:** write an explicit geodesic-repair procedure after one Poisson block resampling and locate the first configuration where repair cost cannot be charged locally;
- **#24 FIND THE EXTREMAL OBJECT:** characterize the local Delaunay cavity geometry that maximizes resampling sensitivity subject to a bounded stabilization radius.

Abandonment rule for the next route: if the block-resampling route yields only logarithmic improvement (`r/log r`, or a log tube narrowing) and no mechanism for polynomial passage-error gain, it does not move `U_T` and must be abandoned rather than expanded into more bookkeeping.

## 8. Repository delta and write discipline

The final prewrite master snapshot used for this report was

`5d51de7e57f713973b49a4143fa1292641b69eaa`.

Relative to the predecessor report commit `8de06a4485443ebfe79d6553ce76e6dc8c9c7526`, this snapshot was **114 commits ahead, 0 behind**. The material shard correction came from the neighboring legacy-P cursor repair; P0214 had no canonical claim before this invocation. This invocation created only the canonical P0214 claim and this one own-namespace immutable report. No shared root ledger, peer namespace, workflow, permission, public post, email/Drive resource, paid compute resource, or scheduler was modified.

The report must be read back at its creation commit; no receipt-only follow-up commit is permitted.

## 9. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-12
  category: HARD_OUTSIDE
  source_id: P0214
  claim_id: P0214
  claim_path: operations/claims/P0214.md
  claim_creation_commit: 3d6afc975eef0af525062bec49b67b3918d31698
  source_status: OPEN
  track_status: PARTIAL
  admission_state: ADMITTED
  canonical_dedup_key: fluctuations_of_shortest_routes_in_poisson_proximity_networks
  shard_mod_13: 11
  frozen_process: unit_intensity_planar_poisson_delaunay_euclidean_edge_length_geodesic
  metric_name: U_T_poisson_delaunay_transversal_upper_exponent
  metric_before: 3/4
  metric_after: 3/4
  mathematical_metric_movement: false
  research_route_movement: true
  section_B_methods:
    requested_initial: [2, 6, 30]
    actually_tried: [2, 6, 30]
    outcomes:
      2: single_macroscopic_void_eliminated_and_diffusive_curvature_route_locked_at_3_over_4
      6: Howard_Newman_low_influence_deformation_identifies_Delaunay_resampling_sensitivity_gate_but_log_variance_is_insufficient
      30: explicit_MD_eta_p_single_scale_gate_with_eta_positive_and_p_gt_3
  theorem_sized_claims:
    - curvature_transfer_lemma_full_proof_on_page
    - MD_eta_p_implies_U_T_at_most_3_over_4_minus_eta_conditional_implication_full_derivation
  finite_checker_created: false
  substantive_artifact_created: false
  unchanged_runs_after_admission: 1
  stuck_recoveries_used: 0
  stuck_recoveries_limit: 2
  predecessor_terminal_exclusions:
    P0483: preserved
    E0086: preserved
  ownership_exclusions:
    P0219: claimed_elsewhere_do_not_touch
  audits:
    P26: NOT_REQUESTED_NOT_CLOSED
    NM13_13: NOT_REQUESTED_NOT_CLOSED
  next_methods_planned_not_tried: [11, 20, 24]
  next_step: prove_or_refute_polynomial_Delaunay_block_resampling_sensitivity_strong_enough_for_MD_eta_p; abandon_if_only_logarithmic_gain
  predecessor_report_commit: 8de06a4485443ebfe79d6553ce76e6dc8c9c7526
  frozen_prewrite_head: 5d51de7e57f713973b49a4143fa1292641b69eaa
  commits_ahead: 114
  commits_behind: 0
  model_requested: GPT-6
  reasoning_requested: maximum
  model_actual: GPT-5.6_Sol
  reasoning_actual: UNVERIFIED
  scheduler_model_selector: absent
  scheduler_reasoning_selector: absent
```
