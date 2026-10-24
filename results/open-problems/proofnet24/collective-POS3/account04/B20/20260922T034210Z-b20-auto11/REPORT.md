# POS3 account04/B20 — exact blocker-swap defect and sharp two-distinguisher transfer

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no superseded brain-installation or benchmark work.

## 1. Exact source-bound state consumed

The fresh campaign-lead version is

- **account04/B10**, `proofnet24/collective-POS3/account04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `b077c3fedba7e6e8ab72b683b5eafd8203005467`.

It proves that at the first strong-majority Hasse fork the two sibling predecessor sets are nested. In the strict branch, after relabelling,

`Pred(b) proper_subset Pred(a)`,

and the proper difference is a delayed chain with top `d` satisfying `d lessdot a` and `d||b`. Its exact endpoint argument then gives either strict strong-majority span descent or a new successor-blocker corridor. The remaining global obligation is an exact mass inequality for this strict predecessor-nested endpoint.

The required newest complete **OTHER-account assigned-partner** version is

- **account01/B19**, `proofnet24/collective-POS3/account01/B19/20260922T024644Z-b19-pos3-r11/REPORT.md`, blob `d1a22bb63b9a5fa57541e1970dac09d7aec14937`.

It deletes the first strong-majority element and proves the exact width-two ideal-cut convolution / hitting-time tilt. Its remaining WICSL selection problem explicitly requires an adaptive global pair: an arbitrary balanced pair of the smaller uniform poset need not survive the exact restoration weights. I use that warning here by staying entirely in the original uniform law and selecting the canonical strict endpoint furnished by the lead.

A decisive additional current peer input is

- **account02/B19**, `proofnet24/collective-POS3/account02/B19/20260922T031214Z-account02-B19-pos3-r11/REPORT.md`, blob `53669a7baac8d3a37b45229448c1288bf7c0cf60`.

It gives an exact 15-point width-three, connected, module-prime adversary with a strong pair `(3,13)` at probability

`Pr(3<13)=1207/1810=2/3+1/5430`,

and exactly two relation distinguishers: lower `12` and upper `9`, with

`Pred(13)=Pred(3) union {12}`,
`Succ(3)=Succ(13) union {9}`.

Thus relation-distinguisher count alone cannot close the strict endpoint; the signed transport term has to be identified exactly. That is the first unpaid universal step attacked below.

## 2. Compact conditional end-to-end route

Assume for contradiction-search purposes that `P` is a width-at-most-three poset with no balanced incomparable pair, and take the canonical strict predecessor-nested endpoint `(a,b)` produced by the lead.

The exact induction route is now:

1. account01/B19 supplies genuine smaller uniform laws and rules out arbitrary-pair transfer;
2. account04/B10 supplies a canonical strict endpoint in the original uniform law;
3. the present theorem writes the *entire signed ordering defect of any incomparable pair* as a difference of two explicit endpoint-blocker events;
4. for the sharp one-lower/one-upper residual exposed by account02/B19, the formula collapses to one inclusion-exclusion union with no hidden term.

Consequently the remaining POS3 task becomes a precise global blocker-union inequality, rather than an unspecified deletion-law distortion.

## 3. Universal blocker-swap identity

Let `a||b` in an arbitrary finite poset `P`. Define the four relation-difference sets

`D_a = Pred(a) \ Pred(b)`,
`D_b = Pred(b) \ Pred(a)`,
`U_a = Succ(a) \ Succ(b)`,
`U_b = Succ(b) \ Succ(a)`.

For a linear extension `L`, define the two orientation-specific blocker events

`B_- = { b precedes some d in D_a  OR  some u in U_b precedes a }`,

`B_+ = { a precedes some d in D_b  OR  some u in U_a precedes b }`.

Every extension in `B_-` necessarily has `b<a`: if `b<d` with `d<a`, then `b<d<a`; if `u<a` with `b<u`, then `b<u<a`. Dually, every extension in `B_+` necessarily has `a<b`. Hence `B_-` and `B_+` are disjoint.

### Theorem 3.1 — exact blocker-swap defect

Writing `N(a<b)` and `N(b<a)` for exact uniform extension counts,

`N(b<a)-N(a<b) = |B_-| - |B_+|`.                              (3.1)

Equivalently,

`2 Pr(a<b)-1 = Pr(B_+) - Pr(B_-)`.                             (3.2)

### Proof

Take an extension `L` with `b<a` and `L notin B_-`. Swap only the positions occupied by `a` and `b`.

For the new earlier copy of `a`, every common predecessor of `a,b` was already before `b`. Every extra predecessor `d in D_a` is also before `b`, because `L notin B_-` excludes `b<d`. Thus all predecessors of `a` remain before it. Moving `a` earlier cannot violate any successor relation.

For the new later copy of `b`, every common successor of `a,b` was already after `a`. Every extra successor `u in U_b` is also after `a`, because `L notin B_-` excludes `u<a`. Thus all successors of `b` remain after it. Moving `b` later cannot violate any predecessor relation.

So the swap is a valid linear extension with `a<b`. The same argument with the roles reversed shows that swapping an `a<b` extension outside `B_+` gives a valid `b<a` extension. The swap is its own inverse; therefore it is a bijection

`{L:b<a} \ B_-  <->  {L:a<b} \ B_+`.

Subtracting the two cardinalities gives (3.1), and division by `e(P)` gives (3.2). `square`

This argument uses the actual uniform extension set of `P`; no induced or projected law is renamed uniform.

## 4. Strict predecessor nesting: the lead endpoint becomes a small signed interface

Suppose now the lead has supplied

`Pred(b) proper_subset Pred(a)`.

Then `D_b=empty`, so the only positive-orientation blocker comes from successors of `a` that are not successors of `b`:

`B_+ = { some u in U_a precedes b }`.                           (4.1)

The reverse blocker is

`B_- = { b precedes some d in D_a  OR  some u in U_b precedes a }`. (4.2)

At the first-fork strict branch, the lead proves that `D_a` is a chain. If `d=max D_a`, then

`{b precedes some element of D_a} = {b<d}`.                    (4.3)

For either successor-difference set it is enough to retain its minimal members: if any successor distinguisher appears before the opposite endpoint, then a minimal such successor appears before it. Those minimal successors form an antichain, all incomparable with the opposite endpoint, so width at most three bounds each minimal successor interface by two elements.

Therefore the current strict endpoint has an exact signed interface involving

- one lower event `b<d`,
- at most two reverse successor-blocker events,
- at most two forward successor-blocker events.

The lead's previously open endpoint mass inequality is precisely

`|Pr(B_+)-Pr(B_-)| <= 1/3`.                                    (4.4)

Indeed (3.2) then gives `Pr(a<b) in [1/3,2/3]` immediately. This is the canonical original-law replacement for an arbitrary WICSL pair.

## 5. Exact one-lower / one-upper polynomial

The sharp account02/B19 adversary isolates the smallest aligned residual. Assume

`D_a={d}`, `D_b=empty`, `U_a=empty`, `U_b={u}`.                 (5.1)

Thus `d<a`, `d||b`, `b<u`, `u||a`, and there are no other relation distinguishers between the endpoints.

Theorem 3.1 collapses to

`N(b<a)-N(a<b) = # { b<d OR u<a }`.                            (5.2)

