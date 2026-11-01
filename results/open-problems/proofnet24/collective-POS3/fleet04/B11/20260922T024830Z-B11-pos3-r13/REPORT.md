# POS3 fleet04/B11 — bounded-range localization of the exact chain-deletion obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run stays in the owner-selected POS3 scope and attacks the exceptional bounded-range/high-comparability branch left by the actual bounded-width theorem. It does not assume a finite-kernel reduction. The preceding B11 run already refuted that shortcut, even at `pi(P)=7`; the new step below instead proves that bounded incomparability range gives two exact **localization** statements that are strong enough to be used inside the current partner recurrence without claiming that the whole poset has bounded size.

## 1. Exact state consumed

I used only the following essential completed state.

1. **Campaign lead fleet04/B10**, `proofnet24/collective-POS3/fleet04/B10/20260922T011127Z-fleet04-B10-POS3-r11/REPORT.md`, blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. In a hypothetical width-three counterexample, the transitive strong-majority order `L_*` pins every element to its `L_*` rank with probability `>1/81`; at a one-sided endpoint the analogous initial-rank atom is `>4/9`. The lead explicitly leaves the global consecutive-boundary / signed-flux compatibility step open.

2. **Assigned partner fleet01/B19, latest complete version actually present**, `proofnet24/collective-POS3/fleet01/B19/20260922T021702Z-pos3-b19-r11/REPORT.md`. For the first maximal strong-majority chain block `C={c_1<...<c_m}` and `Q=P\C`, it proves the exact first-interruption renewal decomposition

   `e(P)=e(Q)+sum_{q in M} sum_{j=lambda(q)}^{m-1} e(R_{q,j})`,

   with `|M|<=2`, where `M` is the set of minimal `Q`-elements that can interrupt `C`, `lambda(q)=max{j:c_j<q}`, and `R_{q,j}=P\{c_1,...,c_j,q}`. The corresponding probability law is an exact convex combination of **uniform** laws on `Q` and these smaller residual posets. This is the named OTHER-account result applied below.

3. **Partner fleet01/B19 chain-profile recurrence**, run `20260922T004631Z-b19-pos3-r11`, blob `c2f771152d5be6943cce6872c500ca81c572e962`. For an arbitrary deleted chain `C`, every `q` has an integer profile interval `I(q)=[lambda(q),rho(q)]`; adjacent swaps reduce exactly to two interval order counts. Endpoint-ordered profiles have context-independent sign, and only **nested** profiles can have context-sensitive sign.

