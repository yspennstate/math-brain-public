# BT4 report — shortest-cycle fresh-cross parity trap

Run: `20260922T074352Z-account03-B05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: `account03/B05`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-SHORTEST-CROSS-PARITY-TRAP-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and exact assignment

Target: every finite loopless simple digraph of minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs are allowed and digons count.

Exact B05 assignment: prove the disjointness-preserving exchange promised by the current two-partition or linkage candidate; averages do not replace minimum-degree hypotheses. Assigned partner: `account04/B06`.

No full BT4 proof is claimed here.

## 2. Exact inherited state actually consumed

### Assigned partner — account04/B06

Applied `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, shared handoff Git blob `47d7e7c2fd312fd647604bf61113c46fd980a237`; canonical report commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`, report blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`.

The partner proves, in the inherited 3-vertex-strong normal form with packed cycles `A,B,H` and acyclic remainder `R`, that each ordered light-support direction has a rank-two remainder linkage unless third-support mediation occurs. Opposite-direction remainder intersections emit a same-support bypass or a bounded short-support event. Therefore, in the all-long/no-bypass/no-`H`-mediation residual, connector rank and remainder-intersection debts are paid and the first debt is packed-port cyclic order / endpoint compatibility.

### Shortest mixed-cycle input — account01/B04

Applied `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, shared handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`, canonical report blob `84a4f2e7929cbe4844f2421240a3dc8eb822d431`.

Let a shortest mixed cycle be

`K = F0 + B[beta0,gamma0] + G0 + A[delta0,alpha0]`,

where `F0` is an `A->B` connector from `alpha0` to `beta0`, and `G0` is a `B->A` connector from `gamma0` to `delta0`. The theorem forces either a same-support remainder bypass or a packed cross whose source lies outside `K`. In the direct `A->B` cross case write that fresh cross as

`F1 : alpha1 -> beta1`.

Because its source is outside `K` and its target is a packed hit on `K`, in the distinct-port case the cyclic positions satisfy

`alpha1 in int A[alpha0,delta0]`,

`beta1 in int B[beta0,gamma0]`.

The symmetric statement holds if the fresh cross is `B->A`.

### Exact cyclic-order criterion — account04/B05

