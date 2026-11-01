Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime telemetry or binding model/effort selector was exposed.

# R7-03 source-admission screen: P0415

Date checked: 2026-09-19 UTC  
Worker: R7-03 (`6aabe7be74008191b526b109ee4e9e80`)  
Pre-write master snapshot: `2194a2b3697febf72e8073da8ba0d31d9207faa6`  
Canonical candidate: `P0415`  
Shard check: `sum(ord(c) for c in "P0415") = 282 ≡ 2 (mod 7)`  
R7-03 decision: **NOT ADMITTED; HARD/BROAD OUTSIDE; PENDING_ADMISSION continues.**

## 1. Exact outside source and source scope

Primary source: Anna Gusakova, “(S1) Random tessellations in hyperbolic space,” in Ruth Kellerhals and Christoph Thäle (organizers), *Mini-Workshop: Hyperbolic meets Stochastic Geometry*, Oberwolfach Report 57/2025, workshop 7–12 December 2025, published 4 March 2026, DOI `10.4171/OWR/2025/57`.

Source URL: `https://ems.press/journals/owr/articles/14299586`  
Direct report DOI: `https://doi.org/10.4171/OWR/2025/57`  
Problem locator: report pp. 3046–3047, PDF pp. 15–16, especially the paragraph immediately after the classical center-based definition of cell intensity and typical cell.

Exact source-level request, paraphrased: for an isometry-invariant tessellation of hyperbolic space that can contain infinite-volume / unbounded cells, find a natural extension of the notions of cell intensity and the typical-cell distribution. The source first explains the bounded-cell construction using an isometry-covariant center function and then notes the mass-transport obstruction for infinite-volume cells.

Canonical repository alias: `P0415`, “Canonical intensity and typical-cell laws for unbounded hyperbolic cells,” dedup key `canonical_intensity_and_typical-cell_laws_for_unbounded_hyperbolic_cells`.

The campaign’s earlier partial observation was only the volume-Palm obstruction: if one tried to retain a finite positive cell intensity `gamma` and a probability typical-cell law satisfying `gamma E Vol(C_typ)=1`, then positive typical probability of an infinite-volume cell is impossible. No canonical replacement or uniqueness principle was supplied.

At the frozen pre-write master, `operations/claims/P0415.md` does not exist. This is not enough for admission: the source endpoint is deliberately open-ended (“find a natural extension”), and is not an honest short finite/sharp-parameter closure target.

## 2. Current-status / later-work check dated 2026-09-19

The current source version was re-read at the EMS/Oberwolfach report. The closest later author-side work located is:

1. Tillmann Bühler, Anna Gusakova, Konstantin Recke, *Critical Poisson hyperplane percolation in hyperbolic space has no unbounded cells*, arXiv:2512.19425 (22 Dec 2025). It proves that subcritical hyperbolic Poisson hyperplane tessellations have infinitely many unbounded cells, while critical and supercritical tessellations have none. Its Lemma 2.2 proves the interior-center obstruction by mass transport. This sharpens the motivating model but does not construct a generalized typical cell in the subcritical regime.
2. Tillmann Bühler, Christoph Thäle, *The volume of hyperbolic Poisson zero cells: critical divergence and exact second moment*, arXiv:2604.05760 (7 Apr 2026). This concerns zero-cell moments at/above criticality, not a typical-cell replacement below criticality.
3. Matteo D’Achille, Christoph Thäle, *Face volume densities of positive-intensity and ideal Poisson–Voronoi tessellations in hyperbolic spaces*, arXiv:2606.26049 (June 2026). It derives face-volume densities and typical-face quantities in the highly structured IPVT setting. It does not supply a general full-isometry typical-cell construction for arbitrary tessellations with unbounded cells.
4. Florian Besau, Anna Gusakova, Christoph Thäle, *Random hyperbolic polyhedra in horoballs*, arXiv:2609.10007 (submitted 9 Sep 2026, updated 10 Sep 2026). With a distinguished ideal direction and a bounding horosphere, projection produces a stationary Euclidean tessellation with a genuine cell intensity and typical cell. This is a strong solved analogue showing that extra boundary/horospherical structure can repair the problem, but it does not descend to an unrooted full-isometry construction in the source’s general setting.

Bounded searches through 2026-09-19 did not locate a paper claiming the source-level general extension. This is negative evidence only and is **not** an openness or novelty certificate.

## 3. B2 — attack the negation first: a boundary-root no-go theorem

A tempting response to the failure of interior centers is to anchor an unbounded cell at an ideal boundary point. The first theorem shows that a *probability-valued*, fully isometry-invariant boundary anchor cannot replace the missing center.

### Theorem 3.1 (no invariant probability boundary root)

Let `d>=2`, `G=Isom(H^d)`, and let `T` be any `G`-stationary random tessellation. There is no measurable construction (even with auxiliary randomness in a jointly `G`-stationary coupling) of a single random ideal point `Xi in ∂∞H^d` satisfying the covariance rule

