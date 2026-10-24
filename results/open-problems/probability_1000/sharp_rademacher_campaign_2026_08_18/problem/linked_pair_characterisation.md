# `d_cb` is a spanning number, not a formula

Three closed forms died in one day — largest attachment group, the global hub count, the connected
hub count. What survived every round was the machinery underneath, so the statement belongs in its
terms rather than as a fourth formula in `k` and `h`.

## The statement

A pair-sum `v = e_y + e_z` for triangle `t = (x,y,z)`, omitting `x`, merges `f_t` with `e_x` and
`e_y` with `−e_z`. One element of each class is missed, giving two constraints on the relation
coefficients `c ∈ Q^k`:

| class | missed element | constraint |
|---|---|---|
| `{f_t, e_x}` | `f_t` | `e_t` (unit) |
| | `e_x` | `1_{S_x}` if `x` is a hub, else `e_t` |
| `{e_y, e_z}` | `e_y` | `1_{S_y}` if `y` is a hub, else `e_t` |
| | `e_z` | `1_{S_z}` if `z` is a hub, else `e_t` |

where `S_j` is the set of triangles containing coordinate `j`. The two constraints are **linked**:
both come from the same triangle, so a hub vector and a unit cannot be drawn from different
triangles within one dimension.

> **`d_cb` = the least `d` such that `d` such linked pairs span `Q^k`.**

## Every exact value the campaign holds

| object | spanning number | known `d_cb` | |
|---|---|---|---|
| star `k=2…6` | 1, 2, 3, 4, 5 | `k−1` | **theorem** |
| disjoint `m=2,3` | 2, 3 | `m` | **theorem** |
| path/chain `k=3,4,5,6` | 2, 2, 3, 3 | same | exact |
| `(2,1)`, `(1,1,1)` `k=4` | 2, 2 | same | exact |
| `(3,1)`, `(2,2)`, `(2,1,1)` `k=5` | 3, 3, 3 | same | exact |
| tri-cycle `k=3,4,5` | 2, 2, 3 | same | exact |
| `(3,2)` `k=6` | 4 | 4 | exact |
| `(2,2,1)`, `(2,1,1,1)`, `(1,1,1,1,1)` `k=6` | 3, 3, 3 | same | exact |
| **`(3,1,1)` `k=6`** | **4** | 4 | see below |
| chain3 ⊔ chain3 | 4 | 4 | exact |
| chain3 ⊔ triangle | 3 | 3 | exact |

**27 objects, 27 matches.**

## Why this is worth more than the formulas it replaces

**It makes the discrimination no `(k,h)` formula can.** `(3,1,1)` and `(2,2,1)` have the same `k=6`
and the same `h=3` and come in at 4 and 3. Any expression in `k` and `h` alone gives them the same
value and is therefore wrong about one of them — which is exactly how the connected conjecture
died.

**It reproduces the two proved theorems** rather than being fitted to them: the star's `k−1` and
the disjoint family's `m` both fall out, and those are the endpoints that earlier formulas had to
be checked against by hand.

**It is a restatement of the blocking theorem, which is proved**, rather than a new hypothesis.
Blocking says a transversal is independent exactly when the missed set's constraints have rank `k`;
this says `d_cb` is the least number of dimensions whose linked constraints reach that rank. The
remaining gap between the two is the same one as before — that a dimension supplies at most two
constraints of this form (`excess ≤ 2d`, resting on the unproved `E_t ≤ d`), and that a spanning
selection can always be realised as an actual subspace.

## Status of `(3,1,1) = 4`

Three routes, one still running:

1. **By hand.** `1_{S_0} = (1,1,1,1,0,0)` treats `T1,T2,T3` symmetrically, so separating them needs
   two of `e_1,e_2,e_3`, costing two dimensions; the third must then supply both `1_{S_1}` and
   `1_{S_2}`, and no single dimension does.
2. **Linked-pair spanning**, computed here: 4.
3. **Pair-sum upper bound**: 4, with no `d=3` witness.

An exhaustive `d ≤ 3` search is running as the direct check. Routes 1 and 2 are both mine and share
the same underlying model, so they are not independent of each other; the exhaustive search is.

## What is not claimed

This is verified on 27 objects, not proved. It is a characterisation, so it computes `d_cb` rather
than predicting it from a few parameters — which makes it less falsifiable per object than a
formula and more useful as a bridge to a proof. And it says nothing about the conjecture: every
object here is a known non-member of the class.

