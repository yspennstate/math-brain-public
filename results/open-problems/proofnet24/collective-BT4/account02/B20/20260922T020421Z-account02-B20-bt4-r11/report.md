# BT4 account02/B20 — collision-funnel localization after the two-pivot fork

Run: `20260922T020421Z-account02-B20-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target-level change: `NONE` — no proof of BT4 is claimed.  
Mechanism change: `YES` — the `(4,1,1,1)` collision from the prior two-pivot fork is reduced to a short-light alternative or an exact two-block cross-linkage with a reserved, topologically separated remainder exit; the `(5,0,0,2)` collision gains a quantitative inport-density/cross-transition alternative.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact target and current source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and directed digons are permitted by the source problem. The oriented exact-outdegree-seven model below is only the inherited minimal-counterexample normal form.

Fresh scientific master checked before write: `3a4c530471ef88fc74d52a88ccd8967ed605a2ff`.

Latest campaign lead actually consumed:

- account02/B04 `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

Its current conditional proof requires six-fan closure, cross-linkage closure, and exclusion of long neutral no-six orbits. Its off-pivot witness lemma says a neutral light pivot at a `(3,2,2)` no-six sink either creates a six-fan or regenerates a five-witness outside the pivot pair.

Named completed OTHER-account partner actually consumed:

- account04/B06 `20260922T011432Z-b06-bt4-r11`, candidate `BT4-SINKLINK-v1`, report blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`.

Its source-valid sink-inneighborhood localization derives a directed cycle in the inneighborhood of a no-six sink and converts it into either a short light cycle or a genuine two-way light-cycle linkage through the acyclic remainder.

I also use the universal deletion-deficit and arc-domination normal form already present in the lead state, and the prior account02/B20 late addendum `late_lead_addendum.md`, blob `aac4b9da986de7371a255291e71268e2f47aeca2`.

## Before this run: exact first unpaid collision

In the named partner's linkage branch, the prior B20 two-pivot argument makes both light neutral pivots available. If neither pivot creates a six-fan, the lead's regenerated deficit theorem gives five-witnesses `z_B,z_C` for the two complementary pairs. If they coincide at `z`, then `z` lies in the original remainder and has one of exactly three profiles

`(a_A(z),a_B(z),a_C(z),d_R^+(z))`

`=(5,0,0,2), (4,1,1,1), (3,2,2,0)`.

The last profile is another no-six sink and therefore already feeds the named partner's localization. The first two non-sink funnel profiles were still unconstrained beyond their degree counts. This run attacks those profiles directly, beginning with `(4,1,1,1)`.

Throughout, `(A,B,C)` is a globally minimum-total three-cycle packing in the exact-seven oriented counterexample and `R` is its acyclic remainder.

## Lemma 1 — a `(4,1,1,1)` collision has at most two inports from each light cycle

Let `z in R` satisfy

`|N+(z)∩A|=4`, `|N+(z)∩B|=|N+(z)∩C|=1`, `d_R^+(z)=1`.

Write

`N+(z)∩B={beta}`, `N+(z)∩C={gamma}`, `N+(z)∩R={rho}`.

Then

`N-(z)∩B subset {beta^-, beta^{--}}`,
`N-(z)∩C subset {gamma^-, gamma^{--}}`.

In particular each light cycle contributes at most two inports to `z`.

### Proof

Because the `A`-fan has size four, the inherited one-vertex exchange lemma forbids every arc from `A` to `z`.

Take any `b in B` with `b->z`. Orientation gives `b!=beta`. Let `p=d_B(b,beta)` be the forward edge-distance on `B`, so `1<=p<=|B|-1`. The arcs

`b -> z -> beta`

followed by the directed complementary segment `B[beta,b]` form a genuinely directed cycle `W_b` using only `z` and vertices of `B`. It is disjoint from `A` and `C`. Its order is

`|W_b|=|B|-p+2`.

Since `(A,B,C)` minimizes total covered vertices among three-cycle packings, `(A,W_b,C)` cannot be smaller. Hence

`|B|-p+2 >= |B|`,

so `p<=2`. Therefore `b` is `beta^-` or `beta^{--}`. The proof for `C` is identical. QED.

This is the non-sink analogue of the named partner's unique-light-return localization: the one light outport permits two, but only two, possible return ports, and their positions are fixed.

## Lemma 2 — a shortest inneighborhood cycle has two-vertex block form

Under Lemma 1, the induced digraph `D[N-(z)]` contains a directed cycle. Choose one, `Q_z`, of minimum length. Then:

1. `Q_z` is disjoint from `A`;
2. `Q_z` is disjoint from `N+(z)`, hence from `beta,gamma,rho`;
3. `Q_z` meets `B union C`;
4. `Q_z∩B` is either empty, one vertex, or the consecutive directed block `beta^{--}->beta^-`; likewise `Q_z∩C` is empty, one vertex, or `gamma^{--}->gamma^-`.

### Proof

Every arc of the extremal counterexample is dominated. If `u->z`, a dominator `v` satisfies `v->u` and `v->z`. Thus every vertex of `D[N-(z)]` has indegree at least one inside that induced digraph, so it contains a directed cycle.

No vertex of `A` sends an arc to `z`, proving (1). Every vertex of `Q_z` sends an arc to `z`; if `z` also sent an arc back to such a vertex, the oriented normal form would contain a digon. Hence (2). Since `D[R]` is acyclic and `Q_z` avoids `A`, it must meet `B union C`, proving (3).

Lemma 1 gives at most the two displayed candidates on each light cycle. If both `beta^{--}` and `beta^-` lie on `Q_z`, the arc `beta^{--}->beta^-` lies in the induced inneighborhood. A shortest directed cycle has no chord: any non-cycle arc between two of its vertices together with the complementary directed segment gives a shorter directed cycle. Therefore the two vertices must be consecutive on `Q_z` via that old `B`-edge. The `C` statement is symmetric. QED.

## Lemma 3 — collision-funnel localization for `(4,1,1,1)`

Put `r=|R|`. At least one of the following holds.

**(S1) Short-light alternative.** One light cycle, say `B`, satisfies

`|B| <= r`.

If `Q_z` meets only `B` in one vertex, the sharper bound `|B|<=r-1` holds. If `|B|=r` in the one-light branch, then necessarily `Q_z∩B={beta^{--},beta^-}` and `Q_z` uses every vertex of `R\{z,rho}`.

**(L1) Reserved-exit block-linkage alternative.** `Q_z` meets both `B` and `C`. Each intersection is a block of size one or two as in Lemma 2. The two portions of `Q_z` between the `B`-block and the `C`-block have pairwise disjoint internal vertex sets contained in

`R\{z,rho}`.

Every such internal remainder vertex sends an arc to `z`, while `rho` is not on the linkage and satisfies

`Reach_R(rho) ∩ (V(Q_z)∩R) = emptyset`.                    (1)

Consequently, if both light cycles have order strictly greater than `r`, alternative (L1) is forced.

### Proof

If `Q_z` meets only `B`, the three cycles `A,Q_z,C` are vertex-disjoint. Global minimum therefore gives `|B|<=|Q_z|`. By Lemma 2, `Q_z` uses at most two vertices of `B`. Its remainder vertices avoid both `z` and the unique remainder outneighbor `rho`, so there are at most `r-2` of them. Thus

`|B| <= |Q_z| <= 2+(r-2)=r`.

If only one `B` vertex occurs, the upper bound improves to `r-1`. Equality `|B|=r` forces both `B` vertices and all `r-2` allowable remainder vertices to occur, giving the stated exact cage. The same argument holds with `C` in place of `B`.

If `Q_z` meets both light cycles, Lemma 2 says each light intersection is one contiguous directed block. Hence the two complementary segments of the simple cycle `Q_z` between these blocks have only remainder vertices internally; they are internally disjoint. Item (2) of Lemma 2 removes `rho`, and every vertex of `Q_z` points to `z` by definition of the inneighborhood cycle.

Finally, if a directed path in `R` ran from `rho` to some `q in Q_z∩R`, then

`z -> rho -> ... -> q -> z`

would be a directed cycle inside `R`, contradicting acyclicity. This proves (1). If both `|B|` and `|C|` exceed `r`, neither one-light case is possible, so (L1) is forced. QED.

The new information is not merely another linkage name: in the surviving cross branch the unique remainder exit of the collision witness is guaranteed to stay outside the linkage and is topologically unable to reach its remainder interior.

## Lemma 4 — the `(5,0,0,2)` collision has a dense-inport/cross-transition alternative

Now let `z in R` have profile

`(5,0,0,2)`

and write its two remainder outneighbors as `rho_1,rho_2`. Again `A` sends no arc to `z`. Let `Q_z` be a shortest directed cycle in `D[N-(z)]`. Then `Q_z` avoids

`A union {z,rho_1,rho_2}`

and meets `B union C`.

If `Q_z` meets only `B`, putting `k=|Q_z∩B|` gives

`k >= |B|-r+3`.                                             (2)

Thus, for example, `|B|>r` forces at least four distinct vertices of `B` to send arcs to `z`. The same holds symmetrically for `C`.

If `Q_z` meets both `B` and `C`, then along `Q_z` there is a directed transition from a last `B`-vertex to a first `C`-vertex and another from a last `C`-vertex to a first `B`-vertex whose internal vertices lie in `R\{z,rho_1,rho_2}`; all such internal vertices point to `z`. Moreover neither `rho_i` can reach any `Q_z` remainder vertex inside `R`.

### Proof

The existence and avoidance statements are the same domination/orientation argument as Lemma 2. If `Q_z` meets only `B`, then `A,Q_z,C` is a three-cycle packing, so `|B|<=|Q_z|`. At most `r-3` remainder vertices are available because `z,rho_1,rho_2` are excluded. Hence

`|B| <= |Q_z| <= k+r-3`,

which is (2). If both light cycles occur, take adjacent changes of packed-cycle type in the cyclic sequence of `B/C` vertices on `Q_z`; the intervening vertices are in `R`. The reachability exclusion follows exactly as in Lemma 3 from `z->rho_i`, `q->z`, and acyclicity of `R`. QED.

This does not yet bound the number of light inports in the `(5,0,0,2)` branch; instead it turns a one-light inneighborhood cycle into a quantitative return-density requirement, while every cross-light cycle carries two reserved downstream exits.

## Comparison with the last three substantive B20 runs

- `20260922T000112Z`: fan-only counting was refuted and replaced by global missing-arc saturation.
- `20260922T010226Z`: neutral exchanges gained a quadratic confinement, unique heavy-target inport, third-side inlink, and a five-fan reachability cut.
- `20260922T013238Z`: the six-fan equality cage gained the port-triangle/triple-dominator reduction; after the later lead/partner update, the no-six linkage branch gained the two-pivot fork and the three exact collision profiles.

The present run does not repeat any of those mechanisms. It takes the first still-unpaid non-sink collision profiles and applies a different device: a shortest directed cycle in the collision witness's inneighborhood, plus exact one-light replacement accounting. There is therefore no three-unchanged-run stagnation; mechanism movement is new.

## Updated conditional end-to-end route and first unpaid universal step

The lead's conditional route remains valid: close six-fans; close cross-linkages; exclude persistent neutral no-six orbits. In the partner linkage branch, the prior two-pivot fork reduces a collision to the three profiles above. This run now sends them as follows:

- `(3,2,2,0)`: another no-six sink, handled by the partner's sink localization;
- `(4,1,1,1)`: either a light cycle has order at most `|R|`, or there is a source-valid two-block `B/C` linkage whose unique `R` exit is reserved and topologically separated from the linkage interior;
- `(5,0,0,2)`: either a one-light inneighborhood cycle forces the exact inport-density bound (2), or a cross-light transition exists with two reserved downstream exits.

The first unpaid universal implication is therefore narrower:

> Exploit the reserved-exit separation in `(L1)` (or the two-exit analogue in Lemma 4) together with the account03/B05 segment-exchange inequality and account04/B06 missing-arc/forced-exit certificates to force a strict two-cycle exchange, a six-fan state, or four vertex-disjoint directed cycles. In the one-light branches, either close the exact `|light|<=|R|` cage or convert the dense return set of (2) into the same cross-linkage/strict-exchange outcome.

No edge-disjoint, near-directed, one-reversed-arc, higher-threshold, finite-order or routine-subclass surrogate is used.

## Honest status

`ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

Full BT4 remains open in this candidate. The target-level state is unchanged; the mechanism-level collision obstruction is strictly narrower and now carries an explicit reserved-exit reachability cut suitable for the next splice argument.
