# POS3 account03/B10 — high-probability equal-predecessor conditioning in the strict corridor

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run remains in `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It changes mechanism from the preceding scalar variance / mean-lift analysis to an exact conditioning decomposition of the **actual uniform linear-extension law**. No projected law is replaced by an unproved uniform surrogate.

## 1. Exact assignment and source-bound state

The active account03/B10 assignment is:

> Apply bounded-width/high-variance results to the exact width-three target and derive the remaining exceptional-case requirement with constants/hypotheses explicit.

The assigned partner is **account04/B11**. I consumed its latest complete report

`proofnet24/collective-POS3/account04/B11/20260922T024830Z-B11-pos3-r13/REPORT.md`

(blob `bcf691d042edddf8d0a3600d97684d3bb4eeade2`). It proves, for a cardinality-minimal hypothetical counterexample with `K=pi(P)`, that first/last strong-majority chain blocks have length at most `K`, internal blocks at most `2K`, the exact first-interruption renewal law has at most `1+2K` genuine uniform residual components, and every nested chain-profile lift distortion is between `1/(K+1)` and `K+1`. It explicitly refutes an unproved finite-kernel shortcut.

I apply that result below in the surviving bounded-range branch: any delayed predecessor-difference corridor consists of elements all incomparable with the smaller-predecessor sibling, so its length is at most `K`. Together with the preceding account03/B10 result

`proofnet24/collective-POS3/account03/B10/20260922T0214Z-a03-b10-r11/REPORT.md`

(blob `3e50b4d0adaa18c79a96079139d660b832418a2d`), the source-parametric range is

`K < K_AK(1,6560)^2`,

where `K_AK` is the existential threshold in Aires--Kahn's bounded-width variance-vs-range theorem. No numerical value is invented.

The newest campaign-lead input is account04/B10,

`proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`

(blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`). At the first Hasse-fork sibling pair, after relabelling,

`Pred(b) subseteq Pred(a)`,

and the proper difference

`D=Pred(a)\Pred(b)`

is a delayed chain. The same lead report imports the exact equal-predecessor deletion-channel identity from account01/B11. The strict branch `D != empty` remained global/unpaid.

The result below pays a substantial part of that strict branch without using a biased deletion law.

## 2. Conditional route

Assume for contradiction-search purposes that `P` is a width-at-most-three poset with **no balanced incomparable pair**, and let `L_*` be the inherited transitive strong-majority linear extension. Consider an incomparable pair `a,b` satisfying

`Pred(b) proper_subset Pred(a)`,

with

`D=Pred(a)\Pred(b)`

nonempty and a chain. This is exactly the strict delayed-predecessor corridor supplied at the first fork by the lead.

Every `d in D` satisfies `d<a` and `d||b`. Hence

`|D| <= pi(b) <= K < K_AK(1,6560)^2`.                         (2.1)

The new argument treats the branch in which the sibling carrying the **larger predecessor set is majority-early**:

`a prec_* b`, equivalently `p:=Pr_P(a<b)>2/3`.                 (2.2)

Let `d=max D`, which exists because `D` is a finite nonempty chain.

## 3. One strong relation collapses the whole predecessor corridor

Since `d<a` in the poset and `a prec_* b`, the strong-majority extension has

`d prec_* a prec_* b`.                                         (3.1)

Because `d||b` and `P` has no balanced pair,

`gamma := Pr_P(d<b) > 2/3`.                                   (3.2)

Also `gamma<1`, since an incomparable pair can occur in either order in some linear extension.

Define two genuine posets on the same ground set:

`P^+ := P + (d<b)`,
`P^- := P + (b<d)`,                                            (3.3)

where transitive closure is understood. Both additions are acyclic because `d||b` in `P`.

### Lemma 3.1 — exact two-child uniform decomposition

The uniform linear-extension law of `P` decomposes exactly as

`Law(P) = gamma Law(P^+) + (1-gamma) Law(P^-)`.                (3.4)

Here `Law(P^+)` and `Law(P^-)` are the genuine **uniform** laws on their full sets of linear extensions.

### Proof

Every linear extension of `P` orders the incomparable pair `d,b` in exactly one of the two ways. The extensions with `d<b` are exactly `L(P^+)`, and those with `b<d` are exactly `L(P^-)`. Conditioning a uniform finite set on either part is therefore uniform on that part. `square`

This is an actual-uniform-law identity, not a surrogate for an induced deletion law.

