# POS3 account01/B10 — threshold-free heavy-bridge child descent

**Run:** `20260922T084926Z-b10-pos3-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and extension counts below are for the original uniform law on the full linear extensions of the original poset. No deletion-induced distribution is treated as uniform.

## 1. Fresh collective state consumed

The latest complete campaign-lead report consumed is account04/B10 r18,

- `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, science commit `a4b6e9bf76d078c98a82f44be0af30c57def7f99`, report blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

Its exact-backtrack state is a heavy Hasse bridge

`l lessdot r`, `m || l,r`, `l prec_* m prec_* r`,

with the exact three-cell partition

`A=#{m<l<r}`, `H=#{l<m<r}`, `C=#{l<r<m}`, `E=A+H+C`.

It proves `H>E/3`; its then-unpaid branch was global recycling through strict envelope expansions and non-exact/multi-distinguisher exact backtracks.

The immediately preceding account01/B11 support theorem is also consumed:

- `proofnet24/collective-POS3/account01/B11/20260922T081324Z-b11-pos3-r11/REPORT.md`, report blob `369bdbc02461f4a6a1c8b67d026f159766b20443`.

For the canonical Hasse families

`F1={z:l lessdot z, z||m, z!=r}`,
`F2={z:z lessdot m, z||l}`,
`F3={z:m lessdot z, z||r}`,
`F4={z:z lessdot r, z||m, z!=l}`,

it proves, in the low-endpoint regime, that after balance and authorized strict strong-majority span descent are removed, all positive canonical bad-swap support purifies to one of two modes: `F2/F3` only (through-middle) or `F1/F4` only (fork-fork).

A named OTHER-account result used directly is account02/B10 r12,

- `proofnet24/collective-POS3/account02/B10/20260922T084851Z-b10-pos3-r12/REPORT.md`, report blob `0d6b6aaf49e848e27daf8bc78d672cb28ed58aa4`.

It proves that every exact backtrack has noncentral outgoing Hasse defects on both sides, with the two external witness families vertex-disjoint; in the low-endpoint regime each side contains a distinct `>2E/33` packet. This guarantees that the exact backtrack is not a closed two-state object and identifies the external Hasse support to which the child construction below applies.

The designated partner account02/B11 r18 is also applied in the global reduction:

- `proofnet24/collective-POS3/account02/B11/20260922T075311Z-b11-pos3-r18-aa069b32/REPORT.md`.

It proves that after strict span descent is exhausted, an incomparability articulation has only a two-boundary interface or a two-boundary-plus-one-leaf interface; arbitrarily long ordinal corridors cannot hide the bridge descent below.

A later compatible account01/B11 delta states that the remaining low-endpoint recycler, after its rigid-support cases, is genuinely multi-distinguisher while attempting to reabsorb both distinct leak packets. The theorem below does not assume bounded distinguisher support and therefore applies to that residual as well.

## 2. New observation: purification does not need the `3/11` cutoff

The `3/11` assumption in the preceding support-purification report is needed for its quantitative packet floors, but not for the **qualitative two-mode purification itself**.

Assume only a heavy bridge

`l lessdot r`, `m||l,r`, `l prec_* m prec_* r`,                         (2.1)

inside a no-balanced branch, and assume the already-authorized strict strong-majority span-descent exits have been removed for this bridge. Then

`A/E=Pr(m<l)<1/3`, `C/E=Pr(r<m)<1/3`,                              (2.2)

and therefore

`H-A = E-2A-C >0`,
`H-C = E-A-2C >0`.                                                   (2.3)

The exact two-sided swap-defect inequalities give

`|B_L| >= H-A >0`, `|B_R| >= H-C >0`,                              (2.4)

where `B_L` is the bad middle-cell swap set for `l <-> m` and `B_R` is the bad middle-cell swap set for `m <-> r`.

Thus there is positive canonical support on at least one member of `F1 union F2` and on at least one member of `F3 union F4`, without any `3/11` numerical hypothesis.

Ray localization from the lead gives

`F2^+ union F4^+` strictly to the left of `l` in `prec_*`,
`F1^+ union F3^+` strictly to the right of `r`.                    (2.5)

