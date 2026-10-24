Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Source metric `d_sym: 3 -> 3` (NO MOVEMENT). Methods tried: B2 / B5 / B11.**

# HARD7-01 — symmetric Mahler admission and a dimension-four shadow-flow incidence obstruction

**Status:** `PARTIAL / SOURCE OPEN`.

The source conjecture is not solved here. This run obeys the terminal-rotation rule: it first handed off and released the twice-stuck BLYZ log-Brunn–Minkowski target, then admitted a genuinely different classical outside problem and performed mathematical work immediately.

## 1. Continuity, terminal release, ownership, and exclusions

I resumed from the newest checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T02-01-47Z__stuck2_xi_radial_cubic_selector.md`.

That report was the second allowed Section-I recovery on BLYZ Problem 1.1, so continuing Xi's generalized-radii route would violate the owner protocol. The actual terminal state was preserved in

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T03-05-00Z__logbm_terminal_handoff.md`

and the canonical BLYZ claim was changed, without deletion, to `UNASSIGNED AFTER HARD7-01 HANDOFF`. No source closure was claimed: `B_cart=infinity` but unrestricted `d_full=2` remained unchanged.

Before admitting a successor I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- root `POSTED.md` and `RESULTS.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- the outgoing claim and latest HARD7-01 reports,
- repository searches for the successor's canonical aliases.

KLS is separately owned/excluded. No posted owner manuscript or existing Gaussian-inequality claim is reused.

Repository alias searches for `Mahler conjecture centrally symmetric convex bodies`, `volume product`, `reverse Santaló`, `Hanner volume product`, `4^n/n!`, and `SYMMETRIC-MAHLER` found no equivalent active canonical owner. Broad `Mahler` hits were Mahler measure / random-matrix uses and are not this problem. A create-only claim then succeeded at

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`.

## 2. Exact successor target and verified source baseline

Historical origin: Mahler's 1938/1939 reverse volume-product problem. A current explicit source statement is in Chen--Li--Xi--Xu, *The Mahler Conjecture in Three Dimensions*, arXiv:2605.09334v3, Introduction. The symmetric target is:

> for every origin-symmetric convex body `K=-K subset R^n`, prove
> 
> `P(K):=|K||K^circ| >= 4^n/n!`.

This track claims only the origin-symmetric statement, not the non-symmetric Santaló-centered conjecture.

Current-status check, 20 September 2026:

- Iriyeh--Shibata proved the symmetric conjecture in dimension three; Chen--Li--Xi--Xu give a new 2026 shadow-flow proof.
- Chen--Li--Xi--Xu's current combined paper explicitly remains three-dimensional; it does not settle dimension four or all dimensions.
- Their general shadow-system input is Meyer--Reisner polar-volume convexity/rigidity; the new three-dimensional ingredient is an admissible-speed dimension count and combinatorial classification.
- A 2026 discrete-KKT preprint treats local minimality/stability around Hanner configurations, not the global symmetric Mahler conjecture.
- Fresh searches for a four-dimensional/all-dimensional solution and higher-dimensional admissible-shadow resolution found none. This is a bounded search, not a worldwide openness or priority certificate.

Frozen source metric admitted here:

`d_sym = largest d for which P(K)>=4^d/d! is rigorously established for every origin-symmetric K subset R^d`.

Verified before/after:

`d_sym: 3 -> 3`.

So the source metric has **NO MOVEMENT**. The progress below is auxiliary and structural.

## 3. New route before code

