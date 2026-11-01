Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in retired I0082: `2/3 -> 2/3`, retirement count remains `6`; no successor metric is admitted. Reserve-route movement on F0083: direct thickening of the source's atomic one-dimensional chain is now ruled out by exact disagreement-flow accounting, while a positive-volume parcel-realization lemma shows that finite strict site-preference data itself is not the Euclidean obstruction. Methods actually used: B1 CHANGE THE CATEGORY, B7 TAKE THE LIMIT, B25 COUNT THE SAME THING TWICE.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083: from atomic nonuniqueness to shrinking Euclidean disagreement parcels

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The later six-unchanged immutable R08 handoff controls operationally despite the stale `ADMITTED_ACTIVE` wording in `operations/claims/I0082.md`: the frozen I0082 metric remains `2/3`, retirement count `6`, and the C005/C006 classification candidate still lacks the two outside source-level closure audits. This run does not increment a retired stagnation counter.

At run start I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling new-methods owner directive, `operations/claims/I0082.md`, the newest R08 report, the F0083 intake/catalog/old-attempt material, and the newest neighboring R09 report. R09 is now on its separately owned G0013 target and has no ownership overlap with F0083.

The immediately preceding R08 report used B3/B20/B27 and proved the full `d=1` uniqueness theorem for arbitrary stable Lebesgue allocations, correcting the earlier all-sated proof. I preserve that result rather than reproving it. Consequently any F0083 counterexample must have `d>=2`.

## 2. Source / current literature / ownership refresh

Reserve source:

Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), 1241--1272, arXiv:math/0505668, Open problem (i), PDF p.31.

The source asks whether there exists a discrete set of centers `Xi subset R^d` admitting two stable allocations differing on a Lebesgue-nonnull set. The source explicitly says any such example must have greater-than-quadratic growth and cannot arise from a translation-invariant finite-intensity point process.

Primary pages checked this run:

- arXiv abstract: `https://arxiv.org/abs/math/0505668`;
- source full-text page: `https://www.researchgate.net/publication/2120133_A_stable_marriage_of_Poisson_and_Lebesgue`;
- Hoffman--Holroyd--Peres, *Tail Bounds for the Stable Marriage of Poisson and Lebesgue*, arXiv:math/0507324 / Canadian J. Math. 61 (2009).

The 2006 source contains the crucial nearby countermodel: in `d=1`, replace Lebesgue measure by unit point masses at the even harmonic partial sums and put centers at the odd harmonic partial sums. Then two stable allocations exist, one shifting every site mass left and one shifting it right (with the first center unsated in the latter). The authors immediately state that they do not know whether this can happen for Lebesgue measure.

Fresh bounded searches dated 2026-09-17 used the exact title/authors plus `two stable allocations`, `discrete set of centers`, `Lebesgue`, `nonuniqueness`, and later stable-allocation/stable-transport literature. They recovered the source, the 2009 tail paper, random-appetite/percolation follow-ups and stationary matching work, but no later primary paper claiming to resolve exact Open Problem (i). This is bounded negative-search evidence only; worldwide open status and publication novelty remain **UNVERIFIED**.

Repository search still recovers F0083 only in intake/catalog material, the old F0083-A001 attempt, and recent R08 reserve-route reports. No canonical `operations/claims/F0083.md` or competing current owner was recovered. I do not create a claim: F0083 remains a promising reserve route, not a certified CLOSABLE admission.

## 3. B25 — exact flow accounting rules out the naive atomic-chain thickening

This is the first useful correction to the obvious idea suggested by the source itself.

Let `psi_1, psi_2` be two stable allocations with common appetite `alpha`, and suppose a center `xi` is sated in **both** allocations. Put

`C_xi = psi_1^{-1}(xi) intersect psi_2^{-1}(xi)`,

`O_xi = psi_1^{-1}(xi) \ psi_2^{-1}(xi)`,

`I_xi = psi_2^{-1}(xi) \ psi_1^{-1}(xi)`.

Since both territories have volume `alpha`, counting the same territory in the two ways gives the exact identity

`L(O_xi) = alpha - L(C_xi) = L(I_xi)`.

Now partition `O_xi` according to its center under `psi_2`. If

`F(xi,eta) = {x : psi_1(x)=xi, psi_2(x)=eta}`

(modulo the usual null set), and put

`q(xi,eta)=L F(xi,eta)`,

then for every center sated in both allocations

`sum_eta q(xi,eta) = sum_zeta q(zeta,xi)`.                       (3.1)

So on the all-sated part the disagreement capacities are **divergence-free**, not merely increasing.

The source's Lemma 12 proves something independent and much stronger along any forward disagreement ray:

`sum_{i>=0} q(xi_i,xi_{i+1}) < infinity`.                       (3.2)

