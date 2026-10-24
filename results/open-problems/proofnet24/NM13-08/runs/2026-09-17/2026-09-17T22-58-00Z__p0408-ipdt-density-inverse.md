Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `A_triangle` stays exactly `(1/4, infinity)`; Section-B methods actually tried this run: #14, #20, #29. A full on-page proof of source Question 7.2(ii) was found, but parent P0408 remains PARTIAL and no closure/audit pass is claimed.**

# NM13-08 — P0408: reconstructing the IPVT from the IPDT by an infinite-star density

Date: 2026-09-17 UTC  
Track: NM13-08  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-08/`

## 1. Continuity, ownership, and controlling state

This run **continues** the admitted P0408 assignment. It does not reopen intake and it does not create a second ownership record.

Authoritative continuity recovered before the attack:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current canonical claim `operations/claims/P0408.md`;
- newest NM13-08 report, `proofnet24/NM13-08/runs/2026-09-17/2026-09-17T21-35-50Z__p0408-finite-injectivity-obstructions.md`;
- neighboring NM13-07 and NM13-09 reports visible on current `master`;
- the historical P0408 intake/rank row and the Codex attempt in `probability_1000_intake_claude_20260907/brain_bundle_C006a06.json`.

The historical attempt had only the conditional observation that a sequence of local decoders with summable error would reconstruct the tessellation by Borel--Cantelli. It did not construct such a decoder, did not recover radial marks, and did not solve either source clause. The previous NM13-08 run instead proved exact **finite** obstructions showing why any purely finite-star decoder can fail.

Exclusive ownership remains:

- source / claim ID: **P0408**;
- owner: **NM13-08**;
- canonical dedup key: `recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual`;
- shard residue: `int(SHA256(UTF-8 key),16) mod 13 = 7`;
- claim path: `operations/claims/P0408.md`.

No conflicting current or historical owner, handoff, posted result, or campaign closure was found. The claim file is unchanged this run.

## 2. Exact source and current status

Source: Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson--Voronoi tessellations on hyperbolic spaces*, **Annals of Probability 54(2) (2026), 846--891**, DOI `10.1214/25-AOP1781`.

Exact locator: **Question 7.2 (Equivariant injectivity)**. It asks:

1. whether the map sending an IPVT to the set of its vertices is almost surely injective;
2. whether the map sending an IPVT to its ideal Poisson--Delaunay tessellation (IPDT) is almost surely injective.

The source ingredients used below were re-read in the paper/author PDF rather than inferred from the intake paraphrase:

- Theorem 3.11: the ideal-nucleus PPP on the corona, the separation field, and the IPVT are Möbius-equivariantly isomorphic. Its inverse from the IPVT first recovers **relative** corona radii from neighboring-cell bisectors and then fixes their common scale by an infinite asymptotic, `1/r_1 = lim_i (r_i/r_1)/i`.
- Equation (3.10) and Lemma 3.10: the Möbius group acts transitively on the corona and preserves the corona intensity measure.
- Proposition 3.13: after an incident ideal nucleus is moved to `infinity` in the upper-half-space model, the ideal Delaunay simplices incident to it are exactly the Euclidean beta-prime Delaunay simplices dual to the stationary Laguerre tessellation of Section 5.3.2; they tessellate `R^(d-1)`.
- Section 5.3: conditional on the central corona mark being `(infinity,s)`, the corresponding typical ideal cell `T_d(s)` is stationary and ergodic under horizontal translations.
- Lemma 5.5: the mean Euclidean volume of a typical Delaunay cell of the associated Laguerre tessellation is `s * DV_d`, where `DV_d>0` is the explicit source constant.
- Lemma 5.6 together with `j_{d,0}=1`: the Euclidean counting intensity of Laguerre vertices is exactly `1/(s*DV_d)`.
- Section 5.3 / Mecke--Slivnyak discussion: a cell attached to any fixed corona point is the Palm cell obtained by adding that point to an independent PPP.

These are published source mechanisms. The argument below is a new combination of them found in this run; I do **not** claim publication novelty from a bounded search.

### Fresh bounded literature check — 2026-09-17 UTC

Queries included:

- `"Equivariant injectivity" "Ideal Poisson" Voronoi Delaunay 2026`;
- `"Ideal Poisson-Voronoi" injectivity Delaunay vertices 2026`;
- `"map that sends an IPVT to its IPDT" injective`;
- source title plus `Question 7.2`, `injectivity`, `Delaunay`, and the source authors.

The search recovered the March 2026 Annals publication and later neighboring work, including:

- Sam Mellick, *Indistinguishability of cells for the ideal Poisson Voronoi tessellation*, Proc. AMS (2026), which resolves the different indistinguishability question;
- D'Achille--Thäle, arXiv:2606.26049 (24 June 2026), on face-volume densities and typical face volumes;
- D'Achille--Khezeli, arXiv:2606.30517 (29 June 2026), on convergence toward IPVTs in broader spaces and Diestel--Leader graphs;
- the source author's current IPVT/publications pages and related 2026 IPVT material.

No later source-matching resolution of **Question 7.2(ii)** was recovered. This is bounded dated evidence only. It is **not** a proof of worldwide openness or originality.

## 3. Frozen metric — deliberately unchanged

The claim froze the first-attack metric

`A_triangle = {a>0 : the 3-nucleus H^2 source-faithful analogue at cube-root boundary directions and marks (a,1,1) has the same full ideal-Delaunay triangle while its Voronoi diagram varies}`.

The previous run proved exactly

`A_triangle = (1/4, infinity)`.

This run does not alter that normalization or replace the metric merely because a stronger source-level route was found.

- **Before:** `(1/4, infinity)`.
- **After:** `(1/4, infinity)`.
- **Frozen-metric movement:** **none**.

The source-clause advance below is reported separately and does not reset the metric.

## 4. New idea before proof/code

The preceding finite family showed exactly what the IPDT forgets locally: a finite ideal Delaunay star can remain combinatorially/geometrically unchanged while a radial corona mark varies. Therefore a finite decoder cannot determine that mark.

The source itself supplies the missing infinite statistic. Once an ideal vertex `theta` is moved to `infinity`, its **entire incident IPDT star** becomes a stationary Euclidean Delaunay tessellation of `R^(d-1)`. Section 5.3 computes its cell/vertex intensity, and that intensity scales as **`1/s`**, where `s` is precisely the transformed radial corona mark of the central nucleus.

So the finite ambiguity is not a dead end: it predicts that the missing variable should live in an **asymptotic density at infinity**.

This led to the following source-level theorem.

## 5. Theorem — the IPDT determines the ideal-nucleus PPP almost surely

### Theorem `NM13-08-P0408-IPDT-DENSITY-INVERSE-01`

Fix `d>=2` and the source normalization of the corona PPP with intensity `mu_d`. Let `X` be that PPP, let `V_d(X)` be its IPVT, and let `D_d(X)` be its IPDT. Then there exists a measurable inverse on a full-probability set

`G : D_d(X) -> X`

such that

`G(D_d(X)) = X` almost surely.

Consequently the map

`IPVT -> IPDT`

is almost surely injective. In fact, together with Theorem 3.11, the IPDT, the IPVT, the separation field, and the ideal-nucleus PPP are Möbius-equivariantly isomorphic on full-probability sets.

**Scope:** this proves source Question 7.2(ii) on the page, subject to independent audit. It does **not** prove Question 7.2(i), so parent P0408 remains **PARTIAL** and is not called closed.

### Proof

We separate the argument into five steps to make the normalization and simultaneous-a.s. issue explicit.

#### Step 1. A canonical Euclidean chart at an ideal IPDT vertex

Fix once and for all the hyperbolic basepoint `o`. Let `theta` be an ideal vertex of an IPDT realization. Choose an isometry

`c_theta : H^d -> U^d`

from the ball model to the upper-half-space model satisfying

`c_theta(o) = (0,...,0,1)` and `c_theta(theta)=infinity`.

Any two such choices differ by an orthogonal transformation of the horizontal `R^(d-1)` coordinates: the stabilizer of both `(0,...,0,1)` and `infinity` is `O(d-1)`. Hence Euclidean balls, Euclidean volumes, and asymptotic counting densities in the horizontal boundary are independent of the choice of `c_theta`.

This can equivalently be phrased intrinsically using the horosphere through `o` centered at `theta`; its parabolic Euclidean metric is canonical up to an orthogonal change of coordinates.

Now consider every ideal `d`-simplex of the IPDT that contains `theta`. Under `c_theta` it has ideal vertices

`(infinity, x_1, ..., x_d)`, with `x_i in R^(d-1)`.

Delete `infinity`. Proposition 3.13 states that, for an actual IPDT, the resulting Euclidean `(d-1)`-simplices are precisely the beta-prime Delaunay simplices dual to the stationary Laguerre tessellation `L_{d-1}` of Section 5.3.2, and they tessellate `R^(d-1)`.

Crucially, this Euclidean simplicial tessellation is visible from the **IPDT alone**: it uses only the ideal directions/vertices and the incidence relation of the IPDT, not the hidden radial marks.

For each such finite Euclidean simplex `sigma`, put one point at its barycenter `b(sigma)`. Let

`Xi_theta(D) := { b(sigma) : sigma is an incident Delaunay simplex after deleting infinity }`.

This is a translation-covariant point process/function of the normalized IPDT star. Define, when the limit exists,

`lambda_theta(D) := lim_{R->infinity} #(Xi_theta(D) intersect B_R) / Vol_{d-1}(B_R)`.

