# POS3 account02/B19 — same-ray packets force descent; exact opposite-ray frontier adversary

**Run:** `20260922T071111Z-account02-B19-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the literal uniform law on all full linear extensions of the original poset. No deletion/projection law is renamed uniform, and no finite computation is promoted to arbitrary-size closure.

## 1. Exact collective state consumed

Fresh owner control remains revision `2026-09-22.2` under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; the owner stop on new brain-installation and benchmark work is respected.

The latest complete campaign-lead result actually consumed is:

- **account04/B10 r16**, `proofnet24/collective-POS3/account04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`, report blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`.

Its low-endpoint branch starts from a heavy cover state

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

with

`A=#{a<x<y}<3E/11`, `C=#{x<y<a}<3E/11`, `H=#{x<a<y}=E-A-C`.

After canonical Hasse reduction it proves two distinct fully outward boundary-anchored actual pairs, one from each failed-swap side, each carrying more than `2E/33` marked full extensions. Same-ray packets are classified as nested if the blocker vertices are comparable and as a width-saturating three-antichain gate if they are incomparable. The remaining lead obligation is `OUTWARD-STATE RECYCLING`.

The required named partner actually consumed is:

- **account03/B10**, `proofnet24/collective-POS3/account03/B10/b10-20260922t061504z-r11/REPORT.md`, report blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.

It proves that the exact-two recurrence reaches the first actual non-exact boundary with **zero probability defect**:

`A_prev + 3A + B = E + K`.

Thus extra distinguishers do not first appear as an additive correction to the boundary-pair probability; the residual is structural conversion of already-existing charge.

A later essential OTHER-account input was also consumed:

- **account04/B20**, science commit `79a609ff83b87121fbe66814dcb4bd66d94fa7e1`, handoff `proofnet24/collective-POS3/account04/B20/20260922T071019Z-b20-pos3-r11/HANDOFF.md`.

It proves canonical reverse-transposition/incoming cancellation moves to a strict strong-order **superinterval**, so pure incoming-cancellation steps are acyclic in the integer `span_*` potential. Its remaining obligation is mixed-mechanism outward recycling.

For the exact canonical frontier definitions I also use:

- **account04/B19**, `proofnet24/collective-POS3/account04/B19/B19-20260922T061559Z-r45/REPORT.md`, whose canonical sets are `T_L,U_L,U_R,T_R` and active sets `C_L=T_L union (U_L\{y})`, `C_R=U_R union (T_R\{x})`.

## 2. Compact conditional end-to-end route

Assume POS3 is false and take a cardinality-minimal no-balanced width-three counterexample. Use the inherited transitive strong-majority order `prec_*`.

The live route after the lead/partner inputs is:

1. obtain the lead's heavy cover state and exhaust strict span descent inside the old intervals `(x,a)` and `(a,y)`;
2. in the low-endpoint branch, export two distinct `>2E/33` fully outward boundary packets;
3. use the theorem below to eliminate the lead's entire **same-ray** recycling alternative by immediate balance-or-span-descent;
4. therefore a genuinely surviving two-packet state must export its lead-selected packets to **opposite rays**;
5. the exact prime example in Section 4 shows that opposite-ray boundary anchoring alone still need not expose the balanced pair: every immediate boundary-anchor pair can remain unbalanced while balance lives in a blocker-blocker cross pair / immediate child frontier;
6. combine this with account03/B10's zero-defect boundary recurrence and account04/B20's superinterval acyclicity. The first remaining global implication is an **opposite-ray cross-frontier / mixed-mechanism transfer theorem**, not a same-ray classification and not a scalar boundary correction.

## 3. Same-ray packet theorem: the lead's nested/gate branch already forces balance or strict span descent

### Theorem 3.1 — two same-ray r16 packets cannot survive the no-balance/no-descent branch

Take the two distinct fully outward actual pairs supplied by account04/B10 r16 Theorem 4.1.

If they lie on the right ray, write them as

`(y,r1)`, `(y,r2)`,

with `y||r1,r2` and

`y prec_* r1`, `y prec_* r2`.

If they lie on the left ray, dually write them as

`(r1,x)`, `(r2,x)`,

with `r1,r2||x` and

`r1 prec_* x`, `r2 prec_* x`.

Then **either** the blocker cross-pair `r1||r2` is balanced, **or** one of the two lead-selected boundary pairs has the other blocker vertex strictly inside its strong-order span. Hence the same-ray state has an immediate strict strong-majority span descent.

### Proof

Consider the right ray. If `r1||r2` is balanced, POS3 is already witnessed.

Otherwise there are two cases.

- If `r1,r2` are comparable, their poset order agrees with `prec_*` (this is already recorded in lead r16 Corollary 5.1).
- If `r1||r2` and the pair is not balanced, the hypothetical-counterexample assumption gives one strict strong-majority orientation between them.

