# POS3 fleet03/B19 — deletion cut-charge identity and finite collapse of the clean fork branch

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform linear-extension law lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run keeps the exact owner-selected POS3 scope and changes the mechanism from the preceding weighted-width-two obstruction. The two new ingredients are (i) an exact signed identity converting the full chain-deletion rank defect into actual pair-order numerators involving the deleted chain, and (ii) a finite-descent argument showing that the current campaign lead's equal-predecessor span-descent/fork-escalation branch cannot remain clean forever in a finite counterexample.

No projection of a uniform extension law is silently replaced by the uniform law on a deleted subposet.

## 1. Exact state consumed

The named partner actually consumed is **fleet04/B10**, run `20260922T024220Z-B10-POS3-r39`, report blob `c1b4721b079ea67e9176948c7f5ea4cc179c79f3`. Its equal-predecessor theorem says that if `a||b`, `Pred(a)=Pred(b)`, and `a prec_* b` in a hypothetical no-balanced width-three counterexample, then the exact deletion-fiber defect decomposes into positive first-successor Hasse-blocker channels. Either:

1. **span descent:** a positive blocker `z` satisfies `a <_P z`, `z||b`, and `a prec_* z prec_* b`; or
2. **fork escalation:** exactly two positive blockers `z_1,z_2` are Hasse covers of `a`, both lie after `b` in the strong-majority order, `{b,z_1,z_2}` is an antichain, their positive channel mass is `>E/3`, and one channel has mass `>E/6`.

The exact arbitrary-chain insertion/deletion recurrence from **fleet01/B19**, report blob `2c2a46da29d5b4114b5a7f71e6b0072d27b9c437`, is also used. For a chain `C={c_1<...<c_m}`, `Q=P\C`, and `tau in L(Q)`, it retains the true corridor multiplicity `W_C(tau)` and slice counts `H_t^tau(r)`. If `q` has position `k` in `tau`,

`N_tau(q<c_t)=sum_{r=k}^n H_t^tau(r)`,

`N_tau(c_t<q)=sum_{r=0}^{k-1} H_t^tau(r)`.

The preceding B19 report, blob `07b199a92b9493193bfa7d847c1d41011975a822`, proved that under the exact weighted projection law every chain deletion with nonchain remainder has a strong boundary whose weighted expected rank gap is at most one, and showed on a 349-extension example that the weighted two-chain remainder itself need not contain a balanced pair. The escape pairs in that example meet the deleted chain.

The latest compatible fleet02/B11 structural report, blob `a8e5e6dc7fc402c714d87da86b4b833a7efa0c38`, is used only as context: any counterexample is both comparability-connected and incomparability-connected, so the residual is not a trivial parallel/ordinal decomposition.

## 2. Exact deletion cut-charge identity

Let `P` be any finite poset, let `C` be any subset (the application has `C` a chain), and put `Q=P\C`. Let `E=e(P)`. For distinct `u,v in P`, define the integer signed pair numerator

`B_P(u,v)=#{L in L(P):u<_L v}-#{L in L(P):v<_L u}`.

Thus `B_P(u,v)/E=2 Pr_P(u<v)-1`.

For retained `x,y in Q`, write

`R_P(x,y)=sum_{L in L(P)} (r_L(y)-r_L(x))`,

and

`R_Q^C(x,y)=sum_{L in L(P)} (r_{L|Q}(y)-r_{L|Q}(x))`.

The second sum is exactly the weighted projected-rank numerator. When `C` is a deleted chain, it is expectation under the genuine corridor-weighted law `mu_C(tau)=W_C(tau)/E`, multiplied by `E`.

### Theorem 2.1 — cut-charge identity

For every finite `P`, every deleted set `C`, and every distinct retained pair `x,y`,

`sum_{c in C} [B_P(x,c)-B_P(y,c)]`

`= 2 [R_P(x,y)-R_Q^C(x,y)].`                         `(CC)`

Equivalently, in normalized form,

`sum_{c in C} [beta_P(x,c)-beta_P(y,c)]`

`= 2( E_P[r_P(y)-r_P(x)] - E_mu[r_Q(y)-r_Q(x)] ),`      `(CCn)`

where `beta_P(u,v)=2Pr_P(u<v)-1` and `mu` is the exact law induced on `L(Q)` by restriction of a uniform extension of `P`.

### Proof

Fix one full extension `L` and one deleted element `c`. The quantity

`sgn_L(x,c)-sgn_L(y,c)`,

where `sgn_L(u,v)=+1` if `u<_L v` and `-1` otherwise, is zero when `c` lies on the same side of both `x,y`; it equals `+2` when `x<c<y`; and it equals `-2` when `y<c<x`.

On the other hand, deleting `C` from `L` changes the signed rank difference `r_L(y)-r_L(x)` by exactly

`#{c in C:x<c<y in L} - #{c in C:y<c<x in L}`.

