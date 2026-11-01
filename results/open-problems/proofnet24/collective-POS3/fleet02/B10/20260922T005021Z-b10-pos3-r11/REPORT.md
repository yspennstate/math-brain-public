# POS3 fleet02/B10 — exact two-deletion reflection coupling with retained conditioning weights

**Run:** `20260922T005021Z-b10-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** OPEN / NOT PROVED.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Model self-report:** GPT-5.6 Sol. Requested effort: maximum actually supported. Configured/self-reported effort: UNKNOWN. Provider reasoning tokens/time: NOT EXPOSED.

## 1. Control and source state

Fresh owner control is revision `2026-09-22.2` under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`: B10 is POS3 research and new installation/benchmark work is stopped.

The assigned campaign-lead scientific root `proofnet24/collective-POS3/fleet04/B10/` was still absent at the checked canonical-research snapshot, so no lead theorem was fabricated. I therefore used the freshest complete named-partner result actually present:

- fleet03/B11, `20260922T003936Z-fleet03-B11-pos3-r11/REPORT.md`, blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d`.

That report proves the exact order-polytope swap-defect identity and, in a hypothetical POS3 counterexample, the double-canonical-blocker certificate at every adjacent strong-majority chain-block boundary. At the first block boundary `(x,y)`, there are no positive predecessor blockers and exactly two minimal positive successor blockers, in distinct later blocks.

I also consumed and applied the completed OTHER-account result:

- fleet01/B19, `20260922T004631Z-b19-pos3-r11/REPORT.md`, blob `c2f771152d5be6943cce6872c500ca81c572e962`.

Its arbitrary-deleted-chain recurrence proves a midpoint-reflection/short-gap formula for adjacent swaps while retaining the exact nonuniform lift multiplicities, and proves that only nested chain profiles can have context-dependent sign. The present result is the pair-deletion dual: instead of deleting one chain and comparing adjacent orders of two outside elements, delete the two candidate elements and compare their exact simultaneous insertion fibers.

## 2. Compact conditional end-to-end route

Assume a POS3 counterexample `P`. The strong-majority relation on incomparable pairs is a transitive total order extending `P`; partition it into maximal comparable chain blocks. Take an adjacent block boundary `(x,y)` with `x` immediately before `y` in that strong-majority order. Then `p_xy>2/3`.

By the named-partner double-blocker theorem, every such boundary has at least two canonical positive blockers. At the first block boundary there are exactly two minimal successor blockers `s,t` and no predecessor positive blocker.

The new theorem below rewrites the true uniform linear-extension law as an exact size-biased mixture over `P\{x,y}`. Inside each deletion fiber, a reflection coupling gives the sign and exact magnitude of the `x/y` bias from the two admissible insertion intervals. At the first boundary, every positively biased fiber is routed canonically and disjointly to the earliest of the two successor blockers `s,t`.

Thus a full proof would follow from the still-unproved global implication:

> Along the consecutive strong-majority block boundaries of a width-three counterexample, the disjoint routed positive center-flow cannot exceed the opposing center-flow by more than `e(P)/3` at every boundary unless some incomparable pair is already balanced.

The local one-boundary version of this statement is false; Section 7 gives an exact width-three counterexample to that stronger shortcut. Hence the remaining implication must genuinely couple multiple boundaries (or equivalently the nested-profile defects seen by fleet01/B19).

## 3. Exact two-deletion fiber law

Let `x||y` in any finite poset `P`, set `Q=P\{x,y}`, and fix a linear extension

`tau=(q_1,...,q_m)` of `Q`.

For `z in {x,y}`, define its admissible insertion-gap interval in `tau` by

`L_z(tau)=max({pos_tau(a): a<z} union {0})`

and

`R_z(tau)=min({pos_tau(b)-1: z<b} union {m})`.

Write

`I_z(tau)=[L_z,R_z] subset {0,...,m}`.

These intervals are nonempty.

For `i in I_x`, `j in I_y`:
- if `i<j`, there is exactly one lift of `tau` with `x<y`;
- if `i>j`, there is exactly one lift with `y<x`;
- if `i=j`, there are exactly two lifts, one in each order.

Therefore, with `C_tau=|I_x cap I_y|`,

`T_tau = |I_x||I_y| + C_tau`

is the exact number of full linear extensions restricting to `tau`, while

`N_xy(tau)=#{(i,j): i<j}+C_tau`,

