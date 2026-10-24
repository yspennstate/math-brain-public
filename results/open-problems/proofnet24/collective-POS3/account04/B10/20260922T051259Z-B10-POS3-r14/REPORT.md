# POS3 account04/B10 — bridged blocker corridors force a target-scale heavy cover flux

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no installation or benchmark work and makes no novelty or priority claim. Every probability below is under the original uniform law on all full linear extensions.

## 1. Exact state consumed

The latest complete campaign-lead report consumed is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

That report proves, in the strict delayed-predecessor corridor after strong-majority span descent is exhausted, a canonical incomparable pair with minority probability in `(1/6,1/3)`. In the majority-late small-endpoint branch it proves that the smaller-predecessor endpoint `b` has exactly two Hasse-successor blockers `u_1,u_2`, and that the previous fork endpoint `c` satisfies `c<u_i` for at least one blocker. Its first unpaid target-level step is a global amplification/charge theorem through the resulting three-chain corridor.

The assigned **OTHER-account partner** input consumed and applied is

- account01/B11, `proofnet24/collective-POS3/account01/B11/20260922T041226Z-B11-pos3-r11/REPORT.md`, blob `25c37b00c097cd863fb6e2898af10b135927cd83`.

It proves that in the exact-two terminal geometry the set

`N(a,b)={v:v||a and v||b}`

is a chain in width at most three, and reduces the comparable-outer residual to a one-dimensional neutral-chain corridor. It also gives exact deep-fiber decay in that corridor.

A second named OTHER-account input used directly is

- account01/B19, `proofnet24/collective-POS3/account01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, blob `003d2bf0593cb55f11738f50d68509413bb8d234`.

Its exact three-chain flux formula identifies a probability drop across a cover as literal `F*G` edge mass. Its Cover Two-Witness Theorem says that if `x lessdot y` and `a||x,y`, then a strong cover flip

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`

cannot occur in a no-balanced poset with at most one external relation distinguisher after the unavoidable cover endpoints are removed: at least two distinct external witnesses are forced.

I also use account02/B10,

- `proofnet24/collective-POS3/account02/B10/20260922T044758Z-b10-r12-9941265a/REPORT.md`, blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`,

which upgrades the local strict-chain terminal selector to minority at least `1/5`, and to at least `1/4` in the exact-two branch, via defect/arity compression. This makes clear that the remaining obstruction is global rather than another local constant improvement.

Finally, account03/B19,

- `proofnet24/collective-POS3/account03/B19/20260922T045925Z-b19-pos3-r12/REPORT.md`, blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`,

proves that two consecutive exact-two crossed states carry a conserved latent mass `K` with `E/3<K<2E/3`; the first missing global step there is boundary realization of that balanced-sized charge.

The source claim and frozen frontier remain `operations/claims/I0122.md`, blob `b9dac0d3f56b5119e495fc70f71769100124fc58`: `n_bal=14` is partial and does not close the universal conjecture.

## 2. Compact conditional end-to-end route

Assume for contradiction-search purposes that `P` is a finite width-at-most-three poset with no balanced incomparable pair, and use the inherited transitive strong-majority order `prec_*`.

The lead's majority-late small-endpoint branch supplies

- `c||a`, `c||b`, `a||b`;
- `c prec_* b prec_* a`;
- a Hasse blocker `b lessdot u` with `u||a` and `a prec_* u`;
- the width-three bridge relation `c<u`.

The missing amplification question is whether this bridge can carry only diffuse subcritical mass. The theorem below proves that it cannot: **every such bridge contains a unique cover edge carrying strictly more than one third of all linear extensions as the event that `a` falls inside that cover gap**.

Therefore the bridged branch already creates target-scale `>E/3` flux. Applying the account01/B19 two-witness theorem shows that, in a hypothetical counterexample, this heavy edge must immediately export into at least two distinct external asymmetry channels. Thus a bridged two-blocker branch cannot terminate silently or continue as a one-channel obstruction.

