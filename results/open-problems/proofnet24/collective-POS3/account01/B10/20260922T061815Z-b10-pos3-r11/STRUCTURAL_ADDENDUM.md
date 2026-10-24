# Structural addendum — a persistent (2,2) reverse-channel state forces one synchronized double-heavy cover

This addendum strengthens the same invocation's immutable `REPORT.md`. The run's primary outcome label remains `CANDIDATE_REFUTED` because the tested cross-anchor PQD mechanism is false, but the argument below is a separate arbitrary-size structural step toward the surviving POS3 route.

All probabilities are under the uniform law on all full linear extensions.

## 1. Setup inherited from the exact reverse-channel compression

Let `P` be a hypothetical width-at-most-three poset with no balanced pair. Let `a||b` be a strict nested endpoint with

`Pred(b) subseteq Pred(a)`, `b prec_* a`,

and define

`T=Max(Pred(a)\Pred(b))`,

`U=Min{z:b<z and z||a}`.

For every `t in T`, account02/B11 proves `t lessdot a` and `t||b`; for every `u in U`, `b lessdot u` and `u||a`. In the inherited no-strong-majority-span-descent branch,

`Pr(b<t)<1/3`, so `Pr(t<b)>2/3`,

and

`Pr(u<a)<1/3`, so `Pr(a<u)>2/3`.

Assume that the current pair `(b,a)` is span-minimal in the branch: there is no element `z` strictly between `b` and `a` in the inherited strong-majority order for which either `(b,z)` or `(z,a)` is an incomparable pair furnishing a strict span descent.

## 2. Cross relation is forced in the (2,2) state

### Lemma 2.1

If `|T|=|U|=2`, then there exist `t in T`, `u in U` with `t<u` in the poset.

### Proof

For any `t in T`, `u in U`, the relation `u<t` is impossible: since `b<u` and `t<a`, it would imply

`b<u<t<a`,

hence `b<a`, contradicting `a||b`.

If no relation `t<u` held either, every member of `T` would be incomparable with every member of `U`. Since `T` and `U` are themselves two-element antichains, `T union U` would be a four-element antichain, contradicting width at most three. Therefore some `t<u`. `square`

Thus the apparently worst four-channel state necessarily contains a genuine poset bridge between one predecessor channel and one successor channel.

## 3. One-sided threshold cuts on a saturated bridge

Fix a forced cross relation `t<u` from Lemma 2.1 and a saturated chain

`t=z_0 lessdot z_1 lessdot ... lessdot z_k=u`.

Define

`f_i=Pr(z_i<b)`, `g_i=Pr(z_i<a)`.

Both sequences are nonincreasing because `z_i<z_(i+1)`.

For the `b` sequence:

- `f_0=Pr(t<b)>2/3`;
- `f_k=0`, because `b<u` in the poset;
- no `z_i` can satisfy `z_i<b` as a poset relation, because then `t<=z_i<b`, contradicting `t||b`;
- therefore every `z_i` is either incomparable with `b` or lies above `b`. In a no-balanced poset, each nonzero incomparable value `f_i` lies outside `[1/3,2/3]`.

Hence there is a unique edge index `j_b` with

`f_(j_b)>2/3`, `f_(j_b+1)<1/3`,

and the exact cover-gap identity gives

`Pr(z_(j_b)<b<z_(j_b+1)) = f_(j_b)-f_(j_b+1) > 1/3`.      (3.1)

For the `a` sequence:

- `g_0=1`, because `t<a` in the poset;
- `g_k=Pr(u<a)<1/3`;
- no `z_i` can satisfy `a<z_i` as a poset relation, because then `a<z_i<=u`, contradicting `a||u`;
- therefore every `z_i` is either below `a` or incomparable with `a`, so again the nontrivial incomparable values avoid `[1/3,2/3]`.

Thus there is a unique edge index `j_a` with

`g_(j_a)>2/3`, `g_(j_a+1)<1/3`,

and

`Pr(z_(j_a)<a<z_(j_a+1)) = g_(j_a)-g_(j_a+1) > 1/3`.      (3.2)

These are exact full-extension fluxes across Hasse edges; no projected law is used.

## 4. The two heavy cuts are ordered

### Lemma 4.1

`j_b <= j_a`.

### Proof

For every `i`,

`{z_i<b} subseteq {z_i<a} union {a<b}`,

because if an extension has `z_i<b` but not `z_i<a`, then its total order has `a<z_i<b`, hence `a<b`.

