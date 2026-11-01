# Addendum — predecessor nesting needs only the endpoint inclusion

This addendum strengthens Lemma 3.1 and Theorem 5.1 of the immutable run report without modifying that report.

## A. Stronger fork-sibling nesting lemma

Let `P` have width at most three. Suppose

- `a||b` and `Pred(b) subseteq Pred(a)`,
- `a lessdot u` and `a lessdot v`,
- `u||v`, `u||b`, and `v||b`.

Then `Pred(u)` and `Pred(v)` are nested.

### Proof

Assume neither predecessor set contains the other. Choose

`d in Pred(u)\Pred(v)`, `e in Pred(v)\Pred(u)`.

As in the report, `d||a`: if `d<a`, then `d<a<v`, contradicting `d notin Pred(v)`; if `a<d<u`, this contradicts `a lessdot u`. Likewise `e||a`.

Now `d||b`. If `d<b`, then `d in Pred(b) subseteq Pred(a)`, contradicting `d||a`. If `b<d<u`, then `b<u`, contradicting `b||u`. Thus `d||b`; similarly `e||b`.

Also `d||v` and `e||u`: for example `d<v` is excluded by choice of `d`, while `v<d<u` would imply `v<u`, contrary to `u||v`.

Finally `d||e`: `d<e<v` would imply `d<v`, and `e<d<u` would imply `e<u`.

Hence `{a,b,d,e}` is a four-antichain, contradicting width at most three. `square`

The equality `Pred(a)=Pred(b)` used in the original report was stronger than necessary.

## B. Consequence at the actual first boundary

At the inherited first strong-majority boundary `x prec_* y`, the previous endpoint exchange state gives

`Pred(y) subseteq Pred(x)`,

and the inherited Hasse-fork theorem gives exactly two blockers `s_1,s_2` with

`x lessdot s_1`, `x lessdot s_2`, `s_1||s_2`, and `s_i||y`.

The stronger lemma therefore applies **immediately** to the first fork:

`Pred(s_1)` and `Pred(s_2)` are nested.

Thus the lead's lower-distinguisher branch is not an independent uncontrolled branch:

- if the nesting is strict, the sibling pair is already a strict predecessor-nested extreme endpoint;
- if the predecessor sets are equal, orient the siblings by the strong-majority order and enter the equal-predecessor span-descent/fork-escalation theorem.

Every subsequent clean fork again satisfies the stronger lemma (indeed its parent pair has equal predecessor sets). A clean continuation moves both new blockers strictly to the right of the old right endpoint. Therefore the finite-position argument from Theorem 5.1 applies unchanged.

### Strengthened funnel theorem

In the inherited minimal-counterexample first-boundary setting, after the first two-cover Hasse fork, **all** sibling cases—both the lower-distinguisher and no-lower-distinguisher cases—funnel after finitely many clean fork steps to an extreme incomparable pair `(x',y')` with strictly nested predecessor sets.

Consequently the first surviving structural branch is the strict predecessor-nested endpoint itself. The exact endpoint exchange then reduces it to

`Pr(x'<y') = 1-(Q+R)/(2E)`

after labeling so that `Pred(y') proper_subset Pred(x')`.

The first essential missing implication is therefore the nested-endpoint mass lemma from the report, not a separate lower-distinguisher termination theorem.

## C. Relation to fleet02/B19 r13

The fleet02/B19 linear-depth family remains relevant exactly as stated in the report: the strengthened funnel is a finite structural reduction, not a bounded-radius balanced-pair selector. The partner family prevents upgrading “finite funnel to nested endpoint” into an unjustified `O(1)` or `o(n)` local-balance claim.

**Status:** stronger fork-sibling nesting and the unified first-boundary funnel are proved; POS3 remains open.
