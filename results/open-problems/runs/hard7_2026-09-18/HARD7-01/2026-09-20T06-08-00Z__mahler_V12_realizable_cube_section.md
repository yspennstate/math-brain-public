Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B1 / B20 / B26**.

# HARD7-01 — exact realization of the V=12 incidence boundary; combinatorial/shadow route is insufficient

**Status:** `PARTIAL / SOURCE OPEN / STUCK1 TRIGGERED`.

The symmetric Mahler conjecture is not solved here. The substantive result of this run is instead a sharp **negative result about the current proof route**: the entire `n=4,V=12,E=5` equality pattern isolated in the preceding shadow-flow/incidence analysis is genuinely realizable by an explicit rational centrally symmetric 4-polytope, including the two simultaneous full-spark conditions. Thus no argument using only the previous incidence debt, the antipodal circuit quotient, and cube-section realizability can improve the structural bound. The explicit polytope itself satisfies the Mahler inequality with a certified positive gap.

Priority of the explicit configuration as a literature statement is **UNVERIFIED**. It is not presented as a source solution.

## 1. Continuity, ownership, and evidence consumed

Canonical claim remains:

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`

owned exclusively by `HARD7-01`. The exact source target is

`P(K)=|K||K^circ| >= 4^n/n!`

for every origin-symmetric convex body `K=-K subset R^n`.

I resumed from

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T04-58-00Z__mahler_exact_quotient_and_V12_boundary.md`.

That report proved the exact shadow quotient criterion, the incidence debt

`I >= nF+V-2`,

and, in the first post-Lopez--Reisner case `n=4,V=12`, reduced equality to a codimension-two central section of the 6-cube with five antipodal edge-intersection pairs in five distinct coordinate directions, together with full-spark normal and circuit conditions.

This run reread/reconciled the controlling files `CONTROL.md`, `NEW_METHODS_2026-09-16.md`, `OWNER_DIRECTIVE.md`, root `POSTED.md` and `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the canonical claim, the newest own report, and repository alias searches for `Mahler conjecture`, `volume product`, `reverse Santalo`, `cube section`, and related log-concave/convex-geometric work. No ownership collision was found and no peer claim or shared root ledger was overwritten.

The mathematical route was written before code at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T05-12-00Z__idea_before_code_mahler_cube_edge_section.md`

(commit `456a138ccda070aa84c69815c82b143b2091fc2d`).

## 2. Fresh source/literature check

Bounded current searches on 20 September 2026 confirm the following relevant scope.

1. Chen--Li--Xi--Xu, *The Mahler Conjecture in Three Dimensions*, arXiv:2605.09334 (2026), proves the three-dimensional result and includes the symmetric 3D case by shadow flow. The companion symmetric preprint is arXiv:2605.13795. Neither is a dimension-four theorem.
2. Lopez--Reisner, *A special case of Mahler's conjecture*, Discrete Comput. Geom. 20 (1998), 163--177, DOI `10.1007/PL00000076`, proves the symmetric conjecture for polytopes with at most `2n+2` vertices or facets for `n<=8`; therefore `V<=10` is known in dimension four.
3. Daniel Martin Jimenez Cuevas, *A Discrete KKT Variational Characterization of the Local Minimality of the Mahler Volume in Centrally Symmetric Polytopes*, arXiv:2606.14709 (2026), gives an exact KKT stationarity framework and strict local minimality/stability of the Hanner orbit. It does not classify all 12-vertex 4-polytopes or prove the global conjecture.
4. Agam Guberman, *A connection between the Mahler conjecture and floating bodies*, arXiv:2608.10994 (11 Aug 2026), studies combinatorial structure of volume-product minimizers; the abstract does not state a global four-dimensional resolution.
5. A fresh bounded search found no verified theorem settling the full symmetric dimension-four conjecture. This is a bounded negative search, not a worldwide openness certificate.

## 3. B1: exact change of category

Let `P=conv{+-v_1,...,+-v_6}` be a centrally symmetric 4-polytope, let `A:R^6->R^4` send `e_i` to `v_i`, and let `K=ker A` have dimension two. Choose a `2 x 6` matrix `B` with row space `K`. Then `A^T` identifies the polar with

`P^circ ~= L cap [-1,1]^6`, where `L=K^perp=ker B`.

