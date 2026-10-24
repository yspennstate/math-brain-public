# The rooted target in the pair-sum frame

Everything this campaign has measured about `d_cb` is the **unrooted** selector distance. The
dossier's open statement — the named gap — is the **rooted** one: a subspace `R` meeting the
selector condition *and* satisfying `R ∩ span W ⊆ R_<`. With `R_< = 0` that is `R ∩ span W = 0`.

## The condition becomes combinatorial

A combination of chosen pair-sums lies in `span W` exactly when it vanishes at every coordinate
**outside** `W`. So

> `R ∩ span W = 0` **iff** the chosen vectors, restricted to the non-`W` coordinates, are still
> linearly independent.

The rooted target therefore asks for pair-sums that both **block** — their constraints span `Q^k`,
per the blocking theorem — and **survive deletion of the window**.

## Checked against the dossier's proved rooted theorem

The dossier proves (tag 38g) that for the rooted NAE path on `N` vertices, with the root and the
two endpoints as boundary and the `m = N−2` interior vertices private, there is a
boundary-preserving basis with `d_m = ⌈(m+1)/3⌉` and `R_m ∩ span W = 0`. That object is the **fan**:
a fan of `k` triangles has `N = k+1` rim vertices and `m = k−1`, so the dossier's value is `⌈k/3⌉`.

| object | `W` | unrooted | **rooted** | dossier | |
|---|---|---|---|---|---|
| fan `k=3` | {0,1,4} | 1 | **1** | 1 | matches |
| fan `k=4` | {0,1,5} | 2 | **2** | 2 | matches |
| fan `k=5` | {0,1,6} | 2 | **2** | 2 | matches |

Three for three against a proved rooted result, computed from the combinatorial reading above with
no knowledge of the construction the dossier uses.

## Rooting is free on everything tested

| object | `W` | unrooted | rooted | cost |
|---|---|---|---|---|
| star `k=3`, `k=4` | {0,1,2} | 2, 3 | 2, 3 | **0** |
| chain `k=3`, `k=4`, `k=5` | {0,1,2k} | 2, 2, 3 | 2, 2, 3 | **0** |
| fan `k=3,4,5` | {0,1,k+1} | 1, 2, 2 | 1, 2, 2 | **0** |

On every object measured, the rooted minimum equals the unrooted one — the window can be avoided
for free. That is consistent with the dossier's path result, where the rooted and unrooted values
also coincide, and it is the first evidence here on the question the named gap actually asks.

## What this is not

The windows tested are small and of one shape — a root plus two boundary coordinates. The
interesting regime for the named gap is *dense, singleton-layer cyclic blocks*, where `W` is
larger and the connector condition is expected to bite. A cost of zero on five small objects with
three-element windows says the machinery reproduces the known case; it says nothing yet about the
case that is open. The next thing worth running is larger and adversarially chosen `W` — windows
picked to make the deletion condition hard rather than windows inherited from the path setup.

## Adversarial windows: where rooting does cost something

The five friendly windows above were inherited from the dossier's path setup. Maximising over
**every** window of each size instead:

| object | unrooted | worst rooted at `\|W\| = 1,2,3,4` | |
|---|---|---|---|
| star `k=3`, `k=4` | 2, 3 | unchanged at every window | no cost, any `W` |
| chain `k=3`, `k=4` | 2, 2 | unchanged at every window | no cost, any `W` |
| fan `k=4` | 2 | unchanged at every window | no cost, any `W` |
| **fan `k=3`** | 1 | 1, 1, **2**, **none** | raises `d`, and some window blocks |

These are exhaustive over windows, so the "no cost" rows are statements about all windows of those
sizes rather than samples.

**The bad windows, named.** fan `k=3` is `(0,1,2),(0,2,3),(0,3,4)` on `r=5`, with hubs exactly
`{0,2,3}`:

| window | rooted minimum | |
|---|---|---|
| `{0,2,3}` — precisely the hub set | 2 | raises `d` from 1 |
| `{0,1,2,3}`, `{0,2,3,4}` — hubs plus one private coordinate | none | blocks entirely |

Every other window leaves the minimum at 1.

