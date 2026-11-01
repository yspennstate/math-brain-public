# POS3 fleet04/B19 — charged sibling-fork funnel eliminates the coherent same-ray gate

**Run:** `B19-20260922T071535Z-r46`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair `u,v` with `1/3 <= Pr(u<v) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the uniform law on the full linear extensions of the original poset. No deletion-induced law is treated as uniform. No computation is used in the new argument.

## 1. Exact source-bound state consumed

The latest complete team-lead version used is:

- **fleet04/B10 r17**, `proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, Git blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

Its live low-endpoint heavy-cover state is

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

with

`A=#{L:a<x<y}`, `H=#{L:x<a<y}`, `C=#{L:x<y<a}`, `E=A+H+C`,

and `A,C<3E/11`. It uses the canonical Hasse blocker families

`F1={r:x lessdot r, r||a, r!=y}`,
`F2={r:r lessdot a, r||x}`,
`F3={r:a lessdot r, r||y}`,
`F4={r:r lessdot y, r||a, r!=x}`.

The left-swap defect uses `F1 union F2`, the right-swap defect uses `F3 union F4`. In the no-span branch, `F2 union F4` lies strictly to the left of `x` in the strong-majority order and `F1 union F3` lies strictly to the right of `y`. R16/r17 supply one selected left-swap witness and one selected right-swap witness, each with more than `2E/33` canonical marks, recoded losslessly to genuine boundary-pair minority events.

R17 pays the comparable same-ray gate and the anti-aligned incomparable same-ray gate. Its sole same-ray exception is the **coherent three-antichain gate**:

- right coherent gate: `y prec_* r_1 prec_* r_3`, with `r_1 in F1`, `r_3 in F3`, and `{y,r_1,r_3}` a three-antichain;
- left coherent gate: `r_2 prec_* r_4 prec_* x`, with `r_2 in F2`, `r_4 in F4`, and `{r_2,r_4,x}` a three-antichain.

The latest **complete** assigned OTHER-account partner result used is:

- **fleet01/B10**, run `20260922T061815Z-b10-pos3-r11`, scientific blob `8530091b5d47d9ae4c431026cabb70a6a6afde5d`.

A newer partner invocation `20260922T072132Z-b10-pos3-r11` had only a start record when this derivation was made, so it is not treated as a finalized mathematical source. The complete partner result rigorously refutes unconditional cross-anchor positive quadrant dependence, with an exact width-three witness, and proves that even perfect cross-group overlap does not push the scalar channel method to `1/3`. It explicitly retains the exact **same-anchor** TP2/PQD theorem. This run uses that retained same-anchor theorem only; it does not use the refuted cross-anchor shortcut.

A same-slot source used as an already-proved lemma is:

- **fleet04/B19**, `proofnet24/collective-POS3/fleet04/B19/B19-20260922T031150Z-r46/REPORT.md`, Git blob `9079d05dcdf18d3afdb391d39148ed8c4653768d`.

That report derives from the partner TP2 theorem the clean equal-predecessor fork budget. If `u||v`, `Pred(u)=Pred(v)`, `u prec_* v`, and the lead's two-blocker fork alternative occurs with blockers `z_1,z_2`, then at least one blocker reversal obeys

`Pr(z_i<v) > rho := 1-sqrt(2/3) = 0.183503...`.

It also records the lead's equal-predecessor dichotomy: either a span-descending Hasse blocker appears, or the two-cover fork appears.

## 2. Compact conditional route

Assume for contradiction that `P` is a width-at-most-three no-balanced counterexample in the lead's low-endpoint heavy-cover branch. R17 reduces a same-ray two-packet state to one unresolved orientation: the coherent three-antichain gate.

The missing issue is not merely to leave the old anchor; the lead asks for an exit that does not throw away the certified local packet scale `2/33`.

The observation below does exactly this. Every high-weight `F1` or `F4` blocker already forms a **sibling Hasse pair** with the old heavy-edge boundary. If that sibling pair has unequal one-sided neighborhoods, it is the required structural exit immediately. If the one-sided neighborhoods are equal, the lead's equal-neighborhood dichotomy plus the partner's same-anchor TP2 fork budget produces an unequal-neighborhood extreme pair while retaining a minority lower bound strictly above `2/33`.

Consequently the coherent same-ray gate is not a genuine residual. More generally, after this funnel any surviving two-packet low-endpoint state with no such charged structural exit has exact types `F2` and `F3`, hence lies on opposite rays around the two-edge Hasse chain `r_2 lessdot a lessdot r_3`.

## 3. Charged equal-predecessor exit lemma

Put

`delta = 2/33`.

### Lemma 3.1

Let `u||v` in a finite width-at-most-three no-balanced poset, with

`Pred(u)=Pred(v)`, `u prec_* v`, and `Pr(v<u)>delta`.

Assume the team-lead equal-predecessor dichotomy applies. Then there is an extreme incomparable pair `(s,t)` with

`Pred(s) != Pred(t)`

and minority probability strictly larger than `delta`.

### Proof

There are two lead alternatives.