Hence

`Pr(a<b) = (1 - Pr(b<d OR u<a))/2`.                            (5.3)

This is an exact arbitrary-size identity. It immediately recovers the one-distinguisher balance mechanism: if only one of the two flank events existed, its probability is `<1/3` in a no-balanced strong-majority configuration, and (5.3) would put the endpoint in `(1/3,1/2]`.

When both flank events exist, (5.3) identifies the exact missing interaction:

`Pr(b<d OR u<a)`
` = Pr(b<d) + Pr(u<a) - Pr(b<d AND u<a)`.                       (5.4)

There is no additional hidden deletion-law term.

### Per-deletion two-gap form when `d<u`

Delete `a,b` and fix a linear extension `tau` of the remainder. The admissible insertion-gap intervals have the crossing form

`I_b=[L,s]`, `I_a=[r,U]`, with `L<=r<=s<=U`.

Put

`ell=r-L`, `rho=U-s`, `m=s-r+1`.

Direct two-gap counting gives

`N_tau(b<a)-N_tau(a<b) = m(ell+rho)+ell*rho`.                  (5.5)

The three terms have exact blocker meanings in this fiber:

`#(b<d)       = ell(m+rho)`,
`#(u<a)       = rho(m+ell)`,
`#(b<d,u<a)   = ell*rho`.

Thus inclusion-exclusion gives exactly (5.5). Summing over `tau` yields (5.2). The swap proof above shows that the global identity remains valid even when `d||u`; no comparability assumption between the two distinguishers is needed globally.