**Two mechanisms, both readable.**

*A needed pair-sum can be swallowed.* The construction here wants `e_2 + e_3`, from the middle
triangle `(0,2,3)`, and **both** of its coordinates are hubs. Once `W ⊇ {0,2,3}` that vector lies
inside `span W` and is forbidden, so the construction must spend an extra dimension. The star never
suffers this: its useful pair-sums are arm pairs built from two *private* coordinates, which survive
any window containing only the hub. So the cost of rooting is not about the window containing hubs
as such — it is about the window containing **both coordinates of a pair-sum the construction
needs**.

*A hard ceiling from counting.* After deleting `W`, only `r − |W|` coordinates remain, and the
chosen vectors must stay independent there, so

> `rooted d ≤ r − |W|`.

At `|W| = 4` with `r = 5` that caps `d` at 1, and when no valid one-dimensional `R` survives the
deletion the window blocks outright. That is the second row, and it is a counting obstruction
rather than a structural one.

This is the connector condition biting, on the smallest object where it can. It is also a caution
about the earlier "rooting is free" reading: free at the windows the dossier's setup supplies, not
free in general.

## The full cost profile: rooting is free or fatal, almost never expensive

Exhaustively, for every object and every window size, the worst rooted minimum, how many windows
raise `d`, and how many block:

| object | `r` | unrooted | windows raising `d` | windows blocking | note |
|---|---|---|---|---|---|
| **fan `k=3`** | 5 | 1 | **1** (at `w=3`) | 2 (at `w=4`) | the only raise found anywhere |
| fan `k=4` | 6 | 2 | 0 | 6 (at `w=5`) | `r−w = 1 < 2`, so arithmetic |
| fan `k=5` | 7 | 2 | 0 | 3 (at `w=5`) | structural |
| star `k=3` | 7 | 2 | 0 | 3 (at `w=5`) | structural |
| star `k=4` | 9 | 3 | 0 | 6 (at `w=5`) | structural |
| chain `k=4` | 9 | 2 | 0 | 2 (at `w=5`) | structural |
| chain `k=5` | 11 | 3 | 0 | 2 (at `w=5`) | structural |
| tri-cycle `k=4`, `k=5` | 8, 10 | 2, 3 | 0 | **0** | never blocks |

Roughly two thousand windows in total, enumerated exhaustively per size.

**The pattern.** Exactly **one** window in the whole sweep raises the dimension — the hub set of
fan `k=3`, the smallest object on which the condition can bite. Everywhere else the rooted minimum
equals the unrooted one whenever a rooted `R` exists at all. So the connector condition behaves as
a feasibility constraint, not a cost:

> rooting is **free or fatal**, and almost never merely expensive.

**Why that matters for the named gap.** The dossier's open statement asks for a rooted estimate
`dim((R+R_<)/R_<) ≤ C·L_{Q|W}` with a constant. If the rooted dimension equals the unrooted one
wherever it is defined, then the rooted constant is the unrooted constant, and the whole difficulty
of the rooted problem sits in feasibility — in which windows admit a valid `R` at all — rather than
in a worse bound. That is a different shape of problem from the one the dimension-raising reading
would suggest, and it is testable further.

**Tri-cycles never block.** Both cyclic objects tolerate every window tested, while every tree-like
object has blocking windows at `w=5`. If that holds up it says cyclic structure is *more* robust to
rooting, not less — which cuts against the intuition that cyclic blocks are the hard case, and is
worth checking on bigger cycles before being believed.

**Limits.** Windows up to size 5, objects up to `r=11`, and the search ranges over pair-sums only,
so a "block" means no *pair-sum* `R` survives the window rather than no `R` whatsoever. The
non-pair-sum directions have excess 1 and cannot help reach a maximal-excess subspace, but that is
an argument, not a check, and it has not been run here.

### The blocks are genuine, not an artefact of searching pair-sums

The caveat above — that a "block" meant no *pair-sum* `R` survives rather than no `R` at all — was
checked rather than argued. Re-running the blocking and control windows over **every line of the
dual**:

