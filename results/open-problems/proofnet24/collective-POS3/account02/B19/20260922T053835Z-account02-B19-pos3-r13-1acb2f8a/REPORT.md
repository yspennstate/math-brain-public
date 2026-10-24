# POS3 account02/B19 — two-channel heavy-edge overlap adversary

**Run:** `20260922T053835Z-account02-B19-pos3-r13-1acb2f8a`  
**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run obeys `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; it performs no installation or benchmark work. Every probability below is under the actual uniform law on all full linear extensions of the displayed poset.

## 1. Exact source state consumed

Fresh owner control was revision `2026-09-22.2`. The latest complete campaign-lead report consumed is:

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, report blob `50bac494667235f3630991a512438eac42c30521`.

Its new bridge theorem says: in the lead's majority-late bridged branch, if `c<u`, `c||a`, `u||a` and `c prec_* a prec_* u`, then every saturated chain from `c` to `u` contains a unique cover `x lessdot y` for which

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`, and `Pr(x<a<y)>1/3`.

Together with account01/B19's Cover Two-Witness Theorem, the lead concludes that such a heavy cover edge must have at least two distinct external relation-distinguisher channels in any hypothetical no-balanced counterexample. Its first unpaid step is a **two-channel heavy-edge recycling theorem**: the `>E/3` edge mass and its forced witness channels cannot recycle indefinitely without a balanced pair, span descent, an autonomous reduction, or a controlled multi-distinguisher/non-crossed exit.

The named partner actually consumed is:

- account03/B10, `proofnet24/collective-POS3/account03/B10/20260922T051823Z-account03-B10-r11/REPORT.md`, report blob `8413593b751695eba06afe73a83ca2ad09e1c191`.

For first-element deletion it proves the exact projected law `d mu/d nu=(kappa+1)/M`, with `nu` uniform on the deletion poset and `mu` the actual law inherited from the original uniform extension measure. It proves every deletion-balanced pair retains actual minority `>4/27` and localizes all such pairs to strong-majority distance at most `3786`; the remaining `BR3786-SH741` obligation is adaptive covariance transfer, not a bounded-density estimate.

I also use the account01/B19 exact three-chain flux / Cover Two-Witness result from `proofnet24/collective-POS3/account01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`: a strong cover flip in a no-balanced poset forces at least two external distinguishers after the cover endpoints are removed.

The immediate account02/B19 predecessor is `proofnet24/collective-POS3/account02/B19/20260922T051105Z-account02-B19-pos3-r12/REPORT.md`, blob `1faad20ca2758064e9c3634cf089f9da969ec841`, which showed that all three local majority-late blocker channels can be support-essential in a connected autonomous-prime width-three core. The present run changes mechanism: it attacks the new lead's **global heavy-cover charge interface** and the partner's exact deletion tilt in one common core.

## 2. Conditional end-to-end route and tested implication

Assume POS3 is false and take a cardinality-minimal no-balanced width-three candidate. The current route now reaches a cover `x lessdot y` and point `a||x,y` with a literal heavy-gap event

`H={x<a<y}`, `|H|>E/3`.

The Cover Two-Witness Theorem forces at least two external relation channels. A tempting next implication is that these two channels can immediately absorb the heavy gap locally, for example by charging each heavy-gap extension into one of the two canonical witness-minority events. If that were always possible, repeated heavy edges would produce a non-overlapping target-scale charge without further global geometry.

The construction below refutes that local unit-charge implication, even under connectedness and autonomous-primality. The same core simultaneously refutes fixed-pair stability under the partner's deletion tilt even when `W<=2` everywhere and there is no deep tail at all.

Neither result refutes the lead theorem, the partner theorem, or POS3. They sharpen the first essential missing implication to a genuinely **global adaptive anti-overlap transfer theorem**.

## 3. Exact width-three autonomous-prime core

Let `P` have vertices `0,...,10` and transitive-reduction covers

