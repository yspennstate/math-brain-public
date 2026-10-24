# POS3 account03/B11 — exact heavy-gap defect flux and six-channel export

**Run:** `20260922T061153Z-account03-B11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose order probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run implements `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B11 assignment is to use a distinct order-polytope/correlation mechanism to improve the decisive pair-selection statement. The named partner is `account04/B19`. No installation or benchmark work is resumed.

## 1. Exact peer result consumed

The required named OTHER-account result consumed and applied is:

- `account04/B19`, `proofnet24/collective-POS3/account04/B19/B19-20260922T053844Z-pos3/REPORT.md`, blob `504ea477951b9a4eba4bdec84009325c7b511b1a`.

That report proves the following live bridge fact. In the team lead's saturated bridge

`z_0 lessdot z_1 lessdot ... lessdot z_k`

with `a || z_i` for every `i`, the unique heavy transition `x=z_j lessdot y=z_{j+1}` satisfies

`H={x<a<y}`,  `Pr(H)>1/3`,

and at least one relation distinguisher for `(x,a,y)` lies outside the entire bridge. Its first unpaid implication is **OFF-BRIDGE CHARGE REALIZATION**: turn that existence statement, together with the exact heavy-cover flux, into a quantitative packet attached to actual incomparable-pair channels.

The immediately preceding account03/B11 result was `proofnet24/collective-POS3/account03/B11/20260922T044349Z-account03-B11-pos3-r11/REPORT.md`, blob `337b660656cf3df6fc194a4be79b4801bfc99b97`. It produced a different `>1/3` three-point shadow charge in the amplified outer-fringe branch. The present run changes mechanism to an exact two-sided transposition identity at the partner's heavy bridge cover.

## 2. Exact three-state decomposition

Let `P` be any finite poset. Assume

`x lessdot y`,  `a || x`,  `a || y`.

Write `E=e(P)` for the number of linear extensions and partition the extensions according to the relative position of `a` among the forced pair `x<y`:

`A={L:a<x<y}`,  `H={L:x<a<y}`,  `C={L:x<y<a}`.

These three sets are disjoint and exhaustive, so

`|A|+|H|+|C|=E`.                                                (2.1)

For `L in H`, let `T_x(L)` be the total order obtained by exchanging the positions of `a` and `x`. Define

`D_H^-={L in H:T_x(L) is not a linear extension}`,  
`D_A^+={L in A:T_x(L) is not a linear extension}`.

On the complements, `T_x` is an involutive bijection between `H\D_H^-` and `A\D_A^+`. Therefore

`|D_H^-|-|D_A^+|=|H|-|A|`.                                    (2.2)

Likewise exchange the positions of `a` and `y`. With the analogous outgoing and incoming defect sets `D_H^+` and `D_C^-`,

`|D_H^+|-|D_C^-|=|H|-|C|`.                                    (2.3)

Adding (2.2)-(2.3) and using (2.1) gives the exact identity

`|D_H^-|+|D_H^+| = 3|H|-E + |D_A^+|+|D_C^-|`.                 (2.4)

This is an integer identity for the original full linear-extension law. No deletion law, conditioning approximation or unproved correlation property is used.

### Corollary 2.1 — strong-majority excess is conserved as outgoing swap-defect charge

Because `x<y` is forced,

`|H|=N(x<a)+N(a<y)-E`.                                        (2.5)

Define the two integer strong-majority margins

`m_x=3N(x<a)-2E`,  `m_y=3N(a<y)-2E`.

Then

`3|H|-E=m_x+m_y`.                                              (2.6)

Hence, whenever the bridge transition is heavy (`|H|>E/3`),

`|D_H^-|+|D_H^+| >= m_x+m_y = 3|H|-E > 0`.                    (2.7)

Thus the amount by which the two adjacent strong-majority comparisons exceed the `2/3` threshold cannot disappear inside the middle gap: at least their entire integer margin reappears as outgoing failed-swap incidence.