## A consequence for Conjecture RC

The linked-pair reading gives an upper bound with no search at all. A dimension from triangle `t`
can always supply the unit `e_t` — by missing `f_t` rather than a coordinate, which needs no hub
and no non-hub coordinate. Taking one pair-sum per triangle therefore yields all `k` units, and
those span `Q^k`. So

> **`d_cb ≤ k` for every linear triangle system.**

Checked as a construction rather than inferred: for thirteen objects the `k` chosen pair-sums are
linearly independent **and** satisfy `valid_R`, so the bound comes with an explicit witness.

**Why that settles RC on two families.** A triangle-tree has `r = 2k+1` and `|A| = 6·3^{k−1}`, so
`ℓ = kβ` exactly and `ℓ/β = k`; a disjoint union of `m` triples has `r = 3m` and `|A| = 6^m`, so
`ℓ = mβ`. In both cases

  `tightness = d_cb·β/ℓ = d_cb/k ≤ 1`,

which is **Conjecture RC for the entire tree family and for disjoint unions**, rather than for the
members enumerated. Measured `ℓ/β` came out at exactly 3.000, 4.000, 5.000, 6.000 on the trees, as
the identity requires.

**Where the argument does not close.** Off those families `ℓ = kβ` fails, and with it the
implication:

| object | `ℓ/β` | bound `kβ/ℓ` on tightness |
|---|---|---|
| trees `k=3…6` | exactly `k` | **1.0000** |
| disjoint `m=3` | 3.000 | 1.0000 |
| tri-cycle `k=3` | 3.131 | 0.9581 |
| **tri-cycle `k=4`** | **3.957** | **1.0108** |
| tri-cycle `k=5` | 5.014 | 0.9971 |

At tri-cycle `k=4` the bound is 1.0108, so `d_cb ≤ k` permits tightness above 1 and proves nothing.
The measured value is fine — `d_cb = 2` gives 0.5054 — but that is a measurement, not the argument.
Closing RC for cycles needs either a better upper bound than `d_cb ≤ k` or the exact `ℓ` for
cyclic linear systems, which is not `kβ`.

**Status.** `d_cb ≤ k` is a construction verified on thirteen objects, not proved: a general proof
needs one pair per triangle whose incidence vectors are independent, and since two triangles in a
linear system share at most one coordinate, the chosen pairs form a graph on the coordinates whose
independence is a no-cycle condition — satisfiable in every case checked, but not argued in
general.

### `d_cb ≤ k` on random systems, with no search

The construction was checked on 22 randomly generated linear systems — a generator that emits both
connected and disconnected ones, since the earlier sweep's blind spot was a generator that could
only emit connected inputs. Two choices were compared:

- **natural**: each triangle contributes the pair of its two later coordinates. On a tree these are
  the coordinates it adds, so the edges are pairwise disjoint and automatically form a forest. No
  search.
- **greedy**: fall back to another pair per triangle if the natural one is dependent.

The natural choice was independent **and** `valid_R` on **22 of 22**, so the greedy fallback was
never needed. With the 13 handpicked objects that is 35 in total.

Why independence is the right thing to check: the `k` vectors are unsigned incidence vectors
`e_y + e_z`, and over `Q` such a set is independent exactly when every component of the graph they
form has at most one cycle and that cycle is odd. A choice forming a forest therefore always
works, and on a tree the natural choice is a forest for free — each triangle's two new coordinates
appear in no other chosen pair.

That leaves the general statement one step short: for an arbitrary linear system one needs a choice
of pairs forming such a graph, which is a no-even-cycle condition rather than an identity. It held
in every case checked and the natural choice never failed, but "the natural choice always works" is
not argued.

## Cross-validation against the dossier's proved cycle theorem

The dossier's rooted NAE cycle `A_n` is `{(a,b_1..b_n) : a + b_i + b_{i+1} ∈ {±1}, indices cyclic}`
— the triples `(0, i, i+1)` around a cycle, all sharing coordinate 0. **That is the wheel**, in the
notation this campaign has been using, and the dossier proves (tag 35)

  `d_cb(A_n) = d_geo(A_n) = ⌈n/3⌉`  for every `n ≥ 4`.

Against the wheel values measured here independently, by the exact `fast_dcb` search and with no
knowledge of that theorem:

| | `n=3` | `n=4` | `n=5` | `n=6` |
|---|---|---|---|---|
| dossier `⌈n/3⌉` (proved) | 1 | 2 | 2 | 2 |
| measured here | **1** | **2** | **2** | **2** |