`0<1, 0<5, 1<2, 1<6, 1<10, 2<3, 4<1, 4<5, 5<3, 5<6, 6<7, 8<9, 8<0, 9<5, 9<10, 10<3, 10<7`.

An explicit three-chain cover is

`(0<1<2<3)`, `(4<5<6<7)`, `(8<9<10)`,

and `{0,4,9}` is a 3-antichain, so the width is exactly three. The incomparability graph is connected. Exhaustive checking of every proper nontrivial subset finds **no nontrivial autonomous subset**, so this core is autonomous-prime.

Exact enumeration gives

`E=e(P)=515`

uniform linear extensions.

## 4. The lead's heavy-cover interface is realized sharply

Take

`x=5`, `y=6`, `a=10`.

The relation `5 lessdot 6` is a cover and both `5||10` and `6||10`. Exact counts give

`Pr(5<10)=374/515 > 2/3`,

`Pr(6<10)=161/515 < 1/3`,

and therefore

`Pr(5<10<6)=213/515 = 374/515-161/515 > 1/3`.

The exact relation-distinguisher sets are

`D(5,10)={1,6}`,
`D(6,10)={3,5}`.

After deleting the unavoidable cover endpoints, the external witness union is **exactly**

`{1,3}`.

Thus the account01/B19 / lead lower bound of two external channels is attained with equality.

Moreover every incomparable pair inside the natural heavy-edge-plus-witness block `{1,3,5,6,10}` is unbalanced:

`Pr(1<5)=387/515 >2/3`,
`Pr(3<6)=88/515 <1/3`,
`Pr(5<10)=374/515 >2/3`,
`Pr(6<10)=161/515 <1/3`.

So connectedness, autonomous-primality, a literal `>E/3` heavy gap and exactly two forced witnesses do not produce a balanced pair inside the local five-vertex block.

## 5. Direct local unit charging is cardinality-impossible

For the two external witnesses, the natural minority events are

`A={5<1}`, with `|A|=128`,
`B={3<6}`, with `|B|=88`.

Their overlap is `|A intersect B|=16`, hence

`|A union B|=128+88-16=200`.

But the heavy gap has

`|H|=213`.

Therefore

`|A union B|=200 < 213=|H|`.

No injection can charge each heavy-gap extension to one of these two witness-minority events with unit capacity. More sharply, restricted to the 213 heavy-gap extensions, the exact `(A,B)` patterns are

- neither: `105`;
- `A` only: `56`;
- `B` only: `36`;
- both: `16`.

So **105/213 of the heavy-gap extensions lie in neither natural witness-minority event**.

This refutes the following local strengthening of the current selector:

> `LOCAL-TWO-WITNESS-UNIT-CHARGE`: once a heavy cover gap `H` and its two forced external witnesses are found, the heavy-gap mass can be absorbed locally into the union of the two corresponding witness-minority events by a unit-capacity charge.

The lead's actual two-channel recycling theorem is stronger and global, so it is not refuted. What fails is the simplest local realization of its charge.

## 6. Named-partner deletion tilt fails on a fixed pair even with W<=2 everywhere

The same poset gives a very shallow exact first-element deletion example. Delete the minimal element

`c=8`.

Then `Q=P\{8}` has exactly `376` uniform linear extensions. The set incomparable with `8` is

`S={4}`.

Hence for every `tau in L(Q)`, the partner's insertion multiplicity is

`W(tau)=kappa(tau)+1 in {1,2}`.

There is **no deep tail at all**. The exact total weight is `515`, so

`M=515/376`,
`Pr_P(J=0)=376/515 > 4/9`.

For the incomparable pair `(4,9)`, the genuine uniform deletion law is balanced:

`nu(4<9)=229/376`.

Exactly `139` deletion extensions start with `4`; all of them lie in the event `4<9`, and precisely those fibers have weight `W=2`. Therefore the exact actual projected law gives

`mu(4<9)=(229+139)/515=368/515 > 2/3`.

