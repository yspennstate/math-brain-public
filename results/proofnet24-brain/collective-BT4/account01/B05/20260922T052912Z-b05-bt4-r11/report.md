# BT4 B05 — compatible bypass condensation

Run: `20260922T052912Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact inherited state used

I read the latest complete shared BT4 handoff available in the control repository, account03/B06 `20260922T052316Z`, candidate `BT4-R4-F3-MAJORITY-CROSS-v1` (shared blob `dad56a7b89ccd82a4393c147e26985485305378d`), and its exact canonical report blob `697fde372dee5fec64d03923523d13fc6edcab7a`. That result proves that the arc-maximal triangular F3 state always supplies a light-to-light cross of length at most two, and in the both-repeat cover case supplies internally-disjoint opposite crosses. Its first unpaid implication is the genuine disjoint-splice step.

I also consume and apply the named OTHER-account account04/B06 result `BT4-SIX-DUAL-WALL-LIFT-v1`, shared blob `76bf6ed16c06e44b5a23dd5da5df2fe5fd94a69e`. In the all-long exact-six / zero-remainder-exit branch, each incoming-ladder/outgoing-ray pair yields either a genuine CROSS or a distinct-port same-support BYPASS (apart from the already-accounted short-support boundary). Thus the live team repeatedly accumulates genuine R-internal same-support bypasses, but the old reports treated a strict collar or common-port collection as an interface rather than an actual multi-bypass augmentation.

The inherited normal form used below is only the team's already-established one: a hypothetical BT4 counterexample has three pairwise-disjoint directed packed cycles `C1,C2,C3`; their remainder `R` is acyclic (indeed the statement below only needs this consequence); and in the exact-seven oriented normal form every vertex has outdegree seven. No relaxed cycle is used.

## Compact conditional end-to-end route

The current collective route contains multiple mechanisms producing distinct-port same-support R-internal bypasses: the SIX dual-wall lift above, the SC2 third-port theorem, and strict/equality collar outputs. The missing exchange question is what can be done when more than one such bypass is simultaneously available.

This report proves the following route:

`compatible bypass family`
`-> simultaneous support replacement`
`-> released-block dependency digraph`
`-> dependency circuit gives a fourth directed cycle`
`-> otherwise a terminal released block has no arc into any released block`.

If the selected bypasses consume all old remainder vertices, the terminal block endpoint is therefore a sink of the exchanged remainder. In the exact-seven normal form all seven of its outneighbors are packed, so some two packed cycles receive at least five; in the global NO-SIX branch the fan profile is forced to `(3,2,2)`. Thus a full-remainder bypass family cannot terminate as an unstructured strict collar: it either closes BT4 immediately or regenerates the campaign's canonical five-witness / `(3,2,2)` sink state.

The first remaining implication on this mechanism is consequently a source-valid **bypass-cover selection** statement: in the accumulated CROSS/BYPASS interfaces, force either a cross-based closure or a compatible same-support bypass family whose interiors consume all of `R` (or quantify the unavoidable uncovered core). Common packed ports and overlapping support intervals are now the exact obstruction, not the absence of an exchange once compatibility is achieved.

## Theorem — BT4-COMPATIBLE-BYPASS-CONDENSATION-v1

Let `D` be any digraph with pairwise vertex-disjoint directed cycles `C1,C2,C3`, and let

`R = V(D) \ (V(C1) union V(C2) union V(C3))`.

Assume `D[R]` is acyclic.

A **same-support bypass switch** `sigma_i` consists of:

- a support cycle `C_{tau(i)}`;
- distinct support vertices `a_i,b_i`;
- the forward directed support segment `S_i=C_{tau(i)}[a_i,b_i]`;
- a directed path `P_i:a_i -> ... -> b_i` whose internal vertices lie in `R`.

Write `B_i=int(S_i)` for the released support block. We call a finite family `F` **compatible** when:

1. all bypass interiors `int(P_i)` are pairwise vertex-disjoint;
2. on each support cycle, the support segments `S_i` belonging to `F` are pairwise vertex-disjoint (including their endpoints);
3. every `B_i` used as a dependency node is nonempty.

Then all switches in `F` can be performed simultaneously, replacing each `S_i` by `P_i`. This produces three pairwise vertex-disjoint directed cycles `C1',C2',C3'`. Their remainder is exactly

`R_F = (R \ union_i int(P_i)) union (union_i B_i)`.          (1)

For each nonempty released block `B_i`, let `t_i` be its terminal vertex in the old support direction. Define a directed dependency graph `J_F` on the switch indices by

`i -> j` iff `t_i` has an arc to some vertex of B_j.             (2)

Self-arcs are allowed in this definition.

### Claim 1: a directed circuit in `J_F` gives four disjoint directed cycles

Suppose

`i_1 -> i_2 -> ... -> i_m -> i_1`

is a directed circuit. For each edge `i_k -> i_{k+1}`, choose a hit vertex `y_{k+1} in B_{i_{k+1}}` with

