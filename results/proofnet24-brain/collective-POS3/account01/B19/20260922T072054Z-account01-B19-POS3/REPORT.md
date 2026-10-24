# B19 POS3 — exact chain-profile swap defect and one-crossing propagation

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: **OPEN / NOT PROVED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## Source-bound inputs consumed

This run works under owner revision `2026-09-22.2` and `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; installation/benchmark work stays stopped.

Named OTHER-account inputs actually used:

1. **account02/B10, run `20260922T064948Z-b10-a11`**, shared handoff blob `bc7b56b0f40e2a1a1ff27f0a8f85b61465d60f12`.  It proves the exact first-boundary overload identity and the four-Hasse-channel localization.  In particular, outbound reverse defects lie on `d<x`, while immediate old-endpoint return is supported on the disjoint common boundary-minority event `x<d`; its residual is `POS3-RAY-RETURN-FRESH-MASS-v1`.
2. **campaign lead account04/B10 r17**, shared handoff blob `f5a263be6f1255619bc09574c10833602f1b8b85`.  It gives strict direction for comparable same-ray blockers, an anchor-free `>2/33` output for the anti-aligned incomparable case, and leaves only the aligned coherent width-saturating three-antichain gate (`COHERENT-GATE EXIT`).

The new result below attacks the common residual: can a same-ray defect be returned repeatedly merely by transporting the same insertion/deletion bias, without paying a genuinely new relation-profile source?

## 1. Exact chain-insertion model

Let

`C={c_1<...<c_m}`

be a deleted chain and put `Q=P\C`.  For `q in Q` define its chain-prefix interval

`I(q)=[lambda(q),rho(q)] subset {0,...,m}`

by

`lambda(q)=max({j:c_j<q} union {0})`,

`rho(q)=min({j-1:q<c_j} union {m})`.

For a fixed `tau=(q_1,...,q_n) in L(Q)`, a full extension above `tau` is equivalent to a weakly increasing state sequence

`z_1<=...<=z_n`,  `z_i in I(q_i)`,

where `z_i` is the number of elements of `C` preceding `q_i`.  Thus the exact lift multiplicity is the monotone-path count

`W_C(tau)=#{z_1<=...<=z_n : z_i in I(q_i)}`.

No induced law on `L(Q)` is replaced by a uniform law.

If `u,v` are incomparable, then `I(u)` and `I(v)` overlap.  Indeed, if `rho(u)<lambda(v)`, then with `k=rho(u)+1<=lambda(v)` one has `u<c_k<v`, a contradiction; the reverse separation is identical.

## 2. Exact adjacent-swap defect in one outside fiber

Fix an outside insertion skeleton in which `u,v` are adjacent.  Fix all chain-prefix states outside this adjacent block.  Let `s` be the state immediately before the block and `t` the state immediately after it (`0<=s<=t<=m`).  Write

`A=I(u)=[a,b]`,  `B=I(v)=[c,d]`.

Define

`N_AB(s,t)=#{(x,y) in A x B : s<=x<=y<=t}`,

`N_BA(s,t)=#{(x,y) in B x A : s<=x<=y<=t}`,

and `Delta=N_AB-N_BA`.

### Theorem 2.1 — closed defect formula

Because `A,B` overlap, exactly the endpoint-ordered or nested cases occur.

**(i) A is shifted left of B:** `a<=c<=b<=d`.  Put, after intersecting all sets with `[s,t]`,

`L=[a,c-1]`, `O=[c,b]`, `R=[b+1,d]`,

and let `ell,o,r` be their cardinalities.  Then

`Delta = ell*o + ell*r + o*r >= 0`.

If B is shifted left of A, the corresponding formula has the opposite sign.

**(ii) A is nested in B:** `c<=a<=b<=d`.  Put

`L=[c,a-1]`, `O=[a,b]`, `R=[b+1,d]`

inside `[s,t]`, again with cardinalities `ell,o,r`.  Then