`Xi(gT,gU) = g Xi(T,U)`

for every `g in G` almost surely.

#### Proof

If such `Xi` existed, its unconditional law `nu` would be a Borel probability measure on `∂∞H^d`. Stationarity and covariance imply

`nu(gA) = P(Xi in gA) = P(g^{-1}Xi in A) = P(Xi in A) = nu(A)`

for every Borel set `A` and every `g in G`. Hence `nu` would be a `G`-invariant probability measure on the ideal boundary.

No such measure exists. To see this directly, fix `o in H^d`. Invariance under the compact stabilizer `K=Stab_G(o)` forces `nu` to be the unique `K`-invariant probability, namely the visual/spherical probability `sigma_o` on `∂∞H^d`. Choose a hyperbolic translation `g` with `go != o`. Then `g_* sigma_o = sigma_{go}`. The two visual measures are not equal: their Radon–Nikodym derivative is the nonconstant Poisson/Busemann kernel. Therefore `sigma_o` is not invariant under `g`, contradiction. ∎

### Corollary 3.2 (no finite boundary intensity)

There is no nonzero equivariant random finite Borel measure `M_T` on `∂∞H^d` with

`0 < E M_T(∂∞H^d) < infinity`

and `M_{gT}=g_*M_T`.

Indeed `E M_T` would be a nonzero finite `G`-invariant Borel measure; after normalization it would contradict Theorem 3.1.

**Interpretation.** Replacing one interior center per cell by one ideal boundary anchor per cell does not merely require a technical change of measure. The boundary has no nonzero finite isometry-invariant Radon reference measure at all. Any useful construction must therefore be sigma-finite/non-Radon, retain a root/frame/horosphere, or use a quasi-invariant measure with a cocycle correction.

## 4. B6 — deform from a solved case: the visual-measure route and its exact failure

For bounded cells, the classical construction uses invariant hyperbolic volume as the sigma-finite reference measure for the center point process. A natural deformation toward unbounded cells is to replace a center by the ideal boundary shadow and weight it by the visual probability `sigma_x` seen from a base point `x`.

For a Borel set `A subset ∂∞H^d`, define

`u_A(x) := sigma_x(A)`.

The family `(sigma_x)_x` is covariant, but not invariant: changing `x` multiplies boundary density by the Poisson/Busemann kernel.

### Lemma 4.1 (visual weights cannot descend unless trivial)

If `u_A(x)` is independent of `x in H^d`, then `sigma_x(A)` is either `0` for every `x` or `1` for every `x`.

#### Proof

`u_A` is the Poisson extension of the boundary function `1_A`, hence is a bounded harmonic function. If it is constant, its almost-everywhere radial boundary limit is the same constant. But the radial boundary limit of the Poisson extension is `1_A` almost everywhere. Therefore `1_A` is almost everywhere constant, so the constant is `0` or `1`. ∎

Thus if a tessellation has two genuinely different ideal shadows of positive visual measure, the weights of those cells necessarily depend on the observer/root. A visual-shadow typical-cell law can be made *root-covariant*, but it cannot simply be forgotten down to an unrooted full-isometry law.

The 2026 horoball-polyhedra paper is a useful deformation point: there an ideal direction/horosphere is part of the model, and projection yields a stationary Euclidean tessellation with ordinary intensity and typical-cell notions. The extra ideal direction is not cosmetic; Theorem 3.1 says a fully stationary tessellation cannot manufacture such a single direction equivariantly as a probability-valued root.

## 5. B30 — localize the gluing failure in the motivating Poisson hyperplane model

The previous obstruction could still leave hope that, for the motivating Poisson hyperplane tessellation, visual measure of the union of ideal ends might itself provide enough mass. In fact it provides **zero** mass.

Let `H_gamma` be the tessellation induced by an isometry-invariant Poisson process of totally geodesic hyperplanes of positive intensity `gamma`. Let

`L_gamma := union_{C in H_gamma} ∂∞ C`,

where bounded cells contribute the empty set. Let `sigma_x` be visual probability on `∂∞H^d` from any fixed `x`.

### Theorem 5.1 (visual-nullity of all cell ideal ends)

For every `gamma>0` and every fixed `x in H^d`,

` sigma_x(L_gamma) = 0  almost surely. `

Consequently, in the subcritical regime where Bühler–Gusakova–Recke prove that there are almost surely infinitely many unbounded cells, the union of all their ideal boundary sets is nevertheless visual-measure null.

#### Proof

Fix an ideal point `xi in ∂∞H^d`. We first show

`P(xi in L_gamma)=0`.