`t_{i_k} -> y_{k+1}`.

Inside each released block, the old support orientation gives a directed path

`y_k -> B_{i_k} -> t_{i_k}`.

Concatenating these block suffixes and the chosen cross-arcs gives

`y_1 -> ... -> t_{i_1} -> y_2 -> ... -> t_{i_2} -> ... -> y_1`,

a genuine directed cycle contained entirely in `R_F`. Different blocks are disjoint by compatibility. Hence this residual cycle is vertex-disjoint from `C1',C2',C3'`, giving four pairwise vertex-disjoint directed cycles in `D`.

For `m=1`, an arc from `t_i` to an earlier vertex of its own block similarly closes a directed cycle inside `B_i` (a loop at `t_i` itself is unavailable in a loopless digraph).

Therefore in a BT4 counterexample `J_F` has no directed circuit.

### Claim 2: every compatible family in a counterexample has a terminal released block

Since `J_F` is acyclic, choose a sink index `i`. There is no self-circuit and no outgoing edge from `i` to another block. Hence

`N^+(t_i) intersect (union_j B_j) = empty`.                    (3)

Combining (1) and (3), every outneighbor of `t_i` that remains in the exchanged remainder lies in the untouched old-remainder set

`R_0 = R \ union_j int(P_j)`.                                  (4)

Consequently

`d^+_{R_F}(t_i) <= |R_0|`.                                     (5)

This conclusion uses no minimum-packing comparison and is valid for both equality bypasses and strict collars.

### Claim 3: full consumption regenerates a five-witness sink

If the compatible bypass interiors consume all old remainder vertices, then `R_0=empty`. Equation (5) says that `t_i` is a sink of `D[R_F]`.

Now enter the inherited exact-outdegree-seven normal form. Since all seven outneighbors of `t_i` lie on `C1' union C2' union C3'`, two of the three packed cycles together contain at least five of them: for nonnegative integers `d_1+d_2+d_3=7`, the two largest satisfy `d_(1)+d_(2)>=5`.

Thus the simultaneous bypass exchange either already produced a fourth cycle by Claim 1, or it regenerates a pair-deletion five-witness on the exchanged packing. In the campaign's global NO-SIX subbranch, every two-cycle fan is at most five, so the only sorted fan partition of seven is

`(3,2,2)`.                                                       (6)

Hence a full-remainder compatible bypass family routes directly back into the canonical `(3,2,2)` sink machinery rather than remaining a free collar obstruction.

QED.

## Quantitative uncovered-core corollary

The same proof gives a useful non-full-cover estimate. If exactly `q=|R_0|` old remainder vertices are not consumed, then the terminal released vertex satisfies

`d^+_{C1' union C2' union C3'}(t_i) >= 7-q`.                   (7)

Thus the obstruction to immediate sink regeneration is measured exactly by the uncovered old-remainder core, not by the number or lengths of the bypasses.

## Application to the current team frontier

Apply the theorem to the account04/B06 `BT4-SIX-DUAL-WALL-LIFT-v1` outputs whenever two or more of its distinct-port same-support BYPASS interfaces can be selected with pairwise-disjoint R interiors and pairwise-disjoint support segments. A directed circuit among the released blocks closes BT4 immediately. If the selected bypasses cover `R`, absence of such a circuit forces a new `(3,2,2)` sink in global NO-SIX and therefore recycles into the existing five-witness machinery.

The same mechanism applies to distinct-port same-support bypasses generated from the SC2 third-port branch after the account03/B06 F3 short-cross theorem supplies the bounded light-to-light transition. It is deliberately not claimed that the current 2x2 dual-wall paths automatically admit a compatible full cover: their possible common packed ports, support overlap, and shared R interiors are exactly the unpaid selection problem.

## Exact first unpaid implication

`BT4-BYPASS-COVER-SELECTION-v1`:

> In the accumulated SIX/SC2/F3 CROSS-BYPASS frontier, prove that either existing cross interfaces splice to a legal two-cycle replacement/fourth cycle, or one can select a compatible family of genuine same-support R-internal bypasses whose interiors consume all old remainder vertices. Equivalently, if no such family exists, derive from the overlap/common-port obstruction a strict smaller three-packing, a cyclic exchanged remainder, SIX, or a new forced packed port.

This is strictly narrower than the previous instruction to “splice the accumulated bypasses”: once compatibility and full consumption are present, the theorem above completes the exchange or regenerates the canonical sink state automatically.

## Nonclaims / failure boundary

- A single CROSS is not counted as a fourth cycle.
- A single bypass is not itself a contradiction.
- Compatibility and full remainder consumption are not inferred from the existence of the four ladder/ray interfaces.
- The result does not close F2, the separate SIX boundary, or BT4 globally.
- No relaxed, edge-disjoint, or one-reversal cycle is substituted for a genuine directed cycle.

Honest outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains `OPEN_NOT_PROVED`.