**Span descent.** The lead gives a canonical blocker `z` with

`u lessdot z`, `z||v`, and `u prec_* z prec_* v`.

Because `u<z` but `u||v`,

`u in Pred(z)\Pred(v)`,                                              (3.1)

so `(z,v)` already has unequal predecessor sets. Its minority orientation is `{v<z}`. Moreover

`{v<u} subseteq {v<z}`                                              (3.2)

because `u<z` in the poset. Therefore

`Pr(v<z) >= Pr(v<u) > delta`.                                      (3.3)

**Two-cover fork.** The lead gives two Hasse covers `z_1,z_2` of `u`, with `{v,z_1,z_2}` a three-antichain and

`v prec_* z_i` for `i=1,2`.

For each `i`, again

`u in Pred(z_i)\Pred(v)`,                                          (3.4)

so every pair `(v,z_i)` has unequal predecessor sets. The previously proved same-anchor TP2 fork budget gives one `i` such that

`Pr(z_i<v) > rho := 1-sqrt(2/3)`.                                 (3.5)

Since

`rho = 1-sqrt(2/3) > 2/33 = delta`,                               (3.6)

the selected `(v,z_i)` is an unequal-predecessor extreme pair carrying a minority probability strictly above the required packet scale.

Thus either lead alternative exits the equal-predecessor state in one application; no repeated clean-fork ascent is needed for the charged conclusion. `square`

### Corollary 3.2 — dual charged equal-successor exit

If `u||v`, `Succ(u)=Succ(v)`, `u prec_* v`, and `Pr(v<u)>delta`, then there is an extreme incomparable pair with unequal successor sets and minority probability `>delta`.

**Proof.** Apply Lemma 3.1 in the order-dual poset to the reversed pair `(v,u)`. Uniform linear extensions are carried bijectively to reversed linear extensions, so the minority probability is unchanged. `square`

This is stronger for the present purpose than the earlier finite-ascent statement: it keeps a certified quantitative packet while making the first structural exit immediately.

## 4. High `F1` channels always exit with charge

Let `r in F1` be a selected high left-swap witness on the right ray. By the lead's boundary recoding,

`y||r`, `y prec_* r`, and the selected mark set is contained in `{r<y}`.

Since the witness has more than `2E/33` marks,

`Pr(r<y)>delta`.                                                   (4.1)

Also `x lessdot y` and `x lessdot r`, so `(y,r)` is an actual sibling upper-cover pair sharing `x`.

If

`Pred(y) != Pred(r)`,                                             (4.2)

we already have a charged lower-distinguisher exit. If instead

`Pred(y)=Pred(r)`,                                                (4.3)

apply Lemma 3.1 with `u=y`, `v=r`. It produces an unequal-predecessor extreme pair with minority probability `>delta`.

Therefore:

> **Theorem 4.1.** Every selected `F1` witness carrying `>2E/33` canonical marks forces a charged lower-distinguisher exit. It cannot remain a recycling state.

In a no-balanced core, the established one-distinguisher reduction then implies that this extreme output has at least two distinguishers in total; the new point here is that the `2/33` packet scale survives the exit.

## 5. High `F4` channels always exit with charge

Let `r in F4` be a selected high right-swap witness on the left ray. The lead's recoding gives

`r||x`, `r prec_* x`, and the selected marks are contained in `{x<r}`.

Hence

`Pr(x<r)>delta`.                                                   (5.1)

The Hasse relations `r lessdot y` and `x lessdot y` make `(r,x)` a sibling lower-cover pair sharing `y`.

If

`Succ(r) != Succ(x)`,                                             (5.2)

this is already a charged upper-distinguisher exit. If the successor sets are equal, apply Corollary 3.2 to `(r,x)`. The output is an unequal-successor extreme pair with minority probability `>delta`.

Thus:

> **Theorem 5.1.** Every selected `F4` witness carrying `>2E/33` canonical marks forces a charged upper-distinguisher exit. It cannot remain a recycling state.

## 6. Coherent same-ray gate is eliminated

Return to the two coherent gates left open by lead r17.

### Right coherent gate

Here the selected left-swap witness is `r_1 in F1` and carries `>2E/33` marks. Theorem 4.1 applies immediately. Hence the state

`y prec_* r_1 prec_* r_3`, `{y,r_1,r_3}` a three-antichain,

cannot be a terminal same-ray gate: it exports, with minority lower bound `>2/33`, to an extreme pair with unequal predecessor sets.

### Left coherent gate

Here the selected right-swap witness is `r_4 in F4` and carries `>2E/33` marks. Theorem 5.1 applies. Hence

`r_2 prec_* r_4 prec_* x`, `{r_2,r_4,x}` a three-antichain,

exports, with the same certified packet scale, to an extreme pair with unequal successor sets.

Therefore the lead's exact first unpaid implication `COHERENT-GATE EXIT` is paid **at the structural/packet level**: the coherent same-ray gate necessarily enters the already identified multi-distinguisher branch without dropping below the incoming `2/33` certificate. This does not prove that the resulting multi-distinguisher branch is balanced; that global transport remains open.

