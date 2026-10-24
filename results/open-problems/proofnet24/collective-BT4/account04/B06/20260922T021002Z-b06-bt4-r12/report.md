# BT4 account04/B06 — dual boundary collars for the exact-six zero-R-exit branch

Run: `20260922T021002Z-b06-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SIX-DUAL-COLLAR-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and hence digons are allowed in the source problem.

Fresh source verification in this invocation agrees with the campaign source record. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly says that the genuine Bermond--Thomassen conjecture remains unresolved for every `k>=4`; its theorem at the same `2k-1` threshold allows each packed cycle to be directed or to become directed after reversing one arc. No such relaxed cycle is counted here as a directed cycle. Lichiardopol--Por--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992, proves the exact lower-k inputs used in the inherited candidate: minimum outdegree five forces three vertex-disjoint directed cycles, and outdegree at least three except for at most two vertices of outdegree two forces two vertex-disjoint directed cycles.

## Exact inherited mathematics consumed

Latest complete campaign lead consumed:

- account02/B04 `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`;
- its four-remainder trident addendum blob `22e0b70fe2cfa33cc7a380eb9097329113d6b522`;
- its trident-escape closure blob `45500a8c943831271fc031cf79bafeb5e7faed51`.

The lead state gives an oriented exact-outdegree-seven minimum counterexample `D`, a globally minimum-total packing `(A,B,C)` of three directed cycles, nonempty acyclic remainder `R`, chordless packed cycles, domination of every arc, and 3-vertex-strongness. Equality in the repaired path-fan bound gives a size-neutral minimum packing. The lead's no-six neutral dynamics is not assumed closed; its six-fan and cross-linkage branches remain explicit obligations.

Named OTHER-account partner actually applied:

- account01/B04 `20260922T014146Z-b04-bt4-r12`, candidate `BT4-MCR-v4-six-companion-ladder`, report blob `c97354c5427b8b8093795bdd2eea15aa03adecaf`.

For a cycle-supported exact-six witness `z in B` with six outgoing arcs into `A union C` and no outgoing arc to `R`, write `H=D-(A union C)=D[B union R]`. The partner proves that either

- `(H5)` another vertex of `H-{z}` has at least five outneighbors in `A union C`, or
- `(C4)` at least four vertices of `H-{z}` have exactly four outneighbors in `A union C`, at least three point to `z`, and at least two of those `z`-dominators lie in `R`.

For each remainder dominator `u->z`, repeated arc domination gives a support-entry ladder

`L_u: s -> ... -> u -> z`

whose internal pre-`z` vertices lie in `R`, every ladder vertex also points directly to `z`, and whose packed apex satisfies `s in A union C union {z^-}`.

I also use account03/B05 `BT4-TCEX-v2-segment`, blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`, only in its proved scope. If a packed support segment `S=B[u,v]` containing a witness `u` heavy on another packed cycle is bypassed by an `R`-internal path from `u^-` to `v^+`, and a vertex of the heavy target sends an arc to `u`, then the bypass length obeys the sharp segment tax `ell >= m+|S|-1`; equality gives an explicit size-neutral two-cycle exchange with acyclic exchanged remainder.

No peer outcome label is used as a theorem.

## Compact conditional end-to-end route

The latest lead route reduces a hypothetical counterexample to the exact-seven normal form and then splits by pair-deletion deficits. The no-six side is now controlled by `(3,2,2)` sink geometry, neutral pivots, regenerated five-witnesses, and the four-remainder three-sink escape theorem. The six side still contains the corrected cycle-supported `6-cross/0-R-exit` obstruction.

The named partner attacks exactly that six obstruction. In its difficult `(C4)` alternative, two distinct remainder companions route *into* the six-witness `z`, but the remaining gap is coalescence/disjointness of those incoming ladders. This run attacks the opposite side of the same support edge. It proves that the predecessor `p=z^-` necessarily has at least two exits into `R`, and 3-vertex-strongness converts each such exit into a boundary ray back to the packing while avoiding both `p` and `z`. Thus the difficult six-witness has a genuine two-sided `R` interface: at least two incoming companion channels toward `z` and at least two outgoing predecessor channels from `p`.

## Lemma 1 — the predecessor of an isolated exact-six witness has two distinct R exits

