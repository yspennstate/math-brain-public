# POS3 fleet02/B10 — exact four-channel transposition exports every strong pair

**Run:** `20260922T075033Z-b10-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below use the original uniform law on the complete set of full linear extensions of the original finite poset. No deletion-induced distribution is introduced, much less treated as uniform.

## 1. Sources actually consumed

Fresh campaign state was taken from the current fleet04/B10 lead report:

- `proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, Git blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

Its live unresolved same-ray state is a coherent width-saturating three-antichain gate. On the right ray it has incomparable `y,r_L,r_R` with strong-majority order

`y prec_* r_L prec_* r_R`,

and on the left ray the dual gate has incomparable `r_L,r_R,x` with

`r_L prec_* r_R prec_* x`.

The lead has already paid the comparable same-ray gate and the anti-aligned incomparable gate. Its next missing implication is `COHERENT-GATE EXIT`.

The required named partner result consumed and applied is fleet03/B11:

- `proofnet24/collective-POS3/fleet03/B11/20260922T061153Z-fleet03-B11-pos3-r11/REPORT.md`, Git blob `007674f27dd243e81ec49b646fbbe8ccd6cc6ae9`.

That report supplies the exact full-extension transposition-defect/Hasse-witness mechanism: a failed endpoint position swap is localized to a canonical Hasse obstruction, without replacing the full uniform extension law by a projected or deletion law.

A second OTHER-account dependency actually used is fleet01/B10:

- `proofnet24/collective-POS3/fleet01/B10/20260922T072132Z-b10-pos3-r11/REPORT.md`.

Under the no-balanced-pair hypothesis it proves that the strong-majority orientation `prec_*` on incomparable pairs is a strict total order and that the corresponding same-ray potentials strictly increase on same-ray transitions. Its remaining obstruction is genuine ray switching/crossed accounting.

## 2. Compact conditional end-to-end route

Assume, for contradiction, a finite width-at-most-three nonchain poset with no balanced pair. Enter the campaign lead's low-endpoint heavy-cover state. The lead's exact swap analysis exports two typed outward packets; all same-ray cases are paid except its coherent three-antichain gate. The result below now shows that **every** strong incomparable pair, hence in particular either endpoint pair of that coherent gate, has an exact full-law transposition defect exceeding one third of all extensions and therefore exports, through at most four Hasse channels, a genuine incomparable pair carrying more than `1/12` of all extensions in one orientation. If that marked orientation is majority, it gives the campaign's strict span-descent exit; if it is minority, it is an outward charged pair with minority mass `>1/12`.

Applied to the coherent three-antichain, the witnessing cover cannot be the third antichain vertex because that vertex is incomparable with both swapped endpoints, whereas a swap witness is Hasse-comparable with one endpoint. Thus the coherent gate is not a closed local recycler: it must leave the gate, descend, or balance. If the exported pair remains on the same ray, fleet01/B10's same-ray potential strictly increases. Therefore the first unpaid implication is reduced to **genuine ray-switch/crossed charge accounting**: prove that successive `>1/12` outward charges cannot alternate rays indefinitely without a balanced pair, strict span descent, a four-antichain, or a proper autonomous/ordinal reduction.

This is not a full proof because that final global ray-switch implication remains open.

## 3. Four-channel strong-pair transposition lemma

Let `P` be a finite poset of width at most three and let `p||q`. Write

`E = e(P)`,  `M = #{L in L(P): p<q in L}`,  `N=E-M`.

Assume

`M > 2E/3`.                                                   (3.1)

For a full linear extension `L`, let `T(L)` be the word obtained by exchanging the positions of `p` and `q` and leaving every other position fixed. Define

`D_M = {L: p<q in L and T(L) is not a linear extension}`,  
`D_N = {L: q<p in L and T(L) is not a linear extension}`.

Define the two Hasse witness families

