# BT4 fleet01/B05 — rigid collision compression and the one-one domination fork

Run: `20260922T021302Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-RCC-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and directed digons are allowed in the source statement.

The fresh source check remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the exact conjecture remains unresolved for every `k>=4`; its theorem at the same `2k-1` threshold permits cycles that become directed after reversing one arc. No such near-directed cycle is counted below.

The inherited counterexample normal form used here is the campaign lead's oriented exact-outdegree-seven form, so digons have already been removed by the proved reduction before any oriented argument below is used.

## Exact peer mathematics consumed

I use the latest complete campaign-lead state:

- fleet02/B04, `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

It gives the oriented exact-seven minimum-counterexample normal form, a globally minimum-total packing `(A,B,C)` of three directed cycles, nonempty acyclic remainder `R`, chordless packed cycles, arc domination, 3-vertex-strongness, the universal pair-deletion `six-or-three-five` deficit split, and the equality-completion principle for neutral exchanges. Its conditional end-to-end proof still requires six-fan closure, cross-linkage closure, and exclusion of the remaining persistent no-six dynamics.

I consume the named assigned OTHER-account partner result:

- fleet02/B06, `b06-20260922T005655Z-24f482784ae2`, shared handoff blob `4698b80b250deb1ae5a9b289ed9be576d394c89a`.

That result constructs an exact-seven source-valid adversary to the false local claim that three cycle-supported five-witnesses must have distinct remainder exit heads. Total exit-head coalescence is therefore retained as a legitimate hard branch. Nothing below assumes distinct exit heads, two disjoint collars, or any local separation invalidated by that adversary.

The decisive new input is the newer OTHER-account integrator result:

- fleet02/B20, `20260922T020421Z-fleet02-B20-bt4-r11`, report blob `46c40bc86e66cf628612866d3efd3545dc27c6ba`, candidate collision-funnel localization.

For an original-remainder collision witness `z` of exact profile

`(a_A(z),a_B(z),a_C(z),d_R^+(z))=(4,1,1,1)`,                  (1)

write

`N+(z)∩B={beta}`, `N+(z)∩C={gamma}`, `N+(z)∩R={rho}`.        (2)

Then no vertex of `A` sends an arc to `z`, and

`N-(z)∩B subset {beta^-,beta^{--}}`,
`N-(z)∩C subset {gamma^-,gamma^{--}}`.                         (3)

A shortest directed cycle `Q` in `D[N-(z)]` avoids `A` and `N+(z)`, hence avoids `beta,gamma,rho`; its intersection with each light cycle is either a singleton from the two positions in (3), or the consecutive two-vertex block

`beta^{--}->beta^-`, respectively `gamma^{--}->gamma^-`.       (4)

If both light cycles have order greater than `r=|R|`, then `Q` meets both light cycles. Its internal remainder vertices lie in `R\{z,rho}`, and the reserved exit satisfies

`Reach_R(rho) ∩ (V(Q)∩R) = emptyset`.                           (5)

This run attacks that all-long `(4,1,1,1)` block-linkage branch by an actual two-cycle packing exchange.

## Correction to my preceding B05 residual

My preceding report `BT4-OLPA-v1` contained a correct orthogonal linkage--pivot augmentation lemma, but its later "triangle phase-lock" residual was vacuous inside the all-long three-sink linkage core in which it was presented.

Indeed, fleet04/B06 `BT4-SINKLINK-v1` supplies the linkage alternative only when both light cycles at the relevant sink have order strictly greater than `|R|`. In a three-sink remainder its predecessor lemma already gives `|R|>=4`. Hence three packed directed triangles of order three cannot simultaneously lie in that all-long linkage branch.

The orthogonal augmentation lemma remains valid as a conditional statement, but the triangle phase-lock corollary must not be counted as progress on the live all-long residual. I therefore change mechanism here rather than continue that vacuous subcase.

## Compact conditional route for this run

Assume BT4 false and work in the lead's normal form. Pair-deletion amplification gives a six-fan branch or persistent no-six branch. The six-fan closure is separate. In the persistent no-six branch, neutral pivots and fixed-pair deficits feed cross-linkages and collision witnesses. The newest B20 result reduces the difficult `(4,1,1,1)` collision to either a short-light branch or the all-long block-linkage (2)--(5).

The first unpaid implication is to turn that block-linkage plus its reserved exit into a legal exchange rather than merely name it. The theorem below does so whenever a singleton first-predecessor block has its only possible same-cycle mate. It also gives an exact new fork when both blocks are singletons.

## Lemma 1 — complementary singleton compression exchange

Assume (1)--(5), and assume the all-long branch

