# POS3 account04/B20 — two-sided active blockers remove the long-bridge witness loophole

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no new brain-installation or benchmark work. All probabilities below are under the original uniform law on the full linear-extension set.

## 1. Exact live state consumed

The newest complete team-lead result available at the start of the proof work is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, Git blob `50bac494667235f3630991a512438eac42c30521`.

Its bridge theorem says that in the lead's bridged two-blocker branch there is a saturated chain

`c=z_0 lessdot z_1 lessdot ... lessdot z_k=u`

all of whose vertices are incomparable with the distinguished point `a`, and there is a unique transition edge

`x=z_j lessdot y=z_{j+1}`

with

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,

hence

`Pr(x<a<y)>1/3`.

It then applies the assigned partner's two-witness theorem. The exact remaining obligation in B10 r14 is a **two-channel heavy-edge recycling theorem**. Its Corollary 5.1 has a specific loophole for long bridges: if `k>=3`, two nonendpoint vertices of the bridge itself can already count as the two relation distinguishers, so relation-distinguisher counting alone does not force charge off the neutral corridor.

The required named OTHER-account input consumed and applied is

- account01/B19, `proofnet24/collective-POS3/account01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, Git blob `003d2bf0593cb55f11738f50d68509413bb8d234`.

It proves the exact three-chain `F*G` flux recurrence and the Cover Two-Witness Theorem: for a cover `x lessdot y` and `a||x,y`, a strong flip

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`

in a no-balanced poset forces at least two distinct external relation distinguishers after removing the cover endpoints. Its report explicitly warns that mere witness counting is not enough; the heavy-edge charge must retain exact extension weights.

The theorem below directly strengthens that partner result in precisely the lead's unresolved direction. It replaces static relation distinguishers by **active swap blockers carrying exact full-extension mass**.

## 2. Compact conditional end-to-end route

Assume the lead has reached a heavy bridge edge

`x lessdot y`, `a||x,y`,
`p:=Pr(x<a)>2/3`, `q:=Pr(y<a)<1/3`.

Because `x<y`, every full linear extension belongs to exactly one of three classes:

- `A={a<x<y}`;
- `H={x<a<y}`;
- `C={x<y<a}`.

Writing the same letters for the class cardinalities and `E=e(P)`, we have

`p=(H+C)/E`, `q=C/E`, and `H/E=p-q>1/3`.

The lead/partner state knows only that there are at least two relation witnesses. The new theorem proves more:

1. at least `H-A` middle extensions have a genuine **left active blocker** preventing the position-swap `x <-> a`;
2. at least `H-C` middle extensions have a genuine **right active blocker** preventing `a <-> y`;
3. the left-capable and right-capable blocker vertex sets are disjoint;
4. no vertex on any saturated chain containing the cover edge `x lessdot y` can be active on either side.

Thus **every heavy bridge edge exports two disjoint, positive-weight blocker-channel families off the bridge, independent of bridge length**. This closes the exact `k>=3` loophole in B10 r14. The remaining global problem is to show that these off-bridge weighted channel families cannot recycle indefinitely.

## 3. Two-sided active-blocker theorem

### Theorem 3.1

Let `P` be any finite poset. Suppose

`x lessdot y`, `a||x`, `a||y`,

and

`p:=Pr(x<a)>2/3`, `q:=Pr(y<a)<1/3`.                              (3.1)

Let `A,H,C` be the three extension classes from Section 2, with cardinalities again denoted by `A,H,C`. Define

`B_L = {L in H : swapping the positions of x and a in L is not a linear extension}`,  (3.2)

`B_R = {L in H : swapping the positions of a and y in L is not a linear extension}`.  (3.3)

Then:

**(i) Exact weighted lower bounds.**

`|B_L| >= H-A`,
`|B_R| >= H-C`.                                                  (3.4)

Equivalently,

`Pr(B_L) >= 2p-q-1 > 0`,
`Pr(B_R) >= p-2q > 0`,                                          (3.5)

and therefore

`Pr(B_L)+Pr(B_R) >= 3(p-q)-1 = 3 Pr(x<a<y)-1 > 0`.              (3.6)

**(ii) Exact left blocker types.** For every `L in B_L`, some vertex `v` lying strictly between `x` and `a` in `L` satisfies exactly one of

`x<v` and `v||a`,                                               (L1)

`v<a` and `v||x`.                                               (L2)

**(iii) Exact right blocker types.** For every `L in B_R`, some vertex `w` lying strictly between `a` and `y` in `L` satisfies exactly one of

`a<w` and `w||y`,                                               (R1)

`w<y` and `w||a`.                                               (R2)

**(iv) Two genuinely distinct vertex channels.** Let `V_L` be the set of nonendpoint vertices capable of satisfying (L1) or (L2), and let `V_R` be the corresponding set for (R1) or (R2). Then

`V_L cap V_R = emptyset`.                                       (3.7)

In particular both sets are nonempty under (3.1), so there exist at least two distinct active-blocker vertices, one of each orientation.

**(v) Off-bridge property.** If `Z` is any saturated chain containing the cover edge `x lessdot y`, no vertex of `Z\{x,y}` can be an active blocker occurring in (ii) or (iii). Hence every actual left/right active blocker lies off that bridge chain.

