> **READ THIS FIRST (added 2026-08-20).** The formula in this title is **REFUTED**, twice.
> Globally it fails on `chain3 + chain3` by the campaign's own proved additivity lemma (4 against
> its 3). Restricted to connected systems it fails at `(3,1,1)` at `k=6`, which is **4** where the
> formula says 3 - proved by hand and confirmed by an exhaustive search. `(2,1,1,1)` has the same
> `k` and the same `h` and comes out 3, so no expression in `k` and `h` alone can be right.
> The replacement is not a formula: `d_cb` is the least `d` such that `d` linked pairs
> `(1_{S_j}, e_t)` span `Q^k` - see `linked_pair_characterisation.md`.
> What survives here: the exact values, the `k=7` measurements, and the registered-prediction
> record, which is the point of the document even though its formula died.

# `d_cb = max(⌈k/2⌉, k − h)`: the hub count, not the group size

Registered before the runs that discriminate it. The predecessor,
`max(largest attachment group, ⌈k/2⌉)`, fitted eleven values and died on `(3,2)` at `k=6`.

## Where it comes from

Not a fit over the data this time — read off the two obstructions in
`why_ceil_k_over_two.md`.

Let **`h`** be the number of coordinates lying in **two or more** triangles (the hubs). For a
coordinate `j` in `n_j` triangles, the local star there has obstruction `n_j − 1`, and

  `Σ_j (n_j − 1) = 3k − r`,

which is `k − 1` for every tree (`r = 2k+1`) regardless of shape. The local obstructions overlap
wherever hubs share a triangle, and discounting that overlap — one triangle shared per additional
hub — leaves `k − h`. Against the counting bound:

> **`d_cb = max(⌈k/2⌉, k − h)`**

The counting term is derived (`why_ceil_k_over_two.md` §3, modulo the `E_t ≤ d` lemma). The `k − h`
term is the blocking/transversal obstruction of §14, counted.

## Every exact value in hand

| object | `k` | `h` | `k−h` | `⌈k/2⌉` | formula | measured | source |
|---|---|---|---|---|---|---|---|
| star `k` | any | 1 | `k−1` | | `k−1` | `k−1` | **theorem** |
| `m` disjoint triples | `m` | **0** | `m` | `⌈m/2⌉` | **`m`** | `m` | **theorem** |
| single triangle | 1 | 0 | 1 | 1 | 1 | 1 | exact |
| star `k=2` / chain `k=2` | 2 | 1 | 1 | 1 | 1 | 1 | exact |
| star `k=3` | 3 | 1 | 2 | 2 | 2 | 2 | exact |
| path `k=3` | 3 | 2 | 1 | 2 | 2 | 2 | exact |
| star `k=4` | 4 | 1 | 3 | 2 | 3 | 3 | exact |
| `(2,1)` `k=4` | 4 | 2 | 2 | 2 | 2 | 2 | exact |
| `(1,1,1)` / chain `k=4` | 4 | 3 | 1 | 2 | 2 | 2 | exact |
| `(3,1)` `k=5` | 5 | 2 | 3 | 3 | 3 | 3 | exact |
| `(2,2)` `k=5` | 5 | 2 | 3 | 3 | 3 | 3 | exact |
| `(2,1,1)` `k=5` | 5 | 3 | 2 | 3 | 3 | 3 | exact |
| chain `k=5` | 5 | 4 | 1 | 3 | 3 | 3 | exact |
| tri-cycle `k=3` | 3 | 3 | 0 | 2 | 2 | 2 | exact |
| tri-cycle `k=4` | 4 | 4 | 0 | 2 | 2 | 2 | exact |
| tri-cycle `k=5` | 5 | 5 | 0 | 3 | 3 | 3 | exact |
| `(3,2)` `k=6` | 6 | 2 | **4** | 3 | **4** | **4** | exact |
| `(2,2,1)` `k=6` | 6 | 3 | 3 | 3 | 3 | 3 | exact |
| `(2,1,1,1)` `k=6` | 6 | 4 | 2 | 3 | 3 | 3 | exact |
| chain `k=6` | 6 | 5 | 1 | 3 | 3 | 3 | exact |

No exceptions, and it absorbs the two families that killed the predecessor: disjoint unions are
the `h = 0` case, and `(3,2)` is `k − h = 4`.

## What would show it is wrong

