# POS3 fleet01/B10 — no chain-cover choice eliminates nested third-chain defects

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact state consumed

This run continues the owner-selected POS3 workstream and does not perform benchmark or FEI work.

The named other-account partner result consumed is **fleet02/B11**, report

`proofnet24/collective-POS3/fleet02/B11/20260921T235736Z-b11-44e20585/REPORT.md`, blob `b71c5087c4982769946c31f1ec76242bf297fe17`.

It proves exact ordinal factorization by connected components of the incomparability graph. Hence a cardinality-minimal counterexample may be taken incomparability-connected; together with the inherited state, it has width exactly three, at least 15 elements, and at least five maximal chain blocks in the transitive strong-majority order.

I also use the following exact collective inputs.

- fleet01/B10, prior report blob `3a0d4e63665646adc853bb48192eba0f81629a15`: the exact three-chain ideal-state path encoding, the flux identity
  `Pr(x<c_{b,s}) = E^{-1} sum_{t<s} W_{x,b}(t)`, and the heavy-slice normal form `W_{x,b}(g_b(x))>E/3` in a hypothetical counterexample.
- fleet01/B19, report plus blocker-defect addendum: after deleting a chain `C`, the exact projected weight is the corridor multiplicity `W_C(tau)`. For an adjacent incomparable swap with endpoint-ordered `C`-profiles, the swap sign is context-independent and the weight defect is exactly a chain-blocker union. **Only strictly nested profiles can have context-dependent swap sign.**
- fleet03/B11, report blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d`: every adjacent strong-majority boundary in a width-three counterexample has a double-blocker certificate; a purely one-boundary local closure is false.
- fleet04/B19 as consumed by fleet03/B11: a cardinality-minimal counterexample has no proper autonomous nonchain; in particular the module-reduced core is the relevant setting.

At the checked archive state the named team-lead root `fleet04/B10` still had no complete source-bound POS3 report, so the current candidate was reconstructed from the completed peer results above rather than fabricating a lead version.

## 2. Compact conditional route and the first structural escape to test

Fix a width-three minimal counterexample `P` and a three-chain cover

`P=C_1 disjoint_union C_2 disjoint_union C_3`.

Delete one chain `C` and put `Q=P\C`, so `width(Q)<=2`. The actual uniform law on `L(P)` projects to the exact weighted law

`mu_C(tau)=W_C(tau)/sum_sigma W_C(sigma)`

on `L(Q)`.

For `q in Q`, write

`I_C(q)=[lambda_C(q),rho_C(q)]`,

where `lambda_C(q)` is the number of forced chain predecessors and `rho_C(q)` the last allowed chain-prefix count before `q`. The fleet01/B19 recurrence proves:

1. if two adjacent incomparable elements of `Q` have endpoint-ordered profiles, their projected swap has a context-independent sign and an explicit injection;
2. a swap can change sign with the outer insertion context **only when the two intervals are strictly nested**.

This makes the following structural lemma a natural possible escape from the nested-defect problem.

> **Nesting-free deletion candidate.** Every connected, module-reduced width-three poset admits some three-chain cover and some chain `C` in that cover such that no incomparable pair in `P\C` has strictly nested `C`-profiles.

If true, it would remove the only context-sensitive local swaps by choosing the chain cover/deletion intelligently, leaving a weighted width-two problem with only the already-controlled endpoint-ordered defects.

The main result of this run is that this candidate is false in a particularly strong finite form.

## 3. A 9-element connected module-prime counterexample to nesting-free deletion

Let `P_9` be the poset on `{0,1,...,8}` whose transitive reduction has the ten covers

`0<1`, `0<3`, `1<4`, `1<5`, `2<5`, `3<5`, `4<7`, `5<6`, `5<8`, `6<7`.

All displayed relations are oriented from the smaller label to the larger label, so the natural labels give a topological order.

### Theorem 3.1 — every chain deletion in every three-chain cover has a nested incomparable profile pair

`P_9` has width exactly three, connected incomparability graph, and no nontrivial proper autonomous subset. Moreover, for **every** partition of `P_9` into three chains

`P_9=C_1 disjoint_union C_2 disjoint_union C_3`

and for **every** `r in {1,2,3}`, there exist incomparable `u,v in P_9\C_r` such that

`I_{C_r}(u) proper_subset I_{C_r}(v)`

or

`I_{C_r}(v) proper_subset I_{C_r}(u)`.

Thus no choice of three-chain cover and no choice of deleted chain eliminates the context-sensitive nested-profile mechanism.

### Exact finite certificate

A chain is precisely an independent set in the incomparability graph. Therefore unordered partitions into three chains are exactly proper three-colorings of that graph modulo color permutation. Since `width(P_9)=3`, all three color classes are nonempty.

The verifier exhaustively enumerates those colorings and finds exactly `16` distinct unordered three-chain covers. For every one of the `16*3=48` possible deleted-chain choices it computes every interval profile and every incomparable pair in the remaining two-chain poset. Every one of the 48 choices contains at least one strictly nested incomparable profile pair. The minimum number of such pairs over all deleted-chain choices is exactly `1`.

The same exact verifier checks:

- width `3`, with antichain witness `{1,2,3}`;
- connected incomparability graph;
- zero proper autonomous subsets of size `2,...,8`, so the example is stronger than merely having no autonomous nonchain;
- `109` uniform linear extensions.

Hence the counterexample survives both of the principal structural reductions already available to the collective POS3 proof: incomparability-connectedness and module reduction.

## 4. This is not a counterexample to POS3

The example is deliberately a counterexample only to the nesting-free-deletion lemma, not to the parent conjecture. Exact enumeration of all `109` linear extensions gives balanced pairs including

`Pr(1<2)=48/109`,

`Pr(1<3)=62/109`,

`Pr(2<3)=67/109`,

`Pr(4<5)=45/109`,

`Pr(6<8)=70/109`.

Thus `P_9` satisfies POS3. Its role is to show that a proof cannot dispose of nested insertion profiles merely by optimizing the Dilworth three-chain cover or by first reducing to a connected/module-prime core.

## 5. Why this directly changes the surviving proof route

The previous chain-deletion analysis had isolated nested profiles as the sole source of context-dependent adjacent-swap sign. Before this run there was still a possible structural shortcut: perhaps a suitable chain cover/deletion made nested profiles disappear in the reduced core.

Theorem 3.1 closes that shortcut. Even at nine elements, before any hypothetical counterexample behavior is imposed, connectedness plus complete module-primality does not provide a nesting-free deletion; in `P_9`, **all 48** cover/deletion choices retain a nested incomparable pair.

Therefore any end-to-end chain-deletion proof of POS3 must actually control the signed nested-profile defects. It cannot assume they can be removed by choosing a better chain cover.

The first essential surviving implication is consequently the following genuinely weighted statement.

> **Global nested-defect cancellation/charge problem.** For a three-chain cover of a hypothetical width-three counterexample, after deleting a chain `C`, sum the exact adjacent-swap defects of `W_C` along the width-two path/exchange argument. Endpoint-ordered swaps already have the correct fixed sign and exact blocker-union formula. Prove that the **context-dependent signed contributions from nested profile swaps**, when summed over the relevant width-two path boundary, can be charged to actual `C`-involving pair events strongly enough to force a probability in `[1/3,2/3]`.

The present counterexample shows that this nested term is indispensable; it is not a removable artifact of a poor chain cover.

A useful exact local variable for the next step is the fleet01/B19 truncated midpoint displacement

`Delta_{L,U}=(gamma-alpha)+(delta-beta)`

for the two truncated profile intervals in an outer prefix window `[L,U]`. For nested profiles `Delta_{L,U}` can change sign with `[L,U]`. The next proof must therefore retain the joint outer-prefix distribution and seek cancellation of the signed short-gap bands, rather than replace each profile by one scalar weight or select another deletion chain.

## 6. Reproducibility

Authoritative verifier:

`verify_no_nestingfree_deletion.py`

Git blob: `5b01974eb9041ed3e68daca5cf472c513693c676`.

The exact checker uses only integer/transitive-closure enumeration, exhaustive subset tests, exhaustive three-colorings of the incomparability graph, and exact rational linear-extension probabilities. Its independently recorded local SHA-256 before upload was

`ca16d66b45478487e99413e091fecd6060e133261605cc784ebc86774c14f742`.

Authoritative output:

`verify_output.txt`

Git blob: `514b0e6306e7200fc88e4c4232b06c4c93811cfb`.

Its independently recorded local SHA-256 before upload was

`f12263f9cfef3a32b76199563f651166edd5838bfa7c794d8cae7ba1b33d4ee9`.

Terminal certificate:

`POS3_NO_NESTING_FREE_DELETION_COUNTEREXAMPLE_PASS`.

The finite computation certifies only the explicitly stated structural counterexample and exact probabilities; it is not evidence that POS3 itself is false.

## 7. Claim status

- Exact three-chain path/flux representation: inherited **PROVED**.
- Incomparability-component reduction from fleet02/B11: inherited **PROVED** and applied.
- Endpoint-ordered versus nested swap dichotomy from fleet01/B19: inherited **PROVED** and applied.
- `P_9` is width three, incomparability-connected and has no proper autonomous subset: **EXACTLY VERIFIED**.
- Every chain in every three-chain cover of `P_9` leaves a nested incomparable profile pair after deletion: **EXACTLY VERIFIED** over all 16 covers / 48 deletions.
- Nesting-free deletion candidate: **REFUTED**.
- Parent width-three 1/3–2/3 target: **NOT PROVED**.

No novelty or priority claim is made. No benchmark material, FEI proof content, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive action, paid model/API/Codex call, remote workflow, public posting, or permission change was used.