Therefore

`f_i <= g_i + p`, where `p=Pr(a<b)<1/3`.                    (4.1)

If `f_i>2/3`, then `g_i>1/3`. But `g_i` is either `1` (when `z_i<a` in the poset) or, for an incomparable pair, lies outside `[1/3,2/3]`. Hence `g_i>2/3` whenever `f_i>2/3`.

So every index on the high side of the `b` threshold is also on the high side of the `a` threshold, which is exactly `j_b<=j_a`. `square`

## 5. Span minimality synchronizes the cuts

### Theorem 5.1 — synchronized double-heavy cover

Under the no-span-descent hypothesis of Section 1,

`j_b=j_a`.

Consequently there is a single Hasse edge

`z lessdot z'`

on the cross-channel bridge such that simultaneously

`Pr(z<b<z')>1/3`,                                             (5.1)

`Pr(z<a<z')>1/3`.                                             (5.2)

### Proof

Suppose `j_b<j_a` and put `w=z_(j_b+1)`. Then, by definition of the two cuts,

`Pr(w<b)<1/3`,

`Pr(w<a)>2/3`.

Relative to `b`, the relation `w<b` in the poset is impossible by the argument in Section 3. Thus either `b<w` in the poset or `b||w` with `Pr(b<w)>2/3`. In either case `b prec_* w`.

Relative to `a`, the relation `a<w` in the poset is impossible. Thus either `w<a` in the poset or `w||a` with `Pr(w<a)>2/3`. In either case `w prec_* a`.

Hence

`b prec_* w prec_* a`.                                       (5.3)

The vertex `w` cannot be comparable with both endpoints: the only possible comparable orientations are `b<w` and `w<a`, and together they would imply `b<a`, contradicting `a||b`. Therefore at least one of `(b,w)` and `(w,a)` is incomparable. Equation (5.3) then supplies a strict strong-majority span descent, contrary to the branch hypothesis.

Thus `j_b=j_a`. Substituting the common edge into (3.1)-(3.2) proves (5.1)-(5.2). `square`

## 6. Consequence for the current worst state

Combine Lemma 2.1 and Theorem 5.1:

> **(2,2)-state double-heavy-cover theorem.** In a width-three no-balanced nested endpoint with `|T|=|U|=2`, once strict strong-majority span descent is exhausted, one forced cross relation `t<u` produces a saturated bridge containing a single Hasse edge `z lessdot z'` across which **both original endpoints** have target-scale insertion flux greater than one third.

This converts the worst four-channel cross-anchor state into one concrete cover carrying two `>E/3` insertion channels. It is strictly more structural than any covariance estimate between the original reverse events.

The same invocation's counterexample shows why the no-balanced/span-minimal hypotheses matter: local cross-anchor covariance can be negative. In that finite witness the saturated bridge actually passes through balanced intermediate pairs, exactly the escape excluded in Theorem 5.1.

## 7. Interaction with the latest team results

The campaign lead account04/B10 already proved that a single target-scale heavy cover in the bridged branch must export through relation-distinguisher channels. The theorem above shows that the persistent `(2,2)` endpoint creates a **synchronized double-heavy cover**, not merely a single heavy cover.

The assigned partner account02/B11 latest leaf-splice theorem says a series-indecomposable no-balanced core cannot dispose of such a branch through an incomparability leaf whose majority-facing side is a nonempty chain. Thus a terminal escape from this synchronized cover must involve a genuinely nonchain leaf side, a multi-distinguisher state, a proper reduction with valid balance transfer, or a balanced pair.

The next unpaid implication is now sharply local:

> classify a Hasse cover `z lessdot z'` carrying both `Pr(z<b<z')>1/3` and `Pr(z<a<z')>1/3` with `b prec_* a`, and prove that in width three its external distinguisher geometry cannot persist without balance, span descent, or a valid reduction.

This replaces the now-refuted plan of obtaining the missing progress solely from cross-anchor positive correlation.

## 8. Status

- Cross-anchor pairwise PQD: **REFUTED** in the main report.
- Overlap-only scalar route to `1/3`: **INSUFFICIENT**, ceiling `2-sqrt(3)`.
- Forced cross relation in persistent `(2,2)` state: **PROVED**.
- Ordered threshold cuts along that bridge: **PROVED**.
- Synchronization of the two target-scale cuts under no-span descent: **PROVED**.
- Parent POS3: **OPEN / NOT PROVED**.
