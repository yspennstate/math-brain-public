Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 4915895464189826625935291363546259379089219326781/7812500000000000000000000000000000000000000000000 = 0.629234619416297808119717...` -> `b_NUV >= 4915930154808341640583728863546259379089219326781/7812500000000000000000000000000000000000000000000 = 0.629239059815467729994717... > 0.629239`; actual Section-B methods tried: #3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #26 HUNT THE SPORADIC CASE.**

# NM13-11 — P0257 continuous radius-deficit stratification and disjoint-cap improvement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: **P0257**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED**

## 1. Fixed source, metric, and result

This invocation continues the already-admitted source `P0257`, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867).

The exact source model remains unchanged:

- `n` i.i.d. uniform points in the unit square;
- a uniformly chosen starting vertex;
- at each step the walk moves to the nearest unvisited vertex;
- `L_n` is the source's area-`n` Euclidean-length scaling;
- the source's first-order challenge asks for sharper asymptotics, in particular existence/identification of the proposed constant `c = lim_n L_n/n`.

The frozen NM13-11 metric remains

`b_NUV` = the explicit certified lower endpoint in

`liminf_{n -> infinity} E[L_n]/n >= b_NUV`.

The preceding immutable report certified

`b_prev = 4915895464189826625935291363546259379089219326781 / 7812500000000000000000000000000000000000000000000`

`= 0.629234619416297808119717...`.

This invocation proves and exactly certifies

`b_NUV >= 4915930154808341640583728863546259379089219326781 / 7812500000000000000000000000000000000000000000000`

`= 0.629239059815467729994717... > 0.629239`.

The exact gain over the preceding endpoint is

`145503 / 32768000000 = 0.000004440399169921875`.

This is genuine movement of the already-frozen source-valid metric. It is not a literature-baseline correction, not a changed model, and not a finer numerical mesh for the preceding one-parameter envelope. The source remains OPEN because no existence theorem for `lim L_n/n` is proved here.

Counters after this run:

- admitted-target unchanged runs: **0 -> 0**;
- HARD stuck-recovery episodes: **0 / 2**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

## 2. Runtime and scheduler-control truth

The requested `GPT-6 / maximum` line remains prompt text, not a binding scheduler selector in the exposed interface. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The task-control surface exposed to this worker offers task title/prompt, schedule or relative-start configuration, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary. Current root `RESULTS.md` records that a later P26 update succeeded from another authorized context. The compliant workaround for a future denial is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for that same existing task—not task duplication, identity substitution, or permission bypass. No scheduler or permission was modified in this invocation.

## 3. Authoritative continuity and required reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T08-58-00Z__p0257-asymmetric-core-movement.md`

at creation commit

`01487a16cefccad6bbe2a9df706350863c971e22`.

Its durable state is:

- P0257 admitted and exclusively owned by `proofnet24/NM13-11/`;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`, SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`, residue 10 modulo 13;
- source model and metric `b_NUV` frozen;
- prior exact endpoint `0.629234619416297808119717...`;
- methods already genuinely used on P0257 before this run: `#2/#4/#8`, `#11/#20/#24`, `#5/#14/#25`, and `#15/#18/#30`;
- next planned methods `#3/#17/#26`;
- unchanged count 0 and HARD recoveries 0/2.

Before substantive work I freshly read or recovered the current controlling/state surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the predecessor report; current `operations/claims/P0257.md`; P0257 canonical dedup/source and prior-attempt evidence; newest neighboring NM13-10 and NM13-12 reports; the current exact-arithmetic artifact/output; and the complete predecessor-to-prewrite Git delta.

Newest neighboring continuity at the frozen prewrite state:

- NM13-10: `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T09-50-30Z__admission-delta-screen-39-g0004-p0342-owned-offshard.md`; it remains admission-pending and records no P0257 release, alias collision, or audit.
- NM13-12: `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T10-00-30Z__p0214-recovery2-cavity-tail-coalescence-rate-barrier.md`; it remains on P0214, has consumed its second HARD recovery, and records no P0257 audit or ownership mutation.

The append-only intake and attempt corpora are too large to honestly claim every unchanged historical byte was freshly rendered model-visible. I make no such claim. P0257's canonical identity, source, prior attempted-unsolved state, claim, and newest own continuity were reopened directly; the complete Git delta below contains no screened intake `problems.jsonl` or probability attempt-ledger mutation. Missing display is never treated as permission to reset history.

