# POS3 fleet01/B11 — active defect support purifies into two opposite-ray modes

**Run:** `20260922T081324Z-b11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below refer to the original uniform law on the full linear extensions of the original poset. No deletion-induced distribution is treated as uniform.

## 1. Latest complete state consumed

The latest complete campaign-lead report is

- fleet04/B10 r18, `proofnet24/collective-POS3/fleet04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

R18 proves that every surviving outward four-channel export recreates a lead-type heavy Hasse bridge and that a two-step ray switch has only three local outcomes: strict span descent, strict strong-order envelope expansion, or exact backtrack through that heavy bridge. In the low-endpoint exact-backtrack branch, writing

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

`A=#{a<x<y}`, `H=#{x<a<y}`, `C=#{x<y<a}`, `E=A+H+C`,

we have

`A,C<3E/11`, hence `H>5E/11`.

The exact canonical outgoing blocker families inherited from lead r16 are

`F1={r:x lessdot r, r||a, r!=y}`,
`F2={r:r lessdot a, r||x}`,
`F3={r:a lessdot r, r||y}`,
`F4={r:r lessdot y, r||a, r!=x}`.

A bad left swap `x <-> a` is assigned to `F1 union F2`; a bad right swap `a <-> y` is assigned to `F3 union F4`. Let `B_L,B_R` be the corresponding bad middle-extension sets. Lead r16 gives

`|B_L| >= H-A > 2E/11`,
`|B_R| >= H-C > 2E/11`,                                      (1.1)

and the width-three cardinality bounds

`|F1|<=1`, `|F2|<=2`, `|F3|<=2`, `|F4|<=1`.                  (1.2)

It also gives the lossless boundary recoding:

- every positive `F2/F4` mark is a minority mark on an actual left-ray pair `(r,x)` with `r prec_* x`;
- every positive `F1/F3` mark is a minority mark on an actual right-ray pair `(y,r)` with `y prec_* r`.

The required named OTHER-account partner consumed and applied is

- fleet02/B19 r11, `proofnet24/collective-POS3/fleet02/B19/20260922T071111Z-fleet02-B19-pos3-r11/REPORT.md`, blob `3dda5f9df837b64f7cf7fc6103eb353284ca60dd`, together with its later addendum blob `d0eba0343a375499b460fd29336064c81d16cfc0`.

B19 proves that two positive outgoing boundary pairs on the same strong-order ray force either a balanced blocker cross-pair or a strict strong-majority subspan; its exact 108-extension width-three core also shows that opposite-ray boundary anchors alone need not expose the balanced pair.

For the quantitative radius corollary I additionally use fleet03/B10 r12, `proofnet24/collective-POS3/fleet03/B10/20260922T071308Z-fleet03-B10-r12-turning/REPORT.md`, blob `7c194b61648e3a61dd64cfe06ee12bf9739b6123`, whose inherited actual-law estimate is

`m(u,v) < 2125440/(d_*(u,v)+1)^2`                             (1.3)

for every strong incomparable pair in a hypothetical no-balanced candidate, where `m` is its minority probability and `d_*` its strong-order distance.

## 2. First missing implication attacked

R18 leaves the non-exact/multi-distinguisher low-endpoint exact-backtrack bridge as a genuine unpaid branch. At first sight its extra failed-swap mass can occupy all four Hasse families, and a mixed `F1/F2/F3/F4` support could feed a complicated cross-envelope recycler.

The new observation is that after the already authorized balance and strict-span exits have been removed, **the whole positive defect support, not just the two largest selected packets, must purify into exactly one of two opposite-ray modes**. This removes every mixed four-family backtrack state.

## 3. Active-support purification theorem

Fix a deterministic canonical Hasse witness for each bad swap as in the lead construction. Write `F_i^+` for the vertices in `F_i` that receive positive assigned weight.

### Theorem 3.1 — only two pure support modes survive

Assume the low-endpoint heavy state (1.1), and assume that neither an actual balanced pair nor an authorized strict strong-majority span descent has occurred. Then exactly one of the following holds.

**Mode T — through-`a`:**

`F1^+=F4^+=emptyset`,
`F2^+ != emptyset`, `F3^+ != emptyset`.

Thus every positive left-swap defect uses a lower cover of `a`, and every positive right-swap defect uses an upper cover of `a`.

**Mode F — fork-fork:**

`F2^+=F3^+=emptyset`,
`F1^+ != emptyset`, `F4^+ != emptyset`.

Thus every positive left defect uses the unique possible sibling upper-fork channel and every positive right defect uses the unique possible sibling lower-fork channel.

No mixed third mode survives.

### Proof