`U(p,q) = {r: p lessdot r and r||q}`,                         (3.2)
`D(p,q) = {r: r lessdot q and r||p}`.                         (3.3)

### Lemma 3.1 — exact defect identity

`|D_M|-|D_N| = M-N = 2M-E`.                                  (3.4)

In particular,

`|D_M| > E/3`.                                                (3.5)

**Proof.** On the domain where `T` is legal, `T` is its own inverse and bijects legal `p<q` extensions with legal `q<p` extensions. Hence

`M-|D_M| = N-|D_N|`.

Rearrangement gives (3.4), and (3.1) gives (3.5). No conditioning or projection is involved. `square`

### Lemma 3.2 — every outgoing defect has a Hasse witness in (3.2) or (3.3)

For every `L in D_M`, at least one member of `U(p,q) union D(p,q)` lies strictly between `p` and `q` in `L`.

**Proof.** Because only `p,q` move, illegality of `T(L)` must arise in one of two ways.

First, moving `p` right crosses some `z` with `p<z` in the poset and `p<z<q` in `L`. Choose a saturated chain from `p` to such a `z` and let `r` be its first vertex after `p`. Then `p lessdot r`, and `r` lies between `p,q` in `L`. We also have `r||q`: the relation `r<q` would imply the forbidden poset relation `p<q`, while `q<r` is incompatible with the displayed order in `L`. Thus `r in U(p,q)`.

Second, moving `q` left crosses some `z` with `z<q` in the poset and `p<z<q` in `L`. Choose a saturated chain from `z` to `q` and let `r` be its last vertex before `q`. Then `r lessdot q`, it lies between `p,q` in `L`, and `r||p`: the relation `p<r` would imply `p<q`, while `r<p` contradicts the displayed order in `L`. Thus `r in D(p,q)`. `square`

### Lemma 3.3 — width three gives at most four channels

`|U(p,q)| <= 2`, `|D(p,q)| <= 2`.                             (3.6)

**Proof.** Distinct covers of `p` are pairwise incomparable. Every member of `U(p,q)` is also incomparable with `q`. Hence three members of `U(p,q)` together with `q` would be a four-element antichain. Width at most three excludes this. The proof for `D(p,q)` is dual. `square`

Choose one deterministic witness from `U union D` for each `L in D_M`. By (3.5)-(3.6), one of at most four channels receives strictly more than `E/12` marked extensions. If the selected witness is `r in U`, every one of its marks lies in the genuine order event

`p<r<q`,

so, because `r||q`,

`Pr(r<q) > 1/12`.                                             (3.7)

If the selected witness is `r in D`, every mark again lies in `p<r<q`, and because `p||r`,

`Pr(p<r) > 1/12`.                                             (3.8)

We have therefore proved:

**Theorem 3.4 — four-channel transposition export.** For every strong incomparable pair `p prec_* q` in a width-at-most-three poset, at least one of the following holds.

