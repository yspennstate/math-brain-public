# POS3 account03/B11 — inward-fringe suppression and F2/F3 cross-support funnel

**Run:** `20260922T074511Z-b11-pos3-r11c`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all full linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and multiplicities below are for the original uniform law on the full linear extensions of the actual poset. No deletion-induced law is treated as uniform.

## 1. Fresh source-bound state consumed

The active owner programme is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B11 assignment is the distinct order-polytope/correlation route, with designated partner `account04/B19`.

The required named OTHER-account result consumed is the latest complete partner result:

- account04/B19 run `B19-20260922T071535Z-r46`,
- canonical report `proofnet24/collective-POS3/account04/B19/B19-20260922T071535Z-r46/REPORT.md`,
- report blob `26c2eab1c40a8da73357764efd0aab4160391e07`.

That result eliminates high `F1` and high `F4` same-ray recycling with a retained `2/33` packet. Its surviving low-endpoint state is therefore forced to selected types

`l := r_L in F2`, `r := r_R in F3`

with Hasse chain

`l lessdot a lessdot r`

and the heavy cover

`x lessdot y`,

together with

`a||x,y`, `l||x`, `r||y`

and strong-majority order

`l prec_* x prec_* a prec_* y prec_* r`.

The selected boundary minorities `{x<l}` and `{r<y}` retain the partner's positive packet scale, and the total assigned `F2` and `F3` masses are each `>4E/33`. The partner labels the first unpaid implication `F2/F3 DISCREPANCY-CHAIN TRANSPORT`.

I also use the already established account03/B11 exact two-distinguisher sign theorem, report blob `e6cf43b104d7d072d21362a4af2c21739c703506`: an extreme incomparable pair with exactly two distinguishers cannot have opposite signs.

## 2. New arbitrary-size exact-fiber theorem

The useful missing local fact is not another cross-anchor positive-correlation assertion. The partner stream has already shown that unconditional cross-anchor PQD is false. Instead, retain the exact deletion fibers and exploit the geometry forced when an extreme pair has exactly two **positive crossed distinguishers**.

### Theorem 2.1 — inward-fringe suppression

Let `p||q` in any finite poset. Suppose the only two vertices distinguishing `p` from `q` are `d,u`, with

`d<q`, `d||p`, `p<u`, `u||q`.

Thus `d` is a positive lower distinguisher and `u` a positive upper distinguisher relative to the orientation `p<q`.

Then, under the uniform law on all full linear extensions,

`Pr(p<d) <= 1/2`,                                            (2.1)

and

`Pr(u<q) <= 1/2`.                                            (2.2)

No width assumption is needed.

### Proof

Delete the four distinguished vertices and put

`R=P\{p,q,d,u}`.

Fix an arbitrary `tau in L(R)`. Because `d,u` are the **only** distinguishers of `p,q`, every vertex of `R` has the same three-valued relation to `p` as to `q`. Hence the exact admissible external-gap intervals of `p,q` in the fixed skeleton `tau` coincide:

`I_p=I_q=I=[L,U]`.

Since `d<q`,

`Pred_R(d) subseteq Pred_R(q)` and `Succ_R(q) subseteq Succ_R(d)`,

so the admissible interval `I_d` is weakly left-shifted from `I`:

`L_d <= L`, `U_d <= U`.

Similarly `p<u` gives

`L_u >= L`, `U_u >= U`,

so `I_u` is weakly right-shifted from `I`.

The relation `u<d` is impossible: it would imply `p<u<d<q`, contradicting `p||q`. Hence either `d||u` or `d<u`.

For a fixed special-element word, its exact multiplicity over `tau` is the number of weakly increasing external-gap assignments respecting the four exact intervals. Equal-gap letters are ordered by the displayed word. This is a bijective encoding of all lifts of `tau`.

#### Case 1: `d||u`

The six legal special words are

`w1 = p d q u`,
`w2 = p d u q`,
`w3 = p u d q`,
`w4 = d p q u`,
`w5 = d p u q`,
`w6 = d q p u`.

Write `n_i=N_tau(w_i)`.

