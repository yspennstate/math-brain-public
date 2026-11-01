# POS3 fleet01/B10 — fixed-ray mixed recycling has an exact integer potential

**Run:** `20260922T072132Z-b10-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the original uniform law on all full linear extensions. No deletion-induced law is treated as uniform.

## 1. Fresh collective inputs consumed

The current campaign-lead state consumed is fleet04/B10 r17:

- `proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, science commit `732a848a9fa315f3907c654f0c54591dfe04535d`, report blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

It reduces the same-ray heavy-cover exception to a coherent width-saturating three-antichain gate after proving strict packet order in the comparable typed gate and an anchor-free `>2/33` blocker pair in the anti-aligned incomparable gate.

I apply three named OTHER-account results.

1. **fleet03/B19 same-ray outward export**, `proofnet24/collective-POS3/fleet03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/REPORT.md`, report blob `48cf2835f68b5c19c6f1d262335267ca2ad172d1`. After excluding already-authorized strict span descent, a right same-ray nested gate forces an external relation distinguisher strictly beyond its current envelope, and the coherent three-antichain gate forces two; the left statement is dual.
2. **fleet04/B20 incoming-superinterval theorem**, `proofnet24/collective-POS3/fleet04/B20/20260922T071019Z-b20-pos3-r11/REPORT.md`, report blob `3d2ecfd550256af2288f570d8de9b7a217e2c963`. Every incoming reverse-transposition defect is losslessly recoded to a minority pair whose strong-majority interval is a strict superinterval of the old charged half-interval.
3. **fleet02/B11 r17 leaf theorem**, `proofnet24/collective-POS3/fleet02/B11/20260922T065006Z-b11-pos3-r17-50176f59/REPORT.md`, report blob `c1e9ea6932c90f6dfe361041c0b817dccb03bb9d`. An incomparability-graph leaf in the surviving majority-late branch cannot be terminal: its reverse channel is exactly a two-channel double fan in the hard case and is rerouted to span descent or a successor-chain corridor / further nonlocal mechanism.

I also use fleet04/B20's earlier successor-staircase theorem: for `x||y_0`, `Pred(x) subseteq Pred(y_0)`, and a non-crossed successor staircase `y_0 lessdot ... lessdot y_m` with all `y_i||x`, the minority counts `q_i=Pr(y_i<x)` decrease and the cover-gap charges telescope.

## 2. The strong-majority relation is an actual total order in a hypothetical counterexample

Assume throughout this section that there is no balanced pair. Define, for distinct vertices,

`u prec_* v`

when either `u<v` in the poset or `u||v` and `Pr(u<v)>2/3`.

Because there is no balanced pair, exactly one of `u prec_* v` and `v prec_* u` holds for every distinct pair.

### Lemma 2.1 — transitivity

`prec_*` is a strict total order.

**Proof.** It is a tournament orientation. A directed triangle

`u prec_* v prec_* w prec_* u`

would give three events `u<v`, `v<w`, `w<u`, each of probability strictly greater than `2/3` (or probability one when supplied by a poset relation). Hence

`Pr(u<v, v<w, w<u) > 1-1/3-1/3-1/3 = 0`,

where strictness comes from the strict `>2/3` inequalities. But no linear extension can realize a cyclic order. Thus the tournament has no directed triangle. Every cyclic tournament contains a directed triangle, so the tournament is transitive. `square`

Let `rho(v) in {0,...,n-1}` denote the rank of `v` in this total order. For an active incomparable pair `p prec_* q`, put

`sigma(p,q)=rho(q)-rho(p)`.

## 3. New fixed-right-ray potential

For a right-facing charged incomparable pair `p prec_* q`, define

`Psi_R(p,q) = n*rho(q) + sigma(p,q)`.

This is an integer in a finite interval. The coefficient `n` is deliberately larger than the largest possible loss of span in one transition.

### Theorem 3.1 — three current right-ray mechanisms strictly increase `Psi_R`

Suppose a transition stays on the same right strong-majority ray, no balanced pair or authorized strict span descent has occurred, and the transition is one of the following three already proved collective mechanisms.

**(A) Same-ray distinguisher export.**  A B19 nested or coherent-gate export produces a required external distinguisher `z` with the old right envelope endpoint `q prec_* z`. Because `z` distinguishes the active incomparable pair, it is comparable with exactly one endpoint and incomparable with the other. The incomparable endpoint together with `z` is therefore a new actual incomparable pair `p' || z`, and its right endpoint has rank strictly larger than `rho(q)`.

**(B) Incoming reverse-transposition recoding.**  B20 recodes the current charged interval `[p,q]_*` to an actual incomparable pair `p' prec_* q'` whose `prec_*` interval is a strict superinterval:

`[p,q]_* proper_subset [p',q']_*`.

Thus `rho(q')>=rho(q)`, `rho(p')<=rho(p)`, and at least one inequality is strict.

**(C) Non-crossed successor staircase.**  In B20's staircase `y_i lessdot y_(i+1)` with `x||y_i`, orient the initial pair as `x prec_* y_0`, so `q_0=Pr(y_0<x)<1/3`. Since

`{y_(i+1)<x} subseteq {y_i<x}`,

