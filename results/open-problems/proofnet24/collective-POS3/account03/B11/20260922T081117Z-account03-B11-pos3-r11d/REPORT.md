# POS3 account03/B11 — exact two-distinguisher chain identity and shared-support double-fork exit

**Run:** `20260922T081117Z-account03-B11-pos3-r11d`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all full linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All counts below are counts of full linear extensions of the original poset. Deletion skeletons are used only as an exact partition of the full extension set; no induced deletion law is treated as uniform.

## 1. Fresh state and named partner consumed

The active programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B11 assignment remains the distinct order-polytope/correlation route with designated partner `account04/B19`.

The immediate account03/B11 predecessor is

- `proofnet24/collective-POS3/account03/B11/20260922T074511Z-b11-pos3-r11c/REPORT.md`, blob `53d2dd83cc5691143f968fe40fac1bf962791673`.

It reduces the partner's `F2/F3 DISCREPANCY-CHAIN TRANSPORT` to the fully crossed bridge

`l<a<r`, `x<y`, `l<y`, `x<r`,

with

`l||x`, `a||x,y`, `r||y`,

and strong-majority order

`l prec_* x prec_* a prec_* y prec_* r`.

In a no-balanced counterexample the charged side pair `l||x` has central positive upper distinguisher `a`, while `y||r` has central positive lower distinguisher `a`. If either side has only one additional distinguisher, the predecessor's sign theorem forces that additional support to have the same positive sign. Thus the rigid minimum-support branch has exactly one positive external support on each charged side.

The required named OTHER-account result consumed is the latest complete partner report:

- account04/B19 run `B19-20260922T071535Z-r46`, report blob `26c2eab1c40a8da73357764efd0aab4160391e07`.

It eliminates high `F1`/`F4` recycling and proves that the only no-exit high-packet state is the opposite-ray `F2/F3` discrepancy chain with side packet totals `>4E/33`. The predecessor account03/B11 report then turns that into the fully crossed bridge above unless a fresh cross-pair distinguisher already exits the core.

This run attacks the remaining rigid **double-support** branch. The new point is an exact multiplicity identity for two comparable same-side distinguishers. It pays the entire branch in which the two charged sides try to reuse the **same** external support.

## 2. Exact comparable-two-distinguisher identity

### Theorem 2.1 — upper-chain identity

Let `p||q` in an arbitrary finite poset. Suppose the only two vertices distinguishing `p` from `q` are `u,v`, and they satisfy

`p<u<v`, `q||u,v`.

Thus, relative to the orientation `p<q`, both distinguishers are positive upper distinguishers and are comparable. Then the exact full-extension counts obey

`N(q<u) = 2 N(q<p)`.                                           (2.1)

No width hypothesis is used.

### Proof

Put

`R=P\{p,q,u,v}`

and fix an arbitrary skeleton `tau in L(R)`. Because `u,v` are the only distinguishers of `p,q`, every vertex of `R` has exactly the same relation to `p` as to `q`. Hence the exact admissible external-gap intervals of `p,q` in `tau` coincide:

`I_p(tau)=I_q(tau)`.

The induced order on the four special vertices is the three-chain `p<u<v` plus a vertex `q` incomparable with every member of that chain. Hence exactly four relative words are legal:

`q p u v`, `p q u v`, `p u q v`, `p u v q`.

Let their exact lift multiplicities over `tau` be `n_1,n_2,n_3,n_4`.

There is an exact bijection between the first two classes. Given a lift with word `q p u v`, keep all numerical external gaps fixed and exchange the labels `p,q`. Their admissible intervals are identical. The new `p` occupies the earlier old `q` position, so `p<u<v` is still respected; `q` has no order constraint to `p,u,v`. The operation is involutive. Therefore

`n_1=n_2`.                                                       (2.2)

Within this fiber, the event `q<p` is exactly the first word, while `q<u` is exactly the union of the first two words. Thus

`N_tau(q<u)=n_1+n_2=2n_1=2N_tau(q<p)`.                          (2.3)

Summing (2.3) over every `tau in L(R)` proves (2.1) for the original full uniform law. `square`

### Corollary 2.2 — lower-chain dual

Suppose instead that the only two distinguishers of `p||q` are positive lower distinguishers `u<v` with

`u<v<q`, `p||u,v`.

Then

`N(v<p)=2N(q<p)`.                                               (2.4)

This is the order-dual of Theorem 2.1. Equivalently, in each exact deletion fiber the last two legal words have equal multiplicity because the endpoint intervals of `p,q` coincide.

### Consequence at the `2/3` threshold

Equation (2.1) has the exact threshold consequence

`Pr(p<q)>2/3  =>  Pr(q<u)<2/3`.                                (2.5)

