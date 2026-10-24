# BT4 account02/B05 — two-support domination lift and four-remainder cross-or-neutral closure

Run: `20260922T022612Z-b05-bt4-888b6a96`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-RSC-v5-two-support-lift`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

The target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so digons count. The oriented exact-outdegree-seven model below is only the inherited minimum-counterexample normal form.

The current source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the exact conjecture is still unresolved for `k>=4`; their theorem at the same `2k-1` threshold allows each packed cycle to become directed after reversing at most one arc. No such near-directed cycle is promoted here to a directed cycle.

## Exact peer state consumed

I read the newest complete campaign-lead state:

- account02/B04, `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`;
- its four-remainder escape addendum blob `45500a8c943831271fc031cf79bafeb5e7faed51`.

The lead normal form used here is an oriented spanning counterexample `D` in which every vertex has outdegree exactly seven, `(A,B,C)` is a globally minimum-total packing of three directed cycles, the remainder

`R=V(D)\(V(A) union V(B) union V(C))`

is nonempty and acyclic, the packed cycles are chordless, every arc is dominated, and `D` is 3-vertex-strong. For each packed pair, the strengthened `k=2` input gives either a residual vertex of outdegree at most one (a six-or-more fan into that pair) or at least three residual vertices of outdegree exactly two (five-fan witnesses). The global `NO-SIX` branch means the second alternative holds for all three packed pairs, equivalently every vertex sends at most five arcs into each packed pair.

The named OTHER-account partner result actually consumed and applied is account03/B06:

- `BT4-G1-PORT-EXCLUSION-v1`, run `20260922T014956Z-account03-B06-BT4-r12`, report blob `1e45b25528a0a5f5b87edcf80290f33d4f394894`.

Its exact input used below is: at a G1 no-six sink `x`, the unique light return port `b` is not a five-witness for the opposite packed pair, so at least two additional opposite-pair five-witnesses lie in `(B\{b}) union R`. Its exact sharpness certificate also warns that support cardinality alone cannot force those witnesses out of the immediate light-cycle collar.

I also use these completed compatible results:

- account04/B05 `BT4-COUNT-v3-FOUR-R-ESCAPE`, report blob `1a21f9b5ea72de714311d6927183c73062323632`, which had reduced every four-remainder no-six state to a cross transition, a neutral equality exchange, or an `R`-internal same-cycle bypass;
- account01/B06 fixed-pair/collar report blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`: an `R`-supported five-witness heavy on a packed cycle with fan `m>=3` gives either a genuine cross-packed transition, a size-neutral equality exchange, or three strict pure-`R` collars forcing `|R|>=3m-2`;
- account03/B05 overlap report blob `0ef2992efa4cc705d5479f1d061c1cc70327190e` and collision addendum blob `17dfd5ed1d8b141ec7c3d1f4fc21478cf1cb4f5b`, especially the pairwise-overlap five-witness profile;
- account02/B20 collision-funnel report blob `46c40bc86e66cf628612866d3efd3545dc27c6ba`, especially its surviving `(4,1,1,1)` collision with one remainder exit and positive packed support on both light cycles.

No peer outcome label is used as a theorem.

## Lemma 1 — finite domination lift for an internal remainder arc

Let `z,rho in R` and suppose `z->rho`. Then there is a packed vertex `p in A union B union C` and a directed path

`p=q_k -> q_{k-1} -> ... -> q_1 -> q_0=z`

whose internal vertices `q_0,...,q_{k-1}` all lie in `R`, and every `q_i` (including `p=q_k`) also sends an arc directly to `rho`.

### Proof

Put `q_0=z`. Since every arc is dominated, the arc `q_i->rho` has a dominator `q_{i+1}` with

`q_{i+1}->q_i` and `q_{i+1}->rho`.

Continue while the chosen dominator lies in `R`. The vertices cannot repeat: a repetition in the sequence would close a directed cycle along the arcs

`q_{j}->q_{j-1}->...->q_i=q_j`

inside `R`, contradicting acyclicity. Because `R` is finite, the process eventually leaves `R`; the first vertex outside `R` lies on one of the three packed cycles. The displayed path and the direct arcs to `rho` are exactly the domination relations accumulated in the construction. QED.

This is the boundary-lift mechanism from the previous B05 run, stated here in the minimal form needed below. No heavy-target avoidance is required.

## Lemma 2 — two packed supports plus one remainder exit force a genuine cross transition

Let `z in R` have an outneighbor `rho in R`. Suppose `z` also has outneighbors on two distinct packed cycles, say

`z->b`, `b in B`, and `z->c`, `c in C`.

Then there is a directed path from one packed cycle to a *different* packed cycle whose internal vertices all lie in `R`.

### Proof

Apply Lemma 1 to `z->rho`. Let the packed apex `p` lie on cycle `X in {A,B,C}`. The lifted path

`p -> ... -> z`

