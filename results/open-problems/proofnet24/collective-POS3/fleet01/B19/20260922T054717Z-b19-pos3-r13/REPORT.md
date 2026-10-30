# POS3 fleet01/B19 — four-state exact-two selector and deep-corridor latent-mass amplification

**Run:** `20260922T054717Z-b19-pos3-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is under the original uniform law on all full linear extensions. Deletion skeletons appear only through exact lift counts; no induced deletion law is treated as uniform.

## 1. Exact collective inputs consumed

The latest complete campaign-lead report used is

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, blob `50bac494667235f3630991a512438eac42c30521`.

It proves that a lead bridge `c<u` with `c||a`, `u||a`, `c prec_* a prec_* u` contains a unique saturated-chain cover `x lessdot y` with

`Pr(x<a<y)>1/3`,

and, using the fleet01/B19 cover theorem, that such a heavy flip must export through at least two external relation channels in a hypothetical no-balanced core. Its remaining obligation is global recycling/boundary realization.

The assigned OTHER-account partner used directly is

- fleet02/B10, `proofnet24/collective-POS3/fleet02/B10/20260922T044758Z-b10-r12-9941265a/REPORT.md`, blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`.

Its defect/arity compression lemma gives a local exact-two selector of at least `1/4`, and a general strict-corridor selector of at least `1/5`, while retaining the true full-extension weights.

The second essential OTHER-account input is

