# BT4 fleet02/B20 r16 — fresh-port splice tax and cyclic port wall

Run: `20260922T065811Z-fleet02-B20-bt4-r16`

Classification: **ESSENTIAL_STEP_APPLIED**

FULL_TARGET_CHANGE: **NONE**. This is not a proof of BT4 and not a proof of unrestricted Bermond–Thomassen.

MECHANISM_CHANGE: the fresh-port/nonreuse wall is reduced by (i) converting any interior intersection of opposite connectors into a same-support bypass with an exact packing-minimality tax, and (ii) converting every splice-compatible internally disjoint 2x2 connector system in the live four-remainder branch into an exact omitted-gap inequality. The remaining obstruction is localized to endpoint collision, cyclic-order/parity mismatch, an eight-edge collar, or third-support mediation.

Execution context: `WITHOUT_VERIFIED_BRAIN`. No brain installation or benchmark work was performed.

## Exact target and source model

Prove: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four **vertex-disjoint genuinely directed cycles**. Opposite arcs and digons are allowed; no order restriction is imposed.

Throughout the live reduction, assume for contradiction a minimum counterexample and a globally minimum three-cycle packing `(A,B,H)` with remainder `R`. The established campaign reductions give the acyclic-remainder / small-remainder regime and, in the clean four-port branch, an opposite connector pair between the two light packed cycles. Nothing below uses edge-disjointness, nearly directed cycles, a one-reversed-arc relaxation, or a larger degree threshold.

## Source-bound inputs actually consumed