Suppose first that `F1^+` and `F3^+` are both nonempty. Choose positive blockers `b in F1^+` and `u in F3^+`. By the lead's boundary recoding, `(y,b)` and `(y,u)` are two distinct actual incomparable pairs on the same right strong-order ray, both with `y prec_* b,u`. If `b||u` is balanced, we are done. Otherwise the no-balanced hypothesis, or ordinary comparability if `b,u` are comparable in the poset, orders them strictly in `prec_*`; after relabeling,

`y prec_* b prec_* u`.

Then `(y,b)` is a strict strong-majority subspan of `(y,u)`, an authorized span-descent exit. Hence in the surviving branch

`F1^+` and `F3^+` cannot both be nonempty.                         (3.1)

The order-dual same-ray argument gives

`F2^+` and `F4^+` cannot both be nonempty.                         (3.2)

By (1.1), both bad-swap sets are nonempty. Therefore at least one of `F1^+,F2^+` is nonempty and at least one of `F3^+,F4^+` is nonempty.

If `F1^+` is nonempty, (3.1) forces `F3^+=emptyset`, so right positivity forces `F4^+` nonempty. Then (3.2) forces `F2^+=emptyset`. This is Mode F.

If `F1^+` is empty, left positivity forces `F2^+` nonempty. Then (3.2) forces `F4^+=emptyset`, so right positivity forces `F3^+` nonempty. This is Mode T. `square`

The point is stronger than the earlier statement that the two *selected* large packets can be taken on opposite rays: after balance/span descent is excluded, **every positive canonical defect channel is forced into one pure type-pair**.

## 4. Quantitative gain in the two modes

### Theorem 4.1 — Mode T improves the packet floor from `2/33` to `1/11`

In Mode T the left mass `|B_L|` is partitioned among at most two `F2` vertices and the right mass `|B_R|` among at most two `F3` vertices. Hence there exist

`t in F2^+`, `u in F3^+`

with assigned weights

`lambda_t > E/11`, `rho_u > E/11`.                              (4.1)

The boundary recoding therefore gives actual incomparable pairs with

`Pr(x<t) > 1/11`,
`Pr(u<y) > 1/11`.                                               (4.2)

Moreover every `F2` blocker satisfies `t lessdot a`, every `F3` blocker satisfies `a lessdot u`, so for every cross choice

`t < a < u`                                                     (4.3)

in the poset. Thus **all cross-blocker pairs in Mode T are comparable**. Any remaining proof of this branch must use cover-pivot/envelope charge; a blocker-blocker balanced-pair shortcut is structurally unavailable.

Applying (1.3) to (4.2), every selected Mode-T packet has

`d_* <= 4834`.                                                  (4.4)

### Theorem 4.2 — Mode F carries the entire side defects on two unique blockers

In Mode F, (1.2) says there is a unique positive `b in F1` and a unique positive `c in F4`. Consequently

`lambda_b=|B_L|>2E/11`,
`rho_c=|B_R|>2E/11`.                                            (4.5)

An `F1` bad mark has

`x<b<a<y`,

so the same mark is simultaneously a minority mark for both actual pairs `(a,b)` and `(y,b)`. An `F4` bad mark has

`x<a<c<y`,

so it is simultaneously a minority mark for `(c,x)` and `(c,a)`. Therefore

`Pr(b<a), Pr(b<y), Pr(x<c), Pr(a<c) > 2/11`.                   (4.6)

All four quantities are still `<1/3` in a hypothetical counterexample. Their containment of the full side-defect sets also gives

`H-A < E/3`, `H-C < E/3`,

hence

`2A+C > 2E/3`,
`A+2C > 2E/3`.                                                  (4.7)

In particular

`A>13E/66`, `C>13E/66`,
`A+C>4E/9`,
`5E/11 < H < 5E/9`.                                            (4.8)

Thus the fork-fork backtrack is forced into a substantially narrower numerical window than the generic low-endpoint branch.

By (1.3), each of the four Mode-F packet pairs in (4.6) has

`d_* <= 3418`,                                                  (4.9)

while the old endpoint pairs, using `A,C>13E/66`, satisfy `d_*<=3283`.

### A further exact fork-fork intersection identity

Let `D=B_L cap B_R`. In Mode F, every `L in D` has the literal order

`x<b<a<c<y`,                                                    (4.10)

so in particular `b<c` in that extension. Inclusion-exclusion inside the middle class gives

`|D| >= |B_L|+|B_R|-H`
`     >= (H-A)+(H-C)-H`
`      = 2H-E`.                                                 (4.11)

The only possible poset comparability between the fork blockers is `c<b`: the opposite relation `b<c` together with `c<y` would contradict `b||y`. Hence, if `H>E/2`, (4.11) forces `b||c`; the strong-order ray locations give `c prec_* b`, and