The same-ray support argument of account01/B11 is qualitative: simultaneous positive `F1^+,F3^+` gives either a balanced blocker cross-pair or an authorized strict subspan; dually simultaneous positive `F2^+,F4^+` does the same. Hence, in the surviving branch,

`F1^+` and `F3^+` cannot both be nonempty,
`F2^+` and `F4^+` cannot both be nonempty.                          (2.6)

Combining (2.4) and (2.6) yields exactly two possible modes, now **without a `3/11` cutoff**:

- **Mode T:** `F1^+=F4^+=empty`, while `F2^+,F3^+` are nonempty;
- **Mode F:** `F2^+=F3^+=empty`, while `F1^+,F4^+` are nonempty.

This threshold-free extension is the first new ingredient of the run.

## 3. Heavy-bridge child lemma

Define a heavy bridge to be a triple `(l,m,r)` satisfying (2.1). Let `rho` denote rank in the strict total strong-majority order `prec_*` of a hypothetical no-balanced candidate.

### Theorem 3.1 — every span-exhausted heavy bridge has a heavy child with smaller left endpoint

Assume `(l,m,r)` is a heavy bridge and no balanced pair or authorized strict strong-majority span descent has occurred. Then there exists another heavy bridge `(l',m',r')` with

`rho(l') < rho(l)`.                                               (3.1)

More explicitly:

1. in Mode T, choose any positive `t in F2^+`. Then
   
   `t lessdot m`, `t||l`, and `t prec_* l prec_* m`.
   
   Therefore
   
   `(l',m',r')=(t,l,m)`                                           (3.2)
   
   is a heavy bridge and `rho(t)<rho(l)`;

2. in Mode F, choose the positive `c in F4^+` (uniqueness is not needed for the argument). Then
   
   `c lessdot r`, `c||m`, and `c prec_* l prec_* m prec_* r`.
   
   Therefore
   
   `(l',m',r')=(c,m,r)`                                           (3.3)
   
   is a heavy bridge and `rho(c)<rho(l)`.

**Proof.**

For Mode T, `t in F2` gives the cover `t lessdot m` and `t||l`. The old bridge gives `l||m`. Ray localization gives `t prec_* l`, while the old bridge gives `l prec_* m`. Hence `t prec_* l prec_* m`, so `(t,l,m)` has a cover as its two endpoints and a middle element incomparable with both.

Partition full extensions by the position of `l` relative to the forced cover `t<m`. The two endpoint cells have probabilities

`Pr(l<t)` and `Pr(m<l)`.

Because `t prec_* l prec_* m` and there is no balanced pair, both are strictly below `1/3`. Hence the middle cell `Pr(t<l<m)` is strictly above `1/3`. Thus `(t,l,m)` is a heavy bridge. Its left endpoint has strictly smaller `rho`.

For Mode F, `c in F4` gives `c lessdot r` and `c||m`; the old bridge gives `m||r`. Ray localization gives `c prec_* l`, and the old bridge gives `l prec_* m prec_* r`; therefore `c prec_* m prec_* r`. Partitioning full extensions by the position of `m` relative to the forced cover `c<r`, the endpoint cells have probabilities `Pr(m<c)` and `Pr(r<m)`, each strictly below `1/3`. Hence `Pr(c<m<r)>1/3`, so `(c,m,r)` is a heavy bridge, again with a strictly smaller left-endpoint rank. `square`

The argument uses only actual full-extension probabilities and Hasse relations. It is independent of how many external distinguishers support the active channels.

## 4. Well-founded bridge descent

### Corollary 4.1 — no closed span-exhausted heavy-bridge recycler

Starting from any heavy bridge, repeatedly apply Theorem 3.1 whenever the current bridge has neither balance nor an authorized strict span-descent exit. At every such step the nonnegative integer

`Phi(l,m,r)=rho(l)`                                               (4.1)

strictly decreases.

Therefore after at most `rho(l)+1` bridge states, the iteration must encounter one of:

1. an actual balanced incomparable pair; or
2. an authorized strict strong-majority span-descent exit.