This pays the first charge-transfer implication for the bridged branch. It does not yet prove that the two witness channels themselves terminate in a balanced pair; that remains the global recycling/realization obligation.

## 3. Bridge corridor theorem

### Theorem 3.1 — a lead bridge contains a unique heavy cover cut

Let `P` be any finite poset with no balanced incomparable pair. Suppose `a,c,u` satisfy

`c<u`, `c||a`, `u||a`, and `c prec_* a prec_* u`.              (3.1)

Take any saturated chain

`c=z_0 lessdot z_1 lessdot ... lessdot z_k=u`.                 (3.2)

Then:

1. every `z_i` is incomparable with `a`;
2. the sequence

   `f_i:=Pr(z_i<a)`                                             (3.3)

   is nonincreasing;
3. there is a unique index `j` with

   `f_j>2/3` and `f_{j+1}<1/3`;                                (3.4)

4. the corresponding cover edge carries exact flux

   `Pr(z_j<a<z_{j+1})=f_j-f_{j+1}>1/3`.                        (3.5)

#### Proof

If some internal `z_i<a`, then `c<z_i<a`, contradicting `c||a`. If `a<z_i`, then `a<z_i<u`, contradicting `a||u`. Thus every `z_i||a`, proving item 1.

Because `z_i<z_{i+1}`, the event `{z_{i+1}<a}` is contained in `{z_i<a}`, so `f_i>=f_{i+1}`. This proves item 2.

The strong-majority orientation in (3.1), together with incomparability, gives

`f_0=Pr(c<a)>2/3`,
`f_k=Pr(u<a)<1/3`.                                             (3.6)

No pair `(z_i,a)` is balanced, so each `f_i` lies outside `[1/3,2/3]`. A nonincreasing sequence beginning above `2/3` and ending below `1/3` therefore crosses from the upper region to the lower region at one unique adjacent index `j`, proving item 3.

Finally, because `z_j<z_{j+1}` and both are incomparable with `a`, every extension contributing to `z_j<a` either has `z_j<a<z_{j+1}` or `z_j<z_{j+1}<a`, while the latter event is exactly `{z_{j+1}<a}`. Hence

`Pr(z_j<a)-Pr(z_{j+1}<a)=Pr(z_j<a<z_{j+1})`.                  (3.7)

Using (3.4) gives (3.5). `square`

The theorem is arbitrary-size. It uses no projected/deletion law and no finite census.

## 4. The lead bridge is exactly a neutral-chain corridor up to its blocker endpoint

Return to the lead's majority-late small-endpoint branch and choose the blocker `u` for which `c<u`. Recall also

`c||b`, `b lessdot u`, `c prec_* b prec_* a prec_* u`.         (4.1)

Take a saturated bridge chain (3.2).

### Lemma 4.1

Every `z_i` with `i<k` is incomparable with `b`. Therefore

`z_0,...,z_{k-1} in N(a,b)`.                                  (4.2)

#### Proof

Item 1 of Theorem 3.1 already gives `z_i||a`. Suppose `i<k`.

If `z_i<b`, then `c<=z_i<b`, contradicting `c||b`. If `b<z_i`, then `b<z_i<u`, contradicting the Hasse cover `b lessdot u`. Hence `z_i||b`. `square`

By the account01/B11 result, `N(a,b)` is a chain. Thus the lead bridge is not an unrelated auxiliary path: all of its vertices except the terminal blocker lie on the exact one-dimensional neutral corridor isolated independently by the assigned partner.

Theorem 3.1 therefore identifies the neutral corridor's strong-majority cut with a literal heavy cover edge.

## 5. Target-scale charge must branch twice

Let

`x=z_j`, `y=z_{j+1}`                                           (5.1)

be the unique transition edge from Theorem 3.1. Then

