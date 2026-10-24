# POS3 account04/B20 — non-crossed successor exits carry a half-minority disjoint staircase charge

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no brain-installation or benchmark work. All probabilities below are under the original uniform law on all full linear extensions.

## 1. Exact collective state consumed

The newest complete team-lead report available before the derivation is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, Git blob `50bac494667235f3630991a512438eac42c30521`.

It supplies the live strict-corridor/bridge reduction and leaves global charge recycling unpaid.

The required named OTHER-account partner input is

- account01/B19, `proofnet24/collective-POS3/account01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, Git blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`.

Its four-state exact-two theorem gives an actual local minority count at least `3E/11` in every continuing four-pair window, solves the conserved-`K` recurrence, and identifies the first non-exact boundary defect as the remaining target-level obstruction.

A second source-bound team input is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, Git blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

Its crossed-neighborhood identity says that for an incomparable pair `x,y` with

`Pred(x) subseteq Pred(y)`, `Succ(y) subseteq Succ(x)`,

putting

`D=Pred(y)\Pred(x)`, `U=Succ(x)\Succ(y)`,

one has the exact full-extension formula

`2 Pr(x<y)-1 = Pr( (exists d in D: x<d) OR (exists u in U: u<y) ).`  (1.1)

The immediately preceding B20 run used active swap blockers at a heavy bridge edge. The present run deliberately changes mechanism and attacks a different unresolved branch: **failure of successor nesting at the first non-exact exit**.

## 2. Compact conditional end-to-end route

Suppose a live fringe pair `x||y_0` already has

`Pred(x) subseteq Pred(y_0)`                                    (2.1)

but the crossed-successor condition fails:

`Succ(y_0) not subseteq Succ(x)`.                              (2.2)

This is the separate non-crossed successor branch left open in the crossed-neighborhood work.

The new result shows that (2.2) is not an unstructured escape. One can climb from `y_0` through a saturated chain of vertices all incomparable with `x` until successor nesting becomes true. Along that chain the reverse probabilities telescope through literal, pairwise-disjoint cover-gap events. At the terminal crossed pair, (1.1) forces the last reverse probability to be at most half the preceding one. Therefore **at least half of the original minority mass is converted into an exact disjoint staircase charge before the branch reaches crossed form**.

Applied to account01/B19's `3E/11` actual packet, any such non-crossed successor exit carries at least `3E/22` of exact full-extension mass into disjoint cover-gap events. This does not finish POS3, but it removes the possibility that the non-crossed successor exit can lose an arbitrarily large fraction of the incoming packet without an exact accounting.

## 3. Successor-staircase construction

### Lemma 3.1 — finite terminal crossed lift

Let `P` be a finite poset and let `x||y_0` satisfy (2.1) and (2.2). Then there exists a saturated chain

`y_0 lessdot y_1 lessdot ... lessdot y_m`, `m>=1`,             (3.1)

such that

1. `x||y_i` for every `i`;
2. `Pred(x) subseteq Pred(y_i)` for every `i`;
3. `Succ(y_m) subseteq Succ(x)`.                               (3.2)

### Proof

Let

`T={z : y_0<=z and z||x}`.

It contains `y_0`. Condition (2.2) supplies a successor `z>y_0` that is not a successor of `x`. Such a `z` cannot satisfy `z<x`, because `y_0<z<x` would imply `y_0<x`, contrary to `x||y_0`; hence `z||x`, so `T` contains an element strictly above `y_0`.

Choose a maximal `y_m` of `T` above `y_0` and take any saturated chain from `y_0` to `y_m`. Every intermediate element `z` on that interval is incomparable with `x`: `z<x` would imply `y_0<x`, while `x<z` would imply `x<y_m`. This proves (1).

If `t<x`, then (2.1) gives `t<y_0`, hence `t<y_i` for every `i`, proving (2).

Finally, let `w>y_m`. If `w` were not a successor of `x`, then `w<x` is impossible because `y_m<w<x` would imply `y_m<x`; therefore `w||x`, which would place `w` in `T` above the maximal `y_m`. Hence every successor of `y_m` is also a successor of `x`, proving (3). `square`

The construction uses only finiteness; no width assumption is needed.

## 4. Exact telescoping and terminal halving

For the chain (3.1), put

`q_i := Pr(y_i < x)`.                                          (4.1)

Because `y_i<y_(i+1)`, the event `{y_(i+1)<x}` is contained in `{y_i<x}`, and the difference is exactly the literal cover-gap event

`G_i := { y_i < x < y_(i+1) }`.                               (4.2)

Hence

`q_i-q_(i+1) = Pr(G_i)`.                                      (4.3)

The `G_i` are pairwise disjoint, since in a linear extension the fixed element `x` can lie in at most one gap of the chain. Consequently

`sum_(i=0)^(m-1) Pr(G_i) = q_0-q_m`.                          (4.4)

The new point is that the terminal crossed identity forces a factor-two loss of reverse mass.

### Theorem 4.1 — terminal halving

For every staircase from Lemma 3.1,

`q_m <= q_(m-1)/2`.                                            (4.5)

Therefore

`q_m <= q_0/2`,                                                (4.6)

and the exact disjoint staircase charge satisfies