Summing the first identity over `c`, then over all `L`, gives exactly twice the sum in the second identity. This proves `(CC)`, and division by `E` proves `(CCn)`. `□`

The theorem itself does not require `C` to be a chain. The chain hypothesis matters because fleet01/B19 gives an exact, computable corridor recurrence for every term and for the induced rank law.

## 3. Fiberwise corridor refinement

For a chain deletion use the fleet01/B19 slice counts. Fix `tau in L(Q)`, let `k_x,k_y` be the positions of `x,y`, and define the fiber signed count

`B_tau(q,c_t)=N_tau(q<c_t)-N_tau(c_t<q)`.

The forward/backward formula gives immediately

`B_tau(q,c_t)=W_C(tau)-2 sum_{r<k_q} H_t^tau(r)`.         `(3.1)`

Hence if `k_x<k_y`,

`B_tau(x,c_t)-B_tau(y,c_t)`

`=2 sum_{r=k_x}^{k_y-1} H_t^tau(r)`,                    `(3.2)`

and the same expression has the opposite sign when `k_y<k_x`.

Thus `(3.2)` is literally twice the number of lifts of `tau` in which `c_t` is between `x` and `y`, with sign determined by the order of `x,y`. Summing `(3.2)` over `tau,t` recovers `(CC)`. This is the exact cross-interface charge requested by the preceding B19 residual: the formerly opaque corridor/rank defect is a sum of genuine deleted-chain pair numerators, not a surrogate under a uniform remainder law.

## 4. No-balanced sign consequence

Assume now that `P` is a hypothetical POS3 counterexample with the inherited transitive strong-majority order `prec_*`. Let `x prec_* y`, and let `h` be the number of deleted-chain elements satisfying

`x prec_* c prec_* y`.

Because there is no balanced incomparable pair, every incomparable strong-majority comparison has signed bias of absolute value strictly greater than `1/3`; comparable pairs have bias `+/-1` with the same order sign. Therefore:

- for every `c` strictly between `x,y` in `prec_*`,
  `beta(x,c)-beta(y,c)>2/3`;
- for every deleted `c` on the same side of both endpoints,
  `beta(x,c)-beta(y,c)>-2/3`.

If `m=|C|`, `(CCn)` gives the necessary inequality

`E_P[r_P(y)-r_P(x)] - E_mu[r_Q(y)-r_Q(x)]`

`> (2h-m)/3`.                                            `(4.1)`

This is not yet a contradiction, but it is a quantitative constraint on every strong compressed boundary. In particular the exact weighted rank compression from the previous B19 run can now be combined with the actual number of deleted-chain elements lying between the boundary endpoints in the common majority order; there is no missing conversion from a rank defect to pair events.

## 5. Clean equal-predecessor escalation cannot continue forever

The partner's fork theorem left open the possibility of repeated clean fork escalation. That possibility can be eliminated abstractly.

### Theorem 5.1 — finite collapse to a lower distinguisher

Assume `P` is finite, width at most three, has no balanced incomparable pair, and has the inherited transitive strong-majority order `prec_*`. Let

`a_0 || b_0`, `a_0 prec_* b_0`, and `Pred(a_0)=Pred(b_0)`.

Then after finitely many applications of the fleet04/B10 equal-predecessor channel theorem one obtains an extreme incomparable pair `u prec_* v` with

`Pred(u) != Pred(v)`.

More precisely, every recursive clean step is a fork-escalation step, and the chosen left endpoints form a strict poset chain.

### Proof

Apply the partner theorem to a current equal-predecessor pair `a||b`, `a prec_* b`.

**Span-descent case.** There is a positive blocker `z` with `a<_P z`, `z||b`, and `a prec_* z prec_* b`. The new extreme pair is `(z,b)`. It already has unequal predecessor sets: `a in Pred(z)`, while `a notin Pred(b)` because `a||b`. Thus span descent terminates the clean branch immediately, with the old left endpoint `a` itself as an explicit lower distinguisher.

**Fork-escalation case.** There are two positive Hasse blockers `z_1,z_2`, both strictly above `a` in the poset and incomparable with each other. Orient them in the total strong-majority order, say `a' prec_* b'`. If `Pred(a')!=Pred(b')`, the desired lower-distinguisher branch is reached. If their predecessor sets are equal, apply the partner theorem again to `(a',b')`.

In the latter recursive case the new left endpoint satisfies `a<_P a'`. Consequently every clean recursive fork strictly raises the left endpoint in the partial order. A finite poset has no infinite strict ascending chain. Hence clean fork escalation cannot continue indefinitely. The process must eventually terminate either by span descent, which was just shown to produce unequal predecessor sets immediately, or by a fork whose two blockers already have unequal predecessor sets. `□`

### Consequence for the current lead route