No private-repository history needed for this continuation was known to be inaccessible.

## 4. Exact predecessor-to-prewrite Git delta and ownership

Frozen pre-report `master` head:

`c9c5a7141d7d2a9028b41a409ff93676e0d3ed42`.

Exact comparison

`01487a16cefccad6bbe2a9df706350863c971e22 .. c9c5a7141d7d2a9028b41a409ff93676e0d3ed42`

reports:

- status: `ahead`;
- commits ahead: **127**;
- commits behind: **0**;
- total commits: **127**;
- `too_large = null`, so the returned changed-file set is complete.

In that complete interval:

- `operations/claims/P0257.md` is unchanged;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, screened intake `problems.jsonl`, probability attempt ledgers, and controlling owner/NM13 policy files are unchanged;
- canonical claim additions are unrelated `F0011`, `G0004`, and `P0342`;
- no P0257 release, handoff, retirement, alias collision, or ownership transfer appears;
- the only NM13-11 substantive files added before this report are the exact checker and its archived output used below.

A fresh direct read of `operations/claims/P0257.md` still records `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, the canonical residue-10 key above, and the frozen `b_NUV` metric. Ownership therefore remains intact.

## 5. Fresh source and bounded literature check — 2026-09-19

This is bounded current-status evidence, not proof of worldwide openness, novelty, or priority.

The exact Aldous source was rechecked by title and publication record. Cambridge records publication online 5 April 2021 and volume 36 issue 3 (July 2022), pages 851–867, and its abstract still says establishing sharper results is challenging. Aldous's currently crawled home/research page still lists the NUV walk and states the challenge as improving beyond order of magnitude for models of random graphs. His open-problem collection explicitly warns that it is updated haphazardly, so this is not treated as exhaustive bibliographic certification.

Focused 2024–2026 searches for the exact title, `nearest unvisited vertex`, Euclidean random points, law of large numbers, and limiting constant did not surface a checked later primary source resolving the source's Euclidean first-order limit question. The current independent Euclidean-MST background lower bound remains `0.6289`, from Draganov–Edelsbrunner–Rosenmeier–Saghafian, arXiv:2510.23373 (27 October 2025), below the carried NM13-11 endpoint.

The load-bearing geometric comparison remains Bezdek–Connelly, *Pushing disks apart — The Kneser-Poulsen conjecture in the plane*, arXiv:math/0108098 / J. reine angew. Math. 553 (2002), 221–236: if pairwise center distances of finitely many planar disks do not decrease, union area does not decrease. Their theorem permits unequal disk radii; that is prior art and is used explicitly below.

Method #17 also triggered a deliberate search for the same kind of explicit constants in nearby stochastic-geometry literature. Andrew Wade's *Explicit laws of large numbers for random nearest-neighbour-type graphs* applies Penrose–Yukich stabilization machinery to total lengths of several nearest-neighbor graphs and obtains explicit limiting constants. This is genuinely nearby in shape, but the NUV path is history-dependent and the closed-triple bonus used here is not an additive stabilizing graph functional covered by that result. I found no transferable published constant that moves `b_NUV`; therefore Method #17 produced a useful boundary on technique, not mathematical credit.

Queries/scope included:

- exact title `"The Nearest Unvisited Vertex Walk on Random Graphs"`;
- `"nearest unvisited vertex" Aldous limit constant Euclidean random points` with 2024–2026 emphasis;
- exact Bezdek–Connelly title / unequal-radius union-area terms;
- `nearest-neighbour graph law large numbers Penrose Yukich Wade explicit constants`;
- `0.6289 Euclidean minimum spanning tree lower bound 2025`.

Access was through indexed author, arXiv, and publisher text. No simulation, plot, or unverified PDF-only statement is used as proof.

## 6. Carried closed-triple architecture

I do not re-prove the predecessor's finite-binomial-to-Poisson transfer or its closed-two-nearest-triple lemma. The established source-valid architecture is

`b_NUV >= 5/8 + C/2`,

where in the unit-intensity planar Poisson limit

`C = (1/6) integral_{x in R^2} integral_{y in R^2} integral_{t>=0} exp(-A_t(x,y)) dt dy dx`.

For the inserted triple `{0,x,y}`, write

`D = max(|x|, |y|, |x-y|)`.

At a vertex `v_i`, let `r_i` be the larger of its two distances to the other inserted points. Then

`A_t(x,y) = area( union_i B(v_i, r_i+t) )`.

The 08:03 report enlarged all three radii to `D+t`, expanded the centers to an equilateral triangle by Kneser–Poulsen, and obtained the normalized equal-radius majorant

`q(rho) = pi*rho^2 + 3*rho^2*asin(1/(2rho)) + (3/4)*sqrt(4rho^2-1) + sqrt(3)/4`,

`rho = 1+t/D >= 1`, with

`q'(rho) = 2*pi*rho + 6*rho*asin(1/(2rho)) > 0`.

