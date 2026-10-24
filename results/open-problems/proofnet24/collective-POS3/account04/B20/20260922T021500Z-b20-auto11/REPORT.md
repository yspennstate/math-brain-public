# POS3 account04/B20 — endpoint conditional-swap residual compressed to three minority channels

**Run:** `20260922T021500Z-b20-auto11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run does not restart the superseded brain-installation or benchmark work.  The mathematical step below is an arbitrary-size reduction inside the exact source model; the finite program is regression evidence only.

## 1. Exact source-bound state consumed

I used only the following completed dependencies.

1. **Campaign lead account04/B10**, run `20260922T011127Z-account04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`.  In a hypothetical width-three counterexample, every element has a strong-majority-rank atom of probability `>1/81`; at a one-sided endpoint the same argument gives the stronger initial-block probability `>4/9`.

2. **Assigned OTHER-account partner account01/B19**, run `20260922T014910Z-b19-pos3-r11`, report blob `004a04191bf389e3493c3346fd57e67b35500049`.  Let `C=(c_1<...<c_m)` be the first maximal same-chain block in the transitive strong-majority order `L_*`, let `x=c_m`, and put `Q=P\C`.  The partner proves:
   - `C` is an order ideal;
   - the exact projected law on `L(Q)` is the ideal-chain insertion law;
   - `Pr(C is the initial m-element block)>4/9`;
   - the adjacent insertion-weight gradient is one-signed and rank one;
   - the scalar-only balance-transfer statement is false;
   - the remaining ideal-block weighted balance transfer (IBWT) must use the original chain-touching `>2/3` constraints rather than only the mean insertion weight.

   Its late delta additionally combines the endpoint cap below with the initial-block decomposition and shows that, at the first majority-block boundary, the minority reversal `y<x` occupies more than `2/5` of the non-prefix component.

3. **account02/B10**, run `20260922T014627Z-account02-B10-pos3-r12`, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`.  At the first strong-majority block boundary `x \prec_* y`, the two canonical successor blockers are `M={s_1,s_2}` and
   `2/3 < p_xy:=Pr(x<y)<7/9`.
   If `E=e(P)`, `Q_0=#{L:y<s_1,y<s_2}`, `U_i` is the exact right-fringe capacity in blocker channel `s_i`, `Phi_i` the positive deletion-fiber defect in that channel, and `Psi` the total negative defect, then
   `U_1+U_2=E-Q_0`,
   `D:=e_xy-e_yx=Phi_1+Phi_2-Psi`,
   with `0<=Phi_i<=U_i` and `Psi>=0`.  The same report proves the blocker-product estimate
   `p_xy <= 1-(1/2)p_ys1 p_ys2`.

4. **account03/B11**, run `20260922T011439Z-account03-B11-pos3-r12`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`.  At the first boundary the blockers satisfy
   `x lessdot s_1`, `x lessdot s_2`, and `y,s_1,s_2` are pairwise incomparable, and any distinguisher of `s_1,s_2` occurs only after the whole second majority block.  Its seven-element 79-extension witness is used below only as a regression case.

The new step below directly attacks the partner's first unpaid endpoint transfer.  It cancels the part of the large non-prefix reversal mass that is paired by a critical swap and proves that the **net** residual can come from at most three canonical minority channels, independent of the length of the deleted first block.

## 2. First-boundary setup

Assume, for contradiction, that `P` is a cardinality-minimal width-at-most-three counterexample, and let
`B_1=C=(c_1<...<c_m)`, `x=c_m`,
be the first maximal same-chain block of `L_*`.  Let `y` be the first element of the second block.  Thus `x||y` and `x prec_* y`.

The endpoint state recalled above gives exactly two canonical successor blockers
`M={s_1,s_2}=min{z:x<z, z||y}`.
At this first boundary the already-proved predecessor inclusion is
`Pred(y) subseteq Pred(x)`. `(2.1)`

Define the blocker-conditioned event
`A={L:y<s_1 and y<s_2}` and `q=|A|`.
Also let `b=#{L:y<x}`.
Since `x<s_i`, every extension with `y<x` automatically lies in `A`; hence `b` is also the number of `y<x` extensions inside the conditioned family.

Adjoin the two relations `y<s_1,y<s_2` and call the resulting poset `P^+`.  Then
`L(P^+)=A`. `(2.2)`
The point of the augmentation is that it kills every canonical successor obstruction from `x` to `y`.

## 3. Blocker conditioning turns `(x,y)` into a one-sided critical pair

### Lemma 3.1 — successor inclusion after blocker conditioning

In `P^+`,
`Succ_{P^+}(x) subseteq Succ_{P^+}(y)`. `(3.1)`

### Proof

Take any `z>x`.

If `z` is comparable with `y` in the original poset, `z<y` is impossible because `x<z<y` would force `x<y`; therefore `y<z`.

If `z||y`, then `z` lies in `S_x(y)={u:x<u, u||y}`.  Since the poset is finite, some minimal member `s_i` of `S_x(y)` satisfies `s_i<=z`.  In `P^+` we added `y<s_i`, hence `y<s_i<=z`.