The mathematical idea was written first in

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T03-12-00Z__idea_before_code_mahler_shadow4.md`.

The three attacks are materially different:

- **B2 (attack the negation):** test whether a plausible exact 4D centrally symmetric polytope can be shadow-rigid enough to be a local volume-product minimizer.
- **B5 (add a parameter):** put vertices into an odd one-parameter shadow flow and use affine primal volume plus Meyer--Reisner polar convexity/rigidity.
- **B11 (dualize):** apply the same obstruction to the polar, converting facet-size debt into vertex-degree debt.

The main gain is that the three-dimensional Chen--Li--Xi--Xu speed count has a clean `n`-dimensional form. In dimension four it gives explicit necessary incidence inequalities, and in every dimension it excludes all simplicial/simple local minimizers except the cross-polytope/cube.

## 4. Symmetric admissible speeds in general dimension

Let `P=-P subset R^n` be a full-dimensional centrally symmetric polytope. Write

- `V=V(P)` for its number of vertices,
- `F=F(P)` for its number of facets,
- `m(G)` for the number of vertices of a facet `G`,
- `I=sum_G m(G)` for the vertex--facet incidence total.

Fix `theta in S^{n-1}`. A **symmetric speed** is a number `alpha_x` for each vertex with

`alpha_{-x}=-alpha_x`.

It is `theta`-admissible when, for every facet `G`:

1. if `theta notin lin(G-G)`, the values `alpha_x` on `Vert(G)` are restrictions of one affine function on `aff G`;
2. if `theta in lin(G-G)`, there is no condition from `G`.

Denote the linear space by `A^s_theta(P)`.

The `n`-dimensional trivial speeds are

`alpha_x = w dot x`, `w in R^n`.

They form an `n`-dimensional subspace because the vertices span `R^n`.

Define

`C_theta(P) := (1/2) sum_{G: theta in lin(G-G)} (m(G)-n)`.

The factor `1/2` is natural because facets come in opposite pairs.

### Proposition 4.1 — dimension-free incidence lower bound

For every centrally symmetric `n`-polytope and every `theta`,

`dim A^s_theta(P) >= (V-I+nF)/2 + C_theta(P)`.

#### Proof

Oddness leaves exactly `V/2` free vertex variables. On an `(n-1)`-dimensional facet `G`, an affine function has `n` degrees of freedom. Therefore, if `theta` is not parallel to `G`, requiring `m(G)` assigned values to come from an affine function imposes at most `m(G)-n` independent homogeneous linear restrictions.

The opposite facet `-G` imposes the same restrictions once oddness is imposed: if `ell_G` interpolates the values on `G`, then `x -> -ell_G(-x)` interpolates the prescribed values on `-G`. Thus each opposite nonparallel pair costs at most `m(G)-n`, not twice that number. Parallel pairs cost zero. Hence

`dim A^s_theta(P)
 >= V/2 - (1/2) sum_{G: theta notin lin(G-G)} (m(G)-n)`.

Since `sum_G (m(G)-n)=I-nF`, separating the parallel terms gives exactly

`dim A^s_theta(P) >= (V-I+nF)/2+C_theta(P)`.

QED.

This proposition is pure linear algebra; no inequality conjecture is used.

## 5. Why nontrivial admissible speeds contradict local Mahler minimality

The next point is the deformation mechanism, not just a dimension count.

### Lemma 5.1 — short admissible flows preserve the needed polyhedral structure and have affine volume

Let `alpha in A^s_theta(P)` and move each vertex by

`x(t)=x+t alpha_x theta`.

For sufficiently small `|t|`, the resulting centrally symmetric polytope

`P_t=conv{x(t): x in Vert(P)}`

has the same labeled facet incidences as `P`, and `t -> |P_t|` is affine.

#### Proof

For a nonparallel facet `G`, admissibility says `alpha|_G` is affine. Thus the map

`x -> x+t alpha_x theta`

restricted to `aff G` is an affine map; all moved vertices of `G` remain in a single moving hyperplane `H_G(t)`. For a parallel facet, every displacement is tangent to `aff G`, so those vertices stay in the original facet hyperplane.

At `t=0`, every vertex not belonging to `G` has strictly positive supporting-hyperplane slack. There are finitely many facet/nonvertex pairs. Continuity therefore gives one `epsilon>0` for which, for every old facet and every `|t|<epsilon`, its moved hyperplane supports `P_t` and its contact vertices are exactly the moved old facet vertices. The old facets hence persist with their labeled incidences. The finite boundary complex varies continuously and remains an embedded polyhedral sphere, so it exhausts the boundary; no additional facet can appear without replacing one of these supported cells. Thus the labeled face lattice is unchanged for a shorter interval if necessary.

Fix a triangulation of this boundary complex using only its vertices, and cone every boundary `(n-1)`-simplex to the origin. Central symmetry keeps the origin in the interior. Each resulting oriented `n`-simplex has determinant

`det(x_1+t alpha_1 theta, ..., x_n+t alpha_n theta)`.

All terms containing `theta` in two columns vanish, so the determinant is affine in `t`. Its sign is unchanged for small `t`. Summing the simplex volumes shows `|P_t|` is affine.

QED.

### Proposition 5.2 — local-minimizer shadow rigidity

If `P=-P` is a local minimum of the volume product among origin-symmetric convex bodies (Hausdorff topology), then every symmetric admissible speed is trivial. Consequently

`dim A^s_theta(P)=n`

for every `theta`.

#### Proof

Take any admissible speed and the short flow from Lemma 5.1. The volume is affine. Since `P=P_0` is a local minimum of `P(K)=|K||K^circ|` along this shadow system, the Meyer--Reisner polar-volume convexity theorem and its rigidity corollary imply that the volume product is constant on a short two-sided interval and that the bodies are related by affine shear maps of the form

`A_t(x)=x+t((w dot x)+beta) theta`.

Every `P_t` is origin-symmetric, hence has centroid zero. Since the centroid of `A_t(P)` is `t beta theta`, central symmetry forces `beta=0`. Face-lattice persistence labels the vertices continuously, so the velocity of vertex `x` equals `w dot x`. Thus `alpha_x=w dot x`, i.e. the speed is trivial.

The trivial speeds already form an `n`-dimensional subspace, so `A^s_theta(P)` has dimension exactly `n`.

QED.

Combining Propositions 4.1 and 5.2 gives the necessary condition

`(V-I+nF)/2 + C_theta(P) <= n`                         (5.1)

for every direction `theta` at any centrally symmetric polyhedral local minimizer.

This is the central new mathematical output of the run. Priority is **UNVERIFIED**: the argument is written in full here, but the bounded literature search did not establish whether this dimension-free formulation is already folklore or explicitly published.

## 6. Specialize the obstruction to dimension four

Now `n=4`. For generic `theta` parallel to no facet, `C_theta=0`, so (5.1) gives

`I >= V+4F-8`.                                         (6.1)

Polarity is a continuous involution on origin-symmetric bodies containing the origin in their interiors and preserves the volume product. Hence a local minimizer `P` has a local-minimizer polar `P^circ`. Vertex--facet incidence is duality-invariant, while `V` and `F` exchange. Applying (6.1) to `P^circ` gives

`I >= F+4V-8`.                                         (6.2)

Thus every 4D polyhedral local minimizer must satisfy

`I >= max(V+4F-8, F+4V-8)`.                            (6.3)

This is **B11**: the obstruction is simultaneously primal and dual.

There is a stronger directional version. If a facet `G` has `q=m(G)` vertices, choose nonzero `theta in lin(G-G)`. Its opposite facet is also parallel, and the pair contributes `q-4` to `C_theta`. Therefore (5.1) yields

`I >= V+4F+2q-16`.                                     (6.4)

With `q_max=max_G m(G)`, (6.4) holds with `q=q_max`. Applying it to the polar gives the dual inequality

`I >= F+4V+2r_max-16`,                                 (6.5)

where `r_max` is the largest number of facets incident to one vertex of `P`.

These are exact necessary inequalities, not sampled curvature data.

## 7. All-dimensional structural corollary: simple/simplicial local minima

### Corollary 7.1

In every dimension `n>=2`, the only centrally symmetric **simplicial** polytope that can be a local minimum of the volume product is an affine cross-polytope. By polarity, the only centrally symmetric **simple** polytope that can be a local minimum is an affine cube/parallelotope.

#### Proof

If `P` is simplicial, every facet has exactly `n` vertices, so `I=nF` and `m(G)-n=0` for every facet. Proposition 4.1 therefore gives

`dim A^s_theta(P) >= V/2`

for every direction. Local minimality requires this dimension to be at most `n`, hence `V<=2n`. A full-dimensional centrally symmetric polytope has at least `2n` vertices: choose one vector from each antipodal pair; fewer than `n` pairs cannot span `R^n`. Therefore `V=2n`.

There are exactly `n` antipodal pairs `+-v_1,...,+-v_n`, and full dimensionality makes `v_1,...,v_n` a basis. Hence

`P=conv(+-v_1,...,+-v_n)`

is an affine image of the cross-polytope.

For a simple local minimizer `P`, the polar is a simplicial local minimizer, hence an affine cross-polytope. Polarizing again makes `P` an affine cube.

QED.

This does **not** prove Mahler for every simple or simplicial body. It says a genuine global/local minimizing counterexample cannot remain in either class; a minimization/deformation argument can exit such a stratum at its boundary. That boundary issue is part of the remaining source gap.

## 8. A sharper ten-vertex 4D obstruction

Let a 4D centrally symmetric candidate have `V=10`. A facet cannot contain both `x` and `-x`, because a proper supporting hyperplane cannot contain an antipodal pair of boundary vertices. There are five antipodal vertex pairs, so every facet has at most five vertices. Every 4D facet has at least four vertices. Thus every facet has size 4 or 5.

Let `p` be the number of **opposite facet pairs** whose facets have five vertices. Then

`I=4F+2p`,

and the generic dimension lower bound is

`(V-I+4F)/2 = 5-p`.

For any `k<=3` chosen five-vertex facet pairs, the `k` corresponding three-dimensional linear hyperplanes in `R^4` have a nonzero common direction, because their intersection has dimension at least `4-k`. Choose `theta` in that intersection. Each selected opposite pair contributes one to `C_theta`, so

`dim A^s_theta(P) >= 5-p+k`.

If `p<=3`, take `k=p` and obtain

`dim A^s_theta(P) >= 5>4`,

contradicting local-minimizer rigidity. Therefore

`p>=4`.                                                 (8.1)

So a shadow-rigid ten-vertex candidate must have **at least eight five-vertex facets**. If `p=4`, the four facet-parallel hyperplanes must have trivial common intersection; otherwise choosing a common nonzero direction gives `C_theta>=4` and again dimension at least five. Equivalently, their four facet normals must span `R^4`.

This is a concrete combinatorial narrowing of the smallest post-cross-polytope vertex count; it is not a proof of the conjecture.

## 9. B2 exact negation test: a natural ten-vertex candidate fails maximally

Before running code I selected

`P_* = conv(+-e_1,...,+-e_4,+-u)`, `u=(1,1,1,1)`.

The exact-integer/rational checker

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T03-12-00Z__mahler_shadow4_exact_check.py`

