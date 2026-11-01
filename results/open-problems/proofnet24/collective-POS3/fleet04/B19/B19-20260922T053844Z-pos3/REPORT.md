# POS3 fleet04/B19 — a heavy bridge cover must export off the bridge

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no brain-installation or benchmark work. All probabilities below are under the original uniform law on all full linear extensions. No projected deletion law is renamed uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead version read before the derivation is:

- **fleet04/B10 r14**, `proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, blob `50bac494667235f3630991a512438eac42c30521`.

Its bridged-blocker theorem gives, in the surviving majority-late branch, a saturated chain

`c=z_0 lessdot z_1 lessdot ... lessdot z_k=u`

with every `z_i || a`, and a unique adjacent pair `x=z_j lessdot y=z_{j+1}` satisfying

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,

hence the literal cover-gap event

`H_j={x<a<y}` has `Pr(H_j)>1/3`.

The lead then applies fleet01/B19's cover theorem to force at least two relation distinguishers beyond the cover endpoints, but its first remaining recycling case allows those witnesses to be absorbed by the bridge itself when the bridge is long.

The required named **OTHER-account partner** result consumed and applied is:

- **fleet01/B10 r11**, `proofnet24/collective-POS3/fleet01/B10/20260922T045216Z-fleet01-B10-pos3-r11/REPORT.md`, blob `7ab3502e574d795c8300fd0ec70dc33f12b87f0a`.

It proves exact same-anchor TP2 for canonical reverse channels and obtains the local thresholds `(3-sqrt(7))/2`, `(5-sqrt(21))/2`, and `2-sqrt(3)` in the corresponding channel-count cases. Crucially, it leaves different-anchor cross-group transport unpaid rather than assuming an FKG statement.

That caution is source-valid and necessary: fleet04/B20,

- `proofnet24/collective-POS3/fleet04/B20/20260922T051509Z-b20-auto11-pos3/REPORT.md`, blob `7f869810aea2161196b91c2b9c7625b84ed17247`,

constructs an exact width-three example where a lower canonical reverse channel and an upper canonical reverse channel have negative covariance. I therefore do **not** try to extend the partner's TP2 across anchors. The argument below changes mechanism to an exact three-gap swap at the lead's heavy cover.

Two additional compatible inputs fix the global meaning of the result:

- fleet01/B19, `proofnet24/collective-POS3/fleet01/B19/20260922T044807Z-pos3-r11-b19/REPORT.md`, blob `003d2bf0593cb55f11738f50d68509413bb8d234`, proves the exact `F*G` cover-flux identity and that a strong cover flip in a no-balanced poset has at least two external relation witnesses;
- fleet03/B19, `proofnet24/collective-POS3/fleet03/B19/20260922T045925Z-b19-pos3-r12/REPORT.md`, blob `56d9b17c5e501fcf67881c9e91ffd92b6b68bdcd`, proves that two consecutive exact-two crossed states carry a conserved latent count `K` with `E/3<K<2E/3`;
- fleet01/B11, `proofnet24/collective-POS3/fleet01/B11/20260922T051731Z-b11-pos3-r11/REPORT.md`, blob `bba2357120a72c7e2d473dd23095240f61e2f266`, realizes part of that repeated-corridor charge by showing an actual canonical pair minority at least `3E/11`.

## 2. Compact conditional end-to-end route

Assume a cardinality-minimal width-at-most-three counterexample and use the inherited transitive strong-majority order.

The current route is:

1. local same-anchor canonical channels are controlled by fleet01/B10 TP2, while static cross-anchor positive association is forbidden by the fleet04/B20 counterexample;
2. the lead r14 bridged branch produces an **actual** cover-gap event of mass `>E/3`;
3. fleet01/B19 forces at least two relation witnesses at that cover;
4. **new here:** the bridge itself can never absorb all of those witnesses: every such heavy cover has at least one relation witness outside the whole saturated bridge;
5. repeated exact-two recycling then carries the fleet03/B19 latent balanced-sized mass and the fleet01/B11 `3/11` actual-pair packet to a genuinely off-corridor structural exit.

Step 4 is proved below. Step 5 still needs a quantitative realization/charge theorem at the off-corridor exit; I do not promote existence of an off-bridge witness into a target-level balance claim.

## 3. Three-gap symmetry lemma

For vertices `r,s`, write `rel(w,r)` for one of `w<r`, `w||r`, `r<w`.

### Lemma 3.1 — no off-chain distinguisher implies a `1/3` gap cap

Let

`Z: z_0<z_1<...<z_k`

be a chain in a finite poset, and let `a` be incomparable with every `z_i`. Fix `0<=j<k`, put

`x=z_j`, `y=z_{j+1}`,

and suppose that every vertex `w` outside `Z union {a}` has the **same** relation to the three vertices `x,a,y`:

`rel(w,x)=rel(w,a)=rel(w,y)`.                                  (3.1)

Then

`Pr(x<a<y) <= 1/3`.                                            (3.2)

This statement is for the original uniform law on all linear extensions and has no width hypothesis.

### Proof

For `-1<=i<=k`, let `H_i` be the event that `a` occupies the `i`-th gap of the chain `Z`:

- `H_{-1}: a<z_0`;
- `H_i: z_i<a<z_{i+1}` for `0<=i<k`;
- `H_k: z_k<a`.

Because `a` is incomparable with every chain vertex, these events partition all linear extensions.

The middle event is

`H_j={x<a<y}`.

There is a bijection

`H_j <-> H_{j-1}`                                               (3.3)

obtained by exchanging the positions of `a` and `x` in the linear extension. To check validity, first consider vertices on `Z`. All chain vertices below `x` remain before `x` after the exchange, because the old position of `a` is still between `x` and `y`; all chain vertices above `x` remain after it. The element `a` has no required comparison with any chain vertex. For a vertex `w` outside `Z union {a}`, condition (3.1) says that `w` has exactly the same relation to `a` as to `x`; therefore moving `a` and `x` across the same intervening vertices cannot violate a required comparison. The same exchange is its own inverse. This also covers `j=0`, where `H_{j-1}=H_{-1}`.

Likewise exchanging the positions of `a` and `y` gives a bijection

`H_j <-> H_{j+1}`.                                              (3.4)

The three events `H_{j-1},H_j,H_{j+1}` are disjoint, so (3.3)-(3.4) give

`1 >= Pr(H_{j-1})+Pr(H_j)+Pr(H_{j+1}) = 3 Pr(H_j)`.

Hence `Pr(H_j)<=1/3`. `square`

The point is not a correlation inequality. It is an exact pair of full-extension bijections. It remains valid with arbitrary additional vertices and arbitrary multiplicities because no deletion or conditioning changes the law.

## 4. Heavy bridge covers must have an off-bridge witness

### Theorem 4.1 — bridge self-recycling exclusion

In the fleet04/B10 r14 bridge configuration, let

`c=z_0 lessdot ... lessdot z_k=u`

be any saturated bridge chain supplied by the lead and let

`x=z_j lessdot y=z_{j+1}`

be its unique heavy transition, so

`Pr(x<a<y)>1/3`.                                                (4.1)

Then there exists a vertex

`w notin {a,z_0,...,z_k}`                                      (4.2)

such that

`rel(w,x) != rel(w,a)` or `rel(w,y) != rel(w,a)`.              (4.3)

Equivalently, at least one relation distinguisher for one of the two cover endpoint pairs `(x,a)` and `(y,a)` lies **outside the entire bridge**.

### Proof

The lead r14 bridge theorem already proves `z_i||a` for every `i`. If no vertex `w` satisfying (4.2)-(4.3) existed, then every vertex outside `Z union {a}` would obey (3.1). Lemma 3.1 would therefore imply

`Pr(x<a<y)<=1/3`,

contradicting the exact lead flux (4.1). `square`

### Corollary 4.2 — exact-two witness recycling cannot be bridge-closed

Fleet01/B19 forces at least two distinct relation witnesses at every strong cover flip. Theorem 4.1 shows that, at a lead bridge transition, those witnesses cannot all be supplied by other vertices of the bridge.

Thus:

- if the cover has exactly two external witnesses, **at least one is off the bridge**;
- more generally, no matter how long the neutral bridge is, it cannot by itself satisfy the entire asymmetry budget of the heavy transition.

This strictly strengthens the length-only conclusion in lead r14 Corollary 5.1. There the existence of an off-bridge witness followed immediately only for bridges with one or two covers. The three-gap swap above removes the length restriction.

## 5. Consequence for the repeated exact-two / latent-K branch

The fleet03/B19 recurrence and fleet01/B11 `3/11` theorem show that repeated exact-two crossed states already transport substantial actual or latent mass. Before this run, a maximal bridge exit could still have been combinatorially self-contained: the cover two-witness theorem allowed all required witnesses to be other vertices on a sufficiently long neutral bridge.

Theorem 4.1 eliminates precisely that case. Therefore a maximal repeated exact-two corridor that reaches a lead r14 bridge must encounter a **genuine off-corridor relation defect** at the heavy cover. The corridor cannot close by merely recycling its two witnesses along the same neutral chain.

This is an arbitrary-size induction step: it applies to every bridge length and does not rely on the finite `n_bal=14` frontier.

It does **not** yet prove that the off-bridge witness receives `K` units of charge, nor that its associated incomparable pair is balanced. The remaining first implication is now:

> **OFF-BRIDGE CHARGE REALIZATION.** At the heavy bridge cover, use the exact `F*G` flux and the off-bridge witness forced by Theorem 4.1 to show that either (i) an actual incomparable pair absorbs enough of the `>E/3` gap / repeated-corridor `K` packet to enter `[E/3,2E/3]`, or (ii) the off-bridge relation defect forces strict strong-majority span descent, a proper autonomous reduction, or the already isolated multi-distinguisher/non-crossed exit with an exact conserved charge.

The fleet04/B20 nine-element example remains a guard: this next step cannot be replaced by a static positive-covariance claim between lower and upper channels.

## 6. Status and integrity

- fleet01/B10 same-anchor TP2 amplification: **CONSUMED/APPLIED** to the surviving local-channel architecture; no unsupported cross-anchor extension is made.
- fleet04/B20 static cross-group positive-association shortcut: **PRESERVED AS REFUTED**.
- lead r14 target-scale heavy bridge cover: **CONSUMED/APPLIED**.
- three-gap symmetry lemma: **PROVED**.
- bridge self-recycling exclusion / existence of an off-bridge witness: **PROVED**.
- latent-`K` or `3/11` packet realization at that off-bridge witness: **OPEN**.
- parent POS3 theorem: **OPEN / NOT PROVED**.
- outcome: `ESSENTIAL_STEP_APPLIED`.

No code or numerical search is used as proof in this run; the new step is symbolic. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex calls, remote workflows, permission changes, public posting, or native brain activation is used or claimed.