Therefore a positive disagreement component cannot be an infinite directed chain in which every interior vertex has exactly one incoming and one outgoing positive edge. By (3.1), the edge capacity would be a positive constant `q`; then (3.2) would read `sum_i q < infinity`, impossible.

### Consequence

The source's atomic harmonic example cannot be converted into a Lebesgue counterexample merely by replacing each unit site atom by a positive-volume blob while preserving its one-in/one-out shift pattern. Its disagreement chain carries constant mass. A genuine all-sated Lebesgue counterexample needs **branching (or another mechanism changing the vertex balance)** so that individual edge capacities can shrink along every directed ray while total incoming and outgoing volume at a center still balance.

This is not a refutation of F0083. It is a refutation of the most literal `thicken the authors' atomic example` construction.

It also explains why the earlier R08 polynomial two-ended flow scaffold was structurally closer to the source than the atomic chain: branching lets edge capacities decay while conserving total appetite at vertices.

## 4. B1 — change category: an atomic preference can be thickened to a Lebesgue parcel

The preceding obstruction is **not** caused by an inability to realize a strict point-site preference with positive Lebesgue measure. That local step is easy and exact.

### Lemma 1 — product thickening preserves every collinear site preference

Let

`c_j=(a_j,0,...,0) in R^d`, `1<=j<=m`, `d>=2`,

be finitely many distinct collinear centers, and let `b in R` be such that the distances `|b-a_j|` have whatever strict comparisons we want to preserve. Then for every prescribed volume `v>0` there is a measurable set `E subset R^d` with `L(E)=v` such that **every** `x in E` has exactly the same strict ranking of the centers `c_j` as the point `(b,0,...,0)`.

**Proof.** Because there are only finitely many strict comparisons, choose `delta>0` so their signs are unchanged for every `t in (b-delta,b+delta)`. Choose any measurable `A subset R^(d-1)` with

`L_(d-1)(A)=v/(2 delta)`

and put

`E=(b-delta,b+delta) x A`.

For `x=(t,z)` we have, for every pair `i,j`,

`|x-c_i|^2-|x-c_j|^2 = (t-a_i)^2-(t-a_j)^2`;

the common transverse term `|z|^2` cancels **exactly**. Hence the sign of every pairwise distance comparison is the same as at `b`, for every point of `E`. The product volume is `v`. QED.

So arbitrary positive mass is locally available once the centers relevant to one preference gadget are collinear.

### Lemma 2 — small parcels can simultaneously control center-side radii

For later use, fix also a target transverse radius `R>0` and tolerance `tau>0`. Instead of arbitrary `A`, take `A` inside the annulus

`R-tau < |z| < R+tau`.

After reducing `delta` if necessary, every point of the resulting parcel still has the same site-side center ranking, while for each fixed center `c_j` its squared distance lies in an arbitrarily small neighborhood of

`R^2 + (b-a_j)^2`.

Any sufficiently small prescribed parcel volume can be obtained by taking a measurable subset of this positive-measure shell-product set. Thus **shrinking edge capacities** can be represented by positive-volume parcels while also placing their center-side distance ranges in a prescribed strict order.

The important limitation is global: these lemmas only encode finitely many local comparisons. They do not ensure that some remote center outside the finite gadget is not closer, and they do not fill all closer sites that stability forces a center to accept before a remote disputed parcel. That is now the real geometric obstruction.

## 5. B7 — the correct limiting object is branching, shrinking, and controlled from infinity

The source's proof of uniqueness for recurrent configurations constructs exactly the object a counterexample would have to support:

- an acyclic directed disagreement graph;
- `q(e)=L F(e)` with outgoing capacity at least incoming capacity;
- uniformly bounded Euclidean edge lengths;
- summable capacities on every directed ray;
- hence a transient underlying graph (source Proposition 13).

Combining that with Section 3 says that an **all-sated** counterexample should be searched for as a divergence-free transient branching network with shrinking edge parcels, not as a chain.

The recent R08 two-ended scaffold already supplied an abstract exact example of this bookkeeping: polynomially growing layers, bounded edges, exact incoming=outgoing capacity at each vertex, and summable edge capacities along rays. The new product-thickening lemma says the *size* of a shrinking disputed parcel is not itself the obstacle to turning that abstract flow into positive Lebesgue measure.

What remains is a single genuinely Euclidean stability problem:

> **Shielding / active-cell realization.** Embed a transient divergence-free directed network in Euclidean space and realize each edge capacity by a positive-volume parcel so that, in both allocations, every site closer to a center than one of its assigned disputed parcels is either assigned to that center or assigned to another center that the site strictly prefers.

Equivalently, in the all-sated finite-radius language from earlier R08 reports, the parcels cannot be inserted independently: they have to arise as pieces of the active nearest-center cells cut out by the acceptance balls. Sparse remote blobs leave closer unclaimed holes and immediately create unstable pairs.

