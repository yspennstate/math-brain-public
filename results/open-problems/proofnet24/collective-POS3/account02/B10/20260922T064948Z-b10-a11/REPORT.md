# POS3 account02/B10 — first-boundary overload is exact four-channel outward swap defect

**Run:** `20260922T064948Z-b10-a11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose order probability under the uniform law on all full linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability and count below is for the original uniform law on all full linear extensions of the actual poset. No deletion-induced distribution is treated as uniform.

## 1. Exact completed inputs consumed

The newest complete campaign-lead result consumed is

- account04/B10 r15, `proofnet24/collective-POS3/account04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

It proves that the canonical failed-swap charge of a heavy bridge cover leaves the already-exhausted strong-majority interval on one of two outer rays. In the low-endpoint branch more than `2E/11` marked incidence lies on one ray, and one concrete outward Hasse channel gets more than `2E/33` marks. Its first unpaid implication is a ray-return/reuse exclusion.

The named OTHER-account partner result actually consumed is

- account03/B11, `proofnet24/collective-POS3/account03/B11/20260922T061153Z-account03-B11-pos3-r11/REPORT.md`, blob `007674a740f490d5c90b2820dadde4d5ee48de52`.

It gives the exact two-sided transposition defect identity at a heavy cover and the canonical-Hasse-witness reduction, with every failed swap charged to an actual incomparable-pair orientation under the original full-extension law.

The boundary algebra used below is the compatible account03/B10 report

- `proofnet24/collective-POS3/account03/B10/b10-20260922t061504z-r11/REPORT.md`, blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.

For the last exact-two crossed state and its actual first non-exact lower-fringe pair it proves the zero-probability-defect recurrence and, in the same-polarity no-balanced branch, the strict overload

`Omega := K-B = A_prev+3A-E > 0`.

The previous account02/B10 result used for continuity is

- `proofnet24/collective-POS3/account02/B10/20260922T0548Z-b10-pos3-auto11/REPORT.md`, blob `9bc5232277fd7687b1511e555ced92be03c9e4fa`.

It showed that a second canonical blocker in the amplified outer branch carries a `>1/2` sandwich event but that one such superheavy sandwich alone does not force local balance. The remaining mechanism therefore has to couple/transport actual channels rather than infer balance from a single three-point event.

## 2. Boundary state and the hidden exact identity

Use the account03/B10 notation at the last exact-two crossed state. The four distinguished points are `d,x,y,u`, with

- `x || y`;
- `d<y` and `d||x`;
- `x<u` and `u||y`;
- `d,u` are exactly the two relation distinguishers of the pair `(x,y)`.

Let the six full-extension word counts be

`A=N(d y x u)`,
`C=N(d x y u)`,
`X=N(d x u y)`,
`Y=N(x d y u)`,
`Z=N(x d u y)`,
`W=N(x u d y)`.

The exact-two identity gives `C=A`. The inherited transfer gives `Z=K-A`, and the actual first boundary minority is

`B=N(x<d)=Y+Z+W`.

Therefore the account03/B10 overload has the stronger literal word form

`Omega=K-B=A-Y-W`.                                           (2.1)

This already shows that the boundary overload is not an additive correction to the pair probability; it is an imbalance between concrete four-point word classes.

## 3. Exact positional transposition theorem

Let `sigma` exchange the **positions** of `d` and `x` in a full linear extension, leaving every other element in its old position.

### Theorem 3.1 — every `Y` word transposes legally into `C`

For every full extension with distinguished order

`x < d < y < u`,

`σ` is a legal linear extension and has distinguished order

`d < x < y < u`.

#### Proof

Only relations involving an element `q` whose position lies strictly between `x` and `d` can be broken.

First, moving `x` to the right could fail only if `x<q` in the poset. Since `q` occurs before `d<y` in this extension, `y<q` is impossible. Also `q<y` together with `x<q` would imply `x<y`, impossible. Thus `x<q` would make `q` an upper relation distinguisher for `(x,y)`. Exact-two says that the only such point is `u`, but `u` occurs after `y`, not between `x` and `d`. Contradiction.

Second, moving `d` to the left could fail only if `q<d`. Then `q<d<y`, so `q<y`. Because `q` occurs after `x`, one cannot have `q<x`; and `x<q<d` would imply `x<d`, contradicting `d||x`. Hence `q||x`, so `q` is a lower relation distinguisher for `(x,y)`. Exact-two says the only such point is `d` itself, again impossible for an interior `q`.

Therefore no relation is broken. `square`