The 08:58 report then retained one fixed positive-measure subset where the radius at the vertex opposite the longest side is smaller by `D/4`. The present run strengthens that geometry over a continuum of shape strata and adds one disjoint shape cap.

The following elementary correction principle will be used twice. Suppose a normalized shape subfamily has four-volume `W D^4` up to diameter `D`, and on it the unequal-radius geometry saves at least `h D^2` in union area relative to the equal-radius majorant, uniformly for `u=t/D in [0,1]`. Then

`e^{-D^2(q-h)} - e^{-D^2 q} = e^{-qD^2}(e^{hD^2}-1) >= hD^2 e^{-qD^2}`.

The diameter shell is `4W D^3 dD`, `dt=D du`, and

`integral_0^infinity D^6 e^{-qD^2} dD = 15*sqrt(pi)/(16*q^(7/2))`.

Since `q(1+u) <= q(2)` on `0<=u<=1`, the resulting increment in the final `b_NUV` endpoint is at least

`(5/16) W sqrt(pi) h q(2)^(-7/2)`.                    (6.1)

The same formula integrates over a differential shape volume `dW`.

## 7. Method #3 — PROVE SOMETHING STRONGER: continuous radius-deficit stratification

The preceding `|w|<=D/4` core can be replaced by a full one-parameter continuum.

Choose one of the three possible unique longest sides, write it as

`z = x-y`, `D=|z|`, `w=(x+y)/2`,

and normalize

`s = |w|/D`.

The linear map `(x,y) <-> (z,w)` has absolute Jacobian 1. For every

`0 <= s <= 1/2`,

we have

`|x|, |y| <= |w| + |z|/2 = D(1/2+s) <= D`,

so `z` is a longest side (ties occur only on a null boundary). At the opposite vertex the initial exclusion radius is at most `D(1/2+s)`, hence the radius deficit relative to `D` is at least

`d(s) = 1/2 - s`.                                      (7.1)

For fixed `|z|=r`, the `w`-annulus with normalized radius in `[s,s+ds]` has area

`2*pi*s*r^2 ds`.

Multiplying by the polar measure `2*pi*r dr` for `z`, integrating `0<r<D`, and multiplying by the three choices of unique longest side gives differential four-volume

`dW = 3*pi^2*s ds`.                                    (7.2)

Now keep the two longest-side endpoint disks at normalized radius `rho=1+t/D` and the opposite disk at radius at most `rho-d(s)`. Expand the three centers to an equilateral triangle of side 1. All pairwise distances weakly increase, so Kneser–Poulsen says the union area can only increase.

In the equilateral configuration, compare radii `(rho,rho,rho-d)` to `(rho,rho,rho)`. Put the smaller disk's center at `C` and take the outward sector of angular width `pi/3`. A point at polar distance `r` from `C` in this sector has minimum squared distance to the other two equilateral centers at least

`r^2 + r + 1`.

For `rho>=1`, `0<=d<=1/2`, and `r>rho-d`,

`r^2+r+1-rho^2 >= (rho-d)^2+(rho-d)+1-rho^2`

`= rho(1-2d)+d^2-d+1 > 0`.

Thus this entire outward annular sector of the radius-`rho` disk is uncovered by the other two disks and disappears when the third radius is reduced to `rho-d`. Its area is

`h_d(rho) = (pi/6) [rho^2-(rho-d)^2]`

`= pi*d*(2rho-d)/6`

`>= pi*d*(2-d)/6 = h_d(1)`.                            (7.3)

Integrating (6.1) against (7.2), with `d=d(s)`, yields

`Delta_radial >= (5/16)*sqrt(pi)*q(2)^(-7/2) * (pi^3/2) * I`,

where

`I = integral_0^(1/2) s(1/2-s)(3/2+s) ds`

`= 7/192`.                                             (7.4)

