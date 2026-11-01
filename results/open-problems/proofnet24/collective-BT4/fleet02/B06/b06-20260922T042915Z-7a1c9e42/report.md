# BT4 fleet02/B06 — F3 one-fan wedge redirect and exact adversaries

Run: `b06-20260922T042915Z-7a1c9e42`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Local false candidate: `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Control and scope


Exact target retained throughout: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven should contain four pairwise vertex-disjoint genuinely directed cycles. Digons count as directed cycles.

No authenticated brain retrieval/context was used. No benchmark or sealed-answer material was used.

## Current lead and named OTHER-account input

The latest complete campaign-lead version read in this invocation is fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, primary science commit `71ff185ec9b372cc24c02c4630cd7c202d13eee7`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`. Its theorem reduces the four-remainder heavy-triangle state to forced multi-light three-dominators, a rigid same-heavy exact-five-witness pair, or a split-heavy certified cross; the first global unpaid implication is still a genuine port splice/strict replacement (with SIX separate).

The named OTHER-account result actually consumed is fleet03/B04 run `20260922T035106Z-fleet03-B04-bt4-r11`, report blob `c000e636818c9bf4ca77ea457b88fa702cfd8a77`, candidate `BT4-R4-F3-TWOFAN-COLLAPSE-v1`. Its live four-remainder F3 state has a freed remainder vertex `q` that:

- dominates the other three remainder vertices;
- has exactly one outneighbor on its support cycle `C`;
- has fan sizes two and one on the other two packed cycles `A,B`;
- after the partner's two-fan collapse has **no** inport from `A`;
- on the one-fan cycle `B` has the residual wedge `b^- -> q -> b`, with `b^{--} -> q` only a possible extra inport.

I apply that exact residual state rather than copying its outcome label.

## Compact conditional end-to-end route

A complete BT4 proof would follow from the current team reductions if all remaining neutral/cross interfaces are forced to terminate in a strict packing decrease, two legal replacement cycles, an exchanged-remainder cycle, or a fourth disjoint cycle:

1. A digon is immediately one of the four cycles: deleting its two vertices leaves minimum outdegree at least five, so the genuine `k=3` theorem supplies the other three cycles. Hence a counterexample is oriented.
2. Pass to the inherited exact-seven, 3-vertex-strong, globally minimum three-cycle packing with acyclic remainder.
3. The lead's newest heavy-triangle theorem reduces that four-remainder obstruction to explicit port/witness interfaces; SIX remains separately unpaid.
4. The named fleet03/B04 result removes the F3 two-fan-inport branch by a neutral pivot/collapse and leaves only the one-fan predecessor wedge above.
5. The theorem below proves that this residual F3 wedge **always has a neutral pivot**. The tempting stronger claim that the pivot must occur on the one-fan cycle is false; if that arc is absent, 3-vertex-strongness redirects the pivot to the support cycle.
6. The first unpaid implication after this run is therefore orbit/splice termination: prove that iterating these neutral pivots cannot return to an equivalent F3 state indefinitely without producing one of the lead's strict/cross/fourth-cycle exits.

This is not a full proof candidate.

## Exact local adversary: the one-fan second-predecessor arc is not locally forced

Candidate refuted:

> `BT4-F3-WEDGE-PIVOT-v0`: the exact local F3 degree data, acyclic four-vertex remainder and 3-vertex-strongness force `b^{--}->q`, so the residual one-fan wedge always pivots on `B`.

The checker archives a 17-vertex oriented digraph `D0` with 135 arcs. It has only one nonadjacent unordered pair, minimum outdegree seven, maximum outdegree twelve, outdegree vector

`(7,7,7,7,7,7,7,7,7,7,7,7,7,10,11,11,12)`,

and remains strongly connected after deleting any at most two vertices.

Take

- `q=0` and remainder `R=(0,1,2,3)`, with `0` dominating `1,2,3` and the displayed remainder transitive/acyclic;
- support cycle `C=(4,5,6,7)`;
- two-fan cycle `A=(8,9,10,11)`;
- one-fan cycle `B=(12,13,14,15,16)`.

Then

`N+(q) cap R = {1,2,3}`,
`N+(q) cap C = {4}`,
`N+(q) cap A = {8,9}`,
`N+(q) cap B = {14}`.

Writing `b=14`, `b^-=13`, `b^{--}=12`, the wedge `13->0->14` holds, while `0` and `12` are nonadjacent. Thus `12->0` is not forced by those local degree/strongness/profile hypotheses.

The same graph already exhibits the repaired alternative: on `C`, with `c=4`, both `c^-=7` and `c^{--}=6` point to `q`, and

`6 -> 0 -> 4 -> 5 -> 6`

is a same-size directed replacement of `C`, freeing vertex `7`.

This exact graph is deliberately **not** a BT4 counterexample and is not claimed to satisfy global packing minimality: the checker exhibits four disjoint directed triangles `(0,1,5)`, `(2,3,6)`, `(4,10,7)`, `(8,13,11)`. Its role is precise: it refutes only the local inference that `b^{--}->q` follows before global minimum-packing structure is used.

## Packing-distance lemma

Let `(C,A,B)` be a globally minimum-total three-cycle packing in an oriented BT4 counterexample and let `q` lie in the remainder. Suppose `q` has a unique outneighbor `c` on `C`. If `p in C` satisfies `p->q`, then

`dist_C(c,p) >= |C|-2`.

Indeed,

`p -> q -> c -> C[c,p]`

is a directed cycle disjoint from `A` and `B`. Its order is `dist_C(c,p)+2`. If this were smaller than `|C|`, replacing `C` would contradict global minimum of the packing. Since orientation excludes `p=c`, the only possible inports from `C` are therefore

`p in {c^-, c^{--}}`.