The equal-predecessor branch is no longer a terminal global obstruction. Starting from the first-boundary sibling pair, either a lower distinguisher is already present or the exact positive-channel process reaches one after finitely many fork steps. The unresolved structural branch is therefore the **unequal-predecessor / lower-distinguisher branch**, not an indefinitely iterated clean fork.

This does not solve POS3: the missing theorem is to use such a lower distinguisher, together with the exact heavy-slice/pinned-rank constraints or the cut-charge identity above, to force a balanced pair, a width-four antichain, or an excluded module/decomposition.

## 6. Exact ideal-state regression checks

A dependency-free verifier accompanies this report. It checks two source-valid finite witnesses, only as regression evidence for the symbolic statements above.

### 6.1 The 349-extension chain-deletion witness

For the preceding B19 nine-element poset, deleting `C=(2,5,8)` leaves the exact weighted remainder on `Q=(0,1,3,4,6,7)`. The checker verifies `(CC)` for **every ordered pair of distinct retained elements**.

For four previously compressed strong boundaries it prints:

```text
(0,1): Q rank numerator 265, full rank numerator 353,
       chain charge pieces 176,0,0; total 176 = 2(353-265).
(1,3): Q rank numerator 320, full rank numerator 427,
       pieces 136,78,0; total 214 = 2(427-320).
(4,6): Q rank numerator 281, full rank numerator 390,
       pieces 94,124,0; total 218 = 2(390-281).
(6,7): Q rank numerator 310, full rank numerator 548,
       pieces 84,182,210; total 476 = 2(548-310).
```

The two known parent-rescuing cross-interface balanced pairs are still exactly

`Pr(2<3)=156/349`, `Pr(5<6)=156/349`.

The cut-charge decomposition exposes these in the relevant boundary pieces: for `(1,3)` the `c=2` endpoint has signed numerator `B(3,2)=37`, and for `(4,6)` the `c=5` endpoint has `B(6,5)=37`, both inside the balanced signed band `[-349/3,349/3]`. This is evidence that `(CC)` points at the correct interface in the obstruction; it is not promoted to a universal forcing theorem.

### 6.2 The 79-extension clean-fork witness

For the seven-element Hasse-fork example from fleet03/B11, take the equal-predecessor pair `(a,b)=(4,3)`. Exact counting gives `E=79`, `Pred(4)=Pred(3)={0}`, and `Pr(4<3)=56/79>2/3`.

The partner channel decomposition is reproduced exactly:

`C_{4->3}(5)=10`, `C_{4->3}(6)=23`, total `33>79/3`,

with the `6` channel alone `23>79/6`. The next blocker pair is not clean:

`Pred(6)={0,4}`,

`Pred(5)={0,1,2,4}`.

So this concrete fork terminates after one escalation exactly as Theorem 5.1 predicts. The known balanced escape `(2,3)` remains `42/79` in the displayed orientation.

The captured output terminates with

`POS3_B19_CUT_CHARGE_FORK_COLLAPSE_CHECK_PASS`.

The verifier Git blob after readback is recorded in the coordination handoff. The local regression execution used only the Python standard library; the finite checks are not the proof of Theorems 2.1 or 5.1.

## 7. What moved and what remains

**Paid in this run.** Two pieces of the first missing global implication moved:

1. the exact chain-deletion rank/corridor defect now has a closed signed charge identity landing directly on actual deleted-chain pair numerators; and
2. the campaign lead's clean equal-predecessor branch cannot recurse forever: it must reach unequal predecessors after finitely many exact channel steps.

**Still unpaid.** POS3 itself remains open. The decisive residual is now narrower:

> **Lower-distinguisher interface implication.** In a cardinality-minimal width-three no-balanced candidate, take the unequal-predecessor extreme pair forced by Theorem 5.1. Combine its first lower distinguisher with the exact cut-charge identity `(CC)`, the partner's `>E/6` channel when the pair arises from a fork, the `>1/81` pinned-rank atoms, and the existing simultaneous heavy-slice inequalities. Prove that one actual pair meeting the relevant chain enters the balanced band, or derive a four-antichain / proper autonomous nonchain / forbidden decomposition.

The new identity means this next step can be stated directly in pair numerators; no unproved uniformity of a deleted law remains hidden in the formulation.

## 8. Claim status

- Exact deletion cut-charge identity `(CC)`: **PROVED** for every finite poset and every deleted subset.
- Fiberwise chain-corridor refinement `(3.1)-(3.2)`: **PROVED**, using the exact fleet01/B19 recurrence.
- Strong-majority interposed-chain inequality `(4.1)`: **PROVED**, conditional on the standard hypothetical no-balanced state.
- Finite collapse of repeated clean equal-predecessor fork escalation to unequal predecessors: **PROVED**, conditional on the fleet04/B10 span-descent/fork theorem.
- Parent width-three `1/3–2/3` conjecture: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark work, brain installation, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, remote workflow, or permission change was used.
