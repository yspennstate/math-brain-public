# BT4 account03/B04 — domination-ladder path upgrade and exact residual port collisions

Run: `b04-20260922t055204z-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-PORT-PATH-UPGRADE-v2`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Source-bound input actually consumed

Assigned partner result consumed this run:

- account04/B05 run `b05-20260922t051421z-r34`;
- candidate `BT4-HT-XFREE-HALL-v1`;
- source-bound handoff commit `face1d9aa603ac2a2a1f0bef6e3e8306999f8dbf`;
- canonical scientific report blob `e63f331533e20a4a1231458a6c5c43c7eb5c4bf1`;
- shared handoff blob `1ac9d889a7aba352f13e6d43b19c376a679d7a3c`.

The partner works in the exact four-remainder cage

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with exact induced structure from its Lemma 1. For each cycle-supported exact five-witness `h_i`, after choosing a heavy light target `A_i` and a target port `a_i` outside `N+(x) cap A_i`, its domination ladder produces an x-free cross transition whose R-interior is empty or `{r_{i-1}}`; the packed start is either `h_{i-1}` or a vertex of the opposite light cycle. For a same-heavy pair it proves the target-port Hall alternative: distinct ports, or the exact fan collision. Its fourth witness `r2` supplies either a genuine packed cross or a neutral equality return from a light cycle to `r2`, extendable via `r2->h0` to an x-free light-to-H return.

An earlier immutable draft in this run mistranscribed the domination-ladder path by inserting `h_i` into the cross transition. That draft is explicitly superseded by `CORRECTION-v1.md`; the corrected proof below follows the partner's actual domination construction.

## Lemma 1 — exact escape shapes

Fix `i` modulo three, a heavy target `A_i`, a chosen port `a_i`, and let `B_i` be the other light packed cycle. The partner's escape `P_i` can be taken in exactly one of the following four forms:

`h_{i-1}->a_i`,
`h_{i-1}->r_{i-1}->a_i`,
`b_i->a_i`,
`b_i->r_{i-1}->a_i`,

where `b_i in B_i`.

Thus every escape has one of two support signatures:

- **H-type:** its only vertex on `H` is the packed start `h_{i-1}`;
- **L-type:** it has no vertex on `H` and its packed start is one vertex `b_i` on the opposite light cycle `B_i`.

In both cases its R-interior is empty or `{r_{i-1}}` and its only vertex on the target light cycle `A_i` is the terminal port `a_i`.

### Proof

Dominate the fan arc `h_i->a_i`. Let `q0` satisfy `q0->h_i,a_i`. Since `a_i` is outside the sink fan, `q0!=x`; since the heavy target has no inport to `h_i`, `q0` does not lie on `A_i`.

If `q0` is packed, exactness of the cage leaves only the support predecessor `h_{i-1}` on `H` or a vertex `b_i` on the opposite light support `B_i`. The direct arc `q0->a_i` is then the desired cross transition.

If `q0=r_{i-1}`, then `r_{i-1}->a_i`. Dominate `r_{i-1}->h_i`. The partner proves that no remainder vertex can perform this second domination in the exact cage, so the next dominator `q1` is packed. Again it cannot lie on `A_i` because it points to `h_i`; hence it is `h_{i-1}` or a vertex `b_i` of `B_i`. The path `q1->r_{i-1}->a_i` is the desired transition. QED.

## Lemma 2 — the distinct-port Hall pair is already path-disjoint except for one exact start collision

Let `h_i,h_j`, `i!=j`, be a same-heavy pair from account04/B05 with common heavy target `A`. Suppose its Hall alternative is the distinct-port case, so the selected target ports satisfy `a_i!=a_j`. Let `B` be the other light cycle. The partner already proves the R-interiors of `P_i,P_j` are disjoint.

Then `P_i` and `P_j` are fully vertex-disjoint **unless both are L-type with the same packed start vertex on `B`**. More precisely:

1. two H-type escapes are vertex-disjoint;
2. an H-type escape and an L-type escape are vertex-disjoint;
3. two L-type escapes are vertex-disjoint if and only if their light starts are distinct.

### Proof

Distinct target ports eliminate intersection on `A`; the partner's theorem eliminates intersection in `R`.

If both paths are H-type, their only H vertices are `h_{i-1}` and `h_{j-1}`. These are distinct because `i!=j`. They contain no vertices of `B`, so there is no further possible intersection.

If one is H-type and the other L-type, the first has one vertex on `H` and none on `B`, while the second has one vertex on `B` and none on `H`. Their target ports and R-interiors are already disjoint, so the paths are disjoint.

If both are L-type, they contain no H vertices, have distinct target ports on `A`, and have disjoint R-interiors. Their only possible common vertex is therefore their packed start on `B`, proving the last assertion. QED.