## 7. Stronger type collapse: the only no-exit high-packet state is `F2/F3`

The r16/r17 low-endpoint theorem selects

- one high left-swap witness from `F1 union F2`, and
- one high right-swap witness from `F3 union F4`,

each with more than `2E/33` assigned marks.

If the left selected witness lies in `F1`, Theorem 4.1 gives a charged lower-distinguisher exit. If the right selected witness lies in `F4`, Theorem 5.1 gives a charged upper-distinguisher exit.

Consequently, in the branch where neither charged exit is taken, the selected types are forced to be

`r_L in F2`, `r_R in F3`.                                       (7.1)

Their Hasse relations are therefore exactly

`r_L lessdot a lessdot r_R`,                                    (7.2)

while the lead's ray localization gives

`r_L prec_* x prec_* a prec_* y prec_* r_R`.                    (7.3)

The two selected boundary-pair minority events are

`{x<r_L}` and `{r_R<y}`,                                        (7.4)

and each contains more than `2E/33` assigned extensions.

So the unresolved high-packet branch is no longer a generic same-ray or four-family recycling problem. It is an **opposite-ray discrepancy-chain state** centered on the two-edge Hasse chain (7.2).

There is also a useful exact mass refinement. If no `F1` channel is allowed to trigger Theorem 4.1, its assigned weight is at most `2E/33`; because the total left bad-swap mass is strictly greater than `2E/11=6E/33`, the total assigned `F2` mass is strictly greater than

`4E/33`.                                                        (7.5)

Dually, excluding a high `F4` exit leaves total assigned `F3` mass strictly greater than

`4E/33`.                                                        (7.6)

Since `|F2|,|F3|<=2`, the partner's retained same-anchor TP2 may still be used separately inside either family. It must **not** be extended across the `F2/F3` anchors: the latest complete partner report gives an exact counterexample to precisely that cross-anchor shortcut.

For reference only, if a two-member same-anchor family has union probability `>4/33` and each atomic minority is at most `c`, TP2 gives `2c-c^2>4/33`, hence

`c > 1-sqrt(29/33)`.                                            (7.7)

Equation (7.7) is auxiliary; it is not claimed as closure and is not the reason for the present `ESSENTIAL_STEP_APPLIED` classification.

## 8. Revised first unpaid implication

After combining lead r17, the charged sibling-fork funnel above, and the partner's cross-anchor obstruction, the first local residual on this route is now:

> **F2/F3 DISCREPANCY-CHAIN TRANSPORT.** Starting from `r_L lessdot a lessdot r_R` with `r_L in F2`, `r_R in F3`, opposite-ray strong order (7.3), and side packet totals (7.5)-(7.6), use width three plus the heavy-slice/path structure to force one of: an actual balanced pair; strict strong-majority span descent; a proper autonomous/ordinal reduction; or a charged multi-distinguisher/non-crossed exit. The proof must not assume cross-anchor PQD, because the assigned partner has rigorously refuted that implication.

This is strictly narrower than the lead's previous `COHERENT-GATE EXIT`: every same-ray gate, including its coherent orientation, has now been discharged into an already known structural branch with the local packet certificate retained.

A compact conditional end-to-end route for the low-endpoint branch is therefore:

1. lead r17 handles comparable and anti-aligned same-ray gates;
2. Theorems 4.1-6 eliminate the coherent same-ray gate with charge;
3. any high `F1`/`F4` channel exits to unequal one-sided neighborhoods with charge;
4. otherwise the state is exactly the opposite-ray `F2/F3` discrepancy chain;
5. paying the discrepancy-chain transport plus the already exposed multi-distinguisher recycling obligation would close this heavy-cover branch.

Steps 4-5 are not silently assumed. The parent POS3 theorem remains open.

## 9. Status / integrity

- Latest complete lead r17: **CONSUMED/APPLIED**.
- Latest complete assigned partner fleet01/B10 result: **CONSUMED/APPLIED**; its same-anchor TP2 theorem is used, and its cross-anchor counterexample is respected.
- Charged equal-predecessor one-step exit: **PROVED HERE**.
- Charged equal-successor dual exit: **PROVED HERE**.
- High `F1` charged lower-distinguisher funnel: **PROVED HERE**.
- High `F4` charged upper-distinguisher funnel: **PROVED HERE**.
- Lead r17 coherent same-ray gate: **RESOLVED INTO THE MULTI-DISTINGUISHER BRANCH WITH MINORITY CERTIFICATE >2/33**.
- No-exit high-packet type collapse to `F2/F3`: **PROVED HERE**.
- `F2/F3` discrepancy-chain transport: **OPEN**.
- Global multi-distinguisher recycling: **OPEN**.
- Parent POS3 target: **OPEN / NOT PROVED**.
- Honest run classification: `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

No code or numerical search was used in the new proof. No novelty or publication-priority claim is made. No benchmark, brain-installation, paid/remote compute, email/Drive, public posting, scheduler mutation, credential access, permission change, machine-specific path, or unrelated private data was used.