At `k=6` the remaining cases do **not** discriminate — `(4,1)`, `(3,1,1)` and `(1,1,1,1,1)` get
the same answer from both formulas. The discriminating cases are at `k = 7`, where the largest
group and `k − h` come apart:

| profile `k=7` | largest group | `h` | `k−h` | old formula | **this formula** |
|---|---|---|---|---|---|
| `(4,2)` | 4 | 2 | 5 | 4 | **5** |
| `(3,3)` | 3 | 2 | 5 | 4 | **5** |
| `(5,1)` | 5 | 2 | 5 | 5 | 5 (agrees) |
| `(2,2,2)` | 2 | 3 | 4 | 4 | 4 (agrees) |

So **`(4,2)` and `(3,3)` at `k=7` are the tests**: this formula says 5, the dead one said 4. A
measured 4 refutes this formula outright; a measured 5 is a genuine discriminating hit rather
than another fit.

Also worth testing, because it is cheap and the formula makes a sharp claim there: a linear
object with `h` between the extremes — a tri-cycle with an extra pendant triangle, or two stars
joined at a coordinate.

## Status

A fit, but a differently-earned one: it was read off two obstructions that were derived
separately, it covers three families with proved values rather than only enumerated ones, and its
discriminating test is stated before the run. That is exactly what the predecessor could not say.

It is still not a theorem. `k − h` has no proof, only a counting story about overlapping local
stars, and the counting term rests on the unproved `E_t ≤ d` lemma. Nothing here touches the
conjecture: every object remains a known non-member of the class.

---

## The discriminating test: both cases went to the hub count

| case | `h` | `k−h` | old formula | hub formula | pair-sum UB | |
|---|---|---|---|---|---|---|
| star `k=6` (control) | 1 | 5 | 5 | 5 | **5** | control OK |
| `(3,2)` `k=6` (control) | 2 | 4 | 3 | 4 | **4** | control OK |
| **`(4,2)` `k=7`** | 2 | 5 | 4 | **5** | **5** | hub wins |
| **`(3,3)` `k=7`** | 2 | 5 | 4 | **5** | **5** | hub wins |
| `(5,1)` `k=7` | 2 | 5 | 5 | 5 | 5 | agree |
| `(2,2,2)` `k=7` | 3 | 4 | 4 | 4 | 4 | agree |

Both discriminating cases came in at 5, where the dead formula said 4. Predictions were written
into this file before the run, and both controls passed in the same run.

**What this is and is not.** These are pair-sum *upper* bounds. `UB = 5` proves `d_cb ≤ 5`; the
old formula's 4 is not directly refuted, because the search is incomplete. But the same search
recovered all eleven known exact values, so a missing `d = 4` witness is strong evidence that
none exists. It is evidence, not proof.

## And the formula is now derived, not fitted

The blocking picture of `why_ceil_k_over_two.md` §14 gives both terms from one count. A missed
element imposes one linear constraint on the relation coefficients `c`:

- missed `f_t`, or a **non-hub** coordinate of `t` → `c_t = 0` (a *unit* constraint)
- missed **hub** coordinate `j` → `Σ_{t ∋ j} c_t = 0` (a *hub* constraint)

Blocking every relation means these constraints have rank `k`. Two ceilings:

- `|M| = excess ≤ 2d`, so `rank ≤ 2d`
- a hub coordinate lies in exactly one class, so it can be missed at most once: **at most `h` hub
  constraints exist**. And a pair-sum vector belongs to a single triangle, so both of its merges
  give the same `c_t = 0`: **each dimension supplies unit constraints for at most one triangle**.
  Hence `rank ≤ h + d`.

`min(2d, d+h) ≥ k` is exactly `d ≥ ⌈k/2⌉` and `d ≥ k − h`:

> **`d_cb ≥ max(⌈k/2⌉, k − h)`**

and it reproduces the star (`h=1`, `k−1`), disjoint triples (`h=0`, `m`) and the chain
(`h=k−1`, `⌈k/2⌉`) as the three extremes of one formula.

**Verified at `d = 1`:** every line of ten objects reaches at most one triangle's unit
constraint. **The `d ≥ 2` composition is still being checked** — a `d`-dimensional `R` contains
combinations of its generators, so "at most `d` triangles" does not follow formally from the
one-dimensional case, and that is the gap.

A first version of this check reported `EXCEEDS 1` everywhere. That was a bug in the checker, not
a refutation: it unioned the triangles over *every* choice of which element to miss, when only
one element per class is actually missed. Corrected, the answer is 1 throughout.

