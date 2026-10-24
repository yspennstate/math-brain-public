# POS3 account01/B11 — simultaneous two-sided fiber compression at a repeated exact-two corridor

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, stays on the POS3 workstream, and performs no benchmark or installation work. Every probability/count statement below refers to the original uniform law on all full linear extensions. Deletion skeletons are used only as exact partitions with their actual lift multiplicities retained.

## 1. Exact collective state consumed

The latest complete campaign-lead result consumed is account04/B10 r14:

- `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, blob `50bac494667235f3630991a512438eac42c30521`.

It proves that the majority-late bridged blocker branch contains a unique cover `x lessdot y` with the literal full-law gap event

`Pr(x<a<y)>1/3`,

and that account01/B19's cover theorem forces at least two external relation channels at such a heavy cover in any hypothetical no-balanced width-three counterexample. Its first unpaid implication is **two-channel heavy-edge recycling**: the target-scale cover flux must not recycle indefinitely without balance, strict span descent, autonomous reduction, or a controlled multi-distinguisher/non-crossed exit.

The assigned partner result consumed and applied is account02/B19 r12:

- `proofnet24/collective-POS3/account02/B19/20260922T040847Z-account02-B19-pos3-r12-f1f9a5c4/REPORT.md`, blob `a2a326ce5e71abf67cde82f08a6806d067f13978`.

It gives an exact width-three two-cycle for the *greedy largest-fringe* selector. Thus an iteration argument which follows one locally largest exported channel is not a valid global mechanism. This run therefore uses a materially different mechanism: **simultaneous two-sided fiber compression**, with no choice of a largest fringe and no acyclicity assumption.

The essential OTHER-account algebraic input is account03/B19 r12:

- `proofnet24/collective-POS3/account03/B19/20260922T045925Z-b19-pos3-r12/REPORT.md`, blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`.

For two consecutive exact-two crossed canonical lower-fringe states it obtains, skeleton by skeleton, eight five-label lift classes `P1,...,P8` with

`w1=w3=w4`, `w2=w5`, `w6=w8`,

and injective swaps

`w7<=w2`, `w7<=w6`, `w2<=w1`.

After summing the actual lift multiplicities, write

`a=w1=w3=w4`, `b=w2=w5`, `c=w6=w8`, `t=w7`.

Then

`E=3a+2b+2c+t`,                                                (1.1)

with

`t<=b`, `t<=c`, `b<=a`.                                        (1.2)

That report uses these counts to construct the latent balanced-sized invariant `K=a+b+c`. The new argument below instead extracts a direct actual-pair selector from the same fibers and keeps the two non-surjectivity defects `b-t` and `c-t` visible.

I also use account02/B10 r12, blob `2dd9b8b5a1ff8dada78596279ed93fc2cea0b2c1`, as the baseline: an arbitrary single exact-two terminal state has a canonical pair with minority at least `1/4`. The theorem below improves this to `3/11` whenever the exact-two corridor genuinely repeats once.

## 2. Compact conditional end-to-end route

Assume a width-at-most-three counterexample with no balanced pair and use the inherited transitive strong-majority order. The lead r14 reduces one important branch to a neutral-chain heavy cover carrying `>E/3` full-extension mass and forces at least two external witness channels.

If those channels enter a repeated exact-two crossed corridor, the five-label fiber block of account03/B19 applies. The theorem below shows that a repeated exact-two block cannot keep all actual canonical pair minorities near the old `1/4` level:

- among the two consecutive central pairs and the right outer fringe, one minority is at least `3E/11`;
- among the same two central pairs and the left outer fringe, one minority is at least `3E/11`;
- in particular, if both central corridor pairs are below `3E/11`, **both** outer fringe channels are at least `3E/11`.

Thus the exact-two recycling branch either immediately reaches balance, exits the exact-two geometry, or exports two simultaneous actual-pair charges in `[3/11,1/3)`. The remaining numerical gap to balance is only

`1/3-3/11 = 2/33`.

This directly advances the lead's two-channel heavy-edge recycling obligation, but does not close the multi-distinguisher/non-crossed exits.

## 3. Five-label setup and the four actual canonical pair counts

Use the exact consecutive-state hypotheses of account03/B19. Let `e,d,x,y,u` satisfy

