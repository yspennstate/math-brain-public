# POS3 account04/B11 r18 — Hasse-cover stationary exits cannot be neutral

**Run:** `20260922T090813Z-B11-pos3-r18`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform linear-extension probability lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No finite-kernel reduction is used. All probabilities refer to the uniform law on the original full linear extensions.

## 1. Exact dependencies consumed

Latest complete team-lead version consumed:

- account04/B10 r18, source report `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, commit `a4b6e9bf76d078c98a82f44be0af30c57def7f99`, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

It proves that every surviving outward four-channel export re-enters a heavy Hasse bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

and that a two-step ray switch has only strict span descent, strict envelope expansion, or literal exact backtrack. Its first unpaid global issue is cross-envelope reuse through non-exact/multi-distinguisher exact-backtrack bridges.

Assigned OTHER-account partner consumed and applied:

- account01/B19 r11 source-bound handoff commit `d07c98d628f5da8745feee6e0c2f128e43d2a932`, handoff blob `32be4d8d8abb773fa2a6606bf31edaf4c50b92b9`, canonical report blob `c1442ecaf5ca6f61b5a97fcbf1fc18ca85518aff`.

For a deleted chain `C`, repeated projected elements with one fixed chain-prefix profile `J=[alpha,beta]` of width `h` act after the first restriction by the prefix matrix `S`, with `(S^k)_{r,s}=binom(k+r-s-1,r-s)`. Hence every fixed downstream statistic `D(k)=ell^T S^k g` is polynomial of degree at most `h`; any fixed threshold can be crossed at most `h` times unless the threshold identity is identically zero. The partner's first unpaid step was to control the first exit from a maximal stationary profile block.

Two additional exact existing results are applied only in the branch where a sibling relation distinguisher is produced:

- account02/B10 one-distinguisher balance handoff commit `a6b42401716b4ad5436054bd433fc38d5b046ecf`: any incomparable pair with exactly one relation distinguisher is balanced;
- account03/B11 two-distinguisher sign handoff commit `a91d15a1cf9d64c794fd9ee917dd38cc4465734f`: an incomparable pair with exactly two distinguishers of opposite signs is balanced.

## 2. Cover-profile dictionary

Fix one of the lead's heavy Hasse bridges

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`.

Delete the two-element chain `C={p<r}`. For an outside element `z`, let `J_C(z)` be the interval of possible numbers of elements of `C` appearing before `z` in a full extension. Because `C` has two elements, the only formal intervals are subintervals of `{0,1,2}`. The cover relation excludes the singleton middle profile.

### Lemma 2.1 — exact dictionary

For every `z` outside `C`, exactly one of the following holds:

1. `J_C(z)=[0,0]` iff `z<p`;
2. `J_C(z)=[0,1]` iff `z||p` and `z<r`;
3. `J_C(z)=[0,2]` iff `z||p` and `z||r`;
4. `J_C(z)=[1,2]` iff `p<z` and `z||r`;
5. `J_C(z)=[2,2]` iff `r<z`.

The formal profile `[1,1]` would mean `p<z<r`, impossible because `p lessdot r`.

**Proof.** The number of chain elements preceding `z` is 0,1,2. Poset comparabilities with `p<r` determine which of these counts are allowed. Transitivity rules out all noninterval patterns, and `p lessdot r` rules out an element strictly between the two chain points. `square`

Thus the partner's stationary profile for an element incomparable with both endpoints is exactly `J=[0,2]`, with width `h=2`. Consequently any fixed downstream statistic inside a genuinely stationary `[0,2]` block has degree at most two and can cross `1/3` or `2/3` at most twice unless it is identically on that threshold.

## 3. New theorem: first exit from `[0,2]` has a complete Hasse normal form

Consider the first projected element `z` after a maximal stationary `[0,2]` block for the fixed cover `p lessdot r`. Then `J_C(z)` is one of the four nonstationary profiles in Lemma 2.1.

### Theorem 3.1 — outer singleton profiles are strict envelope exits

If `J_C(z)=[0,0]`, then `z<p`. If `z||q`,

`Pr(z<q) >= Pr(p<q) > 2/3`,

so `z prec_* p prec_* q` and `(z,q)` is a strict left envelope expansion. If `z` is comparable with `q`, the only possibility is `z<q`; the alternative `q<z<p` would contradict `q||p`.

Dually, if `J_C(z)=[2,2]`, then `r<z`. If `z||q`, then

`Pr(q<z) >= Pr(q<r) > 2/3`,

so `q prec_* r prec_* z` and `(q,z)` is a strict right envelope expansion. If `z` is comparable with `q`, only `q<z` is possible.

Hence neither outer singleton profile creates a neutral exact-backtrack recycler.

### Theorem 3.2 — a lower half-profile lifts to a sibling Hasse gate

Suppose `J_C(z)=[0,1]`, so `z||p` and `z<r`. Choose any saturated chain from `z` to `r`, and let `s` be its penultimate element. Then

`s lessdot r`, `s != p`, and `p||s`.