has all internal vertices in `R`.

At least one of `B,C` differs from `X`. If `X!=B`, append `z->b`; otherwise append `z->c`. The resulting directed path starts on `X`, ends on a different packed cycle, and has no packed internal vertex. It is therefore a genuine cross-packed transition in the original digraph. QED.

### Useful contrapositive

In any branch containing **no** cross-packed transition, every nonsink vertex of `R` sends packed arcs to at most one of `A,B,C`.

This is stronger than the earlier heavy-target version of the boundary lift. It does not need the target of the internal `R` arc to be heavy; the second packed support supplies the change of cycle at the *other end* of the lifted path.

## Corollary 3 — the `(4,1,1,1)` two-pivot collision is already a cross-transition branch

Account02/B20's surviving collision profile has a remainder vertex `z` with

`(a_A(z),a_B(z),a_C(z),d_R^+(z))=(4,1,1,1)`.

Thus `z` has a remainder exit and has packed outneighbors on both `B` and `C`. Lemma 2 applies immediately.

Hence the whole `(4,1,1,1)` collision is sent directly to the lead's cross-linkage closure. The additional short-light / reserved-exit block-linkage subdivision from the B20 report remains true but is not needed merely to obtain a genuine cross-packed transition.

This is a strict simplification of the current collision funnel. It uses the actual directed graph and does not turn a reversed-arc cycle into a directed one.

## Corollary 4 — pairwise-overlap five-witnesses have a sharp no-cross form

Suppose `z in R` is a five-witness for a packed pair, say `A union B`, and `d_R^+(z)>0`.

If `z` has at least one outneighbor in each of `A` and `B`, Lemma 2 gives a cross-packed transition. Therefore in a no-cross branch all five pair-fan arcs of such a witness must lie on one packed cycle, say `A`:

`a_A(z)=5`, `a_B(z)=0`.

Now apply the account01/B06 `R`-supported heavy-witness collar with `m=5`. It yields one of:

1. a genuine cross-packed transition;
2. a size-neutral equality exchange;
3. `|R|>=3*5-2=13`.

Consequently:

> In a no-cross, no-equality branch with `|R|<=12`, no nonsink remainder five-witness can occur for any packed pair.

Applied to account03/B05's pairwise-linkage-overlap analysis, this means that a pairwise-overlap vertex which is itself a five-witness cannot remain a small-remainder obstruction: its two forced remainder arcs either combine with a split pair-fan to give Lemma 2, or a monochromatic five-fan invokes the `m=5` collar above.

## Corollary 5 — application to the named partner's G1 port-exclusion theorem

In account03/B06's G1 state, the unique return port `b` is not an `H union C` five-witness, and persistent no-six therefore supplies at least two further `H union C` five-witnesses in

`(B\{b}) union R`.

Assume in addition that there is no cross-packed transition, no equality exchange, and `|R|<=12`. By Corollary 4, any one of those additional witnesses that lies in `R` must be a **sink** of `R`; a nonsink remainder witness would force cross/equality or `|R|>=13`.

Thus the partner's localization sharpens in this range to

`additional witnesses subseteq (B\{b}) union Sink(R)`.

This uses the partner's exact port-exclusion result rather than merely citing its outcome. It also respects the partner's 20-vertex sharpness certificate: that certificate has `|R|=8` but places its extra witnesses on the immediate support collar, which is explicitly allowed by the sharpened conclusion.

## Theorem 6 — every four-remainder no-six state has a cross transition or a neutral exchange

Assume the inherited exact-seven minimum-counterexample normal form, the global `NO-SIX` branch, and

`|R|=4`.

Then at least one of the following occurs:

1. a genuine cross-packed transition;
2. a size-neutral globally minimum packing exchange.

In particular, the strict same-cycle bypass in account04/B05's `BT4-COUNT-v3-FOUR-R-ESCAPE` theorem is no longer needed as a third terminal output in the four-remainder branch.

### Proof

Suppose for contradiction that neither a cross transition nor a neutral exchange exists.

**Step 1: every nonsink of `R` has at least two `R`-outneighbors.**  
Take a nonsink `v in R`. It has some internal arc `v->rho`. By the contrapositive of Lemma 2, all packed outneighbors of `v` lie on at most one packed cycle.

Because the state is global NO-SIX, `v` sends at most five arcs into every packed pair. Since all its packed arcs lie on one cycle, the total number of packed outneighbors of `v` is at most five. Exact outdegree seven therefore gives

`d_R^+(v)>=2`.                                                    (1)

For `|R|=4`, this also means every nonsink has packed degree four or five and `R`-outdegree three or two.

**Step 2: the DAG `D[R]` has at least two sinks.**  
Every finite DAG has a sink. If it had a unique sink, take the last nonsink in a topological ordering. All its `R`-outneighbors would have to be that single sink, so its `R`-outdegree would be at most one, contradicting (1).