1. Campaign lead `fleet02/B04`, complete report:
   - `proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`
   - scientific commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`
   - Used for the minimum-packing normal form and the live clean opposite connector pair around the four-remainder interface.

2. Named partner `fleet04/B06`, completed `BT4-SIX-DUAL-WALL-LIFT-v1`:
   - Used in the conditional end-to-end skeleton: the exact-six cycle-supported wall already reduces to a clean opposite cross pair or bounded same-support bypass. Its local witness geometry is not silently transplanted into the remainder-supported rank-wall proof below.

3. Completed OTHER-account result `fleet03/B05`, `BT4-PORT-RANK-WALL-v1`:
   - This is used directly. It proves that one connector each way has pairing rank one and supplies, by 3-vertex-connectivity, either a fresh reverse connector avoiding the old reverse endpoints or an explicit third-support `B→C→A` mediation.

4. Completed OTHER-account result `fleet01/B04`, `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`:
   - Used to obtain a fresh packed-source cross outside a shortest mixed cycle, unless a distinct-port same-support bypass has already appeared.

5. Safety correction retained: `fleet04/B05` correction `BT4-CORRECTION-fleet04-B05-20260922T0632Z.md`. No equality `|T|=4` is used; only the corrected weaker conclusion is permitted.

## Compact conditional end-to-end argument

The current campaign implication can be organized as follows.

- A minimum counterexample is 3-vertex-strong and admits a globally minimum three-cycle packing `(A,B,H)`; if four disjoint directed cycles already exist, stop.
- Existing lead/partner reductions force the hard branch into a small acyclic remainder, and the exact-six branch already yields a clean opposite cross pair or a bounded same-support bypass.
- In the four-remainder clean-pair branch, write one known `A→B` connector `P1` and one known `B→A` connector `Q1`. The rank-one obstruction means these two alone do not create two replacement cycles.
- `fleet01/B04` supplies a fresh cross in one direction unless a bypass is already obtained. By symmetry interchange `A,B` if necessary so this is a second `A→B` connector `P2`.
- `fleet03/B05` then supplies either a fresh `B→A` connector `Q2` avoiding the old reverse endpoints, or a third-support mediation. The latter is a separately named live branch.
- The new lemmas below show that, in the `R`-internal `Q2` branch, an interior intersection with `P1` is already a bypass, while an internally disjoint 2x2 system either has an endpoint/cyclic-order obstruction or obeys a sharp total omitted-gap bound `G_A+G_B≤8` in the live `|R|=4` geometry.
- Therefore BT4 would follow once the localized **fresh-port parity/collar/mediation wall** is universally closed by a strict three-packing reduction, a directed cycle in the exchanged remainder, or a fourth cycle disjoint from the other three.

The final bullet is not yet proved.

## First essential unpaid implication before this run

In the exact source model and the live globally minimum packing, start with a clean opposite connector pair between `A` and `B`. After the shortest-mixed-cycle fresh-cross theorem and the 3-connectivity fresh-reverse theorem, show that the resulting additional ports can be combined without vertex reuse into two legal directed replacement cycles, or else force a strictly smaller three-packing / a directed remainder cycle / a fourth disjoint directed cycle. The missing point was not mere existence of paths: it was **nonreuse plus cyclic compatibility of four ports**.

## Lemma 1 — opposite-intersection bypass

**Lemma `BT4-OPPOSITE-INTERSECTION-BYPASS-v1`.** Let `A,B` be vertex-disjoint directed cycles of the globally minimum three-packing, and let `R` be the remainder. Let

- `P=p0→…→pm` be a directed `A→B` connector with `p0∈A`, `pm∈B`, and every internal vertex in `R`;
- `Q=q0→…→qn` be a directed `B→A` connector with `q0∈B`, `qn∈A`, and every internal vertex in `R`;
- `p0≠qn` and `pm≠q0`.

If `Int(P)∩Int(Q)≠∅`, then there is a genuine directed same-support `A`-bypass `L_A:p0→…→qn` whose internal vertices all lie in `R`. Moreover, if `d_A(p0,qn)` is forward directed distance on `A`, then

`|E(L_A)| ≥ d_A(p0,qn)`.

The symmetric statement holds with `A,B` exchanged.

**Proof.** Choose `v∈Int(P)∩Int(Q)` with minimum index along `P`. Consider the prefix `P[p0,v]` and the suffix `Q[v,qn]`. If they shared a vertex `u≠v`, then `u` would be a common vertex of `P,Q` appearing strictly before `v` on `P`, contradicting the choice of `v`. Thus their concatenation

`L_A := P[p0,v] · Q[v,qn]`

is a simple genuinely directed path from `p0` to `qn`, with all internal vertices in `R`.

If `|E(L_A)|<d_A(p0,qn)`, replace the forward segment `A[p0,qn]` by `L_A`. The complementary segment `A[qn,p0]` together with `L_A` is a genuine directed cycle strictly shorter than `A`, is disjoint from `B` and `H`, and therefore produces a strictly smaller three-cycle packing, contradicting global minimum. Hence the inequality. ∎

**Consequence for the fresh-reverse wall.** In the `fleet03/B05` branch where the fresh reverse connector is `R`-internal, any interior intersection with the old opposite connector is already an accepted BYPASS output. Thus when analyzing the genuinely new nonreuse obstruction, the fresh reverse connector may be assumed internally disjoint from the old forward connector; this is a proved reduction, not an extra hypothesis.

## Lemma 2 — two-by-two splice tax

**Lemma `BT4-2X2-SPLICE-TAX-v1`.** Let `A,B,H` be the globally minimum three-cycle packing. Suppose there are two directed `A→B` connectors

`P_i : a_i → … → b_i` (`i=1,2`)

and two directed `B→A` connectors

`Q_j : β_j → … → α_j` (`j=1,2`),

all connector interiors lying in `R`. Assume the four ports on each packed support are distinct and that the connector interiors used below are pairwise disjoint. For a permutation `σ∈S_2`, define

`C_i^σ := P_i · B[b_i,β_{σ(i)}] · Q_{σ(i)} · A[α_{σ(i)},a_i]`.

If for some `σ` the two displayed `A`-intervals are vertex-disjoint and the two displayed `B`-intervals are vertex-disjoint, then `C_1^σ,C_2^σ` are genuine vertex-disjoint directed cycles, disjoint also from `H`. Put

`L_X = Σ_i |E(P_i)| + Σ_j |E(Q_j)|`,
`L_A = Σ_i |E(A[α_{σ(i)},a_i])|`,
`L_B = Σ_i |E(B[b_i,β_{σ(i)}])|`,

and omitted support gaps

`G_A=|A|-L_A`, `G_B=|B|-L_B`.

Then global minimum of the three-packing forces

`G_A + G_B ≤ L_X`.

**Proof.** The disjointness assumptions make `C_1^σ,C_2^σ,H` a legal three-cycle packing. Their total order differs from the original only in the `A∪B` part, and the two new cycles have total edge/order contribution

`L_X+L_A+L_B`.

If this were less than `|A|+|B|`, replacing `A,B` by `C_1^σ,C_2^σ` would strictly reduce the globally minimum three-packing. Therefore

`L_X+L_A+L_B ≥ |A|+|B|`,

which rearranges to `G_A+G_B≤L_X`. Equality is only a neutral exchange and is not claimed to be a contradiction without an additional tie-break. ∎

## Lemma 3 — exact cyclic compatibility test

**Lemma `BT4-2X2-CYCLIC-MATCH-v1`.** On one directed support cycle with four distinct ports, two of one connector type and two of the opposite type, a pairing whose two forward support intervals are vertex-disjoint exists if and only if the two port types alternate in cyclic order. When they alternate, the admissible pairing is unique. Consequently, for the 2x2 system above a splice-compatible `σ` exists exactly when both `A` and `B` have alternating port types and their two unique matching parities agree.

**Proof.** If the types alternate, pair each first-type port to the next second-type port in the forward cyclic order; the resulting intervals are disjoint, and the other pairing nests/crosses them. If the types do not alternate, after cyclic rotation the type word is `XXYY`; either perfect pairing has one forward interval containing an endpoint of the other, so the two intervals cannot be vertex-disjoint. Applying this independently on `A` and `B` gives the parity-agreement criterion. ∎

This converts the vague “cyclic-order wall” into two explicit possibilities: a grouped `XXYY` port pattern on at least one support, or alternating patterns on both supports with opposite matching parity.

## The live four-remainder quantitative collapse

Now specialize to the clean four-remainder branch from the lead.

- The old forward connector is `P1=p→x→b`, so `|P1|=2` and its only remainder interior vertex is `x`.
- The old reverse connector `Q1` is direct, so `|Q1|=1`.
- `fleet01/B04` gives, unless a bypass already appears, a fresh direct packed cross. Relabel `A,B` if needed so it supplies the second forward connector `P2`; hence `|P2|=1`. Endpoint collision is kept as an explicit residual branch, not silently excluded.
- `fleet03/B05` gives either third-support mediation or a fresh reverse connector `Q2` whose endpoints avoid the old reverse endpoints and whose interior is in `R`.
- If `Q2` meets `x`, Lemma 1 already gives a same-support bypass. Hence in the no-bypass branch `Q2` avoids `x`. Because `|R|=4`, `Q2` then has at most three internal remainder vertices, so `|Q2|≤4`.

Therefore, whenever the four ports are distinct and the cyclic compatibility lemma supplies a legal matching,

`L_X ≤ 2+1+1+4 = 8`,

and Lemma 2 yields the exact collar

`G_A+G_B ≤ 8`.

Equivalently, any splice-compatible 2x2 state with `G_A+G_B≥9` is impossible in a globally minimum three-packing.

This is the new universal movement: the `R`-internal fresh-port branch is no longer an unstructured “four paths may reuse vertices” problem.

## Before / after

**Before.** One opposite connector pair has rank one. A fresh direct cross and a fresh reverse path exist, but the proof had no general way to control reuse or determine when four ports form two legal directed replacement cycles.

**After.** In the live four-remainder branch, the fresh system falls into the following explicit list:

1. same-support BYPASS, if the fresh reverse path intersects the old opposite connector internally;
2. endpoint collision;
3. third-support `C` mediation from the 3-connectivity construction;
4. grouped cyclic port order on at least one support;
5. alternating port orders with mismatched matching parity;
6. splice-compatible system with the exact collar `G_A+G_B≤8`;
7. otherwise a strict two-cycle splice contradicts global minimum.

This is target-relevant mechanism progress, but cases 2–6 are not yet universally closed.

## First unpaid universal step after this run

`BT4-FRESH-PORT-PARITY-COLLAR-WALL`:

For every finite loopless digraph in the source model with `δ^+≥7`, in the globally minimum three-packing / acyclic `|R|=4` clean-port state described above, prove that each of the residual branches

- endpoint collision,
- grouped port order,
- alternating parity mismatch,
- splice-compatible collar `G_A+G_B≤8`, or
- explicit third-support `B→C→A` mediation

forces at least one of:

(a) two vertex-disjoint genuine directed replacement cycles giving a strict three-packing reduction;
(b) a directed cycle in the exchanged remainder;
(c) a SIX/fan state already covered by the existing closure machinery; or
(d) a fourth genuine directed cycle vertex-disjoint from the retained packed cycles.

All quantifiers are universal over graph order and over all globally minimum three-packings satisfying the live branch hypotheses.

## Next method / stagnation

No three-run stagnation trigger applies: the mechanism changed materially in response to the newly exposed rank-one/fresh-port obstruction. The next method is to attack the localized port wall by cyclic word and shortest-mixed-cycle descent:

1. grouped `XXYY`: take the shortest mixed cycle determined by the two inner ports and apply the fresh-source cross theorem; test whether its fresh source necessarily breaks the grouping or creates a strict bypass;
2. parity mismatch: compare the two unique admissible matching parities and use the first cross-chord along the shorter support gap to force a shorter mixed cycle;
3. collar `≤8`: perform a finite **symbolic gap case split only**, not finite graph search, retaining arbitrary graph order and using minimum-packing inequalities to eliminate each gap word;
4. third-support mediation: close through the shortest `B→C→A` mediator and reduce back to the same 2x2 port language or to a genuine four-cycle packing.

## Integrity / privacy

No credentials, scheduler identifiers, machine paths, raw private transcripts, unrelated private data, broad mixed-domain memory, or plaintext benchmark gold are present. Existing artifacts and histories were not modified. No brain installation, benchmark generation, paid API/model, email, Drive, public posting, remote workflow, permission change, or other-account authentication was used.