This is the same minimum-packing distance mechanism used by the named fleet03/B04 result, now applied symmetrically to the support and one-fan cycles.

## Theorem — BT4-F3-PIVOT-REDIRECT-v1

Assume the named partner's residual F3 state in the inherited normal form:

- `D` is oriented and 3-vertex-strong;
- `(C,A,B)` is a globally minimum-total three-cycle packing with acyclic remainder `R`;
- `q in R` dominates `R-{q}`;
- `q` has exactly one outneighbor `c` on support cycle `C`, exactly two outneighbors on `A`, and exactly one outneighbor `b` on `B`;
- `A` sends no arc to `q`;
- `b^- -> q -> b` on `B`.

Then at least one same-size neutral pivot exists:

1. either `b^{--}->q`, and replacing the segment `b^{--}->b^-->b` by `b^{--}->q->b` gives a neutral pivot on `B` freeing `b^-`;
2. or `c^{--}->q`, and replacing `c^{--}->c^->c` by `c^{--}->q->c` gives a neutral pivot on `C` freeing `c^-`.

### Proof

If `b^{--}->q`, conclusion 1 is immediate, so suppose this arc is absent.

Apply the packing-distance lemma on `B`. Since `q` has the unique `B`-outneighbor `b`, every `B`-vertex that points to `q` must lie in `{b^-,b^{--}}`. By hypothesis `b^- -> q`, by the branch assumption `b^{--} not->q`.

Because `D` is 3-vertex-strong, `D-b^-` is 2-vertex-strong. Directed Menger therefore gives two internally vertex-disjoint directed paths from `b^{--}` to `q` in `D-b^-`. The direct arc `b^{--}->q` is absent, so each path has a last internal vertex `p_i` with `p_i->q`, and the two vertices `p_1,p_2` are distinct.

Neither `p_i` lies in `R-{q}`, because `q` dominates every other remainder vertex and `D` is oriented. Neither lies on `A`, because this is exactly the partner's residual no-`A`-inport branch. Neither lies on `B`: the only possible `B` inports are `b^-` and `b^{--}`, but `b^-` was deleted and `b^{--}->q` is absent.

Hence both distinct last predecessors `p_1,p_2` lie on `C`.

Apply the packing-distance lemma again, now to the unique support outneighbor `c`. Every `C`-inport to `q` lies in `{c^-,c^{--}}`. Since `p_1,p_2` are distinct, they are exactly these two vertices. In particular `c^{--}->q`, proving conclusion 2.

The replacement cycle has the same order as `C`, so the new three-packing is still globally minimum. In a genuine counterexample its exchanged remainder must remain acyclic, since any directed cycle there together with the three packed cycles would already be a four-pack. QED.

### Significance

The residual F3 branch cannot be terminal merely because the one-fan second-predecessor arc is absent. Three-vertex-strongness plus the exact F3 no-inport data force a **redirected support pivot**. The next obstruction is therefore genuinely an orbit/compatibility problem, not an existence-of-pivot problem.

## Digon boundary: the threshold-five loss is sharp

A separate exact adversary repairs the common overstatement that deleting a digon from a `delta^+>=7` digraph should leave minimum outdegree at least six. Take complete bidirected `K8`. Every vertex has outdegree seven. Delete the two vertices of any chosen digon: the survivor is complete bidirected `K6` and has minimum outdegree exactly five.

Thus the valid digon reduction is sharp at this level: delete the digon, invoke the genuine `k=3` theorem at threshold five on the remainder, then restore the digon as the fourth cycle. No threshold-six or threshold-seven preservation may be assumed.

## Exact computation

The deterministic checker was executed in this invocation and returned `PASS`.

- checker path: `proofnet24/collective-BT4/fleet02/B06/b06-20260922T042915Z-7a1c9e42/checker.py`
- checker immutable commit: `641b599a8b981b5a704e8a7ce218f69a89e9d395`
- checker local byte SHA-256: `764b99778379044915bac8fc526d888d9ad86c0bdd89a172165a283231ad9a88`
- output path: `proofnet24/collective-BT4/fleet02/B06/b06-20260922T042915Z-7a1c9e42/checker_output.json`
- output immutable commit: `e89eebf4be64e9e4e195a74ea6b33c8bf038a728`
- output local byte SHA-256: `78728d58ec2c1e6ab59b7d3156012472e65a68589253c773a0fcb6333eb14aef`

The code contains the complete 135-arc adjacency set and assertions for orientation, the unique nonedge, exact degree vector, three-vertex-strongness, the F3 local profile, redirected support pivot, explicit four-pack, and the bidirected-`K8` digon threshold test.

## Honest boundary and next implication

`BT4-F3-PIVOT-REDIRECT-v1` does not prove that a neutral pivot strictly advances a global potential. A finite family of globally minimum packings could in principle form a neutral orbit. The next essential implication is to orient such an orbit by a source-valid potential (or show a repeated state forces one of the lead's reciprocal/third-port/same-heavy interfaces) so that repeated redirected pivots cannot cycle forever without a strict packing decrease, exchanged-remainder cycle, or fourth directed cycle.

The lead's multi-light/same-heavy/split-heavy interfaces and the separate SIX closure remain independently unpaid.

No full BT4 proof is claimed.

## Model / execution accounting

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured effort: `UNKNOWN_NOT_EXPOSED`. Known/self-observed effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning tokens: `null / NOT_EXPOSED`. Provider thinking seconds: `null / NOT_EXPOSED`.

Privacy/secret review: scoped BT4 mathematics and control provenance only; no credentials, scheduler identifiers, machine paths, benchmark gold, sealed answers, unrelated private data, raw transcripts, email/Drive data, public posting, paid API/model/Codex use, remote workflows, or permission changes.
