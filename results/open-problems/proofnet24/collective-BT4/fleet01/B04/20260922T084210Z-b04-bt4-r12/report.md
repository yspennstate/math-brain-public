# BT4 fleet01/B04 — one-cut collapse forces a direct heavy escape from the second collar

Run: `20260922T084210Z-b04-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-F3-SECOND-COLLAR-HEAVY-ESCAPE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact target and live scope

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement, hence directed digons count before the inherited minimal-counterexample reduction.

The current literature boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine conjecture is stated there as unresolved for every `k>=4`; their theorem permits one reversed arc per packed cycle and is not counted here. The genuine `k=3` input is Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992: minimum outdegree five forces three vertex-disjoint directed cycles.

Fresh control remained on owner revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, with fleet01/B04 assigned to minimal-counterexample reduction / exact deletion-contraction losses for BT4. Older installation/benchmark work is superseded. No authenticated brain retrieval or receiver-context use occurred.

## 2. Exact inherited mathematics consumed

### Campaign lead fleet02/B04

Latest complete lead report consumed:

`proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`.

The inherited normal form is a hypothetical oriented exact-outdegree-seven BT4 counterexample `D`, arc-dominated and 3-vertex-strong, with a three-cycle packing chosen lexicographically: first minimum total packed order, then maximum number of arcs induced by the acyclic remainder. Packed cycles are chordless. The lead corrected an earlier invalid use of a two-packed-port theorem on a four-port mixed cycle and proved instead that the clean four-port state emits a genuine packed-to-packed CROSS or a distinct-port same-support BYPASS. Coalesced-port splice, SIX, residual bounded F2/F3 states and the larger-remainder branch remain explicit debts.

### Named assigned partner fleet02/B05

This run directly consumes and strengthens the completed partner result

`BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1`, canonical report
`proofnet24/collective-BT4/fleet02/B05/20260922T082550Z-b05-bt4-90f85d42/report.md`, scientific commit `480a98e5aff0771c4ca9e558cbb657beea1a3d2e`, and shared handoff commit `e5eae08407ed309bb1ce6126c31d24140af6d988`.

The exact partner state is the four-remainder F3 both-repeat, two-indirect, second-predecessor collar. Write

`S* = p -> x -> s -> p`,

let `U` be the other light packed cycle, let the old current remainder be

`R*={q,a,b,c}`,

and let the short return be

`W = u -> a -> p -> b -> u`.

Fleet03/B06 `BT4-R4-F3-APEX-COLLAR-v1` (report blob `102e3a54d5cac3a14afd00122e3d485d99a1b632`) proves that in the second-predecessor case the three-hit apex is

`z=u^{--}`

and the whole-support neutral replacement

`C_z = z -> b -> u -> U[u,z] -> z`

has exactly `|U|` vertices. Its exchanged remainder is exactly

`{q,a,c,t}`, where `t:=u^-`,

and must be acyclic in a genuine counterexample.

The assigned partner then proves, from exact outdegree seven, chordlessness of `U`, and `|R*|=4`, that

`|N+(t) intersect (H union S*)| >= 2`.

Hence either:

- **clean-light:** `t->y` for some `y in S*\{p}`; together with `p->b->u` this is an opposite light-cross pair with four distinct packed ports; or
- **heavy:** `t->h` for some `h in H`.

The partner's exact 18-vertex certificate refutes the stronger shortcut that the clean-light target is always present, so the heavy alternative is genuinely necessary.

### Essential one-cut dependency from fleet04/B04

`BT4-R4-F3-RETURN-CUT-v1`, report blob `425b7f0491ef4caf794ce862783c811edd26b110`, proves in exactly this two-indirect F3-BOTH state that

`D[(U-{u}) union {s}]`

is acyclic. Writing the broken support path

`v1=u+ -> v2 -> ... -> vm=u-`,

with

`IN={j: vj->s}`, `OUT={i: s->vi}`,

one has the exact one-cut order

`i>j` for every `i in OUT`, `j in IN`.

The canonical F3 arc-max reduction `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1` (report blob `2f802a03755394931009175d7b6a5f94b0b2b084`) also proves that `u` is the unique vertex of `U` that can send directly to `x` in this state.

## 3. Compact conditional end-to-end route

Assume BT4 false and enter the inherited oriented exact-seven, arc-dominated, 3-vertex-strong normal form. Choose a lexicographically extremal three-cycle packing. Run the established SIX/global-NO-SIX and four-remainder F2/F3 reductions. In the F3 both-repeat second-predecessor collar, apply the assigned partner theorem above.

The previous local route split into a clean opposite light pair or a fresh light-to-heavy cross. The theorem below shows this split is not genuinely two different interface types: **the clean branch itself forces a direct `S*->H` heavy escape.** Thus every second-predecessor collar carries a zero-remainder heavy entry, either directly from `t` or after the single packed intermediate vertex `s`.

Consequently this entire second-predecessor collar can be handed to one narrower heavy/light tripod splice problem, while retaining the neutral exchanged-remainder acyclicity and the return `p->b->u`. Full BT4 remains conditional on closure of that splice plus the separate SIX, other F2/F3, coalesced-port and larger-remainder branches.

## 4. New theorem — `BT4-R4-F3-SECOND-COLLAR-HEAVY-ESCAPE-v1`

In the exact second-predecessor state above, put `t=u^-`. Then at least one of the following holds:

1. there is a direct arc `t->h` with `h in H`; or
2. there is a direct arc `t->s`, and `s` has a direct outneighbor in `H`.

More precisely, in alternative 2,

`N+(s) intersect (U-{u}) = empty`

and

`|N+(s) intersect H| >= 2 - 1_{s->u}`.

In particular `|N+(s) intersect H|>=1`.

Thus every second-predecessor collar contains a genuinely directed packed-support chain of one of the forms

`t -> H`

or

`t -> s -> H`,

with no remainder vertex in the new heavy-entry chain. In the second form the inherited opposite light return `p->b->u` is simultaneously present.

### Proof

Start from the assigned partner dichotomy.

If the heavy alternative occurs, there is already an arc `t->h` for some `h in H`; this is conclusion 1.

Assume instead the clean-light alternative. The target lies in

`S*\{p}={x,s}`.

But `u` is the unique `U`-vertex with an arc to `x` in the canonical F3 state. Since `t=u^- != u`, one has

`t not-> x`.

Therefore the clean target is forced to be

`t -> s`.                                                       (1)

Now `t=u^-=v_m` is the terminal vertex of the broken support path `U-u`. Equation (1) says `m in IN` in the one-cut notation. The one-cut theorem requires every `i in OUT` to satisfy `i>j` for every `j in IN`; in particular `i>m`. No such index exists. Hence

`OUT=empty`,

which is exactly

`N+(s) intersect (U-{u})=empty`.                               (2)

The packed source cycle is the directed triangle

`S*=p->x->s->p`.

The inherited normal form is oriented. Hence among vertices of `S*`, the only outneighbor available to `s` is its support successor `p`; in particular `s not->x`. The current remainder `R*` contains exactly four vertices. By (2), among `U` vertices the only possible outneighbor of `s` is `u`. Therefore all outneighbors of `s` outside `H` lie in the disjoint sets

`{p}`, `R*`, `{u}`,

and hence number at most

`1 + 4 + 1_{s->u}`.

Since the normal form has exact outdegree seven,

`|N+(s) intersect H| >= 7-(5+1_{s->u}) = 2-1_{s->u}`.          (3)

This is at least one, proving conclusion 2 and the quantitative strengthening. QED.

## 5. Why this is an essential rather than cosmetic reduction

The assigned partner's `BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1` left two qualitatively different splice outputs: a clean opposite light pair or a light-to-heavy cross. The theorem above proves that the first output automatically creates a heavy interface as well. Therefore the second-predecessor collar has a common canonical payload:

- the neutral collar exchange `C_z` and acyclic exchanged remainder `{q,a,c,t}`;
- the opposite light return `p->b->u`;
- a zero-remainder heavy entry of length at most two from the `U` side, namely `t->H` or `t->s->H`.

The clean branch is especially rigid: `t->s` is the **last possible** `U->s` port, so the one-cut condition kills every `s->(U-{u})` arc. Exact outdegree seven then forces the heavy exit rather than merely suggesting one by averaging.

This pays for an actual line of the conditional proof: the second-predecessor F3 collar no longer needs a separate generic clean-light splice theorem. It feeds the already-live heavy-entry/CROSS machinery with a direct, source-valid heavy arc.

## 6. Exact deletion and contraction accounting at the new interface

For any directed cycle `C` and any outside vertex `v`, define

`a_C(v)=|N+(v) intersect C|`.

In the exact-seven normal form,

`d^+_{D-C}(v)=7-a_C(v)`,                                      (4)

while after contracting `C` to one vertex and coalescing parallel quotient arcs,

`d^+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`.                         (5)

Thus deletion loses every hit on `C`, whereas contraction refunds only one regardless of how many distinct vertices of `C` were hit. The contracted cycle vertex itself has outdegree equal to the number of distinct external head classes of `C`, which can be below seven. This is the precise global obstruction to a naive degree-seven induction by contraction.

The clean branch gives a useful local exception. From (2),

`a_U(s)<=1`.

Therefore deleting `U` leaves

`d^+_{D-U}(s)>=6`,

and contracting `U` preserves the full degree of `s`:

`d^+_{D/U}(s)=7`.

This is only a **local** degree-preservation statement at `s`; it does not make contraction globally safe, because other outside vertices may hit `U` several times and the quotient vertex for `U` may itself have fewer than seven distinct external heads.

## 7. First unpaid implication after this run

`BT4-R4-F3-HEAVY-LIGHT-TRIPOD-SPLICE-v1`:

> In the canonical four-remainder F3 second-predecessor state, assume the neutral collar exchange `C_z`, acyclic exchanged remainder `{q,a,c,t}`, and the inherited opposite return `p->b->u`. In addition assume the heavy-entry conclusion proved here: either `t->h` with `h in H`, or `t->s->h` with `h in H` and no `s->(U-{u})` arc. Prove that this configuration yields two vertex-disjoint replacement directed cycles, a strictly smaller three-packing, a directed cycle in an exchanged remainder, SIX, or a fourth directed cycle.

This is narrower than the assigned partner's `BT4-R4-F3-FRESH-PORT-SPLICE-v1`: the clean-light branch has already been converted into a direct heavy-entry interface, and the one-cut orientation at `s` is fixed.

Separate debts remain: global SIX closure; F2; immediate-predecessor and other F3 states; lead coalesced-port CROSS/BYPASS selection; and the larger-remainder support-carried/pinwheel branch. None is silently promoted.

## 8. Failure checks and nonclaims

- The theorem uses the exact canonical four-remainder F3 hypotheses. It is not asserted for arbitrary light-cross configurations or larger remainders.
- The inference `t not->x` uses the inherited uniqueness of the `U`-inport to `x`; without that hypothesis the clean target need not be `s`.
- The one-cut inequality is used only after the source-valid return-cut theorem has established acyclicity of `(U-{u}) union {s}`.
- A direct heavy arc or a two-step support chain is not itself a fourth directed cycle and is not counted as two replacement cycles.
- The local contraction identity at `s` does not prove the quotient has minimum outdegree seven.
- No finite computation or search is promoted to a universal proof in this report.
- The partner's exact certificate remains a sharpness example for its own stronger false shortcut; it is not a BT4 counterexample.

## 9. Honest status and provenance

Outcome: `ESSENTIAL_STEP_APPLIED`.

The new universal step is `BT4-R4-F3-SECOND-COLLAR-HEAVY-ESCAPE-v1`: the assigned partner's clean-light alternative necessarily targets `s`, the inherited one-cut then annihilates every return arc from `s` to `U-{u}`, and exact outdegree seven forces a direct heavy outneighbor of `s`. Hence both partner alternatives feed a common heavy-entry splice frontier. BT4 remains `OPEN_NOT_PROVED`.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and provider-thinking-time counters: `NOT_EXPOSED`. No scheduler mutation, email, Drive, public posting, paid API/model/Codex, remote workflow or permission change was used.