In the equality case from the previous report, five nonsimplicial facet pairs omit five distinct antipodal vertex-pair indices. Relabel them `1,...,5`; index `6` is common to all five. Orient one vertex from each antipodal polar pair so its sixth coordinate is `+1`. The five points lie in

`H=L cap {x_6=1}`,

a 3-dimensional affine section of the 5-cube facet `[-1,1]^5 x {1}`. Point `q^(j)` must lie in the relative interior of an edge parallel to coordinate `j`.

Thus the hoped-for obstruction became a finite-sign/continuous-diagonal problem: can a 3-flat in the 5-cube hit five edge interiors, one in every coordinate direction, while satisfying the two full-spark conditions?

## 4. B20: contraction identities for a five-edge section

Write the five oriented edge points as rows of `Q=[M|1]`, where

- `M_jj=t_j`, `|t_j|<1`;
- `M_ij in {+1,-1}` for `i!=j`.

Because they lie in one 3-flat in the slice `x_6=1`, there is an affine dependence `lambda !=0` with

`lambda^T M=0`, `sum_i lambda_i=0`.

For column `j`, define

`S_j={i != j: M_ij=-1}`.

Using `sum lambda_i=0`, the column equation is exactly

`sum_{i in S_j} lambda_i = -c_j lambda_j`,

where

`c_j=(1-t_j)/2 in (0,1)`.                         (4.1)

So realizability requires five strict signed-subset contractions with one common zero-sum vector `lambda`. This is the precise B20 obstruction; unlike the preceding scalar incidence budget, it remembers the sign pattern.

The negation-first hope was that (4.1), together with full-sparkness, might be impossible. It is not.

## 5. B26: an exact rational sporadic realization

Take the five oriented edge points

`q1=( 1/6,-1,  -1,   1,    1, 1)`,

`q2=( 1,   1/7,-1,  -1,   -1, 1)`,

`q3=(-1,   1,  -1/4, 1,    1, 1)`,

`q4=(-1,  -1,   1,  -1/9,  1, 1)`,

`q5=(-1,   1,   1,  -1,  -1/6, 1)`.

Let

`B = [[564,245,224,-189,564,0],`

`     [564,140,504, 315,  0,235]]`.                (5.1)

Direct exact multiplication gives `B q_j^T=0` for every `j`. Hence all five points belong to the four-dimensional subspace `L=ker B` and each is in the relative interior of the required cube edge.

The unique affine dependence of the five points is

`lambda=(-12,7,8,9,-12)`,                            (5.2)

whose coefficients are all nonzero. Therefore every four of `q1,...,q5` are affinely independent in the slice `x_6=1`; equivalently, since `A^T` below is injective, every four associated facet normals are linearly independent.

For (4.1) one may take

`S1={3,4,5}, S2={1,4}, S3={1,2}, S4={2,5}, S5={2}`

with indices displayed one-based. Substitution of (5.2) gives `0<c_j<1` and exactly the five diagonal values `1/6,1/7,-1/4,-1/9,-1/6` above.

The first five column directions of `B` are pairwise nonparallel: every `2 x 2` determinant made from two of columns `1,...,5` is nonzero. Parameterizing `K=row(B)` by `z in R^2`, the circuit line

`K cap {c_j=0}`

is the kernel of the linear functional `z -> z dot b_j`, where `b_j` is column `j` of `B`. Thus the five circuit lines are pairwise distinct, exactly as required by the equality theorem of the previous run.

### Proposition 5.3 — the entire equality incidence pattern is realized

Let

`L=ker B`, `C=L cap [-1,1]^6`.

Then `C` has exactly 22 vertices: 12 have exactly four saturated cube coordinates and 10 have exactly five saturated coordinates. The ten five-saturated vertices are precisely

`+-q1,...,+-q5`.

Moreover every one of the twelve coordinate inequalities `x_i=+-1` cuts a 3-dimensional facet of `C`.

#### Proof

A vertex of a four-dimensional linear section of a cube has at least four independent active cube inequalities. Consequently every vertex is captured by choosing four saturated coordinates, assigning their `+-1` signs, and solving the two equations `Bx=0` for the remaining two coordinates whenever the corresponding `2 x 2` minor of `B` is nonzero. Conversely every resulting point in the cube with rank-four active restrictions is a vertex.

