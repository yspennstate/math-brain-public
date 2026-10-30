# BT4 fleet01/B05 — residual degree staircase and saturated-triangle support orbit

Run: `20260922T012616Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: `BT4`  
Candidate: `BT4-LPR-STAIRCASE-SATSWITCH-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

No full proof of the k=4 Bermond–Thomassen conjecture is claimed. The target remains open in this report. The new contribution is (i) a stronger pair-deletion certificate obtained by applying the complete 2023 outdegree-sequence theorem for two disjoint directed cycles, and (ii) a genuine equal-size three-packing exchange in the saturated total-coalescence triangle branch which exposes every formerly cycle-supported five-witness as a legitimate remainder sink, one at a time.

## 1. Exact team state consumed

The controlling BT4 normal form is the campaign-lead fleet02/B04 run `20260922T001806Z-b04-bt4-a1ceeb3c`, report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72` and correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`. I use only the corrected statements: an exact-seven oriented counterexample, a globally minimum-total three-cycle packing `(C1,C2,C3)`, acyclic remainder `R`, arc domination, 3-vertex-strongness, the valid remainder path-fan exchange, and the correct distinction between remainder-supported and third-cycle-supported pair witnesses.

The named OTHER-account result applied directly is fleet02/B06 run `b06-20260922T005655Z-24f482784ae2`, report blob `749c5848dc20e2023bcb8312e8b90d8f8746742f`. Its exact adversary refutes automatic separation of the three unique R-exit heads of cycle-supported five-witnesses and isolates the first hard branch: three five-witnesses on a complementary directed triangle `C3=(z0,z1,z2)` may all send their unique R-exit to one common head `h`; in the locally sharp saturated case there is a sink `x` with paths `zi->h->x` and arcs `x->zi` for all `i`. It also proves that in total coalescence the common head must have at least three R-outneighbors unless it is already an R-supported pair witness.

I also use fleet03/B04 `BT4-MENGER-COLLAR-v1`, shared commit `ceed1a3f204c7127bfedb51b872681224403fd0d`, only as a compatibility check: the new argument below does not assume a prescribed path belongs to a Menger family and does not extend nonsaturated port uniqueness to the saturated case.

## 2. New published input: the complete k=2 outdegree-sequence theorem

The team had so far used the 2009 Lichiardopol–Pór–Sereni consequence saying that a digraph with no two vertex-disjoint directed cycles must either have a vertex of outdegree at most one or at least three vertices of outdegree exactly two.

A strictly stronger published theorem is available:

M. Lewandowski, J. Polcyn, C. Reiher, *Two disjoint cycles in digraphs*, J. Graph Theory 104 (2023), 461–469, arXiv:2205.10826v2, Theorem 1.4.

It characterizes exactly which nondecreasing outdegree sequences force two vertex-disjoint directed cycles. I only need the following immediate specialization of their theorem, and include the derivation so no black-box strengthening is hidden.

### Lemma 2.1 — residual staircase

Let `H` be a finite digraph with no two vertex-disjoint directed cycles and minimum outdegree at least two. Write its nondecreasing outdegree sequence as

`d1 <= d2 <= ... <= dn`.

Then

1. `d1=d2=d3=2`, and
2. for every `j>=4`, `dj <= j-1`.

#### Proof

In the terminology of Lewandowski–Polcyn–Reiher, a sequence is `(r,s)`-large when two explicit inequalities hold, and Theorem 1.4 says that a sequence forces two disjoint cycles iff it is large for some `(r,s)`.

Because `d1>=2`, the first condition for `(r,s)=(1,1)` is automatic: `d1>=1` and `d1>=2`. If `d3>=3`, the exceptional antecedent in their second condition (`d3=2`) is false, so the sequence is `(1,1)`-large. That would force two disjoint cycles in every digraph with this sequence, contradicting the existence of `H`. Hence `d3=2`; together with minimum outdegree two this gives `d1=d2=d3=2`.

Now the exceptional antecedent for `(1,1)` is true. To keep the sequence nonlarge, there can be no index `j>=4` with `dj>=j`. Thus `dj<=j-1` for every `j>=4`. QED.

This is exactly stronger than the three-degree-two dichotomy: after the three degree-two vertices it forces a complete low-degree staircase.

## 3. Pair deletion: five-fan witnesses extend to a 5/4/3/2/1 fan staircase

Work in the lead's exact-seven normal form. Delete two packed cycles `Ci,Cj` and let

`H_k = D - (V(Ci) union V(Cj)) = D[V(Ck) union R]`.

`H_k` cannot contain two disjoint directed cycles, or together with `Ci,Cj` they would give four cycles in `D`.

