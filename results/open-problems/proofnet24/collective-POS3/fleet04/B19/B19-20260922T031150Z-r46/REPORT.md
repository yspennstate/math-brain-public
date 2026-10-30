# POS3 fleet04/B19 — clean-fork ascent termination and TP2 fork budget

**Run:** `B19-20260922T031150Z-r46`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no brain-installation or benchmark work. The result below is an arbitrary-size structural reduction in the width-three target; it is not a finite census and is not promoted to a full proof.

## 1. Exact source-bound state consumed

The newest complete team-lead version read before the derivation was:

1. **Team lead fleet04/B10**,  
   `proofnet24/collective-POS3/fleet04/B10/20260922T024220Z-B10-POS3-r39/REPORT.md`,  
   blob `c1b4721b079ea67e9176948c7f5ea4cc179c79f3`.

   Its equal-predecessor channel theorem says: in a width-at-most-three poset with no balanced pair, if `a||b`, `Pred(a)=Pred(b)`, and `a prec_* b` in the transitive strong-majority order, then either

   - **span descent:** there is a canonical positive Hasse blocker `z` with `a lessdot z`, `z||b`, and `a prec_* z prec_* b`; or
   - **fork escalation:** there are exactly two canonical positive blockers `z_1,z_2`, both Hasse covers of `a`, with `{b,z_1,z_2}` a three-antichain and both blockers after `b` in `prec_*`.

   The same report gives the exact endpoint identity
   `Pr(a<b)=1-(Q+R)/(2E)`, where `E=e(P)`, `Q` counts extensions in which `b` precedes every positive blocker, and `R` is the reverse nonneutral channel total.

The required named **OTHER-account partner result** consumed and applied is:

2. **Partner fleet01/B10**,  
   `proofnet24/collective-POS3/fleet01/B10/20260922T024151Z-b10-pos3-r11b/REPORT.md`,  
   blob `19b166fc7ab374365c098e88da1148a79da78de4`.

   For every element `x` in any three-chain cover, its exact two-coordinate flux matrix `W_x(s,t)` is TP2. Equivalently, the two other-chain prefix counts are positively quadrant dependent under the actual uniform full-extension law. No deletion law is substituted.

A second compatible structural input is:

3. **fleet02/B10**,  
   `proofnet24/collective-POS3/fleet02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`,  
   blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`.

   It proves that every extreme incomparable pair has at least two distinguishers: zero distinguishers give probability `1/2`, and exactly one distinguisher forces probability into `[1/3,2/3]`.

The immediately preceding B19 report was:

4. `proofnet24/collective-POS3/fleet04/B19/B19-20260922T021406Z-r45/REPORT.md`,  
   blob `4bcecc82236db10ef98bd1c67edc810c4bb0057b`.

   It handles the proper-autonomous-chain branch when the maximum neutral corridor size is at most the chain length, and leaves the large-neutral chain-module residual. This run does not repeat that mechanism; it returns to the module-prime/global fork branch isolated by the newer team-lead report.

## 2. Compact conditional end-to-end architecture

Assume for contradiction that `P` is a cardinality-minimal counterexample to POS3.

Inherited reductions allow one to work with width exactly three, connected incomparability graph, no proper autonomous nonchain, and a transitive strong-majority order `prec_*`. At the first majority-block boundary one obtains an extreme incomparable sibling pair. There are then two structural branches.

- If the sibling pair already has unequal predecessor sets, there is a **lower distinguisher** and one is in the structural branch left unpaid by the lead.
- If the sibling pair has equal predecessor sets, the lead's span-descent/fork-escalation theorem applies.

The first uncovered case is whether the second branch can keep escalating cleanly through arbitrarily many majority blocks without ever entering the lower-distinguisher branch. The answer is **no** in every finite poset. Moreover, every clean fork carries a quantitative TP2 budget coming from the named other-account partner.

Thus the equal-predecessor branch is not an independent infinite residual: after finitely many Hasse-cover ascents it reaches an extreme pair with unequal predecessor sets. By the fleet02/B10 theorem, that exit pair has at least two distinguishers, at least one of which is lower.

## 3. Clean-fork ascent theorem

### Theorem 3.1 — equal-predecessor escalation terminates in a lower-distinguisher pair

Let `P` be a finite poset of width at most three with no balanced incomparable pair. Let `prec_*` be its transitive strong-majority order. Suppose

`a_0 || b_0`, `Pred(a_0)=Pred(b_0)`, and `a_0 prec_* b_0`.

Repeatedly apply the team-lead equal-predecessor theorem whenever the current pair `(a_i,b_i)` still satisfies `Pred(a_i)=Pred(b_i)`.

Then after finitely many steps one obtains an extreme incomparable pair `(u,v)` with

`Pred(u) != Pred(v)`.

In particular `(u,v)` has a lower distinguisher. The number of consecutive clean fork-escalation steps is at most the length of a strict chain above `a_0`, hence at most `|P|-1`.

### Proof

Fix a current equal-predecessor pair `(a_i,b_i)` with `a_i prec_* b_i`.

**Span-descent case.**  
The team-lead theorem gives a canonical positive blocker `z` such that

`a_i lessdot z`, `z||b_i`, and `a_i prec_* z prec_* b_i`.

Consider the new incomparable pair `(z,b_i)`. Because `a_i<z` but `a_i||b_i`,

`a_i in Pred(z) \ Pred(b_i)`.

Therefore `Pred(z) != Pred(b_i)`. The process has already reached the lower-distinguisher branch and stops.

**Fork-escalation case.**  
The team-lead theorem gives exactly two positive blockers `z_1,z_2`, both Hasse covers of `a_i`, with `{b_i,z_1,z_2}` a three-antichain and both blockers after `b_i` in `prec_*`. Since the poset has no balanced pair, orient the blocker pair by the same total order; after relabeling,

`z_1 prec_* z_2`.

If `Pred(z_1) != Pred(z_2)`, we have again reached a lower-distinguisher pair and stop. If instead

`Pred(z_1)=Pred(z_2)`,

set

`a_{i+1}=z_1`, `b_{i+1}=z_2`.

Because both blockers are Hasse covers of `a_i`,

`a_i lessdot a_{i+1}`.

Hence every continuation through another clean equal-predecessor fork strictly raises the first member in the original poset order. A finite poset contains no infinite strict chain, so clean fork escalation cannot continue forever.

If the process did not terminate, it would produce

`a_0 < a_1 < a_2 < ...`

with all inequalities covers, contradicting finiteness. Therefore it terminates after finitely many steps at an incomparable extreme pair with unequal predecessor sets. `□`

### Corollary 3.2 — the clean branch has a two-distinguisher exit

At the terminal pair `(u,v)` from Theorem 3.1, at least one lower distinguisher exists because the predecessor sets differ. Since `(u,v)` is still extreme in a no-balanced poset, the fleet02/B10 one-distinguisher theorem implies that `(u,v)` has at least **two distinct** distinguishers in total.

Thus a clean equal-predecessor fork chain cannot be the final obstruction. It must feed the already identified multi-distinguisher branch.

## 4. TP2 budget at every fork escalation

The preceding theorem is structural. The named partner's TP2 theorem gives an additional exact quantitative restriction at every fork-escalation step.

Let `(a,b)` be an equal-predecessor extreme pair in the fork-escalation alternative, and let `z_1,z_2` be its two positive Hasse blockers. Normalize by `E=e(P)`.

Because `{b,z_1,z_2}` is a three-antichain and `width(P)<=3`, every three-chain cover puts these three elements in three distinct chains. Use the chain containing `b` as the distinguished chain and consider the exact partner flux surface `W_b`.

Put

`p_i = Pr(z_i precedes b)`.

Fork escalation places `b prec_* z_i`, so no-balancedness gives

`p_i < 1/3`.                                                     (4.1)

Let

`Q/E = Pr(b precedes z_1 and b precedes z_2)`.

The events `b precedes z_i` are lower-tail threshold events in the two other-chain prefix counts for `W_b`. By the partner's TP2 / positive-quadrant-dependence theorem,

`Q/E >= Pr(b precedes z_1) Pr(b precedes z_2) > 4/9`.           (4.2)

This is the first direct use here of the fleet01/B10 TP2 result.

Now use the lead's exact endpoint identity

`Pr(a precedes b) = 1 - (Q+R)/(2E)`,                            (4.3)

where `R>=0` is the reverse nonneutral channel total. Since `(a,b)` is oriented strongly,

`Pr(a precedes b) > 2/3`.

Therefore

`(Q+R)/E < 2/3`.                                                 (4.4)

Combining (4.2) and (4.4) yields the new fork-remainder bound

`R/E < 2/9`.                                                     (4.5)

If `U=E-Q` denotes the total positive first-blocker channel mass, then the lead's signed channel identity gives

`U-R = N(a<b)-N(b<a) > E/3`.

Hence

`1/3 < U/E < 5/9`.                                              (4.6)

The lower bound is the strong bias; the upper bound is the TP2 consequence `Q/E>4/9`.

There is also a forced non-negligible reversal probability for at least one blocker pair. Let

`q = Pr(z_1<b and z_2<b)`.

TP2 gives `q>=p_1p_2`, while

`U/E = p_1+p_2-q <= p_1+p_2-p_1p_2`.

Set

`rho = 1-sqrt(2/3)`.

Because `2 rho-rho^2=1/3`, (4.6) implies

`max(p_1,p_2) > rho = 1-sqrt(2/3) > 0.1835`.                   (4.7)

Together with (4.1), every clean fork has at least one blocker reversal probability in the strict interval

`(1-sqrt(2/3), 1/3)`.

This does not itself produce a balanced pair, but it is a quantitative transport constraint that survives at each clean fork before Theorem 3.1 forces an exit.

## 5. Consequence for the first-boundary induction

Return to the first strong-majority boundary from the current team state.

- If its sibling blockers already have different predecessor sets, the induction is in the lower-distinguisher branch.
- If they have equal predecessor sets, Theorem 3.1 shows that repeated clean escalation cannot propagate forever. Every span-descent immediately creates a lower distinguisher (the previous first element), while every genuinely clean fork raises that first element by one Hasse edge. Finiteness forces eventual exit.
- Along every clean fork before exit, (4.2)-(4.7) hold: `Q/E>4/9`, reverse remainder `R/E<2/9`, positive channel total in `(1/3,5/9)`, and one blocker reversal probability exceeds `1-sqrt(2/3)`.

Therefore the team's module-prime/global residual can now be stated without a separate "infinite clean equal-predecessor escalation" case:

> **Remaining module-prime obligation.** Analyze an extreme incomparable pair with at least two distinguishers, at least one lower, reached from the first-boundary fork after finitely many Hasse-cover ascents; combine its distinguisher geometry with the heavy-slice/central-cell constraints and the TP2 fork budgets accumulated before exit.

The separate proper-autonomous-chain residual from the preceding B19 report remains: an internally split chain module must lie in the large-neutral regime `|N|>|C|` (more precisely `kappa(C)>=|C|+1`). This report does not claim to close that branch.

## 6. Exact source-valid regression and sharp failure boundary

The companion verifier reconstructs the exact eight-element width-three witness already used by fleet02/B10:

`0<2, 0<5, 1<2, 1<3, 1<6, 2<4, 3<4, 3<5, 5<7, 6<7`.

It has `121` linear extensions.

For the equal-predecessor extreme pair `(3,6)`:

- `Pred(3)=Pred(6)={1}`;
- `Pr(3<6)=82/121`;
- the two positive blockers are exactly `{4,5}`;
- `Pr(6<4)=103/121` and `Pr(6<5)=83/121`;
- `Q=78`, so `Q/E=78/121`;
- the exact TP2 lower-tail cross-product is
  `78*121=9438 >= 103*83=8549`, slack `889`;
- `U=43`, so `U/E=43/121`;
- the reverse remainder recovered from (4.3) is `R=0`.

The blocker pair is strongly oriented `5 prec_* 4`, with

`Pr(5<4)=93/121`.

Its predecessor sets are unequal:

`Pred(5)={0,1,3}`,  
`Pred(4)={0,1,2,3}`,

and its distinguishers are exactly `{2,7}`. Thus this source-valid example exhibits the theorem's one-step clean-fork exit: the first pair is equal-predecessor, the fork escalates once, and the next extreme pair has a lower distinguisher (`2`) plus a second distinguisher (`7`).

This same witness also prevents an overclaim: the terminal lower-distinguisher pair is still extreme (`93/121>2/3`), so "clean-fork termination" is **not** itself a proof of POS3. The lower-distinguisher transport remains genuinely necessary.

Captured verifier terminator:

`POS3_CLEAN_FORK_ASCENT_REGRESSION_PASS`.

## 7. Claim status

- Team-lead equal-predecessor channel dichotomy: inherited **PROVED**.
- Partner fleet01/B10 TP2 flux theorem: inherited **PROVED**, and applied in Section 4.
- fleet02/B10 one-distinguisher balance theorem: inherited **PROVED**, and applied in Corollary 3.2.
- Clean equal-predecessor fork escalation terminates at an unequal-predecessor extreme pair in every finite no-balanced width-three poset: **PROVED here**.
- Every clean fork satisfies `Q/E>4/9`, `R/E<2/9`, `1/3<U/E<5/9`, and one blocker reversal probability `>1-sqrt(2/3)`: **PROVED here**.
- Claim that the resulting lower-distinguisher pair must already be balanced: **REFUTED by the exact 121-extension witness**.
- Full POS3 target: **OPEN / NOT PROVED**.

Outcome is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 8. Next exact implication

The first remaining implication on this route is now:

> **Lower-distinguisher transport.** Starting from the terminal extreme pair `(u,v)` supplied by Theorem 3.1, with at least two distinguishers and at least one lower, use width three plus the strong-majority block geometry to force either a balanced pair, a four-antichain contradiction, a proper autonomous nonchain, or violation of the heavy-slice / central-cell / TP2 fork budgets.

The proof must retain exact full-extension multiplicities. The 121-extension witness shows that one lower and one upper distinguisher can coexist with an extreme pair, so a one-witness local argument is insufficient.

## 9. Provenance and privacy

Only the source-bound collective POS3 reports named above and the already shared exact eight-element mathematical witness were used. The regression code is standard-library only and contains no network calls.

A scoped fallback privacy/secret review was run over the intended changed files for this run. The files contain mathematical statements, repository-relative source paths, Git object identifiers, exact finite relation data, and nonsecret run labels only. They contain no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email or Drive data, paid-model/API/Codex calls, remote workflow instructions, public-posting actions, or permission changes.