Because `d` is weakly left-shifted from `p`, swapping the adjacent labels `p,d` while leaving their two numerical gaps fixed gives injections

`w1 -> w4`, `w2 -> w5`,

hence

`n1<=n4`, `n2<=n5`.                                          (2.3)

Because `u` is weakly right-shifted from `q`, the analogous adjacent injections give

`w2 -> w1`, `w5 -> w4`,

so

`n2<=n1`, `n5<=n4`.                                          (2.4)

There is one non-adjacent crossing word. Take any admissible gap assignment for

`w3 = p u d q`

and denote its weakly increasing gaps by

`g1<=g2<=g3<=g4`.

Keep the four numbers fixed and relabel them as

`d q p u`.

This is admissible: `g1` lies in `I_d` because `g1 in I` and `g1<=g3 in I_d`; `g2` lies in `I` because `g2 in I_u`, `g2<=g3<=U_d<=U`; `g3` lies in `I` because `g3>=g2>=L_u>=L`; and `g4` lies in `I_u` because `g4 in I`, `g4>=g2>=L_u`, and `U_u>=U`. The numerical gap sequence determines the original assignment, so this is injective:

`n3<=n6`.                                                     (2.5)

Now

`N_tau(p<d)=n1+n2+n3 <= n4+n5+n6=N_tau(d<p)`

by (2.3) and (2.5). Likewise

`N_tau(u<q)=n2+n3+n5 <= n1+n6+n4=N_tau(q<u)`

by (2.4) and (2.5).

#### Case 2: `d<u`

The word `p u d q` is forbidden, while the other five words above remain legal. The adjacent injections alone give

`N_tau(p<d)=n1+n2 <= n4+n5 <= N_tau(d<p)`

and

`N_tau(u<q)=n2+n5 <= n1+n4 <= N_tau(q<u)`.

Thus both inequalities hold separately in every exact deletion skeleton `tau`. Summing the integer inequalities over all `tau in L(R)` proves (2.1)-(2.2) under the original full uniform law. `square`

## 3. Calibration: this does not forbid an extreme endpoint pair

The exact-two positive crossed configuration can still support a very extreme `p,q` pair. In the five-element poset generated by

`0<2`, `0<4`, `1<4`,

the pair `(p,q)=(1,2)` has exactly the positive lower/upper distinguishers

`d=0`, `u=4`.

There are exactly `25` linear extensions and

`N(p<q)=20`,
`N(p<d)=10`,
`N(u<q)=10`.

Thus `Pr(p<q)=4/5`, while both inward fringes equal `2/5`. The theorem isolates the feature needed by the current F2/F3 state: **an exact-two crossed pair cannot simultaneously have a strongly inward lower or upper fringe.**

## 4. Application to the partner's F2/F3 discrepancy chain

Retain the partner notation from Section 1.

### Corollary 4.1 — left cross incomparability forces a fresh distinguisher

Assume `l||y`.

For the cross pair `(p,q)=(l,y)`, the two central vertices

`d=x`, `u=a`

are positive crossed distinguishers:

`x<y`, `x||l`, `l<a`, `a||y`,

and `x||a`.

If these were the only distinguishers of `l,y`, Theorem 2.1 would give

`Pr(l<x)<=1/2`.

But the live strong-majority order has

`l prec_* x`,

hence `Pr(l<x)>2/3`. Contradiction.

Therefore `l||y` forces at least one additional relation distinguisher of the cross pair `l,y` outside `{x,a}`.

### Corollary 4.2 — right cross incomparability forces a fresh distinguisher

Assume `x||r`.

Apply Theorem 2.1 to `(p,q)=(x,r)` with

`d=a`, `u=y`.

Indeed

`a<r`, `a||x`, `x<y`, `y||r`,

and `a||y`.

If these were the only distinguishers, Theorem 2.1 would give

`Pr(y<r)<=1/2`,

contradicting `y prec_* r` and hence `Pr(y<r)>2/3`.

Thus `x||r` forces at least one additional relation distinguisher of `x,r` outside `{a,y}`.