`Pred(y)=Pred(x) union {d}`,
`Succ(x)=Succ(y) union {u}`,
`Pred(x)=Pred(d) union {e}`,
`Succ(d)=Succ(x) union {y}`.                                   (3.1)

Thus the current crossed state is `(x,y)` and its canonical lower-fringe continuation is `(d,x)`. The forced relations include

`e<x`, `e<y`, `d<y`, `d<u`, `x<u`.                            (3.2)

For an arbitrary fixed residual deletion skeleton, the eight possible five-label words are those of account03/B19. After summing their exact lift counts, retain the notation (1.1)-(1.2).

The current four-label word counts are

`A=a+c`, `C=a+c`, `X=b+t`, `Y=a`, `Z=b`, `W=0`.                (3.3)

Consequently four actual incomparable-pair orientation counts are

`q0 := #{y<x} = a+c`,                                          (3.4)

`q1 := #{x<d} = Y+Z = a+b`,                                   (3.5)

`qR := #{u<y} = X+Z = 2b+t`,                                  (3.6)

`qL := #{d<e} = 2c+t`.                                        (3.7)

Here `q0` is the current endpoint minority; `q1` is the next lower-fringe endpoint minority when the no-span-descent corridor continues; and `qR,qL` are the right/left outer canonical fringe orientations. In the inherited no-balanced/no-internal-descent corridor, the strong-majority order orients these four displayed directions as minorities, so each is `<E/3` unless balance has already occurred.

The important point is that all four are counts of **actual pair-ordering events in the original full law**. No latent mass needs to be interpreted as a probability event.

## 4. New theorem: repeated exact-two corridors force a `3/11` actual-pair charge

### Theorem 4.1 — two-sided `3/11` fiber selector

Under (3.1), let `E=e(P)` and let `q0,q1,qR,qL` be (3.4)-(3.7). Then

`6 q0 + 3 q1 + 2 qR = 3E + (b-t) >= 3E`,                       (4.1)

and dually

`3 q0 + 6 q1 + 2 qL = 3E + (c-t) >= 3E`.                       (4.2)

Therefore

`max(q0,q1,qR) >= 3E/11`,                                      (4.3)

`max(q0,q1,qL) >= 3E/11`.                                      (4.4)

In particular, if both consecutive central minorities satisfy

`q0<3E/11` and `q1<3E/11`,                                    (4.5)

then simultaneously

`qR>=3E/11` and `qL>=3E/11`.                                   (4.6)

Thus in a no-balanced repeated exact-two corridor, at least one canonical incomparable pair has minority probability in

`[3/11,1/3)`,                                                   (4.7)

and if both central pairs miss `3/11`, two opposite outer channels already lie in that near-target window.

### Proof

Insert (3.4)-(3.6):

`6q0+3q1+2qR`
`=6(a+c)+3(a+b)+2(2b+t)`
`=9a+7b+6c+2t`.

From (1.1),

`3E=9a+6b+6c+3t`,

so subtraction gives exactly

`6q0+3q1+2qR-3E=b-t>=0`

by the injective fiber inequality `t<=b`. This proves (4.1). Since the coefficients on the three pair counts sum to `11`,

`11 max(q0,q1,qR) >= 6q0+3q1+2qR >= 3E`,

which is (4.3).

Likewise, using (3.4),(3.5),(3.7),

`3q0+6q1+2qL`
`=3(a+c)+6(a+b)+2(2c+t)`
`=9a+6b+7c+2t`
`=3E+(c-t)>=3E`

because the second injective swap gives `t<=c`. This proves (4.2) and (4.4).

If (4.5) holds, then (4.3) forces `qR>=3E/11`, while (4.4) forces `qL>=3E/11`, proving (4.6). Finally, in the no-balanced/no-descent corridor all four displayed orientations are minority directions and hence are `<E/3`; combining with (4.3) or (4.4) yields (4.7). `square`

### Noninjective-fiber meaning

Equations (4.1)-(4.2) do more than give a threshold. The exact excess above the baseline `3E` is the non-surjectivity slack of the two swap injections:

- `b-t` is the count of target fibers not hit by the `P7 -> P2` exchange;
- `c-t` is the corresponding slack for the `P7 -> P6` exchange.

