# BT4 handoff — account04/B05 gap-signature invariance and two-cross parity gate

Run: `b05-20260922t100847z-r34`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Canonical scientific report: `yspennstate/math-open-problems:proofnet24/collective-BT4/account04/B05/b05-20260922t100847z-r34/report.md`, blob `fd5055a18e9374ba0d4edafd0a7c849f031848f0`, creation commit `ec0c18cada93ea0d963f1c8f0f97c4d59816c882`.

## Applied inputs

- Latest complete lead: account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.
- Named OTHER-account result: account01/B06 `BT4-R4-DIRECT3X3-NONTRANSPOSE-v1`, followed by `BT4-R4-DIRECT3X3-SWITCH-CLASSIFICATION-v1`.
- Compatible forcing input: account03/B04 `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`, which supplies a fresh-source direct cross unless a bypass/third-support exit already occurs.

## New exact result

Fix the reverse direct-cross triple `G_j: gamma_j -> delta_j`. The `delta_j` cut A into three source gaps and the `gamma_j` cut B into three target gaps. A fully alternating forward triple is therefore a permutation `m` from A-gaps to B-gaps. In the surviving direct-3x3 branch, `m` is a 3-cycle.

**ONE-FRESH-GAP-INVARIANCE.** Replacing exactly one selected forward cross `F_r` by a fresh direct cross while preserving distinct endpoints and full alternation forces the replacement to occupy the unique vacated source gap `r` and the unique vacated target gap `m(r)`. Thus the monodromy remains exactly `m`. A single fresh cross cannot change the residual 3-cycle class by one-for-one alternating reselection.

**TWO-FRESH-PARITY-BREAK.** For distinct `r,t`, if two vertex-disjoint usable fresh direct crosses occupy complementary swap cells `(r,m(t))` and `(t,m(r))`, then replacing `F_r,F_t` preserves full alternation and changes the monodromy to `m o (r t)`, a transposition. The account01/B06 nontransposition theorem then excludes this configuration in the unresolved globally minimum state.

Hence, for each unordered pair `{r,t}`, the two complementary swap cells cannot simultaneously have vertex-disjoint usable representatives. Dependencies are explicit; no independent-choice assumption is used.

An exact finite verification of the one-cross theorem over normalized cyclic port classes gave:

```
normalized_3cycle_classes = 8
fresh_source_target_gap_insertions = 288
one_for_one_replacements_preserving_full_alternation = 96
still_3cycle_monodromy = 96
identity_or_transposition_after_one_replacement = 0
```

## First unpaid implication

`BT4-R4-TWO-FRESH-CROSS-DIVERSITY-v1`: use exact outdegree seven, global NO-SIX, and the R4 cage/fan constraints to force either a second vertex-disjoint fresh cross in a complementary swap cell, or a productive endpoint collision/nonalternating 2x2 splice, or a same-support bypass, H/third-support mediation, SIX, short support, strict packing decrease, or cyclic exchanged remainder.

Do not assume the second cross is independent of the first. The two-cross theorem identifies the exact pairwise dependence to be paid.