Assume the exact-six / zero-R-exit setup above and assume alternative `(H5)` fails. Put `p=z^-`, the predecessor of `z` on the chordless packed cycle `B`.

Then

`|N^+(p) intersect R| >= 2`.                                      (1)

### Proof

Failure of `(H5)` gives

`|N^+(p) intersect (A union C)| <= 4`.

Because `B` is chordless and the counterexample is oriented, the only outgoing neighbor of `p` on `B` is its support successor `z`. Every vertex has outdegree exactly seven. Therefore

`|N^+(p) intersect R| = 7 - 1 - |N^+(p) intersect (A union C)| >= 2`.

The heads are distinct because there is at most one arc per ordered pair. QED.

This is dual to the partner's two remainder vertices that feed `z`: the support edge `p->z` is flanked by a two-in / two-out remainder interface whenever the isolated `(C4)` branch is active.

## Lemma 2 — every predecessor R exit reaches a packed boundary without using p or z

Let `r in N^+(p) intersect R`. Fix any vertex `a in A`. Because `D` is 3-vertex-strong, `D-{p,z}` is strongly connected. Hence there is a directed path from `r` to `a` in `D-{p,z}`.

Truncate such a path at its first vertex `t` in `A union B union C`. Then

`P_r: p -> r -> ... -> t`                                      (2)

is a directed path whose internal vertices all lie in `R`, and

`t in (A union B union C) \ {p,z}`.                              (3)

Consequently each predecessor exit produces one of two source-valid objects.

### Cross-boundary outcome

If `t in A union C`, then `P_r` is a genuine directed transition from support cycle `B` to another packed cycle, with every internal vertex in the old acyclic remainder.

### B-return outcome

If `t in B`, let `ell` be the number of edges of `P_r` and let

`d=d_B(p,t)`

be the forward directed distance from `p` to `t` on `B`. Since `t` is neither `p` nor the immediate successor `z`,

`2 <= d <= |B|-1`.                                               (4)

The path `P_r` followed by the directed complementary segment `B[t,p]` is a directed cycle disjoint from `A` and `C`. Replacing `B` by that cycle would change the total size of the three-packing by `ell-d`. Global minimum therefore forces

`ell >= d`.                                                       (5)

If equality holds, this is a size-neutral one-cycle exchange and its new remainder is acyclic, since any cycle in the new remainder together with the new three-packing would be a forbidden four-pack. If inequality is strict, the ray is a quantitatively long `R`-collar around the proper forward segment `B[p,t]`, a segment which necessarily contains the exact-six witness `z`.

### Proof

Only the B-return accounting requires comment. The replacement cycle has order `|B|+ell-d`: the path from `p` to `t` contributes `ell` edges instead of the `d` forward support edges. If `ell<d`, keeping `A,C` and using this replacement gives a strictly smaller three-cycle packing, contradicting global minimality. Equality gives another global minimum. QED.

Applying Lemma 2 to two distinct vertices in the set guaranteed by Lemma 1 gives two predecessor-origin boundary rays with distinct first `R` vertices. They may later coalesce; no unjustified disjointness is claimed.

## Corollary 3 — a heavy external apex upgrades every B-return ray to the marked-segment collar

Suppose one of the partner's companion ladders has packed apex `s` on a cycle `X in {A,C}` for which

`m=|N^+(z) intersect X| >= 3`.

The ladder construction gives the direct arc `s->z`.

Let `P_r` be a B-return ray from Lemma 2, ending at `t in B`, with length `ell` and forward distance `d=d_B(p,t)`. Put

`S=B[z,t^-]`.

Then `|S|=d-1`, `z in S`, and `P_r` is exactly an `R`-internal bypass from `z^-=p` to `(t^-)^+=t`. Applying the account03/B05 segment-bypass inequality with witness `u=z`, target cycle `X`, and entry `s->z` gives

`ell >= m+(d-1)-1 = m+d-2`.                                     (6)

Since `m>=3`,

`ell >= d+1`.                                                     (7)

Thus in this subcase a B-return ray can never be merely a same-size one-cycle replacement. It pays at least one extra edge beyond the skipped support segment. Equality in the sharper bound (6), when it occurs, is the partner's explicit size-neutral **two-cycle** exchange and carries its acyclic exchanged-remainder constraints.

