# FOREST B02 — signed switching and exact 3-edge-cut reservoir injection

Run: `20260922T002011Z-account01-B02-FOREST-r11`  
Candidate: `FOREST-SWITCH-CORE-v2`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent target: **OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact target and inherited exact reduction

The target is the Grimmett–Winkler uniform-unrooted-forest pairwise negative-correlation conjecture: for every finite simple graph `G`, with `F` uniform over all acyclic edge subsets and distinct edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.


No complete current collective FOREST artifact from lead `account01/B01` was present at the bounded fresh archive check, so I used the exact compatible reduction from `account01/B03`, brain handoff blob `b49c6b896238cd62508b98549526dd12a469ceb3`, rather than wait.

Fix `e,f` and let `K=G-{e,f}`. For a forest `H` of `K`, put `X=1` iff `H+e` is a forest and `Y=1` iff `H+f` is a forest. Let `Aij` be the forests with `(X,Y)=(i,j)`, `nij=|Aij|`, `N=sum nij`, and

`Q={H in A11 : H+e+f is cyclic}`, `q=|Q|`.

The exact inherited identity is

`Delta := Z_e Z_f - Z Z_ef = n10*n01 - n00*n11 + N*q`.

Thus the whole conjecture for the marked pair is exactly

`n00*n11 <= n10*n01 + N*q`.                                  (1)

A proof that discards `q` is invalid; the inherited four-vertex regression already disproves that stronger route.

## 2. Compact conditional end-to-end argument

The desired injection-level proof can be organized as follows.

1. Start with the bad product set `D=A00 x A11` and the ordinary switch target `T=A10 x A01`.
2. Cancel every pair in `D` whose two coloured forests admit a marked 1-separation by a literal colour-swap involution. This has multiplicity exactly one and preserves acyclicity.
3. Send remaining bad pairs to either the remaining ordinary targets or the overlap reservoir `H_all x Q`.
4. Since `|T|=n10*n01` and `|H_all x Q|=Nq`, an injection in step 3 proves (1).

This run proves step 2 globally and step 3 completely whenever the marked edges lie in a cut of size at most three. The first unpaid universal implication is therefore the corresponding core injection after all marked 1-separations and marked cuts of size `<=3` have been removed.

## 3. Exact signed switching on marked 1-separations

For `(R,B)` two forests of `K`, colour the edges of `R` red and of `B` blue and write `U=R union B` for the uncoloured support.

A **marked 1-separation** of `U` is an edge partition

`E(U)=S disjoint_union T`

such that there are subgraphs on the two edge sets whose vertex sets contain the two endpoints of `e` on the `S` side and the two endpoints of `f` on the `T` side, and the two vertex sets intersect in at most one vertex. Isolated marked endpoints are permitted on their assigned side. Choose one canonically from `U` using any fixed total order on edge subsets.

Define the colour swap on the `S` side by

`R'=(R\S) union (B intersect S)`,
`B'=(B\S) union (R intersect S)`.                            (2)

### Lemma 3.1 — acyclicity

Both `R'` and `B'` are forests.

**Proof.** A cycle using edges from both sides of the separation would have to pass from one side to the other and back. A simple cycle therefore supplies two distinct common vertices, contradicting the intersection bound `<=1`. Hence every cycle is contained entirely in one side. On each side the relevant colour class in (2) is a subset of the original forest of that colour, so no such cycle exists. QED.

### Lemma 3.2 — marked connectivity is localized

Connectivity between the endpoints of `e` in `U` is determined entirely by the `S` side, and connectivity between the endpoints of `f` is determined entirely by the `T` side.

**Proof.** A simple path with both endpoints on one side cannot leave that side and later return if the two sides share at most one vertex: leaving and returning would force two distinct common vertices, or a repeated common vertex on a simple path. QED.

Therefore, if `(R,B) in A00 x A11`, the swap exchanges the `e`-connectivity status between the two colours while retaining their `f`-connectivity statuses. Hence

`(R',B') in A10 x A01`.

Conversely the same operation sends `A10 x A01` to `A00 x A11`. Because the uncoloured union `U` is unchanged, the canonical marked 1-separation is unchanged, and applying (2) twice returns the original pair. Thus this is a genuine involution with multiplicity exactly one.

Let `D_sep,T_sep` be the pairs admitting a marked 1-separation and `D_core,T_core` their complements. Then

`|D_sep|=|T_sep|`

and consequently the exact signed identity is

`n00*n11 - n10*n01 = |D_core|-|T_core|`,

so

`Delta = N*q + |T_core|-|D_core|`.                           (3)

This is the promised signed-switching reduction: all genuinely 1-separated mass cancels exactly; only a core with no such separation needs the overlap reservoir.

## 4. Exact reservoir injection across a marked 3-edge cut

### Theorem 4.1

Suppose some vertex cut of `G` has crossing edge set exactly

`delta_G(S)={e,f,g}`.

Then the marked pair `(e,f)` satisfies the desired negative-correlation inequality. More strongly,