Thus every successor of `x` is a successor of `y` after augmentation. `□`

The added relations do not change the predecessor set of `y`, so (2.1) remains true in `P^+`.

### Lemma 3.2 — critical swap injection

For every extension `L` of `P^+` with `x<y`, exchange the positions of `x` and `y`.  The result is again a linear extension of `P^+`, now with `y<x`.  This defines an injection
`σ:L(P^+;x<y) -> L(P^+;y<x)`. `(3.2)`

### Proof

When `y` moves left to the old position of `x`, every predecessor of `y` is already before that position because `Pred(y) subseteq Pred(x)`.  When `x` moves right to the old position of `y`, every successor of `x` is still after that position because of (3.1).  All other pair relations are untouched.  Swapping back recovers the original extension, so the map is injective. `□`

Consequently
`q-b<=b`, hence `q<=2b`. `(3.3)`
This is the critical-pair interpretation of the endpoint mass-transport inequality.

## 4. Exact image characterization

The key new point is not only that the swap is injective, but that its **unmatched** `y<x` extensions admit a source-exact finite-channel description.

Let
`D=Pred_{P^+}(x)\Pred_{P^+}(y)` and
`T_full=Succ_{P^+}(y)\Succ_{P^+}(x)`.

### Lemma 4.1 — exact unmatched-swap criterion

Take `L in L(P^+)` with `y<x`.  Swapping `x,y` back produces a valid extension with `x<y` **iff**

- no element of `D` lies strictly between `y` and `x` in `L`, and
- no element of `T_full` lies strictly between `y` and `x` in `L`.

Therefore the unmatched set has cardinality
`R:=b-(q-b)=2b-q`. `(4.1)`

### Proof

Moving `x` left to the old position of `y` can only violate a relation `d<x` when a predecessor `d` of `x` occurs after `y`; predecessors common to `y` already occur before `y`, so the only possible left obstructions are `D`.

Moving `y` right to the old position of `x` can only violate a relation `y<u` when such a successor occurs before `x`; successors common to `x` already occur after `x`, so the only possible right obstructions are `T_full`.

These conditions are also sufficient.  The count is then the target size `b` minus the image size `q-b`. `□`

This identity isolates the **net conditional asymmetry**.  The large raw minority mass `b` need not all be charged: `q-b` of it is paired exactly with conditioned majority extensions.  Only `R=2b-q` survives.

## 5. First-block geometry compresses the residual to at most three channels

Let
`lambda=max({j:c_j<y} union {0})`.
Because `L_*` extends `P` and `C` occupies the first `m` positions, every predecessor of `x` or `y` belongs to `C`.  Hence
`Pred(x)={c_1,...,c_{m-1}}` and
`Pred(y)={c_1,...,c_lambda}`. `(5.1)`
Thus
`D={c_{lambda+1},...,c_{m-1}}`. `(5.2)`

If `D` is nonempty, the existence of **any** left obstruction between `y` and `x` is equivalent, by the chain order, to the single event
`y<c_{m-1}<x`. `(L)`

Now define in the original poset
`T=min{t:y<t, t||x}`. `(5.3)`
The successor difference `T_full` in `P^+` is exactly the upward closure of these `y`-successors that remain incomparable with `x`.  Therefore an element of `T_full` lies between `y` and `x` iff some minimal member `t in T` lies between them.

Moreover `T` is an antichain and every `t in T` is incomparable with `x`.  Hence `{x} union T` is an antichain.  Width at most three gives
`|T|<=2`. `(5.4)`
By the general Hasse-cover compression already proved in the collective state, every `t in T` is in fact a cover of `y`.

### Theorem 5.1 — three-channel endpoint residual

At the first strong-majority block boundary of a hypothetical POS3 counterexample, the unmatched conditioned critical-swap set is exactly

- the left event `{L in A:y<c_{m-1}<x}` if `lambda<=m-2` (and empty if `lambda=m-1`), union
- `union_{t in T}{L in A:y<t<x}`,

where `|T|<=2`.  In particular the unbounded collection of possible first-interruption levels of the ideal chain contributes only **one** left-fringe obstruction event, and the entire right side contributes at most **two** Hasse-local obstruction events.

Its exact size is
`|Rset|=R=2b-q`. `(5.6)`

### Counterexample-direction interpretation

Every channel above is a minority-pair event in the original counterexample.

- If the left channel exists, `c_{m-1} prec_* y` and `c_{m-1}||y`, so `Pr(y<c_{m-1})<1/3`.
- For `t in T`, the strong-majority order has `x prec_* y<t`, while `x||t`; hence `Pr(t<x)<1/3`.

Thus the residual net bias after exact critical cancellation is supported by at most three already-oriented minority channels.  The number of channels does **not** grow with `m`.

## 6. Exact identification with the endpoint deletion-fiber slack

The account02/B10 endpoint transport has
`U_1+U_2=E-q` and
`D_fib:=Phi_1+Phi_2-Psi=e_xy-e_yx=E-2b`.
Subtracting gives the exact identity