exhaustively enumerates supporting facets from all 4-subsets and verifies the facet hyperplanes with exact SymPy arithmetic. Its archived output is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T03-12-00Z__mahler_shadow4_exact_check.out`.

Actual executed output:

`VERTICES = 10`

`FACETS = 30`

`FACET_SIZE_COUNTS = {4: 30}`

`OPPOSITE_FACET_PAIRS = 15`

`INCIDENCE_I = 120`

`GENERIC_DIM_LOWER_BOUND = 5`

`EXPLICIT_ODD_SPEED_NONTRIVIAL = True`

`TEN_VERTEX_SHADOW_RIGID_REQUIRES_P_GE_4 = True`

`ALL_EXACT_CHECKS_PASS = True`.

Thus this natural exact candidate is simplicial, not shadow-rigid. An explicit nontrivial odd speed is

`alpha(+-e_i)=0`, `alpha(u)=1`, `alpha(-u)=-1`.

It is not globally linear because the zero values on `e_1,...,e_4` force `w=0`, while `alpha(u)=1`. Since every facet is a tetrahedron, arbitrary speed values on a facet extend affinely; hence this odd speed is admissible for every direction. Proposition 5.2 rules out local minimality without any numerical volume-product computation.

This is the requested counterexample-first work: an attempted small structured minimizer candidate fails for a rigorous reason, and the failure identifies what a real 10-vertex obstruction would need (at least four opposite pairs of nonsimplicial five-vertex facets).

## 10. What the three methods accomplished

**B2 — attack the negation.** The exact `+-e_i,+-u` ten-vertex candidate is decisively non-rigid. More generally, every simplicial candidate in every dimension is excluded from local minimality unless it is the cross-polytope.

**B5 — add a parameter and differentiate/deform.** The parameterized odd shadow flow converts local Mahler minimality into a rigidity statement. The new usable output is inequality (5.1), not another finite checker.

**B11 — dualize.** Polarity produces the simultaneous 4D incidence debts (6.1)--(6.5) and turns the simplicial classification into the simple classification.

The three routes meet at the same obstruction but are not copies of one another: B2 tests candidate geometry, B5 supplies the analytic deformation implication, and B11 imposes the independent dual combinatorics.

## 11. Source metric, auxiliary delta, and remaining full-scope gap

Source-relevant before/after:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Auxiliary progress, stated separately:

- proved the dimension-free admissible-speed lower bound and local-minimizer incidence obstruction;
- in dimension four obtained primal/dual inequalities (6.1)--(6.5);
- classified simple/simplicial centrally symmetric local minimizers in every dimension as cube/cross-polytope;
- for a 10-vertex 4D shadow-rigid candidate, forced at least four opposite pairs (eight facets) of five-vertex facets;
- exact candidate `conv(+-e_i,+-(1,1,1,1))` is certified simplicial with 30 tetrahedral facets and an explicit nontrivial admissible speed.

The full source gap is still large and explicit: in dimension four a minimizing sequence may converge to a nonsimple, nonsimplicial polytope (or, before polyhedral reduction, a nonpolyhedral body). The present incidence inequalities do not classify all shadow-rigid 4-polytopes and do not prove the sharp constant `4^4/4!=32/3`. A successful continuation must either classify the remaining 4D shadow-rigid face lattices, prove every global minimizer can be reduced to a tractable polyhedral class without increasing volume product, or introduce a stronger deformation that survives the nonsimple/nonsimplicial boundary.

This restricted progress remains `PARTIAL`, not `PROVED`.

## 12. Current literature / priority limits

Fresh searches included the exact conjecture aliases, `dimension four Mahler`, `shadow flow higher dimensions`, and recent local-minimality work. They recovered the 3D Chen--Li--Xi--Xu shadow-flow paper and a 2026 discrete-KKT local Hanner result, but no four-dimensional/global resolution and no exact match for Corollary 7.1 or inequalities (6.1)--(6.5). This negative search is not proof of novelty. The structural statements are therefore marked **priority UNVERIFIED** pending independent literature review.

## 13. Runtime / scheduler capability honesty

The actual model exposed to this run is **GPT-5.6 Sol**. Reasoning level is **UNVERIFIED**. It is not GPT-6 maximum and I do not claim otherwise.

The native scheduler interface still exposes schedule/title/prompt/timing/enabled controls but no model selector, reasoning-effort selector, or guaranteed execution duration. Therefore GPT-6/maximum remains prompt-requested only. Changing that requires platform support for a model/effort selector or an authorized execution interface that exposes those controls; a repository edit cannot do it.

Historical native modification probes for P26/P01/P03 included `You cannot modify this task`. The authorized workaround remains to use the owning account/workspace/interface or platform support; do not bypass the restriction and do not create duplicate schedules. This run made **no scheduler changes**.

## 14. Next genuinely different methods

Do not repeat B2/B5/B11 next run. The next triple should be:

- **B14 (find the group acting):** quotient 4D shadow-rigid incidence data by central symmetry and facet-normal projective symmetry;
- **B16 (compute every small case):** if an exact face-lattice source/enumerator is available, exhaust centrally symmetric 4-polytopes at the first feasible vertex/facet sizes against (6.1)--(6.5), clearly separating enumeration completeness from samples;
- **B24 (find the extremal object):** optimize the admissible-speed deficiency over incidence structures and identify whether a non-Hanner face lattice can actually attain equality in every directional debt.

No source closure or independent audit is requested by this report.

```text
ledger_delta:
  track: HARD7-01
  predecessor: BLYZ-LOG-BM-SYMMETRIC
  predecessor_action: RELEASED_AFTER_SECOND_SECTION_I_RECOVERY
  source_target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
  owner: HARD7-01
  status: PARTIAL
  source_metric: d_sym
  before: 3
  after: 3
  movement: NO
  methods: [B2, B5, B11]
  auxiliary: dimension-free shadow incidence obstruction; simple/simplicial local-minimum classification; 10-vertex p>=4 obstruction
  exact_checker: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T03-12-00Z__mahler_shadow4_exact_check.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T03-12-00Z__mahler_shadow4_exact_check.out
  closure: false
```