### Consequence

This removes most of the packed-support collision uncertainty left in the partner handoff. The distinct-port Hall alternative does **not** require a new H-order argument to obtain path-level vertex-disjointness: the only unresolved path-level collision is the explicit state

`LL-COMMON-START`:

both escapes start at the same vertex of the opposite light cycle.

Thus the first unpaid implication `HT-PORT-CLOSE` sharpens to a smaller problem: close `LL-COMMON-START` or, when the two escapes are already disjoint, solve only the genuine cyclic endpoint-order/splice issue on the packed supports.

## Lemma 3 — exact fan collision supplies a canonical direct R-free cross arc

Suppose the partner's Hall alternative is the exact fan collision for a same-heavy pair. Orient that unordered pair cyclically as `h_i,h_{i+1}`. If the common target is `A`, with `X=N+(x) cap A`, and the unique extra port is `a` so that both heavy fans equal `X union {a}`, then

`h_i->a`

is an x-free H-to-A cross transition with empty R-interior, and `h_i` is simultaneously a dominator of the fan arc `h_{i+1}->a`.

### Proof

The exact collision gives `a in N+(h_i) cap N+(h_{i+1})`; the packed triangle gives `h_i->h_{i+1}`. Hence `h_i` points to both endpoints of `h_{i+1}->a`, while its own fan arc `h_i->a` is already a direct H-to-A transition. QED.

The collision state therefore has a completely rigid R-free transition at the common extra port. What remains is not internal-path uncertainty but the fact that both witnesses offer the same non-sink port.

## Lemma 4 — exact compatibility map with the neutral equality return

Assume the partner's fourth-witness branch is the neutral equality case. In the exact cage, the pure-R suffix of the equality path ending at `r2` is one of

`r2`, `r1->r2`, `r0->r1->r2`.

After appending `r2->h0`, call the resulting x-free light-to-H return `Q`. Then for an escape `P_i` from Lemma 1:

- `P0` has no forced H-collision with `Q`; it meets `Q` in `R` exactly when it is R-bearing, because its possible R-interior is `{r2}`;
- an H-type `P1` necessarily meets `Q` at `h0`; an L-type `P1` has no forced H-collision, and its possible R-intersection is only `r0`;
- `P2` has no forced H-collision with `Q`; its possible R-intersection is only `r1`.

The only other possible intersection is at a light packed endpoint/start when the support containing the start of `Q` is also used by the escape.

### Proof

The exact remainder arcs include `r0->r1`, `r1->r2`, no `r0->r2`, and `x` is an R-sink. Hence an R-internal directed path ending at `r2` can enter the remainder only at `r2`, `r1`, or `r0`, yielding exactly the three displayed suffixes. Appending `r2->h0` makes `Q` use `h0,r2` and possibly `r1,r0`, but never `x`.

By Lemma 1, H-type `P_i` uses only `h_{i-1}` on `H`; L-type `P_i` uses no H vertex; and the only possible R vertex is `r_{i-1}`. Substituting `i=0,1,2` gives the stated collision map. QED.

## Direct disposition of the partner's first missing implication

The partner's `HT-PORT-CLOSE` was not yet a theorem; it was the first unpaid implication. This run directly resolves one of its hidden subquestions and refutes one unnecessary obstacle:

- **derived:** in the distinct-port branch, disjoint R-interiors upgrade to fully vertex-disjoint whole escape paths automatically except for the single exact `LL-COMMON-START` collision;
- **derived:** the exact fan-collision branch contains a canonical direct R-free H-to-light transition at the common extra port;
- **derived:** the equality-return branch has the finite collision map of Lemma 4;
- **not yet derived:** these paths necessarily splice into two legal vertex-disjoint replacement cycles. Cyclic endpoint order on the packed supports, `LL-COMMON-START`, and the common-extra-port collision remain the genuine blockers.

The earliest remaining statement is therefore

`HT-START-ORDER-CLOSE-v2`:

> show that either the two distinct-port escapes can be chosen without `LL-COMMON-START` and with splice-compatible cyclic endpoint order, or the common-start condition forces a SIX witness, strict lexicographic packing improvement, exchanged-remainder directed cycle, or fourth directed cycle; in the exact fan-collision branch, combine the canonical direct cross arc with the partner's cross/equality return to obtain the same alternatives.

This is a strictly smaller obligation than the partner's original wording because whole-path disjointness is now paid in every distinct-port signature except one explicit start collision.

No full BT4 proof and no novelty claim are made. The graph itself is never altered, so the exact seven-outdegree hypothesis is preserved. Every vertex-disjointness assertion above is proved from the exact support signatures and the partner's already-proved R-interior disjointness. Brain status remains `WITHOUT_VERIFIED_BRAIN`.