`N_yx(tau)=#{(i,j): i>j}+C_tau`.

Set

`Delta_tau=N_xy(tau)-N_yx(tau)=#{i<j}-#{i>j}`.

Summing over `tau in L(Q)` gives

`e(P)=sum_tau T_tau`,

`e_xy-e_yx=sum_tau Delta_tau`,

and hence

`p_xy = 1/2 + (sum_tau Delta_tau)/(2 sum_tau T_tau)`.      (3.1)

This displays the exact conditioning law:

`mu(tau)=T_tau/e(P)`.

It is generally **not** uniform on `L(Q)`. Every conclusion below retains this size bias.

## 4. Reflection coupling and exact center-strip identity

Put

`H_tau=(L_y+R_y)-(L_x+R_x)`.

Reflect the insertion pair `(i,j)` by

`R(i,j)=(L_x+R_x-i, L_y+R_y-j)`.

This is an involution of `I_x x I_y`. If `d=j-i`, then after reflection

`d'=H_tau-d`.

### Theorem 4.1

If `H_tau>0`, then

`Delta_tau = #{(i,j) in I_x x I_y : 1 <= j-i <= H_tau}`.      (4.1)

If `H_tau=0`, then `Delta_tau=0`.

If `H_tau<0`, then

`Delta_tau = -#{(i,j) in I_x x I_y : H_tau <= j-i <= -1}`.    (4.2)

In particular,

`sign(Delta_tau)=sign(H_tau)`.

### Proof

Assume `H_tau>0`. Reflection bijects every reverse pair `d<0` with a forward pair having `d'=H_tau-d>H_tau`; conversely every forward pair with `d>H_tau` reflects to a reverse pair. These cancel in the signed count `#{d>0}-#{d<0}`. The uncancelled pairs are exactly `1<=d<=H_tau`, proving (4.1). The case `H_tau=0` is exact cancellation. The case `H_tau<0` is the symmetric argument. `□`

This is the pair-deletion analogue of fleet01/B19's arbitrary-chain midpoint-reflection formula.

A useful probabilistic corollary follows immediately from (3.1). Since `Delta_tau/T_tau<=1` on positive-center fibers and is nonpositive otherwise,

`p_xy>2/3  =>  mu{tau:H_tau>0}>1/3`.                         (4.3)

So a strong majority cannot be inferred from a uniform sample of deletion skeletons; it forces positive insertion-center displacement on more than one third of the **correct size-biased deletion-fiber mass**.

## 5. Application to the named partner's first-boundary pair

Let `(x,y)` be the first chain-block boundary in a hypothetical counterexample and let `s,t` be the exact two canonical minimal successor blockers supplied by fleet03/B11.

Because there is no positive predecessor blocker,

`D(y) subseteq D(x)`.

Indeed, if `a<y`, then `a` is comparable with `x`; the alternative `x<a<y` would force `x<y`, impossible, hence `a<x`. Thus in every deletion skeleton

`L_y <= L_x`.                                                (5.1)

Consequently `H_tau>0` forces `R_y>R_x`. Let `b(tau)` be the first element of `tau` that is above `x` but not above `y`. Then:
1. `b(tau)` occurs exactly at Q-position `R_x+1`;
2. `b(tau)||y`, so it is a successor blocker;
3. if it were not minimal among successor blockers, a smaller blocker would have appeared earlier in `tau`.

Therefore, on every positive-center fiber,

`b(tau) in {s,t}`.                                           (5.2)

This gives a **disjoint**, exact routing of positive center-flow. Define

`Phi_s=sum_{H_tau>0, b(tau)=s} Delta_tau`,
`Phi_t=sum_{H_tau>0, b(tau)=t} Delta_tau`,
`Psi=sum_{H_tau<0} (-Delta_tau)`.

Then

`e_xy-e_yx = Phi_s+Phi_t-Psi`.                               (5.3)

Since `p_xy>2/3`,