Orthogonal ambiguity in `c_theta` does not change this number.

#### Step 2. The star density is exactly `1/(s DV_d)` under Palm conditioning

Take a fixed corona point `Y`. By the source Mecke--Slivnyak/Palm description, the ideal cell of `Y` in

`Vor(X union {Y})`

is obtained by adding `Y` to an independent corona PPP. Apply an isometry `c_Y` as in Step 1. By Lemma 3.10 the rest of the process is still a PPP of intensity `mu_d`, and the distinguished nucleus is sent to a point of the form

`(infinity,s)`

for a uniquely determined `s>0` (the transformed corona radius).

The source Section 5.3 identifies the corresponding cell with `T_d(s)`. Its horizontal law is stationary and ergodic. Therefore the projected Laguerre tessellation `L_{d-1}` and its dual Delaunay tessellation are stationary ergodic factors as well.

By Lemma 5.6, the counting intensity of the `0`-faces of `L_{d-1}` is

`j_{d,0}/(s DV_d) = 1/(s DV_d)`,

because the source records `j_{d,0}=1`.

Each Laguerre vertex is in one-to-one dual correspondence with one Delaunay `(d-1)`-simplex. Replacing the Laguerre vertex by the barycenter of its dual simplex is a translation-equivariant one-to-one point shift, so mass transport preserves counting intensity. Equivalently, Lemma 5.5 says the mean volume of a typical Delaunay simplex is `s DV_d`, and the stationary tessellation identity gives reciprocal cell intensity.