### Corollary 4.3 — support-free F2/F3 state is a fully crossed bridge

If neither fresh cross-distinguisher exit from Corollaries 4.1-4.2 is taken, then both cross pairs are comparable. Their orientations are forced:

- `y<l` would imply `y<l<a`, contradicting `a||y`, so `l<y`;
- `r<x` would imply `a<r<x`, contradicting `a||x`, so `x<r`.

Hence the only cross-support-free central five-point configuration is

`l<a<r`,
`x<y`,
`l<y`,
`x<r`,

with `l||x`, `a||x,y`, `r||y`.

In particular the formerly generic opposite-ray F2/F3 recycler has collapsed to the **fully crossed bridge** unless it emits a genuinely new relation distinguisher.

This reduction does not use cross-anchor PQD and does not assume any projected/deletion law is uniform.

## 5. Charged-side consequence in a no-balanced counterexample

The central five-point fully crossed bridge has exactly one central-core distinguisher of the charged side pair `l||x`, namely `a`; the vertices `y,r` lie above both `l,x` and therefore do not distinguish them. Dually, `a` is the only central-core distinguisher of the charged side pair `y||r`.

The already established account02/B10 one-distinguisher balance theorem (`proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`) therefore implies that in a hypothetical no-balanced counterexample the fully crossed bridge must acquire external support on **both** charged sides. If a charged side has exactly one additional distinguisher, the account03/B11 sign theorem forces it to have the same positive sign as the central witness `a`; otherwise that charged side is balanced.

So the surviving F2/F3 state is no longer an arbitrary opposite-ray discrepancy chain. It is one of:

1. a fresh cross-pair distinguisher exits the five-point core;
2. one charged side already has at least three distinguishers;
3. the rigid fully crossed bridge carries coherent positive external support on both charged sides.

The original `>2/33` selected side packets are not discarded by this structural reduction.

## 6. Exact regression

The companion standard-library verifier has two independent components.

1. It checks `8,844` exact interval-fiber instances, including both `d||u` and `d<u`, and verifies the two fiber inequalities in Theorem 2.1.
2. It exhausts all `5,230` distinct transitive closures of naturally labelled posets through `n=6`, scans `86,340` ordered incomparable pairs, and finds `3,951` exact-two positive lower/upper crossed configurations. Every one satisfies both global inequalities.

Recorded output:

```text
fiber_instances 8844
posets 5230
ordered_incomparable_pairs 86340
crossed_exact_two_cases 3951
cases_by_n {2: 0, 3: 0, 4: 11, 5: 198, 6: 3742}
POS3_INWARD_FRINGE_SUPPRESSION_CHECK_PASS
```

The finite verifier is regression evidence only. The arbitrary-size theorem is the exact fiber proof in Section 2.

## 7. Revised first unpaid implication

The partner's `F2/F3 DISCREPANCY-CHAIN TRANSPORT` is now reduced to a more rigid target:

> **FULLY-CROSSED DOUBLE-SUPPORT TRANSPORT.** In the branch with
> `l<a<r`, `x<y`, `l<y`, `x<r`,
> `l||x`, `a||x,y`, `r||y`,
> and coherent external positive support on the two charged side pairs,
> use width three plus the heavy-slice/path structure to force balance, strict strong-majority span descent, a proper autonomous/ordinal reduction, or transfer into an already controlled exact-two/non-crossed charged corridor.

Any failure of either cross comparability has already been converted above into a genuinely fresh cross-pair distinguisher. The parent POS3 theorem remains open.

## 8. Integrity/status

- fresh owner control and exact assignment: consumed;
- named partner account04/B19 r46: **CONSUMED/APPLIED**;
- new inward-fringe suppression theorem: **PROVED**, arbitrary finite size;
- F2/F3 cross-support funnel: **PROVED**;
- fully crossed double-support transport: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**;
- execution context: **`WITHOUT_VERIFIED_BRAIN`**.

No scheduler repair, extra task creation, cross-account native action, email/Drive/public/workflow dispatch, paid model/API/Codex use, credential access, or unrelated private transcript access occurred.