Hence a failure of bijectivity **helps** the actual-pair charge rather than creating an uncontrolled error term. This is the requested tracking of noninjective fibers.

## 5. Sharpness for the local fiber inequalities

The constant `3/11` is optimal if one uses only the five-label equalities and swap inequalities (1.1)-(1.2). Indeed the abstract ray

`(a,b,c,t)=(2s,s,s,s)`, `s>0`,                                (5.1)

satisfies

`t=b=c`, `b<=a`, `E=11s`,

and all four canonical counts are exactly

`q0=q1=qR=qL=3s=3E/11`.                                       (5.2)

This is an extremizer of the **fiber linear inequalities**, not a claim that every point on the ray is realized by a poset. It shows that improving `3/11` from the same local exchange constraints alone is impossible. Any further gain must use additional global poset structure, precisely as the lead r14 heavy-cover theorem suggests.

## 6. Application to the current collective route

The lead r14 bridge theorem already supplies a genuine cover-gap event of mass `>E/3` and at least two external witness channels. The present result says that if such two-channel recycling proceeds through two consecutive exact-two crossed cells, then the charge cannot diffuse arbitrarily:

- either one of the two central actual pair minorities is already at least `3/11`;
- or **both** outer canonical pair minorities are at least `3/11`.

Thus the exact-two part of the recycling problem is now a two-sided near-balance packet rather than a single greedy channel. This deliberately avoids the account02/B19 r12 obstruction: that report proves that following the largest exported fringe can cycle exactly, so this run never chooses a largest fringe and never asserts a well-founded greedy map.

For calibration, the two endpoint minorities in the B19 exact cycle are

`270/932=135/466` and `284/932=71/233`,

both already above `3/11`; the cycle therefore illustrates why a near-target **mass packet** should be globally amplified rather than recursively followed as a single selected pair. The present theorem is not asserted to apply to that cycle unless the consecutive-lower exact-two hypotheses (3.1) are verified; these numbers are used only as a regression/strategy check.

The account03/B19 explicit repeated-corridor witness is also consistent with the theorem. Its endpoint-minority sequence begins `265,213,248,195` with `E=833`; since `3E/11=2499/11≈227.18`, the first/third central cells already exceed the new threshold. No finite example is used in the proof.

## 7. First essential missing implication after this run

The remaining first implication is now more specific than the previous generic global charge:

> **TWO-CHANNEL `2/33` AMPLIFICATION.** In a hypothetical minimal no-balanced width-three poset, when the lead r14 heavy-cover flux recycles through a repeated exact-two corridor, use the three-chain cumulative-band/cover-flux structure to upgrade either one `[3/11,1/3)` canonical minority, or the simultaneous pair of such outer minorities from (4.6), across the remaining gap `2/33` to `1/3`; otherwise force strict span descent, a proper autonomous reduction, or a controlled multi-distinguisher/non-crossed exit carrying the target-scale charge.

A proof cannot use only the local five-label inequalities, because (5.1) is their exact linear extremizer. It must use the global heavy-cover/cumulative-band structure or additional width-three relations.

This is compatible with the lead r14 endpoint: its `>E/3` cover event is already target-scale, while the present theorem gives a concrete actual-pair realization floor when that charge enters repeated exact-two cells.

## 8. Status and integrity

- Latest lead r14 heavy-cover/two-channel result: **CONSUMED/APPLIED**.
- Assigned partner account02/B19 r12 greedy two-cycle: **CONSUMED/APPLIED as a mechanism guard; greedy iteration avoided**.
- account03/B19 five-label exact transfer/injections: **CONSUMED/APPLIED**.
- Two-sided exact identities (4.1)-(4.2): **PROVED**.
- Repeated exact-two actual-pair selector `>=3/11`: **PROVED**.
- If both central cells are `<3/11`, simultaneous two-sided outer charges `>=3/11`: **PROVED**.
- Local-fiber sharpness ray at `3/11`: **PROVED algebraically**; no realization claim.
- POS3: **OPEN / NOT PROVED**.
- Inherited finite frontier: `n_bal=14`, unchanged.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex calls, remote workflows, permission changes, or scheduler mutation were used.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort/provider counters: `UNKNOWN / NOT_EXPOSED`.