The exact checker exhausts all `C(6,4) 2^4=240` saturated choices using rational arithmetic only, deduplicates the solutions, and obtains exactly the stated 22 vertices and saturation histogram `{4:12,5:10}`. It separately verifies that the ten five-saturated vertices equal `+-q1,...,+-q5`. For each coordinate/sign pair, it computes the affine rank of all section vertices satisfying that equality and obtains rank three, proving each coordinate inequality supports a genuine facet. No floating acceptance test is used. QED.

Now choose `A` to have rows `q1,q2,q3,q4`. These four rows are independent and `BA^T=0`; since both row space of `A` and `L` have dimension four,

`row(A)=L`.

Let `v_i` be column `i` of `A` and set

`P=conv{+-v_1,...,+-v_6}`.

The map `y -> A^T y` identifies `P^circ` with `C`. Since all twelve coordinate inequalities cut facets of `C`, all twelve points `+-v_i` are genuine vertices of `P`. Vertices of `C` correspond to facets of `P`, and the number of saturated coordinates is the number of vertices in that facet. Hence

- `V(P)=12`;
- `F(P)=22`;
- exactly 10 facets (five opposite pairs) have five vertices;
- the remaining 12 facets are tetrahedral;
- the total vertex--facet incidence count is

`I=10*5+12*4=98=4F+V-2`.

Thus the sharper incidence bound from the previous run is attained by a genuine centrally symmetric 4-polytope satisfying both full-spark equality conditions. QED.

This is the decisive outcome of B26: **joint cube-section realizability is not the missing contradiction.**

## 6. Exact volume-product test of the realized polytope

The same exact checker computes the volume product of this explicit `P`. It obtains

`|P| = 36937/4536`,

`|P^circ| = 17281169/11938752`,

and therefore

`P(P)=638314539353/54154179072`

`     =(638314539353/577644576768)*(32/3)`

with

`638314539353/577644576768 = 1.105029918... > 1`.

Equivalently the exact additive gap above the conjectured four-dimensional minimum is

`60669962585/54154179072 = 1.120319126...`.

So this exact realizable incidence-boundary polytope is **not** a Mahler counterexample and is not itself an equality body.

### Why the volume computation is exact

The checker does not use Qhull, floating-point hull acceptance, or numerical quadrature. From the exactly enumerated face incidences it computes four-dimensional volume by a deterministic rational subdivision: for each 3D facet take its vertex-average, cone it to every 2D ridge; for each ridge take its vertex-average and cone it to every edge; finally cone every resulting boundary tetrahedron to the origin. Every simplex volume is a rational `4 x 4` determinant divided by `4!`. The same construction is applied to `P^circ`, whose twelve facets are the coordinate equalities of the section. Thus the displayed rational volumes are finite exact claims, not fitted decimals.

Artifact:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T05-42-00Z__mahler_V12_exact_section_check.py`

Archived output:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T05-42-00Z__mahler_V12_exact_section_check.out`

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

## 7. What the three methods did

**B1 — change the category.** The `V=12,E=5` Mahler boundary became a 3-flat/5-cube edge-incidence problem. This made the exact obstruction algebraic rather than a vague 4-polytope classification issue.

**B20 — find why the algorithm fails.** The no-realization algorithm fails because the signed-subset contraction system (4.1) has full-spark rational solutions. The missing ingredient is not another incidence inequality of the same type.

**B26 — hunt the sporadic case.** This succeeded in the strongest useful negative sense: an exact rational section realizes all previously derived equality conditions. Its exact volume product lies about `10.5%` above the Mahler minimum, so the next route must use analytic stationarity/volume information, not merely realizability.

## 8. Source metric and auxiliary delta

Frozen source metric:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Source status remains `OPEN`; track status remains `PARTIAL`.

Auxiliary delta, separately:

- exact contraction formulation for five-edge cube-section realizability;
- explicit rational `B` and five edge points satisfying it;
- exact realization of the `V=12,F=22,I=98` equality incidence boundary;
- simultaneous full-spark normal and circuit conditions both certified;
- exact volume product of the realized polytope, with positive Mahler gap;
- therefore a rigorous obstruction to continuing the same combinatorial/shadow-incidence route unchanged.

None of these moves `d_sym`.