Indeed `s=p` would imply `z<p`, contradicting `z||p`; and two distinct lower covers of the same element are incomparable.

Moreover `q<s` is impossible, because `q<s<r` would imply `q<r`, contradicting `q||r`. Therefore exactly one of

- `s<q`, or
- `s||q`

holds.

In the second case `{p,s,q}` is a three-antichain, so width three is saturated locally. This is exactly the sibling three-antichain geometry to which the lead's coherent-gate analysis applies; all noncoherent strong-order orientations are already routed to the lead's accepted descent/export mechanisms, leaving only its coherent orientation.

In the first case `q` is a relation distinguisher for the incomparable sibling pair `(p,s)`: it is comparable with `s` and incomparable with `p`. By the one-distinguisher balance theorem, a no-balanced candidate forces at least one further distinguisher of `(p,s)`. If there are exactly two and their signs are opposite, the two-distinguisher sign theorem gives a balanced pair. Hence the only no-balanced residue of this branch is:

- exactly two same-sign distinguishers, or
- at least three distinguishers.

Thus a lower half-profile exit is never a structureless profile change: it lands in the already isolated coherent three-antichain gate or in the delayed same-sign/multi-distinguisher branch.

### Theorem 3.3 — upper half-profile is the exact dual

If `J_C(z)=[1,2]`, then `p<z` and `z||r`. Choose the first element `t` after `p` on a saturated chain from `p` to `z`. Then

`p lessdot t`, `t != r`, and `t||r`.

The relation `t<q` is impossible because `p<t<q` would contradict `p||q`. Hence either `q<t` or `q||t`. In the incomparable case `{q,r,t}` is a width-saturating three-antichain; in the comparable case `q` is a relation distinguisher for the incomparable upper-sibling pair `(r,t)`. The same one-/two-distinguisher theorems reduce the no-balanced residue to exactly two same-sign distinguishers or at least three distinguishers.

` square `

## 4. Consequence for the partner's stationary-profile exit obligation

For the lead heavy Hasse bridge, the first exit from a stationary `[0,2]` backtrack block has no new neutral geometry. It is forced into one of four existing classes:

1. strict strong-order envelope expansion;
2. an already comparable outer element, hence no new incomparable recycling state;
3. a width-saturating sibling three-antichain gate, with only the lead's coherent orientation surviving the existing local reductions;
4. a same-sign/multi-distinguisher sibling branch (exactly two same-sign distinguishers or at least three distinguishers in a no-balanced candidate).

This directly pays the structural part of account01/B19's `POS3-COHERENT-STATIONARY-RAY-EXIT-CHARGE` obligation for the two-element heavy-cover chain. Since the stationary profile width is exactly two, the fixed-environment crossing budget is also exactly two, not merely a qualitative finite bound.

What is still unpaid is quantitative charge at class (4), and, in the coherent class (3), the lead's already named global cross-envelope/backtrack reuse. A static same-sign distinguisher is not promoted to a probability packet without an exact counting map.

## 5. Compact conditional end-to-end route

Assume a finite width-at-most-three counterexample with no balanced pair. The lead converts surviving four-channel exports into heavy Hasse bridges and classifies two-step ray switches. On any fixed heavy cover, account01/B19 bounds stationary `[0,2]` threshold oscillation by degree two. The theorem above shows that the first profile exit cannot create a fresh neutral state: it expands the strong-order envelope, enters the already isolated coherent sibling gate, or enters the same-sign/multi-distinguisher branch. Therefore an infinite-style recycler in the finite counterexample cannot be justified by arbitrary profile switching.

The first essential missing implication is now narrower:

> **`POS3-SAME-SIGN-SIBLING-CHARGE-v1`.** At a heavy-cover stationary-profile exit producing sibling lower covers `p,s lessdot r` (or the dual upper covers) and the no-balanced same-sign/multi-distinguisher residue, convert at least one of the relation distinguishers into an exact positive full-extension packet on an incomparable pair, or force strict span descent, a balanced pair, or a proper autonomous/ordinal reduction. The conversion must retain original full-extension multiplicities.

Conditional on that charge lemma, the partner's finite stationary crossing budget plus the lead's expansion/backtrack normal form removes the remaining stationary-profile recycling mechanism. The parent POS3 theorem is not claimed.

## 6. Integrity/status

- parent POS3: **OPEN / NOT PROVED**;
- lead r18: **CONSUMED/APPLIED**;
- assigned account01/B19 r11 stationary-profile theorem: **CONSUMED/APPLIED**;
- account02/B10 one-distinguisher theorem: **CONSUMED/APPLIED**;
- account03/B11 opposite-sign two-distinguisher theorem: **CONSUMED/APPLIED**;
- cover-profile dictionary: **PROVED for arbitrary finite posets**;
- first nonstationary profile exit normal form: **PROVED for arbitrary finite posets**;
- no finite-kernel reduction: **USED NONE**;
- quantitative same-sign sibling charge: **OPEN**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation was used in this run. No benchmark material, sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive, paid or remote model/API/Codex execution, workflow dispatch, permission change, or public posting was used.