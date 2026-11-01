Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B14 / B16 / B24**.

# HARD7-01 — exact antipodal quotient for shadow rigidity, a sharper incidence theorem, and the first post-Lopez--Reisner 4D boundary

**Status:** `PARTIAL / SOURCE OPEN`.

The symmetric Mahler conjecture is not solved here. This run produces a stronger exact formulation of the shadow-speed obstruction, corrects one analytic phrasing from the previous report, identifies a previously missed 1998 theorem covering the ten-vertex regime, and moves the structural attack to the first vertex count not covered by that theorem. Priority of the new auxiliary structural statements is **UNVERIFIED**.

## 1. Continuity, ownership, and evidence consumed

The canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned by `HARD7-01`. The exact source target is the origin-symmetric Mahler inequality

`P(K):=|K||K^circ| >= 4^n/n!`

for every origin-symmetric convex body `K=-K subset R^n`. The non-symmetric Santaló-centered conjecture is not claimed.

I resumed from

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T03-20-00Z__mahler_shadow4_incidence.md`.

That report had `d_sym=3`, proved a dimension-count obstruction for admissible shadow speeds, and left the proposed next methods B14/B16/B24. I did not restart the older BLYZ/log-Brunn--Minkowski target; its second Section-I recovery and terminal handoff remain preserved.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current Mahler claim and the newest HARD7-01 report;
- repository alias searches for `Mahler`, `volume product`, `reverse Santaló`, and `floating body`.

No equivalent active repository owner was found by those bounded alias searches. No claim file or shared ledger was overwritten. The source claim remains exclusive to HARD7-01.

The mathematical idea was persisted **before code** at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T04-32-00Z__idea_before_code_mahler_quotient_rigidity.md`.

## 2. Current literature check and a necessary prior-art correction

### 2.1 The ten-vertex 4D regime is already known

A fresh search recovered M. A. Lopez and S. Reisner,

* A special case of Mahler's conjecture, Discrete Comput. Geom. 20 (1998), 163--177,
* DOI `10.1007/PL00000076`,
* source page: `https://cris.haifa.ac.il/en/publications/a-special-case-of-mahlers-conjecture/`.

The abstract states that the symmetric Mahler conjecture is proved for polytopes with at most `2n+2` vertices (or facets) for `n<=8`, with the minimal bodies characterized.

Therefore, in dimension four, **every symmetric polytope with at most ten vertices or at most ten facets is already in a rigorously solved regime**. The preceding run's exact ten-vertex shadow calculation is still a correct internal structural test, but it is not a new source theorem and must not be advertised as such. The first vertex count beyond the scope of this particular Lopez--Reisner theorem is `V=12`.

This is a literature correction, not a mathematical regression of the source metric: `d_sym` was and remains 3 because Lopez--Reisner covers a restricted polytope class, not every symmetric body in dimension four.

### 2.2 Shadow systems: correction of the previous analytic phrasing

I read the relevant pages of Fradelizi--Meyer--Zvavitch,

* *An Application of Shadow Systems to Mahler's Conjecture*, Discrete Comput. Geom. 48 (2012), 721--734,
* DOI `10.1007/s00454-012-9435-3`,
* author PDF `https://www.math.kent.edu/~zvavitch/FMZ-2-11-2011.pdf`.

Their Proposition 1 gives the Meyer--Reisner convexity/equality statement for the reciprocal Santaló-polar volume along a shadow system. Their Corollary 2 says: when the primal volume is affine, the **volume product is quasi-concave**, and if an interior parameter is a minimum, the product is constant on at least one of the two one-sided subintervals.

The preceding HARD7-01 report said too quickly that local minimality plus the Meyer--Reisner input makes the product constant on a short two-sided interval. The correct argument only needs **one-sided constancy**. Reparameterize the constant one-sided interval as a nondegenerate shadow-system interval and then apply the equality clause of Proposition 1. The affine-shear conclusion survives unchanged. I give the corrected argument below.

