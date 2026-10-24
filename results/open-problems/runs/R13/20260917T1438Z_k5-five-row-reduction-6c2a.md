Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric `B_R13(n)`; supported stagnation is now 2. Auxiliary obstruction moved sharply: any counterexample to the candidate exact five-column value `(4+sqrt(142))/9` already exists with at most five rows, so the arbitrary-row `n=5` problem reduces to the square `5 x 5` case. Methods actually used: #25 COUNT THE SAME THING TWICE, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R13 — Boolean Komlós: five-row reduction at the candidate exact `n=5` threshold

Run ID: `20260917T1438Z_k5-five-row-reduction-6c2a`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source scope, and fixed metric

The target remains the **real Boolean** Komlós signing problem: for a real `m x n` matrix `A` with every column of Euclidean norm at most one, find `epsilon in {-1,+1}^n` minimizing `||A epsilon||_infinity`. Complex phases, rank-two/vector colorings, and average-case bounds are not substitutes.

Before research I recovered/read the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042/Bandeira intake record, the newest R13 report, recent Komlós commits/audits, and the neighboring R-series state. `QUEUE.md` still records Boolean Komlós as assigned R13 work, not a reserve target. No shared root or peer file was edited.

The newest complete R13 report before this run was

`runs/R13/20260917T1335Z_k5-priorart-obstruction-4e2b.md`

at commit `9655efef0b823e5465efd3f2273ccdfbe305ea5b`. It was the first unchanged upper-envelope run after the preceding movement, so this second unchanged upper-envelope run has supported stagnation count **2**.

The complete retained certified pointwise upper envelope remains

- `B_R13(1)=1`;
- `B_R13(2)=sqrt(2)`;
- `B_R13(3)=(sqrt(11)+sqrt(2))/3`;
- `B_R13(4)=sqrt(3)`;
- for `5 <= n <= 75`,
  `B_R13(n) <= min{ sqrt(3n/4), (sqrt(2)+1/2)*sqrt(ceil(n/5)) }`;
- for `n >= 76`,
  `B_R13(n) < 3 sqrt(2 pi)` from Guo--Fang--Lu.

The later finite entries are upper certificates unless separately proved exact. In particular, the certified five-column interval remains

`(4+sqrt(142))/9 <= K_5^* <= sqrt(2)+1/2`.

Thus the fixed upper metric did **not** move this run.

Fresh source navigation on 17 September 2026 remains separated correctly:

1. Bansal--Jiang, arXiv:`2508.03961`, gives the earlier full **Boolean** `\widetilde O((log n)^(1/4))` Komlós bound.
2. Guo--Fang--Lu, arXiv:`2609.11189`, submitted 10 September 2026, states the unrestricted deterministic **real Boolean** theorem with universal bound `< 3 sqrt(2 pi)`.
3. Guillen--Kobzar, arXiv:`2609.15071`, submitted 14 September 2026, allows arbitrary unit-modulus complex phases; for real vectors this is rank-two vector discrepancy, not Boolean signing.
4. Belhaouari--AlQudah (2019 preprint; Contemporary Mathematics 2024) advertises exact small-dimensional values in the abstract, but the accessible `n=5` derivation itself explicitly concludes only
   `K(5) >= (4+sqrt(142))/9`.
   The preceding R13 run independently certified that lower obstruction and did not inherit the paper's unsupported global divergence conclusion.

A bounded exact-value search did not locate a later rigorous arbitrary-row proof of `K_5^*=(4+sqrt(142))/9`. Novelty of the reduction below is therefore **UNVERIFIED**; a negative search is not a novelty certificate.

## 2. Starting point: the exact projective row-cover formulation

Retain the preceding exact reformulation. Let

`S_5 = {s in {-1,+1}^5 : s_1=1}`,

the 16 antipodal Boolean signing classes. A level-one row cover is a finite family `r_alpha in R^5` such that for every `s in S_5` some row satisfies

`|r_alpha . s| >= 1`.

For such a cover write its coordinate energies

`E_j = sum_alpha r_{alpha,j}^2`

and let

`c_5 = inf max_j E_j`

