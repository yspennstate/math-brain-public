# BT4 account03/B04 — exact packed-support collision map for the x-free Hall escapes

Run: `b04-20260922t055204z-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-PORT-COLLISION-MAP-v1`  
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

I use only the partner's proved exact cage and escape statements. No inference below assumes that disjoint remainder interiors imply disjoint whole paths.

The partner's exact four-remainder cage is

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with the exact induced arcs stated in its Lemma 1. In particular each `h_i` has an x-free heavy-fan escape to a chosen heavy light target `A_i`; its R-interior is empty or `{r_{i-1}}`, and its packed start is either `h_{i-1}` or a vertex of the opposite light cycle. For a same-heavy pair, the partner proves either distinct target ports on the common target `A`, or the exact fan collision `N+(h_i) cap A=N+(h_j) cap A=X union {a}`, where `X=N+(x) cap A` and `|X|=2`. The fourth witness `r2` gives either a genuine cross-packed transition or a neutral equality return from a light cycle to `r2`, which extends through `r2->h0` to an x-free light-to-H return.

## Lemma 1 — every partner escape has one of two exact support signatures

Fix `i` modulo three and one of the partner's chosen target ports `a_i` on its heavy target `A_i`. Let `B_i` be the other light packed cycle. The domination-ladder proof in account04/B05 gives an escape `P_i` of exactly one of the following support signatures:

- **H-type:** packed start `h_{i-1}`, H-vertex set exactly `{h_{i-1},h_i}`, R-interior either empty or `{r_{i-1}}`, and terminal vertex `a_i` on `A_i`;
- **L-type:** packed start some `b_i in B_i`, H-vertex set exactly `{h_i}`, R-interior either empty or `{r_{i-1}}`, and terminal vertex `a_i` on `A_i`.

More explicitly the possible path shapes are

`h_{i-1}->h_i->a_i`,
`h_{i-1}->r_{i-1}->h_i->a_i`,
`b_i->h_i->a_i`,
`b_i->r_{i-1}->h_i->a_i`.

### Proof

In the partner's proof, domination of `h_i->a_i` either reaches a packed dominator immediately, or first reaches the unique possible remainder predecessor `r_{i-1}`. If it reaches `r_{i-1}`, the next domination step is packed because the exact cage has no allowable second remainder dominator. The packed dominator cannot lie on `A_i`; hence it is either the support predecessor `h_{i-1}` or a vertex of the opposite light cycle `B_i`. No further packed or remainder vertex occurs before `h_i->a_i`. This is exactly the list above. QED.

## Lemma 2 — exact whole-path collision classification for a distinct-port Hall pair

Let `h_i,h_j` be the partner's same-heavy pair with common target `A`, and suppose the Hall alternative is the distinct-port case, so the selected endpoints satisfy `a_i != a_j`. Put `B` for the other light cycle. The partner already proves the R-interiors of `P_i,P_j` are disjoint. Then the two *whole paths* are vertex-disjoint if and only if one of the following holds:

1. one path is H-type at index `k` and the other is L-type at index `k+1` (indices modulo three); or
2. both are L-type and their light starts are distinct.

Equivalently, failure of whole-path disjointness is confined to exactly three packed-support collision patterns:

- **HH:** both escapes are H-type;
- **HL-backward:** one is H-type at `k` and the other is L-type at `k-1`;
- **LL-common-start:** both are L-type with the same light start vertex.

### Proof

Distinct target ports eliminate intersection on `A`. The partner's theorem eliminates intersection in `R`. An H-type escape has H-set `{h_{k-1},h_k}` and no light-start vertex; an L-type escape at `j` has H-set `{h_j}` and one light-start vertex `b_j in B`.

Two different two-element subsets `{h_{i-1},h_i}` and `{h_{j-1},h_j}` of the three-vertex cycle `H` always meet, proving HH collision.

For H-type `P_k` and L-type `P_j`, the only possible H-intersection is `h_j in {h_{k-1},h_k}`. Since `j!=k`, this occurs exactly when `j=k-1`; when `j=k+1`, their H-sets are disjoint. Their other support vertices lie on disjoint packed supports (`B` versus `A`).

For two L-type paths, the H vertices `h_i,h_j` are distinct, the `A` endpoints are distinct, and the R-interiors are disjoint, so the sole possible intersection is their light start. Thus they are disjoint exactly when `b_i!=b_j`. QED.