### 2.3 2026 neighboring literature

Bounded searches on 20 September 2026 also recovered:

- Chen--Li--Xi--Xu, *The Mahler Conjecture in Three Dimensions*, `arXiv:2605.09334`, solving the general three-dimensional conjecture and giving a new proof of the symmetric 3D case via shadow flow;
- Daniel Martin Jimenez Cuevas, *A Discrete KKT Variational Characterization of the Local Minimality of the Mahler Volume in Centrally Symmetric Polytopes*, `arXiv:2606.14709`, on local Hanner/KKT structure;
- Agam Guberman, *A connection between the Mahler conjecture and floating bodies*, `arXiv:2608.10994`, whose abstract explicitly concerns the combinatorial structure of volume-product minimizers.

I did not obtain a source-level theorem match showing that the exact quotient statement below is new. Because the 2026 papers are very close in theme, **priority remains UNVERIFIED**. A bounded negative search is not a novelty certificate.

No four-dimensional/global solution was found in this bounded search, but that sentence is likewise not a worldwide openness proof.

## 3. Corrected local shadow-rigidity step

I first record the analytic implication needed by the new linear-algebra reduction.

### Lemma 3.1 — corrected one-sided shadow rigidity

Let `P=-P subset R^n` be a centrally symmetric polytope and let `alpha` be an odd admissible speed in direction `theta`. Move each vertex by

`x(t)=x+t alpha_x theta`

and put `P_t=conv{x(t)}`. Suppose `P=P_0` is a local minimizer of the volume product among origin-symmetric convex bodies. Then the speed is trivial:

`alpha_x = w dot x`

for one `w in R^n` and every vertex `x`.

#### Proof

The previous run proved the elementary polyhedral part: admissibility keeps every nonparallel facet coplanar, moves parallel facets tangentially, and hence preserves the labeled face incidences for sufficiently small two-sided `|t|`. Triangulating the fixed boundary complex and coning to the origin shows `t -> |P_t|` is affine, because every simplex determinant contains the shadow direction in at most one nonzero multilinear term.

The family is centrally symmetric because the speed is odd. Since `P_0` is a local volume-product minimum, for sufficiently small `c>0`,

`P(P_0)=min_{t in [-c,c]} P(P_t)`.

Fradelizi--Meyer--Zvavitch Corollary 2 applies because the primal volume is affine. It yields constancy of `P(P_t)` either on `[0,c]` or on `[-c,0]`. Choose the constant side and reparameterize a nontrivial closed subinterval of it onto a symmetric parameter interval. Proposition 1's equality characterization then says the bodies on that interval are related by affine shears of the form

`x -> x+t((w dot x)+beta) theta`

after the harmless affine reparameterization of `t`.

Each `P_t` is centrally symmetric about the origin. The center of a full-dimensional centrally symmetric body is unique, so the affine map taking `P_0` to `P_t` must send `0` to `0`. Thus its translation term vanishes, `beta=0`. Face-lattice persistence continuously identifies every labeled vertex, so taking the one-sided derivative at `t=0` gives

`alpha_x=w dot x`

for each vertex. QED.

This repairs the previous phrasing while preserving the rigidity conclusion actually used below.

## 4. B14: the exact antipodal quotient, not merely a constraint count

The previous report bounded the dimension of admissible speeds by counting possible facet constraints. There is a more exact description after quotienting central symmetry.

Let

`Vert(P)={+-v_1,...,+-v_r}`

with `v_1,...,v_r` chosen representatives. Let

`A:R^r -> R^n,   Ae_i=v_i`,

and put

`K:=ker A`, so `dim K=r-n`.

An odd speed is specified by a vector `y in R^r` through

`y_i=alpha(v_i)`, `alpha(-v_i)=-y_i`.