over all level-one covers. The preceding report proved

`K_5^* = 1/sqrt(c_5)`.

The explicit Belhaouari--AlQudah obstruction gives

`c_5 <= c0`,

where

`c0 = 1 / ((4+sqrt(142))/9)^2
    = 79/98 - 2 sqrt(142)/49
    = 0.3197397841708985...`.

Therefore proving the claimed exact value is equivalent to proving `c_5 >= c0`.

## 3. Method #25 — count the same cover twice

The main idea is to count how many projective sign classes a single row can cover and charge that count against its Euclidean energy.

For `1 <= k <= 16`, define the purely finite cube quantity

`M_k = max ||t_1+...+t_k||_2^2`,

where the maximum ranges over `k` distinct antipodal classes of the five-cube and over one orientation `t_i in {s_i,-s_i}` for each chosen class.

The exact values are

`M_1,...,M_16 =
  5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256`.

Now let one row `r` cover exactly `k` projective classes at level one. Orient each covered class so that `r.t_i >= 1`. Then

`k <= r . (t_1+...+t_k)
   <= ||r||_2 ||t_1+...+t_k||_2`,

so

`||r||_2^2 >= q_k := k^2/M_k`.

Thus the exact lower-charge table is

`q_1,...,q_16 =
  1/5, 1/4, 9/29, 1/3, 25/61, 9/20, 49/101, 1/2,
  81/133, 25/36, 121/157, 9/11, 169/189, 49/52, 225/229, 1`.

This estimate is deliberately weaker than solving each row QP exactly; its strength is that it composes without knowing the row geometry.

Suppose a pruned cover uses `m` nonzero rows and row `i` covers `k_i` projective classes. Since their union covers all 16 classes,

`sum_i k_i >= 16`.

Therefore

`sum_i ||r_i||_2^2 >= sum_i q_{k_i}`.

The exact finite minimization over positive integers `1<=k_i<=16` with total at least 16 gives

`m=1: 1`,
`m=2: 1`,
`m=3: 7/6`,
`m=4: 4/3`,
`m=5: 89/60`,
`m=6: 49/30`,

and every `m=7,...,16` is still larger. For six rows the minimizing coverage-count profile is

`(1,1,1,1,4,8)`,

with exact lower energy `49/30`.

But any putative cover with `max_j E_j < c0` would have total row energy

`sum_i ||r_i||_2^2
 = sum_j E_j
 < 5 c0`.

The comparison is strict:

`49/30 - 5 c0
 = 2(-881+75 sqrt(142))/735 > 0`,

because

`75^2 * 142 - 881^2 = 22589 > 0`.

Hence such a cover cannot have six or more rows.

### R13-C33 — five-row reduction at the candidate exact threshold

**Theorem.** If `c_5 < c0`, then a level-one projective cover witnessing some value `<c0` exists using at most five nonzero rows. Equivalently, to prove

`K_5^* <= (4+sqrt(142))/9`

for arbitrary row dimension, it is enough to prove it for matrices with at most five rows; padding by zero rows reduces this to the square `5 x 5` case.

**Proof.** If `c_5<c0`, choose a cover with `max_j E_j<c0`. For each of the 16 projective classes choose one witness row and discard every row not selected; this leaves at most 16 nonzero rows and only decreases every column energy. If `m>=6`, the preceding count-energy inequality and exact finite minimization force total row energy at least `49/30`, while the column-energy cap forces it below `5c0<49/30`, contradiction. Therefore `m<=5`. QED.

This is the main progress of the run. It does **not** prove the old `K(5)` equality, but it removes arbitrary ambient row dimension from the remaining exact five-column problem. The explicit lower obstruction itself already lives in five rows.

## 4. Method #19 — make the count into an exact algorithm

The finite core above is certified by a short exact dynamic program rather than by heuristic enumeration.

For each of the 16 projective representatives the DP has exactly three choices:

- skip the class;
- select the representative with `+` orientation;
- select it with `-` orientation.

For each cardinality `k` it stores the set of attainable integer coordinate sums in `Z^5`. Taking the largest squared norm gives `M_k` exactly. A second rational DP minimizes