`x lessdot y`, `a||x,y`,
`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,
`Pr(x<a<y)>1/3`.                                               (5.2)

Apply account01/B19's Cover Two-Witness Theorem to the cover `x lessdot y` and the incomparable point `a`. Define

`D(v,a)={w notin {v,a}: rel(w,v) != rel(w,a)}`.                (5.3)

In a no-balanced poset we must have

`|(D(x,a)\{y}) union (D(y,a)\{x})| >= 2`.                     (5.4)

This is the promised first global charge implication:

> **Bridged blocker charge theorem.** Every width-three lead bridge from the majority-late two-blocker branch contains a cover edge carrying more than `E/3` full-extension mass, and that heavy edge must export through at least two distinct external relation channels in any hypothetical POS3 counterexample.

No choice of a single canonical blocker can absorb the charge.

### Corollary 5.1 — short bridges force genuinely off-bridge witnesses

The saturated bridge has `k+1` vertices. Every bridge vertex other than `x,y` is itself an external distinguisher for the cover pair relative to `a`: a vertex before `x` is below `x` but incomparable with `a`, while a vertex after `y` is above `y` but incomparable with `a`.

Hence the number of witnesses forced **outside the bridge** is at least

`max(0, 2-(k-1))`.                                             (5.5)

In particular:

- if `c lessdot u` (`k=1`), at least two off-bridge witnesses are forced;
- if the bridge has two covers (`k=2`), at least one off-bridge witness is forced;
- if `k>=3`, the bridge itself already contains at least two nonendpoint witness vertices for the heavy transition edge.

Thus every bridged branch has a clean length-or-branch alternative: either the neutral corridor has genuine depth, or new asymmetry channels are forced outside it.

## 6. Relation to the latent-`K` corridor and the remaining charge problem

The account03/B19 result shows that two consecutive exact-two crossed states transport a latent integer `K` with

`E/3<K<2E/3`.                                                   (6.1)

Its missing step is to realize that balanced-sized mass at a maximal corridor boundary, or export an equivalent charge into a multi-distinguisher/non-crossed exit.

The present theorem pays that boundary step for the **lead-bridge exit subclass** in the following exact sense: whenever the exact-two/fork corridor exits through the lead relation `c<u`, there is already an actual cover-gap event

`H={x<a<y}`                                                     (6.2)

with

`|H|>E/3`.                                                      (6.3)

Thus bridged exits cannot lose all target-scale mass into a diffuse tail. What is not proved is `|H|>=K`; no such inequality is claimed. The remaining task is to show that the two external channels forced by (5.4) cannot recycle this `>E/3` edge mass indefinitely without producing a balanced pair, strict span descent, an autonomous reduction, or the already-isolated multi-distinguisher/non-crossed exit.

This is more specific than the previous generic instruction to perform a global charge: the charge is now a concrete `F*G` cover edge with mass `>E/3`.

## 7. Source-valid counterexample to fixed-outside chain-module lifting

As an adversarial check on a different possible induction route, I tested the tempting statement:

> if contracting an autonomous chain `M` to `z` gives a balanced quotient pair `(z,x)`, then some descendant `c in M` gives a balanced pair `(c,x)` with the **same outside endpoint** `x`.

This statement is false even in width two.

Let the core poset be the disjoint union

`M=(c_1<c_2)` and `Y=(y_1<x<y_3)`.                             (7.1)

The module `M` is an autonomous chain, the incomparability graph is the connected graph `K_{2,3}`, and the poset has width two. Contracting `M` to `z` gives a singleton incomparable with the three-chain. There are four quotient extensions, with `z` in the four possible gaps, so

`Pr_Q(z<x)=1/2`.                                                (7.2)

Indeed `(z,x)` is the unique balanced quotient pair: the two other quotient probabilities are `1/4` and `3/4`.

The expanded core has exactly `C(5,2)=10` linear extensions. Direct shuffle counting gives

`Pr(c_1<x)=7/10`,
`Pr(c_2<x)=3/10`.                                               (7.3)

Thus **neither descendant paired with the same outside point `x` is balanced**. Balance survives only after the outside endpoint migrates:

`Pr(c_1<y_1)=2/5`,
`Pr(y_3<c_2)=2/5`.                                              (7.4)

For arbitrary finite order, take

`C_s op (C_2 disjoint_union C_3) op C_t`,                       (7.5)

with arbitrary `s,t>=0`. Forced ordinal prefix/suffix factors add no incomparable cross-pairs and leave all probabilities (7.2)-(7.4) unchanged. Hence this is an arbitrary-size source-valid family refuting fixed-outside descendant lifting.

This does **not** refute the broader global chain-module crossing sought by account02/B19, because a balanced descendant/outside pair still exists after the outside endpoint is allowed to migrate. It shows that any valid module induction must permit that migration and cannot keep the quotient's outside endpoint fixed.

## 8. Exact executable certificate for Section 7

The deterministic verifier saved with this run enumerates the ten interleavings of the two chains and the four quotient extensions. Recorded output:

```text
core_extensions 10
P(c1<y1)=4/10
P(c1<x)=7/10
P(c1<y3)=9/10
P(c2<y1)=1/10
P(c2<x)=3/10
P(c2<y3)=6/10
quotient_extensions 4
P_Q(z<x)=2/4
same_outside_descendants_balanced False
escape_balanced_pairs c1||y1 y3||c2
POS3_MODULE_LIFT_COUNTEREXAMPLE_PASS
```

Files:

- `verify_pos3_module_lift.py`, local executed SHA-256 `489930d6ebcef0741a98496065e67e31e708370c132275527043addcdf3dc2af`;
- `verify_pos3_module_lift.out`, local captured-output SHA-256 `b95716808d3f355ae66b82802de9a91bb9caf83d76a9b19e5aff34cb24e5e763`.

The bridge-cover theorem is symbolic and does not depend on this finite computation.

## 9. Exact remaining obligation

The lead branch now has the following conditional route.

1. The inherited first-fork funnel reaches the strict predecessor-nested corridor or descends in strong-majority span.
2. Local defect/arity compression supplies canonical minority at least `1/5`, and at least `1/4` in the exact-two branch.
3. In the lead's small-endpoint two-blocker subbranch, the width-three bridge `c<u` is no longer merely qualitative: Theorems 3.1 and 5.1 produce an actual cover-gap event of mass `>E/3`.
4. Any such heavy cover edge in a hypothetical counterexample has at least two external witness channels.
5. The next unpaid implication is therefore a **two-channel heavy-edge recycling theorem**: along the one-dimensional neutral corridor, show that repeated heavy cover edges and their two witness channels cannot be reused indefinitely without yielding a balanced incomparable pair, a strict span descent, a proper autonomous reduction, or a controlled multi-distinguisher/non-crossed exit carrying the charge forward.

The non-bridged terminal-selector branch and the separate non-crossed successor branch remain unpaid. No automatic truth promotion is made.

## 10. Status and integrity

- Lead bridge -> neutral corridor identification: **PROVED**.
- Unique `>E/3` heavy cover edge on every lead bridge: **PROVED**.
- At least two external witness channels on that edge in a hypothetical counterexample: **PROVED** by direct application of account01/B19's theorem.
- Fixed-outside autonomous-chain descendant lift: **REFUTED**, with an arbitrary-size width-two family and exact certificate.
- POS3: **OPEN / NOT PROVED**.
- I0122 finite frontier: `n_bal=14`, unchanged.
- Run classification: `ESSENTIAL_STEP_APPLIED`.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured effort and provider reasoning-token/thinking-time counters are `UNKNOWN / NOT_EXPOSED`, not zero. Elapsed execution is recorded separately in the operational receipt and is not pure thinking.

Scoped provenance/privacy review: this report contains only mathematical statements, repository-relative source references, deterministic nonsecret code/output and logical run labels. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, paid model/API/Codex execution, remote workflow dispatch, public posting, permission change, notification enablement or production-brain mutation was used.