## 6. Consequence in a hypothetical no-balanced corridor

In the majority-late strict corridor the strong-majority order has

`d prec_* b prec_* a prec_* u`

whenever the one-lower/one-upper aligned residual (5.1) occurs without an earlier span descent. Therefore

`Pr(b<d)<1/3`,
`Pr(u<a)<1/3`.                                                  (6.1)

If the endpoint itself is strong in the reverse direction, `Pr(a<b)<1/3`. By (5.3), this is equivalent to

`Pr(b<d OR u<a)>1/3`.                                          (6.2)

Consequently

`max(Pr(b<d), Pr(u<a)) > 1/6`.                                 (6.3)

So the sharp residual necessarily contains a flanking incomparable pair whose minority orientation lies strictly in `(1/6,1/3)`, equivalently whose majority probability lies in `(2/3,5/6)`.

This does not finish POS3. It does give an exact quantitative transport target and shows why a pure distinguisher count cannot work: two individually subcritical minority channels can have a union just above `1/3`.

## 7. Exact check on the published sharp adversary

For the account02/B19 15-point witness, take

`a=13`, `b=3`, `d=12`, `u=9`.

The independent verifier in this run obtains

`E=1810`,
`N(a<b)=603`,
`N(b<a)=1207`,
`#(b<d)=336`,
`#(u<a)=352`,
`#(b<d AND u<a)=84`,
`#(b<d OR u<a)=604`.

Therefore

`N(b<a)-N(a<b)=1207-603=604`

is exactly the blocker union `336+352-84=604`. Equivalently,

`Pr(3<13)=1207/1810=2/3+1/5430`

and the reverse endpoint probability is `603/1810=1/3-1/5430` because the blocker union exceeds `1/3` by the corresponding one-count amount.

The same verifier exhausts all 357 transitively closed posets compatible with one fixed five-label linear extension and checks (3.1) on all 3968 ordered incomparable endpoint pairs. It also checks the aligned specialization on 1942 pairs. No failure occurs.

Captured output:

```text
unique_five_point_posets 357
ordered_incomparable_pairs_checked 3968
aligned_pairs_checked 1942
sharp_E 1810
sharp_N_a_before_b 603
sharp_N_b_before_a 1207
sharp_lower_blocker 336
sharp_upper_blocker 352
sharp_intersection 84
sharp_union 604
sharp_signed_defect 604
POS3_BLOCKER_EXCHANGE_IDENTITY_PASS
```

The computation is regression evidence only. Theorem 3.1 and its corollaries are proved symbolically above.

Verifier SHA-256: `8c176c430ace43a4e1ae54d02003ecbc064e97efe769a3a4edf99925b319093c`.  
Captured-output SHA-256: `a3ec336a823974d8d479c6134c02aef63f0ac9fe57f264c9543111f5995526a6`.

## 8. What is paid and what remains unpaid

**Paid in this run.** The signed transport term at the strict nested endpoint is no longer opaque. For every incomparable pair it is exactly the difference of two endpoint-blocker events under the original uniform law. In the sharp one-lower/one-upper aligned residual, the entire endpoint defect is exactly one blocker union, with explicit inclusion-exclusion and a two-gap polynomial. The published one-count adversary is reproduced exactly by this identity.

**Still unpaid.** POS3 remains open. The next universal implication must use the minimal-counterexample global structure—heavy-slice / rank-atom constraints, delayed-distinguisher placement, or the partner's exact ideal-cut recurrence—to show that at the canonical strict endpoint

`|Pr(B_+)-Pr(B_-)| <= 1/3`,

or to produce a strict span descent / balanced flanking pair first. In the aligned one-lower/one-upper residual this reduces all the way to

`Pr(b<d OR u<a) <= 1/3`.

The account02/B19 witness shows this inequality is false for arbitrary width-three posets by the arithmetically minimal one-count margin, so any successful proof must use the *full minimal-counterexample constraints*, not merely width, module-primality, transitive majority order, or the number of distinguishers.

This is the exact failure boundary carried forward.

## 9. Integrity

No novelty or priority claim is made. No finite census is promoted to proof. No biased induced law is declared uniform. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, public posting, permission bypass, or production-brain mutation was used. No authenticated brain retrieval/context was used, so the run remains `WITHOUT_VERIFIED_BRAIN`.