Four sinks are impossible by the established no-six sink localization: every no-six sink has an inneighbor in `R`. Hence the number of sinks is two or three.

**Step 3: three sinks contradict the lead's four-remainder trident.**  
The lead's addendum blob `45500a8c943831271fc031cf79bafeb5e7faed51` treats precisely the `|R|=4`, three-sink no-six core. Each support cycle carries a forced residual-degree-two port, and the resulting support moves include explicit size-neutral exchanges; indeed at least one support-distinct neutral move must leave the three-sink hard core. This contradicts the present assumption that no neutral exchange exists.

**Step 4: two sinks force an `m=5` remainder witness.**  
Suppose exactly two vertices of `R` are sinks. The other two are nonsinks. Choose the later nonsink `v` in a topological ordering of `D[R]`. Its only possible later vertices are the two sinks, hence

`d_R^+(v)<=2`.

Together with (1),

`d_R^+(v)=2`.

So `v` has exactly five packed outneighbors. By Lemma 2's no-cross contrapositive, all five lie on one packed cycle, say `A`.

Then `v` is an `R`-supported five-witness for either packed pair containing `A`, with heavy fan `m=5`. Apply account01/B06's collar trichotomy. It gives a cross transition, a neutral equality exchange, or

`|R|>=3m-2=13`.

The first two contradict our assumptions and the third contradicts `|R|=4`.

All possible sink counts are excluded. Hence the assumed featureless state cannot exist. QED.

## What changed relative to the inherited frontier

Before this run, account04/B05 had proved that a four-remainder global-no-six state exports at least one of three objects:

- a cross-packed transition;
- a neutral equality exchange;
- an `R`-internal same-cycle bypass, possibly strict.

After Theorem 6, the third object is not needed as a terminal possibility. Every four-remainder no-six state already exports either a genuine cross transition or a neutral minimum-packing exchange.

Independently, the account02/B20 `(4,1,1,1)` collision no longer needs to be split into short-light versus reserved-exit linkage subbranches in order to reach cross geometry: its single `R` exit plus its two light packed supports force the cross transition directly by Lemma 2.

These are disjointness-preserving inputs. They do **not** assert that one cross transition by itself gives two replacement cycles.

## Compact conditional end-to-end argument at the new frontier

Assume a minimum BT4 counterexample and use the lead's exact-seven/global-minimum normal form.

1. Pair-deletion amplification splits each minimum-packing state into the SIX or NO-SIX branch.
2. The SIX branch remains the lead's separate six-fan/two-cycle-splice obligation.
3. In NO-SIX with `|R|=4`, Theorem 6 now forces either a genuine cross-packed transition or a neutral minimum-packing exchange. There is no additional featureless strict-bypass endpoint.
4. A neutral exchange regenerates the universal pair deficits because the ambient digraph and the untouched pair-deletion theorem are unchanged. The lead's three-sink addendum already proves that the smallest three-sink neutral core cannot close on itself.
5. The `(4,1,1,1)` collision branch and every small-remainder nonsink five-witness with split packed support feed cross geometry immediately by Lemma 2.

Therefore the first essential missing implication is now narrower:

> **Cross-to-two-cycle splice / neutral-orbit closure.** Given one of the genuine cross-packed transitions forced above, combine it with the team's support-correct return/linkage structure to construct two vertex-disjoint replacement directed cycles, or prove that repeated neutral exchanges in the `|R|=4,s<=2` branch must reach such a cross transition (or the SIX branch) before returning to the same packing state.

One cross transition alone can merge two packed cycles into one and is not yet enough for four vertex-disjoint cycles. That disjoint two-cycle reconstruction remains unpaid. The SIX branch and all `|R|>=5` branches also remain live.

## Failure checks and nonclaims

- No edge-disjoint or near-directed surrogate is used.
- The source problem permits digons; orientation is used only inside the inherited minimum-counterexample normal form where digons have already been eliminated.
- Lemma 2 needs a real internal remainder arc and positive packed support on two different cycles. It does not apply to a remainder sink or to the `(5,0,0,2)` collision profile, whose packed support is monochromatic.
- Corollary 4 uses the account01/B06 collar only after the witness is genuinely in `R`; no cycle-supported witness is fed into a remainder-only lemma.
- Theorem 6 does not close the cross-linkage branch and does not exclude a neutral orbit in the two-sink four-remainder state by itself.
- The named partner's local sharpness certificate is not contradicted: its difficult off-pivot witnesses can stay cycle-supported, exactly as Corollary 5 permits.
- No computation was used in this run.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

New proved step: a nonsink remainder vertex with packed support on two cycles automatically lifts, by arc domination and acyclicity, to a genuine cross-packed transition. This directly closes the `(4,1,1,1)` collision into the cross branch and strengthens the entire `|R|=4` global-NO-SIX frontier to **cross transition or neutral exchange**.

Full BT4 remains OPEN / NOT PROVED.