Thus even the pointwise bound `1<=W<=2`, with 100% of the mass in the shallow core, does **not** preserve a fixed deletion-balanced pair. This does not refute the partner's adaptive `BR3786-SH741` lemma; it proves that its adaptive/covariance content is essential and cannot be replaced by same-pair bounded-density stability.

## 7. Full incomparable-pair check and arbitrary-size padding

The verifier checks all 15 incomparable pairs. The balanced ones are exactly

`(0,4):188/515`,
`(0,9):319/515`,
`(2,6):66/103`,
`(2,10):49/103`,
`(3,7):277/515`.

Hence this poset is **not** a POS3 counterexample.

For any `s,t>=0`, the ordinal sum

`C_s op P op C_t`

has width three and exactly the same internal incomparable-pair probabilities, because every full extension is the forced prefix, one of the 515 extensions of `P`, then the forced suffix. Thus the local heavy-edge/witness overlap obstruction and the deletion-tilt obstruction persist at arbitrarily large finite sizes and arbitrary asymmetric prefix/suffix lengths. The padded posets are not claimed autonomous-prime; the 11-element core is.

## 8. Exact executable certificate

Authoritative verifier:

`verify_two_channel_overlap_adversary.py`

Execution/source SHA-256:

`7dd35580f669b40f3ad98f30205d704dada8f5486b2c3e0f798a5383efd2aa44`

Captured exact output SHA-256:

`c7e4ba8c4bd5e53aac7ab2ec8fc4cb215805012eba835efbd4b9f3c4f5b7df55`

Terminal marker:

`POS3_TWO_CHANNEL_OVERLAP_ADVERSARY_PASS`

The verifier independently:

- constructs the transitive closure from the displayed covers;
- enumerates all 515 full linear extensions with unit weight;
- certifies the chain cover, 3-antichain, connected incomparability graph and autonomous-primality;
- checks the heavy-cover identity and exact two-witness sets;
- checks the local five-vertex probabilities and witness-event overlap;
- reconstructs the exact deletion law for `c=8` and verifies the `W in {1,2}` tilt;
- prints every incomparable-pair probability; and
- cross-checks key event counts by an independent subset-DP route with augmented order constraints.

No random vectors, sampled probabilities, projected-uniform substitution, or finite-census-to-universal inference is used.

## 9. Accepted gate and first remaining implication

**Classification:** `CANDIDATE_REFUTED` for `LOCAL-TWO-WITNESS-UNIT-CHARGE` and for fixed-pair balance stability under bounded shallow deletion weight. POS3 remains **OPEN**.

The accepted movement is:

**before:** the lead had proved that a bridge contains a `>E/3` heavy cover gap and that at least two external witness channels are necessary, while the partner had localized deletion-balanced pairs under an exact bounded tilt;

**after:** an exact connected autonomous-prime width-three core shows that (i) the two forced witness-minority events can have union strictly **smaller** than the heavy gap, with almost half of the heavy-gap extensions in neither event, and (ii) even `W<=2` everywhere can push a fixed deletion-balanced pair beyond `2/3`.

The first essential missing implication is therefore:

> **GLOBAL ADAPTIVE ANTI-OVERLAP TRANSFER.** In a cardinality-minimal no-balanced width-three candidate, use the global three-chain / strong-majority / deletion structure to prevent repeated `>E/3` heavy-gap mass from recycling through overlapping witness channels. Either produce a genuinely non-overlapping target-scale charge, adaptively switch to a different deletion-balanced pair whose exact tilted probability stays in `[1/3,2/3]`, or force strong-majority span descent, a proper autonomous nonchain, or a controlled non-crossed/multi-distinguisher exit.

The example proves that this implication cannot be replaced by a local five-vertex charge or a fixed-pair bounded-density argument.

## 10. Integrity

No target closure, novelty, or priority claim is made. No biased induced law is renamed uniform. The only computation is deterministic exact integer/rational enumeration plus an independent exact DP cross-check. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, remote workflows, permission change, or production-brain mutation was used.