Since positional transposition is an involution on total orders, Theorem 3.1 implies that exactly `Y` members of the `C` cell transpose legally back into the `Y` cell. Hence the reverse defect set

`D = {L in C : sigma(L) is not a linear extension}`

has exact size

`|D| = C-Y = A-Y = W+Omega`.                                 (3.1)

In particular, at every surviving same-polarity first boundary,

`|D| >= Omega > 0`.                                          (3.2)

This is the missing conversion of the strict boundary overload into actual failed-swap incidence. It uses no projected law and no approximate conditioning.

## 4. Every reverse defect has one of four outward Hasse channels

Take `L in D`. Its distinguished order is

`d < x < y < u`.

Because swapping the positions of `d` and `x` is illegal, some element `q` strictly between those positions causes one of exactly two kinds of failure:

1. `q<x`, so moving `x` before `q` violates a predecessor relation; or
2. `d<q`, so moving `d` after `q` violates a successor relation.

In case 1, follow a saturated chain from `q` to `x` and take its last vertex `r` before `x`. Then

`r lessdot x`, `r||d`, and the full extension contains `d<r<x`.

Indeed, `d<r<x` as a poset chain would imply `d<x`, while `r<d` is impossible because this extension places `d` before `r`.

In case 2, follow a saturated chain from `d` to `q` and take its first vertex `r` after `d`. Then

`d lessdot r`, `r||x`, and the full extension contains `d<r<x`.

Here `r<x` as a poset relation would again imply `d<x`, while `x<r` is impossible because this extension places `r` before `x`.

Thus every defect has a canonical witness in one of the two families

`F_-={r:r lessdot x, r||d}`,
`F_+={r:d lessdot r, r||x}`.                                 (4.1)

Width at most three gives

`|F_-|<=2`, `|F_+|<=2`.                                      (4.2)

For example, three distinct lower covers of `x` belonging to `F_-`, together with `d`, would be a four-element antichain; the upper-cover argument is dual.

Choose any deterministic Hasse witness for each defect. Equations (3.1) and (4.2) imply that one concrete incomparable-pair Hasse channel receives at least

`ceil((W+Omega)/4) >= ceil(Omega/4)`                          (4.3)

marked full extensions.

This improves the first-boundary structural conversion from an unnamed extra distinguisher to **at most four concrete Hasse channels with exact conserved overload weight**.

## 5. No-span branch: all four channels point strictly outward

Now impose the live hypothetical-counterexample branch. The actual boundary pair has

`B=N(x<d)<E/3`,

so `d prec_* x`. Assume, as in the lead's surviving branch, that strict strong-majority span descent inside `(d,x)` has been exhausted.

If `r in F_-`, then `r<x` is forced, hence `r prec_* x`. Since `r||d`, the alternative `d prec_* r prec_* x` would be a strict span descent. Therefore

`r prec_* d prec_* x`,                                       (5.1)

and the marked defect event `d<r` is the minority side of `(d,r)`.

If `r in F_+`, then `d<r` is forced, hence `d prec_* r`. Since `r||x`, the alternative `d prec_* r prec_* x` is again a strict span descent. Therefore

`d prec_* x prec_* r`,                                       (5.2)

and the marked defect event `r<x` is the minority side of `(r,x)`.

So the strict first-boundary overload cannot be absorbed by an interior channel. Every one of its exact failed-swap marks is exported to an actual minority orientation lying strictly to the left of `d` or strictly to the right of `x` in the strong-majority order.

This is the boundary analogue of the lead r15 outer-ray localization, but with a different source quantity: here the conserved source is precisely the first-boundary overload `Omega=K-B`, and the support is at most four Hasse channels.

## 6. One-step return tax: the same marked extensions cannot immediately recycle

The previous statement can be sharpened in a way directly relevant to the lead's ray-return problem.

For `r in F_-`, the old endpoint `x` is an upper relation distinguisher for the new incomparable pair `(r,d)` because `r<x` and `d||x`. For `x` to act as the literal between-endpoints blocker in a direct return step, a full extension must contain

`r < x < d`.

But `r<x` is forced, so this event is **exactly** the old boundary-minority event `x<d`, whose total size is `B`.

For `r in F_+`, the old endpoint `d` is a lower relation distinguisher for the new pair `(x,r)` because `d<r` and `d||x`. A direct return through `d` requires

`x < d < r`,

and because `d<r` is forced this is again exactly the same old boundary-minority event `x<d`, of size `B`.

Hence:

> all canonical immediate returns through the old opposite endpoint, from **any** of the at-most-four outward channels, live in one common reservoir of exactly `B` full extensions.

By contrast every outgoing defect in (3.1) lies in the `C` cell and therefore has `d<x`. The outbound marked set and this direct-return reservoir are disjoint. Thus the boundary overload cannot be recycled at zero cost by reusing the same full extensions; any immediate old-endpoint return must pay fresh mass from the actual boundary minority `B`.

This does **not** yet exclude a longer return through different witnesses, so it is not a proof of global recycler acyclicity. It does remove the simplest same-mark return loophole and identifies the exact return budget rather than a qualitative obstruction.

## 7. Exact finite regression

A deterministic standard-library verifier exhaustively checks every naturally labelled width-at-most-three poset through `n=6`, every exact-two crossed quadruple `(d,x,y,u)`, and the statements that are finite/local consequences of the theorem:

- the six-word partition;
- `C=A` on the exact-two quadruples;
- every `Y -> C` positional transposition is legal;
- the number of reverse `C -> Y` defects is exactly `C-Y`;
- every reverse defect has a Hasse witness in `F_- union F_+`;
- each family has size at most two;
- positive `Omega=A-Y-W` is fully covered by the reverse defect count;
- each canonical direct old-endpoint return event equals the same boundary event `x<d`.

Captured output:

```text
POS3_BOUNDARY_OVERLOAD_FOUR_CHANNEL_CHECK_PASS
n 4 width_le_3_natural_posets 39 exact_two_quadruples 11 positive_overload_cases 0
n 5 width_le_3_natural_posets 314 exact_two_quadruples 198 positive_overload_cases 37
n 6 width_le_3_natural_posets 3339 exact_two_quadruples 2602 positive_overload_cases 969
total_exact_two_quadruples 2811
total_positive_overload_cases 1006
all_failure_counters_zero True
```

Executed-byte SHA-256 values:

- `verify_boundary_overload_four_channel.py`: `59613c79dcc06d632199e69e4b4b13ac33f37d163cea5c9c47057475ff861e5e`;
- `verify_boundary_overload_four_channel.out`: `95fc0412a2366b6979a6a57e8ceae04e70d376ebf3fab0154359f4a24b2fdeb6`.

The finite run is regression evidence only. Theorems 3.1--5.2 and the return-tax statement are symbolic arbitrary-size arguments.

## 8. Conditional end-to-end route and first remaining implication

The live conditional route can now be stated more tightly:

1. the lead heavy-cover mechanism creates exact full-extension defect charge and localizes it to outer strong-order rays;
2. an exact-two corridor transports a conserved integer `K` to its actual first non-exact boundary with zero probability correction;
3. if that boundary remains same-polarity and unbalanced, `Omega=K-B>0`;
4. **proved here:** `Omega` is realized as reverse positional-swap defect incidence on at most four concrete outward Hasse minority channels, with one channel carrying at least `ceil(Omega/4)` marks;
5. **proved here:** a canonical immediate return through the old opposite endpoint cannot reuse those marks and is confined to the common boundary-minority reservoir of exactly `B` extensions;
6. the remaining global obligation is to rule out a longer return using fresh/different witnesses, or show that repeated payment from successive minority reservoirs forces a balanced pair, span descent, a four-antichain, or a proper autonomous/ordinal reduction.

I label that residual

`POS3-RAY-RETURN-FRESH-MASS-v1`.

It is strictly narrower than the previous generic ray-return statement: the first non-exact boundary now has an exact four-channel outward export and an exact one-step return budget.

## 9. Status

- lead r15 outer-ray heavy-cover packet: **CONSUMED/APPLIED**;
- named partner account03/B11 exact transposition/Hasse-defect mechanism: **CONSUMED/APPLIED**;
- account03/B10 zero-defect first-boundary recurrence and overload: **CONSUMED/APPLIED**;
- identity `Omega=A-Y-W`: **DERIVED**;
- legal `Y -> C` position-transposition theorem: **PROVED**;
- reverse-defect identity `|D|=W+Omega`: **PROVED**;
- four-channel width-three Hasse export: **PROVED**;
- no-span outward strong-order localization: **PROVED**;
- common `B`-sized immediate-return reservoir / no same-mark immediate recycling: **PROVED**;
- longer fresh-witness ray return exclusion: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- inherited finite frontier: `n_bal=14` unchanged;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No novelty/priority claim is made. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex calls, remote workflow, public posting, permission change, or native verified-brain activation is used or claimed.