## 3. Every outgoing defect has a canonical Hasse witness

Take `L in H`, so its displayed order contains `x<a<y`.

### Left swap

If swapping `x` and `a` is invalid, some element `q` lying strictly between their positions must satisfy either

- `x<q` in the poset, so moving `x` after `q` breaks that relation; or
- `q<a` in the poset, so moving `a` before `q` breaks that relation.

The two relations cannot hold for the same `q`, because they would imply `x<a` in the poset.

In the first case follow a saturated chain from `x` to `q` and take its first vertex `r`. Then

`x lessdot r`,  `r || a`,  and in this extension `x<r<a`.

In the second case follow a saturated chain from `q` to `a` and take its last vertex `r`. Then

`r lessdot a`,  `r || x`,  and again `x<r<a`.

### Right swap

Dually, if swapping `a` and `y` is invalid, there is a canonical witness `r` with either

`a lessdot r`, `r || y`, `a<r<y` in the extension,

or

`r lessdot y`, `r || a`, `a<r<y` in the extension.

These witnesses are Hasse-adjacent to one of the three distinguished vertices; no long noncanonical relation is needed.

## 4. Width three compresses all exported charge to at most six pair channels

Now assume `width(P)<=3`. Define the four canonical witness families

`F1={r: x lessdot r, r||a, r!=y}`,  
`F2={r: r lessdot a, r||x}`,  
`F3={r: a lessdot r, r||y}`,  
`F4={r: r lessdot y, r||a, r!=x}`.

They satisfy the sharp structural bounds needed here:

`|F1|<=1`, `|F2|<=2`, `|F3|<=2`, `|F4|<=1`.                   (4.1)

Indeed, distinct covers of the same endpoint are pairwise incomparable. If `F1` contained two vertices, those two together with `y` and `a` would form a four-element antichain. The `F4` argument is dual. Three members of `F2`, together with `x`, would be a four-antichain; three members of `F3`, together with `y`, would be a four-antichain.

Consequently there are at most six canonical vertices to which every outgoing defect incidence can be assigned. The associated **actual incomparable-pair order events** are

- `F1`: `r<a` for the pair `r||a`;
- `F2`: `x<r` for the pair `x||r`;
- `F3`: `r<y` for the pair `r||y`;
- `F4`: `a<r` for the pair `a||r`.

Choose a deterministic canonical witness for every outgoing defect incidence. From (2.7), one of at most six concrete incomparable-pair orientation events then receives at least

`ceil((m_x+m_y)/6)`                                             (4.2)

marked full extensions. This is a genuine transfer from the abstract heavy-gap excess to actual pair-order mass.

### Bridge specialization

In the partner's saturated bridge, every bridge vertex below `x` precedes `x` in every extension and every bridge vertex above `y` follows `y`. Since `x lessdot y`, no other bridge vertex can lie between `x` and `a`, or between `a` and `y`, in an extension belonging to `H`.

Therefore **every canonical witness supporting an outgoing defect in (2.4) is off the entire bridge**. The partner's qualitative off-bridge witness theorem is thus strengthened to a quantitative exact statement:

> the heavy bridge exports at least `m_x+m_y=3|H|-E` failed-swap incidences to at most six concrete off-bridge incomparable-pair channels.

This is the first part of the requested off-bridge charge realization.

## 5. No-span branch: the exported charge lands on minority orientations

Assume, as in the surviving minimal-counterexample branch, that there is no strong-majority span descent inside either interval `x prec_* a` or `a prec_* y`.

Then each defect orientation above is the **minority** side of its corresponding pair:

- if `r in F1`, `x<r` forces `x prec_* r`; no descent forces `a prec_* r`, so the defect event `r<a` is minority;
- if `r in F2`, `r<a` forces `r prec_* a`; no descent forces `r prec_* x`, so `x<r` is minority;
- if `r in F3`, `a<r` forces `a prec_* r`; no descent forces `y prec_* r`, so `r<y` is minority;
- if `r in F4`, `r<y` forces `r prec_* y`; no descent forces `r prec_* a`, so `a<r` is minority.

