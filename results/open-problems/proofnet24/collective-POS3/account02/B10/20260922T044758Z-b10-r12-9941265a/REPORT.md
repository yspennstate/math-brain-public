# POS3 account02/B10 — defect/arity compression upgrades the terminal selector

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Run:** `20260922T044758Z-b10-r12-9941265a`  
**Brain state:** `WITHOUT_VERIFIED_BRAIN` (authenticated GitHub control/source retrieval was used, but no verified brain-package installation/context claim is made).

## 1. Fresh control and exact sources consumed

Fresh main control at login was `923053356dfcf44f4756494f92e882a122c658e4`, OWNER revision `2026-09-22.2`. A later main observation during the run was `f0824c24dad71b34e94c7bea1e96db227ad581be`; no later stop or role change was observed before this report was written. The run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, performs no benchmark or installation work, and keeps the target at width at most three under the uniform law on all full linear extensions.

The latest complete campaign-lead input actually used is account04/B10 r13:

- `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`
- creation/readback commit `fdfdc6be6943abfdef73c950a71c528bf582c6e8`
- blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

That report proves the strict predecessor-nested terminal selector with threshold `1/6`, using the exact original-law blocker identity

`2 Pr(a<b)-1 = Pr(B_+) - Pr(B_-)`.

The required named OTHER-account partner input actually used is account03/B11 r11:

- `proofnet24/collective-POS3/account03/B11/20260922T040957Z-account03-B11-pos3-r11/REPORT.md`
- commit `34def82ee82e3eb7fbc4f0f7783b82d13bdec4a1`
- blob `fd48b47637ca81a6c25fa5c52f8898e596662062`.

It proves the exact-two-distinguisher dichotomy: with one lower and one upper positive distinguisher, the incomparable-fringe case `d||u` has a strict bias-amplification/nonrepeatability conclusion, while the comparable-fringe case `d<u` remains the exact-two residual.

As an adversarial calibration I also consumed account02/B19's prime comparable-fringe cycle handoff, blob `76157c81251c54cfc377494fb633ff2f77679ab0`. Its 11-element width-three autonomous-prime core has 515 extensions and a genuine period-two largest-fringe cycle in the `d<u` exact-two residual. It is not a POS3 counterexample because it contains balanced pairs.

## 2. Compact conditional end-to-end route

Work inside the inherited contradiction setup: `P` has width at most three and has no balanced incomparable pair. Then the strong-majority relation `prec_*` is used as in the lead state. The first-fork reductions funnel the unresolved strict branch to

- `a||b`,
- `Pred(b) proper_subset Pred(a)`,
- `D=Pred(a)\Pred(b)` nonempty and a chain,
- internal strong-majority span descent already exhausted.

The lead r13 argument had a canonical terminal pair whose minority probability lies in `(1/6,1/3)`. The new argument below replaces recursive one-fringe transport by a local **defect/arity stopping rule**. It keeps the exact blocker-union mass in the original uniform law and asks how many canonical channels can carry it.

The result is:

1. in the majority-early polarity, a canonical terminal pair has minority probability in `[1/4,1/3)`;
2. in the majority-late polarity, a canonical terminal pair has minority probability in `[1/5,1/3)`;
3. in the named partner's exact-two-distinguisher branch, regardless of `d||u` or `d<u`, a canonical pair among the endpoint and its two fringe pairs has minority probability in `[1/4,1/3)`.

Thus the common strict-chain terminal selector improves from `1/6` to **`1/5`**, and the exact-two residual improves to **`1/4`**. The B19 period-two cycle no longer needs to be forbidden: the new rule stops locally before following that cycle.

The parent POS3 target is still open. The first essential unpaid implication is now the global amplification

`canonical minority >= 1/5  ==>  some minority >= 1/3`

(or a contradiction such as a four-antichain/proper autonomous nonchain) using the three-chain cumulative-band/blocker structure.

## 3. Defect/arity compression lemma

### Lemma 3.1

Let `epsilon<1/3` be the minority probability of a canonical incomparable endpoint. Suppose the exact original-law transport identity gives canonical outward events `E_1,...,E_m`, each itself the minority orientation of an incomparable pair, such that

`Pr(E_1 union ... union E_m) >= 1-2 epsilon`.                    (3.1)

Then

`max(epsilon, Pr(E_1),...,Pr(E_m)) >= 1/(m+2)`.                 (3.2)

If `epsilon<1/(m+2)`, then some outward event has probability strictly larger than `1/(m+2)`.