`Pr(b<c) >= 2H/E-1`.                                           (4.12)

If instead `H<=E/2`, then `A+C>=E/2`, and the individual upper bounds `A,C<3E/11` sharpen to

`A,C>5E/22`.                                                    (4.13)

Equations (4.11)-(4.13) are exact full-extension statements, not an induced-law approximation.

## 5. Direct application to the assigned partner's 108-extension adversary

I independently reconstructed the exact fleet02/B19 width-three core from its cover list. For its heavy state `(x lessdot y;a)=(2 lessdot 0;5)` the computation gives

`E=108`, `(A,H,C)=(29,52,27)`,

`F1=[]`, `F2=[6]`, `F3=[7]`, `F4=[3]`,

`|B_L|=23`, with `lambda_6=23`,
`|B_R|=25`, with `rho_7=19`, `rho_3=6`.

Thus the partner's source-valid adversary has simultaneous positive `F2` and `F4` support on the left ray. Theorem 3.1 says that in a no-balanced/no-descent candidate such mixing cannot survive. And in the actual partner poset the promised exit is exactly visible:

`Pr(3<6)=60/108=5/9`,

so the `F2/F4` blocker cross-pair is balanced. This explains structurally why the partner example defeats an immediate-boundary-only rule but cannot survive the purified hypothetical-counterexample branch. Its two large selected packets `6 in F2` and `7 in F3` already exhibit the genuine Mode-T geometry; the extra positive `F4` channel is precisely where the balanced cross-pair enters.

The committed verifier reproduces these counts and ends with

`POS3_ACTIVE_SUPPORT_PARTNER_CHECK_PASS`.

## 6. Integration with lead r18

R18's unpaid exact-backtrack residue was the **non-exact / multi-distinguisher low-endpoint heavy bridge**. Theorem 3.1 now replaces that generic residue by two explicit source-valid normal forms:

1. **Mode T (through-`a`)** — at most two lower-cover channels and at most two upper-cover channels, every cross blocker comparable through `a`, and each side has an actual boundary packet of minority `>1/11` and strong-order radius at most `4834`;
2. **Mode F (fork-fork)** — exactly one active blocker on each side, each side's entire bad-swap mass is `>2E/11`, four associated actual pair minorities are `>2/11`, and the endpoint/middle masses obey (4.8), with the extra double-bad relation (4.11).

So an exact backtrack cannot hide its extra defect in an arbitrary mixed four-family frontier. All mixed support either already exposes a balanced pair or gives strict span descent.

## 7. First essential remaining implication

The first unpaid implication can now be split, without weakening the parent target, into the following two pure-mode statements.

> **`POS3-PURE-MODE-CROSS-ENVELOPE-EXIT-v1`.** In a span-descent-exhausted, no-balanced width-three candidate, show that a cross-envelope recycler built from r18 exact backtracks and strict envelope expansions cannot persist in either of the two purified low-endpoint modes:
>
> - **Mode T:** reciprocal cover pivots through `F2/F3` with side packet floors `>1/11` and all cross blockers ordered through the central vertex `a`;
> - **Mode F:** the unique `F1/F4` fork pair with full side-defect floors `>2/11`, the mass window `5/11<H/E<5/9`, and the double-bad lower bound `|B_L cap B_R|>=2H-E`.
>
> Prove that the first reuse of a previously exposed strong-order envelope forces a balanced pair, strict span descent, a proper autonomous/ordinal reduction, or one of the already controlled exact-two/non-crossed exits.

This is strictly narrower than r18's generic `POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`. POS3 itself remains open.

## 8. Status and integrity

- latest lead fleet04/B10 r18: **CONSUMED/APPLIED**;
- assigned partner fleet02/B19 r11 + late addendum: **CONSUMED/APPLIED**;
- whole positive active support purifies to `F2/F3` or `F1/F4`: **PROVED**;
- mixed four-family low-endpoint backtrack support: **ELIMINATED modulo balance/span descent**;
- Mode-T packet floor `>1/11` and comparable cross blockers: **PROVED**;
- Mode-F full-side packet floor `>2/11`, endpoint window, and double-bad identity: **PROVED**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

The verifier is used only to reconstruct the named partner's exact finite witness; the arbitrary-size purification and quantitative statements above are symbolic proofs. No novelty or publication-priority claim is made.

Scoped privacy/provenance review: this report contains only mathematical statements, logical account/slot/run labels, repository-relative source references and nonsecret Git object identifiers. It contains no benchmark gold, held-out keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid or remote model/API/Codex execution, workflow dispatch, permission change or public-posting action.
