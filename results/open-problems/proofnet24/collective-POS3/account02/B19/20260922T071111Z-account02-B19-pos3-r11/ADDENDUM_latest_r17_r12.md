# POS3 account02/B19 late-dependency addendum — coherent same-ray gate exits immediately by span descent

This addendum preserves the immutable main report and records the later complete lead/partner versions discovered by the final freshness pass.

**Classification remains:** `ESSENTIAL_STEP_APPLIED`.  
**Parent POS3 remains:** `OPEN / NOT PROVED`.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Later complete sources consumed

The latest complete campaign lead is now:

- **account04/B10 r17**, science commit `732a848a9fa315f3907c654f0c54591dfe04535d`, report `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, report blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

R17 pays the comparable same-ray branch by a strict packet-order identity and pays the anti-aligned incomparable branch by exporting an anchor-free blocker pair with minority `>2/33`. Its sole unpaid same-ray case is the **coherent width-saturating three-antichain gate**:

- right ray: `y prec_* r_F1 prec_* r_F3`, with `{y,r_F1,r_F3}` a three-antichain;
- left ray: `r_F2 prec_* r_F4 prec_* x`, with `{r_F2,r_F4,x}` a three-antichain.

The latest complete named partner is now:

- **account03/B10 r12**, science commit `593818378136c8082236ead59eb916d8f8fefa77`, report `proofnet24/collective-POS3/account03/B10/20260922T071308Z-account03-B10-r12-turning/REPORT.md`, report blob `7c194b61648e3a61dd64cfe06ee12bf9739b6123`.

R12 proves that every change of handedness in the canonical outer walk is an actual heavy Hasse sandwich. Either a turn already yields a `[3/11,1/3)` minority pair, or the sandwich mass is `>5/11` and the lead exports two bounded-span outward packets with minority `>2/33`. Its remaining obligation is `BOUNDED-TURN ACTIVATION`.

I also retain account04/B20's incoming-superinterval theorem at science commit `79a609ff83b87121fbe66814dcb4bd66d94fa7e1`: pure incoming/reverse-transposition cancellation strictly increases `span_*`, so a true cycle must mix mechanisms.

## 2. First essential missing implication — paid

### Theorem — the r17 coherent gate is already an authorized strict strong-majority span descent

Consider the r17 **right-ray coherent gate**

`y prec_* r_F1 prec_* r_F3`,

with `{y,r_F1,r_F3}` a three-antichain.

Because the three vertices are pairwise incomparable, both `(y,r_F1)` and `(y,r_F3)` are actual incomparable pairs. The displayed strong-order chain puts `r_F1` strictly inside the strong-majority interval from `y` to `r_F3`. Therefore

`(y,r_F1)`

is a strict strong-majority subspan of

`(y,r_F3)`.

So the coherent right-ray gate exits immediately through the already-authorized **strict strong-majority span descent**. No extra probability injection, finite census, or induced-law argument is needed.

The left-ray case is dual. In

`r_F2 prec_* r_F4 prec_* x`,

with `{r_F2,r_F4,x}` a three-antichain, the pair `(r_F4,x)` is a strict strong-majority subspan of `(r_F2,x)`.

Hence r17's `COHERENT-GATE EXIT` is paid completely by span descent.

### Consequence

After excluding an actual balanced pair and strict strong-majority span descent, **no same-ray selected-packet gate survives at all**:

1. comparable typed gate — r17 gives strict packet gain;
2. anti-aligned incomparable gate — r17 exports an anchor-free `>2/33` blocker pair;
3. coherent incomparable gate — the theorem above gives immediate strict span descent.

Thus the unresolved recycler is genuinely an **opposite-ray / mixed-mechanism** problem.

## 3. Applying the newest named partner

Account03/B10 r12 proves that an outer-walk handedness reversal cannot be silent: it creates a heavy Hasse sandwich, and in the low-endpoint branch the lead emits two outward packets at actual minority scale `>2/33`, each within strong-order distance at most `5920`.

The same-ray coherent-gate theorem above removes the last local same-ray exception next to that turn mechanism. Together with account04/B20's strict-superinterval direction for pure incoming cancellation, a surviving cycle must alternate genuinely different mechanisms and must preserve/transfer charge across **opposite-ray** frontiers.

This matches the exact eight-element regression guard in the main report: its selected `>2E/33` packets are on opposite rays, every immediate boundary-anchor pair is unbalanced, while balance occurs in a blocker-blocker cross pair (`Pr(3<6)=5/9`) and again on the immediate child frontier (`Pr(4<5)=47/108`).

## 4. Updated first unpaid implication

The first unpaid implication is now the partner's global activation problem in its sharper form:

> **OPPOSITE-RAY BOUNDED-TURN ACTIVATION / CROSS-FRONTIER TRANSFER.** Starting from an r12 heavy turn or an r17 low-endpoint heavy state after all same-ray gates are eliminated, prove that the two opposite-ray `>2E/33` packets cannot be reused through mixed fork/exact-two/non-crossed/bridge/incoming mechanisms without forcing a balanced blocker cross-pair, strict span descent, proper autonomous/ordinal reduction, four-antichain contradiction, `[3/11,1/3)` pair, or a quantitatively charge-preserving new canonical state.

Account03/B10's zero-defect boundary law and account04/B20's superinterval theorem rule out scalar correction and pure incoming cycling; the exact B19 adversary rules out boundary-anchor-only closure. The missing theorem must therefore be genuinely cross-frontier and mixed-mechanism.

No full-proof claim is made. No novelty or publication-priority claim is made.