| object | window | pair-sum search | full line search | |
|---|---|---|---|---|
| fan `k=3` | `{0,1,2,3}` | none | **none** | genuinely blocked |
| fan `k=3` | `{0,2,3,4}` | none | **none** | genuinely blocked |
| fan `k=3` | `{0,2,3}` | 2 | 2 | the raise is real |
| fan `k=3` | `{1,4}` | 1 | 1 | control agrees |
| star `k=3` | `{1,2,3,4,5}` | 2 | 2 | control agrees |
| star `k=3` | `{0}` | 2 | 2 | control agrees |
| chain `k=4` | `{0,1,2}` | 2 | 2 | control agrees |

The full search finds nothing where the restricted one found nothing, and reproduces every value
where it found one. So the pair-sum restriction did not manufacture the blocking result, and the
one dimension-raising window survives the wider search too.

That does not extend the check to every blocking window in the profile — only these two, plus five
controls — but it removes the specific failure mode the caveat named.

### "Tri-cycles never block" was a window-size artefact

Flagged above as worth checking before believing, and it does not survive. Extending tri-cycle
`k=6` (`r=12`) past the earlier sweep's `|W| ≤ 5`:

| `\|W\|` | windows | worst rooted | raises | **blocks** | ceiling |
|---|---|---|---|---|---|
| 3 | 220 | 3 | 0 | 0 | no |
| 4 | 495 | 3 | 0 | 0 | no |
| 5 | 792 | 3 | 0 | 0 | no |
| 6 | 924 | 3 | 0 | 0 | no |
| **7** | 792 | 3 | 0 | **6** | no |

So cyclic objects do block — they simply need a larger window than the first sweep reached, and
`r − |W| = 5` still exceeds the unrooted value of 3, so these are structural blocks rather than the
arithmetic ceiling. The earlier reading ("cyclic structure is more robust to rooting") was an
artefact of stopping at `|W| = 5`, which is exactly the failure mode this campaign has hit before:
a maximum over a bounded enumeration read as a property of the objects.

**"Free or fatal" survives the extension.** Across all 3,223 windows above, **zero** raise the
dimension. The one dimension-raising window in the whole investigation is still fan `k=3`'s hub set.
That claim is now tested on windows up to size 7 and objects up to `r = 13`, rather than the
`|W| ≤ 5`, `r ≤ 11` that produced it.

### Both `k=6` values confirmed from the second direction

The `dmax = 3` runs were kept as a cross-check on the `dmax = 4` results:

| object | `d ≤ 3` exhaustive | `dmax = 4` | conclusion |
|---|---|---|---|
| `(3,1,1)` `k=6` | `> 3` (2962s) | 4 (5289s) | **exactly 4** |
| `(4,1)` `k=6` | `> 3` (3423s) | 4 (5851s) | **exactly 4** |

Two search directions, same answer. Also a second refutation of my "infeasible" call: every one of
these four runs terminated, the longest in under 100 minutes.

### "Free or fatal" is refuted too, and the hub-set explanation with it

**A second dimension-raising window exists, on a much larger object.** chain `k=6` (`r=13`) at
`|W| = 5`: worst rooted 4 against an unrooted 3, one window in 1,287, alongside 2 blocks. So
raising is not confined to fan `k=3`, and the earlier "free or fatal, almost never merely
expensive" reading was again an artefact of the range swept — `|W| ≤ 5` on `r ≤ 11`.

The honest form: **raises are rare — two known across roughly five thousand windows — but they
occur on large objects as well as small.** Rarity is not confinement, and the previous statement
conflated them.

**And the mechanism I guessed for them is wrong.** The natural reading of fan `k=3` was that the
window swallows the hubs, taking with it the pair-sums whose both coordinates are hubs. Tested
directly:

| object | hub set | rooted at that window | |
|---|---|---|---|
| fan `k=3` | `{0,2,3}` | 2 vs unrooted 1 | **raises**, and it is the *unique* size-3 raiser |
| chain `k=4` | `{2,4,6}` | 2 | free |
| chain `k=5` | `{2,4,6,8}` | 3 | free |
| chain `k=6` | `{2,4,6,8,10}` | 3 | free |