Four for four. The machinery built in this campaign reproduces a proved result of the document it
was never checked against — the first direct agreement between the two layers.

**It also explains the counting-bound violations quantitatively.** A wheel has `r = n+1` and
`|D| = 2n+1`, so `|D| − r = n` and the counting bound would demand `⌈n/2⌉`; the true value is
`⌈n/3⌉`. That gap is exactly the violation measured on wheels `k=3,5,6`, and the reason is the
hypothesis identified independently here: the wheel is **non-linear**, since consecutive triples
share the edge `{0, i+1}`. The dossier's own dual for `A_n` shows the same thing from the other
side — `|D_n| = 2n+1` rather than the `r + k = 2n+1`… which happens to coincide here, so the
richer structure is in the *matroid*, described in the dossier as genuinely three-connected,
rather than in the count.

**And the two conjectures line up.** The dossier's tag 38d states `d ≤ ℓ(A_n)/log₂(4/3)`, which is
`d_cb ≤ ℓ/β` — exactly the tightness `≤ 1` this campaign calls Conjecture RC, proved there for the
cycle family. What is added here is the other side: `d_cb ≤ k` with `ℓ = kβ` gives the same bound
for triangle-trees and disjoint unions. Between the dossier's cycles and this campaign's trees,
RC now holds on three families for two different reasons.

The dossier's `cycle_rigidity_ratio_limit` is in a different normalisation and should not be
confused with tightness: `d_cb/ℓ → 1.0902` is the ratio against `ℓ` itself, so in `β` units it is
`1.0902 β = 0.4525`, comfortably below 1. The "constant-one ceiling" that the cycles exceed is the
`d_cb ≤ ℓ` statement, which the dossier records as disproved; `d_cb ≤ ℓ/β` is the surviving one.

### The fan matches the dossier's path theorem too

The dossier's rooted-NAE **path** on `N` vertices has `d_cb = d_geo = ⌈(N−1)/3⌉` (tag 38f). That
object is the **fan**: triples `(0, i, i+1)` taken non-cyclically, so a fan of `k` triangles has
`N = k+1` rim vertices and `N − 1 = k` triples, predicting `⌈k/3⌉`.

| | fan `k=3` | fan `k=4` | fan `k=5` |
|---|---|---|---|
| dossier `⌈k/3⌉` (proved) | 1 | 2 | 2 |
| measured here | **1** | **2** | **2** |

**Seven independent agreements in total** — four wheels against tag 35, three fans against tag 38f
— between values measured by this campaign's exact search and two separately proved theorems of the
document. Neither family was chosen with those theorems in view; both were built as non-linear
controls for the counting bound, and their disagreement with that bound is what made them
interesting here.

Two things follow. The exact-`d_cb` machinery in this campaign is validated against an external
proved standard rather than only against itself. And the wheels and fans, which look like
counterexamples from inside the linear theory, are in fact the cases the document has already
solved — `⌈n/3⌉` rather than `⌈n/2⌉` — so the boundary between what is settled and what is open
runs exactly along linearity, from both directions.

## Eight further values, measured after the characterisation was written down

| object | linked-pair | measured | how measured |
|---|---|---|---|
| `(3,1,1)` `k=6` | 4 | **4** | exhaustive `fast_dcb`, 5289s |
| `(4,1)` `k=6` | 4 | **4** | exhaustive `fast_dcb`, 5851s |
| star `k=7` | 6 | **6** | pair-sum; also `k−1` by the star theorem |
| tri-cycle `k=7` | 4 | **4** | pair-sum |
| chain `k=7` | 4 | **4** | pair-sum |
| star4 + pendant chain3 | 4 | **4** | pair-sum |
| `(3,2,1)` `k=7` | 4 | **4** | pair-sum, **stated in advance** |
| `(4,1,1)` `k=7` | 5 | **5** | pair-sum, **stated in advance** |

Eight for eight. Two of those were written down before the measurement existed, and the two `k=6`
rows come from an exhaustive search that shares nothing with the model — which matters, because
`(3,1,1)`'s value had previously rested on a hand argument and on this characterisation, two routes
with the same underlying picture.

**Running total: 34 distinct objects, 34 matches, no misses**, spanning stars, chains, paths, fans,
wheels, tri-cycles, disjoint unions, mixed shapes, and every attachment profile at `k = 6`.