Applied the support-order criterion from `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1`, shared handoff blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`, canonical report blob `47bb1d2b3a2d01f6821e639310290557b3a54bc2`: for two `A->B` connectors `F_i:alpha_i->...->beta_i` and two `B->A` connectors `G_j:gamma_j->...->delta_j` whose interiors/endpoints are otherwise disjoint, two vertex-disjoint mixed replacement cycles exist exactly when endpoint types alternate on both supports and the unique support pairings agree.

## 3. New theorem — shortest-cycle fresh-cross parity trap

### Statement

Assume the distinct-port, pairwise-interior-disjoint branch above. Let

`K = F0 + B[beta0,gamma0] + G0 + A[delta0,alpha0]`

be the working shortest mixed cycle. Suppose the deletion/shortest-cycle mechanism produces a fresh direct `A->B` cross

`F1 : alpha1 -> beta1`

with source outside `K` and target on the `B` support trace of `K`, so

`alpha1 in int A[alpha0,delta0]`,
`beta1 in int B[beta0,gamma0]`.

Then **no single additional reverse connector**

`G1 : gamma1 -> ... -> delta1` (`B->A`)

with fresh packed endpoints and interior disjoint from `F0,F1,G0` can make the four connectors `F0,F1,G0,G1` into two vertex-disjoint mixed replacement cycles.

Equivalently: in this exact shortest-cycle fresh-source geometry, rank two in the opposite direction is not merely potentially insufficient; its pairing parity is forced to disagree with the pairing parity on the other support whenever endpoint alternation is possible.

The symmetric theorem holds when the shortest-cycle output is a fresh direct `B->A` cross.

### Proof

Assume for contradiction that the four connectors can be paired into two vertex-disjoint mixed cycles.

On `A`, the cyclic order of the three already fixed ports is

`alpha0, alpha1, delta0`

because `alpha1` lies on the complementary `A` arc from `alpha0` to `delta0`, while `K` uses `A[delta0,alpha0]`.

For two directed `A` support segments from the reverse endpoints `delta0,delta1` to the forward endpoints `alpha0,alpha1` to be disjoint, endpoint types must alternate. Therefore the only possible location of `delta1` is

`delta1 in int A[alpha0,alpha1]`.

In that alternating order

`alpha0, delta1, alpha1, delta0`,

the unique disjoint pairing on `A` is

`G0 with F0`, and `G1 with F1`.

Indeed the disjoint directed `A` segments are `A[delta0,alpha0]` and `A[delta1,alpha1]`.

Now inspect `B`. Since `beta1` is a distinct packed target on the `B` trace of `K`, the fixed cyclic order is

`beta0, beta1, gamma0`.

Again endpoint alternation is necessary. Hence the only possible location of `gamma1` is

`gamma1 in int B[beta0,beta1]`.

The alternating order is then

`beta0, gamma1, beta1, gamma0`.

But the unique disjoint pairing on `B` is now

`F0 with G1`, and `F1 with G0`,

because the disjoint directed `B` segments are `B[beta0,gamma1]` and `B[beta1,gamma0]`.

Thus `A` forces the identity pairing while `B` forces the transposed pairing. No single permutation can satisfy both supports. This contradicts the existence of two vertex-disjoint mixed replacement cycles.

If `delta1` or `gamma1` lies anywhere else, endpoint types fail to alternate on the corresponding support, so the splice is already impossible there. Therefore no placement of a fresh, distinct-port reverse connector closes the splice. QED.

The `B->A` fresh-cross case is obtained by interchanging `A` and `B` and reversing the connector labels.

## 4. Exact application to the assigned partner result

Account04/B06 proves that the pure long-support/no-bypass/no-third-support branch cannot stay at reverse connector rank one: a second reverse route exists (or `H` mediation occurs). The theorem above shows that, when the new forward cross is the shortest-cycle fresh-source output, **that rank-two reverse route alone cannot be the missing disjointness-preserving implication**.

Therefore the former hoped-for arrow

`fresh source CROSS + fresh reverse connector -> two-cycle splice`

is false in the distinct-port shortest-cycle geometry.

The correct next mechanism must change the port signature, not merely increase reverse rank. At least one of the following must be forced:

1. a new `A->B` connector whose source/target is not in the shortest-cycle fresh-source quadrant (a side-switching forward connector);
2. a packed-endpoint collision that supports a separate exchange/short-support argument;
3. a same-support remainder bypass;
4. third-support (`H`) mediation;
5. SIX / bounded short-support exit.

The assigned partner's three-linkage theorem makes (1) the natural next attack: use the third Menger path, not another copy of reverse rank two, and prove that it either side-switches or forces one of (2)--(5).

## 5. Local countermodel to the discarded linkage-only implication

The parity obstruction is not a proof-artifact. At the pure port-system level take cyclic orders

`A: alpha0, delta1, alpha1, delta0`,

`B: beta0, gamma1, beta1, gamma0`,

and let all four connectors be pairwise vertex-disjoint (they may even be direct). The fresh-cross source `alpha1` lies outside the `A` trace of `K`, while `beta1` lies on the `B` trace. Both supports alternate, but `A` uniquely requires the identity pairing and `B` uniquely requires the transposition. Hence there are no two vertex-disjoint mixed cycles using exactly these four connectors.

This is an exact countermodel to the **local linkage-only implication**. It is not asserted to be a minimum-outdegree-seven BT4 counterexample and is not used as one.

## 6. First unpaid implication after this run

`BT4-THIRD-LINKAGE-SIDE-SWITCH-v1`:

> In the aligned four-remainder heavy-triangle long-support state, combine the partner's three vertex-disjoint Menger paths in the fresh-cross direction with the shortest-cycle geometry. Prove that the third path either has a side-switched packed-port signature relative to `K`, has a productive packed-endpoint collision, is `H`-mediated, or emits a same-support bypass / SIX / bounded short-support exit. If a side-switched connector exists, combine it with the rank-two opposite linkage and the exact cyclic-order criterion to obtain a legal two-cycle reconstruction and apply the minimum-packing tax.

This is strictly narrower than the previous generic `RANK2-PORT-ORDER` debt: one whole proposed mechanism (adding only an opposite fresh connector) is now ruled out, and the next required object is a side-switching third linkage or an explicit structural exit.

Global campaign debts remain separate: SIX/H5 closure, bounded F2/F3 states, and the support-carried seven-remainder branch.

## 7. Honesty and scope

Classification: `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

No authenticated brain retrieval/context was used; `WITHOUT_VERIFIED_BRAIN` is preserved. No scheduler mutation, email, Drive, public posting, paid API/model, Codex, remote workflow, credential use, or cross-account native action occurred. This report contains only scoped graph-theoretic mathematics and artifact provenance.