For `v in H_k` write

`f_ij(v)=|N+(v) intersect (V(Ci) union V(Cj))|`.

Because `D` is exactly seven-outregular,

`d^+_{H_k}(v) = 7 - f_ij(v)`.

In the pairwise NO-SIX branch, `f_ij(v)<=5` for every `v`, hence `delta^+(H_k)>=2`. Apply Lemma 2.1. If the residual degrees are sorted increasingly, the pair-fans are sorted decreasingly, and we obtain:

- at least three vertices have pair fan exactly `5`;
- at least four vertices have pair fan at least `4`;
- at least five vertices have pair fan at least `3`;
- at least six vertices have pair fan at least `2`;
- if `|H_k|>=7`, at least seven vertices have pair fan at least `1`.

The first line is the old Lichiardopol–Pór–Sereni consequence. The next four lines are new information for the BT4 candidate.

I will call this the **pair-deletion fan staircase**.

The derivation is source-valid even when the five-fan vertices lie on `Ck`: it is a statement about the actual residual degree sequence and makes no illegal one-vertex exchange at a cycle-supported witness.

## 4. Forward-cone staircase in the hard total-coalescence triangle

Now take the exact hard branch isolated by fleet02/B06. Write the complementary support cycle as the directed triangle

`C=(z0,z1,z2)`, with arcs `z0->z1->z2->z0`.

Assume all three `zi` are exact five-fan witnesses for the pair `(A,B)=(C1,C2)` and have the same unique R-exit

`zi -> h`  for `i=0,1,2`.

Thus in the residual graph `H=D[V(C) union R]` each `zi` has exactly the two residual outarcs

`zi -> zi+` and `zi -> h`.

Assume the NO-SIX branch for this pair, so every vertex of `H` has residual outdegree at least two. The common-head obstruction is only hard when `q(h)=d_R^+(h)>=3`; if `q(h)<=2`, fleet02/B06 already makes `h` an R-supported pair witness.

Let `U` be `h` together with every R-vertex reachable from `h` by an R-internal directed path, and put

`G = D[V(C) union U]`.

### Lemma 4.1 — forward-cone fan staircase

`G` has no two disjoint directed cycles and minimum outdegree at least two. Consequently, among vertices of `U` there are distinct vertices satisfying the nested thresholds

- one vertex with `f_AB >= 4`;
- two vertices with `f_AB >= 3`;
- three vertices with `f_AB >= 2`;
- four vertices with `f_AB >= 1`.

#### Proof

`G` is an induced subdigraph of `H`, so two disjoint cycles in `G` would already contradict the BT4 counterexample by adjoining `A` and `B`.

Each `zi` has degree exactly two in `G`, because its residual outarcs are its cycle successor and `h`, both retained.

For `u in U`, every R-outneighbor of `u` is again reachable from `h`, hence belongs to `U`. All C-outneighbors are also retained. Therefore

`d_G^+(u)=d_H^+(u)=7-f_AB(u)>=2`.

So `delta^+(G)>=2`. Since `q(h)>=3`, the set `U` contains `h` and at least three distinct R-outneighbors of `h`; hence `|G|>=7`.

Apply Lemma 2.1 to `G`. Besides the three triangle vertices of degree two, the inequalities `d4<=3`, `d5<=4`, `d6<=5`, `d7<=6` force respectively at least one, two, three, and four vertices of `U` with residual degree at most `3,4,5,6`. Translating by `f_AB=7-d_G^+` gives the four stated thresholds. QED.

This localizes the extra fan mass to the **forward cone of the common head**, not merely somewhere in the pair-deletion residual graph.

### Corollary 4.2 — the first exchange-ready gate

There is a vertex `u in U` with at least four outneighbors in `A union B`.

- If `f_AB(u)=5`, then `u` is an R-supported five-witness and the support-location obstruction has disappeared.
- If `f_AB(u)=4` and one of `A,B` receives at least three of these arcs, then `u` is a legal heavy **remainder** target for the corrected one-vertex/path-fan machinery.
- The only branch not immediately handed to those existing mechanisms is the balanced type

`(a_A(u),a_B(u))=(2,2)` and `a_C(u)+q(u)=3`.

Thus the total-coalescence triangle cannot consist only of the three cycle-supported five-witnesses and a high-R-degree common head. It necessarily carries a reachable R-supported four-fan gate; if all stronger remainder exits are excluded, that gate has the exact finite family

`(a_A,a_B,a_C,q)=(2,2,t,3-t)`, `t=0,1,2,3`.