Thus the barycenter point process `Xi_Y` has intensity exactly

`1/(s DV_d)`.

Because it is stationary and ergodic, the Euclidean point-process ergodic theorem gives

`lim_{R->infinity} #(Xi_Y intersect B_R)/Vol(B_R) = 1/(s DV_d)` almost surely.      (1)

This is precisely the kind of face-count ergodic limit the source itself uses immediately after Lemma 5.6.

Therefore an infinite normalized IPDT star determines the transformed radial mark by

`s = 1/(DV_d * lambda_Y)`.                                                    (2)

#### Step 3. The density formula holds simultaneously at every random nucleus

Equation (1) was stated first for one fixed Palm-inserted corona point. Since the actual PPP has countably infinitely many random nuclei, we must not silently upgrade a one-point almost-sure statement to an all-points statement.

Let `Bad(Y,X)` be the event that, in `X union {Y}`, the limit (1) for the star of `Y` fails to exist or differs from `1/(s(Y) DV_d)` after the basepoint normalization above. For every fixed `Y`, Step 2 gives

`P(Bad(Y,X))=0`.

Exhaust the corona by finite-`mu_d` sets, for example

`A_m := S^(d-1) x [1/m,m]` in the source ball-corona coordinates.

Mecke's formula gives

`E[ # {Y in X intersect A_m : Bad(Y, X\{Y})} ]`