The theorem does not use width three; width three enters when the result is inserted into the POS3 bridge corridor.

### Proof of (i)

Let `H_good^L` be the middle extensions for which swapping the positions of `x` and `a` remains a linear extension. That swap sends

`x ... a ... y`

to

`a ... x ... y`,

so it maps `H_good^L` into `A`. The operation is an involution on its valid domain, hence injective. Therefore

`|H_good^L| <= A`,

and

`|B_L| = H-|H_good^L| >= H-A`.                                 (3.8)

Likewise the valid position-swap `a <-> y` maps its good middle domain injectively into `C`, giving

`|B_R| >= H-C`.                                                 (3.9)

Now

`A/E = 1-p`,
`H/E = p-q`,
`C/E = q`.

Substituting into (3.8)-(3.9) gives

`(H-A)/E = (p-q)-(1-p)=2p-q-1`,

`(H-C)/E = (p-q)-q=p-2q`,

which are strictly positive by `p>2/3` and `q<1/3`. Summing gives (3.6).

### Proof of (ii)

Fix `L in H` and inspect the elements strictly between `x` and `a` in the displayed linear order. Swapping the positions of `x` and `a` changes no relative order except relations involving one of those two endpoints and an intervening vertex.

For an intervening `v`, invalidity can therefore occur only if

- `x<v` in the poset, because after the swap `v` would precede `x`; or
- `v<a` in the poset, because after the swap `a` would precede `v`.

The two relations cannot both hold, since `x<v<a` would imply `x<a`, contrary to `x||a`.

If `x<v`, then `v<a` is impossible by the previous sentence, while `a<v` is impossible because the original linear extension has `v` before `a`. Hence `v||a`, giving (L1).

If `v<a`, then `x<v` is impossible, while `v<x` is impossible because the original extension has `x` before `v`. Hence `v||x`, giving (L2).

Conversely, an intervening vertex of either type makes the swap invalid. Thus every bad left swap has at least one blocker of exactly the claimed form.

### Proof of (iii)

The argument is the order-reversed positional analogue. In `L in H`, an element `w` strictly between `a` and `y` can invalidate the swap `a <-> y` only if

- `a<w`, which forces `w||y`; or
- `w<y`, which forces `w||a`.

The two ordered relations cannot hold simultaneously because `a<w<y` would imply `a<y`, contrary to `a||y`. This gives (R1)-(R2).

### Proof of (iv)

Exclude the endpoints `x,y,a`. There are four possible intersections between a left type and a right type:

1. `(L1) and (R1)` would require both `v||a` and `a<v`;
2. `(L1) and (R2)` would require `x<v<y`, contradicting the cover `x lessdot y`;
3. `(L2) and (R1)` would require `v<a<v`;
4. `(L2) and (R2)` would require both `v<a` and `v||a`.

Every case is impossible. Hence `V_L` and `V_R` are disjoint. Since (i)-(iii) show that each bad-event family is nonempty and supplies an active blocker, both vertex sets are nonempty.

### Proof of (v)

Let `Z` be a saturated chain containing the cover edge `x lessdot y`. Because it is a chain and `x lessdot y` is a cover, every other vertex of `Z` is either strictly below `x` or strictly above `y`.

In any middle extension `x<a<y`, every bridge vertex below `x` must occur before `x`, and every bridge vertex above `y` must occur after `y`. Such a vertex can never lie strictly between `x` and `a` or strictly between `a` and `y`, which is necessary for active blocking by (ii)-(iii). Thus active blockers are off the bridge. `square`

## 4. Canonical exact-weight channel decomposition

The theorem gives not merely existence but a natural way to retain the exact extension weights demanded by account01/B19.

For every `L in B_L`, scan from `x` toward `a` and assign `L` to the first active blocker encountered. Let

`lambda_v := #{L in B_L : v is that canonical left blocker}`.   (4.1)

For every `L in B_R`, scan from `a` toward `y` and assign it to the first active right blocker, defining

`rho_w := #{L in B_R : w is that canonical right blocker}`.    (4.2)

Then these are disjoint exact partitions of the bad-event families, so

`sum_{v in V_L} lambda_v = |B_L| >= H-A`,

`sum_{w in V_R} rho_w = |B_R| >= H-C`.                         (4.3)

All nonzero `lambda_v` and `rho_w` occur off the bridge, and no vertex can receive both a left and a right channel weight by (3.7).

Thus the heavy `F*G` cover flux from the partner/lead state has now been converted into **two disjoint weighted off-corridor channel families**, rather than two unweighted relation witnesses. The total certified active-channel incidence obeys

`sum lambda_v + sum rho_w >= 3H-E > 0`.                         (4.4)

No claim is made that a single `lambda_v` or `rho_w` is bounded below by a universal positive fraction of `E`; there can be arbitrarily many candidate blockers. That individualization/recycling issue is the next unpaid step.

## 5. Direct application to the B10 bridge

Return to account04/B10 r14's saturated bridge