`Delta = o*(r-ell)`.

If B is nested in A, then `Delta=o*(ell-r)` after reversing the roles.

### Proof

For the shifted case partition the two interval profiles into the ordered regions `L<O<R`.  Pairs lying in `O x O` occur equally in the two orders and cancel.  The excess for `uv` consists exactly of the disjoint classes

`L x O`, `L x R`, `O x R`,

whose sizes are `ell*o`, `ell*r`, `o*r`.

For `A subset B`, write `B=L disjoint-union A disjoint-union R`.  The `A x A` pairs again cancel.  The only positive excess consists of `A x R`, of size `o*r`; the only negative excess consists of `L x A`, of size `ell*o`.  Hence `Delta=o(r-ell)`.  This is an exact bijective decomposition of the swap defect, not an estimate.  QED.

### Consequence: exact fresh-tail labels

In the only sign-changing case, nesting, every positive defect unit is canonically labelled by

`(inner admissible state, right-tail state) in O x R`,

and every negative defect unit by

`(left-tail state, inner admissible state) in L x O`.

The two classes are disjoint.  Therefore a nested-profile reversal cannot be generated without using the opposite tail of the outer profile.  In poset language these tails are precisely chain-prefix states allowed to one element but not the other, i.e. relation-profile distinguishers against the deleted chain.

This is the chain-insertion analogue of account02/B10's full-extension return tax: opposite defect directions have disjoint exact sources.

## 3. One-crossing theorem

Still assume `A subset B`.  For fixed `t`, while `O` is nonempty,

`r=r(t)` is fixed and `ell=ell(s)` is nonincreasing as `s` increases.  Hence the sign of

`Delta(s,t)=o(s,t)*(r(t)-ell(s))`

can change at most once as a function of `s` (zeros ignored).  Similarly, for fixed `s`, `ell` is fixed while `r(t)` is nondecreasing, so the sign can change at most once as `t` increases.

Thus a raw nested chain-profile swap defect is a **single-crossing defect** in either boundary coordinate.

## 4. Variation-diminishing propagation through further insertions

For an interval `I subset {0,...,m}`, one insertion step acts on a boundary-state vector `f` by

`(T_I f)(r) = 1_I(r) * sum_{q<=r} f(q)`.

### Lemma 4.1

If `f` has at most one sign change after zeros are deleted, then `T_I f` has at most one sign change.

### Proof

If the signs of `f` are negative then positive, its cumulative sum is nonincreasing before the unique switch and nondecreasing afterwards, so it can cross zero at most once.  If the signs are positive then negative, the same argument with inequalities reversed applies.  Multiplication by the indicator of one interval only deletes a prefix and/or suffix and therefore cannot create an additional sign change.  QED.

By induction, **any finite product of fixed-profile insertion operators is one-crossing variation diminishing**.  The reverse/suffix recurrence is identical after reversing the state order.

### Theorem 4.2 — no passive repeated return

Take a nested adjacent-pair defect and propagate it through any fixed-profile insertion block on one side.  As a function of the remaining boundary state, its propagated sign can reverse at most once.  In particular an outward/return/outward sequence with two genuine sign reversals cannot be produced solely by passive transport through an unchanged chain-profile block.  A second reversal requires a new source: a profile endpoint change, a change of ray/boundary coordinate, or departure from the fixed-profile insertion regime.

This theorem is arbitrary-size and exact.  It is not a probabilistic approximation.

## 5. Application to the current team residual

account02/B10's `POS3-RAY-RETURN-FRESH-MASS-v1` says that the first outbound defect is localized to at most four Hasse channels and immediate old-endpoint return cannot reuse the same marked full extensions.  The remaining danger was a longer return through different/fresh witnesses.

Theorem 4.2 proves the following part of that residual:

> **Fixed-profile fresh-source principle.** Along any same-ray segment that can be represented by a fixed deleted chain and one-sided monotone chain-prefix propagation, a second defect-direction reversal cannot be recycled from the first defect.  It must be accompanied by a change of chain-profile endpoint (hence an actual new chain relation distinguisher) or by leaving that one-sided same-ray regime.

The lead account04/B10 r17 already removes the comparable same-ray gate by a literal positive strip and removes the anti-aligned incomparable gate by an anchor-free pair of minority `>2/33`.  Therefore the only place where the new source can still hide is the lead's coherent aligned width-saturating three-antichain gate.

## 6. Compact conditional end-to-end argument

A current minimal-counterexample route can now be written as follows.

1. Use the existing exact-two/corridor reductions under the original uniform full-extension law.
2. At the first non-exact-two boundary, use account02/B10's overload theorem to send the excess into at most four concrete outward Hasse channels; immediate old-endpoint return pays from the disjoint `x<d` reservoir.
3. Use account04/B10 r17 to resolve comparable same-ray blockers and anti-aligned incomparable blockers.  Only the coherent aligned three-antichain gate remains.
4. On every coherent segment admitting a fixed-chain profile representation, use Theorem 4.2: passive insertion/deletion transport cannot create repeated returns.  Any further return must change a profile endpoint or exit the regime.
5. **If** one proves the endpoint-reuse exclusion below, every nonterminal coherent return consumes a genuinely fresh endpoint/witness.  Since the poset is finite, the canonical process cannot recycle forever.  It must reach one of the established terminal alternatives: a balanced pair, strict strong-majority span descent, proper autonomous/ordinal reduction, an opposite-ray split, or a previously controlled exact-two/non-crossed mechanism.  The minimal-counterexample induction then closes POS3.

## 7. First essential missing implication

The residual is now narrower than generic `RAY-RETURN-FRESH-MASS`:

### `POS3-COHERENT-ENDPOINT-REUSE-EXCLUSION`

At the account04/B10 r17 coherent aligned three-antichain gate, prove that either

1. the canonical same-ray continuation embeds into the fixed-chain one-sided profile propagation of Theorem 4.2; or
2. the first failure of that embedding changes a `lambda` or `rho` endpoint in a way that can be charged to a Hasse witness not already used by the preceding outward packet; or
3. one of the existing terminal alternatives occurs immediately.

Moreover, the same profile endpoint must not be reusable to pay a later second return without forcing balance, span descent, a width-four obstruction, or an autonomous reduction.

This is the exact point not proved here.  The new theorem removes passive fixed-profile oscillation; what remains is a genuinely structural endpoint-reuse question in width three.

## 8. Verification

A deterministic exact-integer regression independently checked:

- `229306` local interval/window cases for the closed defect formula;
- `64658` nested boundary slices for the one-crossing property;
- `151872` one-step prefix/mask cases over integer vectors with at most one sign change for variation diminution.

The captured output ends

`POS3_CHAIN_PROFILE_DEFECT_CHECK_PASS`.

Verifier Git blob: `8dedcd93f7e847b62701a8b685ed7e4584c74bc2`; executed-byte SHA-256: `461fb9e168898c9e9c81a3fd338e770eee41b663a352792d760622be4b88ba8c`.

Output Git blob: `57ac19b6eef815e9130acefe576deee5c878c63a`; output-byte SHA-256: `114430fc78a1d9ebeafae65c82e9df6eb6f3bf6ef5c4e2d97455a78788758498`.

The computation is regression evidence only; the arbitrary-size statements above are proved symbolically.

## 9. Honest status

This run does **not** prove POS3, does not promote any finite census to closure, and does not claim that every lead coherent gate already has the required fixed-chain embedding.  It supplies an exact arbitrary-chain adjacent-swap recurrence, identifies the positive and negative nested-defect sources bijectively, proves one-crossing under boundary motion, and proves variation-diminishing propagation through arbitrary fixed-profile insertion blocks.  The first unpaid theorem is `POS3-COHERENT-ENDPOINT-REUSE-EXCLUSION`.