`= integral_{A_m} P(Bad(Y,X)) mu_d(dY) = 0`.

Hence there are no bad nuclei in `X intersect A_m` almost surely. Taking the countable union over `m` shows:

> with probability one, **every** nucleus of `X` satisfies the star-density formula simultaneously.

This removes the only Palm-to-global quantifier issue in the reconstruction.

#### Step 4. Reconstruct every corona point from the IPDT

Let `D=D_d(X)` be a realization in the full-probability event of Step 3. The ideal vertices of `D` are exactly the distinct ideal directions of the source nuclei.

For each ideal vertex `theta`:

1. normalize its star using `c_theta`;
2. form the barycenter process `Xi_theta(D)` from the incident simplices;
3. compute its asymptotic density `lambda_theta(D)`;
4. set

   `s_theta(D) := 1/(DV_d * lambda_theta(D))`;

5. recover the corona nucleus

   `Y_theta(D) := c_theta^{-1}(infinity, s_theta(D))`,

   where the inverse is the source corona action of equation (3.10).

The residual orthogonal ambiguity in `c_theta` fixes `(infinity,s_theta)`, so `Y_theta(D)` is independent of the chart choice.

For the actual IPDT, Step 2 says `s_theta(D)` is exactly the transformed radial coordinate of the original nucleus with angle `theta`. Thus

`Y_theta(D)` is exactly that original nucleus.

Therefore

`G(D) := sum_{theta in Vert_infinity(D)} delta_{Y_theta(D)}`

satisfies

`G(D_d(X)) = X` almost surely.                                                (3)

All operations above are measurable on the standard Borel space of locally finite simplicial tessellations: extract the countable ideal-vertex set and incident cells, apply a Borel choice of normalized chart, use barycenters, and take a `limsup` of Borel count ratios (with an arbitrary default off the full-probability set where the genuine limit exists). Thus `G` may be chosen measurable.

#### Step 5. Source consequence and equivariance

The forward map

`X -> D_d(X)`

is Möbius-equivariant by construction (and is recorded in the source as a factor in Remark 3.14). Equation (3) gives a measurable inverse on a full-probability set. As in the source proof of Theorem 3.11, we do not need to prove the displayed inverse formula is visibly equivariant: being an inverse of an equivariant map forces equivariance on the full-probability image.

Theorem 3.11 then reconstructs the IPVT from `X`. Therefore the factor

`IPVT -> IPDT`

has a measurable almost-sure inverse and is almost surely injective.

This proves Question 7.2(ii). `QED`

## 6. Why the previous finite counterexamples do not contradict the theorem

The preceding NM13-08 run found, for three ideal directions, a continuum of radial marks `a>1/4` with the same finite ideal-Delaunay triangle and different finite Voronoi diagrams. That remains correct.

The present proof identifies exactly what those finite examples are missing: **an asymptotic intensity**. A finite star contains no law-of-large-numbers statistic from which to infer the hidden radial scale. An infinite Palm star does: after the central end is sent to `infinity`, the density of incident Delaunay simplices is `1/(s DV_d)`.

There is a second normalization subtlety worth stating explicitly. Multiplying every corona radius in an arbitrary deterministic configuration by one common constant leaves its Voronoi and Delaunay geometry unchanged. Therefore no inverse can exist on the set of all corona configurations without a normalization. But radial multiplication changes the intensity normalization of the source PPP (`Leb(dr)` rescales). Question 7.2 is an **almost-sure statement for the fixed `mu_d` law**. The source's own Theorem 3.11 resolves exactly the same global-scale ambiguity by an infinite order-statistic limit; the present proof resolves it locally-at-each-end by an infinite star-density limit. There is no conflict.