The hub set is the unique raising window for fan `k=3` and is harmless for every chain, including
the one that *does* have a raising window at exactly the hub set's size. So the size coincidence at
chain `k=6` (hubs `{2,4,6,8,10}`, raise at `w=5`) is a coincidence, and whatever raises the
dimension there is a different window.

Two of my readings of this data have now failed in the same way — a pattern from the smallest case
generalised without testing the next one. The check that caught both was cheap: evaluate the
proposed mechanism on the objects where it predicts nothing should happen, not only where something
did.

### The two raising windows, named

Both known dimension-raising windows are now identified, and each is unique at its size:

| object | raising window | what it is |
|---|---|---|
| fan `k=3` | `{0,2,3}` | exactly the triangle `(0,2,3)` — the middle one |
| chain `k=6` | `{4,5,6,7,8}` | exactly triangles `(4,5,6)` and `(6,7,8)` — two adjacent ones |

So both are **unions of whole triangles**, and covering a triangle entirely removes every pair-sum
it could contribute, since all three of its pairs then lie inside `span W`.

**That is an observation, not a mechanism, and here is the case that stops it being one.** chain
`k=4`'s window `{0,1,2}` also covers a whole triangle and does **not** raise the dimension; nor do
the whole-triangle windows of chain `k=5`. So covering triangles is necessary-looking but plainly
not sufficient, and what distinguishes chain `k=6`'s pair from chain `k=4`'s and `k=5`'s is not
established.

The obvious next guess — that the surviving triangles must still contain an independent set of size
`⌈k/2⌉` — is *already known to be the wrong shape*: the selection criterion for a valid `R` is
constraint **rank**, not independence of the chosen triangles, and independence was shown to be
fatal rather than sufficient on `(2,1,1,1)` at `k=6`. Writing it down here only to record that it
was considered and rejected on existing evidence rather than tested afresh.

Three mechanism guesses have died in this file already, each by generalising from the smallest case.
The fourth is not being offered.

### Wheels: the named gap's own family

| object | unrooted | dossier `⌈n/3⌉` | raises | blocks |
|---|---|---|---|---|
| wheel `n=4` | 2 | 2 | 0 at `\|W\| ≤ 3` | 5 at `\|W\| = 4` |
| wheel `n=5` | 2 | 2 | 0 at `\|W\| ≤ 4` | 0 so far |

The unrooted values measured here over the full line set match the dossier's proved theorem, a
further two agreements. No wheel window has raised the dimension so far — the raises remain confined
to the two tree-like objects above.

### The raiser collection: every chain `k=6` raiser covers the same two triangles

Rather than read a mechanism off two examples — which failed three times — the sweep enumerated
every raising window on chains `k=4…7` and fans `k=3…6`. Partial results, with the triangles each
window covers *entirely*:

| object | raising windows |
|---|---|
| chain `k=4` | **none**, at any size |
| chain `k=5` | **none**, at any size |
| chain `k=6` | many at `\|W\| = 8`, and **every one covers triangles `[2,3]` wholly** |

Samples: `{1,4,5,6,7,8,10,12}`, `{2,4,5,6,7,8,9,11}`, `{3,4,5,6,7,8,10,12}` — the coordinates
`4,5,6,7,8` (triangles `(4,5,6)` and `(6,7,8)`) appear in all of them, and the remaining three
coordinates vary freely across the rest of the chain.

So for chain `k=6` the condition looks like **`W ⊇ triangles 2 and 3`**, the adjacent middle pair,
with everything else irrelevant. That matches the unique `\|W\| = 5` raiser found earlier, which is
exactly those five coordinates and nothing more.

**And it still is not sufficient in general.** Covering the middle two triangles of chain `k=4`
(coordinates `{2,3,4,5,6}`) does not raise, and chain `k=5` has no raiser at any size. So "cover two
adjacent middle triangles" raises for `k=6` and not for `k=4` or `k=5`, and what changes at `k=6` is
not established. The honest statement is a clean empirical rule for one object and a hole where the
general mechanism should be.

This is the collection that should have been gathered before the three mechanism guesses, not after.