## The `d ≥ 2` composition holds

The gap flagged above — that "at most `d` triangles" does not follow formally from the
one-dimensional case, since a `d`-dimensional `R` contains combinations of its generators — was
checked directly rather than argued:

| object | `dim` | subspaces searched | max distinct unit-constraint triangles | bound `d` |
|---|---|---|---|---|
| star `k=4` | 1 | 157 | 1 | 1 |
| star `k=4` | 2 | 9,532 | 2 | 2 |
| star `k=4` | 3 | 287,950 | 3 | 3 |
| chain `k=4` | 1 | 157 | 1 | 1 |
| chain `k=4` | 2 | 9,568 | 2 | 2 |
| chain `k=4` | 3 | 291,433 | 3 | 3 |

plus star/path `k=3`, disjoint `m=2` and tri-cycle `k=3` at every dimension up to 3. No subspace
anywhere reaches more than `d` triangles. Roughly 600,000 subspaces.

So the second ceiling `rank ≤ h + d` is verified over the range where it is used, alongside
`rank ≤ 2d`, and together they give `d_cb ≥ max(⌈k/2⌉, k − h)`.

Status of the lower bound, precisely: two counting ceilings, each verified exhaustively at
`d ≤ 3` and neither proved in general. That is one step better than the formula it replaced —
which had no derivation at all — and one step short of a theorem.

## The witnesses have a rule, which is a candidate construction for the upper bound

Everything derived so far bounds `d_cb` from below. The equality needs an explicit `R` of
dimension `max(⌈k/2⌉, k−h)`, and the pair-sum search had been finding one for every object and
discarding it. Printed, they follow a pattern.

| object | `h` | target | triangles contributing, and the coordinate each pair omits |
|---|---|---|---|
| star `k=4` | 1 | 3 | 0, 1, 2 — every pair omits hub 0 |
| `(2,1)` `k=4` | 2 | 2 | 0, 1 — both omit hub 0 |
| chain `k=4` | 3 | 2 | 0, 2 — spread, not consecutive |
| chain `k=5` | 4 | 3 | 0, 1, 3 — spread |
| `(3,1)` `k=5` | 2 | 3 | 0, 1, 2 — all omit hub 0 |
| **`(3,2)` `k=6`** | 2 | 4 | 0, 1, 2 omit hub 0; 4 omits hub 1 |
| `(2,2,1)` `k=6` | 3 | 3 | 0, 1 omit hub 0; 3 omits hub 1 |
| disjoint `m=2`, `m=3` | 0 | 2, 3 | every triangle, each omitting a non-hub |
| tri-cycle `k=4` | 4 | 2 | 0, 1 |

**The rule.** Take one pair-sum from each of `max(⌈k/2⌉, k−h)` distinct triangles, choosing within
each triangle the pair that omits a hub. The count `k − h` is exactly "leave out one triangle per
hub": at a hub carrying `n` triangles, `n−1` of them contribute, and summing over hubs leaves
`k − h`. Where `k − h` drops below the floor, the construction instead takes `⌈k/2⌉ ` pair-sums
from triangles spread so their merges do not overlap — which is why the chains use `0,2` and
`0,1,3` rather than consecutive triangles.

**One exception.** Tri-cycle `k=3` uses two pair-sums from the *same* triangle, `(1,2)` and
`(0,2)`. That is the case `k − h = 0`, where the floor binds alone and there is no hub structure
left to spread across. Whether that is a third regime or an artifact of `k=3` being small is not
settled here.

This is a candidate construction, not a proof. What would make it one is showing that the stated
choice always yields a valid `R` — that its merges are independent and its missed set blocks every
relation — for an arbitrary linear system rather than the thirteen checked.

### The construction works in one branch and my rule for the other is wrong

Applied mechanically — no search, no fallback — the rule splits cleanly along which term of the
max is binding:

| branch | objects | rule builds a valid `R`? |
|---|---|---|
| `k − h ≥ ⌈k/2⌉` (hub-dominated) | star `k=4`, `(3,2)` `k=6`, disjoint `m=3` | **3 of 3** |
| `k − h < ⌈k/2⌉` (floor-dominated) | `(1,1,1,1,1)` `k=6`, tri-cycle `k=5` | 2 of 6 |
| | chain `k=5`, chain `k=6`, `(2,1,1,1)` `k=6`, tri-cycle `k=6` | fail |