`sum_i k_i^2/M_{k_i}`

for every possible nonempty row count `m<=16` subject to total covered-class count at least 16.

The checker uses only integer and rational arithmetic for these finite steps; the one quadratic-irrational comparison is reduced to the positive integer square gap `22589`. It ends

`R13_C33_EXACT_PASS`.

Checker:

`artifacts/R13/20260917T1438Z_k5-five-row-reduction-6c2a_checker.py`

creation/readback commit:

`5f3dbe54fdd90d0b5d3daf157c2a1b6a549306b2`.

Archived executed output:

`artifacts/R13/20260917T1438Z_k5-five-row-reduction-6c2a_output.txt`

creation/readback commit:

`53977cc74876c0c8a249ce8bda7d805e7300777c`.

This is a **self-check**, not an independent audit.

## 5. Method #14 — find the group acting

The five-row theorem makes a full finite attack much more realistic, but the remaining difficulty is still the continuous geometry of how five rows orient and cover the 16 projective sign classes.

There is a classical symmetry reduction that was not used in the preceding R13 route.

Write a projective sign as

`s=(1,x_1,x_2,x_3,x_4)`, `x in {-1,+1}^4`.

For a row `r=(r_0,r_1,...,r_4)`, its sign pattern away from zero is

`sign(r_0 + r_1 x_1 + ... + r_4 x_4)`.

Thus every row orientation pattern is an affine linear threshold function on four Boolean variables. Covered classes have margin at least one, so zero-valued classes are irrelevant to their required orientation; a sufficiently small generic perturbation preserves every covered label.

Classical threshold-logic enumeration gives:

- exactly **1882** four-variable threshold functions (including functions depending on fewer variables);
- exactly **15 NPN-equivalence classes** under input negations, input permutations, and output negation.

These are classical counts (Muroga/Knuth; OEIS A000609 and A001529), not new R13 claims. Their relevance here is structural: input negation/permutation corresponds to signed permutation of the four tail coordinates, while output negation is row sign. These operations preserve the row-cover energy problem.

Therefore the orientation component of the remaining five-row search can be organized around at most **15 classical NPN types**, rather than arbitrary labelings of the 16 projective vertices. Full signed permutations of all five original coordinates can only reduce this further.

This does not by itself prove the square case because, inside one orientation type, one must still choose which positive-margin vertices are actually covered and solve the coupled five-row energy allocation. But it gives a much smaller exact branch structure for the next attack.

## 6. Why the previous local dual does not automatically globalize

I also tested the most tempting way to turn the preceding fixed-partition KKT certificate into a global proof and found a concrete obstruction, so the next run should not spend its effort on that same shortcut.

The preceding local certificate used

`Lambda = diag(x,y,y,y,y)`

with

`x=-1/7+16 sqrt(142)/497`,
`y= 2/7- 4 sqrt(142)/497`

and positive class multipliers `alpha0` or `C` on ten projective classes. A partition-independent rowwise dual would require every admissible row to pay at least the total multiplier weight of the supported classes it covers.

The cap-admissible row

`r=(0,0,-1/2,1/2,0)`

already defeats that pointwise inequality. Its coordinate squares are at most `1/4<c0`; its `Lambda`-energy is `y/2`, while it covers six of the `C`-weighted supported classes, whose multiplier total is `6C`. Exactly,

`6C - y/2
 = 20/49 - 349 sqrt(142)/13916
 > 0`.

So the old fixed-cell multipliers cannot simply be reused as a universal rowwise dual. The five-row reduction and NPN classification are not cosmetic: a successful proof has to retain interactions among multiple rows/coverage cells.

## 7. What the three new routes delivered

**#25 COUNT THE SAME THING TWICE — success.** Counting covered projective classes and total squared row energy yields the sharp-for-this-compiler six-row barrier `49/30`, which is strictly above `5c0`. This reduces any candidate counterexample below `c0` to at most five rows.

**#19 MAKE IT AN ALGORITHM — success.** The entire finite part is an exact three-choice DP on the 16 projective classes followed by an exact rational coverage-profile DP. The checker was executed and archived only because the new reduction was worth certifying.

