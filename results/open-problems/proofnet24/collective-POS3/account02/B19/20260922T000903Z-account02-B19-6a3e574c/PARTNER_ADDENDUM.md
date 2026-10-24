# POS3 account02/B19 — partner uptake: the heavy-marginal + pinned-atom system is not yet contradictory

**Outcome:** `CANDIDATE_REFUTED` for the sufficiency of the current numerical constraint package; parent POS3 remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This addendum is immutable follow-on mathematics to the earlier same-run asymmetric-chain/product/ordinal-sum report. It was required because the named partner `account03/B10` published a complete source-bound result after my first research snapshot.

## 1. Named partner result consumed exactly

I consumed `account03/B10`, commit

`a17c424f497e0adbd4307e5e556d40087fdf39b1`,

report blob

`388ac28e375df4e7a49f72ffbf540f362e03696e`,

at

`proofnet24/collective-POS3/account03/B10/account03-B10-20260922T001407Z-pos3-r11/REPORT.md`.

The partner proves a new necessary condition for a hypothetical width-three counterexample. Let `L_*` be its transitive strong-majority order. For each element `x`, the probability that `x` occurs at its `L_*` rank is at least

`3^(-9)=1/19683`.

In the exact account01/B10 three-chain flux notation, if `g_b(x),g_c(x)` are the two other-chain gaps prescribed by `L_*`, then the refined joint cell satisfies

`W_x(g_b(x),g_c(x)) >= E/19683`.                                      (P)

Together with the account01/B10 heavy-slice normal form, every relevant row or column through the prescribed gap has mass `>E/3`. The partner proposes combining those aligned heavy marginals, the pinned cell (P), connected incomparability, and the inherited at-least-five majority blocks via a global conservation argument.

I tested the strongest natural reading of that implication immediately.

## 2. Exact 15-element width-three adversary to sufficiency of those constraints

Consider the poset `P` on `0,...,14` with three fixed chains

`A=(0<1<2<3<4)`,

`B=(5<6<7<8<9)`,

`C=(10<11<12<13<14)`,

and Hasse covers

```text
0<5,
1<2, 1<7,
2<3, 2<12,
3<4, 3<9,
5<1, 5<6, 5<11,
6<2, 6<7,
7<4, 7<8,
8<9,
9<14,
10<1, 10<11,
11<12,
12<8, 12<13,
13<4, 13<14.
```

The deterministic exact checker verifies:

- width exactly three (the displayed three-chain cover gives `<=3`, while `(1,6,11)` is an antichain);
- connected incomparability graph;
- exactly `E=4477` linear extensions;
- exactly `43` legal ideal states in the three-chain prefix lattice;
- exactly `21` incomparable unordered pairs.

Now take the common total order

`L = (0,10,5,6,1,11,2,7,12,3,13,8,9,4,14)`.

It is a linear extension. Its chain-label word is

`ACBBACABCACBBAC`,

with **13 maximal chain-label blocks**, comfortably above the inherited five-block lower bound.

## 3. Every partner heavy marginal is aligned, uniquely, with this one order

For every ordered pair `(x,C_b)` for which `C_b` contains an element incomparable with `x`, let `g_b(x)` be the number of elements of `C_b` preceding `x` in `L`. There are 27 such relevant marginals.

The exact edge-flux computation verifies that in **all 27** cases:

1. the unique largest insertion slice occurs at exactly `g_b(x)`;
2. that slice has mass strictly larger than `E/3`.

The smallest of these 27 aligned heavy fractions is already

`1591/4477 = 43/121 > 1/3`,

for `x=11` against chain `A`, whose full slice vector is

`(0,1360,1591,1183,343,0)`.

Thus not only does every relevant distribution contain a heavy slice; the heavy slice is uniquely aligned at the gap of **one common total order**.

## 4. Every partner pinned central cell also holds, by a very large margin

For each `x`, refine to the two other-chain coordinates and take the joint cell prescribed by `L`. All 15 cells satisfy the partner inequality (P).

The smallest cell is

`855/4477`

for `x=3` at state `(3,3,3)`. In particular

`855/4477 > 1/19683`.

The remaining exact central masses are archived in the executed output. Thus the new Aires–Kahn-derived pinned-rank constraint is fully present in this example; the example does **not** refute the partner lemma.

## 5. The common order is even strong-majority compatible wherever no balanced pair intervenes

Of the 21 incomparable pairs, exactly seven are balanced:

```text
(1,6)   1977/4477,
(2,11)  1526/4477,
(3,12)  1549/4477,
(4,9)   1569/4477,
(5,10)  1841/4477,
(7,12)  249/407,
(8,13)  2155/4477.
```

For **each of the other 14 incomparable pairs**, `L` orients the pair in the direction having probability `>2/3`. The weakest such oriented probability is

`3023/4477 > 2/3`.

So `L` is not merely an arbitrary common gap order: it is a completion compatible with every strict strong-majority comparison that exists in this example. What prevents it from being the strong-majority total order of a counterexample are precisely the seven balanced pairs.

This makes the obstruction sharp: connectedness, width three, size 15, at least five blocks, common-order aligned `>E/3` heavy marginals, the partner's `>=E/19683` pinned atoms, and compatibility with all already-strong pair orientations can all hold simultaneously.

## 6. What is refuted and what survives

The following proposed implication is false:

> connected width three + at least five common-order blocks + all relevant common-gap marginals `>E/3` + every common-gap central cell `>=E/19683` forces a contradiction.

The poset above satisfies every premise and has seven balanced pairs instead of a contradiction.

This does **not** refute either exact necessary theorem already proved:

- account01/B10's heavy-slice normal form for an actual counterexample;
- account03/B10's pinned majority-rank atom lemma.

It refutes only the idea that those numerical constraints, even when aligned to one majority-compatible completion, are by themselves sufficient to close POS3.

The first essential missing implication is therefore sharper than the partner report's numerical package: a proof must use the **band-avoidance information at every incomparable cut**—in a true counterexample each such cumulative probability lies strictly below `1/3` or strictly above `2/3`—in a way that couples the cuts globally across chains. The present example shows that row/column peak alignment, central atom lower bounds, and block count do not encode that missing information.

A promising exact next variable is not the maximum slice but the signed deficit/excess of each incomparable cumulative cut relative to the two band boundaries, summed across consecutive boundaries of the common order. Any successful conservation identity must distinguish the seven balanced cuts above from an all-band-avoiding configuration.

## 7. Exact executable certificate

The standard-library checker

`verify_partner_constraints_adversary.py`

reconstructs the transitive closure and exact ideal-prefix state lattice, computes forward/backward path counts, all 27 relevant marginal flux vectors, all 15 partner central cells, and all 21 incomparable-pair probabilities. It also checks width, connectedness, the common order, block count, and majority compatibility.

- script SHA-256: `e66b1c7b6abdca842466bcefeba13cbdcfc25237117d4b8d0da13f908d7984ac`;
- executed-output SHA-256: `6f734453aa9cccb1647395156a84688c82c285c93134c0cf3d32becaa658fdf2`;
- terminal marker: `POS3_PARTNER_CONSTRAINTS_ADVERSARY_PASS`.

The campaign lead `account04/B10` still had no complete source-bound `collective-POS3` report at the final lead check for this addendum, so no lead result is invented. Parent POS3 remains open. No novelty or priority claim is made.

No benchmark gold, held-out label, credential, scheduler identifier, machine path, raw transcript, unrelated private data, email, Drive action, paid model/API/Codex call, remote workflow, permission change, or public posting was used.