In either case, after relabelling,

`r1 prec_* r2`.

Together with the two outward packet orientations this gives

`y prec_* r1 prec_* r2`.

Both `(y,r1)` and `(y,r2)` are incomparable actual pairs. Therefore `r1` is a strict strong-order interior vertex of the packet pair `(y,r2)`, and `(y,r1)` is a strict strong-majority subspan. This is exactly an authorized span descent.

The left-ray proof is dual: after relabelling one has

`r1 prec_* r2 prec_* x`,

so `(r2,x)` is a strict subspan of `(r1,x)` (or vice versa, depending on the relabelling).

Thus, once balance and strict span descent are both excluded, the two r16-selected packets **must lie on opposite rays**. `square`

### Consequence

This pays both local same-ray alternatives of lead r16 Corollary 5.1 at once. A nested channel is already a strict strong-order nesting; a width-saturating three-antichain gate either contains a balanced blocker cross-pair or becomes strictly ordered by `prec_*` and again gives a strict subspan.

So the global `OUTWARD-STATE RECYCLING` residual can be narrowed to the **opposite-ray** case.

## 4. Exact connected autonomous-prime opposite-ray adversary

The following eight-element poset is an exact regression guard against the tempting next shortcut “two opposite-ray r16 packets, or even the whole immediate boundary-anchor frontier, must already contain a balanced pair.”

Its transitive-reduction covers are

`1<2, 1<6, 2<0, 2<7, 3<0, 3<4, 4<7, 5<7, 6<0, 6<4, 6<5`.

It has the three-chain cover

`(1<2<0)`, `(3<4<7)`, `(6<5)`

and the 3-antichain `{2,3,5}`, so its width is exactly three. Both comparability and incomparability graphs are connected, and exhaustive relation checking finds **no nontrivial proper autonomous subset**. Thus the core is connected and autonomous-prime rather than an ordinal/module artefact.

There are exactly

`E=108`

uniform linear extensions.

Take the heavy state

`(x lessdot y; a)=(2 lessdot 0; 5)`.

The exact heavy partition is

`A=29`, `H=52`, `C=27`,

so

`A/E=29/108 < 3/11`,

`C/E=1/4 < 3/11`,

`H/E=13/27 > 1/3`.

There is no strong-majority interior vertex in either old interval `(2,5)` or `(5,0)`, so this is genuinely in the lead's no-old-span low-endpoint geometry.

### Canonical frontier and exact r16 packet weights

The canonical sets are

`T_L={6}`, `U_L={0}`, `U_R={7}`, `T_R={2,3}`,

hence

`C_L={6}`, `C_R={3,7}`.

The exact deterministic bad-swap assignment gives

`|B_L|=23`, `lambda_6=23`,

`|B_R|=25`, `rho_3=6`, `rho_7=19`.

Since

`2E/33 = 72/11`,

the lead-selected `>2E/33` packets are necessarily blocker `6` on the left side and blocker `7` on the right side. They lie on opposite rays.

Yet **every immediate boundary-anchor pair in the full canonical frontier is unbalanced**:

- `6 in F2`: minority `Pr(2<6)=35/108 < 1/3`;
- `7 in F3`: minority `Pr(7<0)=11/36 < 1/3`;
- `3 in F4`: minority `Pr(2<3)=11/36 < 1/3`.

So even after lead r16's lossless boundary-anchor recoding and even after inspecting the entire immediate canonical boundary-anchor set, no balanced pair appears.

### Where the balance actually migrates

The two same-left-ray blocker vertices `6 in F2` and `3 in F4` are incomparable; together with boundary endpoint `2` they form the lead's width-saturating gate `{2,3,6}`. Their **cross-pair**, not either boundary pair, is balanced:

`Pr(3<6)=60/108=5/9`.

The two lead-selected packets also create genuine reciprocal heavy children:

- blocker `6` gives `(6 lessdot 5; pivot 2)` with heavy partition `(35,44,29)`;
- blocker `7` gives `(5 lessdot 7; pivot 0)` with heavy partition `(27,48,33)`.

On both immediate child frontiers the same pair `{4,5}` becomes exposed, with

`Pr(4<5)=47/108`,

again balanced.

Thus the exact obstruction is not that balance disappears. It is that **boundary anchoring alone does not see it**. The balance may sit in a blocker-blocker cross pair or one canonical transition deeper.

### All incomparable-pair probabilities

The verifier checks all eleven incomparable pairs exactly:

- `(0,4): 31/108`;
- `(0,5): 1/4`;
- `(0,7): 25/36`;
- `(1,3): 41/54`;
- `(2,3): 11/36`;
- `(2,4): 85/108`;
- `(2,5): 79/108`;
- `(2,6): 35/108`;
- `(3,5): 47/54`;
- `(3,6): 5/9` **balanced**;
- `(4,5): 47/108` **balanced**.