## 9. Section-I STUCK1 trigger

This is the third consecutive Mahler-target run with `d_sym=3`. The owner protocol therefore marks the target **STUCK1** and requires the next run to change method within this problem.

### (a) Exact blocking statement

The first source-relevant special case beyond the Lopez--Reisner theorem remains

`inf { |P||P^circ| : P=-P subset R^4, P a polytope with V(P)=12 } >= 32/3`.   (9.1)

Even the narrower equality-incidence subclass `V=12,F=22,I=98` is not settled uniformly. This run proves only one exact member of that class has positive gap.

### (b) Routes tried and precise failures

1. **Admissible-shadow incidence debt:** gave necessary local-minimizer inequalities but no volume lower bound.
2. **Antipodal circuit quotient/full-spark rigidity:** sharpened the necessary conditions but an abstract equality configuration survived.
3. **Cube-section realizability:** hoped to kill the abstract configuration; this run explicitly realizes it, so that hoped-for contradiction is false.
4. **One exact volume test:** certifies one realizable section is safely above `32/3`, but says nothing uniform about the continuous family of all 12-vertex configurations.

### (c) What a proof now has to contain

A successful continuation needs an ingredient that couples the **continuous coordinates** to volume-product stationarity: e.g. a source-valid KKT/first-variation condition, a floating-body restriction, or a deformation showing every non-Hanner stationary 12-vertex configuration admits a volume-product decreasing direction. Pure incidence rank data cannot suffice, because the exact construction above saturates all of it.

### (d) Simplest special case still unproved

The clean next milestone is (9.1), or more narrowly the complete `V=12,F=22,I=98` family. A single witness or finite sign type is not enough; the continuous parameters must be controlled.

### (e) Nearest solved analogue and missing mechanism

- **Source class:** Lopez--Reisner 1998 proves the full inequality for at most `2n+2` vertices/facets for `n<=8`, hence through `V=10` in dimension four. The present run sits exactly at the next vertex count.
- **Technique analogue:** arXiv:2606.14709 supplies an exact KKT/second-variation mechanism proving strict local minimality of Hanner configurations. What the current shadow-incidence route lacks is precisely such a coordinate-sensitive stationarity inequality for the non-Hanner `V=12` family.

**Chosen recovery for the next run:** port the KKT/stationarity technique from the nearest solved local-minimality theory into the explicit six-generator/codimension-two parameterization. The next Section-B triple should be new for this Mahler target: **B6 / B18 / B22** (deform to a Hanner point; rewrite the surviving family in KKT/Gale language; read the failures/limitations of the existing local-minimality proofs before differentiating).

## 10. Runtime and scheduler capability honesty

Actual model exposed to this run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. It is not GPT-6 maximum, and I do not claim otherwise.

The currently exposed native automation interface still provides task title, prompt, schedule, timing mode and enabled state, but **no model selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains a prompt request only. Changing this requires a platform interface/account capability that actually exposes model/effort controls (or platform support); a GitHub edit cannot change it.

The repository policy records historical native modification probes for P26/P01/P03 returning `You cannot modify this task`, while a later authorized context successfully updated P26. No scheduler modification or permission probe was attempted in this run because the owner explicitly forbids scheduler changes here. If an edit is denied in a particular context, the valid workaround is to use the authorized owning account/workspace/interface or platform support; do not bypass it and do not create a duplicate schedule.

```text
ledger_delta:
  track: HARD7-01
  source_target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
  owner: HARD7-01
  status: PARTIAL
  stuck_state: STUCK1_TRIGGERED
  source_metric: d_sym
  before: 3
  after: 3
  movement: NO
  methods: [B1, B20, B26]
  new_exact_result: explicit rational V12 F22 I98 centrally symmetric 4-polytope realizes the entire shadow/circuit equality boundary
  exact_volume_product: 638314539353/54154179072
  exact_mahler_excess: 60669962585/54154179072
  checker: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T05-42-00Z__mahler_V12_exact_section_check.py
  output: artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T05-42-00Z__mahler_V12_exact_section_check.out
  output_last_line: ALL_EXACT_CHECKS_PASS = True
  next_recovery: port KKT/stationarity into V12 Gale/cube-section parameterization
  next_methods: [B6, B18, B22]
  closure: false
```