### Lemma 3.2 — the `+` child has equal sibling predecessor sets

In `P^+`,

`Pred_{P^+}(a)=Pred_{P^+}(b)=Pred_P(a)`.                        (3.5)

In `P^-`,

`b<d<a`,                                                        (3.6)

so in particular `b<a`.

### Proof

Every old predecessor of `b` is already a predecessor of `a`. Every element of `D` is at most the top element `d`, hence the added relation `d<b` makes every member of `D` a predecessor of `b`. Thus all of `Pred_P(a)=Pred_P(b) union D` becomes predecessor to `b` in `P^+`.

Conversely, any new predecessor of `b` created by adding `d<b` is at or below `d`; since `d<a`, it was already a predecessor of `a`. The added edge points into `b`, so it creates no new predecessor of `a`. This proves (3.5). Equation (3.6) is immediate from the opposite added relation and `d<a`. `square`

Thus a possibly `K`-long strict predecessor corridor is collapsed, in one source-valid conditioning step, to the equal-predecessor geometry already analyzed by the team.

## 4. Exact scaling of the extreme sibling probability

The event `a<b` implies

`d<a<b`,

hence it is contained in the event `d<b`. In the `P^-` child it is impossible because `b<d<a`. Therefore (3.4) gives the exact identity

`p = gamma p^+`,                                                (4.1)

where

`p^+ := Pr_{P^+}(a<b)`.

Since `p>2/3`,

`p^+ > 2/(3 gamma) > 2/3`.                                    (4.2)

The second strict inequality uses `gamma<1`.

This is stronger than merely saying the conditioned pair remains majority-early: it gives the exact amplification factor `1/gamma`.

## 5. Apply the equal-predecessor channel identity inside the genuine uniform child

Work now entirely under the uniform law on `L(P^+)`. Because (3.5) gives equal predecessor sets, the exact deletion-channel identity from the campaign lead applies.

Let

`Z = Min{z : a<z and z||b}`                                    (5.1)

in `P^+`. For each `z in Z`, let `C_z` be the positive first-successor channel count. Let `C_- >=0` be the total negative-channel count. If `E^+=e(P^+)`, then

`sum_{z in Z} C_z - C_- = (2p^+-1) E^+`.                      (5.2)

Every extension counted by `C_z` satisfies

`a<z<b`.                                                        (5.3)

Width at most three is preserved by adding a relation, and `Z` is an antichain all incomparable with `b`, so

`1 <= |Z| <= 2`.                                                (5.4)

(The lower bound follows from (5.2) and `p^+>1/2`.)

The relation `a<z` in `P^+` was already present in `P`: the only new edge is from a predecessor `d<a` into `b`, so it cannot create an outgoing path from `a`. Likewise `z||b` in the more constrained `P^+` implies `z||b` in `P`.

Moreover, because `d<a<z`, the event `z<b` is impossible in `P^-`, where `b<d<a<z`. Consequently