`Phi_s+Phi_t > e(P)/3 + Psi`,                                (5.4)

so one of the two blocker channels satisfies

`Phi_b > e(P)/6 + Psi/2`.                                    (5.5)

No union bound, no re-uniformization of `P\{x,y}`, and no dropped conditioning factor occurs in (5.3)-(5.5).

A parallel mass-only statement from (4.3) is that under the exact induced deletion-skeleton law `mu`, the two blocker channels partition a set of mass `>1/3`; hence one blocker is the earliest positive ceiling on `mu`-mass `>1/6`.

## 6. Canonical blocker reciprocity

The double-blocker geometry also propagates outward.

### Lemma 6.1

If `s` is a minimal successor blocker for `(x,y)`, i.e.

`s in Min{z:x<z, z||y}`,

then `x` is a maximal predecessor blocker for `(y,s)`:

`x in Max{z:z<s, z||y}`.

### Proof

Certainly `x<s` and `x||y`. If `x<z<s` with `z||y`, then `z` is itself a successor blocker for `(x,y)` strictly below `s`, contradicting minimality of `s`. `□`

The dual statement is also true: if `m` is a maximal predecessor blocker for `(x,y)`, then `y` is a minimal successor blocker for `(m,x)`.

Thus the routed channels in Section 5 are not isolated labels: each endpoint blocker canonically reappears as a blocker for an outward incomparable pair. This is the natural bridge to a multi-boundary cancellation argument.

## 7. A local closure shortcut is false

The following exact width-three poset shows that the endpoint fork by itself does not force a balanced pair among the four local vertices.

Take vertices `0,...,6` with Hasse covers

`0<1`, `1<3`, `0<5`, `4<5`, `3<6`, `4<6`.

Let

`x=4`, `y=2`, `s=5`, `t=6`.

The poset has width `3` and exactly `91` linear extensions. For `(x,y)` there are no predecessor positive blockers, while the canonical minimal successor blockers are exactly `{5,6}`.

Exact counts are

`#(x<y)=62`,
`#(y<s)=62`,
`#(y<t)=74`,
`#(s<t)=63`.

Thus

`Pr(x<y)=62/91>2/3`,
`Pr(y<s)=62/91>2/3`,
`Pr(y<t)=74/91>2/3`,
`Pr(s<t)=63/91=9/13>2/3`.

So the complete local order `x<*y<*s<*t` can be strongly biased while retaining the exact two-canonical-successor-blocker endpoint geometry.

This is **not** a counterexample to POS3. For example,

`Pr(1<2)=55/91`,

which is balanced. It refutes only the tempting strengthening that the one-boundary four-vertex fork alone must already contain a balanced pair. The global multi-boundary structure is essential.

The companion exact verifier checks the width, all 91 extensions, canonical blockers, these pair counts, the two-deletion fiber sums, and Theorem 4.1 on every deletion skeleton. Its terminal line is

`POS3_TWO_DELETION_COUPLING_CHECK_PASS`.

For the displayed pair it obtains

`sum T_tau=91`, `sum N_xy=62`, `sum N_yx=29`, `sum Delta_tau=33`,

with positive routed defect masses `{5:25, 6:8}`.

## 8. What moved and what remains

**Moved:** the pair-selection candidate now has an exact two-deletion coupling that preserves every conditioning multiplicity; each deletion fiber's bias is controlled by the relative midpoint of the two admissible insertion intervals. At the partner's first boundary, positive fibers route disjointly to the two canonical successor blockers, with the quantitative flow inequalities (5.3)-(5.5). Blocker reciprocity identifies how those channels can propagate to outward incomparable pairs.

**Refuted subroute:** a proof based only on the first-boundary four-vertex fork is impossible; the seven-element width-three witness in Section 7 satisfies the entire local strong-order pattern.

**First essential missing implication:** prove a global conservation/cancellation rule for the routed blocker channels across consecutive strong-majority block boundaries (or equivalently across the nested-profile defects in fleet01/B19's chain-deletion recurrence). The rule must retain the exact fiber weights and must force a balanced pair once the net signed bias at every boundary is assumed to exceed `e(P)/3`.

No claim of a full POS3 proof is made.
