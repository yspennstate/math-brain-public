# BT4 account01/B04 — reciprocal sink-cross and post-pivot witness staircase

Run: `20260922T034517Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-MCR-v6-reciprocal-staircase`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and source boundary

Target: prove the genuine `k=4` Bermond--Thomassen statement that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint directed cycles. Directed digons are allowed in the source statement.

The fresh literature boundary remains unchanged. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly states that the genuine conjecture is unresolved for all `k>=4`; its theorem permits one arc reversal in each packed object and is not used below as a directed-cycle theorem. The genuine lower-`k` input is Lichiardopol--Por--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992: minimum outdegree five forces three disjoint directed cycles, and their strengthened `k=2` statement allows at most two degree-two exceptions to minimum outdegree three. I also use Lewandowski--Polcyn--Reiher, *Two disjoint cycles in digraphs*, J. Graph Theory 104 (2023), 461--469, arXiv:2205.10826v2, Theorem 1.4, only in the exact `(r,s)=(1,1)` specialization derived below.

## Exact live team state consumed

The newest complete campaign-lead package available at the substantive start remains account02/B04 run `20260922T031823Z-a02-b04-bt4-r11`, primary report blob `17d49d472779d5304d30b93c07ce89c289ab20d1` and controlling frontier addendum blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`. The addendum makes `SC+` the live frontier: in the canonical `NO-SIX` sink state, close the canonical sink-cross together with the neutral-pivot / x-free return interfaces without counting a single cross as a two-cycle replacement.

Named OTHER-account partner actually applied:

- account02/B05, `BT4-RSC-v6-postpivot-wall`, run `20260922T032614Z-b05-bt4-777e9239`, report blob `9ebdea5c728bbcf442a73dfc31df91f66b4da00b`.

Its exact facts used below are the neutral source-fan-two pivot and the freed-vertex wall. If `p in S -> x` is the canonical inport to a remainder sink and `N+(x) intersect S={p^+,p^{++}}`, put `q=p^+` and

`S' = p -> x -> p^{++} -> S[p^{++},p]`,

`R'=(R-{x}) union {q}`.

Then `(S',T,U)` is another globally minimum three-packing, `R'` is acyclic, `q` has exactly one `S'`-outneighbor (`p^{++}`), and, writing `e=d^+_{R'}(q)`, the branch `e>=2` supplies two internally disjoint post-`q` escape arms unless a cross/equality output occurs.