**#14 FIND THE GROUP ACTING — structural success, not closure.** The surviving five-row problem lives inside the classical four-variable affine-threshold-function arrangement: 1882 sign patterns but only 15 NPN classes. This is the correct next finite search space. It has not yet been exhausted, so no five-column equality is claimed.

## 8. Remaining obligation and next route

The exact remaining statement is now narrower:

> Every five-row level-one cover of the 16 projective five-cube classes has
> `max_j sum_i r_{ij}^2 >= c0`.

Equivalently, every real `5 x 5` matrix with column Euclidean norms at most one has a Boolean signing of infinity norm at most

`K0=(4+sqrt(142))/9`.

The next useful attack is an exact branch-and-bound over the **15 NPN row-orientation types**, retaining column-energy vectors rather than collapsing them to total energy. Each branch is a convex quadratic program once the oriented covered subsets are fixed. The fixed-partition C32 KKT method can serve as a branch certificate, but the dual weights must be allowed to change with the branch. A successful exhaustive certificate would prove the old finite equality; a branch with energy `<c0` would refute it and produce a stronger lower obstruction.

Because the fixed `B_R13(n)` metric has now been unchanged for two consecutive runs, another unchanged run triggers the owner's full section-I stuck protocol. Accordingly the next run must either move the upper envelope / exact `n=5` status, or be the required thinking-only stuck report rather than another auxiliary lemma.

## 9. Status and audit discipline

Status: **PARTIAL / NO UPPER-METRIC MOVEMENT / EXACT FIVE-ROW REDUCTION SELF-CHECK PASS / OUTSIDE FINITE-`n` AUDITS PENDING**.

The distinct R12 and P26 PASS audits in the repository concern the Guo--Fang--Lu universal theorem, not R13-C33, the five-column lower obstruction, or the later finite-dimensional upper refinements. No finite `n=5` equality is called proved or closed.

No email, Drive, public posting, workflow, permission, scheduler, shared-root, or peer-track change was made.

## 10. Runtime/model-control status

The exposed scheduler/task interface still provides prompt/title/schedule/enabled/timing controls but no native model-family or reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text rather than authenticated runtime configuration; this run is honestly labeled GPT-5.6 Sol / UNVERIFIED.

The repository records that the earlier `You cannot modify this task` behavior is context/ownership dependent: P26 was later modifiable from an authorized P/C context, while R-series edits were denied in another context. The legitimate fix is to operate from the authorized task/workspace-owner context or for the platform to expose native model/reasoning controls. Duplicating a denied task or bypassing permissions is not an acceptable workaround. No scheduler modification was attempted here, consistent with the current owner instruction.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189; Belhaouari-AlQudah 2019/2024 finite-n source"
  target: "complete real Boolean unit-column discrepancy upper envelope B_R13(n)"
  metric_before: "B_R13 upper envelope from 20260917T1335Z_k5-priorart-obstruction-4e2b"
  metric_after: "UNCHANGED"
  movement: "no upper-envelope movement"
  auxiliary_movement: "candidate exact n=5 problem reduced from arbitrary row dimension to at most five rows below c0"
  candidate_K5_lower: "(4+sqrt(142))/9"
  candidate_cover_energy: "c0=79/98-2sqrt(142)/49"
  new_exact_claim: "R13-C33: any level-one cover with max column energy < c0 has <=5 nonzero witness rows"
  six_row_energy_lower: "49/30"
  exact_comparison: "49/30 - 5c0 = 2(-881+75sqrt(142))/735 > 0"
  checker_status: "R13_C33_EXACT_PASS; self-check only"
  symmetry_reduction: "four-variable affine threshold patterns: 1882 total, 15 NPN classes (classical literature)"
  status: "PARTIAL"
  stagnation_before: 1
  stagnation_after: 2
  methods: [25, 14, 19]
  next_obligation: "prove or refute the square 5x5 bound at K0 using branch-specific convex/KKT certificates over NPN row types; next unchanged run triggers stuck protocol"
```