`Pr_P(z<b)=gamma Pr_{P^+}(z<b)                                (5.5)

for every positive blocker `z`, and (5.3) yields

`Pr_P(z<b) >= gamma C_z/E^+`.                                  (5.6)

Again, all probabilities are from actual uniform laws on complete linear-extension sets.

## 6. Strict-corridor dichotomy: span descent or a conditioned second fork

A positive blocker `z` with

`Pr_P(z<b)>2/3`                                                 (6.1)

gives a strict strong-majority span descent: since `a<z` in the poset,

`a prec_* z prec_* b`,                                         (6.2)

and `(z,b)` is an incomparable extreme pair with strictly smaller `L_*` span than `(a,b)`.

Assume from now on that **no such span descent occurs**. Since `P` has no balanced pair and every `z||b`, this forces

`Pr_P(z<b)<1/3`                                                 (6.3)

for every `z in Z`. By (5.5),

`Pr_{P^+}(z<b)<1/(3 gamma)`,                                   (6.4)

and therefore

`C_z/E^+ < 1/(3 gamma)`.                                       (6.5)

On the other hand, (5.2) gives

`sum_z C_z/E^+ >= 2p^+-1 > 4/(3 gamma)-1`.                    (6.6)

### Theorem 6.1 — one-blocker strict corridor is impossible without span descent

If `|Z|=1`, equations (6.5) and (6.6) give simultaneously

`C_z/E^+ < 1/(3 gamma)`

and

`C_z/E^+ > 4/(3 gamma)-1`.

But because `gamma<1`,

`4/(3 gamma)-1 > 1/(3 gamma)`.                                (6.7)

Contradiction. Therefore the one-positive-blocker case necessarily produces the span descent (6.2).

### Theorem 6.2 — the only no-descent residue has exactly two blockers and a sharp probability window

If no span descent occurs, then `|Z|=2`; write `Z={z_1,z_2}`. Summing (6.5) and using (5.2),

`2p^+-1 < 2/(3 gamma)`,                                        (6.8)

so

`p^+ < 1/2 + 1/(3 gamma)`.                                     (6.9)

Multiplying by `gamma` and using (4.1) gives the original-law corridor

`2/3 < p < 1/3 + gamma/2.                                      (6.10)`

Equivalently,

`gamma > 2p-2/3`.                                               (6.11)

Thus a strict predecessor difference does not remain an arbitrary obstruction. In the majority-early branch it either descends to a shorter extreme pair, or after conditioning on one strong relation it becomes an equal-predecessor **two-blocker fork** and the two original-law probabilities `p` and `gamma` are forced into (6.10).

The equal-predecessor endpoint statistic is also squeezed. Writing the lead's exact identity in `P^+` as

`p^+ = 1-(Q^+ + R^+)/(2E^+)`,                                  (6.12)

(4.2) and (6.9) imply

`1 - 2/(3 gamma) < (Q^+ + R^+)/E^+ < 2 - 4/(3 gamma)`.         (6.13)

This interval is nonempty exactly in the already-forced regime `gamma>2/3`.

## 7. Return to the first Hasse fork

In the campaign-lead first-boundary geometry, `a,b` are sibling Hasse successors and the earlier endpoint `y` is incomparable with both. In the no-descent residue of Theorem 6.2, the two positive blockers `z_1,z_2` are Hasse successors of `a` in `P^+`, hence also in `P`; and

`{b,z_1,z_2}`

is a three-element antichain. Under the no-descent assumption, `b prec_* z_i` for both `i`, so the blockers lie after `b` in `L_*`.

If `y` were incomparable with both `z_1,z_2`, then

`{y,b,z_1,z_2}`

would be a four-element antichain, contradicting width at most three. Therefore at least one `z_i` is comparable with `y`. The strong-majority order places `y` before the later blocker, so the comparability must be

`y<z_i`.                                                        (7.1)

Hence the strict lower-distinguisher, larger-predecessor-majority-early branch now reaches the **same kind of second-fork bridge** as the previously solved equal-predecessor branch, but with the additional quantitative conditioning window (6.10)-(6.13).

## 8. What changed and what remains unpaid

### Paid here

- The assigned partner's bounded-range localization is applied without resurrecting a finite kernel: the delayed predecessor corridor has length at most `K`, with `K<K_AK(1,6560)^2` from the preceding B10 variance result.
- A single relation at the top of that entire corridor gives an exact two-child decomposition into **uniform** laws `P^+` and `P^-`.
- The `P^+` child has equal predecessor sets, while `P^-` forces the opposite sibling order.
- In the larger-predecessor-majority-early branch, the extreme sibling probability scales exactly as `p=gamma p^+`.
- The one-positive-blocker conditioned branch cannot survive without strict span descent.
- The only no-descent residue has exactly two positive blockers and must satisfy `2/3<p<1/3+gamma/2`, together with the endpoint-statistic window (6.13).
- At the inherited first fork, that residue forces the same width-saturating second-fork bridge `y<z_i` seen in the equal-predecessor branch.

### Still unpaid

POS3 is **not proved**. The strict branch in which the sibling with the larger predecessor set is **majority-late** remains. More globally, one must still show that repeated span descent / fork escalation and the majority-late corridor cannot continue through all strong-majority blocks without producing a balanced pair, a four-antichain, an autonomous nonchain reduction, or an exact flux contradiction.

The next source-valid step is now sharper than the previous generic renewal selector: combine the majority-late endpoint polarity from the lead with the bounded `D` corridor, and either obtain an analogous two-child conditioning squeeze or show that some `d in D` lies strictly inside the strong-majority span and therefore already gives descent.

## 9. Integrity

No finite census or computation is used as proof. No induced/deleted law is called uniform without an exact conditioning identity. No novelty or priority claim is made. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public release, permission change, or production-brain mutation was used.