Choose a deterministic countable dense set `D subset H^d`. If `xi in ∂∞C` for some tessellation cell `C`, then `C` has nonempty interior, so choose `q in D ∩ int(C)`. Since `C` is closed and geodesically convex and `xi` is in its ideal boundary, the geodesic ray `[q,xi)` is contained in `C`. Because `q` is an interior point, no tessellation hyperplane intersects this ray at a finite point: such an intersection would leave the open connected component whose closure is `C`.

For each fixed pair `(q,xi)`, however, the invariant hyperplane measure of hyperplanes meeting an initial ray segment of length `R` grows linearly in `R` by the hyperbolic Crofton formula. Hence the set of hyperplanes meeting the full ray has infinite intensity measure. A Poisson hyperplane process of positive intensity therefore has infinitely many hyperplanes meeting `[q,xi)` almost surely; in particular the probability that no hyperplane meets the ray is zero.

Thus, for each fixed `q in D`,

`P([q,xi) is contained in one cell)=0`.

Taking the countable union over `q in D` gives `P(xi in L_gamma)=0`.

Finally, Tonelli/Fubini with the deterministic visual probability `sigma_x` yields

`E[sigma_x(L_gamma)] = integral_{∂∞H^d} P(xi in L_gamma) sigma_x(dxi) = 0`.

Since `sigma_x(L_gamma)>=0`, it follows that `sigma_x(L_gamma)=0` almost surely. ∎

### Why this is a real obstruction rather than a restatement

The prior campaign note ruled out retaining the volume-Palm normalization. Theorem 5.1 separately rules out the most obvious *boundary probability* replacement in the principal motivating model: sampling an ideal direction from any ordinary visual measure misses **all** ideal ends of cells almost surely, even in the phase with infinitely many unbounded cells.

So a successful extension must see a random exceptional boundary set of visual measure zero. Plausible candidates include a critical Hausdorff/Patterson–Sullivan-type measure on the random end set, an encounter-point/cluster-end measure, or a horospherical Palm object. Each requires a new normalization and a uniqueness/covariance theorem; none follows from the source’s existing mass-transport formalism.

## 6. Admission classification

P0415 passes the canonical-ID shard gate and is not presently claimed, but it fails the honest CLOSABLE gate. Its source closure criterion is not a single finite certificate, exact constant, or short yes/no endpoint; it asks for a *natural theory* replacing two classical notions, with canonicity and invariance part of the mathematical content.

The new results above narrow the design space substantially but do not solve the source request:

- full-isometry probability boundary roots are impossible;
- finite nonzero boundary intensity measures are impossible;
- visual-shadow weights cannot descend root-independently except in trivial cases;
- in the Poisson hyperplane model, the complete set of unbounded-cell ideal ends has visual probability zero almost surely.

What remains is to construct and justify a nontrivial generalized Palm object (likely rooted/quasi-invariant or fractal-boundary based), prove its covariance/canonicity, show it extends the bounded-cell theory in the appropriate regime, and establish a meaningful notion of cell intensity. That is a HARD/BROAD research programme, not a CLOSABLE successor.

Therefore **no claim is created** and R7-03 remains `PENDING_ADMISSION`.

## 7. Metric / continuity / next cursor

No target was admitted, so the target metric remains legitimately unfrozen:

`UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

No admitted-target stagnation counter is incremented. The source-admission work is substantive because it proves new exact obstructions, but it is not reclassified as source resolution.

Prior R7-03 state continued from:

- `research7_2026-09-17/R7-03/runs/2026-09-19/2026-09-19T052448Z__report.md`, creation commit `80a26846988357e9b006e93ae27d1acabd5bbdfd`;
- `research7_2026-09-17/R7-03/handoffs/2026-09-19T052409Z__C0117_sixrun_handoff.md`, creation commit `89c06c2b71eaded2632c59174042236934420596`.

No C0117 revival is attempted.

`ledger_delta`:

```yaml
worker: R7-03
native_id: 6aabe7be74008191b526b109ee4e9e80
status_before: PENDING_ADMISSION
status_after: PENDING_ADMISSION
candidate_screened: P0415
shard_gate_mod7: 2
classification: HARD_BROAD_OUTSIDE_NOT_ADMITTED
claim_created: false
metric:
  name: UNFROZEN_UNTIL_ADMISSION
  before: UNKNOWN_UNMEASURED
  after: UNKNOWN_UNMEASURED
methods:
  - B2_ATTACK_NEGATION
  - B6_DEFORM_FROM_SOLVED_CASE
  - B30_LOCALIZE_GLUING_FAILURE
new_math:
  - no_full_isometry_probability_boundary_root
  - no_nonzero_finite_boundary_intensity
  - visual_weights_descend_only_when_trivial
  - poisson_hyperplane_cell_ideal_ends_are_visual_null
stagnation_count: NOT_APPLICABLE_PRE_ADMISSION
literature_check_date: 2026-09-19
next_action: continue ranked delta-only shard-2 admission scan; do not revive retired/held/owned targets
```