`|B|>r`, `|C|>r`.                                                (6)

Suppose

`Q∩B={beta^-}`                                                   (7)

and the second possible `B` inport is actually present:

`beta^{--}->z`.                                                  (8)

Then all of the following hold.

1. There is a size-neutral replacement cycle

   `B_z = beta^{--} -> z -> beta -> B[beta,beta^{--}]`,           (9)

   with

   `V(B_z)=(V(B)\{beta^-}) union {z}`.                            (10)

2. The three cycles `A,B_z,Q` are pairwise vertex-disjoint.

3. Exact size forcing gives

   `|C|=|Q|=r+1`,                                                 (11)

   and necessarily

   `Q∩C={gamma^{--},gamma^-}`,                                   (12)

   `V(Q)∩R=R\{z,rho}`.                                           (13)

4. `(A,B_z,Q)` is another globally minimum-total three-cycle packing. Its remainder is exactly

   `R'=(V(C)\{gamma^{--},gamma^-}) union {rho}`.                  (14)

5. In a BT4 counterexample, `D[R']` is acyclic and has at most two sinks.

6. The reserved exit `rho` is a sink of the original DAG `D[R]`.

### Proof

The arcs in (9) exist by (8), (2), and the directed support cycle `B`. The forward segment `B[beta,beta^{--}]` avoids `beta^-`, because the local cyclic order is

`beta^{--}->beta^-->beta->...->beta^{--}`.

Thus (10) follows and `|B_z|=|B|`.

By the B20 localization, `Q` uses no vertex of `A`, avoids `z`, and by (7) uses exactly the one `B` vertex omitted by `B_z`. Therefore `A,B_z,Q` are pairwise vertex-disjoint. This is the point at which the support accounting is essential: `z` has moved into `B_z`, while `beta^-` has moved into `Q`; no vertex is counted twice.

Since `(A,B,C)` is globally minimum among all three-cycle packings,

`|A|+|B_z|+|Q| >= |A|+|B|+|C|`.

Using `|B_z|=|B|` gives

`|Q|>=|C|`.                                                       (15)

But (7), the B20 two-vertex bound on `Q∩C`, and the fact that `Q` avoids both `z` and `rho` give

`|Q| <= 1+2+(r-2)=r+1`.                                         (16)

By (6), `|C|>=r+1`. Combining with (15)--(16) proves (11). Equality in (16) forces every available contribution to be saturated: `Q` uses two `C` vertices and all `r-2` allowable remainder vertices. The two-vertex form in (4) gives (12), and saturation gives (13).

Thus the new packing has exactly the same total size as `(A,B,C)`. To compute its remainder, note that `B_z` covers every `B` vertex except `beta^-` and covers `z`; `Q` covers `beta^-`, the two vertices in (12), and every original remainder vertex except `z,rho`; `A` is unchanged. Hence the only uncovered vertices are exactly those in (14).

If `D[R']` contained a directed cycle, that cycle together with `A,B_z,Q` would be four vertex-disjoint directed cycles, contradicting the assumed BT4 counterexample. Hence `R'` is acyclic.

Because `C` is chordless, after deleting the consecutive pair `gamma^{--},gamma^-`, the remaining vertices of `C` induce a directed path: every remaining `C` vertex except the unique predecessor of `gamma^{--}` still has its support successor in `R'`. Consequently among the `C` vertices in `R'` at most one can be a sink. The only other vertex of `R'` is `rho`, so `D[R']` has at most two sinks. This proves item 5.

Finally, (5) and (13) imply

`Reach_R(rho) ∩ (R\{z,rho})=emptyset`.                           (17)

If `rho` had an outneighbor `t` in `R`, then `t!=rho`. Also `t!=z`, because `z->rho` by (2) and the inherited normal form is oriented. Hence `t in R\{z,rho}`, contradicting (17). Therefore `d_R^+(rho)=0`, proving item 6. QED.

The proof uses only one remainder exit and is therefore compatible with the assigned partner's warning that exit heads may totally coalesce.

## Corollary 2 — symmetric form and escape from a three-sink hard core

Interchanging `B,beta` with `C,gamma` gives the symmetric statement:

if `Q∩C={gamma^-}` and `gamma^{--}->z`, then

`|B|=|Q|=r+1`,
`Q∩B={beta^{--},beta^-}`,
`V(Q)∩R=R\{z,rho}`,

and replacing `C` by the analogous `C_z` and the other light cycle by `Q` yields a globally minimum packing whose remainder has at most two sinks; again `rho` is an original remainder sink.

Therefore in the exact three-sink all-long hard core, either mate pattern in Lemma 1 is an **escape move** from that core. It does not by itself finish BT4, because the resulting `s<=2` branch and the six-fan branch are still live, but it removes this collision geometry from any closed three-sink neutral orbit.

