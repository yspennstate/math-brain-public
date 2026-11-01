# POS3 fleet03/B11 — opposite-sign two-distinguisher balance theorem

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

The active programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact fleet03/B11 assignment is to pursue a distinct order-polytope/correlation method that improves the decisive pair-selection statement; named partner: fleet04/B19. This run uses exact extension multiplicities and does not resume the superseded installation or benchmark work.

## 1. Exact inherited state and peer result consumed

The immediate fleet03/B11 predecessor is

- `proofnet24/collective-POS3/fleet03/B11/B11-20260922T021330Z-pos3/REPORT.md`, blob `84167cd7b3a69dc8e4c699fc5ca0e5c9ba5e4a8d`.

It proves the exact two-gap deletion-fiber formula for an incomparable pair `a,b`; in particular `Pr(a<b)>2/3` forces a deletion fiber with `A_tau>2B_tau`. It also proves that in width three the elements simultaneously incomparable with `a,b` form a chain, and its exact 121-extension adversary shows that one first Hasse fork plus one delayed distinguisher is not enough to force a balanced pair.

The named other-account partner result consumed in this run is the latest completed fleet04/B19 report available before the derivation:

- fleet04/B19 run `B19-20260922T001218Z-r44`, canonical report commit `d9c8c3761d47861b28bcd63102eb625d596d51df`, blob `ce30dae79d698103f026d4d871033238489b1fb1`.

It proves by an exact fiber bijection that if `M` is autonomous in `P`, then the restriction of a uniform random linear extension of `P` to `M` is uniform on `L(P[M])`. Consequently a cardinality-minimal POS3 counterexample has no proper autonomous nonchain. Applied to the first-boundary blocker siblings, this removes the zero-distinguisher branch under the actual full uniform law rather than under an induced-law approximation.

Two compatible team inputs sharpen the residual. Fleet02/B10 proves that an incomparable pair with exactly one distinguisher is balanced. Fleet04/B10 proves, in the equal-predecessor branch, an exact positive-channel identity and a span-descent/fork-escalation dichotomy. The new theorem below pays the next support-size branch: **two distinguishers whose asymmetries point in opposite directions cannot support an extreme pair either**.

## 2. Distinguisher sign

Fix incomparable `a,b`. An outside element `z` distinguishes them if its three-valued relation to `a` differs from its relation to `b`. Since `a||b`, a distinguisher is comparable with exactly one endpoint. Relative to the orientation `a<b`, define its sign by

- positive: `a<z, z||b`, or `z<b, z||a`;
- negative: `z<a, z||b`, or `b<z, z||a`.

The terminology is only a bookkeeping convention; the proof below derives the probability bound exactly.

If every distinguisher is positive, then

`Pred(a) subseteq Pred(b)` and `Succ(b) subseteq Succ(a)`.

Swapping `a,b` in every extension with `b<a` is then a valid injection into extensions with `a<b`, so `Pr(a<b)>=1/2`. Dually, if every distinguisher is negative, `Pr(a<b)<=1/2`. Thus an extreme orientation `Pr(a<b)>2/3` with exactly two same-sign distinguishers must use the positive sign.

## 3. Exact external-gap representation

Let `z,w` be the only two distinguishers of `a,b`, and put

`R=P\{a,b,z,w}`.

Fix `tau in L(R)`. Number the external gaps of `tau` by integers. Since every element of `R` has the same relation to `a` as to `b`, the exact admissible gap intervals of `a,b` coincide:

`I_a(tau)=I_b(tau)=I=[ell,u]`.

For any special element `v`, its admissible gaps relative to `tau` form a contiguous interval `I_v=[ell_v,u_v]`. If `a<v`, transitivity gives

`Pred_R(a) subseteq Pred_R(v)`, `Succ_R(v) subseteq Succ_R(a)`,

hence

`ell_v>=ell`, `u_v>=u`.

So `I_v` is weakly shifted to the right of `I`. If `v<a`, the inequalities reverse and `I_v` is weakly shifted to the left.

For a fixed relative-order word `pi` of the four special elements, every lift of `tau` with word `pi` is uniquely represented by assigning to the letters of `pi` a weakly increasing sequence of external gaps, each lying in that letter's exact interval. Equal-gap letters are ordered inside that gap by `pi`. This is a bijection, so all counts below are exact extension multiplicities.

### Lemma 3.1 — adjacent interval swap

