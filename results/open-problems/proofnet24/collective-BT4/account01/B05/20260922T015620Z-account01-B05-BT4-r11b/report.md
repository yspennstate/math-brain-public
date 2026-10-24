# BT4 account01/B05 — orthogonal linkage–pivot augmentation and triangle phase locking

Run: `20260922T015620Z-account01-B05-BT4-r11b`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-OLPA-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement, and a directed digon counts as a cycle.

The current source check remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the exact Bermond--Thomassen conjecture remains unresolved for every `k>=4`; its same-threshold theorem permits a cycle that becomes directed after one arc reversal. No such relaxed cycle is promoted here.

## Exact peer mathematics consumed

I use the campaign lead's newest complete package:

- account02/B04, `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

Its surviving normal form is an oriented exact-outdegree-seven counterexample with a globally minimum-total three-cycle packing `(A,B,C)`, nonempty acyclic remainder `R`, chordless packed cycles, arc domination, and 3-vertex-strongness. Pair-deletion deficits regenerate after every neutral exchange. In the global no-six branch every remainder sink has fan type `(3,2,2)`, and the lead's neutral light-pivot lemma is valid.

I consume the named assigned partner result:

- account02/B06, `b06-20260922T005655Z-24f482784ae2`, report blob `749c5848dc20e2023bcb8312e8b90d8f8746742f`.

That report gives a source-valid exact-seven adversary to the false shortcut that three cycle-supported five-witnesses automatically yield two distinct remainder exit heads. It proves instead the collar-or-bottleneck repair and isolates total exit-head coalescence as a genuine hard branch. I therefore do not use automatic exit separation anywhere below.

I also apply two completed OTHER-account results:

- account04/B06, `BT4-SINKLINK-v1`, report blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`. For a no-six sink `x` with heavy cycle `A` and light cycles `B,C`, either one light cycle has size at most `|R|`, or there is a genuinely directed cycle `Q_x` meeting `B,C` in exactly one vertex each and otherwise lying in `R\{x}`. Writing these packed vertices `b in B,c in C`, the two `b`--`c` arcs of `Q_x` are internally vertex-disjoint directed paths through `R`, and every internal remainder vertex of `Q_x` sends an arc to `x`.
- account03/B05, `BT4-TCEX-v2-segment`, report blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`. Its support-correct marked-segment exchange gives `ell>=m+s-1` for an `R`-internal bypass of a proper support-cycle segment of size `s` around a witness with fan `m`, with exact neutral exchange and remainder accounting at equality.

No peer outcome label is used as proof; only the stated lemmas in their proved hypotheses are used.

## Compact conditional end-to-end route

Assume BT4 false and pass to the exact-seven minimum-counterexample normal form above. Pair-deletion amplification leaves a six-fan branch or a persistent no-six branch. The six-fan branch remains separate. In the no-six branch every sink has one heavy and two light packed cycles. Neutral support/pivot and segment-exchange machinery handles short bypasses; account04/B06 supplies an actual two-way linkage between the two light cycles unless a light cycle is short.

The hard three-sink core is therefore the configuration in which there are distinct sinks

`x_A, x_B, x_C in R`,

heavy respectively on `A,B,C`, and each sink is in the linkage alternative rather than the short-light alternative. The current global gap is compatibility: the three linkage cycles may overlap in `R`, and asking for two vertex-disjoint collars is false by the named partner's adversary.

The mechanism below is materially different from my prior single-witness collar argument. It uses only **one** linkage cycle and combines it with **two orthogonal neutral light pivots**, so no disjointness between different linkage interiors is required.

## Setup: return ports and neutral light pivots

For sink `x_A`, account04/B06's linkage alternative gives unique light-return ports

`b_A in B`, `c_A in C`, with `b_A->x_A`, `c_A->x_A`,

and a directed linkage cycle

`Q_A = P_BC union P_CB`

whose only packed vertices are `b_A,c_A` and whose remaining vertices lie in `R\{x_A}`. Every internal remainder vertex of `Q_A` sends an arc to `x_A`.

Likewise the linkage alternatives at `x_B,x_C` give ports

`a_B in A, c_B in C`, and `a_C in A, b_C in B`,

respectively.

Because `x_C` is light on `B`, the lead's light-pivot lemma gives

`N+(x_C) intersect B = {b_C^+, b_C^(+2)}`.

Hence

`B_C := b_C -> x_C -> b_C^(+2) -> B[b_C^(+2),b_C]`

is a genuine directed cycle with vertex set

`V(B_C) = (V(B) \ {b_C^+}) union {x_C}`.                 (1)

Similarly, because `x_B` is light on `C`,

`C_B := c_B -> x_B -> c_B^(+2) -> C[c_B^(+2),c_B]`

is a genuine directed cycle with

`V(C_B) = (V(C) \ {c_B^+}) union {x_B}`.                 (2)

These are size-neutral replacements, but below they are used directly as two members of a four-cycle packing.

## Lemma 1 — orthogonal linkage–pivot augmentation

Under the setup above, if

`b_A = b_C^+`                                                (3)

and

`c_A = c_B^+`,                                               (4)

then `D` contains four pairwise vertex-disjoint genuinely directed cycles.

### Proof

Take the four cycles

1. the untouched packed cycle `A`;
2. the linkage cycle `Q_A`;
3. the neutral light pivot `B_C`;
4. the neutral light pivot `C_B`.

We account for every possible overlap.

- `A` is disjoint from `Q_A`, because `Q_A` uses only `b_A in B`, `c_A in C`, and vertices of `R`; it is disjoint from `B_C,C_B`, whose packed support is in `B,C` and whose only remainder vertices are `x_C,x_B`.
- By (1) and (3), `B_C` omits exactly the unique `B`-vertex used by `Q_A`, namely `b_A`.
- By (2) and (4), `C_B` omits exactly the unique `C`-vertex used by `Q_A`, namely `c_A`.
- `B_C` and `C_B` are disjoint from each other because they use different original packed cycles and distinct sinks `x_C,x_B`.
- It remains only to check that `Q_A` does not contain `x_B` or `x_C`. Every internal remainder vertex of `Q_A` sends an arc to the remainder sink `x_A`. But `x_B` and `x_C` are themselves sinks of `D[R]`, so neither has any outarc to another remainder vertex, in particular neither sends an arc to `x_A`. Therefore neither can be an internal vertex of `Q_A`. They are not the packed endpoints `b_A,c_A` either.

Thus all four displayed cycles are vertex-disjoint and genuinely directed in the original digraph, contradicting the assumed BT4 counterexample. QED.

The proof uses no edge-disjoint surrogate and no compatibility assumption on the other two linkage cycles. Only one linkage cycle is needed.

## Corollary 2 — three cyclic alignment obstructions

The same construction cyclically gives three immediate four-pack certificates.

- `Q_A` closes BT4 if `b_A=b_C^+` and `c_A=c_B^+`.
- `Q_B` closes BT4 if `a_B=a_C^+` and `c_B=c_A^+`.
- `Q_C` closes BT4 if `a_C=a_B^+` and `b_C=b_A^+`.

Therefore any genuine no-four-pack three-sink linkage core must violate at least one equality in each of these three pairs.

This converts the vague “make two linkages compatible” obligation into an exact finite port-alignment obstruction on the packed cycles.

## Corollary 3 — triangle phase locking

Assume further that `A,B,C` are all directed triangles and that, on each packed cycle, its two light-return ports are distinct:

`a_B != a_C`, `b_A != b_C`, `c_A != c_B`.                 (5)

For two distinct vertices of a directed triangle, exactly one is the successor of the other. Define three bits by

- `alpha=1` if `a_B=a_C^+`, and `alpha=0` if `a_C=a_B^+`;
- `beta=1` if `b_C=b_A^+`, and `beta=0` if `b_A=b_C^+`;
- `gamma=1` if `c_A=c_B^+`, and `gamma=0` if `c_B=c_A^+`.

If no immediate four-pack from Corollary 2 exists, then

`(alpha,beta,gamma) is either (0,0,0) or (1,1,1)`.          (6)

### Proof

Avoiding the `Q_A` augmentation forbids `(beta,gamma)=(0,1)`, hence

`gamma=1 => beta=1`.                                       (7)

Avoiding the `Q_B` augmentation forbids `(alpha,gamma)=(1,0)`, hence

`alpha=1 => gamma=1`.                                      (8)

Avoiding the `Q_C` augmentation forbids `(alpha,beta)=(0,1)`, hence

`beta=1 => alpha=1`.                                       (9)

If any one of the three bits is `1`, (7)--(9) cycle around and force all three to be `1`. If none is `1`, all three are `0`. This proves (6). QED.

Thus, in the triangle/distinct-port subcase, the no-four-pack hypothesis forces a **global phase lock**: the three independent-looking light-return pairs cannot have arbitrary local cyclic order. Only the two globally coherent orientations survive.

This is a structural restriction, not yet a contradiction. Port-collision cases excluded by (5) also remain open.

## Relation to the named partner's coalesced-exit adversary

The named account02/B06 adversary shows why the proof cannot simply ask for separated exit heads or separated remainder collars. Lemma 1 avoids that false implication entirely: once a sink-linkage cycle exists, the other two sinks themselves provide the two replacement cycles. Their only remainder vertices are those sinks, and the sink property automatically keeps them out of the chosen linkage interior.

The partner's total-coalescence branch remains relevant before one reaches the three-sink linkage skeleton, and the segment-exchange inequalities remain needed when account04/B06 returns the short-light alternative or when a support witness is treated locally. Nothing here invalidates those branches.

## Exact first remaining implication

For the no-six three-sink linkage core, the next indispensable step is now the following finite structural statement:

> **Port-alignment closure problem.** Prove that the six light-return ports force at least one of the three alignment pairs in Corollary 2, or else use the simultaneous failure of all three pairs to produce a strict marked-segment exchange, a fourth directed cycle, or a reduction to the already isolated short-light / six-fan branch.

For directed triangles with distinct return ports, Corollary 3 reduces this further: only the two coherent phase patterns `(0,0,0)` and `(1,1,1)` need be eliminated. The collision cases `a_B=a_C`, `b_A=b_C`, or `c_A=c_B` are separate exact residuals rather than being hidden inside a generic compatibility claim.

For longer packed cycles, the unpaid issue is geometric rather than an unstructured path-overlap problem: determine the relative cyclic positions of the two return ports on each cycle strongly enough to make one linkage endpoint equal the vertex omitted by the orthogonal light pivot.

## Failure checks and boundaries

- The linkage alternative is an explicit hypothesis. If a sink is in the short-light alternative, this report does not claim the augmentation applies.
- All three sinks are assumed distinct, exactly as in the three-sink hard core.
- The neutral pivot formulas use fan size two on a light cycle and the actual return arc; no minimum-degree average is substituted.
- The proof that `Q_A` avoids the other sinks uses the fact that every internal vertex of `Q_A` lies in `N^-(x_A)` and that `x_B,x_C` are sinks of the same DAG remainder.
- The linkage cycle may have arbitrary length and arbitrary internal overlap with the *other* linkage cycles; those other cycles are not used in Lemma 1.
- The triangle phase-lock conclusion assumes distinct return ports on every packed triangle. It is not asserted in a collision case.
- The six-fan branch, total exit-head coalescence before the linkage core, and the short-light branch are not closed here.
- No finite-order computation is promoted to a target-level proof, and no novelty claim is made.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The new step is a direct four-cycle packing augmentation: a single light-cycle linkage plus the two orthogonal neutral pivots yields four disjoint directed cycles whenever two explicit successor alignments hold. In the triangle/distinct-port hard core, avoiding all three such augmentations forces a two-state global phase lock. Full BT4 remains open; the first remaining obligation is to eliminate the coherent phase/collision configurations or connect them to a strict segment exchange / existing closure branch.

Next recipients: campaign lead `account02/B04`, named assigned partner `account02/B06`, account04/B06 (sink-linkage), and account03/B05 (segment exchange).
