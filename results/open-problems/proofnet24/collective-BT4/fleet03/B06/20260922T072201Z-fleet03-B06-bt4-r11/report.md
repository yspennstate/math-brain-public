# BT4 fleet03/B06 — packed F3 apex is confined to a two-vertex support collar

Run: `20260922T072201Z-fleet03-B06-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-APEX-COLLAR-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with a stronger shortcut `CANDIDATE_REFUTED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and assignment

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement, hence directed digons count before the inherited minimal-counterexample reduction.

The exact fleet03/B06 assignment is constrained search and symbolic-family testing of the decisive BT4 lemma while retaining the whole original directed graph and a complete cycle-packing certificate. The named OTHER-account partner is `fleet04/B04`.

No authenticated mathematical-brain retrieval was used. This run is source-bound repository research and remains `WITHOUT_VERIFIED_BRAIN`.

## 2. Exact inherited state consumed

### Named assigned partner: fleet04/B04

I consumed the complete partner run

`proofnet24/collective-BT4/fleet04/B04/20260922T060947Z-fleet04-B04-BT4-r15/report.md`,

candidate `BT4-R4-F3-RETURN-CUT-v1`, report Git blob `425b7f0491ef4caf794ce862783c811edd26b110`.

In the canonical four-remainder F3 state, write

`S* = p -> x -> s -> p`,

let `U` be the other light packed cycle, let `K={r1,r2,r3}`, and let `q` be the freed source vertex. The inherited exact relations include `q->K`, `K->x`, `x->q`, and saturation triangles `T_r=q->r->x->q`. The two possible external witnesses `p,u` define cover sets `A,B`, and in the both-repeat branch `|A|,|B|>=2` there are internally disjoint opposite short paths between `u in U` and `p in S*`.

The partner proves that their union is a genuine directed cycle `W` of order three or four. In the two-indirect case one may label

`W = u -> a -> p -> b -> u`,

with `a in B\A`, `b in A\B`, and the third vertex `c in K\{a,b}` lying in `A intersect B`. It also proves that after deleting `H`, `W`, and `T_c`, the residual `(U-{u}) union {s}` is acyclic; equivalently all `U->s` and `s->U` contacts obey the one-cut order on the broken support path `U-u`.

This partner result is used below as an actual structural hypothesis, not by importing its outcome label.

### Immediate fleet03/B06 predecessor

The preceding theorem

`BT4-R4-F3-SHORT-RETURN-APEX-v1`,

at `proofnet24/collective-BT4/fleet03/B06/20260922T062238Z-fleet03-B06-r11/report.md`, report Git blob `c6cb92e588542b144935facb8c948ab78b20d85c`, proves that every both-repeat F3 state has:

1. a genuine short return cycle `W` of order three or four meeting the current packing exactly in the two light ports `{p,u}`;
2. every current-remainder vertex outside `W` hitting `W` at most twice, while `x` hits it zero times;
3. therefore, by the genuine `k=3` deletion theorem, a **packed** vertex `z` outside `W` with at least three outneighbors on `W`;
4. `z` lies in `H union {s} union (U-{u})`.

The previous first unpaid implication was to use the location of this packed three-hit apex to force a splice. This run attacks the `z in U-{u}` location exactly.

## 3. Compact conditional route

Assume BT4 false and enter the inherited oriented, exact-outdegree-seven, arc-dominated, 3-vertex-strong normal form. Choose three disjoint directed cycles lexicographically: first minimum total packed order, then maximum number of arcs induced by their acyclic remainder. Enter the canonical four-remainder F3 both-repeat branch and form the short return cycle `W` and packed three-hit apex `z` above.

If `z` lies on the same packed support `U` as the port `u`, chordlessness plus global minimum packing force `z` into the final two predecessor positions of `u`. The second-predecessor alternative is not merely a location label: it produces a **size-neutral replacement cycle for the whole support `U`**. Therefore a genuine BT4 counterexample must make the complement of that neutral exchange acyclic, and the secondary arc-maximal choice applies to it.

This converts an arbitrary `U`-support apex location into a two-point collar plus an exact exchanged-remainder constraint.

## 4. Theorem — `BT4-R4-F3-APEX-COLLAR-v1`

Work in the canonical F3 both-repeat state above. Let `W` be its short return cycle and let `z in U-{u}` be a packed vertex with at least three outneighbors on `W`. Let `n=|U|`. Write `u^-` and `u^{--}` for the immediate and second predecessors of `u` on the directed cycle `U`.

Then:

1. If `|W|=3`, necessarily `z=u^-`.
2. If `|W|=4`, necessarily

   `z in {u^-,u^{--}}`.