This is a strictly stronger use of the same closed-triple theorem than the old fixed `s<=1/4` core: it retains every radial stratum through the full range `0<=s<=1/2`, with its actual guaranteed deficit.

For an exact coarse lower certificate, use

`3 < pi < 22/7`, `sqrt(pi)>17/10`,

and the carried exact bound

`q(2) < 2157/112 < 20`,

so

`q(2)^(-7/2) > 20^(-7/2) > 1/40000`.

Therefore

`Delta_radial > (35/6144)*27*(17/10)*(1/40000)`

`= 1071/163840000`

`= 0.000006536865234375`.                              (7.5)

Outcome of Method #3: **success and metric-moving candidate.**

## 8. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

I searched the nearest-neighbor stochastic-geometry literature for an existing exact Palm/stabilization constant that could replace the coarse `q(2)^(-7/2)` factor or directly certify the density of the relevant closed-triple configurations.

The closest useful literature located was the Penrose–Yukich stabilization framework and Wade's explicit LLNs for random nearest-neighbour-type graphs, including k-nearest-neighbor and online nearest-neighbor graphs. Those results confirm that explicit local constants are often accessible for additive stabilized graph functionals.

The NUV walk, however, is history-dependent: whether a local triangle contributes the forced departure bonus depends on the global visitation order, and the predecessor's closed-triple argument works by a deterministic forcing property plus a Poisson exclusion event, not by an additive stabilized graph score. I found no published constant or theorem whose hypotheses cover this functional and improve the certified endpoint.

Outcome of Method #17: **no direct movement; boundary learned.** I do not transplant an inapplicable stabilization LLN or count this literature search as a theorem.

## 9. Method #26 — HUNT THE SPORADIC CASE: a disjoint perpendicular cap

The radial family in Section 7 only uses `|w|<=D/2`. To test whether useful shapes survive immediately outside that disk, orient the unique longest side horizontally and write

`w = D(a,b)`.

Consider the disjoint cap

`|a| <= 1/8`, `1/2 < |b| <= 5/8`.                     (9.1)

It is disjoint from the radial family because `|b|>1/2` implies `|w|>D/2`.

For either short side,

`|w +/- z/2|^2 / D^2 <= (5/8)^2 + (5/8)^2 = 25/32 < 81/100`.

Hence both short sides are `<(9/10)D`, so the opposite exclusion radius has a guaranteed deficit

`d >= 1/10`.                                           (9.2)

The normalized `w`-area in (9.1) is

`(1/4)*(1/4) = 1/16`.

For one chosen longest side, integrating `2*pi*r * (r^2/16) dr` from 0 to `D` gives four-volume `pi D^4/32`; across three unique-longest-side choices,

`W_cap = 3*pi/32 > 9/32`.                              (9.3)

From (7.3), at `d=1/10`,

`h_(1/10)(1) = 19*pi/600 > 19/200`.                    (9.4)

Applying (6.1) with the same exact coarse bounds gives the independent disjoint correction

`Delta_cap > (5/16)*(9/32)*(17/10)*(19/200)*(1/40000)`

`= 2907/8192000000`

`= 0.0000003548583984375`.                             (9.5)

Outcome of Method #26: **success.** The cap is geometrically disjoint from the radial stratification, so its correction can be added without double counting.

## 10. Combined theorem and exact endpoint

Sections 7 and 9 replace the preceding fixed-core shape correction; they are not added on top of it. Their exact coarse total is

`Delta_shape > 1071/163840000 + 2907/8192000000`

`= 56457/8192000000`

`= 0.0000068917236328125`.                             (10.1)

The preceding 08:58 report used only

`Delta_old = 3213/1310720000`

`= 0.000002451324462890625`.

Therefore the strict certified increment over the preceding endpoint is

`Delta_shape - Delta_old`

`= 145503/32768000000`

`= 0.000004440399169921875 > 0`.                       (10.2)

The exact equilateral-envelope endpoint before any asymmetric shape correction, carried from the 08:03 report, is

`b_base = 4915876313217460292927478863546259379089219326781 / 7812500000000000000000000000000000000000000000000`.

Adding (10.1) gives

`b_NUV >= b_base + 56457/8192000000`

`= 4915930154808341640583728863546259379089219326781 / 7812500000000000000000000000000000000000000000000`

`= 0.629239059815467729994717...`

`> 0.629239`.                                          (10.3)

### Finite-to-infinite validity