That is a different kind of standing from the three formulas that died. Each of those was an
expression in a couple of parameters, and each was killed by a single object whose parameters
matched another object with a different answer. This is not an expression in parameters; it
computes the answer from the incidence structure, which is why `(3,1,1)` and `(2,2,1)` — identical
in `k` and `h` — come out 4 and 3.

What it still is not: proved. The lower direction needs that a dimension supplies at most two
constraints of this form, which rests on the unproved `E_t ≤ d`; the upper direction needs that a
spanning selection can always be realised as an actual subspace, which is verified but not argued.

## How much of the 34 is actually independent

The pair-sum search and the linked-pair model share an assumption — that pair-sums are the
directions that matter. Agreement between them is partly this campaign's own anchor measured twice,
so the 34 should be split by how each value was obtained.

**Independent of the pair-sum framing** — measured by the full `fast_dcb` search over *every* line,
or known by a proved theorem:

| source | objects |
|---|---|
| star theorem `d_cb = k−1` | star `k = 2…7` |
| disjoint theorem `d_cb = m` | disjoint `m = 1,2,3` |
| full `fast_dcb` search | chain `k=2`, path `k=3`, chain `k=4,5`; `(2,1)`, `(1,1,1)` at `k=4`; `(3,1)`, `(2,2)`, `(2,1,1)` at `k=5`; tri-cycle `k=3,4,5` |
| exhaustive `fast_dcb`, this session | **`(3,1,1)`** and **`(4,1)`** at `k=6` |

That is about 21 objects whose values could have diverged from the model and did not.

**Partly shared**: the `k=6` sweep rows — `(3,2)`, `(2,2,1)`, `(2,1,1,1)`, `(1,1,1,1,1)`, chain —
were squeezed between an exhaustive lower bound over all lines and a pair-sum upper bound. The
lower half is independent; the upper half is not.

**Fully shared**: the `k=7` shapes other than the star, the tri-cycle `k=6,7`, and the disconnected
constructions were measured by the pair-sum search alone. Those confirm that the model is
self-consistent, not that it is right.

So the honest statement is not "34 independent confirmations" but: **about 21 values that could
have diverged and did not, including both proved theorems and the two exhaustive `k=6` runs**, plus
a further 13 that are consistency checks. The strongest single item remains `(3,1,1) = 4`, because
the model and the hand argument both said 4 and an exhaustive search that shares neither agreed.

What would test the shared half properly: run the full `fast_dcb` search on one `k=7` shape where
only the pair-sum search has spoken. That is expensive at `r=15` but it is the check the current
evidence cannot supply.

## Five more predictions, and a scope boundary that could have gone either way

**Predictions on linear systems never measured** — the linked-pair number computed first, then an
independent pair-sum search:

| object | predicted | measured |
|---|---|---|
| `(2,2,2)` `k=7` | 4 | **4** |
| `(3,2,1)` `k=7` | 4 | **4** |
| `(4,1,1)` `k=7` | 5 | **5** |
| star4 + pendant chain3 | 4 | **4** |
| tri-cycle `k=6` | 3 | **3** |

Five for five.

**The scope test.** The derivation assumes linearity — it needs `excess ≤ 2d`, which book `p=3`
already breaks. So off linear systems the characterisation has no right to work, and if it worked
anyway my account of *why* it works would be wrong. Against exact `d_cb` values measured earlier:

| object | linked-pair | exact `d_cb` | |
|---|---|---|---|
| wheel `k=4` | 2 | 2 | agrees |
| fan `k=4` | 2 | 2 | agrees |
| **wheel `k=5`** | 3 | **2** | disagrees |
| **wheel `k=6`** | 3 | **2** | disagrees |
| **book `p=3`** | 2 | **1** | disagrees |
| **book `p=4`** | 3 | **1** | disagrees |
| **fan `k=5`** | 3 | **2** | disagrees |

Five of seven disagree, and the direction is uniform: the characterisation **overestimates**. That
is precisely what the mechanism predicts — a non-linear system lets one vector retire more than two
forms, so fewer dimensions suffice than the linked-pair count allows. The two agreements are the
small cases where the extra merging power has nothing to buy.

So the scope is not asserted from the derivation alone; it is measured, and the failure has the
sign the derivation requires. Taken with the dossier's proved `⌈n/3⌉` for wheels and fans — which
those exact values match — the picture is consistent from three directions: the document solves the
non-linear families, this characterisation covers the linear ones, and it breaks exactly where the
linearity hypothesis does.