`n00 <= q` and hence `n00*n11 <= N*q`.

**Proof.** Work in `K=G-{e,f}`. The edge `g` is the unique remaining edge crossing the cut.

Take `R in A00`. Since `R+e` is cyclic, the unique `R`-path between the endpoints of `e` exists. Because `e` crosses the cut and `g` is the only `K`-edge crossing it, that path contains `g`. The same argument for `f` shows the unique `R`-path between the endpoints of `f` also contains `g`.

Delete `g` and set `H=R-g`. Both marked endpoint pairs are now disconnected, so `H+e` and `H+f` are individually forests: `H in A11`.

On each side of the cut, the two marked endpoints on that side are connected in `H`: follow the corresponding prefixes of the two former `R`-paths to the endpoint of `g` on that side. Consequently `H+e+f` contains the cycle made of `e`, `f`, and these two side paths. Thus `H in Q`.

The map

`psi:A00 -> Q`, `psi(R)=R-g`

is injective, because the inverse on its image is simply `H -> H+g`. Therefore `n00<=q`. Since `n11<=N`,

`n00*n11 <= q*n11 <= q*N`,

which is stronger than (1). Equivalently the product map

`Psi:A00 x A11 -> H_all x Q`, `Psi(R,B)=(B,R-g)`

is multiplicity-one injective. QED.

If `delta_G(S)={e,f}` has size two, then no forest of `K` can connect the endpoints of either marked edge across that cut, so `A00` is empty and the claim is immediate. Hence every marked pair lying together in an edge cut of size at most three is settled.

## 5. Named OTHER-account result applied: `FOREST-OVERLAP-RESPONSE-v2`

I consumed `account03/B03` handoff `FOREST-OVERLAP-RESPONSE-v2`, blob `0358d8ad988f3abe17d3a80d4dd51befc5222fbb`. It gives, for `G_m=K_{3,m}` and two spokes `e=x r_1`, `f=y r_1` in the same right star, with `C=4^(m-2)`, among other exact formulas

`n00=C(m-1)(3m-2)/4`,
`n10=n01=C(m-1)`,
`n11=C(3m^2+11m+18)/4`,
`q=3C(m-1)(m+2)/4`.

That peer result proves that a q-free switch is cardinality-impossible and identifies a nontrivial additive three-terminal response coordinate `eta`.

Theorem 4.1 directly resolves this structured same-star marked pair for every `m>=2`: after removing `e,f`, the remaining spoke `g=z r_1` is the sole `K` edge across the cut `{r_1}`. Thus

`R -> R-zr_1`

injects `A00` into `Q` exactly. Numerically from the peer formulas,

`q-n00 = 2*C*(m-1) > 0`.

So the peer's warning is respected rather than bypassed: the overlap reservoir is essential, and in this family its required multiplicity is supplied by a literal cut-edge deletion. This does **not** show that `eta` can be discarded in the general two-separator problem.

The assigned partner `account02/B03` had no completed collective FOREST artifact at the final bounded check, so no partner claim was invented or awaited.

## 6. Exact finite regression

`forest_switching_checker.py` is a standard-library exact checker for the two proved mechanisms. It exhausts every labelled simple graph on `2..5` vertices with at least two edges and every present marked edge pair. It checks the marked-1-separation involution and signed core identity, and every marked three-edge-cut deletion map.

Executed output:

```text
FOREST_SWITCHING_REGRESSION_PASS
edge_pair_instances=11766
graphs=1074
marked_1sep_domain_pairs=19440
marked_1sep_target_pairs=19440
signed_identity_checks=11766
three_edge_cut_A00_forests=13584
three_edge_cut_domain_pairs=306588
three_edge_cut_instances=8130
```

Checker blob: `796802933fc9ef60bd6646b9f50f440eddbfc8eb`.  
Output blob: `be2e77fa985e968bc4528733ca072b7a87554c87`.

This is regression evidence only; the proofs above do not rely on finite enumeration.

## 7. First essential remaining implication

After exact cancellation of marked 1-separations and exact reservoir injection on marked cuts of size `<=3`, prove for every remaining marked pair

`|D_core| <= |T_core| + N*q`,                               (CORE)

by a multiplicity-controlled switch or equivalent signed identity. The genuinely new difficulty begins with a nontrivial 2-separator carrying at least two unmarked crossing possibilities: deleting one distinguished cut edge no longer gives a canonical inverse, and a naive local swap can have multiple preimages.

A useful next version should therefore treat the first true two-separator case with the **full boundary connectivity state** retained, explicitly proving its fibre bound. The `K_{3,m}` result remains a mandatory regression: any mechanism whose bookkeeping collapses the overlap state to three pairwise boundary weights is insufficient.

## 8. Status and limitations

`ESSENTIAL_STEP_APPLIED`, not a full proof candidate. The parent FOREST conjecture remains open. No novelty claim is made for the two lemmas pending literature comparison. No result here promotes repository state to an accepted theorem outside this private research archive.