A compatible newer disjointness result was also source-read: account03/B05 `BT4-SC2-THIRD-PORT-v1`, run `20260922T034032Z-account03-B05-BT4-r13`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`. It shows that in its long-light same-port opposite-cross residual, a minimum return cycle forces a third packed port or a quantified same-support bypass. I use it only as a compatibility boundary: its long-light/same-port hypotheses are not silently extended here.

## Inherited normal form

Assume for contradiction a BT4 counterexample in the team's established normal form. Thus `D` is oriented and every vertex has outdegree exactly seven; `(H,S,U)` is a globally minimum-total packing of three directed cycles; the remainder

`R=V(D)\(V(H) union V(S) union V(U))`

is nonempty and acyclic; the packed cycles are chordless; every arc is dominated; and `D` is 3-vertex-strong.

Choose a sink `x` of `D[R]`. The previous account01/B04 theorem gives a direct packed inport `p->x`, with `p in S`, and the path-fan inequality gives

`m_S(x):=|N+(x) intersect S| <= 2`.

If `m_S(x)<=1`, then at least six arcs from `x` hit the complementary packed pair and the run is already in the separate SIX interface. Hence the persistent `NO-SIX` sink branch has `m_S(x)=2`. Since all seven outneighbors of `x` are packed and no pair receives six arcs, the other two fan sizes must be `3` and `2`. Relabel so

`(m_H(x),m_S(x),m_U(x))=(3,2,2)`.                 (1)

This run changes mechanism from the preceding domination-ladder work: first use 3-vertex-strongness to force a reciprocal cross, then use the complete `k=2` degree-sequence theorem on the partner's post-pivot residual.

## Lemma 1 — every canonical NO-SIX sink-cross has a reciprocal cross avoiding the sink

Under (1), there is a cycle `L in {H,U}` and two oppositely directed cross-packed paths

`P : S -> L`,
`Q : L -> S`,

such that

- `P` has the exact form `p -> x -> y` for some `y in L`;
- every internal vertex of `Q` lies in `R-{x}`;
- consequently `int(P) intersect int(Q)=empty`.

In particular the canonical sink-cross is never an isolated one-way interface: it always belongs to an internally-disjoint opposite-cross pair. The packed endpoints need not coincide, so this is not yet a two-cycle replacement.

### Proof

Because `D` is 3-vertex-strong, `D-x` is strongly connected. Pick any vertex `h in H`. In `D-x` choose a directed path from `h` to `p in S`, and make it simple.

Traverse this path from `h` toward `p`. Let `a` be its first vertex on `S`. Before `a`, let `b` be the last vertex belonging to the old packing. Since `a` is the first `S`-vertex and the path starts on `H`, the vertex `b` lies on `H` or `U`; call that packed cycle `L`. By the choices of `a,b`, every internal vertex of the subpath

`Q=b -> ... -> a`

lies in `R`. The entire ambient path lies in `D-x`, so those internal vertices lie in `R-{x}`. Thus `Q` is a genuine `L`-to-`S` cross-packed path avoiding `x`.

Equation (1) gives `m_L(x)>0`. Choose `y in N+(x) intersect L`. Then

`P=p -> x -> y`

is the canonical `S`-to-`L` cross, with sole internal vertex `x`. Therefore the two R-interiors are disjoint. QED.

### Exact significance

The lead's four-remainder analysis had an opposite-cross configuration as one branch. Lemma 1 shows that **opposite-cross geometry exists at every canonical NO-SIX sink, for every remainder size**, without a long-cycle assumption. What remains is the genuine packed-port/disjointness problem: two opposite crosses with different packed endpoints generally make only one alternating cycle, not two disjoint replacements.

This distinction is essential. The result pays the `return-existence` part of `SC+`; it does not pay the final splice.

## Lemma 2 — exact post-pivot pair-deletion staircase

Apply the partner's neutral pivot to the source-fan-two state and work with `(S',T,U)` and acyclic `R'`. Suppose `e=d^+_{R'}(q)>=2`. Consider

`G = D-(T union U) = D[V(S') union R']`.

Then one of the following happens:

1. there is a SIX witness for the pair `T union U`; or
2. the pair is NO-SIX and `G` has the following degree/fan staircase:
   - at least three vertices have pair fan exactly `5` into `T union U`;
   - at least four vertices have pair fan at least `4`;
   - at least five vertices have pair fan at least `3`;
   - at least six vertices have pair fan at least `2`.

Moreover, in case 2, `x` is one of the exact five-fan witnesses, `q` is not, and there are two additional exact five-fan witnesses `w1,w2` distinct from both `x` and `q`.

### Proof

`G` cannot contain two vertex-disjoint directed cycles: together with the untouched packed cycles `T,U` they would give four disjoint cycles in `D`.

For every `v in V(G)`, exact seven-outregularity gives

`d_G^+(v)=7-f_{TU}(v)`,

where `f_{TU}(v)=|N+(v) intersect (T union U)|`. If some `d_G^+(v)<=1`, then `f_{TU}(v)>=6`, which is case 1.

So assume NO-SIX. Then `delta^+(G)>=2`. Write the nondecreasing outdegree sequence of `G` as

`d1<=d2<=...<=dn`.

Lewandowski--Polcyn--Reiher Theorem 1.4 says a sequence forces two disjoint cycles iff it is large. Since the actual digraph `G` has no two disjoint cycles, its sequence is not large. For `(r,s)=(1,1)`, condition (1) of their Definition 1.3 is automatic from `d1>=2`. Therefore condition (2) must fail. This forces

`n>=3`, `d3=2`, and `dj<j` for every `j>=4`.

Hence

`d1=d2=d3=2`,
`dj<=j-1` for every `j>=4`.                         (2)

The partner's exact pivot gives `d_G^+(q)=1+e>=3`, while the original sink satisfies

`N+(x) intersect V(G) = {p^{++},q}`,

so `d_G^+(x)=2`. Thus `x` is one of the first three degree-two vertices, `q` is not, and there are at least two other exact degree-two vertices `w1,w2`. Degree two is equivalent to pair fan five.

Finally `e>=2` implies `R'` contains `q` and at least two distinct outneighbors of `q`, so `|R'|>=3`. Since `S'` is a directed cycle in an oriented digraph, `|S'|>=3`; hence `n>=6`. Applying (2) at `j=4,5,6` gives the 4/3/2 fan staircase. QED.

## Corollary 3 — compensation for many freed-vertex exits

In the post-pivot `e>=2` branch:

- if `e=2`, then `q` itself has pair fan exactly `4`;
- if `e>=3`, the required fourth vertex of pair fan at least `4` can be chosen distinct from `q,x,w1,w2`;
- if `e>=4`, `q` has pair fan at most `2`, so the fifth vertex of pair fan at least `3` is also distinct from `q`.

Indeed `f_{TU}(q)=7-(1+e)=6-e`. Thus increasing the number of remainder exits from the freed vertex cannot dissipate all cross-fan mass: the complete two-cycle degree-sequence theorem forces compensating high-fan vertices elsewhere.

## Corollary 4 — post-pivot R-witness / support-tripod dichotomy

Still in the pairwise NO-SIX `e>=2` branch, exactly one of the following useful outputs occurs:

- **R-five output:** at least one of `w1,w2` lies in `R'`, giving an additional remainder-supported five-witness for `T union U`; or
- **support-tripod output:** both `w1,w2` lie on `S'`. Then `x,w1,w2` are three distinct cycle-supported five-witnesses for the same pair `T union U`, each with exactly one `R'`-outneighbor and its cycle successor as its two residual outneighbors. Consequently two of the three are heavy on the same one of `T,U`.

### Proof

Only the support-tripod assertion needs explanation. Because `(S',T,U)` is globally minimum, `S'` is chordless: a non-successor chord would close with the complementary directed segment of `S'` to make a shorter cycle, reducing total packing size. Hence a vertex of `S'` has only its successor as an `S'`-outneighbor. If such a vertex has residual degree exactly two in `G`, its other residual outneighbor lies in `R'`, uniquely. The pair fan equals five, so one of `T,U` receives at least three of those five arcs. Three witnesses and two choices of heavy target give the final pigeonhole statement. QED.

This is the direct application of the named account02/B05 `BT4-RSC-v6-postpivot-wall`: its difficult `e>=2` two-arm branch is never accompanied only by `x` and the freed vertex. It necessarily carries two additional exact five-witnesses plus the full staircase above.

## Interaction with current disjointness work

The new reciprocal-cross lemma and the post-pivot staircase constrain different sides of the same `SC+` state:

- before/through the neutral pivot, the sink cross already has an opposite cross whose R-interior avoids `x`;
- after the pivot, the difficult freed-vertex `e>=2` wall automatically carries two more exact five-witnesses, and either an R-supported witness or a three-witness support configuration with a same-heavy pair.

Thus the surviving obstruction is no longer "find a return cross" or "find another deficit witness." Both are forced. The real issue is **packed-port compatibility**: use the opposite return and the additional witness/arm structure to obtain two vertex-disjoint replacements rather than a single alternating cycle.

The newest account03/B05 third-port theorem is compatible with this description. Whenever a reciprocal pair is tightened to its long-light same-port residual, `BT4-SC2-THIRD-PORT-v1` forces a third packed port or a quantified same-support collar. This report does not remove that theorem's long-light/same-port hypotheses.

## Compact conditional end-to-end proof after this run

A full BT4 proof follows if the final port-splice implication below is established.

1. Reduce a counterexample to the inherited oriented exact-seven, arc-dominated, 3-vertex-strong normal form with globally minimum three-packing and acyclic remainder.
2. Choose a remainder sink `x`. The existing account01/B04 theorem gives a direct packed inport and canonical length-two cross.
3. Source fan at most one enters the SIX interface. In persistent NO-SIX, the sink fan pattern is exactly `(3,2,2)`.
4. Lemma 1 now supplies an opposite cross with disjoint R-interior, for every remainder size. Hence the canonical cross is automatically reciprocal at the level of packed-cycle interfaces.
5. In the source-fan-two branch, perform the partner account02/B05 neutral pivot. Its `e=0` and `e=1` cases are SIX / R-five interfaces. For `e>=2`, Lemma 2 forces two further exact five-witnesses and a full 5/4/3/2 pair-fan staircase.
6. Corollary 4 reduces those extra five-witnesses to either an R-supported witness or a same-heavy support pair inside a three-witness tripod, while the partner simultaneously supplies its two-arm wall unless cross/equality already occurs.

Therefore the first essential missing implication is now:

> **BT4-RECIPROCAL-PORT-SPLICE-v1.** In the canonical NO-SIX sink state, use an internally-disjoint opposite-cross pair supplied by Lemma 1 together with the neutral-pivot outputs of account02/B05 and the additional five-witness/staircase structure of Lemmas 2--4 to force either (i) two vertex-disjoint replacement directed cycles, (ii) a strict reduction of the globally minimum three-packing, (iii) a directed cycle in an exchanged remainder, or (iv) a proved SIX/lower-k closure. It is enough to close separately the R-five output and the same-heavy support-tripod output.

This is narrower than the lead's prior `SC+`: existence of a return interface and multiplicity of pair witnesses are now paid. The unpaid part is the actual two-cycle splice with packed endpoints in the correct cyclic order.

## Exact deletion/contraction lesson for this slot

The previous B04 runs already established the exact one-cycle formulas

`d^+_{D-C}(v)=7-a_C(v)`,

`d^+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`,

plus loss of multiplicity at the contracted vertex. This run adds the corresponding **pair-deletion loss profile** in the live post-pivot state: if deleting `T union U` loses at most five outgoing arcs at every surviving vertex, then the whole residual degree sequence is forced into (2), not merely three isolated degree-two exceptions. In particular the partner's freed vertex can spend extra degree inside the remainder only by forcing compensating high pair-fans elsewhere. This is a structural obstruction to using deletion as a naive induction step and a concrete replacement for average-degree reasoning.

## Failure checks and nonclaims

- A single cross or an opposite-cross pair is not counted as two replacement cycles.
- The two reciprocal paths of Lemma 1 have disjoint **remainder interiors**; their packed endpoints are not asserted equal or cyclically aligned.
- The Lewandowski--Polcyn--Reiher theorem is used only on the actual residual outdegree sequence of a digraph known not to contain two disjoint cycles; no average-degree surrogate is used.
- The post-pivot cycle `S'` is chordless because the pivot preserves global minimum total packing size; no chordlessness claim is made for an arbitrary larger replacement packing.
- The target permits digons; orientation is used only in the inherited normal form after the genuine `k=3` theorem removes the digon case.
- No near-directed cycle from the 2026 relaxation is counted.
- No finite computation, edge-disjoint substitute, or novelty claim is used.
- Full BT4 remains open.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

New paid facts: every canonical NO-SIX sink-cross has an opposite R-interior-disjoint return interface, and the partner's difficult post-pivot `e>=2` branch automatically carries two additional exact five-witnesses plus the complete residual fan staircase. The remaining mathematical obstruction is the packed-port/disjointness splice, not return existence or witness multiplicity.