### Consequence

The tempting implication

> distinct target ports + disjoint R-interiors => vertex-disjoint escape paths

is **false as a proof step** under the currently proved hypotheses. For example, any two H-type escapes necessarily share one H vertex. The partner's first unpaid implication `HT-PORT-CLOSE` must therefore include a start/signature compatibility argument; remainder-interior disjointness alone cannot pay vertex-disjointness.

Conversely, the lemma gives an exact positive upgrade criterion: once a Hall pair has signature `H_k/L_{k+1}`, or two L-signatures with distinct starts, the pair is genuinely vertex-disjoint without any additional independence assumption.

## Lemma 3 — exact fan collision forces a canonical R-free short H-to-light transition

Suppose the partner's Hall alternative is the exact fan collision for a same-heavy pair. Orient the pair cyclically as `h_i,h_{i+1}`. If their common heavy target is `A` and the unique extra port outside `X=N+(x) cap A` is `a`, then

`h_i -> h_{i+1} -> a`

is an x-free H-to-A transition with empty R-interior.

### Proof

The exact fan collision says `a in N+(h_i) cap N+(h_{i+1})`. The packed triangle gives `h_i->h_{i+1}`. Hence `h_i` itself dominates the fan arc `h_{i+1}->a`, and the displayed two-edge transition is available. It avoids `x` and all of `R`. QED.

This does not by itself close BT4, because its target port is the same collision port `a`; it does, however, remove all uncertainty about one escape's internal support geometry in the collision branch.

## Lemma 4 — exact equality-return collision map

Assume the partner's fourth-witness branch is the neutral equality case. In the exact cage, the pure-R part of the equality path ending at `r2` has one of the three suffixes

`r2`, `r1->r2`, `r0->r1->r2`.

After appending `r2->h0`, call the resulting x-free light-to-H return `Q`. Then:

- every `P0` collides with `Q` at `h0` (and an R-bearing `P0` also uses `r2`);
- an H-type `P1` collides with `Q` at `h0`;
- an L-type `P1` has no forced H-collision with `Q`; its only possible R-collision is at `r0`, and only when both paths actually use `r0`;
- every `P2` has no forced H-collision with `Q`; its only possible R-collision is at `r1`, and only when both paths actually use `r1`.

Additional intersection can occur only at the light support endpoint/start when `Q` starts on a light support used by the escape.

### Proof

The partner's Lemma 1 gives the exact R-arcs `r0->r1`, `r1->r2`, with no `r0->r2`, while `x` is an R-sink. Therefore an R-internal directed path ending at `r2` can enter R only at `r2`, `r1`, or `r0`, and has exactly the listed suffix. Appending `r2->h0` makes `Q` use `h0,r2` and possibly `r1,r0`, never `x`.

Lemma 1 above gives the support/R signatures of each `P_i`. `P0` always contains `h0`; H-type `P1` contains `{h0,h1}`; L-type `P1` contains `h1` and at most `r0`; `P2` contains `h2` and, only if H-type, `h1`, with at most `r1`. Comparing these exact sets proves the claims. QED.

## What is now paid and what remains

The account04/B05 handoff correctly paid disjointness of R-interiors. This report pays the next bookkeeping layer exactly: it classifies when the Hall escapes are truly vertex-disjoint, identifies the only three packed-support collision patterns, supplies a canonical R-free transition in the exact fan-collision branch, and gives the exact compatibility map with the neutral equality return.

The earliest remaining implication is now narrower than the partner's original `HT-PORT-CLOSE`:

`HT-START-ORDER-CLOSE`: eliminate or splice the three residual packed-support collision patterns `HH`, `HL-backward`, `LL-common-start`, while simultaneously respecting the finite equality-return compatibility map above. In the positive signature cases, whole-path vertex-disjointness is already certified, so only cyclic endpoint order on the packed supports remains.

A productive next attack is a second Hall/SDR argument on possible *packed starts* of the distinct target-port escapes, rather than another Hall argument on the target ports. The exact fan-collision branch should be paired with the canonical short transition `h_i->h_{i+1}->a` and the equality-return suffix classification.

No full BT4 proof, no novelty claim, and no brain-use claim is made. Exact outdegree seven is preserved throughout: the graph is never modified, and the only degree count imported is the partner's already proved exact-five-witness structure. Vertex-disjointness is asserted only in the cases proved above.