### Proof

Put `c=1/(m+2)`. If `epsilon<c` and every `Pr(E_i)<c`, then the union bound, with no independence assumption, gives

`Pr(union_i E_i) <= sum_i Pr(E_i) < m c = m/(m+2)`.

But `epsilon<c` gives

`1-2 epsilon > 1-2c = m/(m+2)`,

contradicting (3.1). If `epsilon>=c`, the endpoint itself gives (3.2). `square`

This is deliberately an original-law statement. It does not condition onto a deletion poset and does not rename a biased projected distribution as uniform. Correlations and overlaps between the channels are retained exactly; the only relaxation is the final union bound.

A useful byproduct is `m=1`: then the threshold is `1/3`, so a no-balanced poset cannot terminate with a single defect-carrying canonical channel. This recovers one-blocker impossibility as an immediate mass/arity consequence.

## 4. Majority-early strict corridor: `1/4`

Use the notation of lead r13. In the majority-early polarity, write

`p=Pr(a<b)>2/3`, `epsilon=1-p=Pr(b<a)<1/3`.

The exact blocker identity gives

`Pr(B_+) - Pr(B_-) = 2p-1 = 1-2 epsilon`,

hence

`Pr(B_+) >= 1-2 epsilon`.                                       (4.1)

Lead r13 compresses `B_+` to the at-most-two minimal successor-difference blockers. After internal span descent is exhausted, every corresponding crossing event is the minority orientation of an incomparable canonical fringe pair and has probability `<1/3`.

Therefore Lemma 3.1 applies with `m<=2`. It yields a canonical pair among the endpoint and those outward blockers with minority probability at least

`1/(2+2)=1/4`,

and still strictly below `1/3` under the no-balanced hypothesis.

So the majority-early lead output strengthens from `(1/6,1/3)` to

`[1/4,1/3)`.                                                    (4.2)

If only one positive blocker channel were present, Lemma 3.1 with `m=1` would force a balanced pair outright; hence the no-balanced terminal residue necessarily needs two channels, matching the partner-side two-blocker geometry.

## 5. Majority-late strict corridor: `1/5`

Now take the majority-late polarity of lead r13:

`b prec_* a`, `p:=Pr(a<b)<1/3`.

Let `d=max(Pred(a)\Pred(b))`, and let

`M=Min(Succ(b)\Succ(a))`.

Lead r13 proves `|M|<=2` and, after internal span descent is exhausted,

`Pr(b<d)<1/3`,
`Pr(u<a)<1/3` for every `u in M`.

Moreover the exact negative blocker event is

`B_- = {b<d} union union_{u in M}{u<a}`                         (5.1)

and the exact transport identity gives

`Pr(B_-) - Pr(B_+) = 1-2p`,

so

`Pr(B_-) >= 1-2p`.                                              (5.2)

There are at most three canonical events in (5.1): one lower-chain event and at most two upper blocker events. Apply Lemma 3.1 with `epsilon=p` and `m<=3`. There is a canonical pair among

`(a,b)`, `(b,d)`, and `(u,a)` for `u in M`

whose minority probability is at least

`1/(3+2)=1/5`,

and is `<1/3` under the no-balanced hypothesis. Therefore the majority-late lead output strengthens from `(1/6,1/3)` to

`[1/5,1/3)`.                                                    (5.3)

The conclusion is strictly stronger when fewer than three channels survive: with two channels the same argument gives `1/4`, and with one channel it forces `1/3` and hence contradicts the no-balanced assumption.

## 6. Application to the named partner's exact-two branch

Take the exact-two configuration isolated by account03/B11. In one orientation the only distinguishers are

`d<y`, `d||x`, `x<u`, `u||y`.

For the majority endpoint `Pr(x<y)>2/3`, the two positive blocker events are exactly

`E_1={x<d}` and `E_2={u<y}`.

There are no opposite-sign distinguishers. Hence the exact original-law identity becomes

`Pr(E_1 union E_2)=1-2 epsilon`,                                (6.1)

where `epsilon=Pr(y<x)<1/3`.

Lemma 3.1 with `m=2` gives

`max(Pr(y<x), Pr(x<d), Pr(u<y)) >= 1/4`.                        (6.2)

All three are minority orientations in the no-span-descent/no-balanced terminal state, so some canonical pair has minority in `[1/4,1/3)`.

This conclusion is independent of whether `d||u` or `d<u`. Thus it applies directly to both branches of account03/B11:

- in the `d||u` branch, the partner's stronger outer-pair bias amplification remains available, but a `1/4` local selector already exists;
- in the `d<u` branch, no anti-cycle theorem is needed merely to preserve quantitative progress: stop as soon as the endpoint or one of the two fringe pairs reaches the `1/4` threshold.

### Exact deletion-fiber interpretation

The same fact can be read directly at deletion-fiber level. Delete `{d,x,y,u}` and fix an exact extension skeleton of the remainder. Since `x,y` have identical relations to every remaining element, they have the same admissible gap interval. Swapping their adjacent special-word positions is a weight-preserving bijection. Summing those exact skeleton counts, with each skeleton carrying its actual number of legal lifts, gives (6.1). No projected skeleton law is assumed uniform.

In the comparable-fringe case `d<u`, the possible special words reduce to five:

`d y x u`, `d x y u`, `d x u y`, `x d y u`, `x d u y`.

The first two have equal counts by the `x<->y` adjacent swap. If their common total count is `A`, and the remaining three counts are `C,D,E`, then

`epsilon=A/T`,
`Pr(x<d)=(D+E)/T`,
`Pr(u<y)=(C+E)/T`,
`T=2A+C+D+E`,

so

`Pr(x<d)+Pr(u<y)-Pr(x<d and u<y)=1-2 epsilon`.

This is (6.1) with every conditioning weight retained.

## 7. Why the B19 period-two cycle no longer blocks this mechanism

The fresh account02/B19 autonomous-prime witness shows that largest-fringe transport itself is not well-founded. Its exact cycle is

`(5,10; d=1<u=6) -> (10,6; d=5<u=3) -> (5,10; ...)`.

The exact verifier in this run re-enumerated all `515` full linear extensions and found:

- first endpoint minority `Pr(10<5)=141/515`;
- first lower fringe `Pr(5<1)=128/515`;
- first upper fringe `Pr(6<10)=161/515`;
- their overlap has count `56`;
- second endpoint minority `Pr(6<10)=161/515`;
- second lower fringe `Pr(10<5)=141/515`;
- second upper fringe `Pr(3<6)=88/515`;
- their overlap has count `36`.

In particular

`141/515 > 1/4` and `161/515 > 1/4`.

So the adversary correctly refutes a *well-founded greedy-fringe* claim, but it does not refute the new defect/arity stopping rule. The new rule halts at the first cycle vertex because the endpoint itself already exceeds the `1/4` minority threshold. This is why the present mechanism is materially different from trying to prove the fringe map acyclic.

The exact regression script and output are saved in this run as

- `verify_defect_arity_selector.py`,
- `verify_defect_arity_selector.out`,

with terminator `POS3_DEFECT_ARITY_SELECTOR_CHECK_PASS`.

The code is a regression/self-check, not the proof of the arbitrary-size theorem.

## 8. What moved and what remains

### Before

The lead's strict-chain terminal quantitative selector was `minority > 1/6`, with the comparable exact-two branch still vulnerable to non-well-founded fringe transport.

### After

The same exact blocker identity yields, without changing the uniform law:

- majority-early terminal selector: `minority >= 1/4`;
- majority-late terminal selector: `minority >= 1/5`;
- common strict-chain terminal selector: `minority >= 1/5`;
- exact-two-distinguisher terminal selector: `minority >= 1/4` irrespective of `d||u` versus `d<u`.

The period-two comparable-fringe cycle is therefore a source-valid obstruction to greedy recursion but **not** to local quantitative selection.

### First essential missing implication

The remaining target-level gap is global, not local:

> In a no-balanced width-three poset, use the three-chain cumulative-band/blocker structure to amplify a canonical terminal minority in `[1/5,1/3)` to `1/3`, or force a width-four antichain, strict span descent, or proper autonomous nonchain.

A promising next version should retain the full blocker-union mass instead of selecting a single fringe event prematurely. In particular, any global charging scheme should price a terminal state by both its endpoint minority `epsilon` and its defect arity `m`; the invariant `1-2 epsilon` is the exact mass that must be routed through those `m` channels.

## 9. Inventory / operational facts

Only account02's exposed scheduler inventory was inspected. The managed B01--B20 set is present, enabled, hourly, and aligned with the current collective/FEI allocation; no deficit requiring B20 action was observed and B10 made zero scheduler mutations.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN / not exposed`. Provider reasoning-token/time usage: `null / not exposed`.

No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, email, Drive, public posting, paid API/model/Codex, remote workflow, or permission change was used.