For an opposite facet pair `{G,-G}`, let `S_G subset {1,...,r}` be the indices of the antipodal vertex pairs represented in `G`. A proper facet never contains both `v_i` and `-v_i`. Define

`K_G := {c in K : supp(c) subset S_G}`.

If `m(G)=|S_G|`, then

`dim K_G=m(G)-n`.                                      (4.1)

Indeed, the vertices of `G` affinely span an `(n-1)`-dimensional supporting hyperplane that does not contain the origin; consequently they span `R^n` linearly, so the restricted matrix `A_{S_G}` has rank `n`.

### Proposition 4.2 — exact quotient formula for admissible speeds

For every nonzero shadow direction `theta`, with `H_G=lin(G-G)`,

`A^s_theta(P) = ( span{K_G : theta notin H_G} )^perp`  (4.2)

under the identification of odd speeds with `R^r`.

#### Proof

Suppose `G` contains the signed vertices `sigma_i v_i`, `i in S_G`. If `theta notin H_G`, admissibility requires the speed values on these vertices to be restrictions of one affine function on `aff G`.

Let the supporting equation of `G` be `phi(x)=1`. Every affine function `ell(x)+b` on `aff G` is the restriction of the linear functional `ell+b phi`, because `phi=1` there. Hence affine compatibility is equivalent to existence of `w in R^n` with

`alpha(sigma_i v_i)=w dot (sigma_i v_i)` for all `i in S_G`.

Oddness gives `alpha(sigma_i v_i)=sigma_i y_i`, and the signs cancel, so this is exactly

`y_i=w dot v_i  (i in S_G)`.

Thus `y|_{S_G}` belongs to the row space of `A_{S_G}`, equivalently it annihilates `ker A_{S_G}=K_G`. A facet parallel to `theta` supplies no constraint. Opposite facets supply the same condition after oddness. Intersecting all active annihilators gives (4.2). QED.

### Corollary 4.3 — exact local-minimizer criterion

If `P` is a local Mahler minimizer, then for every nonzero `theta`,

`span{K_G : theta notin H_G}=K`.                       (4.3)

#### Proof

Global linear speeds `y=A^T w` are exactly `K^perp` and have dimension `n`. Lemma 3.1 says every admissible speed at a local minimum is global linear. By (4.2), the annihilator of the active span is therefore exactly `K^perp`; taking orthogonal complements gives (4.3). QED.

This is strictly more informative than the previous dimension lower bound: it records **which circuit subspaces** must jointly span the antipodal dependency space, not only how many scalar constraints a facet could contribute.

## 5. B24: optimize the directional debt exactly

Choose one facet from each opposite pair and write

`e_G=m(G)-n >= 0`,

`E=sum_G e_G = (I-nF)/2`,                              (5.1)

where `I` is the total vertex--facet incidence count. Since `r=V/2`, (4.2) gives the previous lower bound

`dim A^s_theta(P) >= r-E + sum_{theta in H_G} e_G`.

At a local minimum the left side is `n`, so for every nonzero `theta`,

`sum_{theta in H_G} e_G <= E+n-r`.                    (5.2)

The point of B24 is to optimize (5.2) rather than inspect one facet at a time.

### Theorem 5.1 — sharper incidence debt

Let `P=-P subset R^n` be a centrally symmetric polyhedral local minimizer of the Mahler volume product. If `V=2r>2n`, then

`E >= r-1`,                                            (5.3)

or equivalently

`I >= nF+V-2`.                                         (5.4)

By polarity, if `F>2n`, then also

`I >= nV+F-2`.                                         (5.5)

#### Proof

Call a facet pair positive if `e_G>0`, and list the positive excesses in decreasing order.

There must be at least `n` positive facet pairs. If there were at most `n-1`, the intersection of all their `(n-1)`-dimensional linear hyperplanes `H_G` would contain a nonzero direction `theta`. Then the left side of (5.2) would equal `E`, forcing `E<=E+n-r`, i.e. `r<=n`, contrary to `r>n`.

