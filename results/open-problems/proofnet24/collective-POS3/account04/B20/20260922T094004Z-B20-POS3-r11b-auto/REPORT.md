# POS3 account04/B20 — terminal-block barrier at the canonical earliest endpoint

**Run:** `20260922T094004Z-B20-POS3-r11b-auto`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities inherited below are under the original uniform law on full linear extensions. This run does not use a deletion-induced distribution as though it were uniform.

## 1. Exact collective state consumed

Campaign lead:

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T091028Z-account04-B10-pos3-r11/REPORT.md`, blob `8a856fa924002567c01a8b70880003fe53b86da3`.

That report works in a hypothetical no-balanced width-at-most-three counterexample, where the inherited strong-majority relation `prec_*` is a strict total order extending the poset order. It chooses a canonical incomparable pair `(p,q)` by first minimizing the strong-order rank of the later endpoint `q`, then minimizing the rank of `p` among predecessors of `q` incomparable with it. It proves `D(p,q)=empty`, proves that the first transposition export cannot end in a span-exhausted heavy bridge, and leaves `POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1`: after the forced descent, rule out a later reset to the same earliest barrier.

Designated OTHER-account partner:

- account01/B19, `proofnet24/collective-POS3/account01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`.

The later account01/B19 r14 directory was still start-only when checked, so r13 is the newest complete designated-partner result. R13 proves the exact-two four-state selector `max(M_0,M_1,M_2,M_3) >= 3E/11`, its equality case, and the exact recurrence `A_(i-1)+3A_i+A_(i+1)=E+K`; it also proves by a source-valid long family that a fixed local selector below `1/3` cannot itself close POS3. Its first unpaid step is the first non-exact boundary-defect conversion.

The heavy-bridge step below also uses the threshold-free two-mode Hasse-support theorem exactly as quoted and applied by the lead from account01/B10 r13: absent balance and an already-authorized strict span descent, a heavy bridge is in Mode T (`F2,F3` positive and `F1,F4` empty) or Mode F (`F1,F4` positive and `F2,F3` empty).

## 2. New structural lemma: the entire prefix before the earliest endpoint is a chain

Assume the same hypothetical no-balanced counterexample and write the strong-majority total order as `prec_*`. Let `q` have minimum rank among all later endpoints of oriented incomparable pairs.

### Lemma 2.1 — prefix-chain lemma

Every two vertices strictly before `q` in `prec_*` are comparable in the poset, and their poset order agrees with `prec_*`.

**Proof.** If two such vertices `u prec_* v prec_* q` were incomparable, then `v` would itself be the later endpoint of an incomparable pair with rank strictly below the rank of `q`, contradicting the definition of `q`. Since `prec_*` extends every forced poset comparison, the comparable prefix is a chain in that same order. `square`

Let `p` be the leftmost vertex before `q` that is incomparable with `q`, as in the lead.

### Lemma 2.2 — terminal incomparability block

The vertices before `q` split as

- every `z prec_* p` satisfies `z<q` in the poset;
- every `s` with `p preceq_* s prec_* q` satisfies `s || q`.

Thus all predecessors of `q` in the strong order that are incomparable with `q` form one terminal block `I=[p,q)` inside the prefix chain.

**Proof.** For `z prec_* p`, comparability with `q` follows from the defining minimality of `p`; the orientation cannot be `q<z` because that would reverse the strong order, so `z<q`. Now take `p preceq_* s prec_* q`. By Lemma 2.1, `p<=s` in the poset. If `s<q`, then `p<=s<q` would imply `p<q`, contrary to `p||q`; and `q<s` is impossible because `prec_*` extends the poset order. Hence `s||q`. `square`

## 3. New universal extension: every state in the terminal block has empty lower Hasse family

For an oriented incomparable pair `(s,q)` define

`D(s,q)={z : z lessdot q and z||s}`.

### Lemma 3.1

For every `s in I`,

`D(s,q)=emptyset`.

**Proof.** If `z lessdot q`, then `z<q`, hence `z prec_*q`. Both `z` and `s` lie in the prefix before `q`, which is a poset chain by Lemma 2.1. Thus `z` and `s` are comparable, contradicting `z||s`. `square`

This extends the lead's `D(p,q)=emptyset` from one chosen left endpoint to every possible return state `(s,q)` in the whole terminal block.

## 4. Main theorem: no terminal-block `q`-reset can be span-exhausted

### Theorem 4.1 — terminal-block barrier

Fix any `s in I`. Starting from `(s,q)`, the exact endpoint-transposition/Hasse export cannot enter a span-exhausted heavy-bridge recycler. Under the no-balanced hypothesis, the first positive export either gives an already-authorized strict strong-order subspan or any resulting heavy bridge necessarily exposes such a strict span descent.

**Proof.** Because `s prec_*q` is an incomparable strong-majority pair, the exact transposition identity used by the lead gives positive outgoing defect. Every outgoing defect has a Hasse witness in the upper family `U(s,q)` or the lower family `D(s,q)`. Lemma 3.1 removes the lower family, so choose a positive witness `r` with

`s lessdot r`, `r||q`.

If `r prec_*q`, then Lemma 2.1 and `s<r` give

`s prec_* r prec_* q`,

so `(r,q)` is a strict `q`-anchored subspan of `(s,q)`.

The only remaining branch is

`s prec_* q prec_* r`,

which is a heavy bridge with cover endpoints `s lessdot r` and middle vertex `q` incomparable with both.

Assume, seeking a contradiction, that this bridge has neither a balanced pair nor any authorized strict span descent. Use the four canonical Hasse families `F1,F2,F3,F4` of the inherited threshold-free bridge theorem. Here `F2=D(s,q)=emptyset`. Therefore Mode T is impossible, and Mode F must hold. In particular there is a positive `F4` witness `c` with

`c lessdot r`, `c||q`, `c != s`.

Since `c<r`, the total order places `c prec_*r`. There are only three possible locations relative to `s prec_*q prec_*r`.

1. If `q prec_*c prec_*r`, then `(q,c)` is an incomparable strict subspan of `(q,r)`, an authorized descent.
2. If `s prec_*c prec_*q`, then `(c,q)` is an incomparable strict subspan of `(s,q)`, again an authorized descent.
3. Therefore a no-descent branch would require `c prec_*s`. But `c||q` and `c prec_*q` put `c` inside the same terminal block `I` by Lemma 2.2. Lemma 2.1 then gives `c<s` in the poset. Together with `s lessdot r` this gives the strict chain `c<s<r`, contradicting `c lessdot r`.

All possibilities contradict the assumed span-exhausted branch. `square`

### Corollary 4.2 — the whole earliest-endpoint block is a one-way barrier

A direct `q`-anchored descent `(s,q)->(r,q)` with `s prec_*r prec_*q` moves the left endpoint strictly to the right inside the finite terminal block. Such direct descents can occur at most `|I|-1` times before some other mechanism must occur.

More importantly, a later proof excursion that re-enters the canonical earliest endpoint `q` at **any** state `(s,q)`, not merely the original `(p,q)`, cannot terminate in a neutral span-exhausted heavy bridge. It must immediately expose balance or another authorized strict span descent.

This removes a larger reset class than the lead's original first-return statement, which treated the original `(p,q)` state.

## 5. Application to the designated partner's exact-two boundary problem

Account01/B19 r13 shows that arbitrarily long exact-two corridors can retain every local minority below `1/3`, while a four-state window still contains a real minority of at least `3E/11`. Therefore no bounded local selector can replace the global boundary conversion.

Theorem 4.1 supplies a new exact splice at one important boundary outcome: if the first non-exact boundary mechanism, or a later charged excursion from it, re-enters the canonical earliest endpoint `q`, that charge cannot disappear into a span-exhausted `q`-reset. The re-entry is a forced-descent branch throughout the entire terminal incomparability block.

So the remaining global obligation can exclude neutral `q`-resets and focus on excursions that avoid the earliest endpoint entirely. The still-unpaid statement is now:

> **`POS3-EARLIEST-BLOCK-MIXED-SPLICE-v2`.** Starting from the canonical earliest endpoint and taking every forced strict descent, prove that an excursion through exact-two boundary defects, non-crossed staircases, or other charged Hasse mechanisms either (i) produces a balanced pair, (ii) produces a valid proper autonomous/ordinal reduction, or (iii) returns with a globally well-founded statistic strictly improved. Re-entry at the earliest endpoint `q` may be treated as a forced-descent branch by Theorem 4.1 and is not a neutral reset.

This does **not** prove that all excursions avoid cycling among later endpoints. POS3 therefore remains open.

## 6. Independent finite regression

`verify_terminal_block_barrier.py` exhaustively generates every distinct transitive closure compatible with the natural order through six vertices. For every nonchain closure it chooses the first later endpoint `q`, verifies the prefix-chain lemma, the terminal-block characterization, `D(s,q)=emptyset` for every block vertex, and the structural cover contradiction used in the `F4` part of Theorem 4.1.

Exact output:

```text
POS3_TERMINAL_BLOCK_BARRIER_REGRESSION
2 2 1 1 0
3 7 6 7 1
4 40 39 48 14
5 357 356 439 195
6 4824 4823 5871 3451
POS3_TERMINAL_BLOCK_BARRIER_REGRESSION_PASS
```

The columns after `n` are distinct transitive closures, nonchain closures with a canonical endpoint, tested terminal-block vertices, and tested heavy bridges. The computation is regression evidence only; the arbitrary-size result is the symbolic proof above.

## 7. Status

- Parent POS3: **OPEN / NOT PROVED**.
- Inherited finite frontier `n_bal=14`: **UNCHANGED**.
- Lead canonical earliest endpoint and first-heavy-bridge theorem: **CONSUMED/APPLIED**.
- OTHER-account account01/B19 r13 exact-two selector/recurrence: **CONSUMED/APPLIED**.
- Prefix before the minimal later incomparable endpoint is a poset chain: **PROVED**.
- `q`-incomparable predecessors form a terminal block: **PROVED**.
- `D(s,q)=emptyset` for every state in that block: **PROVED**.
- Span-exhausted heavy bridge impossible after export from every `(s,q)` in the block: **PROVED**, arbitrary finite size, conditional on the inherited threshold-free bridge-support theorem.
- Neutral reset to earliest endpoint anywhere in its terminal block: **ELIMINATED for the transposition/heavy-bridge mechanism**.
- Mixed-mechanism global splice among later endpoints: **OPEN**.
- Run classification: **`ESSENTIAL_STEP_APPLIED`**.

Scoped integrity review: only the named mathematical repositories, source-bound peer reports, sanitized logical run labels, exact formulas, and deterministic standard-library finite regression were used. No benchmark answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex execution, remote workflow, public posting, permission bypass, or production-brain mutation was used or claimed.