Indeed `Pr(p<q)>2/3` means `N(q<p)<E/3`, hence (2.1) gives `N(q<u)<2E/3`.

Dually, (2.4) converts `Pr(p<q)>2/3` into `Pr(v<p)<2/3`.

This is stronger than a qualitative swap injection: it transports the entire minority multiplicity with the exact factor `2`.

## 3. Shared positive support has only one possible geometry

Return to the fully crossed bridge. Work in the rigid minimum-support branch where

- `D(l,x)={a,z_L}` and both distinguishers are positive for `l<x`;
- `D(y,r)={a,z_R}` and both distinguishers are positive for `y<r`.

Here `D(s,t)` denotes the full relation-distinguisher set of the incomparable pair.

Assume first that the two external supports coincide:

`z_L=z_R=:z`.                                                    (3.1)

Relative to `l<x`, a positive support is either lower (`z<x`, `z||l`) or upper (`l<z`, `z||x`). Relative to `y<r`, it is either lower (`z<r`, `z||y`) or upper (`y<z`, `z||r`).

The fixed bridge relation `x<y` leaves only one compatible combination.

- If `z<x`, then `z<x<y`, so `z||y` is impossible; and `y<z` would create a cycle. Thus a left-lower support cannot also support the right pair.
- Hence `z` is left-upper: `l<z`, `z||x`.
- If it were also right-upper, `x<y<z` would contradict `z||x`.
- Therefore it is right-lower: `z<r`, `z||y`.

So every shared positive support has the exact geometry

`l<z<r`, `z||x,y`.                                              (3.2)

It is a second interior bridge point parallel to the central witness `a`.

## 4. Comparable shared support is impossible in the live strong-majority state

The central witness has

`l<a<r`, `a||x,y`.                                              (4.1)

There are three possibilities for `a,z`.

### Case 1: `a<z`

For the charged side pair `l||x`, the **only** distinguishers in the rigid minimum-support branch are `a,z`. By (4.1), (3.2), and `a<z`, they form the positive upper chain

`l<a<z`, `x||a,z`.

Apply Theorem 2.1 with

`p=l`, `q=x`, `u=a`, `v=z`.

It gives the exact global identity

`N(x<a)=2N(x<l)`.                                               (4.2)

But the live strong-majority order contains both

`l prec_* x` and `x prec_* a`.

The first inequality says `N(x<l)<E/3`; (4.2) therefore says

`N(x<a)<2E/3`,                                                  (4.3)

contradicting `x prec_* a`, which requires `N(x<a)>2E/3`.

Thus `a<z` is impossible.

### Case 2: `z<a`

Now the charged side pair `y||r` has exactly the two positive lower distinguishers `z,a`, in the chain

`z<a<r`, `y||z,a`.

Apply Corollary 2.2 with

`p=y`, `q=r`, `u=z`, `v=a`.

We obtain

`N(a<y)=2N(r<y)`.                                               (4.4)

The live order `y prec_* r` gives `N(r<y)<E/3`, so (4.4) yields

`N(a<y)<2E/3`,                                                  (4.5)

contradicting `a prec_* y`.

Thus `z<a` is impossible.

### Theorem 4.1 — shared support must be incomparable with the central witness

In the live rigid minimum-support fully crossed bridge, if the two charged sides reuse the same external positive support `z`, then necessarily

`a||z`.                                                         (4.6)

The proof is the pair of exact factor-two identities above. It uses full extension multiplicities, not a projected-law approximation or cross-anchor PQD.

## 5. The incomparable shared-support branch is a central double Hasse fork

Assume now `a||z`.

We already know

`l lessdot a lessdot r`

from the `F2/F3` Hasse types. I claim the shared support supplies the second cover on each side:

`l lessdot z lessdot r`.                                       (5.1)

For the lower cover, suppose `l<w<z`. Since `z||x`, one cannot have `x<w` (that would imply `x<z`) and one cannot have `w<x` (that would imply `l<x`). Therefore `w||x`. But then `l<w`, `w||x`, so `w` is a third positive upper distinguisher of `l,x`, contradicting `D(l,x)={a,z}`. Hence `l lessdot z`.

Dually, suppose `z<w<r`. Since `z||y`, neither `y<w` nor `w<y` is possible: the first would imply `y<r`, the second `z<y`. Thus `w||y`; then `w<r`, `w||y` makes `w` a third positive lower distinguisher of `y,r`, contradicting `D(y,r)={a,z}`. Hence `z lessdot r`.

Therefore the shared-support residual is the exact double fork

`l lessdot a,z lessdot r`, `a||z`,                              (5.2)

and because both `a,z` are incomparable with `x,y`, both

`{a,z,x}` and `{a,z,y}`                                        (5.3)