**Where `k − h` binds, "leave out one triangle per hub, omitting that hub" is the construction.**
That covers the star, the disjoint family and `(3,2)` — including two proved theorems — and it is
the branch the hub count was introduced to explain.

**Where the floor binds, my spreading rule is wrong.** It fails even on chain `k=5`, one of the
objects the rule was read off, which is the clearest possible sign that what I extracted was not
what the witness was doing. Comparing them: the search's witness took triangles `0,1,3` and
omitted the **non-hub** coordinate 0 for triangle 0, while my greedy took `0,1,2` omitting hubs
throughout. So in the floor branch the choice of *which coordinate to omit* matters, not only
which triangles participate — and "omit a hub where possible" is the wrong preference there.

A valid `R` does exist in every one of these cases; the pair-sum search finds one. What is missing
is a rule that names it. So the upper bound stands as: constructed in the hub-dominated branch,
existence-only in the floor-dominated branch.

### Refined construction: 13 of 14, with the odd case predicted in advance

The floor branch needed a better rule than "spread". Replacing it with **an independent set of
`⌈k/2⌉` triangles in the share-a-coordinate graph** — independence being what stops two chosen
pair-sums from collapsing onto the same triangle's constraint, which is what `rank ≤ h + d`
requires — gives:

| object | branch | triangles chosen | valid |
|---|---|---|---|
| star `k=4`, `k=5` | hub | 0,1,2 / 0,1,2,3 | yes |
| `(3,2)` `k=6` | hub | 0,1,2,4 | yes |
| disjoint `m=3`, `m=4` | hub | all | yes |
| `(2,2,1)` `k=6` | hub | 0,1,3 | yes |
| chain `k=4,5,6` | floor | 0,2 / 0,2,4 / 0,2,4 | yes |
| tri-cycle `k=4`, `k=6` | floor | 0,2 / 0,2,4 | yes |
| **tri-cycle `k=5`** | **floor+reuse** | **0,2,0** | yes |
| `(1,1,1,1,1)` `k=6` | floor | 0,4,5 | yes |
| `(2,1,1,1)` `k=6` | floor | 1,3,4 | **no** |

**The tri-cycle `k=5` case was predicted before the run.** A chain of `k` triangles has a maximum
independent set of exactly `⌈k/2⌉` — the target, with nothing to spare — while a tri-*cycle* of `k`
has only `⌊k/2⌋`. So at `k=5` the target 3 is unreachable by independent triangles, and the
construction must reuse a triangle. It did: `[0,2,0]`, taking two different pairs from triangle 0.
That is the same shape its search witness had, and it was derived from the cycle structure rather
than read off the witness.

**The one failure says independence is necessary but not sufficient.** `(2,1,1,1)` at `k=6` picked
the independent set `{1,3,4}` and failed, while a valid `R` is known there — its search witness
used `0,1,3`, in which `T0` and `T1` share coordinate 0. So that object takes a hub-style choice
even though `k − h = 2` sits below `⌈k/2⌉ = 3`, which means the branch split is not simply
`k − h` against the floor. What selects the working set among the independent ones is not
identified.

Where this leaves the upper bound: a rule that produces a valid witness on 13 of 14 objects
across five families, with its one structural exception predicted in advance and one object it
gets wrong. Still a construction with a gap, not a theorem.

### Two predictions still in flight

Both `k=6` profiles left bracketed `[3,4]` by the squeeze are being determined exactly by an
exhaustive `d=3` search (running at the time of writing, 3717s and 3342s). The formula's values:

| profile | `h` | `k−h` | `⌈k/2⌉` | **predicted `d_cb`** |
|---|---|---|---|---|
| `(4,1)` | 2 | 4 | 3 | **4** |
| `(3,1,1)` | 3 | 3 | 3 | **3** |

`(3,1,1)` is the more interesting of the two: the dead formula also said 3, so it does not
discriminate between them, but a measured 4 would refute **both** and send the whole picture back.
`(4,1)` at 3 would refute this formula alone.

### The selection rule is rank, not independence

Rather than guess a third time, every pair-sum subspace of the target dimension was enumerated
and split by validity:

| object | independent choices among **valid** | among **invalid** |
|---|---|---|
| chain `k=5` | 27 of 252 | **0** of 203 |
| `(1,1,1,1,1)` `k=6` | 135 of 216 | **0** of 600 |
| **`(2,1,1,1)` `k=6`** | **0** of 108 | **135** of 708 |
| tri-cycle `k=5` | 0 (none exist) | 0 (none exist) |