Suppose incomparable adjacent letters `X,Y` occur as `... X Y ...`, and `I_X=[l_X,u_X]` is weakly right-shifted from `I_Y=[l_Y,u_Y]`, meaning `l_X>=l_Y` and `u_X>=u_Y`. Then

`N(... X Y ...) <= N(... Y X ...)`.

**Proof.** Take any admissible weakly increasing gap assignment for `... X Y ...`; write the two adjacent gaps as `i<=j`. We have `i in I_X` and `j in I_Y`. Because

`l_Y <= l_X <= i <= j <= u_Y <= u_X`,

we also have `i in I_Y` and `j in I_X`. Keep the numerical gap sequence unchanged and exchange which of the two labels occupies the two adjacent positions. This is an injective map into assignments for `... Y X ...`. `square`

The left-shifted version is the order-dual statement.

## 4. The two canonical opposite-sign configurations

Up to exchanging `a,b` and/or taking the order dual, two opposite-sign distinguishers have exactly two possible relation patterns.

### Case A — two upper constraints on opposite endpoints

Assume

`a<z`, `b<w`, `b||z`, `a||w`.

Then necessarily `z||w`: either comparison between them would, by transitivity, contradict one of `b||z` or `a||w`. Thus the induced special poset is two disjoint two-chains `a<z` and `b<w`. Both `I_z` and `I_w` are weakly right-shifted from the common interval `I`.

There are six special-element words. Write their exact multiplicities as

`n1=N(a z b w)`, `n2=N(a b z w)`, `n3=N(a b w z)`,

`n4=N(b w a z)`, `n5=N(b a w z)`, `n6=N(b a z w)`.

The words with `a,b` adjacent have equal counts because their intervals are identical:

`n2=n6`, `n3=n5`.

By Lemma 3.1, moving the right-shifted `z` to the right of `b` can only increase the count, and likewise for `w` relative to `a`:

`n1<=n2`, `n4<=n5`.

Hence, with

`A_tau=n1+n2+n3` and `B_tau=n4+n5+n6`,

we obtain

`A_tau <= 2(n2+n3) <= 2 B_tau`,

and symmetrically

`B_tau <= 2(n2+n3) <= 2 A_tau`.

Therefore

`1/2 <= A_tau/B_tau <= 2`,

with the evident interpretation when a count is zero; equivalently

`1/3 <= A_tau/(A_tau+B_tau) <= 2/3`.

### Case B — a sandwich around one endpoint

Assume

`w<a<z`, while `b||w`, `b||z`.

Then `w<a<z` is a three-chain and `b` is incomparable with every member of that chain. The interval `I_w` is weakly left-shifted from `I`, while `I_z` is weakly right-shifted.

There are four special words:

`m1=N(b w a z)`, `m2=N(w b a z)`,

`m3=N(w a b z)`, `m4=N(w a z b)`.

Again `m2=m3` because `a,b` have identical intervals. The left-shifted adjacent-swap inequality gives `m1<=m2`, and the right-shifted one gives `m4<=m3`. Thus, if

`A_tau=m3+m4`, `B_tau=m1+m2`,

then for `C=m2=m3`, both `A_tau` and `B_tau` lie in `[C,2C]`. Consequently

`1/3 <= A_tau/(A_tau+B_tau) <= 2/3`.

These two cases exhaust opposite signs.

## 5. Two-distinguisher sign theorem

### Theorem 5.1

Let `P` be any finite poset and let `a,b` be incomparable. Suppose exactly two vertices distinguish `a` from `b`. If the two distinguishers have opposite signs relative to `a<b`, then

`1/3 <= Pr(a<b) <= 2/3`.

**Proof.** Fix `tau in L(R)`. Sections 3-4 prove the required `[1/3,2/3]` inequality separately in every exact deletion skeleton, with no assumption that the skeletons are uniformly distributed. Equivalently each fiber satisfies

`A_tau <= 2B_tau` and `B_tau <= 2A_tau`.

Summing these two inequalities over all `tau` gives

`N(a<b)<=2N(b<a)` and `N(b<a)<=2N(a<b)`,

which is exactly the asserted probability interval. `square`

The theorem does not use width three. Width three enters when it is applied to the inherited POS3 minimal-counterexample structure.

### Corollary 5.2 — coherent minimum support for an extreme pair

If `Pr(a<b)>2/3` and `a,b` have exactly two distinguishers, then the two distinguishers have the **same positive sign** relative to `a<b`.

Indeed Theorem 5.1 rules out opposite signs. If both had negative sign, the endpoint-swap injection in Section 2 would give `Pr(a<b)<=1/2`.