## Corollary 3 — surviving one-one block linkages force an R-dominator

Assume the same all-long `(4,1,1,1)` setup and suppose the shortest inneighborhood cycle has the smallest cross form

`Q∩B={beta^-}`, `Q∩C={gamma^-}`.                                 (18)

If the state is to remain in the three-sink hard core after all available Lemma 1 exchanges, then

`beta^{--} -/> z`, `gamma^{--} -/> z`.                           (19)

Together with (3) and (18), this makes the light-cycle inport sets exact:

`N-(z)∩B={beta^-}`, `N-(z)∩C={gamma^-}`.                         (20)

Use arc domination on `beta^-->z`. A dominator `d_B` satisfies

`d_B->beta^-`, `d_B->z`.                                        (21)

It cannot lie in `A` because `A -/> z`; it cannot lie in `B` because (20) leaves no `B` inport other than `beta^-` itself. Hence

`d_B in C union R`.                                              (22)

Likewise a dominator `d_C` of `gamma^-->z` lies in

`d_C in B union R`.                                              (23)

If both dominators lay on the opposite light cycles, (20) would force

`d_B=gamma^-`, `d_C=beta^-`,

so (21) and its symmetric counterpart would give the digon

`gamma^- -> beta^- -> gamma^-`,

impossible in the oriented normal form. Therefore:

> at least one of the two singleton port arcs into `z` has a dominator `t in R` with `t->z` and with `t` also pointing to that singleton packed port.       (24)

Moreover `t!=rho`, since `z->rho` and the normal form is oriented. If `t` lies on `Q`, shortestness of `Q` forces the arc from `t` to the packed port to be the actual preceding edge of `Q`; otherwise that arc is a chord of the shortest directed cycle in `D[N-(z)]` and would produce a shorter one. If `t` is not on `Q`, it is a genuine off-linkage remainder predecessor carrying two specified heads.

Thus the smallest surviving block-linkage is no longer just “two singleton ports plus an arbitrary DAG path”: it carries a forced R-supported domination fork.

## How this changes the live proof frontier

The current all-long `(4,1,1,1)` collision branch now has the following exact split.

- If a singleton first-predecessor block has its second-predecessor mate, Lemma 1 gives an explicit neutral **two-cycle compression exchange** and the new remainder has at most two sinks.
- In the one-one block case with no such escape, Corollary 3 forces an R-dominator of one singleton port arc.
- The still-unpaid block geometries are singleton-at-the-second-predecessor, the two-vertex block cases, and the R-dominator fork from (24). The short-light branch from B20 is separate.

The immediate next splice target is therefore precise: combine the forced R-dominator in (24), or a second-predecessor/two-block geometry, with the reserved-exit separation (5) and the fleet03/B05 marked-segment exchange to obtain either a strict two-cycle reduction, another compression to `s<=2`, a six-fan, or a genuine four-pack.

This is strictly narrower than the prior request to “exploit the block-linkage.” It also respects the assigned partner's source-valid coalesced-exit counterexample: no step assumes that two support witnesses have different exit heads.

## Failure checks and boundary cases

- Every cycle displayed above is genuinely directed in the original digraph.
- The oriented hypothesis is used only after the lead's no-digon reduction; the target itself still allows digons.
- The size comparison uses global minimum of the **three-cycle packing**, not an unsupported shortest-cycle assumption.
- The new exchange accounts for every affected vertex explicitly; (14) is an equality of vertex sets, not a cardinality heuristic.
- The `<=2` sink conclusion uses chordlessness of the old packed cycle `C`; without that hypothesis non-support chords inside the new remainder could invalidate the simple path argument.
- The original-sink conclusion for `rho` additionally uses the B20 reserved-exit reachability separation and the orientation that forbids `rho->z` when `z->rho`.
- No claim is made that an `s<=2` remainder is already closed.
- No finite search, edge-disjoint substitute, one-reversed-arc relaxation, average-degree surrogate, or novelty inference from a search miss is used.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

The substantive new step is an explicit two-cycle compression exchange inside the latest `(4,1,1,1)` collision funnel. A singleton first-predecessor block plus its same-cycle mate forces exact equality, consumes every allowable old-remainder vertex, certifies the reserved exit as an original remainder sink, and produces a new globally minimum packing whose remainder has at most two sinks. If both linkage blocks are singleton and those compression moves are unavailable, arc domination forces a new R-supported common predecessor. Full BT4 remains open; six-fan, short-light, `s<=2`, and the residual block/R-dominator splice remain to be closed.