`sum_i Pr(G_i) = q_0-q_m >= q_0/2`.                           (4.7)

### Proof

The terminal pair `(x,y_m)` is incomparable and satisfies both nesting hypotheses of the crossed-neighborhood identity (1.1). Let

`D=Pred(y_m)\Pred(x)`.

The previous chain point `y_(m-1)` belongs to `D`: it is a predecessor of `y_m`, and it cannot be a predecessor of `x` because that would give `y_0<=y_(m-1)<x`, contradicting `x||y_0`.

Thus the lower fringe event in (1.1) contains

`{x<y_(m-1)}`,

whose probability is `1-q_(m-1)`. Since `Pr(x<y_m)=1-q_m`, (1.1) gives

`1-2q_m = 2Pr(x<y_m)-1`
`          >= Pr(x<y_(m-1))`
`          = 1-q_(m-1)`.

Therefore `2q_m<=q_(m-1)`, proving (4.5). Since `q_(m-1)<=q_0`, (4.6) follows, and (4.7) follows from (4.4). `square`

### Corollary 4.2 — bias amplification at the terminal crossed pair

If `q_0<1/3`, then

`Pr(x<y_m)=1-q_m > 5/6`.                                      (4.8)

Thus a no-balanced non-crossed successor exit does not merely reach a crossed pair; it reaches a **strictly more extreme crossed pair** while exporting at least half of the incoming minority mass into literal disjoint cover gaps.

## 5. Direct application of the assigned partner's `3/11` packet

Account01/B19 r13 proves that every continuing four-pair exact-two window contains an actual incomparable pair with minority count at least `3E/11`.

Suppose such a selected pair is oriented as `(x,y_0)` with

`q_0=Pr(y_0<x) >= 3/11`,                                      (5.1)

and its predecessor nesting is already in the inherited crossed direction, but successor nesting fails as in (2.2). Then Theorem 4.1 gives

`sum_i Pr(y_i<x<y_(i+1)) >= 3/22`.                            (5.2)

In exact extension counts,

`sum_i #{L:y_i<x<y_(i+1)} >= 3E/22`.                          (5.3)

The individual summands need not have a uniform positive lower bound; the chain may be arbitrarily long. What is new is that the **total charge is exact, disjoint, and cannot diffuse away under the non-crossed exit**.

Likewise, if the incoming live selector is only known to have minority `>1/6`, the branch still exports `>E/12` of disjoint cover-gap mass.

This is a direct boundary-defect conversion statement of the kind requested by the partner. It pays the successor-nesting-failure subtype of the first non-exact boundary. The remaining boundary work is therefore concentrated on crossed multi-distinguisher/non-recurrence exits and on realizing/recycling the resulting exact charge into an actual balanced pair.

## 6. Why this does not prove POS3

The theorem controls total charge, not its concentration on one new incomparable pair. An arbitrarily long staircase can split `q_0-q_m` among many disjoint cover-gap events. Therefore one may not pigeonhole (5.2) into a target-scale single edge without an independent bound on staircase length, and account04/B11 has already shown that bounded local corridor length is false in general.

Also, `q_m<=q_0/2` makes the terminal pair more extreme, not balanced. The next universal step must use the disjoint packet together with width-three channel constraints, the lead's bridge/fork geometry, or the partner's conserved `K` to prevent repeated exact charge recycling without eventual balance/span descent/autonomous reduction.

The result is therefore `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 7. Deterministic regression

The companion checker exhausts every naturally labelled transitively closed finite poset through six vertices. For every ordered starting pair `(x,y_0)` satisfying

- `x||y_0`;
- `Pred(x) subseteq Pred(y_0)`;
- `Succ(y_0) not subseteq Succ(x)`,

it enumerates every maximal terminal `y_m` in the successor staircase and every possible final saturated predecessor `y_(m-1)`. It verifies terminal successor nesting, predecessor nesting, and the exact inequality

`2 Pr(y_m<x) <= Pr(y_(m-1)<x)`,

as well as the resulting half-charge bound.

Recorded output:

```text
naturally_labelled_transitive_closures 5228
noncrossed_successor_starts 18967
terminal_cover_tests 23323
terminal_or_charge_failures 0
minimum_terminal_halving_slack 0
POS3_SUCCESSOR_STAIRCASE_HALF_CHARGE_PASS
```

Equality occurs already on three vertices, so the factor `1/2` in (4.5) is sharp. The finite enumeration is regression/sharpness evidence only; the arbitrary-size result is the symbolic proof above.

## 8. Exact remaining obligation

After this run, the non-crossed successor branch no longer needs to be treated as an unquantified escape. It has the following exact output:

- a terminal crossed pair `(x,y_m)`;
- terminal minority at most half the incoming minority;
- a family of pairwise-disjoint literal cover-gap events carrying at least half the incoming minority mass;
- in the partner `3/11` regime, at least `3E/22` total exact charge.

The first still-unpaid target-level implication is to prove that this exact charge, or the corresponding charge at a crossed multi-distinguisher exit, cannot be recycled indefinitely in width three without producing an actual pair in `[E/3,2E/3]`, strict strong-majority span descent, or a proper autonomous nonchain.

No finite census is promoted to target closure. No deletion law is renamed uniform. No claim of publication priority or novelty is made.