1. A balanced pair already exists.
2. There is a new strong incomparable pair strictly inside the old endpoint span (the campaign's span-descent exit).
3. There is an outward Hasse-adjacent incomparable pair whose minority orientation has full-law probability `>1/12`.

Indeed, in the `U` case, if `Pr(r<q)>2/3`, then `p<r` is forced and `r prec_* q`, giving the inner pair `(r,q)`. Otherwise no-balancedness forces `Pr(r<q)<1/3`, so `q prec_* r`, and (3.7) is an outward minority charge `>1/12`. The `D` case is the order-dual argument: if `Pr(p<r)>2/3`, then `p prec_* r` with forced `r<q`, giving inner pair `(p,r)`; otherwise `r prec_* p` and (3.8) is the outward minority charge.

The constant is strict: the outgoing defect itself has mass strictly above `1/3`, and the number of width-three channels is at most four.

## 4. Direct application to the lead's coherent three-antichain gate

Consider the lead's right-ray coherent state

`{y,r_L,r_R}` an antichain,  `y prec_* r_L prec_* r_R`.        (4.1)

Apply Theorem 3.4 to the strong pair `(p,q)=(y,r_L)`. If it balances or descends, the campaign has an allowed exit. Otherwise it exports an outward pair with minority probability `>1/12`.

Crucially, the Hasse witness in this export **cannot be `r_R`**. Membership in `U(y,r_L)` would require `y lessdot r_R`, and membership in `D(y,r_L)` would require `r_R lessdot r_L`, while (4.1) says `r_R` is incomparable with both. Hence the outgoing transposition defect necessarily introduces a vertex outside the coherent antichain gate.

The left-ray gate is dual: for

`{r_L,r_R,x}` an antichain,  `r_L prec_* r_R prec_* x`,       (4.2)

apply Theorem 3.4 to `(p,q)=(r_R,x)`. Again the third gate vertex `r_L` is incomparable with both endpoints and therefore cannot be a Hasse swap witness. The gate must genuinely exit, descend, or balance.

Numerically this export does not decrease the lead's certified local packet floor: `1/12 > 2/33`, with difference `1/44`. Thus the coherent gate can be spliced into the lead/fleet01 potential route without losing the already certified packet scale.

## 5. Decisive exact regression

`verify_four_channel_transposition.py` exhaustively enumerates every naturally labelled width-at-most-three poset on `n=3,4,5,6`, all of its full linear extensions, and every ordered incomparable pair satisfying `Pr(p<q)>2/3`. For every such pair it checks the exact defect identity, the `>E/3` outgoing defect bound, Hasse-witness existence, the two width-three channel bounds, deterministic assignment to at most four channels, the strict `>E/12` selected-channel bound, and containment of every selected mark in the claimed genuine incomparable-pair order event.

Exact clean output:

```text
naturally_labelled_width_le_3_posets_n3_to_n6 = 3699
strong_ordered_incomparable_pairs_checked = 12485
witness_channel_histogram = {1: 2002, 2: 7726, 3: 2566, 4: 191}
minimum_observed_selected_channel_share = 7/37
minimum_record(n,E,M,p,q,|U|,|D|,out,in,maxmarks) = (6, 37, 25, 5, 4, 0, 2, 13, 0, 7)
POS3_FOUR_CHANNEL_TRANSPOSITION_CHECK_PASS
```

This computation is a regression test for the arbitrary-size proof above, not finite closure of POS3.

## 6. First essential remaining implication

The local coherent-gate exception has been removed. The first unpaid implication is now:

**`POS3-RAY-SWITCH-CHARGE-ACCOUNTING-v1`.** Starting from an outward pair carrying minority mass `>1/12`, prove that repeated exact transposition exports cannot alternate left/right rays or recycle through crossed states indefinitely while every incomparable pair remains outside `[1/3,2/3]`, unless there is strict span descent, a four-antichain, or a proper autonomous/ordinal reduction.

The fleet01 same-ray strict potential handles same-ray continuations; what is still missing is a global potential or disjoint-charge budget across genuine ray switches. The parent conjecture remains open.

## 7. Status and integrity

- fleet04/B10 r17 coherent-gate frontier: **CONSUMED/APPLIED**;
- named partner fleet03/B11 exact transposition/Hasse-defect mechanism: **CONSUMED/APPLIED**;
- fleet01/B10 same-ray strict-order/potential result: **CONSUMED/APPLIED**;
- exact defect identity `|D_M|-|D_N|=2M-E`: **PROVED**;
- width-three at-most-four witness channels: **PROVED**;
- strong-pair export `>1/12`: **PROVED**;
- coherent three-antichain gate must genuinely exit/descend/balance: **PROVED**;
- global ray-switch charge accounting: **OPEN**;
- POS3 parent target: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

Scoped privacy/provenance review: this report contains only mathematics, logical account/slot/run labels, repository-relative source references, Git object identifiers, and aggregate verifier output. It contains no credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark gold, email, or Drive data.
