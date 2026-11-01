# POS3 fleet03/B10 — the exact-two recurrence reaches the first non-exact boundary with zero probability defect

**Run:** `b10-20260922t061504z-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every count below is a literal count of full linear extensions of the original poset. Deletion skeletons enter only through the already-proved exact lift identities; no induced deletion law is renamed uniform.

## 1. Exact collective state consumed

The exact fleet03/B10 assignment is:

> Apply bounded-width/high-variance results to the exact width-three target and derive the remaining exceptional-case requirement with constants/hypotheses explicit.

The assigned OTHER-account partner consumed directly is **fleet04/B11**, latest completed run

`proofnet24/collective-POS3/fleet04/B11/20260922T051337Z-B11-pos3-r15/REPORT.md`.

Its width-three interval-order family `R_N` has `pi=7`, every rank variance at most `49/4`, arbitrarily many consecutive exact-two states with actual minority in `(1/5,4/13)`, and arbitrarily many heavy cover flips with exactly two external witness channels. The family escapes only at its far boundary, where the actual far pair is balanced. Thus bounded width, bounded incomparability range, bounded rank variance, and bounded local witness arity do **not** imply a bounded corridor. The first missing implication is necessarily a global maximal-boundary statement.

I also use the latest completed campaign lead, fleet04/B10 r14,

`proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`,

which proves that a surviving bridged blocker branch contains a cover carrying `>E/3` full-extension flux and therefore at least two external relation channels in a no-balanced core.

For the exact corridor algebra I use the already-frozen fleet03/B19 r11/r12 transfer:

- `proofnet24/collective-POS3/fleet03/B19/20260922T040111Z-b19-pos3-r11/REPORT.md`;
- `proofnet24/collective-POS3/fleet03/B19/20260922T045925Z-b19-pos3-r12/REPORT.md`.

For two consecutive exact-two crossed states these reports prove, skeleton by skeleton before summation, a conserved integer `K` and

`E/3 < K < 2E/3`,

with the interior recurrence

`A_(i-1) + 3 A_i + A_(i+1) = E + K`.

Finally fleet01/B19 r13,

`proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`,

proves that in a continuing corridor a deep four-pair window at distance `d` from both boundaries gives

`K/E >= 4/11 - eps_d`,

where

`rho=(3-sqrt(5))/2`,
`eps_d = [10/(3(1-rho^2))] rho^d`.

That report phrased the next target as an exit-defect sign/conversion lemma. The theorem below corrects the first part of that formulation: at the *first* non-exact fringe pair there is no probability-count defect at all.

## 2. Setup at the last exact-two state

Let state `i` be an exact-two crossed state reached from a preceding exact-two state `i-1` by the canonical lower-fringe continuation. Use the current four special labels `d,x,y,u`, with

- `x||y`;
- `d in Pred(y)\Pred(x)`;
- `u in Succ(x)\Succ(y)`.

After summing the exact residual-skeleton lift counts, let the six possible relative-word counts be

`A = N(d y x u)`,
`C = N(d x y u)`,
`X = N(d x u y)`,
`Y = N(x d y u)`,
`Z = N(x d u y)`,
`W = N(x u d y)`.

The exact-two swap identity gives

`C=A`.                                                        (2.1)

Because the *preceding* state continues exactly into the present state, the inherited transfer identities give

`Z = K-A`,                                                    (2.2)

`X = A_prev + A - K`,                                        (2.3)

where `A_prev=A_(i-1)` and `K` is the conserved corridor count.

No assumption is now made that the *next* fringe state is exact-two. It may have extra relation distinguishers, fail the next transfer, or be the maximal corridor boundary.

The actual next lower-fringe pair is `(d,x)`. Since `d||x`, its literal full-extension orientation count is

`B := N(x<d) = Y+Z+W`.                                       (2.4)

This is an actual pair-ordering count in `P`, not a formal recurrence variable.

## 3. First-boundary recurrence theorem

### Theorem 3.1 — zero probability defect at the first non-exact boundary

Under (2.1)--(2.4), regardless of whether the next fringe state is exact-two,

`A_prev + 3A + B = E + K`.                                   (3.1)

Equivalently,

`B = E+K-A_prev-3A`.                                         (3.2)

Thus the interior exact-two recurrence extends **one full step to the actual first boundary pair**. In particular the proposed additive exit defect

`Delta := B - (E+K-A_prev-3A)`                               (3.3)

is identically

`Delta=0`.                                                    (3.4)

### Proof

The six full-extension word classes partition all extensions, so by (2.1)

`E = 2A+X+Y+Z+W`.                                            (3.5)

Substitute (2.2)--(2.3):

`E+K-A_prev-3A`
` = 2A+X+Y+Z+W+K-A_prev-3A`
` = Y+Z+W`
` = B`.

No distribution on a deletion skeleton appears. Every term is an exact full-extension count. `square`

### Interpretation

Extra distinguishers at the first non-exact state do **not** create a signed correction to the next pair probability. They obstruct the *next transfer/conservation step*, not the count of the first boundary pair itself. Therefore a proof strategy that tries to show “the extra distinguisher contributes a positive exit defect to `A_next`” is aimed at a quantity whose defect is exactly zero.

The global charge problem is consequently narrower: one must use the new boundary structure to transfer the already-existing latent charge `K` to a different actual event/pair, or force span descent / another controlled exit.

## 4. Explicit exceptional-case requirement in a hypothetical no-balanced core

Assume the first boundary pair `(d,x)` keeps the corridor polarity, so `B=N(x<d)` is its minority count. In a hypothetical POS3 counterexample,

`B<E/3`.                                                      (4.1)

But the inherited latent-mass theorem gives

`K>E/3`.                                                      (4.2)

Subtracting (3.2) from `K` yields the exact boundary-overload identity

`K-B = A_prev+3A-E`.                                         (4.3)

Hence every surviving same-polarity first boundary must satisfy

`A_prev+3A>E`.                                                (4.4)

In particular, because `A_prev<E/3`,

`A>2E/9`.                                                     (4.5)

This is a genuine actual-law exceptional-case requirement: a no-balanced maximal boundary cannot be arbitrary. The last two corridor minorities must already carry more than one full extension-count unit in the weighted combination `A_prev+3A`.

### Long-corridor quantitative overload

If the same conserved `K` has a four-pair window at distance at least `d` from both boundaries, fleet01/B19 r13 gives

`K/E >= 4/11-eps_d`,
`eps_d=[10/(3(1-rho^2))]rho^d`, `rho=(3-sqrt(5))/2`.

Combining with `B<E/3` and (4.3),

`A_prev+3A-E = K-B`
` > K-E/3`
` >= (1/33-eps_d)E`.                                         (4.6)

For `d>=6`, `eps_d < 0.012121 < 1/33`, so a sufficiently deep surviving corridor must satisfy the explicit strict overload

`A_prev+3A > 1.01818 E`                                      (4.7)

(the displayed decimal is a conservative rounding of the `d=6` bound). Larger `d` drives the required excess toward `E/33`.

This does not prove POS3; it identifies the first maximal-boundary configuration that a counterexample would have to realize.

## 5. Direct calibration on the assigned partner's `R_N` family

The fleet04/B11 family is an exact regression guard for Theorem 3.1.

Its full-extension counts satisfy

`E_(n+1)=E_n+E_(n-1)`.

At the far end of the exact-two corridor,

`A_prev = Q_(N,N-4) = 2E_(N-4)`,
`A      = Q_(N,N-3) = E_(N-3)`,
`B      = Q_(N,N-2) = E_(N-2)`.

The Fibonacci recurrence gives

`E_N = 2E_(N-4)+3E_(N-3)`,                                   (5.1)

so this family lies exactly on the overload boundary

`A_prev+3A=E_N`.                                              (5.2)

Theorem 3.1 therefore gives

`B=K`.                                                        (5.3)

And fleet04/B11 proves

`1/3 < B/E_N < 2/5`,                                         (5.4)

which is precisely the balanced far-boundary escape. Thus the assigned partner family does more than refute bounded local termination: it **saturates the new threshold**. A hypothetical no-balanced exit must move strictly to the overload side (4.4).

For `N=30`, the exact numbers are

`E=10397611`,
`A_prev=3033982`,
`A=2454543`,
`B=K=3971534`,

and indeed

`A_prev+3A=10397611=E`,
`B/E=567362/1485373`.

## 6. Deterministic regression

`verify_first_boundary_recurrence.py` checks two independent things:

1. `400500` nonnegative integer tuples satisfying the inherited transfer relations, verifying identically that the actual boundary count equals `E+K-A_prev-3A` even when an arbitrary `W` channel is retained;
2. the fleet04/B11 `R_N` boundary calibration for every `11<=N<=200`, including `A_prev+3A=E_N`, `B=K`, and `1/3<B/E_N<2/5`.

Captured output:

```text
POS3_FIRST_BOUNDARY_RECURRENCE_PASS
algebra_tuples_checked 400500
partner_RN_boundary_checks 190
R30 {'E': 10397611, 'A_prev': 3033982, 'A': 2454543, 'B': 3971534, 'K': 3971534, 'B_over_E': '567362/1485373'}
```

The verifier is regression evidence only; Theorem 3.1 is the symbolic proof above.

## 7. What was derived/refuted and the next exact implication

**Derived.** The exact second-order corridor recurrence reaches the first actual non-exact boundary pair with no change of law and no count correction.

**Refuted.** The candidate mechanism in which extra boundary distinguishers first appear as a signed additive defect in `A_next` is false: that defect is identically zero.

**Derived.** In a same-polarity no-balanced boundary, the last two exact-two minority counts must satisfy `A_prev+3A>E`; with a deep continuing window they satisfy the stronger quantitative overload (4.6).

**Assigned partner applied.** fleet04/B11's `R_N` family lies exactly at `A_prev+3A=E` and realizes `B=K` as a balanced boundary pair, showing that the inequality is sharp at the escape surface.

**First unpaid implication.** Prove a **boundary-overload-to-channel theorem**: under width three, no span descent, no autonomous reduction, and the structural failure of the next exact-two transfer, show that the strict overload `A_prev+3A-E=K-B>0` (or the stronger deep-corridor amount) must be realized by the extra distinguisher channels as an actual balanced pair, a target-scale heavy cover/bridge event, or a controlled multi-distinguisher exit. The probability recurrence itself needs no repair; only the structural conversion is missing.

POS3 remains **OPEN / NOT PROVED**. No novelty or priority claim is made.