Hence the heavy cover does not merely create an off-bridge relation witness. It **exports its entire `2/3`-margin excess into minority-order mass of at most six specific off-bridge incomparable pairs**. This supplies an exact capacity/charging object for the repeated-corridor argument.

## 6. Exact calibration: why this is not yet the full theorem

The export bound alone cannot be promoted to a balanced pair. Consider the five-element poset with relations

`0<2`, `0<3`, `1<2`,

and no others. Take `x=0`, `y=3`, `a=4`. The poset has exactly `E=25` linear extensions, and

`|A|=7`, `|H|=9`, `|C|=9`.

Thus `|H|=9/25>1/3` and

`3|H|-E=27-25=2`.

There is one outgoing canonical channel, `r=2 in F1`. Exact swap counts are

`|D_H^-|=2`, `|D_A^+|=|D_H^+|=|D_C^-|=0`,

so (2.4) is tight. But the associated defect orientation itself is still extreme:

`N(2<4)=7`, hence `Pr(2<4)=7/25<1/3`.

The full poset contains other balanced pairs, so this is not a POS3 counterexample. It shows exactly why the next theorem must use repeated-corridor conservation or structural descent rather than the false inference “positive exported defect mass immediately gives a balanced witness pair.”

## 7. Deterministic verification

`verify_heavy_gap_defect_flux.py`, blob `1d6db358091d611acda726da1816c25233a0a611`, exhaustively checks every naturally labelled width-at-most-three poset through `n=6`, every cover `x lessdot y`, and every `a` incomparable with both endpoints. It verifies:

1. the exact identity (2.4);
2. existence of a canonical Hasse witness for every outgoing defect;
3. the family bounds `(1,2,2,1)` from (4.1);
4. the exact five-point calibration above.

Captured output, blob `41f67ca249638e4d52e42a84751579d1956628d0`, reports:

- `3699` naturally labelled width-at-most-three posets checked for `3<=n<=6`;
- `24996` cover/incomparable triples checked;
- `14033` heavy triples with `3|H|>E`;
- zero assertion failures;
- final marker `POS3_HEAVY_GAP_DEFECT_FLUX_CHECK_PASS`.

The finite verification is regression evidence for the symbolic argument, not a finite proof of POS3.

## 8. Remaining first implication

The first unpaid implication is now strictly narrower than the partner's existence statement:

> **MINORITY-CAPACITY PROPAGATION.** Along a maximal repeated exact-two / heavy-cover corridor in a cardinality-minimal width-three counterexample, prove that the conserved strong-majority margin exported by successive heavy covers cannot be absorbed indefinitely by fresh minority sides of the at-most-six canonical off-bridge channels at each cover. It must instead force an actual pair into `[1/3,2/3]`, strict strong-majority span descent, a proper autonomous/ordinal reduction, or the already isolated multi-distinguisher/non-crossed exit with an exact conserved charge.

The exact quantity to propagate is no longer an unnamed relation witness: it is the integer defect flux in (2.4), with source margin `m_x+m_y` and a canonical map to actual off-bridge incomparable-pair minority events.

## 9. Status and integrity

- named partner account04/B19 off-bridge witness theorem: **CONSUMED/APPLIED**;
- exact two-sided transposition defect identity: **PROVED**;
- strong-majority margin conservation `m_x+m_y`: **PROVED**;
- outgoing defects admit canonical Hasse witnesses: **PROVED**;
- width-three compression to at most six concrete pair channels: **PROVED**;
- in the no-span branch those channels receive minority-order mass: **PROVED**;
- immediate balanced-pair inference from one heavy cover: **REFUTED by exact five-point calibration**;
- full POS3 target: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex calls, remote workflows, public posting, permission changes, or native brain activation are used or claimed.