Now take the `n-1` largest positive excesses. Their `n-1` hyperplanes again have a nonzero common direction. Using that direction in (5.2) gives

`e_(1)+...+e_(n-1) <= E+n-r`.

Each listed excess is a positive integer, so their sum is at least `n-1`. Therefore

`n-1 <= E+n-r`,

which is (5.3). Equation (5.4) follows from (5.1).

The polar `P^circ` is again a local volume-product minimizer, exchanges `V` and `F`, and preserves vertex--facet incidences. Applying (5.4) to `P^circ` yields (5.5). QED.

Compared with the previous generic-direction estimate `I>=nF+V-2n`, (5.4) gains exactly `2n-2` incidences.

## 6. Equality rigidity: two simultaneous full-spark configurations

The exact quotient (4.3) makes equality in Theorem 5.1 much more rigid than the scalar count suggests.

### Theorem 6.1 — equality structure

Under the hypotheses of Theorem 5.1, suppose `r>n` and `E=r-1`. Then:

1. exactly `r-1` opposite facet pairs are nonsimplicial;
2. every one has `e_G=1`, hence exactly `n+1` vertices;
3. any `n` of their facet-direction hyperplanes have trivial common intersection, equivalently the corresponding facet normals span `R^n`;
4. put `k=r-n=dim K`. The one-dimensional circuit spaces `K_G` of these `r-1` facets satisfy: **every `k` of them form a basis of `K`**.

#### Proof

In the proof of Theorem 5.1 the top `n-1` positive excesses satisfy

`n-1 <= sum_{j=1}^{n-1} e_(j) <= E+n-r=n-1`.

Hence those excesses all equal one. Since they are the largest positive excesses, every positive excess equals one. Their number is therefore `E=r-1`. This proves (1)--(2).

If some `n` positive facet-direction hyperplanes had a common nonzero direction `theta`, at least `n` unit excesses would be omitted from the active constraints. The remaining positive facets would number at most

`(r-1)-n = (r-n)-1 = k-1`.

Each active `K_G` is one-dimensional, so their span could have dimension at most `k-1`, contradicting the exact local-minimizer criterion (4.3). Thus any `n` facet normals span `R^n`, proving (3).

Finally choose any `k` of the `r-1` circuit lines and let `Q` be the complementary `n-1` positive facets. The hyperplanes of the facets in `Q` have a nonzero common direction `theta`. They are therefore inactive at `theta`. Criterion (4.3) still requires the active circuit spaces to span the `k`-dimensional space `K`. There are at most the chosen `k` lines left active. Consequently all chosen `k` must in fact remain active and must be linearly independent. Since the chosen `k` were arbitrary, every `k` circuit lines form a basis. QED.

This is a pair of dual-looking full-spark conditions: one in physical normal space `R^n`, one in the antipodal dependency space `K`.

## 7. The first post-Lopez--Reisner 4D vertex count: `V=12`

Set `n=4` and `V=12`, so `r=6` and `dim K=2`.

Theorem 5.1 gives

`E=(I-4F)/2 >= 5`,

hence

`I >= 4F+10`.                                          (7.1)

If equality holds, Theorem 6.1 says there are exactly five opposite pairs of five-vertex facets and every other facet is tetrahedral. Any four of the five nonsimplicial facet normals are independent. Their five circuit lines in the two-dimensional space `K` are pairwise distinct.

There is a further concrete consequence. A five-vertex facet uses five of the six antipodal vertex pairs, so it omits exactly one pair index `j`. For such a facet,

`K_G = K cap {c_j=0}`.

If two of the five nonsimplicial facet pairs omitted the same vertex-pair index, their one-dimensional circuit spaces would be identical, contradicting pairwise distinctness. Therefore:

> **Equality in (7.1) forces the five nonsimplicial facet pairs to omit five distinct antipodal vertex-pair indices. Exactly one antipodal vertex pair is represented in every nonsimplicial facet pair.**