## 6. Application to the first Hasse-fork sibling pair

Return to the inherited hypothetical cardinality-minimal width-three counterexample. At the first strong-majority block boundary `x prec_* y`, fleet03/B11 previously proved a two-cover Hasse fork

`x lessdot s_1`, `x lessdot s_2`,

with `s_1||s_2`, `s_i||y`, and every distinguisher of `{s_1,s_2}` occurring strictly after the entire second majority block `B_2`.

The named fleet04/B19 autonomous-subset theorem removes zero distinguishers. The compatible fleet02/B10 exact insertion theorem removes exactly one distinguisher. The new theorem now removes the **two-distinguisher opposite-sign** branch.

Rename the siblings so that `s_1 prec_* s_2`; then a counterexample has `Pr(s_1<s_2)>2/3`. The residual support structure is therefore:

1. at least three distinct delayed distinguishers after `B_2`; or
2. exactly two delayed distinguishers, and both are positive for the orientation `s_1<s_2`.

This becomes especially sharp in the inherited clean sibling branch `Pred(s_1)=Pred(s_2)`. There no lower distinguisher is possible. Hence in case (2) both witnesses must have the form

`s_1<z_i`, `z_i||s_2`, `i=1,2`.

Combining this with fleet04/B10's exact equal-predecessor channel/fork-escalation theorem shows that these two vertices are precisely the two positive canonical successor channels in the minimum-support branch: both are Hasse covers of `s_1`, `{s_2,z_1,z_2}` is a three-element antichain, the total positive channel mass is `>E/3`, and at least one channel carries `>E/6` extensions. The same fleet04/B10 bridge then forces the original endpoint `y` below at least one member of the new fork.

Thus the former vague requirement “there are delayed witnesses” has been sharpened into a **coherent delayed second-fork alternative** unless there are at least three delayed distinguishers.

## 7. Same-sign is genuinely necessary

The theorem cannot be extended by replacing “opposite signs” with “any two distinguishers.” Consider the five-element poset generated by

`0<2`, `0<4`, `1<4`.

It has exactly `25` linear extensions. For the incomparable pair `(a,b)=(1,2)`, the only distinguishers are

- `0<b`, `0||a` (positive),
- `a<4`, `4||b` (positive).

Exact counting gives

`N(a<b)=20`, `N(b<a)=5`,

so

`Pr(a<b)=4/5`.

Thus two same-sign distinguishers can support much more than `2/3`. This is an adversary to the stronger local statement, not a counterexample to POS3.

The team's previous 121-extension witness is consistent with the same phenomenon: for its extreme sibling pair `(3,6)`, the exactly two distinguishers `{4,5}` both lie above `3` and are incomparable with `6`, hence both have the same positive sign.

## 8. Verification

The companion standard-library verifier performs two independent finite regressions of the symbolic proof:

1. It checks `1,780` interval instances of canonical Case A and `1,780` of Case B, including both endpoint equalities `1/3` and `2/3`, and checks the exact adjacent-word inequalities used above.
2. It exhausts all `357` distinct transitive closures obtained from naturally labelled five-point relation sets, tests `1,984` incomparable pairs, and finds `214` pairs with exactly two opposite-sign distinguishers; every one satisfies the theorem.
3. It reconstructs the five-element same-sign witness exactly and obtains `25` extensions and probability `20/25=4/5`.

Recorded output ends with

`POS3_TWO_DISTINGUISHER_SIGN_CHECK_PASS`.

The finite program is regression evidence. The arbitrary-size result is the exact fiber proof in Sections 3-5.

## 9. New residual

The parent POS3 theorem remains open. The first unpaid structural implication is now narrower:

> At the first strong-majority boundary of a cardinality-minimal width-three counterexample, couple the two active Hasse-cover flow channels with the delayed distinguisher support. Prove that either the `>=3`-distinguisher branch or the coherent exactly-two positive second-fork branch forces a balanced incomparable pair, a four-element antichain, or a proper autonomous nonchain when propagated to the next strong-majority boundary.

For the clean equal-predecessor branch, the exactly-two case is now completely oriented: both delayed witnesses lie above the majority-earlier sibling and become the two Hasse covers in the second fork. The next useful mechanism should exploit that orientation together with the first boundary endpoint relation `y<z_i` and exact channel mass `>E/6`, rather than return to a one-fork or one-fiber local argument already refuted by the exact adversaries.

No novelty or priority claim is made. No benchmark gold or keys, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used.