Independence is sufficient on two of these and **fatal** on the third: every one of `(2,1,1,1)`'s
135 independent choices is invalid. So it was never the criterion, and the 13-of-14 score was a
proxy that happened to hold.

**What actually separates them.** Take `(2,1,1,1)`'s independent set `{3,4,5}`, with
`T3=(1,7,8)`, `T4=(2,9,10)`, `T5=(3,11,12)`. Their pair-sums give, via hub coordinates 1, 2 and 3,
the constraints `c_0+c_3=0`, `c_3=0`, `c_0+c_4=0`, `c_4=0`, `c_1+c_5=0`, `c_5=0` — forcing
`c_0, c_1, c_3, c_4, c_5` to vanish. Rank 5, and **`c_2` is never touched**: triangle 2 hangs off
hub 0, which none of the chosen pair-sums reaches. The working choice `{0,1,3}` does reach hub 0,
whose constraint `c_0+c_1+c_2 = 0` brings `c_2` in.

Whereas on the chain, alternating triangles `{0,2,4}` chain their hub constraints — `c_0=0`,
`c_0+c_1=0`, `c_1+c_2=0`, `c_2+c_3=0`, `c_4=0` — and reach rank 5 precisely because consecutive
hub constraints overlap. Independence gives coverage there by accident of the chain's shape.

> **The construction is: choose pair-sums whose induced constraint system has rank `k`.**

That is not a new rule bolted on; it is what §the derivation demanded from the start — blocking
needs rank `k`, and every combinatorial shorthand for it (largest group, spread, independent set)
has now failed on some object. Stating the construction in the same terms as the bound is the
correction, and it makes the two halves match: the lower bound says rank cannot exceed
`min(2d, d+h)`, and the construction says pick any `d` pair-sums achieving rank `k`.

What remains for the upper bound is to show such a choice always exists at `d = max(⌈k/2⌉, k−h)`
for every linear system — an existence statement about the incidence structure of the hubs, not a
recipe.

### Random linear systems

Every object tested until now was one I chose. A formula that survives only its own families is a
description of those families, so the same squeeze was run on randomly generated linear systems —
random trees of triangles, and random linear hypergraphs where free coordinates are identified to
create cycles, with linearity asserted at generation and again before use.

Through 32 systems at `k = 3,4,5` with `h` ranging from 1 to 4 (including `k−h = 0` cases with
cycles), the count stands at **32 confirmed, 0 refuted, 0 inconclusive**. Each is a genuine
squeeze: every subspace exhausted below the target for the lower bound, a pair-sum witness at the
target for the upper.

### Sketch of the existence argument

The constraints live in `Q^k`, indexed by triangles, and come in two species: unit vectors `e_t`,
and hub vectors `1_{S_j}` where `S_j` is the set of triangles containing hub `j`. A pair-sum of
triangle `t` omitting coordinate `x` supplies two of them — one from the class `{f_t, e_x}` and
one from `{e_y, e_z}` — each being `e_t` if the missed coordinate is non-hub and `1_{S_j}` if it
is hub `j`. Existence at `d = max(⌈k/2⌉, k−h)` means choosing `d` pair-sums whose `2d` constraints
span `Q^k`. The three extremes each work out for a different reason:

- **Star**: every triangle meets coordinate 0, so the single hub vector is all-ones; with `k−1`
  units it spans `Q^k`, and `d = k−1` pair-sums supply exactly one unit apiece.
- **Disjoint triples**: no hub vectors exist, so `k` units are required and each pair-sum supplies
  one, giving `d = m`.
- **Chain**: the hub vectors `1_{\{i,i+1\}}` are path incidence vectors of rank `k−1`; an interior
  triangle carries two hub coordinates so one pair-sum yields two of them, and an end triangle's
  non-hub coordinate supplies the missing unit — hence `⌈k/2⌉`.

That is a sketch across three families, not a proof. The general statement needs: for any linear
system, `d = max(⌈k/2⌉, k−h)` pair-sums can be chosen whose hub-and-unit constraints span `Q^k`.
The counting is right in each case above for a visibly different reason each time, which is
usually a sign that the general argument is about the rank of the hub vectors `1_{S_j}` together
with the units available on triangles carrying a non-hub coordinate.

## Refuted as a global formula, and corrected to a component-wise one

Checked against the campaign's **proved** additivity lemma rather than against more random cases,
the formula fails.