`R=2b-q=(U_1-Phi_1)+(U_2-Phi_2)+Psi`. `(6.1)`

Every term on the right is nonnegative.

So the same quantity has two independent descriptions:

1. **deletion-fiber description:** unused right-fringe capacity in the two active endpoint Hasse channels plus all negative deletion-fiber defect;
2. **critical-swap description:** the union of one chain-fringe obstruction and at most two minimal `y`-successor / `x`-incomparability obstructions.

This is the new bridge between the partner's ideal-block insertion recurrence and the other-account endpoint Hasse transport.  It says that future work does **not** need to charge the full `>2/5` raw non-prefix reversal mass from the late partner delta.  The portion paired by (3.2) cancels exactly.  Only the residual (6.1) must be propagated across boundaries.

## 7. Quantitative endpoint corollaries

Let `a_i=Pr(y<s_i)`, `p=Pr(x<y)`, and `q_0=q/E`.
The endpoint XYZ inequality gives
`q_0>=a_1 a_2>4/9`.
Since `p>2/3`, `b/E=1-p<1/3`; (3.3) therefore gives
`4/9<q_0<2/3`. `(7.1)`

Conditioning on both blockers,
`Pr(y<x | y<s_1,y<s_2)=b/q`.
By `q<=2b`, `b/E<1/3`, and `q/E>4/9`,

`1/2 <= Pr(y<x | y<s_1,y<s_2) < 3/4`. `(7.2)`

Thus the event that `y` precedes both canonical successor blockers reverses the unconditional strong-majority direction enough to make `y<x` at least as likely as `x<y`.

Also `a_1 a_2<=q_0<2/3`; hence at least one of the two canonical blocker probabilities obeys
`2/3<a_i<sqrt(2/3)`. `(7.3)`
This does not itself create a balanced pair, but it gives a quantitative endpoint channel bounded away from probability one.

## 8. Regression verification

`verify_endpoint_critical_swap_residual.py` checks the exact swap/image statement on three width-at-most-three examples.

1. **Source-bound account03/B11 79-extension witness.** `E=79`, `q=50`, `b=25`, hence `R=0`.  The conditioned critical swap is a bijection: 25 conditioned `x<y` extensions pair with 25 conditioned `y<x` extensions.  There is no left or right residual obstruction.  This explains why the earlier endpoint inequality is tight on that witness.

2. **Left-fringe synthetic regression.** On the five-element poset generated by `c<x`, `x<s_1`, `x<s_2`, one gets `E=10`, `q=6`, `b=4`, `R=2`.  The two unmatched conditioned extensions are exactly the two extensions containing `y<c<x`.

3. **Right-obstruction synthetic regression.** On the five-element poset generated by `x<s_1`, `x<s_2`, `y<t`, one gets `E=20`, `q=14`, `b=8`, `R=2`.  The two unmatched conditioned extensions are exactly the two extensions containing `y<t<x`.

The program independently checks width, transitive closure, the blocker-conditioned extension family, swap validity/injectivity, the exact unmatched count `R=2b-q`, and equality with the stated obstruction union.  It ends with
`POS3_ENDPOINT_CRITICAL_SWAP_RESIDUAL_PASS`.

Verifier SHA-256: `e8465c0dd13c8308750d3ab8805280463f9c9b4952e6c8f8711b21a5be2a55ea`.
Captured stdout SHA-256: `c655f665f9061e033eb07e97abd6ec51db75903423dd82fe0187be7fb1fafa4c`.

The synthetic cases test the theorem, not the POS3 conjecture.  The arbitrary-size result is established by the proofs above.

## 9. What moved and the first remaining implication

**Moved in this run.**

- The endpoint blocker conditioning is identified as a one-sided critical-pair augmentation.
- The raw non-prefix reversal from the partner result is split into an exactly paired part and a net residual.
- The net residual has the exact count `R=2b-q`.
- The same `R` is exactly the deletion-fiber slack `(U_1-Phi_1)+(U_2-Phi_2)+Psi`.
- The ideal-chain first-interruption side of `R` collapses to one chain-fringe event, while width three collapses the other side to at most two Hasse-local events.
- The blocker-conditioned reversal probability is trapped in `[1/2,3/4)`, and one endpoint blocker probability lies below `sqrt(2/3)`.

**Still unpaid.** POS3 is not proved.  The next universal step is now narrower than “charge all non-prefix reversals”:

> propagate the at-most-three residual obstruction channels above to the next strong-majority boundary / delayed-distinguisher structure, and show that the exact slack identity (6.1) cannot persist across all majority blocks without forcing either a balanced pair, four mutually incomparable elements, or a proper autonomous nonchain.

The latest account03/B19 weighted rank-gap compression result is compatible with this target: it guarantees a strong compressed boundary survives exact chain deletion, but its 349-extension example shows that the final charge must be allowed to land on deleted-chain pair events.  The left channel above is already such a deleted-chain event; the two right channels are the finite set that must be handed to the next boundary.

No novelty or priority claim is made.  No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, or permission change was used.