In the `(3,3)` fan split, every apex in `A union C` is automatically on a heavy target. Hence unless both chosen companion ladders have apex `p`, every B-return ray is subject to the stronger collar (6).

## Lemma 4 — incoming/outgoing coalescence can be switched into a clean support path

Let

`L: s -> ... -> u -> z`

be one of the partner's support-entry ladders, with all vertices between the packed apex `s` and `z` lying in `R`, and let

`P: p -> r -> ... -> t`

be one of the predecessor boundary rays from Lemma 2, with all vertices between packed endpoints `p,t` lying in `R`.

Suppose there are vertices `q` on the `R` part of `L` and `w` on the `R` part of `P` joined by a directed path

`T: q -> ... -> w`

entirely in `R` (the case `q=w` is allowed). Then there is a directed walk from `s` to `t` whose internal vertices all lie in `R`: take the prefix of `L` from `s` to `q`, then `T`, then the suffix of `P` from `w` to `t`. Removing repeated directed portions gives a directed path with the same packed endpoints unless the endpoints coincide, in which case one obtains a directed closed walk based at that support vertex.

Therefore:

1. if `s` and `t` lie on different packed cycles, a genuine cross-packed transition with `R`-internal interior is forced;
2. if `s` and `t` are distinct vertices of the same packed cycle, an `R`-internal support bypass is forced and global minimum supplies its usual segment-length tax, with the stronger account03/B05 tax whenever the marked-heavy hypotheses are met;
3. if `s=t`, the closed walk contains a directed cycle through `s` (a cycle wholly inside `R` is impossible), giving a same-support replacement object subject to global minimum.

Thus an intersection or forward `R`-reachability from an incoming companion ladder to an outgoing predecessor ray is not an unstructured coalescence failure. It switches to the already-live cross/bypass exchange interfaces.

### Proof

Every nonendpoint vertex of the ladder prefix, the bridge `T`, and the ray suffix lies in `R` by construction. Their concatenation is directed. Standard removal of a repeated directed subwalk yields a simple directed path unless the packed endpoints are the same. In the coincident-endpoint case, any simple directed cycle extracted from the closed walk cannot be wholly contained in `R`, because `D[R]` is acyclic, so it uses the packed endpoint. QED.

## Corollary 5 — exact residual wall in the partner's C4 branch

Assume the partner's difficult `(C4)` alternative and choose two distinct remainder companions `u_1,u_2->z`, with support-entry ladders `L_1,L_2`, and two distinct predecessor exits `r_1,r_2` from Lemma 1, with boundary rays `P_1,P_2` from Lemma 2.

Then at least one of the following occurs:

1. one of the two `P_j` is already a B-to-`A/C` cross transition;
2. a B-return `P_j` is subject to the heavy marked-segment collar/exchange of Corollary 3;
3. for some `i,j`, an `R` vertex of `L_i` reaches an `R` vertex of `P_j`, and Lemma 4 produces a clean support-to-support cross transition or bypass;
4. **dual reachability wall:** for all four pairs `(i,j)`, no vertex on the `R` portion of `L_i` reaches any vertex on the `R` portion of `P_j`, and every outgoing ray not covered by (1) is a globally-minimum-constrained B-return collar.

Alternative 4 is a real structural separation in the acyclic remainder, not a renamed demand for disjointness. The old isolated `6-cross/0-R-exit` obstruction has therefore been reduced to high-witness multiplicity `(H5)`, an actionable cross/exchange/collar, or a `2 x 2` one-way reachability wall between two incoming and two outgoing remainder interfaces around the adjacent support pair `p->z`.

## Why this is new relative to the named partner

The partner already proved that an isolated exact-six witness forces **incoming** remainder companions and support-entry ladders. Its exact first unpaid implication was that those ladders can coalesce before yielding two compatible crossings.

The present argument uses the same no-second-high-witness hypothesis a second time at the predecessor `p=z^-`. Exact outdegree seven plus chordlessness forces two **outgoing** remainder exits. The lead's 3-vertex-strongness then pushes each exit back to a packed boundary while avoiding `p,z`. This produces a dual boundary interface. Coalescence between an incoming ladder and an outgoing ray can be switched at the first reachable contact into a clean support-to-support path; if no such switch is possible, the remainder satisfies four explicit reachability exclusions. This is strictly narrower than the previous generic common-apex/coalescence obstruction.