Additivity: `d_cb` adds over coordinate-disjoint blocks. chain `k=3` has exact `d_cb = 2`, so two
disjoint copies have `d_cb = 4`. The formula reads the union as one system with `k = 6` and
`h = 4`, giving `max(3, 2) = 3`.

Measured: **4**, with chain3 alone returning 2 and star3⊔star3 returning 4 as in-run controls.

> **`d_cb = max(⌈k/2⌉, k − h)` is false as a global formula.**

The refutation does not actually rest on the measurement: additivity is proved and chain `k=3` is
exact, so 4 is forced. The computation only confirms it. And it is not a one-off —
`⌈a/2⌉ + ⌈b/2⌉ > ⌈(a+b)/2⌉` whenever `a` and `b` are both odd, so **every** pair of odd-length
chains breaks it; `chain3 ⊔ chain3` at `r=14` is simply the smallest.

**The correction.** The formula counts hubs globally and never sees block structure. Applied per
connected component and summed:

> **`d_cb = Σ over connected components C of max(⌈k_C/2⌉, k_C − h_C)`**

| object | components | component-wise | measured |
|---|---|---|---|
| chain3 ⊔ chain3 | 2 | 2 + 2 = **4** | **4** |
| star3 ⊔ star3 | 2 | 2 + 2 = 4 | 4 |
| `m` disjoint triples | `m` | `1` each, sum `m` | `m` (proved) |
| star `k`, chain `k`, tri-cycles, `(3,2)` `k=6` | 1 | unchanged | unchanged |

This is consistent with additivity by construction, which the global version was not. Note the
disjoint family now arises as `m` components of one triangle each rather than as the `h = 0` case
— both give `m`, but the component reading is the one that generalises.

**Why the random test missed it.** Every generator used produces a *connected* system:
`random_tree` grows from one triangle, and `random_linear` only identifies coordinates within an
existing tree. Thirty-two confirmations sampled one side of the space. A generator that never
produces disconnected inputs cannot falsify a claim whose failure is about disconnection, and the
lower-bound derivation gives no reason to expect connectivity to matter, which is exactly why the
gap was invisible from inside the argument.

The lower bound survives unchanged: `max(⌈k/2⌉, k − h) = 3 ≤ 4` here, so only the equality died.

### Random test with a disconnection-capable generator

The blind spot was the generator, so the sweep was rerun with one that draws a component count
first and builds each component on its own coordinate range.

24 systems. **22 carried no information** — the global and component-wise formulas give the same
answer there, so they cannot separate them. Of the 2 that discriminated, both went to the
**component-wise** formula and neither to the global one (rows 12 and 13: two components, `k=4`,
`h=2`; global says 2, component-wise says 3, measured 3).

With `chain3 ⊔ chain3` that is three independent discriminating confirmations and zero against.

The honest sample size is 2 out of 24, not 24. Most random systems do not separate the two
formulas, which is worth stating because "24 systems tested" would suggest twenty-four times the
evidence actually collected — the same overcounting that let 32 confirmations hide a refutation
one section earlier.

## The component-wise version is not a new conjecture

Additivity is proved: `d_cb` adds over coordinate-disjoint blocks, so for any linear system
`S` with connected components `C`,

  `d_cb(S) = Σ_C d_cb(C)`.

The component-wise formula is exactly that identity combined with the connected case. So it adds
no new content, and the whole remaining claim is:

> **Conjecture (connected case).** For a *connected* linear triangle system,
> `d_cb = max(⌈k/2⌉, k − h)`.

Three consequences worth having straight.

**The 32 random systems now count for something.** They were dismissed above as uninformative
about the global formula's failure — correctly, since every one was connected. But connectedness
is precisely the hypothesis of the surviving conjecture, so those 32 are direct evidence for it
rather than a wasted sweep. What they could never have tested was the *global* formula's extension
to disconnected systems, which is what failed.

**The refutation was of an unnecessary extension.** Writing `max(⌈k/2⌉, k−h)` for an arbitrary
system silently asserted that the formula commutes with disjoint union, which additivity forbids
whenever the per-component values sum to more than the global expression. That was an assumption
I never stated, not a discovery about `d_cb`.

**Discriminating evidence for the component reading**, all with in-run controls:

| system | component | global | measured |
|---|---|---|---|
| chain3 ⊔ chain3 | 4 | 3 | **4** |
| chain3 ⊔ triangle | 3 | 2 | **3** |
| two random 2-component systems | 3 | 2 | **3** each |