This does not prove the twelve-vertex Mahler inequality. It gives a sharply constrained equality budget for a hypothetical local minimizer in the first vertex count beyond the Lopez--Reisner `2n+2` theorem.

## 8. A useful change of language: central sections of a six-cube

The quotient also exposes the next route cleanly.

Because `A` has rank `n`, `A^T:R^n -> R^r` is injective with image `K^perp`. Moreover

`P^circ = {y in R^n : |v_i dot y|<=1 for every i}`.

Therefore `A^T` identifies the polar with the central section

`Q = K^perp cap [-1,1]^r`.                             (8.1)

A facet of `P` with `m` vertices is dual to a vertex of `P^circ` at which exactly those `m` coordinate inequalities are saturated. Thus in the equality case `n=4,r=6,E=5`, the section `Q` is a four-dimensional central section of the six-cube with five antipodal vertex pairs lying in relative interiors of cube edges (five saturated coordinates), in five distinct coordinate directions. All simplicial facets of `P` correspond to section vertices with exactly four saturated coordinates.

This is a substantially smaller geometric realizability problem than arbitrary twelve-vertex 4-polytopes. It is the most promising continuation produced by this run: decide whether a codimension-two central section of the six-cube can realize the exact five-edge-pair pattern while satisfying the local-minimizer circuit spanning conditions. A negative answer would improve (7.1); a positive exact section would identify what an actual proof must still defeat analytically.

## 9. B16 exact checker and the negation test

Only after the preceding ideas were written did I build the exact checker

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T04-32-00Z__mahler_quotient_exact_check.py`

with archived output

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T04-32-00Z__mahler_quotient_exact_check.out`.

It uses only integer/Fraction Gaussian elimination and exhaustive integer partitions; there is no floating-point acceptance criterion.

Actual executed checks:

1. For dimension four and `r=5,...,10`, it enumerates every positive-integer excess multiset with total `E<=r-1`. The directional budget has no feasible multiset below `E=r-1`, and at equality the unique multiset is exactly `r-1` copies of one.
2. It verifies all five `4x4` determinants for the normal set

   `e_1,e_2,e_3,e_4,(1,1,1,1)`

   are `+-1`, so every four normals are independent.
3. It verifies the five circuit directions

   `(1,0),(1,1),(1,2),(1,3),(1,4)`

   are pairwise independent in `R^2`.
4. For every subset of the five normal hyperplanes having nonzero common intersection, it checks that the complementary abstract circuit lines span `R^2`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

### What the negation test says

The abstract five-normal/five-circuit configuration satisfies all of the **rank/debt** conditions at the equality budget `r=6,E=5`. Therefore the present incidence and abstract spanning inequalities alone cannot prove `E>=6`. That is a useful failure: the unpaid obligation is now **joint realizability by one polytope / one cube section**, or an additional volume/floating-body/KKT condition. Another incidence count with the same data will not close the twelve-vertex case.

The checker does **not** claim that the displayed abstract normal/circuit data are realizable by a centrally symmetric 4-polytope. It deliberately separates the exact combinatorial obstruction from the remaining geometric realizability problem.

## 10. What the three methods accomplished

**B14 — find the group acting.** Quotienting by antipodal symmetry turns odd vertex speeds into `R^r`, identifies trivial speeds with `K^perp`, and gives the exact active-circuit formula (4.2). This replaces a lossy scalar constraint count by a matroid/Gale-like dependency-space criterion.

**B16 — compute every small case.** Exact arithmetic verifies the optimized integer budget and shows the first 4D post-Lopez--Reisner equality pattern is internally consistent at the abstract rank level. The computation is a finite certificate for the stated finite claims only, not a Mahler proof.

**B24 — find the extremal object.** Optimizing the directional debt yields `I>=nF+V-2` and the full-spark equality classification. The extremal abstract `V=12,E=5` pattern survives, which pinpoints joint cube-section realizability as the next obstruction rather than suggesting false source closure.