we have `q_(i+1)<=q_i<1/3`, hence `x prec_* y_i` for every `i`. Poset comparability gives `y_i prec_* y_(i+1)`, so the right endpoint rank strictly increases at every staircase step.

Then every transition of type (A), (B), or (C) strictly increases `Psi_R`.

**Proof.**

For (A) and (C), the right endpoint rank rises by at least one. The span can drop by at most `n-2`, so

`Delta Psi_R >= n-(n-2)=2>0`.

For (B), if `rho(q')>rho(q)`, the same estimate applies. If `rho(q')=rho(q)`, strict superinterval containment forces `rho(p')<rho(p)`, hence `sigma(p',q')>sigma(p,q)` and again `Delta Psi_R>0`. `square`

### Corollary 3.2 — no fixed-right-ray recycler from these mechanisms

No directed cycle can be composed solely of transitions (A)-(C) while staying on one right ray. In fact a chain of distinct such charged states has length at most the number of ordered rank intervals, hence at most `n(n-1)/2` before it must terminate or leave this transition class.

The order-dual statement holds on the left ray with

`Psi_L(p,q)=n*(n-1-rho(p)) + sigma(p,q)`.

Thus B19's same-ray outward export and B20's incoming-superinterval / successor-staircase transport are not merely locally non-returning: **their arbitrary interleaving on a fixed ray is globally acyclic.**

## 4. Application of the designated fleet02/B11 partner result

The fleet02/B11 r17 leaf theorem removes a potential loophole in the preceding reduction. A fixed-ray chain cannot simply stop at an incomparability leaf and declare a neutral terminal state. In the hard no-balanced majority-late leaf state B11 proves that the reverse union has mass in `(1/3,2/3)`, is supported on exactly two Hasse predecessor channels, and the state reroutes to span descent or to the already identified double-fan / successor-corridor continuation.

Therefore a leaf landing has only two outcomes relevant here:

- it triggers one of the accepted terminating alternatives; or
- it exits the present fixed-ray monotone class into a further corridor/crossed/ray-switch mechanism.

It cannot furnish a zero-gain fixed-ray return edge. This is exactly how the designated partner theorem is used in the present end-to-end reduction.

## 5. Compact conditional end-to-end argument

The current collective proof architecture can now be written more sharply.

1. Work in a hypothetical minimal width-at-most-three counterexample. The no-balanced hypothesis supplies the total order `prec_*` by Lemma 2.1.
2. The lead heavy-cover argument creates two genuine outward minority packets at the `2/33` gap scale.
3. Lead r17 pays the generic comparable same-ray gate and the anti-aligned incomparable gate; fleet03/B19 forces the remaining nested/coherent same-ray gate to export a new relation distinguisher beyond the current envelope unless strict span descent occurs.
4. fleet04/B20 shows that an incoming reverse-transposition cancellation cannot absorb charge locally: it moves to a strict strong-order superinterval. Its non-crossed successor staircase transports charge through a strictly advancing sequence of right endpoints.
5. Theorem 3.1 shows that arbitrary mixtures of precisely these three outward mechanisms on one fixed ray admit the strict integer potential `Psi_R` (dually `Psi_L`) and therefore cannot recycle.
6. fleet02/B11 prevents an incomparability leaf from serving as a neutral terminal of this monotone chain.

Hence a surviving recycler in a counterexample must now use a mechanism **outside the fixed-ray monotone class**: it must switch rays or pass through an exact-two/crossed/bridge/non-crossed transition whose charged interval is not already covered by the superinterval/staircase theorem.

## 6. First unpaid implication after this run

The first essential missing implication is now:

> **RAY-SWITCH / CROSSED ACCOUNTING.**  Give the remaining opposite-ray switch and exact-two/crossed/bridge transitions an integer potential or conserved-charge inequality compatible with `Psi_R,Psi_L`, so that a transition which resets the active outward endpoint must compensate by a strict increase in pair-minority charge, exact-two `K`, global exposed hull, or another bounded integer statistic.

Equivalently, a genuine counterexample can no longer recycle using same-ray export plus incoming reverse-transposition plus successor-staircase motion alone. Any cycle must contain at least one presently unpaid ray-changing/crossed edge. Paying those edges would turn the local outward machinery into a finite termination proof.

I do **not** claim this closes POS3, and I do not claim that `Psi_R` is monotone across arbitrary ray switches or crossed states. The theorem is intentionally scoped to the three mechanisms whose endpoint/superinterval behavior has already been proved.

## 7. Integrity/status

- fleet04/B10 r17: **CONSUMED/APPLIED**;
- fleet03/B19 same-ray export: **CONSUMED/APPLIED**;
- fleet04/B20 incoming-superinterval and successor-staircase mechanisms: **CONSUMED/APPLIED**;
- designated partner fleet02/B11 r17 leaf theorem: **CONSUMED/APPLIED**;
- strong-majority total-order lemma: **PROVED**;
- fixed-right / fixed-left integer potentials and acyclicity: **PROVED**;
- mixed fixed-ray recycling for mechanisms (A)-(C): **ELIMINATED**;
- ray-switch / general crossed accounting: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run label: `ESSENTIAL_STEP_APPLIED`.

No computation is required for this arbitrary-size argument. No benchmark material, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive data, paid/remote model/API/Codex calls, workflow dispatch, permission change, or public posting was used.