Four discriminating observations, none against.

### Deliberately discriminating multi-component tests

Random generation is a poor way to collect discriminating cases — 22 of 24 random systems gave
the same answer under both readings. Constructing them directly, using odd chains and lone
triangles as the lever:

| system | component-wise | global | measured | |
|---|---|---|---|---|
| chain3 alone | 2 | 2 | 2 | control OK |
| star3 alone | 2 | 2 | 2 | control OK |
| chain3 ⊔ triangle | **3** | 2 | **3** | component |
| chain3 ⊔ star3 | **4** | 3 | **4** | component |
| chain5 ⊔ triangle | **4** | 3 | **4** | component |
| chain3 ⊔ chain3 | **4** | 3 | **4** | component |

Six discriminating observations across four constructed systems and two random ones, none
against. Note the direction matters here: on every row the component value is the *larger*
candidate, and a pair-sum search is an upper bound, so it cannot manufacture the component answer
by being incomplete — incompleteness can only push a measurement up, and landing on the smaller
global value would have refuted the component reading outright.

### A live test of the connected conjecture, and I expect it to fail

`(3,1,1)` at `k=6` has hubs at coordinates 0, 1 and 2, so `h = 3`, `k − h = 3`, `⌈6/2⌉ = 3`, and
the formula says **3**. Two independent signals say otherwise:

- the pair-sum search found **no** `d=3` witness for it (its upper bound came in at 4), and that
  search recovered all eleven known exact values;
- the earlier run capped at `d=4` was still going at 4860s, past the ~2871s that the same-sized
  `(3,2)` needed to *exhaust* `d ≤ 3` — so it had already ruled out `d=3` and moved on.

Both point to `d_cb((3,1,1)) = 4`, which would refute the connected conjecture — a third
refutation of a formula of mine today, and the first that would hit the *connected* statement
rather than an extension of it.

Recorded before the run returns, because the honest position is that I expect my own formula to
lose here. A returned 3 confirms it; `None` at `dmax=3`, with the upper bound already at 4, makes
the value exactly 4 and kills it.

**Sizing error, owned.** The runs this replaces used `dmax=4`, which after exhausting `d=3` enters
a `d=4` stage of about `C(700,4) ≈ 10^10` subspaces at `r=13` — not slow, infeasible. Both sat
there for over an hour. Capping at `dmax=3` answers the question and terminates, because both
objects are already known to be `≤ 4`: a returned 3 means exactly 3, and `None` means exactly 4.
The general form of the mistake is the familiar one — a search bound chosen from what I wanted to
learn rather than from what the search would cost.

## The connected conjecture is false too, and this one is proved by hand

`(3,1,1)` at `k=6` settles it without waiting for the machine.

**The constraints a dimension can supply are LINKED.** A pair-sum of triangle `t` omitting hub `j`
gives the pair `(1_{S_j}, e_t)` — one hub vector, and the unit for *its own* triangle. You cannot
take a hub vector from one triangle and a unit from another in the same dimension.

For `(3,1,1)` with triangles `T0=(0,1,2)`, `T1=(0,3,4)`, `T2=(0,5,6)`, `T3=(0,7,8)`, `T4=(1,9,10)`,
`T5=(2,11,12)`: coordinates 0, 1, 2 are all hubs, so **`T0` supplies no unit at all**. The
available pairs are `(1_{S_0}, e_t)` for `t ∈ {1,2,3}`, `(1_{S_1}, e_4)`, `(1_{S_2}, e_5)`, with

  `1_{S_0} = (1,1,1,1,0,0)`,  `1_{S_1} = (1,0,0,0,1,0)`,  `1_{S_2} = (1,0,0,0,0,1)`.

At `d = 3` there are two ways to spend the dimensions, and neither reaches rank 6:

- one triangle at each hub → `1_{S_0}, 1_{S_1}, 1_{S_2}, e_a, e_4, e_5` with `a ∈ {1,2,3}`. From
  `1_{S_1}, 1_{S_2}, e_4, e_5` one recovers `e_0`, and then `1_{S_0} − e_0 − e_a` leaves the sum of
  the two remaining units — `e_2 + e_3` if `a = 1` — never separating them. **Rank 5.**
- two triangles at hub 0 plus one elsewhere → `1_{S_0}` repeats, contributing rank 1 rather than
  2. **Rank 5.**

So `d = 3` is impossible, and with the pair-sum upper bound already at 4,