There is also a useful location refinement. The arcs `zi->h` for all three triangle vertices and orientation imply `a_C(h)=0`. Hence `d_G(h)=q(h)`. If `q(h)=3`, then `h` itself has pair fan four; in the stubborn balanced branch it has exact type `(2,2,0,3)`. If `q(h)>=4`, the vertex furnished by `d4<=3` is a **strict descendant** of `h` in the R-DAG.

## 5. Punctured staircase: deleting any non-head remainder vertex

The full degree-sequence theorem gives a further robustness statement which the old three-witness theorem cannot see.

Stay in the total-coalescence triangle and assume, for this pair `(A,B)`, that there is **no R-supported five-witness**. Equivalently every vertex of `R` has residual degree at least three in `H`.

Let `r` be any remainder vertex distinct from `h`. Consider `H-r`. The three `zi` still have degree two because their only R-outneighbor is `h`, not `r`. Every R-vertex had degree at least three in `H` and loses at most the single outneighbor `r`, so every remaining R-vertex has degree at least two in `H-r`. Therefore `delta^+(H-r)>=2`, and `H-r` still has no two disjoint cycles.

Applying Lemma 2.1 again gives a remainder vertex `u_r != r` with

`d^+_{H-r}(u_r)<=3`.

In the original `H` this says

- either `u_r` does not point to `r` and `f_AB(u_r)>=4`, or
- `u_r->r` and `f_AB(u_r)>=3`.

So every puncture of the R-DAG away from the common head leaves an exchange-ready three/four-fan certificate. This is a useful robustness interface for future linkage arguments: the common-head obstruction cannot be protected by a single downstream vertex unless another R-vertex spends at least three cross-arcs into `A union B`.

A particularly rigid subcase follows. If the hard branch also excludes every R-vertex of pair fan at least four, then all such `u_r` must have residual degree exactly four and must point to the deleted `r`. Hence every `r != h` is dominated (inside the residual graph) by some R-vertex with pair fan exactly three. For `r` ranging over the at least three R-outneighbors of `h`, this gives a concrete incidence cover that a final splice argument can attack.

## 6. A genuine equal-size exchange in the direct saturated-collar branch

The preceding staircase does not by itself eliminate the exact local adversary from fleet02/B06. Its hardest geometry has one more feature:

there is `x in R` such that

`h -> x` and `x -> zi` for all `i=0,1,2`.

Equivalently each common-head collar

`zi -> h -> x`

has length two and the terminal vertex is saturated on the support triangle.

This branch admits a concrete packing exchange that was not available before respecting support location.

### Lemma 6.1 — saturated triangle support switch

For each `i in {0,1,2}`, define

`K_i = zi -> h -> x -> zi`.

Then `K_i` is a directed triangle, disjoint from `A` and `B`. Replacing `C` by `K_i` gives another three-cycle packing

`P_i=(A,B,K_i)`

with exactly the same total number of covered vertices as the original packing `(A,B,C)`.

Its remainder is exactly

`R_i = (R \ {h,x}) union (V(C) \ {zi})`.

Because the ambient digraph is assumed to have no four disjoint cycles, `D[R_i]` is acyclic. Thus `P_i` is another globally minimum-total packing to which every **remainder-supported** exchange lemma may legally be applied.

All affected vertices are explicit: `h,x` move from `R` onto the packed triangle; `zi` stays packed; the other two vertices of the old support triangle move into the remainder; `A` and `B` are untouched.

#### Proof

All three arcs defining `K_i` are assumptions of the saturated collar. The vertex sets are disjoint by the original packing/remainder partition. Since both `C` and `K_i` are triangles, total packing size is unchanged. A directed cycle in `R_i` would be disjoint from `A,B,K_i`, yielding four disjoint directed cycles, impossible. QED.

### Corollary 6.2 — every old cycle-supported five-witness is legally exposable as a remainder sink

Fix `j`. Choose `i=j+1` modulo three, i.e. pack the successor of `zj` in `K_i`. Then `zj` lies in the new remainder `R_i`, and both of its old residual outarcs now point into the new packed triangle:

- `zj -> zj+ = zi`,
- `zj -> h`.

Therefore `zj` is a **sink of the new remainder**. Its five cross-arcs into `A union B` are unchanged.

So, one at a time, all three formerly cycle-supported five-witnesses can be moved into a setting where the lead's sink lemmas and the ordinary remainder-supported path-fan machinery are fully legal. This removes the support-location objection in this saturated direct-collar subcase.

If the exchanged packing remains in a global NO-SIX branch, the five cross-arcs of this sink must split `3+2` between `A` and `B`: a `4+1` or `5+0` split, together with its two arcs into `K_i`, would itself create a six-fan for a pair of packed cycles. Hence in the persistent NO-SIX branch the exposed sink has fan vector exactly `(3,2,2)`.

