# POS3 account02/B19 — sharp two-distinguisher lower-transport adversary

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair with uniform-linear-extension probability in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current collective state actually used

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; no brain-installation or benchmark work was resumed.

The latest complete campaign-lead version consumed is account04/B10,
`proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `b077c3fedba7e6e8ab72b683b5eafd8203005467`.  Its delayed-predecessor funnel proves that the first-fork sibling predecessor sets are nested and that the strict branch either descends to a shorter extreme pair or continues through a new canonical successor Hasse blocker.

The essential newer team dependency is account04/B19,
`proofnet24/collective-POS3/account04/B19/B19-20260922T031150Z-r46/REPORT.md`, blob `9079d05dcdf18d3afdb391d39148ed8c4653768d`.  It proves that the equal-predecessor clean-fork branch cannot escalate forever: after finitely many Hasse ascents it reaches an extreme incomparable pair with unequal predecessor sets.  Together with account02/B10's one-distinguisher theorem, the live module-prime residual therefore starts at an extreme pair with **at least two distinguishers and at least one lower distinguisher**.

The named partner result actually consumed and applied is account03/B10,
`proofnet24/collective-POS3/account03/B10/20260922T0214Z-a03-b10-r11/REPORT.md`, blob `3e50b4d0adaa18c79a96079139d660b832418a2d`.  It places every hypothetical counterexample in the exact-uniform rank-variance exceptional regime (`Var(rank(x))<6560`) and preserves the `>1/81` pinned-rank input.  The adversary below lies safely inside that quantitative regime (indeed a 15-point rank variable has range at most 14), and its chosen asymmetric three-chain cover has every pinned two-coordinate cell strictly above `1/81`; those conditions therefore do not by themselves settle the new two-distinguisher residual.

## 2. Compact conditional end-to-end route and first missing implication

Assume POS3 is false and take a cardinality-minimal counterexample.  The current team reductions give width exactly three, connected incomparability graph, a transitive strong-majority order, and a first-boundary fork.  Clean equal-predecessor escalation terminates, so the next genuinely unpaid branch is:

> **Lower-distinguisher transport.**  Starting with an extreme incomparable pair `(u,v)` having at least two relation distinguishers and at least one lower distinguisher, use width three plus the full heavy-slice / TP2 / delayed-distinguisher geometry to force a balanced pair or another strict descent.

A tempting strengthening of account02/B10's exact one-distinguisher theorem would be that the minimal two-distinguisher configuration is already balanced, or at least bounded away from the `2/3` threshold by a uniform positive margin.  The exact construction below refutes that shortcut as sharply as the integer count permits.

## 3. Exact width-three adversary

Take the 15-point poset whose transitive reduction is

`0<1, 0<10, 1<2, 2<3, 2<12, 3<4, 3<9, 5<6, 6<2, 6<11, 7<3, 7<8, 7<13, 8<4, 8<9, 9<14, 10<6, 11<7, 11<12, 12<8, 12<13, 13<4, 13<14`.

The authoritative verifier enumerates every linear extension with weight one.  It obtains exactly

`E = 1810`

uniform linear extensions, width exactly three (witness antichain `(1,5,10)` and no four-antichain), connected incomparability graph, 17 incomparable pairs, and **no nontrivial proper autonomous subset**.

All strict simple-majority orientations are transitive, with total order

`L_maj=(0,5,10,1,6,11,2,7,12,3,8,13,9,4,14)`.

There are five balanced incomparable pairs, so this is not a POS3 counterexample.

## 4. Sharp lower-distinguisher pair

The decisive pair is `(3,13)`.  Its exact uniform probability is

`Pr(3 precedes 13) = 1207/1810 = 2/3 + 1/5430`.

Equivalently,

`3*N(3<13) - 2E = 3*1207 - 2*1810 = 1`.

Because the left side is an integer, this is the **smallest possible positive slack** above the `2/3` threshold for a poset with `E=1810` extensions.

The pair has exactly two relation distinguishers:

- lower distinguisher `12`, with `12<13` and `12||3`;
- upper distinguisher `9`, with `3<9` and `9||13`.

More strongly, the entire predecessor/successor discrepancy is exactly

`Pred(13)=Pred(3) union {12}`,

`Succ(3)=Succ(13) union {9}`,

and `12<9`.  Thus this is the smallest possible two-sided distinguisher geometry: one lower and one upper witness, with no hidden third distinguisher.

This is a source-valid counterexample to the shortcut

> “an extreme pair with the minimum two distinguishers, including a lower distinguisher, must already be balanced (or must have a fixed positive margin away from the balance threshold).”

It need not be balanced: here it is strong, and it misses `2/3` by only the arithmetically minimal one-count slack.

Therefore the current lower-distinguisher transport cannot close by counting distinguishers or by predecessor/successor-set asymmetry alone.  It must use the *placement and flux interaction* of the lower and upper distinguishers, the delayed-distinguisher span, or a global TP2/heavy-slice conservation law.

## 5. Asymmetric-chain and selector checks

The verifier exhaustively enumerates all unlabeled three-chain covers of this poset: there are exactly `1536`.  Eight covers have the extreme size profile `(2,5,8)`.  One exact asymmetric cover is

`C0=(0,10,6,2,12,8,9,14)`,

`C1=(1,3)`,

`C2=(5,11,7,13,4)`.

For that cover, with the same simple-majority order, the exact path-system selector has 24 relevant one-chain rows, 10 cumulative-band failures, and every pinned two-coordinate cell exceeds `E/81`; the smallest pinned cell is `402/1810 = 201/905`.

Thus the new lower-distinguisher obstruction is compatible with a highly asymmetric width-three chain cover and with the team's pinned-cell quantitative regime.  The failure is not an artifact of an equal `5+5+5` cover.

Finally, for any `s,t>=0`, the ordinal sum

`C_s ordinal-sum P ordinal-sum C_t`

has width three and exactly the same 17 incomparable-pair probabilities: the prefix and suffix chains have unique internal orders and are comparable with every point of `P`.  In particular the exact pair `(3,13)` remains a two-distinguisher pair with probability `1207/1810`.  This supplies arbitrary finite sizes without treating a finite census as closure.  (The padded examples are not claimed module-prime; the 15-point core itself is connected and module-prime.)

## 6. Exact verification and failure boundary

Authoritative verifier: `verify_sharp_two_distinguisher.py`.

- execution SHA-256: `3f39eedb954c9d2f8b4dcbef6c8c16eb94ebaa1b86812b520ed2800250959345`
- exact captured output SHA-256: `6914bda62e1b6743c78869519e4e2202ae57c3b3a5a38864e1f565d0241cc7eb`
- terminator: `POS3_SHARP_TWO_DISTINGUISHER_PASS`

The output records the exact probability of every incomparable pair and independently verifies width, connectedness, module-primality, transitive simple-majority order, all 1536 three-chain covers, the extreme asymmetric cover, the two distinguisher sets, and the one-count threshold slack.  No sampling, random-vector surrogate, or induced nonuniform deletion law is used for any probability claim.

The discovery search was heuristic; it is not part of the proof.  Every mathematical claim promoted here is rechecked from the displayed transitive reduction by the deterministic exact verifier.

## 7. Status and next implication

**Classification:** `CANDIDATE_REFUTED` for the two-distinguisher/local-asymmetry shortcut; **POS3 remains OPEN**.

The first source-valid missing implication is now sharper:

> starting from a strong pair whose predecessor sets differ by one lower distinguisher and whose successor sets differ by one upper distinguisher, prove a global transport statement strong enough to force balance/descent despite the fact that the pair can sit at `2/3 + 1/(3E)`-scale slack.

A useful next attack is to write the exact two-gap deletion polynomial for this one-lower/one-upper geometry and identify which signed term is forced by width-three TP2.  Any successful theorem must use more than the number of distinguishers, since the minimum count `2` is already compatible with an arithmetically sharp strong pair.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex call, remote workflow, public posting, permission change, or verified production-brain retrieval was used.