This is a materially sharper remaining obligation than `thicken the atomic example`. The source's atomic example supplies the ordinal preference pattern; the source's Lemmas 9--12 supply the monotone-distance / summable-capacity constraints; Section 3 forces branching; and Lemmas 1--2 show that local positive-volume realization survives. The only unbridged step is the simultaneous global shielding geometry.

### Concrete next construction to test

Use a nonstationary layered center set with layer sizes growing polynomially and edge lengths decreasing along the directed order, so that:

1. layer-to-layer branching permits `q(e)` to be summable on rays while conserving total flow at centers;
2. decreasing edge scales reproduce the source's strict center-side distance order;
3. each disputed parcel sits next to an actual active-cell interface, rather than as an isolated remote blob;
4. the center set is not periodic or a random translate of a finite-intensity stationary set, avoiding the source's Theorem 3 exclusion.

If no such active-cell interface can carry a divergence-free transient flow, that failure itself would be a new uniqueness criterion strictly stronger than the source's recurrence criterion.

## 6. What was tried / what failed / what moved

- **B1 CHANGE THE CATEGORY:** moved the local problem from point masses to positive-volume transport parcels. Outcome: proved the exact product-thickening lemma; local site-preference realization is not the obstruction.
- **B7 TAKE THE LIMIT:** tried to port the source's infinite harmonic atomic shift. Outcome: the literal chain limit is impossible in the all-sated Lebesgue setting; the viable limit must be a branching shrinking-capacity object controlled by boundary conditions at infinity.
- **B25 COUNT THE SAME THING TWICE:** counted each sated center's territory in the two allocations. Outcome: exact incoming=outgoing disagreement volume, which combined with the source's summable-path lemma rules out every positive one-in/one-out infinite disagreement chain.

The source problem is **not solved**. The d=1 theorem from the preceding run remains PARTIAL progress; this run adds a structural obstruction and a local Euclidean realization lemma for the d>=2 construction problem.

## 7. Status and next methods

F0083 remains

`OPEN_CURRENT_BOUNDED / PARTIAL(d=1 uniqueness) / OWNERSHIP_CLEAR_IN_BOUNDED_REPO_SEARCH / HOLD_NOT_READY_CLOSABLE`.

No `operations/claims/F0083.md` was created and no artificial `0/k` source metric was invented.

The next distinct methods, if this reserve route remains best, should be **B14 FIND THE GROUP ACTING, B15 BREAK THE SYMMETRY ON PURPOSE, B19 MAKE IT AN ALGORITHM**: choose a highly symmetric finite layer gadget whose active-cell interfaces and volumes can be computed exactly, then break only the inter-layer symmetry to create a directed radius order, and formulate the infinite construction as a recurrence/algorithm for acceptance radii. If the recurrence is contractive under every source-admissible geometry, abandon this route and record the induced uniqueness criterion.

## 8. Model / reasoning control

The exposed task-management surface still provides prompt/title/schedule/timing/enabled controls but no model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains a prompt request, not a verified scheduler setting in this context. Enforcing it would require native model/reasoning controls plus completed-run telemetry in the authorized owning product/API/workspace.

The historical P26 `You cannot modify this task` result was context/authorization-specific; repository state records a later successful P26 update from another authorized context. The legitimate workaround remains the authorized owning context, supported ownership/admin transfer, or platform support, not duplicate tasks. No scheduler modification was attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  original_target:
    id: I0082
    status: RETIRED_FROZEN_PARTIAL
    metric_name: explicit_candidate_obligations_proved
    before: 2/3
    after: 2/3
    retirement_count_before: 6
    retirement_count_after: 6
    movement: false
  reserve_target:
    id: F0083
    source_status: OPEN_CURRENT_BOUNDED
    ownership: NO_CANONICAL_CURRENT_CLAIM_RECOVERED
    admission: HOLD_NOT_READY_CLOSABLE
    frozen_metric: NOT_ADMITTED
    prior_partial_result: full_d1_uniqueness
    new_results:
      - all_sated_disagreement_flow_is_exactly_divergence_free
      - positive_one_in_one_out_infinite_disagreement_chain_impossible
      - finite_collinear_strict_site_preferences_admit_exact_positive_volume_product_thickening
      - shrinking_parcels_can_add_center_distance_control_via_transverse_shells
    remaining_obligation: global_Euclidean_shielding_active_cell_realization_of_branching_shrinking_flow
  methods_used: [1, 7, 25]
  checker: NOT_APPLICABLE_THEOREM_SIZED_ANALYTIC_ARGUMENTS_ON_PAGE
  shared_roots_edited: false
  peer_files_edited: false
```