- fleet03/B19, `proofnet24/collective-POS3/fleet03/B19/20260922T045925Z-b19-pos3-r12/REPORT.md`, blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`.

For two consecutive exact-two crossed states it gives an eight-word exact lift decomposition with, after summing actual residual-skeleton multiplicities,

`E=3a+2b+2c+t`,                                               (1.1)

`b<=a`, `t<=b`, `t<=c`,                                      (1.2)

and a conserved corridor integer

`K=a+b+c`, `E/3<K<2E/3`.                                     (1.3)

Across a continuing exact-two corridor the endpoint minority counts satisfy the exact second-order recurrence

`A_(i-1)+3 A_i+A_(i+1)=E+K`.                                 (1.4)

Finally I use the source-valid family in

- fleet04/B11, `proofnet24/collective-POS3/fleet04/B11/20260922T051337Z-B11-pos3-r15/REPORT.md`, blob `4954518777f25e543dadcede02952692ca52874d`.

That family has arbitrarily long exact-two corridors in width three and therefore rules out replacing the global boundary step by a bounded local corridor-length argument.

## 2. Compact conditional end-to-end route

Assume for contradiction that a cardinality-minimal width-at-most-three counterexample exists.

1. The lead r14 bridge theorem turns the surviving bridged blocker branch into a literal cover-gap event of mass `>E/3`.
2. The inherited cover two-witness theorem forces at least two external asymmetry channels at that heavy edge.
3. If these channels recycle into the exact-two corridor, fleet03/B19 supplies (1.1)--(1.4).
4. The theorem below improves the assigned partner's `1/4` exact-two selector to `3/11`: every continuing four-pair window contains an actual incomparable pair whose minority count is at least `3E/11`.
5. Solving (1.4) exactly shows that a long corridor cannot keep the latent mass merely just above `E/3`: a deep continuing window forces `K/E` toward at least `4/11` up to an exponentially small boundary term.
6. The fleet04/B11 family shows that this still cannot be promoted to `1/3` by a local fixed-length selector: four consecutive source-valid corridor minorities can all be below `3/10`.

Thus the first unpaid target-level step is now a boundary-defect conversion theorem at the first non-exact-two exit, not another local selector or bounded-length argument.

## 3. Exact four-pair count identities

Use the fleet03/B19 five-label notation `e,d,x,y,u`. The central two exact-two states satisfy

`Pred(y)=Pred(x) union {d}`, `Succ(x)=Succ(y) union {u}`,

`Pred(x)=Pred(d) union {e}`, `Succ(d)=Succ(x) union {y}`.

Delete these five labels and fix any exact residual skeleton. After summing every skeleton with its actual number of legal lifts, the eight possible special-label words have counts

`P1=e d x y u : a`,
`P2=e d x u y : b`,
`P3=e d y x u : a`,
`P4=e x d y u : a`,
`P5=e x d u y : b`,
`P6=d e x y u : c`,
`P7=d e x u y : t`,
`P8=d e y x u : c`.

The exact swap injections of fleet03/B19 give (1.2). Reading the four neighboring incomparable-pair inversion events directly from these words gives

`M_0 := N(d<e) = 2c+t`,                                      (3.1)
`M_1 := N(x<d) = a+b`,                                       (3.2)
`M_2 := N(y<x) = a+c`,                                       (3.3)
`M_3 := N(u<y) = 2b+t`.                                      (3.4)

No projected probability measure occurs in (3.1)--(3.4): these are literal full-extension counts.

In a continuing strong-majority corridor the displayed orientations are the minority orientations. If one of the two outer orientations has already reversed, that is a corridor exit rather than a continuing window; if it lies in `[E/3,2E/3]`, POS3 is already satisfied.

## 4. New theorem: the `3/11` four-state selector

### Theorem 4.1

Under (1.1)--(1.2), put

`M=max(M_0,M_1,M_2,M_3)`.

Then

`M >= 3E/11`.                                                 (4.1)

Equality holds if and only if

`a=2E/11`, `b=c=t=E/11`,                                     (4.2)

in which case

`M_0=M_1=M_2=M_3=3E/11`, `K=4E/11`.                         (4.3)

Consequently a continuing four-pair exact-two corridor in a hypothetical no-balanced poset contains an actual incomparable pair with minority probability in

`[3/11,1/3)`.                                                 (4.4)

If equality occurs with integer lift counts, `11` divides `E`.

### Proof

Let `M` be as above. From (3.2)--(3.3),

`2a+b+c=(a+b)+(a+c)<=2M`.                                    (4.5)

From (3.1) and (3.4),

`b+c+t=((2b+t)+(2c+t))/2<=M`.                                (4.6)

Also (3.2)--(3.3) give `b,c<=M-a`, while (1.2) gives

`t<=min(b,c)<=M-a`.

Hence

`b+c+t<=3(M-a)`.                                              (4.7)

Therefore

`a+b+c+t <= a+min(M,3(M-a)) <= 5M/3`.                       (4.8)

The last inequality is elementary: the two arguments of the minimum cross at `a=2M/3`; on either side the displayed expression is at most `5M/3`.

Using (1.1),

`E=(2a+b+c)+(a+b+c+t)`
` <= 2M+5M/3=11M/3`,

which is (4.1).

For equality, (4.5) must be tight, so `a+b=a+c=M`, hence `b=c=M-a`. Equality in (4.8) forces `a=2M/3` and `b+c+t=M`; thus `b=c=t=M/3`. Substituting into `E` gives `E=11M/3`, which is exactly (4.2)--(4.3). Conversely those ratios give equality. `square`

### What this pays

The assigned partner's exact-two local floor was `1/4`. The new bound is

`3/11 = 0.272727... > 1/4`.

Thus once a lead/partner branch genuinely recycles through two consecutive exact-two states with the same corridor polarity, one of the four neighboring actual pair probabilities is within at most

`1/3-3/11 = 2/33`                                             (4.9)

of the balanced threshold.

## 5. Exact solution of the corridor recurrence

The recurrence (1.4) has a useful boundary form that was not previously extracted.

Let a continuing exact-two corridor have minority counts `A_0,...,A_(n+1)` and recurrence (1.4) for `1<=i<=n`. Put

`q=(E+K)/5`,                                                  (5.1)

`B_i=A_i-q`.

Then

`B_(i+1)+3B_i+B_(i-1)=0`.                                    (5.2)

Set `C_i=(-1)^i B_i`. Then

`C_(i+1)-3C_i+C_(i-1)=0`.                                    (5.3)

Let `theta>0` be defined by `2 cosh(theta)=3`, equivalently

`rho=e^(-theta)=(3-sqrt(5))/2`.                              (5.4)

The unique two-boundary solution is

`C_i = [sinh((n+1-i)theta)/sinh((n+1)theta)] C_0`
`    + [sinh(i theta)/sinh((n+1)theta)] C_(n+1)`.             (5.5)

This is checked by substitution into (5.3) and the two boundary values. Thus exact-two corridor deviations from the central level `q` are entirely boundary-generated and decay exponentially into the interior.

If the whole corridor remains in the no-balanced minority regime `0<=A_j<E/3`, then by (1.3)

`4E/15 < q < E/3`,                                           (5.6)

so `|A_0-q|,|A_(n+1)-q|<=E/3`. For `d=min(i,n+1-i)`, (5.5) gives the convenient bound

`|A_i-q| <= [2E/(3(1-rho^2))] rho^d`.                        (5.7)

No asymptotic probability model is used; (5.5) is an exact solution of the integer-count recurrence after division by the common count `E` only if desired.

## 6. New long-corridor consequence: `K` is forced upward

Take any four-pair window lying at distance at least `d` from both corridor boundaries. Theorem 4.1 supplies some index `j` in that window with

`A_j>=3E/11`.                                                 (6.1)

Apply (5.7) to that index. Since `q=(E+K)/5`,

`K/E >= 4/11 - [10/(3(1-rho^2))] rho^d`.                    (6.2)

Therefore, along arbitrarily long continuing exact-two corridors,

`liminf K/E >= 4/11`.                                        (6.3)

This is a genuine strengthening of the previous universal `K/E>1/3` in the long-corridor regime. It also explains why the earlier explicit family with `K/E ->1/3` cannot simultaneously be an arbitrarily long continuing exact-two corridor: that family only certifies sharpness for the short local latent-mass theorem.

The conclusion is not POS3. It says that a long surviving corridor transports substantially more balanced-sized latent mass than was previously forced, so the remaining boundary realization theorem has a stronger charge available.

## 7. Source-valid counterexample to a stronger local `3/10` selector

The fleet04/B11 family `R_N` gives a regression guard against overclaiming. Its exact full-extension count is

`E_N=8F_(N+1)-13F_(N-7)`,                                    (7.1)

and for `7<=i<=N-3` the adjacent exact-two inversion probability is

`q_i=E_i F_(N-i-1)/E_N`.                                     (7.2)

For `N=30`, the four consecutive interior states `i=12,13,14,15` have exact probabilities

`q_12=410429/1485373 = 0.276313761...`,
`q_13=410592/1485373 = 0.276423498...`,
`q_14=410530/1485373 = 0.276381757...`,
`q_15=410553/1485373 = 0.276397242...`.

All four satisfy

`3/11 < q_i < 3/10 < 1/3`.                                   (7.3)

Thus the tempting stronger local claim

> every continuing four-state exact-two window contains minority at least `3/10`

is false in the actual width-three source model. `R_30` is not a POS3 counterexample: its far boundary contains a balanced pair, exactly as fleet04/B11 proves. The lesson is that the remaining gain to `1/3` must come from the maximal boundary/global exit, not a universal local constant improvement to `3/10`.

## 8. Deterministic regression certificate

`verify_four_state_selector.py` performs two independent checks:

1. exhaustive exact integer verification of `11M>=3E` for all `0<=a,c<=50`, `0<=b<=a`, `0<=t<=min(b,c)`, totaling `901900` nonzero tuples, including the equality characterization;
2. exact rational evaluation of the four `R_30` probabilities above from (7.1)--(7.2).

Captured output begins

```text
POS3_FOUR_STATE_SELECTOR_CHECK_PASS
integer_tuples_checked 901900
minimum_ratio 3/11
minimum_witness (2, 1, 1, 1, 11, (3, 3, 3, 3))
R30_total_extensions 10397611
R30_q12_q15 ['410429/1485373', '410592/1485373', '410530/1485373', '410553/1485373']
```

The finite computation is regression evidence only. The arbitrary-size result is the proof in Section 4; the `R_N` counterexample is the exact symbolic family of fleet04/B11 specialized at `N=30`.

## 9. First essential missing implication

The first unpaid implication is now an **exit-defect sign/conversion lemma** for a maximal exact-two corridor.

At an interior exact-two step the predicted continuation is forced by (1.4):

`A_next^* = E+K-A_prev-3A_current`.                            (9.1)

At the first boundary where exact-two fails, additional relation distinguishers create the difference between the true next fringe ordering count and `A_next^*`. The needed theorem is to derive that difference from the exact deletion-fiber/blocker decomposition and prove, under the inherited no-span-descent/no-autonomous-reduction hypotheses, that either

- an actual boundary incomparable pair already has count in `[E/3,2E/3]`, or
- the extra-distinguisher crossing events carry the missing signed charge into another actual incomparable-pair event that reaches that interval.

This is narrower than a generic `1/5 -> 1/3` amplification request. The exact-two interior is now controlled by (4.1), (5.5), and (6.2); fleet04/B11 rules out a bounded local termination proof. What remains is the first non-exact boundary defect itself.

## 10. Status

- Exact four-neighbor full-extension counts (3.1)--(3.4): **PROVED from the inherited eight-word decomposition**.
- Four-state selector `M/E>=3/11` and equality rigidity: **PROVED**.
- Exact Green-kernel solution (5.5) of the conserved-K corridor recurrence: **PROVED**.
- Deep-corridor strengthening `K/E >= 4/11-o(1)`: **PROVED under the stated continuing-corridor hypotheses**.
- Stronger local selector `>=3/10`: **REFUTED** by the source-valid width-three `R_30` corridor window.
- POS3: **OPEN / NOT PROVED**.

No brain installation or benchmark work was performed. No authenticated brain retrieval/context use occurred. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, public posting, permission change, or production mutation was used.