4. **Previous fleet04/B11**, `proofnet24/collective-POS3/fleet04/B11/B11-20260922T011236Z-pos3-r12/REPORT.md`, blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`. Combining Peczarski's solved 6-thin case with Aires--Kahn's bounded-width range theorem puts every hypothetical width-three counterexample in

   `7 <= pi(P) <= K_3`

   for some finite source-qualitative constant `K_3`, while an explicit arbitrary-size width-three prime family at `pi=7` refutes the finite-kernel shortcut from bounded range/variance/local insertion multiplicity.

5. **Same-slot immediately preceding run**, `proofnet24/collective-POS3/fleet04/B11/20260922T021940Z-B11-pos3-r13/REPORT.md`, blob `5075f5ae42742da375b0688cef37dbc8e8c65484`. It refutes the stronger statement that an arbitrary balanced pair of `Q` must survive the ideal-block weighting; the remaining transfer must select a pair adaptively. The present report does not repeat that counterexample.

The external source behind the exceptional branch is Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134 (2025): for fixed width, `pi(P)->infinity` forces the balance parameter to `1/2`. Peczarski's 2008 6-thin theorem supplies the lower edge `pi>=7` for any counterexample. No numerical value of `K_3` is assumed.

## 2. Conditional end-to-end route and the first missing implication

Assume POS3 is false and choose a cardinality-minimal counterexample `P`. Let

`K=pi(P)=max_x |{y:y||x}|`.

The inherited state gives `7<=K<=K_3`, a transitive strong-majority linear extension `L_*`, and at least five maximal contiguous chain blocks in `L_*`.

The partner's newest renewal route deletes the first block `C` and replaces the biased projected law by a convex combination of genuine uniform laws on smaller residual posets. A valid induction would close if one can select a balanced pair compatibly across those components or force a balanced pair meeting `C`.

The first structural issue is therefore not whether the whole exceptional branch has bounded size—it does not—but whether bounded range at least prevents the deletion recurrence itself from having unbounded local complexity. The answer is **yes** in two precise senses:

1. every strong-majority chain block has bounded length (`K` at the two ends, `2K` internally);
2. the newest first-interruption renewal law has at most `1+2K` uniform components, and every context-sensitive nested chain-profile swap has exact local distortion at most `K+1`.

These are finite-**local-state** statements, not a finite-kernel theorem.

## 3. Bounded range forces short strong-majority chain blocks

Write the maximal contiguous chain blocks of `L_*` as

`B_1, B_2, ..., B_h`,

and inside a block write

`B=(b_1<...<b_r)`

in the poset order, which is the same as its `L_*` order.

### Lemma 3.1 — outside incomparability with one block is a one-sided interval

If `z` occurs before `B` in `L_*`, then the elements of `B` incomparable with `z` form an initial segment of `B`, of size at most `K`.

If `z` occurs after `B`, then the elements of `B` incomparable with `z` form a final segment of `B`, again of size at most `K`.

### Proof

Suppose first that `z` is before `B`. Since `L_*` is a linear extension, `b_i<z` is impossible. If `z<b_j` for some `j`, then transitivity gives `z<b_k` for every `k>=j`. Therefore all indices before the first comparable-above position are incomparable, and all later ones are above `z`: the incomparable set is an initial segment. Its size is at most the total number of elements incomparable with `z`, hence at most `K`.

The later-`z` case is dual. Now `z<b_i` is impossible; if `b_j<z`, then every `b_i` with `i<=j` is also below `z`, so the incomparable set is a final segment, again of size at most `K`. `□`

### Theorem 3.2 — block-length localization

In a cardinality-minimal POS3 counterexample with `pi(P)=K`,

`|B_1| <= K`, `|B_h| <= K`,

and for every internal block

`|B_i| <= 2K`.

### Proof

Take an internal block `B=(b_1<...<b_r)`. If `r>=2K+1`, consider `b_{K+1}`.

For every element `z` before `B`, Lemma 3.1 says that at most the first `K` members of `B` can be incomparable with `z`; hence

`z < b_{K+1}`.

For every element `z` after `B`, at most the final `K` members can be incomparable with `z`. Since

`K+1 <= r-K`,

we have

`b_{K+1} < z`.

Thus `b_{K+1}` is comparable with every element of `P`: all earlier outside elements are below it, all later outside elements are above it, and all elements of `B` are comparable with it.

Deleting `b_{K+1}` changes no ordering probability among the remaining elements. Indeed, if `D` is the set before the block position and `U` the set after it, then every `d in D` satisfies `d<b_{K+1}<u` for every `u in U`, so every linear extension of `P-b_{K+1}` has a unique lift obtained by inserting `b_{K+1}` between `D` and `U`.

The inherited strong-majority decomposition has at least five maximal chain blocks, so deleting this one element leaves a nonchain. Cardinality minimality would then give a balanced pair in the smaller poset, and the unique-lift bijection transfers that pair back to `P`, contradiction. Hence `r<=2K`.

For the first block `B_1=(b_1<...<b_r)`, if `r>=K+1`, Lemma 3.1 applied to every later outside element forces `b_1<z` for every such `z`: if `b_1||z`, the final incomparable segment would have to contain all `r>K` elements of `B_1`. Thus `b_1` is a global minimum and its deletion is again a unique-lift reduction to a smaller nonchain, contradiction. Hence `|B_1|<=K`. The final block is dual. `□`

This is genuinely no-balanced/minimal-counterexample structure. It does **not** contradict the previous arbitrary-size `pi=7` family: such bounded-degree prime families can have arbitrarily many short blocks.

## 4. Applying the latest partner renewal law: at most `1+2K` uniform components

Now take the first block

`C=B_1={c_1<...<c_m}`,

put `Q=P\C`, and use the exact notation from fleet01/B19. The partner proves `C` is an ideal, `Q` is a smaller nonchain, and

`M={q in Min(Q):lambda(q)<m}`

has size at most two.

Theorem 3.2 gives immediately

`m<=K`.                                                        (4.1)

There is also a sharper interpretation of every channel length.

### Lemma 4.1 — interruption depth is exactly a cross-chain incomparability count

For `q in M`,

`m-lambda(q) = |C cap Inc(q)| <= K`.                            (4.2)

### Proof

Because `C` is an ideal, no element of `Q` can be below any `c_i`. By definition of `lambda(q)`, every `c_i` with `i<=lambda(q)` is below `q`. For `i>lambda(q)`, the relation `c_i<q` is excluded by maximality of `lambda(q)`, while `q<c_i` is excluded because `C` is an ideal. Hence exactly the suffix

`c_{lambda(q)+1},...,c_m`

is incomparable with `q`. Its size is `m-lambda(q)` and is at most `pi(q)<=K`. `□`

The partner renewal law contains one prefix component of weight `alpha=e(Q)/e(P)` and, for each `q in M`, one residual component for every

`j=lambda(q),...,m-1`.

Therefore the exact number of nonzero component **indices** is

`1 + sum_{q in M} (m-lambda(q))`

and Lemma 4.1 plus `|M|<=2` gives the uniform bound

`number of renewal components <= 1+2K`.                         (4.3)

In the single-interrupter case it is at most `1+K`.

This is the first valid compactness statement in the bounded-range branch after the finite-kernel shortcut was refuted: the **whole poset may be arbitrarily large**, but the exact first-block induction law is a convex combination of only finitely many uniform residual laws, with the count depending only on the bounded-range parameter.

No component is replaced by an unsupported law: they are exactly the source-valid `Q` and `R_{q,j}` laws proved by the partner.

## 5. Bounded range also caps the old nested-profile obstruction

The previous fleet01/B19 chain-deletion theorem remains useful for arbitrary deleted chains, so it is worth recording what `pi(P)<=K` buys there.

Let `C={c_1<...<c_m}` be any chain and let

`I(q)=[lambda(q),rho(q)]`

be the partner's feasible chain-prefix interval for `q notin C`.

### Lemma 5.1 — profile diameter

The elements of `C` incomparable with `q` are exactly

`c_{lambda(q)+1},...,c_{rho(q)}`,

so

`rho(q)-lambda(q) <= K`.                                       (5.1)

### Proof

All `c_i` with `i<=lambda(q)` are below `q`, and all `c_i` with `i>=rho(q)+1` are above `q`. If `lambda(q)<i<=rho(q)`, then `c_i<q` would contradict maximality of `lambda(q)`, while `q<c_i` would contradict minimality of `rho(q)+1`. Thus precisely the middle interval is incomparable with `q`. `□`

Two consequences follow immediately.

1. A strictly nested chain of distinct profile intervals has length at most `K+1`, because every proper inclusion of integer intervals increases the diameter by at least one while every diameter is at most `K`.
2. More sharply, a context-sensitive adjacent swap has bounded exact local distortion.

### Theorem 5.2 — nested local distortion is at most `K+1`

Consider one of the partner's conditioned adjacent-swap comparisons, and suppose after the common outer-window truncation the profiles are nested integer intervals

`B subseteq A`.

Write

`s=|B|>=1`,

`ell=number of points of A below B`,

`r=number of points of A above B`.

Then

`N_AB = s(s+1)/2 + s ell`,

`N_BA = s(s+1)/2 + s r`.                                       (5.2)

Since `ell+r=|A|-|B|<=K`,

`1/(K+1) <= N_AB/N_BA <= K+1`.                                (5.3)

Consequently, for the **global exact lift weights** of a nested-profile adjacent swap,

`1/(K+1) <= W_C(...,u,v,...)/W_C(...,v,u,...) <= K+1`.         (5.4)

### Proof

Because `B` is a consecutive subinterval of `A`, every point in the lower fringe of `A` is at most every point of `B`, every point in the upper fringe is at least every point of `B`, and the pairs internal to `B` contribute `s(s+1)/2` to each weak order count. This gives (5.2).

Divide by `s`. Each normalized count is `(s+1)/2` plus one nonnegative fringe length. The larger fringe is at most `K`; the smaller denominator is at least `(s+1)/2>=1`. Hence the ratio in either direction is at most

`1 + 2K/(s+1) <= K+1`,

proving (5.3).

In the partner prefix/suffix decomposition, the same nonnegative outer-context weight multiplies `N_AB` and `N_BA`. Contexts with empty `B` contribute zero to both; every nonempty context satisfies (5.3). Summing preserves the pointwise ratio bounds and proves (5.4). `□`

The factor `K+1` is the correct scale: a singleton `B` at one endpoint of an `A` of size `K+1` attains the local ratio `K+1`. Thus bounded range rescues a **K-dependent** distortion bound, but not a universal factor-two bound. This is fully consistent with the partner's earlier width-two family whose distortion grows with the deleted-chain range.

## 6. What is paid and what remains unpaid

The bounded-range exceptional case is **not finished**. What is now paid is the exact local-complexity step that a valid continuation may use:

- the first and last strong-majority chain blocks have at most `K` elements;
- every internal strong-majority chain block has at most `2K` elements;
- the latest first-interruption renewal law has at most `1+2K` genuine uniform components;
- strict nested-profile depth is at most `K+1`;
- each context-sensitive nested adjacent-swap lift ratio is between `1/(K+1)` and `K+1`.

None of these implies `|P|=O_K(1)`: the number of strong-majority blocks may still be unbounded. Therefore this report does not resurrect the refuted finite-kernel shortcut.

The **first essential missing implication** is now finite-channel rather than arbitrary-density:

> In the exact first-block renewal mixture with at most two interrupters and at most `1+2K_3` uniform residual components, use the no-balanced cross-block inequalities and the common strong-majority alignment to prove that some balanced pair supplied by one of the smaller uniform residual posets survives in the mixture, or else force a chain-touching pair into `[1/3,2/3]`.

The same-slot five-element regression shows that this selection must be adaptive: an arbitrary balanced pair need not survive. What bounded range contributes is that only finitely many source-valid interruption channels need to be reconciled at each endpoint, not that one may select an arbitrary pair or enumerate finitely many whole posets.

## 7. Computation and failure record

No computation was used in the proof of Theorems 3.2, 4.1, or 5.2. The argument is symbolic and depends only on the exact source-bound recurrences listed above.

A tempting stronger closure was explicitly **not** used: multiplying the `K+1` local ratio along a long width-two exchange path would give an exponential distortion and does not yield the required factor two. Likewise, the finite `1+2K` renewal-component count by itself does not imply that a fixed balanced pair survives their mixture; the immediately preceding B11 run supplies a source-valid counterexample to that pairwise strengthening.

## 8. Status

- Exceptional range `7<=pi(P)<=K_3`: inherited **SOURCE-BOUND / PRESERVED**.
- Finite-kernel reduction from bounded range/variance/local fibers: inherited **REFUTED**.
- Strong-majority block-length bounds `K,2K,K`: **PROVED**.
- First-interruption renewal component count `<=1+2K`: **PROVED**, directly applying the latest assigned-partner recurrence.
- Arbitrary-chain profile diameter and nested depth bounds: **PROVED**.
- Exact nested-profile global lift-ratio bound `K+1`: **PROVED**.
- Existential finite-channel balance transfer: **OPEN / FIRST UNPAID STEP**.
- Width-three `1/3--2/3` target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, FEI material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex call, remote workflow, permission change, public posting, or production-brain mutation was used.