Hence this is **not** a POS3 counterexample. It is a source-valid adversary to an immediate-boundary-only closure of the current selector.

## 5. Arbitrary-size ordinal amplification

For arbitrary `s,t>=0`, the ordinal sum

`C_s op P op C_t`

has width exactly three (when the core `P` is present) and every incomparable pair lies inside `P`. Every linear extension is the forced prefix chain, one of the 108 core extensions, then the forced suffix chain, so every internal probability above is unchanged.

More generally an ordinal sum of `k` copies of `P` has `108^k` extensions and reproduces the same local obstruction in every block. These padded examples are deliberately **not** used against the minimal-counterexample reduction because they are ordinal-decomposable; they only show the local selector obstruction is not a small-size accident.

## 6. Applying the named partner and the new B20 result

The named partner account03/B10 excludes a scalar repair: at the first non-exact boundary the probability recurrence has zero additive defect, so one cannot hope that the extra opposite-ray distinguisher simply contributes a positive correction to the next pair probability.

Account04/B20 independently excludes a second local cycling mechanism: pure incoming/reverse-transposition cancellation strictly increases strong-order span and therefore cannot cycle by itself.

Theorem 3.1 here excludes a third mechanism: the **two r16-selected packets cannot remain on the same ray** after balance and span descent are excluded.

Therefore any genuinely surviving cycle in a hypothetical counterexample must use **opposite-ray outgoing packets and mix transition mechanisms**. The eight-element core shows why the next theorem must inspect cross-frontier structure rather than only the two boundary anchors.

## 7. Accepted gate and first essential missing implication

**Before this run:** lead r16 left both same-ray nested/gate recycling and opposite-ray recycling inside `OUTWARD-STATE RECYCLING`.

**After this run:**

1. the entire same-ray branch is paid by the symbolic balance-or-strict-subspan theorem above;
2. the surviving low-endpoint two-packet branch can be assumed to send its selected packets to **opposite rays**;
3. a connected autonomous-prime width-three exact witness shows that all immediate boundary-anchor pairs can remain unbalanced in that opposite-ray geometry;
4. in that witness the balance is recovered by a blocker-blocker cross pair and again on the immediate child frontiers.

The first essential missing implication is therefore:

> **OPPOSITE-RAY CROSS-FRONTIER / MIXED-MECHANISM TRANSFER.** In a cardinality-minimal no-balanced width-three candidate, starting from the two opposite-ray `>2E/33` packets of lead r16, use the bounded canonical blocker sets together with the exact-two conserved charge `K` and the incoming-superinterval theorem to prove that a blocker-blocker cross pair, a one-step child frontier, or a mixed bridge/exact-two transition must force balance, strict strong-majority span descent, a proper autonomous/ordinal reduction, a four-antichain contradiction, or a quantitatively charge-preserving new state. Boundary-anchor probabilities alone are insufficient.

This is strictly narrower than the lead's r16 residual and compatible with the named partner's zero-defect theorem.

Parent POS3 remains **OPEN / NOT PROVED**. No novelty or priority claim is made.

## 8. Exact executable evidence

Verifier:

`proofnet24/collective-POS3/account02/B19/20260922T071111Z-account02-B19-pos3-r11/verify_r16_opposite_ray_frontier.py`

- Git blob: `58b8d399283493453de76b6c14bc254c12b2d75d`
- SHA-256 of the executed source bytes: `74396be14d7eeb22471e080dbebe6df9f86dee2ec86d0ff90c69b2c0e6db68bf`

Captured output:

`proofnet24/collective-POS3/account02/B19/20260922T071111Z-account02-B19-pos3-r11/verify_r16_opposite_ray_frontier.out`

- Git blob: `5189e900fa6567fbf7e46ecd5c350e82b138fc7c`
- SHA-256: `67f25a09d4a040f37279bf0d7b60fd71c4cbe6122697505e33b3909de5b09926`
- terminal marker: `POS3_R16_OPPOSITE_RAY_FRONTIER_ADVERSARY_PASS`

The executable reconstructs the transitive closure, enumerates all 108 full linear extensions with unit weight, certifies width exactly three, connected comparability/incomparability graphs, autonomous-primality, all eleven incomparable-pair probabilities, the exact heavy partition, canonical sets, deterministic bad-swap weights, the `>2E/33` selected packets, absence of old-span interiors, the balanced blocker cross-pair, and both immediate reciprocal heavy children.

## 9. Integrity

Scoped privacy/provenance review: this report contains only mathematics, public-to-the-project repository-relative source references, exact nonsecret Git object identifiers, and the logical run label. It contains no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, public posting, paid model/API/Codex use, remote workflow dispatch, permission change, or brain-installation action.