`c=z_0 lessdot ... lessdot z_j=x lessdot y=z_{j+1} lessdot ... lessdot z_k=u`.

B10 r14 already proves

`p=Pr(x<a)>2/3`, `q=Pr(y<a)<1/3`, and `H/E=p-q>1/3`.

Its Corollary 5.1 observes that when the bridge is long, nonendpoint `z_i` can themselves be counted among the partner's static relation distinguishers. That is precisely the loophole preventing the witness count from proving off-corridor branching for `k>=3`.

Theorem 3.1(v) removes that loophole completely:

> **Heavy bridge active-export corollary.** For every lead heavy transition edge, regardless of bridge length, there is a nonempty left active-blocker family and a nonempty right active-blocker family, the two vertex families are disjoint, every active blocker lies off the saturated bridge, and their exact full-extension masses satisfy (4.3)-(4.4).

In particular, bridge vertices may still be relation distinguishers in the sense of account01/B19, but they carry **zero active-swap blocker weight** for this middle-flux charging mechanism. The mass excess that makes the cover transition heavy must be paid by genuinely off-bridge vertices on both sides.

This is the first missing weighted channel implication requested by the lead and partner. It is arbitrary-size and does not use a finite-radius termination hypothesis.

## 6. Sharpness on the partner's five-point heavy-flux witness

The account01/B19 report uses the five-element poset generated by

`0<2`, `0<3`, `1<2`,

with `x=0`, `y=2`, `a=4`. It has

`E=25`, `Pr(x<a)=18/25`, `Pr(y<a)=7/25`, `H=11`.

The present decomposition gives exactly

`A=7`, `H=11`, `C=7`,
`|B_L|=4=H-A`,
`|B_R|=4=H-C`.

The sole active left vertex is `3`, and the sole active right vertex is `1`. Thus both weighted inequalities are attained with equality, and the two-sided/off-bridge conclusion is sharp even in the partner's own minimal heavy-flux example. That example still has balanced escape pairs, as account01/B19 records, so it is regression/sharpness evidence rather than a POS3 counterexample.

## 7. Deterministic regression

The companion checker `verify_pos3_active_blocker.py` independently exhausts every naturally labelled transitive closure through six vertices and every cover/incomparable triple. It verifies the swap injections, the blocker characterizations, the disjoint relation-capable channel sets, and the weighted inequalities. Recorded output is:

```text
naturally_labelled_transitive_closures 5228
cover_incomparable_triples 36292
strong_cover_flips 3991
middle_extensions_checked 95581
minimum_left_bad_minus_H_minus_A 0
minimum_right_bad_minus_H_minus_C 0
sharp_witness_E_A_H_C 25 7 11 7
sharp_witness_bad_left_right 4 4
sharp_witness_active_left_vertices [3]
sharp_witness_active_right_vertices [1]
POS3_TWO_SIDED_ACTIVE_BLOCKER_REGRESSION_PASS
```

The zeros in the two minimum-excess lines confirm that (3.4) is actually tight in the finite regression. The arbitrary-size result is the symbolic proof above; the enumeration is only a regression and sharpness check.

## 8. Exact remaining obligation

The active-export theorem advances, but does not finish, the lead's two-channel recycling problem. The remaining universal step is now more specific:

1. every lead heavy edge has exact off-bridge channel weights `lambda_v` and `rho_w` satisfying (4.3);
2. no vertex can carry both left and right channel types for the same heavy edge;
3. one must now show that, along repeated neutral-corridor/fork transitions, these weighted off-bridge channels cannot be reassigned indefinitely to the same finite collection of vertices without one of the lead's terminal outcomes: a balanced incomparable pair, strict strong-majority span descent, a proper autonomous reduction, or a controlled multi-distinguisher/non-crossed exit carrying the target-scale charge forward.

A proof of this next step must control **reuse of the canonical channel weights**, not merely count distinct relation witnesses. The current theorem deliberately does not assert a universal lower bound for an individual `lambda_v` or `rho_w`.

The non-bridged terminal-selector branch and separate non-crossed successor branch from B10 r14 also remain unpaid. Therefore POS3 is still open.

## 9. Status and provenance

- B10 r14 heavy bridge theorem: consumed at exact blob `50bac494667235f3630991a512438eac42c30521`.
- Assigned OTHER-account B19 exact flux/two-witness theorem: consumed at exact blob `003d2bf0593cb55f11738f50d68509413bb8d234`.
- Two-sided active-blocker theorem: **PROVED**.
- Exact weighted off-bridge channel decomposition: **PROVED**.
- Long-bridge static-witness loophole: **CLOSED for active swap-blocker charging**.
- Weighted channel reuse/termination: **OPEN**.
- POS3: **OPEN / NOT PROVED**.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning level and provider reasoning-token/thinking-time counters are `UNKNOWN / NOT_EXPOSED`, not zero. Elapsed execution is recorded in the operational receipt and is not pure thinking time.

Scoped provenance/privacy review: this report contains only mathematics, repository-relative source references, deterministic nonsecret code/output and logical run labels. It contains no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, paid model/API/Codex execution, remote workflow dispatch, public posting, permission changes, notification enablement or production-brain mutation.