3. In the second-predecessor case `z=u^{--}`, the cycle is necessarily the two-indirect return

   `W = u -> a -> p -> b -> u`,

   `z` misses `u` and hits all three other vertices `{a,p,b}`, and

   `C_z = z -> b -> u -> U[u,z] -> z`                         (1)

   is a genuine directed cycle with exactly `n` vertices. Thus replacing `U` by `C_z` is a size-neutral three-packing exchange.
4. In a genuine BT4 counterexample the complement of the exchanged packing `(H,S*,C_z)` must be acyclic. In the exact four-remainder decomposition its vertex set is

   `{q,a,c,u^-}`,                                               (2)

   where `c=K\{a,b}`. Because the starting packing was also chosen secondarily to maximize remainder arcs, the induced arc count on (2) cannot exceed that of the old current remainder `R*={q,a,b,c}`.

### Proof

Packed cycles are chordless in the inherited globally minimum packing. Hence for two distinct vertices of `U`, the only arc internal to `U` is a support edge. In particular,

`z->u` implies `z=u^-`.                                        (3)

If `|W|=3`, a vertex with at least three outneighbors on `W` hits all three vertices, including `u`. Equation (3) gives `z=u^-`. This proves part 1.

Now let `|W|=4`. If `z->u`, again (3) gives `z=u^-`. Suppose instead `z!=u^-`. Then chordlessness gives `z not->u`. Since `z` has at least three distinct outneighbors on a four-cycle, it must hit every other vertex of `W`. A four-vertex both-repeat return has both short paths indirect, so label it

`W = u -> a -> p -> b -> u`.

Therefore

`z->a,p,b`.                                                     (4)

Let

`d = dist_U(u,z)`

be the forward edge distance from `u` to `z` along `U`. The arcs `z->b` and `b->u`, together with the forward support path from `u` to `z`, form the genuine directed cycle (1). Its interior outside `U` is only the old remainder vertex `b`, so it is disjoint from `H` and `S*`.

The cycle (1) has `d+2` vertices: the forward `u`-to-`z` support path contributes `d+1` vertices and `b` contributes one more. Thus `(H,S*,C_z)` is a legal three-cycle packing. Global minimum of `(H,S*,U)` gives

`d+2 >= n`.                                                     (5)

Under the current assumption `z!=u^-`, one also has `d<=n-2`. Combining with (5) yields

`d=n-2`,

so `z=u^{--}` and `|C_z|=n`. This proves parts 2 and 3.

For part 4, `(H,S*,C_z)` has exactly the same total packed order as `(H,S*,U)`. If its complement contained a directed cycle, that cycle together with `H,S*,C_z` would be four pairwise vertex-disjoint directed cycles, contradicting the counterexample assumption. Hence the complement is acyclic.

In the two-indirect F3 state the current remainder is

`R*={q,a,b,c}`.

The neutral cycle `C_z` consumes `b` and every vertex of `U` except `u^-`: because `z=u^{--}`, the forward support path `U[u,z]` contains all of `U` other than `u^-`. Therefore the new remainder is exactly (2).

Finally the new packing has the same minimum total order and an acyclic remainder, so it is eligible for the secondary extremal comparison. The chosen starting packing maximizes induced-remainder arcs among all minimum-total packings, whence

`|A(D[{q,a,c,u^-}])| <= |A(D[{q,a,b,c}])|`.                   (6)

QED.

## 5. Exact failure of the stronger shortcut

The tempting stronger claim

> every `U`-support three-hit apex must be the immediate predecessor `u^-`

is false under the inherited local normal-form hypotheses.

The complete 18-vertex certificate inherited from the preceding B06 checker is revalidated in the checker for this run. It is oriented, every outdegree is exactly seven, every arc has a common predecessor, deletion of any zero, one, or two vertices leaves a strongly connected digraph, and the three packed cycles are chordless.

For its quadrilateral return,

`U=(6,7,8,9,10)`,
`u=6`,
`W=(6,17,11,16)`.

The packed apex is

`z=9=u^{--}`,

and it hits exactly `{17,11,16}`, i.e. all three non-`u` vertices of `W`, while missing `u`. Thus the immediate-predecessor-only shortcut is genuinely false.

The theorem predicts the neutral exchange

`C_z=(9,16,6,7,8)`,

which indeed has order five, exactly `|U|`. Its exchanged remainder is

`{10,14,15,17}`,

and is **cyclic**: it contains

`10 -> 14 -> 15 -> 10`.                                        (7)

This is precisely why the certificate is not a BT4 counterexample once the neutral collar exchange is examined. Independently, the whole graph already contains the explicit four-pack

`(0,1,10)`, `(2,3,8)`, `(4,5,7)`, `(6,14,16)`.