Its two-fan into `K_i` is also exact. Writing `K_i` cyclically as

`x -> zi -> h -> x`,

we have the direct return `x->zj` and

`N+(zj) intersect K_i = {zi,h} = {x+,x++}`.

Thus the valid neutral light-pivot exchange rotates `K_i` to the triangle `K_j`. The three states `K_0,K_1,K_2` form a genuine neutral orbit. Any secondary potential depending only on the three cycle lengths, including `sum |C_l|^2`, is constant on this orbit. Therefore the saturated branch cannot be closed merely by arguing that equal-size exchanges monotonically balance cycle lengths; a final proof must use the A/B fan/linkage information exposed by the orbit.

The important positive consequence is that for each `zj`, in a legitimate globally minimum packing where `zj` is a remainder sink, its unique heavy member among `A,B` (in the persistent NO-SIX `3+2` split) cannot send an arc directly into `zj`: the one-vertex exchange lemma would otherwise bound that fan by two. This heavy-target avoidance is now source-valid for all three witnesses, despite their being cycle-supported in the original packing.

## 7. Compact conditional end-to-end route after this run

The live proof skeleton can now be stated more sharply.

1. Reduce to the lead's exact-seven, oriented, arc-dominated, 3-vertex-strong minimum counterexample with globally minimum three-packing and DAG remainder.
2. For every pair deletion, split SIX versus NO-SIX.
3. In NO-SIX, replace the old bare “three five-witnesses” certificate by the full pair-deletion fan staircase `5,5,5,>=4,>=3,>=2,(>=1)`.
4. R-supported witnesses feed the already valid remainder exchange/path-fan machinery. Cycle-supported witnesses feed the support-switch/collar machinery.
5. If three cycle-supported five-witness exits have at least two heads, use the existing collar-or-bottleneck branch.
6. If all three exits coalesce on one head and the complementary support is a triangle, use the forward-cone staircase. This forces a reachable R four-fan gate, unless an even stronger R-supported witness/heavy target has already appeared.
7. In the direct saturated collar `zi->h->x`, `x->zi`, use Lemma 6.1. The three equal-size packings expose each old five-witness as a genuine remainder sink and make heavy-target avoidance legal for all three. If a six-fan appears under a switched packing, hand off to SIX; otherwise all three exposed sinks have exact `(3,2,2)` fan type.
8. The first still-unpaid implication is then genuinely narrower: combine the forward-cone three/four-fan gate and the three exposed heavy-target-avoidance constraints to obtain two compatible cross-cycle linkages, or else show that the punctured-staircase incidence cover forces such a linkage. In the direct saturated orbit a cycle-length-only potential cannot solve this; the next invariant must record which of `A,B` is the heavy label and how the R three/four-fan gates link to those labels.

This is an end-to-end conditional argument: closing the final linkage implication in item 8 closes the total-coalescence NO-SIX triangle branch; the independently preserved SIX branch and nontriangle/collar branches remain the other campaign obligations.

## 8. Negative control against overclaiming

The fleet02/B06 16-vertex adversary is compatible with the new residual staircase. For its pair `(C1,C2)` the residual degrees on `C3 union R` are

`(2,2,2,3,3,4,5,5,6,6)`.

This is nonlarge under the Lewandowski–Polcyn–Reiher criterion and satisfies all staircase inequalities. Thus the staircase is a valid strengthening but is not, by itself, a proof of BT4.

The same adversary realizes the saturated switch with `h=R0` and `x=R6`, so the neutral orbit also exists there. This is a useful negative control: none of Lemmas 2.1, 4.1, or 6.1 secretly assumes the global target conclusion. The adversary has an explicit four-pack for other reasons, and a genuine BT4 proof still has to use the no-four-pack condition together with the newly exposed A/B linkage structure.

A deterministic sanity check of the sequence criterion gives:

- `(2,2,2,3,3,4,5,5,6,6)` is nonlarge;
- increasing the fourth residual degree to four makes `(1,1)` large and therefore forces two disjoint cycles by Theorem 1.4.

No finite computation is promoted to target-level evidence.

## 9. Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The full BT4 conjecture is **not proved**. The run does, however, replace the team's pair-deletion degree input by a strictly stronger complete-sequence consequence, localize the new fan staircase to the forward cone of the common head in the hard triangle branch, and supply a genuine equal-size support exchange that legally converts each saturated cycle-supported five-witness into a remainder sink. The first remaining mathematical arrow is now a cross-cycle linkage problem with explicit three/four-fan gates and heavy-label constraints, rather than the earlier unsupported request to separate exit heads or to apply a remainder lemma directly to a cycle-supported witness.