> **`d_cb((3,1,1) at k=6) = 4`, while `max(⌈6/2⌉, 6−3) = 3`.**

**The connected conjecture is refuted.** Not an extension of it this time — the connected
statement itself.

**Why `h` cannot be the invariant.** `(2,2,1)` has the same `k = 6` and the same `h = 3` and comes
in at 3. There hub 0 covers only three triangles, so `1_{S_0} − e_0 − e_1 = e_2` separates, and
rank 6 is reached at `d = 3`. The difference is the *size* of the largest hub relative to the
units its triangles can supply — `(3,1,1)` has a hub covering four triangles while only three of
them can contribute a unit and only one dimension can be spent there without wasting a repeat.

**What the right statement looks like.** `d_cb` is the least `d` such that `d` linked pairs
`(1_{S_j}, e_t)`, with `j ∈ t` and at most one pair per dimension, span `Q^k`. That is a spanning
condition on a bipartite structure between hubs and triangles, not a formula in `k` and `h`. Both
`⌈k/2⌉` and `k − h` remain valid lower bounds; they are simply not tight.

### Closing a gap in that argument

The case analysis above omitted one option: a triangle whose three coordinates are *all* hubs can
supply **two hub vectors and no unit**. In `(3,1,1)`, `T0 = (0,1,2)` omitting hub 0 gives `1_{S_0}`
from the class `{f_0, e_0}`, while its pair `{1,2}` yields `1_{S_1}` or `1_{S_2}`. So `T0`
contributes `(1_{S_0}, 1_{S_1})` or `(1_{S_0}, 1_{S_2})`.

The conclusion survives, by a cleaner route:

- `1_{S_0} = (1,1,1,1,0,0)` treats `T1, T2, T3` symmetrically, and no other available vector
  distinguishes them. Separating three triangles therefore needs at least **two** of the units
  `e_1, e_2, e_3`, and each such unit costs a dimension spent at that triangle. So at least two
  dimensions go to `{T1, T2, T3}`.
- That leaves one dimension to produce both `1_{S_1}` and `1_{S_2}` (or the units `e_4, e_5`
  separating `T4` and `T5` from `T0`). No single dimension does: `T0` yields `1_{S_0}` together
  with only *one* of `1_{S_1}, 1_{S_2}`, and a dimension at `T4` or `T5` yields only its own hub.

Either way `d = 3` falls short, so `d_cb((3,1,1)) = 4` stands. Worth recording because the first
version of the argument reached the right answer while missing a case that could have carried it —
an argument that happens to be right is not the same as one that has considered its alternatives.

## Independent confirmation, and a misdiagnosis of mine

**`(3,1,1)` at `k=6` is 4, by exhaustive search** (5289s), independently of the hand argument and
of the linked-pair model, which share an underlying picture and so were not independent of each
other. `(4,1)` is 4 as well (5851s). Both were run with `dmax=4` and returned exactly, not as
bounds.

So the connected conjecture `d_cb = max(⌈k/2⌉, k−h)` is refuted on measurement as well as on paper:
it says 3 for `(3,1,1)`.

**The misdiagnosis.** I stopped those two runs and relaunched them capped at `d=3`, on the grounds
that a `d=4` stage would have to enumerate about `C(700,4) ≈ 10¹⁰` subspaces at `r=13` and was
therefore infeasible. That was wrong. `fast_dcb` returns the **first** valid subspace it finds, so
it only pays the full enumeration when the answer is *not* at that dimension — and here the answer
was 4, so the search stopped at a witness. Both runs completed normally. The kill was unnecessary,
and the reasoning behind it confused "the search space is large" with "the search must traverse it".

## The `k=7` connected shapes

| case | `h` | `k−h` | `⌈k/2⌉` | formula | measured | |
|---|---|---|---|---|---|---|
| star `k=7` (control) | 1 | 6 | 4 | 6 | **6** | matches; `k−1` by theorem |
| tri-cycle `k=7` | 7 | 0 | 4 | 4 | **4** | matches |
| chain `k=7` | 6 | 1 | 4 | 4 | **4** | matches |
| star4 + pendant chain3 | 4 | 3 | 4 | 4 | **4** | matches |

The refuted formula is still right on all four. That is not a rehabilitation — a formula can be
correct on many objects and still be false — but it locates the failure: the formula breaks on
objects like `(3,1,1)` where a hub covers more triangles than the units its own triangles can
supply, and not on the shapes where the floor binds.