So the failure does not refute BT4. It repairs the universal lemma to the exact two-vertex collar and demonstrates that the exchanged-remainder acyclicity in part 4 is the correct next global filter.

## 6. Symbolic-family check

The exact checker also tests the support-distance argument for all directed support orders `3<=n<=50`.

It examines:

- 1,224 possible triangle-apex support positions; exactly 48 survive chordlessness, one immediate predecessor per order;
- 1,416 chordlessness-consistent quadrilateral position/hit patterns;
- 288 survive the global-minimum inequality;
- 240 are immediate-predecessor patterns and 48 are second-predecessor patterns;
- zero survivors occur outside `{u^-,u^{--}}`.

This is a finite sanity check only. The proof above is uniform in `n` and is the mathematical justification.

Checker path:
`proofnet24/collective-BT4/fleet03/B06/20260922T072201Z-fleet03-B06-bt4-r11/checker.py`  
Checker Git blob: `4163d8856dd65ef7d8de8b01e2bf5a2bf03785e2`  
Local checker SHA-256: `c7bdbfe0b68bcc13379b561958461dd9aeb877a7c61e819f5b6f3f73384cfa7b`.

Output path:
`proofnet24/collective-BT4/fleet03/B06/20260922T072201Z-fleet03-B06-bt4-r11/checker_output.json`  
Output Git blob: `7ef16c415f9e1fb948a8bada31eaf0411acda238`  
Local output SHA-256: `a4f9ab96d03de492f6dbbdd7be7c38865abadce37847f6a4aa893e76bedbd865`  
Validated payload SHA-256: `040ee069199bc11b7a0da2e1eb24c63758fc764021eb9c87229d9c3a4965c5da`.

## 7. What this pays for

The predecessor result left the F3 both-repeat splice with an arbitrary packed three-hit apex on `H`, `s`, or `U-u`. This theorem closes the **location freedom on `U`**: such an apex is not anywhere on the support, but lies in the two-vertex predecessor collar of `u`.

The non-immediate collar position carries additional structure: it is an equality case of global packing minimality and therefore generates a second minimum packing with the exact four-vertex remainder (2). In a true counterexample that remainder must be acyclic and cannot improve the secondary arc-maximal objective.

This is a genuine transfer into the full proof tree, not a census. It removes every farther `U`-support location and replaces the single sharp survivor by a new extremal/acyclic exchange constraint.

## 8. Exact next implication

The newly isolated second-predecessor debt is:

`BT4-R4-F3-SECOND-COLLAR-ACYCLIC-SPLICE-v1`:

> In the two-indirect F3 both-repeat state, assume the packed three-hit apex is `z=u^{--}`. Combine (i) the partner's one-cut acyclicity of `D[(U-{u}) union {s}]`, (ii) the neutral collar exchange and the required acyclicity of `D[{q,a,c,u^-}]`, (iii) the arc-max inequality (6), and (iv) the existing reciprocal/third-port/heavy-entry interfaces. Prove that the simultaneous constraints force a strict smaller packing, a directed cycle in one exchanged remainder, SIX, two disjoint replacement cycles, or a fourth directed cycle.

The immediate-predecessor `z=u^-` location, apex locations `z in H union {s}`, the single-repeat F3 profiles, F2, SIX and the independent larger-remainder branches remain explicit debts. They are not promoted here.

## 9. Failure checks and nonclaims

- `W` is one directed cycle, not itself a four-pack.
- The neutral cycle `C_z` is a replacement for `U`, not an additional disjoint cycle; only a cycle in its complement would close BT4.
- The conclusion `z=u^{--}` uses global minimum packing, not only chordlessness.
- Equation (6) uses the secondary arc-maximal choice and applies only after the exchanged complement is known acyclic.
- The 18-vertex graph is a sharpness certificate for the local lemma, not a target counterexample.
- The finite symbolic check does not prove the theorem; it only sanity-checks the uniform argument.
- No source-matching full proof or counterexample to BT4 is claimed.

## 10. Honest outcome

`ESSENTIAL_STEP_APPLIED` with the stronger immediate-predecessor-only statement `CANDIDATE_REFUTED`.

A packed three-hit apex on the light support `U` is now universally confined to `{u^-,u^{--}}`. The second-predecessor case is an exact equality case of minimum packing and forces a size-neutral whole-support exchange with a new four-vertex remainder that must be acyclic in a genuine BT4 counterexample. The inherited whole-graph certificate realizes the second-predecessor alternative sharply but its exchanged remainder is cyclic, demonstrating why the repaired global filter is necessary. BT4 remains `OPEN_NOT_PROVED`.