No new asymptotic shortcut is introduced here. The predecessor closed-triple theorem already supplies the exact finite binomial event, boundary truncation, and Poisson/Campbell–Mecke limit. The present argument only partitions the same `(x,y)` integral into measurable positive-measure shape subsets and replaces the prior equal-radius area upper bound by a smaller rigorously proved one there. The new correction is dominated by the carried equal-radius integrand and is restricted to `0<=u=t/D<=1`, so the predecessor's truncation/dominated-convergence transfer applies verbatim. Finite plots or simulations play no role.

Thus (10.3) is a theorem in the exact source model, while the parent source's existence/identification problem remains unresolved.

## 11. Exact-arithmetic certificate

The exact checker was created in this invocation at commit

`13b623132250e526bf18294cef8b502ea145d30f`

at path

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T09-58-30Z__p0257_radius_deficit_stratification_exact.py`.

Its executed output was archived at commit

`8098969649b68201aba78896d466321616f7dd32`

at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T09-58-30Z__p0257_radius_deficit_stratification_exact.out`.

The checker uses exact `Fraction` arithmetic and integer/rational inequalities only. It verifies:

- Machin bounds implying `3<pi<22/7`;
- `sqrt(pi)>17/10`;
- `q(2) < 2157/112 < 20`;
- shape integral `I=7/192`;
- radial correction `1071/163840000`;
- cap correction `2907/8192000000`;
- total shape correction `56457/8192000000`;
- strict increment over the preceding correction `145503/32768000000`;
- the exact new endpoint in (10.3);
- `NEW_ENDPOINT_GT_0.629239 = True`.

The archived output terminates

`ALL_EXACT_FINITE_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 12. Status, route decision, and next step

P0257 remains **PARTIAL / SOURCE OPEN**. The metric moved, so the unchanged-run counter remains zero and no stuck recovery is consumed. There is no basis to request closure audits yet because the source itself is not closed; P26 and NM13-12 remain neither requested nor presumed to pass.

The useful lesson is that the previous `D/4` core left substantial certified mass on the table. The continuous radial stratification moves the endpoint by more than the entire preceding shape correction, and a deliberately nonradial cap moves it again. Therefore the next run should not spend its research budget refining the rational constants or the numerical mesh.

Next unused Section-B methods are **#6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY**. The intended route is to parameterize the complete normalized longest-side shape space, deform each shape toward a solvable boundary configuration while tracking an exact radius-deficit/union-area functional, and compactify the large-`u` tail so that a global shape integral can be bounded without another patchwork of isolated caps. Abandon this route if it does not move `b_NUV` rather than manufacturing more certificates for the same endpoint.

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  namespace: proofnet24/NM13-11/
  source_id: P0257
  claim_id: P0257
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  shard_mod_13: 10
  category: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN
  status_after: PARTIAL_SOURCE_OPEN
  metric: b_NUV = certified lower endpoint in liminf E[L_n]/n >= b_NUV
  metric_before_exact: 4915895464189826625935291363546259379089219326781/7812500000000000000000000000000000000000000000000
  metric_before_decimal: 0.629234619416297808119717...
  metric_after_exact: 4915930154808341640583728863546259379089219326781/7812500000000000000000000000000000000000000000000
  metric_after_decimal: 0.629239059815467729994717...
  metric_gain_exact: 145503/32768000000
  metric_movement: true
  methods:
    - 3: continuous radius-deficit stratification; SUCCESS
    - 17: nearest-neighbor/stabilization constant literature transfer; NO_DIRECT_MOVEMENT
    - 26: disjoint perpendicular shape cap; SUCCESS
  exact_checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T09-58-30Z__p0257_radius_deficit_stratification_exact.py
  exact_output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T09-58-30Z__p0257_radius_deficit_stratification_exact.out
  exact_output_terminal: ALL_EXACT_FINITE_CHECKS_PASS
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  hard_recoveries_consumed: 0/2
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  nm13_12_audit: NOT_REQUESTED_NOT_PRESUMED
  next_methods: [6, 12, 29]
  next_step: full normalized-shape deformation / invariant / compactified-tail route; no mesh polishing
  ownership: RETAINED_EXCLUSIVE
  source_closed: false
  report_count_this_invocation: 1
```

No shared root, peer namespace, claim file, scheduler, permission, workflow, email/Drive resource, public surface, or paid compute was modified in this invocation.