## 7. Section-B method outcomes

### #14 FIND THE GROUP ACTING — success

The useful quotient is the stabilizer normalization of one ideal IPDT vertex. Moving `theta` to `infinity` while fixing the basepoint turns its full star into a Euclidean stationary Delaunay tessellation. The remaining chart freedom is only `O(d-1)`, which leaves the required density invariant. This exposed a scalar observable attached to each ideal vertex.

### #20 FIND WHY THE ALGORITHM FAILS — success

The finite-decoder algorithm fails for a precise reason: a finite ideal Delaunay star does not encode the radial mark. The prior `(a,1,1)` family proves that obstruction sharply. But the obstruction does **not** persist to the infinite Palm star, because the number of dual simplices per Euclidean volume depends on the missing mark as `1/s`. Identifying the exact missing datum redirected the route from local geometry to ergodic density.

### #29 ADD THE POINTS AT INFINITY — success

The ideal point `theta` is not merely a boundary decoration. Its complete incident fan, viewed from `theta=infinity`, carries a stationary Euclidean process whose density reconstructs the radial corona coordinate. The source's “point at infinity” geometry therefore supplies the source-level inverse.

These are genuinely distinct attacks from the preceding #2/#5/#12 triple.

## 8. Validation / what was and was not checked

This is an **analytic/infinite** theorem, not a finite enumeration claim, so no exact-arithmetic checker or numerical artifact is appropriate this run. The full theorem-sized argument is written on the page as required.

Self-checks performed against the source:

- the IPDT star at `infinity` really is the beta-prime Delaunay tessellation (Proposition 3.13);
- `T_d(s)` really is stationary and ergodic under horizontal translations (Section 5.3);
- the Delaunay-cell / Laguerre-vertex intensity really is `1/(s DV_d)` (Lemmas 5.5--5.6 and `j_{d,0}=1`);
- the source uses the same Mecke--Slivnyak Palm construction for a fixed corona nucleus;
- the Möbius action preserves `mu_d` and transports the radial coordinate as required (equation (3.10), Lemma 3.10);
- the source itself already accepts an infinite asymptotic to remove global radial-scale ambiguity (Theorem 3.11).

The main risks an external audit should target are therefore not hidden numerics but:

1. the translation-equivariant one-to-one identification between incident IPDT simplices and Laguerre vertices / Delaunay cells;
2. measurability of the all-vertices inverse on the chosen tessellation Borel space;
3. the Mecke step upgrading the fixed-Palm density theorem to all random nuclei simultaneously;
4. exact agreement between the transformed corona mark `s` and the Section-5 parameter under the basepoint-normalized chart.

No independent audit pass is counted in advance.

## 9. Status, counters, and remaining source obligation

Parent source P0408 status after this run: **PARTIAL**.

- Question 7.2(ii), IPVT -> IPDT injectivity: **full proof on this page; AUDIT PENDING; not called closed yet**.
- Question 7.2(i), IPVT -> vertex-set injectivity: **OPEN**.
- P26 audit: **not yet passed / not presumed**.
- NM13-09 secondary audit: **not yet passed / not presumed**.
- paper package: **not created**, because the parent source still has an open clause and the audit requirement is unmet.

Frozen metric:

`A_triangle: (1/4,infinity) -> (1/4,infinity)` — **no movement**.

Unchanged-run count on the frozen metric: **1**.  
Stuck-recovery count: **0**.

This is not a stuck run under the three-run rule: the mathematical route advanced a full source clause even though the deliberately frozen finite metric did not change.

## 10. Next route — first source clause

Do not spend the next research run polishing this proof unless an audit finds a concrete gap. The remaining mathematical target is the **vertex-set** map.