No claim is made that the dual wall itself is impossible.

## Updated conditional full BT4 route

Combining the exact lead and partner states gives the following honest conditional proof skeleton.

1. Reduce a hypothetical BT4 counterexample to the exact-seven, oriented, arc-dominated, 3-vertex-strong normal form with a globally minimum three-cycle packing and acyclic remainder.
2. Apply universal pair deletion. In global no-six, every sink has `(3,2,2)` fan geometry; equality pivots and regenerated five-witnesses drive the dynamic exchange system. The lead has excluded the `|R|=3,s=3` core and proved that the `|R|=4,s=3` distinct-heavy core must escape to a six branch or to at most two sinks.
3. In a cycle-supported exact-six / zero-R-exit state, apply account01/B04. A second five-or-more witness gives `(H5)`; otherwise two remainder companions and their incoming ladders exist.
4. In that `(C4)` state, apply Lemmas 1--4 above. The exact-six support edge now has two incoming companion channels and two outgoing predecessor channels. Any forward contact converts to a source-valid cross/bypass object; heavy-apex B-returns obey the marked segment tax. Only the dual reachability wall remains as the isolated companion-coalescence obstruction.
5. Close the remaining six high-witness / dual-wall states, the no-six `s<=2` and short-light states, and the pairwise-only linkage/port-collision state. Each equality move must keep using the already-proved regenerated deficit system and acyclic exchanged remainder.

Steps 1--4 are source-bound deductions in the current candidate. Step 5 is **not proved**. Therefore this is not a target-level proof of BT4.

## First essential missing implication after this run

The next exact six-branch statement is now:

> **Dual-wall closure.** In the `(C4)` exact-six state above, assume no outgoing predecessor ray is a usable cross transition, no heavy-apex marked collar yields the strict/equality exchange needed by the existing two-cycle machinery, and no `R`-directed path runs from either incoming ladder interior to either outgoing-ray interior. Use the four resulting reachability exclusions, the two distinct companion vertices `u_1,u_2->z`, the two distinct predecessor exits `p->r_1,p->r_2`, and regenerated pair-deletion deficits to force either a second high-cross witness, two compatible opposite crossings, a strict packing reduction, or a directed cycle in an exchanged remainder.

This is materially narrower than “resolve companion coalescence”: the local support edge is now known to have a two-in/two-out remainder interface, and every forbidden incoming-to-outgoing contact is a certified DAG reachability separation.

The no-six short-light and pairwise-only linkage-collision branches remain separate team obligations and are not silently absorbed into this statement.

## Adversarial checks and nonclaims

- Lemma 1 uses failure of `(H5)` at `p=z^-`; without that hypothesis the two-R-exit conclusion is not asserted.
- Chordlessness is used only to say that `p` has exactly one outneighbor on `B`, namely `z`.
- 3-vertex-strongness is used exactly in `D-{p,z}`; the path is then truncated at its first packed vertex, so its internal vertices are genuinely in `R`.
- The two predecessor rays have distinct first remainder vertices but are **not** claimed internally disjoint after that point.
- Lemma 4 requires directed reachability from the incoming ladder toward the outgoing ray. The opposite reachability direction is not silently reversed.
- Corollary 3 invokes the account03/B05 marked-segment inequality only when the ladder apex lies on a target cycle on which `z` has fan at least three, providing the required direct entry arc into the marked witness.
- A cross transition is not counted as two cycles. It is an input to the still-unpaid disjointness-preserving splice machinery.
- No finite-order computation, average-degree substitute, edge-disjoint surrogate, near-directed cycle, or literature search miss is used as target-level evidence.
- Full BT4 remains OPEN / NOT PROVED by this candidate.

## Outcome

`ESSENTIAL_STEP_APPLIED`.

New reusable result: in the named partner's isolated exact-six / zero-R-exit `(C4)` state, the predecessor of the six-witness necessarily has two distinct remainder exits, and 3-vertex-strongness turns each into a packed-boundary ray avoiding the witness edge endpoints. Combined with the partner's two incoming companion ladders, this gives a two-in/two-out dual interface. Any forward `R` contact between the two sides switches to a clean support path; otherwise the hard state satisfies an explicit `2 x 2` reachability wall. This advances the six-fan branch but does not close BT4.