are width-saturating three-antichains.

Moreover none of the four old outer vertices distinguishes `a` from `z`:

- `l` lies below both;
- `r` lies above both;
- `x` is incomparable with both;
- `y` is incomparable with both.

Hence every distinguisher of the new central pair `a||z` is genuinely **external to the six-point double-fork core**.

In a hypothetical no-balanced counterexample, `a||z` cannot have zero distinguishers (the label-swap involution gives probability `1/2`) and cannot have exactly one distinguisher (the team's exact one-distinguisher theorem puts it in `[1/3,2/3]`). Therefore it has at least two fresh external distinguishers. If it has exactly two, the already proved account03/B11 two-distinguisher sign theorem forces them to have the same sign after orienting `(a,z)` by its strong majority.

Thus the shared-support branch does not recycle the old five-point bridge. It exits to a **central double Hasse fork with at least two fresh outside distinguisher channels**.

## 6. What this pays in the current collective residual

The predecessor residual `FULLY-CROSSED DOUBLE-SUPPORT TRANSPORT` had two qualitatively different minimum-support possibilities that were not yet separated:

1. the charged side pairs reuse the same positive external support;
2. they use two distinct positive external supports.

Sections 2-5 pay the first case completely at the structural/exchange level:

- a comparable shared support is impossible because the exact factor-two multiplicity identity collides with two adjacent `>2/3` strong-majority inequalities;
- an incomparable shared support becomes a second Hasse route through the center and necessarily emits at least two entirely fresh distinguishers of the new central pair.

No cross-anchor positive dependence is assumed; in particular this does not use the cross-anchor PQD implication already refuted by the partner stream.

The first unpaid implication on this route is therefore strictly narrower:

> **DISJOINT DOUBLE-SUPPORT TRANSPORT.** In the rigid fully crossed bridge, assume the unique external positive support `z_L` of `l||x` and the unique external positive support `z_R` of `y||r` are distinct. Classify their lower/upper sign types and use exact extension multiplicities plus width three to force balance, strong-majority span descent, a proper autonomous/ordinal reduction, or transfer to one of the already controlled multi-distinguisher/non-crossed charged corridors.

If either charged side already has at least three distinguishers, this minimum-support residual is not entered; that is the separate multi-distinguisher branch already exposed by the predecessor.

## 7. Exact regression and calibration

The companion standard-library verifier checks the new identity in two independent ways.

1. It enumerates `811` exact external-gap interval triples for the canonical upper-chain fiber and checks the word-class equality underlying (2.1).
2. It exhausts all `5,230` distinct naturally labelled transitive closures through `n=6`, scans every ordered incomparable pair having exactly two positive upper distinguishers that form a chain, and verifies (2.1) in all `1,326` such cases.

It also records a six-element calibration showing why one must use the **live adjacent strong-majority conditions** rather than claim that comparable shared support is impossible as a bare poset configuration. The poset generated by

`l<a<z<r`, `x<y`, `l<y`, `x<r`

has exactly `13` linear extensions and

`N(l<x)=9`, `N(x<a)=8`, `N(a<y)=11`, `N(y<r)=9`.

Thus both charged side pairs can be above `2/3`, while the adjacent inner comparison `x<a` is only `8/13<2/3`; exactly the factor-two obstruction from Theorem 2.1 prevents the full live strong-majority chain.

Recorded verifier output:

```text
interval_chain_cases 811
naturally_labelled_posets 5230
ordered_two_upper_chain_cases 1326
shared_comparable_calibration 13 9 8 11 9
POS3_SHARED_SUPPORT_CHAIN_CHECK_PASS
```

The exhaustive computation is regression evidence only. The arbitrary-size result is the exact deletion-fiber proof in Section 2.

## 8. Status

- fresh owner programme and account03/B11 assignment: **CONSUMED**;
- named partner account04/B19 r46: **CONSUMED/APPLIED**;
- immediate account03/B11 fully-crossed predecessor: **CONSUMED/APPLIED**;
- exact comparable-two-distinguisher factor-two identity: **PROVED**, arbitrary finite size;
- shared-support sign geometry: **PROVED**;
- comparable shared-support live branch: **ELIMINATED**;
- incomparable shared-support branch: **REDUCED TO A CENTRAL DOUBLE HASSE FORK WITH AT LEAST TWO FRESH OUTSIDE DISTINGUISHERS**;
- disjoint double-support transport: **OPEN**;
- parent POS3 target: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**;
- execution context: **`WITHOUT_VERIFIED_BRAIN`**.

No scheduler repair, extra task creation, cross-account native action, email/Drive/public/workflow dispatch, paid model/API/Codex use, credential access, benchmark work, or unrelated private transcript access occurred.