Next Section-B triple, not repeated from either previous run:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** first try to settle vertex-set injectivity in `d=2`, where the IPDT is an ideal triangulation and every Voronoi vertex has degree three.
- **#11 DUALIZE:** ask whether the unlabeled geometric Voronoi vertex set determines enough of the IPDT adjacency/face structure to invoke the density inverse above. A sufficient theorem would be: a.s. recover the IPDT from the IPVT vertex set.
- **#19 MAKE IT AN ALGORITHM:** formulate an explicit measurable rule that takes only the vertex cloud and reconstructs candidate edges/dual triangles, then prove it has no false positives/negatives under the source law. The prior finite same-vertex-set example means the proof must use global, not merely local, compatibility.

If that route succeeds, Question 7.2(i) reduces immediately to the now-proved-on-page IPDT inverse plus Theorem 3.11.

## 11. Runtime / scheduler-control disclosure

Actual runtime here identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. The requested GPT-6 / maximum setting is therefore not claimed.

The exposed scheduler/task-control schema still has prompt/title/schedule/timing/enablement fields but no binding model-family or reasoning-effort selector. Changing that requires an authorized product/scheduler surface that actually exposes such controls. Historical `You cannot modify this task` responses are authorization/context failures; the lawful remedy is the owning account/workspace or an authorized product/admin surface, not repository edits, duplicate schedules, or a bypass. No scheduler was created, modified, or disabled in this research run.

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-08
  allocation: CLOSABLE_OUTSIDE
  source_id: P0408
  claim_path: operations/claims/P0408.md
  local_claim_id: NM13-08-P0408-IPDT-DENSITY-INVERSE-01
  source: >-
    D'Achille-Curien-Enriquez-Lyons-Unel, Ideal Poisson-Voronoi
    tessellations on hyperbolic spaces, Ann. Probab. 54(2) (2026),
    Question 7.2 (Equivariant injectivity)
  parent_status: PARTIAL
  source_clause_progress:
    question_7_2_i_vertex_set: OPEN
    question_7_2_ii_ipdt: FULL_PROOF_ON_PAGE_AUDIT_PENDING
  metric_name: A_triangle
  metric_before: "(1/4, infinity)"
  metric_after: "(1/4, infinity)"
  movement: no_frozen_metric_movement
  section_B_methods_tried: [14, 20, 29]
  method_outcomes:
    14: succeeded_normalize_ideal_vertex_to_infinity_and_expose_stationary_star
    20: succeeded_identify_finite_decoder_failure_and_missing_infinite_density
    29: succeeded_recover_radial_mark_from_point_at_infinity_star_density
  theorem_core: >-
    For every IPDT ideal vertex theta, normalize (o,theta) to ((0,1),infinity).
    The incident finite simplices form the source beta-prime Delaunay tessellation.
    Their barycenter intensity is 1/(s_theta*DV_d); ergodicity recovers s_theta
    from the single infinite star. Mecke upgrades the Palm statement to all PPP
    nuclei simultaneously, yielding a measurable a.s. inverse IPDT -> corona PPP.
  exact_artifacts_this_run: []
  checker_required: false
  checker_reason: analytic_infinite_theorem_full_proof_written_on_page
  literature_check_date_utc: 2026-09-17
  literature_scope: >-
    Exact Question 7.2 phrase/source-title/author queries plus later 2026 IPVT
    work. Recovered Mellick indistinguishability, D'Achille-Thale face volumes,
    and D'Achille-Khezeli convergence; no source-matching Q7.2(ii) resolution
    found. Bounded negative search only; novelty/worldwide openness unverified.
  audits_required: [P26, NM13-09]
  audits_passed: []
  closure_claimed: false
  paper_package_created: false
  unchanged_run_count: 1
  stuck_recovery_count: 0
  next_methods: [4, 11, 19]
  next_step: >-
    Attack Question 7.2(i), first in d=2: recover IPDT adjacency/faces from the
    unlabeled Voronoi vertex set by a global measurable rule; then compose with
    the star-density inverse proved in this report.
  shared_roots_edited: false
  peer_files_edited: false
  schedules_modified: false
```

**End of complete immutable run report.**