In particular, **there is no finite closed recycler consisting only of span-exhausted heavy bridges**, even if every bridge has genuinely multi-distinguisher support and even if its leak vertices were exposed in earlier larger envelopes.

This is stronger than tracking cumulative envelope growth. Reuse of an old outer vertex is harmless for the argument: the selected child is ordered by its current left endpoint, and `rho(l)` decreases regardless of whether the child vertex is globally new.

### Why this attacks the newest residual

Account02/B10 r12 and the late account01/B11 delta reduce a low-endpoint exact backtrack to two distinct external leak packets, with the last unresolved branch genuinely multi-distinguisher and potentially reusing an old envelope. Corollary 4.1 bypasses the support-size issue. Once the exact backtrack is viewed again as its heavy bridge, threshold-free purification supplies a left child bridge, and the left-endpoint rank drops. A multi-support state therefore cannot be a stationary exact-backtrack obstruction inside the heavy-bridge class.

The same statement also absorbs the earlier `3/11` split: the qualitative descent does not stop merely because an endpoint minority enters `[3/11,1/3)`. That cutoff remains useful for quantitative packet estimates, but it is unnecessary for the well-founded bridge potential.

## 5. Compact conditional end-to-end consequence

The current collective route can now be sharpened as follows.

1. In a hypothetical minimal width-three counterexample, no-balancedness gives the total strong-majority order `prec_*`.
2. The lead and account02/B10 reduce a neutral two-step ray switch to an exact backtrack through a heavy bridge, or else obtain strict span descent / strict envelope expansion.
3. Account02/B10 r12 proves that an exact backtrack leaks through external Hasse support on both sides; the account01/B11 support theorem purifies the surviving support.
4. Sections 2-4 above show that **regardless of endpoint scale or number of distinguishers**, every span-exhausted heavy bridge has a heavy child with smaller left strong-order rank.
5. Hence repeated exact-backtrack/heavy-bridge recycling must terminate at balance or strict span descent; old-envelope reuse by itself is no longer a missing obstruction.
6. The designated partner account02/B11 r18 ensures that an incomparability articulation cannot hide this termination inside an arbitrarily long ordinal corridor: after descent exhaustion only its two residual boundary interfaces survive.

Thus the first unpaid implication is no longer generic `DISJOINT-DOUBLE-LEAK-MULTISUPPORT-REUSE`. It is the **splice after the forced strict span-descent exit**.

## 6. First essential remaining implication

> **`POS3-SPAN-DESCENT-SPLICE-v1`.** Prove that the strict strong-majority span-descent forced by Corollary 4.1 re-enters the collective reduction with a globally well-founded parameter (or directly yields balance / proper autonomous-or-ordinal reduction), so that the process cannot alternate between a finite left-rank heavy-bridge descent and a span-descent reset that recreates a previously larger bridge.

If the lead's existing use of “authorized strict span descent” already carries a global induction/minimality certificate strong enough for this splice, then Corollary 4.1 closes the exact-backtrack/heavy-bridge recycler branch outright. This report does not assume that unstated global splice and therefore does **not** claim a proof of POS3.

## 7. Status / integrity

- latest lead account04/B10 r18: **CONSUMED/APPLIED**;
- named OTHER-account account02/B10 r12 exact-backtrack double leakage: **CONSUMED/APPLIED**;
- designated partner account02/B11 r18 articulation-corridor reduction: **CONSUMED/APPLIED**;
- account01/B11 canonical support purification: **CONSUMED and extended qualitatively**;
- `3/11`-free positivity of both bad-swap sides: **PROVED**;
- threshold-free two-mode support purification: **PROVED from the exact inequalities and prior same-ray exclusion**;
- heavy-child construction with `rho(left)` strictly decreasing: **PROVED**;
- closed span-exhausted heavy-bridge recycler: **ELIMINATED**;
- global span-descent splice: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation is required for the new arbitrary-size theorem. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email or Drive data, paid/remote model/API/Codex calls, remote workflows, public posting, permission change, or native verified-brain activation was used or claimed.