## 11. Source metric and auxiliary delta

Frozen source metric:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Source status remains `OPEN`; research status remains `PARTIAL`.

Auxiliary progress, separately:

- corrected the local-rigidity use of FMZ from an overstrong two-sided phrasing to the source-valid one-sided quasi-concavity/equality argument;
- recovered Lopez--Reisner 1998 and removed any novelty implication from the already-known `V<=10` 4D regime;
- proved exact quotient formula (4.2) and local spanning criterion (4.3);
- strengthened the local-minimizer incidence debt from `I>=nF+V-2n` to `I>=nF+V-2` for `V>2n`, plus its polar dual;
- proved equality forces unit facet excesses and simultaneous full-spark normal/circuit configurations;
- specialized the first beyond-Lopez--Reisner count `V=12`: `I>=4F+10`, with a five-pentagonal-pair equality pattern and five distinct omitted antipodal pair indices;
- reduced equality realizability to a concrete codimension-two central section of the six-cube.

None of these is counted as movement of `d_sym`.

## 12. Remaining full-scope gap and next methods

The full dimension-four source theorem still requires the sharp bound

`P(K)>=4^4/4!=32/3`

for **every** origin-symmetric convex body, including nonpolyhedral bodies and polytopes outside any bounded vertex/facet class. The present route is a local-minimizer structural reduction only; it neither proves a global minimizing body is captured by the `V=12` class nor evaluates the volume product of the surviving class.

The next run should not repeat B14/B16/B24. The most concrete new triple is:

- **B1 (change the category):** work in the cube-section representation `K^perp cap [-1,1]^6` for the `V=12` equality boundary;
- **B20 (find why the algorithm fails):** characterize exactly when a codimension-two central section can have five antipodal cube-edge intersection pairs in five distinct coordinate directions;
- **B26 (hunt the sporadic case):** either construct one exact realizable section/polytope and compute its circuit/volume data, or rule out the five-edge pattern by a 3D facet/planar-zonotope obstruction.

If the source metric remains unchanged for the next two Mahler runs, the third unchanged run triggers the full Section-I stuck report; this run is only the second Mahler-target run after admission.

## 13. Runtime/capability honesty

Actual runtime model exposed to this run: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**. It is not GPT-6 maximum, and I do not claim otherwise.

The controlling repository policy still records that the native scheduler schema exposes title, prompt, schedule, timing mode and enabled state, but no model selector, reasoning-effort selector or guaranteed duration. GPT-6/maximum is therefore prompt-requested only. Changing that would require an authorized platform interface that actually exposes model/effort controls or platform support; a GitHub edit cannot do it.

The repository contains context-dependent scheduler history: `operations/NEW_METHODS_2026-09-16.md` records earlier `You cannot modify this task` probes for P26/P01/P03, while the newer compact `RESULTS.md` says P26 was successfully updated in another authorized context. I made no scheduler probe or change in this run. If a particular task is denied in the current owning context, the authorized remedy is the owning account/workspace/interface or platform support, not bypassing the restriction or creating a duplicate schedule.

```text
ledger_delta:
  track: HARD7-01
  source_target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
  owner: HARD7-01
  status: PARTIAL
  source_metric: d_sym
  before: 3
  after: 3
  movement: NO
  methods: [B14, B16, B24]
  literature_correction: Lopez-Reisner 1998 covers symmetric polytopes with <=2n+2 vertices/facets for n<=8; 4D V<=10 is known
  auxiliary: exact antipodal circuit quotient; I>=nF+V-2; equality full-spark theorem; V12 cube-section boundary
  exact_checker: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T04-32-00Z__mahler_quotient_exact_check.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T04-32-00Z__mahler_quotient_exact_check.out
  output_last_line: ALL_EXACT_CHECKS_PASS = True
  closure: false
```
