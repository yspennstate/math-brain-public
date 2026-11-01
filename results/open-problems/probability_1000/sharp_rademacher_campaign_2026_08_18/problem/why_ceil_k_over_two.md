> **READ THIS FIRST (added 2026-08-20).** Sections 1-14 below argue for `excess <= 2d` and for
> the counting bound `d_cb >= ceil(k/2)`. **`excess <= 2d` is FALSE** - section 19 gives the
> witness (tri-cycle `k=4`, `dim R = 3`, excess 7), section 21 shows `excess <= 2d+1` fails too,
> and section 23 derives the correct formula `excess = E + (V' - comp)`, from which
> `excess <= 2d` holds **exactly when the pair-sum graph is a forest**. The counting bound has
> **no derivation** as of section 21, though every measured object still satisfies it.
> `E_t <= d`, named in sections 5-7 as the one remaining gap, is **refuted** - it follows from
> `excess = E_c + E_t` with `E_c <= d` proved plus the section 19 witness.
> What survives sections 1-14 unchanged: the explicit dual `|D| = r+k`, `ker Phi = span{rho_t}`,
> the blocking reformulation, `E_c <= d`, and `excess <= 2` at `d = 1` (section 17, proved).

# The `⌈k/2⌉` term is a counting bound, and it reduces to one lemma

`d_cb = max(largest attachment group, ⌈k/2⌉)` fits eleven exact values on triangle-trees and
predicted two of them in advance. Both terms were fitted. This note derives the second one.

## 1. The dual set is completely explicit

For a triangle-tree `T` on `r = 2k+1` coordinates, with `A` the sign vectors having no
monochromatic triple, the full dual `D` is exactly:

- the `2k+1` **coordinate forms** `e_j` — dual because `p_j = ±1` for every sign vector;
- one **triangle form** `f_t = e_a + e_b + e_c` per triangle `t = (a,b,c)` — dual because
  `p_a + p_b + p_c ∈ {±1}` precisely when the triple is not monochromatic, which is the fibre
  condition itself.

So `|D| = (2k+1) + k = 3k+1`. Checked on eight trees at `k = 2,3,4` (star, path, chain,
`(2,1)`, `(1,1,1)`): **exact match every time, no extra forms and none missing**. This is a
description of `D`, not a bound on it, and it is the first time in the campaign that `D` has
been written down rather than computed.

## 2. What `d_cb` has to buy

`valid_R` needs at most `dim = r` classes. Starting from `|D| = 3k+1` forms and needing at most
`2k+1` classes, the subspace `R` must collapse

> **excess = `|D| − #classes` ≥ `(3k+1) − (2k+1)` = `k`**

and `k` is exactly the number of triangles. Confirmed on all eight trees: `|D| − r = k` with no
slack anywhere.

## 3. One dimension buys two merges, because the dual is taken up to sign

Take `v = e_b + e_c` for a triangle `t = (a,b,c)`. It does two jobs at once:

- `f_t − e_a = e_b + e_c = v`, so **`f_t` merges with `e_a`** — a triangle merge;
- `e_b − (−e_c) = e_b + e_c = v`, so **`e_b` merges with `e_c`** — a coordinate merge, available
  only because `D` is a set of `±`-classes.

One dimension, two units of excess. If two is the ceiling, then `excess ≤ 2d`, and since excess
must reach `k`:

> **`d_cb ≥ ⌈k/2⌉` for every triangle-tree.**

## 4. Is two the ceiling?

Searched exhaustively for a subspace beating it — the observation that would kill the derivation,
rather than more confirmations, which the eleven values already imply.

| dim | subspaces searched | max excess found | `2d` |
|---|---|---|---|
| 1 | 43–157 per tree | **2** | 2 |
| 2 | 524–9,568 per tree | **4** | 4 |
| 3 | 1,967–40,629 per tree | **6** | 6 |

No violation on any of eight trees. The bound is **tight, not slack** — the maximum equals `2d`
at every dimension where enough triangles exist to reach it (`k=2` at `d=3` tops out at 5,
because with only two triangle forms there is no third triangle merge to buy). Dimension 3
matters specifically: `⌈k/2⌉ = 3` is where `k=5` and `k=6` sit, so the bound is now tested where
it is actually used rather than only below it.

## 5. Why the factor is two, and what is left

A tight bound usually has a reason with as many halves as its constant. Splitting excess by what
each merge consumes, taking the coordinate merges first:

> `excess = E_c + E_t`, with **`E_c ≤ d`** and **`E_t ≤ d`**

verified on every subspace searched above, both halves tight.

**`E_c ≤ d` is already proved.** A coordinate merge `e_i ~ e_j` requires `e_i ∓ e_j ∈ R`, and the
signed incidence vectors of a forest are linearly independent. `E_c` coordinate merges therefore
put `E_c` independent vectors into `R`.

**`E_t ≤ d` is not proved.** It is the count of merges that consume a triangle form, and it is the
only gap between here and a theorem. Note the two halves are exactly the two jobs `v = e_b + e_c`
performs, which is why the bound is tight: it is met precisely when every dimension is doing both.

So the position is:

| claim | status |
|---|---|
| `D` = coordinates + triangle forms, `\|D\| = 3k+1` | verified on 8 trees, with a proof sketch in §1 |
| excess needed `= k` | follows from `\|D\|` and `r` |
| `E_c ≤ d` | **proved** |
| `E_t ≤ d` | verified exhaustively at `d ≤ 3`, unproved |
| **`d_cb ≥ ⌈k/2⌉`** | **follows from the above** |
| `d_cb ≥ largest attachment group` | proved for the star only (`d_cb = k−1`) |
| `d_cb =` max of the two | unproved; 11 exact values, 2 predicted in advance |

## 6. What this explains that the fit did not

The formula's two terms are two different obstructions, not two halves of one pattern.

`⌈k/2⌉` is a **counting** obstruction: there are `k` too many dual forms and each dimension can
retire at most two. It binds for every non-star tree measured at `k=4` and `k=5` — every one of
them came in at exactly `⌈k/2⌉`, so the counting bound is not merely valid there but achieved.

The largest attachment group is a **transversal** obstruction — the Rado violation this campaign
already identified. It binds for the star, which sits at `k−1`, strictly above its counting bound
of `⌈k/2⌉` for every `k ≥ 3`.

That is why the star is the exception rather than the rule, and why `k = 3` is where the two
coincide (`⌈3/2⌉ = 2 = k−1`) — the star and path tie there because both obstructions give 2. The
tie was previously recorded as a small-`k` accident. It is not; it is where the two curves cross.

## 7. The gap narrows to one sentence

`E_t ≤ d` was an observed inequality with no argument. It can be sharpened into a rank identity,
which is a better target: if the pass-2 edge vectors are linearly independent then `E_t` is the
rank of a set of vectors all lying in `R`, and `E_t ≤ dim R = d` is immediate.

Both identities hold on every subspace searched (7 trees, `d ≤ 3`, up to 40,629 subspaces each):

> `rank(pass-1 edge vectors) = E_c` and `rank(pass-2 edge vectors) = E_t`

One structural fact came out of the derivation and then checked out directly. If `f_t` is adjacent
to two coordinate forms `e_a` and `e_j`, then

  `e_a − e_j = (f_t − e_j) − (f_t − e_a) ∈ R`,

so pass 1 has already merged them. Hence **every triangle form touches at most one coordinate
class** — confirmed on every subspace searched, maximum 1 throughout. The pass-2 graph is
therefore `k` triangle nodes, each with at most one edge to a coordinate class, plus
triangle–triangle edges.

So the chain now reads:

- `D` = coordinates + triangle forms, `|D| = 3k+1` — verified `k = 2,3,4,6`
- excess needed `= |D| − r = k` — immediate
- `excess = E_c + E_t` — construction
- `E_c ≤ d` — **proved** (signed incidence vectors of a forest are independent)
- `E_t ≤ d` ⟸ **pass-2 forest edge vectors are linearly independent** — the one open statement
- therefore `excess ≤ 2d`, therefore **`d_cb ≥ ⌈k/2⌉`**

## 8. What is not proved

The independence of the pass-2 vectors is the hardest piece and it is **not** proved. It is
verified exhaustively for `d ≤ 3` on seven trees. Reducing an inequality to an independence
statement makes the target cleaner; it does not make it established, and `d ≤ 3` is exactly the
range where the interesting cases sit rather than a range chosen for being convincing.

Also unproved: that `d_cb` *equals* `max(group, ⌈k/2⌉)` rather than merely being bounded below by
both. The counting bound gives one lower bound and the star's derangement argument gives the
other; the upper bound — that no further obstruction exists — has eleven exact values behind it
and no argument at all.

And none of this touches the conjecture. Every object here is a known non-member of the class.

## 9. The independence statement, reformulated — and half of it proved

Let `Φ : Q^D → Q^r` send the basis vector `δ_g` to the dual form `g` itself. The edge vector of
`(x,y)` is `Φ(δ_x ∓ δ_y)`, and the `δ`-differences of a forest's edges are linearly independent in
`Q^D` — that is the standard fact, applied upstairs where it is free. So:

> the pass-2 edge vectors are dependent **iff** the forest's signed difference space meets `ker Φ`
> nontrivially.

**`ker Φ` is completely known, and this part is proved.** `D` contains every coordinate form, so
`rank D = r`, and `|D| = 3k+1`, giving `dim ker Φ = (3k+1) − (2k+1) = k`. The `k` relations

  `ρ_t = δ_{f_t} − δ_{e_a} − δ_{e_b} − δ_{e_c}`  (one per triangle `t = (a,b,c)`)

lie in `ker Φ` by the definition of `f_t`, and are linearly independent because each carries its
own `δ_{f_t}` that no other `ρ_s` touches. Counting dimensions, they span it:

> **`ker Φ = span{ρ_t : t a triangle}`, of dimension exactly `k`.**

So the open lemma is no longer about arbitrary linear algebra in `Q^r`. It is the question of
whether a nonzero combination of the `k` triangle relations can lie in the signed difference space
of the pass-2 forest — a statement about `k` explicit vectors and a forest, in a space where the
only relations are the triangles themselves.

Two features of the reformulation are worth keeping. `dim ker Φ = k` is the *same* `k` as the
excess that must be bought, which is why the counting is as tight as it is rather than tight by
coincidence. And the signs are not decoration: over an unsigned graph the obstruction would be a
component-sum condition, while a signed forest can be unbalanced and carry no such constraint, so
any proof has to use the `±` identification that made one dimension buy two merges in the first
place.

This is a route, not a proof. What is established here is `ker Φ`; what remains is the
intersection statement.

## 10. Checking the formula against the families already proved

The discipline that was missing from the four claims retracted earlier today: before trusting a
pattern, evaluate it on every family with a *proved* answer, not only on the ones enumerated.

| family | proved `d_cb` | group | `⌈k/2⌉` | formula | agrees? |
|---|---|---|---|---|---|
| single triangle | 1 | 0 | 1 | 1 | yes |
| star `k` | `k−1` (theorem) | `k−1` | `⌈k/2⌉` | `k−1` | yes |
| `m` disjoint NAE triples | `m` (theorem) | **0** | `⌈m/2⌉` | `⌈m/2⌉` | **no** |

**The disjoint family breaks it.** Those triples share no coordinates, so there are no attachments
and the group term is 0, leaving the formula at `⌈m/2⌉` against a proved `m` — at `m=4`, 2 against
4. The gap grows without bound.

This is not a refutation of anything claimed above, because every measured value and every
prediction concerned *connected* triangle-trees, and disjoint triples are not trees. But it is a
real limit on the formula and it says something the tree data alone could not:

> the transversal obstruction is **not** "largest attachment group" in general. On trees the
> group happens to measure it; off trees it does not, and the disjoint family is the witness.

The counting bound is unaffected and survives the same test. For `m` disjoint triples `r = 3m` and
`|D| = 3m + m = 4m`, so excess needed is `m` and `d ≥ ⌈m/2⌉` — valid, and simply not tight, which
is all a lower bound has to be. So the two halves of the formula have genuinely different scope:
the counting bound looks general, the group term is a tree-specific proxy for something else.

That reading also predicts where to look next. What the disjoint family and the star have in
common is that both sit *above* their counting bound; the chain and the spread trees sit exactly
on it. The right question is not "what is the group term" but what makes an object exceed its
counting bound at all — and the answer has to reduce to the group on trees and to `m` on disjoint
unions.

## 11. The route, its failure, and where the failure lies

Reading the coefficient of `δ_{e_j}` in a putative dependency
`Σ_e λ_e (δ_x − σ_e δ_y) = Σ_t c_t ρ_t` gives, for every coordinate `e_j` that is **not** an
endpoint of a pass-2 forest edge,

  `Σ_{t ∋ j} c_t = 0`,

which for a coordinate private to one triangle reads `c_t = 0` outright. Counting says such
coordinates are plentiful: at most `q ≤ k−1` distinct coordinates are attachment points, so at
least `2k+1−q ≥ k+2` are private, while pass-2 contributes at most one coordinate endpoint per
edge. So the whole lemma turns on whether those rows have rank `k`.

**Tested, and it fails in general.** Across the `d ≤ 3` sweep the rank drops to `k−1` in 144
cases — all of them at `d = 3, k = 3`. Independence of the pass-2 vectors still held everywhere,
so the lemma is not refuted; the argument simply does not close by itself.

**But the failures lie outside the range the theorem needs.** To conclude `d_cb ≥ ⌈k/2⌉` it is
enough to bound excess for `d ≤ ⌈k/2⌉ − 1`; above that the conclusion holds regardless, since
`2d ≤ k−1 < k` for odd `k` and `2d ≤ k−2 < k` for even `k`. At `k=3` that range is `d ≤ 1`, and
the drops occur at `d = 3`.

Rechecking the required range at the `k` that matter:

| tree | `d` | subspaces | `E_t = rank`? | system rank |
|---|---|---|---|---|
| star, chain, `(3,1)`, `(2,2)` at `k=5` | 1, 2 | 241 / ~23,800 each | yes | **5 of 5** |
| chain, `(3,2)` at `k=6` | 1, 2 | 343 / ~50,000 each | yes | **6 of 6** |

Roughly 200,000 subspaces, no drop.

## 12. Where the proof stands

| link | status |
|---|---|
| `ker Φ = span{ρ_t}`, dimension `k` | **proved** |
| signed-forest `δ`-differences independent in `Q^D` | **proved** (standard) |
| dependency ⟹ `Σ_{t∋j} c_t = 0` off pass-2 endpoints | **proved** |
| that system has rank `k` | verified for `d ≤ ⌈k/2⌉−1`, `k = 2…6`; **unproved**, and false at `d=3, k=3` |
| `E_c ≤ d` | **proved** |
| `excess ≤ 2d`, hence **`d_cb ≥ ⌈k/2⌉`** | follows from the above |

One link is unproved, and it is now a finite combinatorial statement — the rank of an incidence
system of triangles against the coordinates pass-2 does not touch — rather than a claim about
arbitrary subspaces of `Q^r`. The remaining obstacle is triangles with no private coordinate,
which contribute no unit row; whether the other rows always make up the rank is the open question.

The value of the failure is that it is specific. The route breaks where `d` is large relative to
`k`, which is exactly where the counting bound is not needed, and that is a much better position
than a route that works everywhere it was tested and might break anywhere it was not.

## 13. The condition is linearity, not treeness — §10 corrected

> **Refuted by §32.** The claim below - `|D| = r + k` for a linear system, hence excess `k`, hence
> `d_cb ≥ ⌈k/2⌉` for every linear triangle system - is false. A linear system can imply not-all-equal
> constraints on triples outside itself, and each implied triple adds a dual form. The bipartite
> construction of §32 gives linear systems with spanning fibres whose duals exceed `r + k` (the
> smallest is the Pasch configuration), and its `K_{4,4}` member has a valid `R` of dimension 7
> against `⌈k/2⌉ = 8`. The measurements in this section are unaffected; the general statement is not.


§10 said the counting bound "looks general" and that it should be tested rather than asserted.
Tested, it is false in general, and the failure identifies the real hypothesis.

**Where it fails.** Exact `d_cb` against `⌈(|D|−r)/2⌉`: wheel `k=3,5,6`, book `p=3,4` and fan
`k=3,5` all come in *below* the bound. So `excess ≤ 2d` is not structure-free.

**Why, worked by hand.** Book `p=3` has triangles `(0,1,2),(0,1,3),(0,1,4)`, all sharing the same
*pair* `{0,1}`. Take `v = e_0 + e_1`:

  `f_1 − e_2 = v`,  `f_2 − e_3 = v`,  `f_3 − e_4 = v`,  `e_0 − (−e_1) = v`

Four merges from one dimension, so excess 4 against `2d = 2`, and `d_cb = 1` beats a bound of 2.
In a tree, `e_b + e_c` names the two non-shared coordinates of one triangle and can serve no
other; a shared *pair* lets one vector serve every triangle on it at once.

**So the hypothesis is linearity** — no two triangles meeting in two coordinates — and not
treeness. Every violation above is non-linear; every linear family obeys.

**The test that separates the two readings**, registered before running: a *linear non-tree*.
Treeness says it may violate; linearity says it must obey.

| object | linear | tree | `\|D\|−r` | bound | `d_cb` | |
|---|---|---|---|---|---|---|
| tri-cycle `k=3` | yes | no | 3 | 2 | **2** | obeys, tight |
| tri-cycle `k=4` | yes | no | 4 | 2 | **2** | obeys, tight |
| tri-cycle `k=5` | yes | no | 5 | 3 | **3** | obeys, tight |
| book `p=3` (control) | no | no | 3 | 2 | 1 | violates |
| book `p=4` (control) | no | no | 4 | 2 | 1 | violates |

The non-linear controls reproduce their violation inside the same script, so the clean linear
result is not a detector that quietly checked nothing.

**The statement, restated at its right generality.** For a *linear* system of `k` triangles on `r`
coordinates, `D` is the `r` coordinate forms plus one form per triangle, `|D| = r + k`, so the
excess that must be bought is exactly `k`, and

> **`d_cb ≥ ⌈k/2⌉` for every linear triangle system**, trees among them.

Triangle-trees have `r = 2k+1`; tri-cycles have `r = 2k`; disjoint unions have `r = 3k`. All three
give the same `|D| − r = k` and the same bound, and the tri-cycles attain it exactly, as the
non-star trees do. Wheel `k=3` is the one object tested whose `|D|` exceeds `r + k` — it has an
extra dual form — and it is non-linear.

This is a better result than the one it replaces. The tree restriction was never doing any work;
what was doing the work was that two triangles in a tree cannot share an edge.

## 14. The second obstruction is blocking, and there is no third one

`(3,2)` sits above both the counting bound and the largest group, which looked like a third
mechanism. It is not. It is the transversal condition, read correctly.

Because `ker Φ = span{ρ_t}`, a dependency among the chosen forms is exactly a kernel element
supported inside the chosen set. Writing that out gives a purely combinatorial criterion:

> A transversal `S` is independent **iff** the only `c` supported on `F = {t : f_t ∈ S}` with
> `Σ_{t ∋ j} c_t = 0` at every coordinate `j` whose `e_j` is **missed** is `c = 0`.

So the Rado condition is a covering condition: **the missed set must block every nonzero
combination of the `k` relations.** Checked against the rank/DFS implementation of `valid_R` on
every subspace of dimension `≤ 2` for eight objects — star `k=2,3,4`, chain `k=2,3,4`, disjoint
`m=2`, tri-cycle `k=3` — roughly 29,000 subspaces, **zero disagreements**.

This is what the two obstructions really are. Excess `≤ 2d` says how much can be missed; blocking
says what has to be missed. And the interaction explains the families that looked unrelated:

- **`m` disjoint triples.** The `m` relations have pairwise disjoint supports, so each needs its
  own hit. One dimension's two merges land inside a single triangle — `v = e_1+e_2` gives
  `f_1 ∼ e_0` and `e_1 ∼ e_2`, both inside triangle 1 — so no dimension blocks two relations.
  Hence `d_cb = m`, though counting alone asks only `⌈m/2⌉`. This is the proved value, recovered.
- **The star.** Every `ρ_t` runs through `e_0`. Missing the single element `e_0` blocks all `k`
  single-triangle relations at once, so blocking is far cheaper than for disjoint triples at the
  same excess — and what remains to be blocked are the pairwise relations `ρ_i − ρ_j`, in which
  `e_0` cancels. That is the derangement structure of the star proof, arrived at from the other
  direction.
- **`(3,2)` at `k=6`.** Two hubs, so the relations share coordinates only partially: neither the
  disjoint picture nor the star picture applies, and it lands above both bounds.

**So "largest attachment group" was a proxy** for how much the relations share a coordinate, which
is why it tracked `d_cb` on trees with one hub and failed on `(3,2)` with two, and why it read as
0 for disjoint triples, whose relations share nothing at all and which are the most expensive
family of the lot.

Stated carefully: this is a validated reformulation plus an explanation of three families, not a
formula. It does not yet predict `d_cb((3,2))`, which is still running, and it does not close the
`E_t ≤ d` lemma. What it removes is the belief that a third, unnamed mechanism is at work.

## 15. The excess-2 directions are exactly the pair-sums, and that makes `d_cb` cheap

A vector buys two merges only by doing both jobs at once, and the candidates for that are the
**pair-sums** `e_x + e_y` over the three pairs of each triangle. Enumerating every line and
computing its excess:

| object | lines | excess-2 lines | are they exactly the pair-sums? |
|---|---|---|---|
| star `k=3`, path `k=3` | 91 | 9 | yes, 0 extras |
| star / chain / `(2,1)` `k=4` | 157 | 12 | yes, 0 extras |
| disjoint `m=2` | 58 | 6 | yes, 0 extras |
| tri-cycle `k=3` | 72 | 9 | yes, 0 extras |
| chain `k=5` | 241 | 15 | yes, 0 extras |
| `(3,2)` `k=6` | 343 | 18 | yes, 0 extras |

Exactly `3k` of them every time, and nothing else reaches excess 2.

**This turns the search inside out.** Instead of `C(|lines|, d)` subspaces — 55 million for
`(3,2)` at `d=4` — search subsets of the `3k` pair-sums: `C(18,4) = 3060`. The restricted search
is *not* complete once `2d` exceeds `k` and there is slack in the excess, so a hit is an **upper
bound** and a miss proves nothing. Soundness is never at risk, only tightness.

**Controls.** Run on eleven objects with known exact `d_cb` — star `k=3,4`, path `k=3`, chain
`k=4,5,6`, `(2,1)` `k=4`, `(3,1)` `k=5`, disjoint `m=2,3`, tri-cycle `k=3` — the pair-sum search
recovers **every** known value. The star `k=6` upper bound also comes in at 5, matching the
theorem.

**The open case, settled.** `(3,2)` at `k=6` was exhausted at `d ≤ 3` on a box (2871s), proving
`d_cb ≥ 4`. The pair-sum search produces an explicit valid `R` at `d = 4` in **26 seconds**. So

> **`d_cb((3,2) at k=6) = 4`, exactly.**

Both bounds are direct computations; neither leans on the unproved `E_t ≤ d` lemma.

**And it confirms the guess registered when the refutation landed.** `(3,2)` has hubs of 3 and 2
attachments, giving local stars of 4 and 3 triangles with star obstructions 3 and 2; discounting
the base triangle they share gives `3 + 2 − 1 = 4`. That was written down before the value was
known, and it is right. One case is not a rule — the same arithmetic has to be checked against
`(4,1)`, `(3,1,1)` and the rest before it is anything more than a coincidence with a story.

**A note on the control column.** The first run printed `CTRL FAILED` for star `k=6` and `(3,2)`.
That was a bug in the verdict logic, not a failure: it tested whether the squeeze *pinned* the
known value rather than whether the bounds *bracketed* it. Both bracket correctly (`[3,5] ∋ 5`,
`[3,4] ∋ 4`). Fixed, and recorded because a verdict column that encodes the wrong test is
indistinguishable from a real finding on the next read.

## 16. Correction: `|D| = r + k` is not a linearity phenomenon

> **Refuted by §32.** Wheel `k=3` is not the only object whose dual exceeds `r + k`, and an enlarged
> dual is not a non-linearity phenomenon: a whole family of *linear* systems has extra dual forms,
> the smallest being the Pasch configuration `{024, 035, 125, 134}` with `|D| = 14` against `r+k = 10`.


§13 recorded wheel `k=3` as "the one object tested whose `|D|` exceeds `r + k` — and it is
non-linear", which implies non-linearity is what produces the extra dual form. That is wrong, and
the dossier's own description of the rooted NAE cycle is what exposed it: it gives
`D_n = {A, B_i, C_i}` with `A = e_0`, `B_i = e_i`, `C_i = e_0+e_i+e_{i+1}`, i.e. exactly the
coordinate forms plus one form per triple, `|D_n| = 2n+1`.

Checking that against the measurements already taken here:

| object | linear | `r` | `k` | `r+k` | measured `\|D\|` |
|---|---|---|---|---|---|
| wheel `k=3` | no | 4 | 3 | 7 | **8** |
| wheel `k=4`, `k=5`, `k=6` | no | 5, 6, 7 | 4, 5, 6 | 9, 11, 13 | **9, 11, 13** |
| book `p=3`, `p=4` | no | 5, 6 | 3, 4 | 8, 10 | **8, 10** |
| fan `k=3`, `k=4`, `k=5` | no | 5, 6, 7 | 3, 4, 5 | 8, 10, 12 | **8, 10, 12** |
| every linear object tested | yes | — | — | — | matches |

So `|D| = r + k` holds on every object measured **except wheel `k=3`**, linear or not. And the
dossier states its cycle theorem for `n ≥ 4`, so `k=3` is a known degenerate case — the 3-cycle,
where the rim closes on itself immediately — not evidence about linearity.

**What this changes.** The counting bound's failure off linear systems is *purely* a failure of
`excess ≤ 2d`, and not at all a matter of the dual being larger. Book `p=3` remains the clean
witness: `|D| = 8 = r + k` exactly as everywhere else, and yet `v = e_0 + e_1` buys four merges
because its triangles share a *pair*. The dual set is the same shape in both regimes; what differs
is how much a single dimension can retire.

That makes the linear hypothesis sharper rather than weaker. It is not needed to describe `D`; it
is needed precisely and only for the two-merges-per-dimension ceiling.

## 17. The `d = 1` case of `excess ≤ 2d` is now proved, and so is the pair-sum characterisation

Both were verified exhaustively but not argued. For a one-dimensional `R = span{v}` on a **linear**
system they follow by cases, using `D = {e_j} ∪ {f_t}` and the fact that a merge is a pair
`f ∓ g ∈ span{v}`.

**`v = e_x + e_y` with `{x,y}` contained in a triangle `t = {a,x,y}`.** Two merges exist:
`e_x − (−e_y) = v`, and `f_t − e_a = e_x + e_y = v`. There is no third:

- another coordinate pair would need `e_i ∓ e_j = e_x+e_y`, forcing `{i,j} = {x,y}`;
- another triangle merge would need `f_s − e_j = e_x+e_y`, i.e. `s = {j,x,y} ⊇ {x,y}`, so `s = t`
  — **because linearity permits at most one triangle on a given pair**;
- `f_s ∓ f_u = v` is impossible: for a linear system `|s ∩ u| ≤ 1`, so `f_s − f_u` has support at
  least 4, and `f_s + f_u` has support at least 5.

Exactly **2**.

**`v = e_x − e_y`.** The coordinate merge `e_x − e_y = v` exists. A second would need
`f_t − f_s = e_x − e_y`, which has support 2 and therefore requires `|t ∩ s| = 2` — forbidden.
`f_t ∓ e_j = e_x − e_y` is impossible since `f_t` has all coefficients `+1`. Exactly **1**.

**`v` of support ≥ 3.** No coordinate pair reaches it. Two triangle-coordinate merges coinciding
would give `f_t − f_s = e_j ∓ e_i`, support 2, again forcing `|t ∩ s| = 2`. And `f_t − f_s` with
`|t∩s| = 1` has sign pattern `(+,+,−,−)` while `f_u − e_i` has `(+,+,+,−)`, so those cannot
coincide either. At most **1**.

> **For every linear triangle system, a one-dimensional `R` produces at most two merges, with
> equality exactly when `v = e_x + e_y` for a pair `{x,y}` lying in a triangle.**

That is `excess ≤ 2d` at `d = 1`, proved rather than verified — and it also proves the
characterisation of §15, that the excess-2 directions are exactly the `3k` pair-sums, three per
triangle, which had only been measured.

**And it proves why linearity is the hypothesis.** Every step above that could fail does so through
one door: `f_t − f_s` drops to support 2 exactly when `|t ∩ s| = 2`, i.e. when two triangles share
an *edge*. That is the book `p=3` witness in general form — its triangles share the pair `{0,1}`,
so `f_i − f_j = e_{2+i} − e_{2+j}` has support 2 and buys merges a linear system cannot.

What remains is the composition: that `d` dimensions give at most `2d`. The `d = 1` case no longer
rests on enumeration, but a subspace is not the union of its lines, so this does not yet close
`E_t ≤ d`.

## 18. A route to the composition, closed off

With `excess ≤ 2` proved at `d = 1`, the obvious next step is to compose it. Every merge edge's
vector lies on some line of `R`, and a line supports at most two merges, so

  `excess ≤ 2 × (number of distinct lines carrying forest edges)`.

If that line count were at most `d`, the composition would close. **It is not.**

| object | `d` | subspaces | max excess | max lines | `d` |
|---|---|---|---|---|---|
| star `k=3` | 1, 2, 3 | 91 / 2,901 / 40,188 | 2, 4, 6 | 1, **3**, **4** | 1, 2, 3 |
| star `k=4`, chain `k=4`, `(2,1)` `k=4` | 1, 2 | up to 9,568 | 2, 4 | 1, **3** | 1, 2 |
| disjoint `m=2` | 1, 2, 3 | up to 7,692 | 2, 4, 5 | 1, **3**, **4** | 1, 2, 3 |
| tri-cycle `k=3` | 1, 2, 3 | up to 15,475 | 2, 4, 6 | 1, **3**, **5** | 1, 2, 3 |

The line count runs to `d+1` (and to `d+2` for tri-cycle `k=3` at `d=3`), so the bound it yields is
`2d+2` — too weak by exactly the amount that matters.

**Why it still fails to bite.** The subspaces with many lines are not the subspaces with high
excess: in every violating case the excess *equals* the line count, i.e. each line carries a single
edge, while the maximal-excess subspaces have `d` lines each carrying two. So there is a trade-off
between "many lines" and "two edges per line", and `excess ≤ 2d` holds because of that trade-off
rather than because either factor is separately bounded. A proof has to capture the interaction,
which the per-line bound alone cannot.

Recorded because it is a natural first thing to try and it does not work — the `d = 1` result is
genuinely local, and lifting it needs an argument about how lines of `R` interact, not a count of
them.

**One checker bug worth noting.** The first run reported the line count exceeding `d` even at
`d = 1`, which is impossible since `R` is then a single line. The cause: a merge means
`f − g ∈ R` **or** `f + g ∈ R`, because `D` is taken up to sign, and the code always formed
`f − g`. For sign-flipped merges that vector is not the one in `R`. Corrected, `d = 1` gives a line
count of 1 throughout — and the failure at `d ≥ 2` survives the correction.

## 19. `excess ≤ 2d` is FALSE, and the derivation of the counting bound is broken

The lemma this whole note rests on does not hold. Constructed deliberately from the trade-off
identified in §18:

| object | `R` | `dim R` | excess | `2d` |
|---|---|---|---|---|
| tri-cycle `k=4` | `span{e₀+e₂, e₂+e₄, e₄+e₆}` | 3 | **7** | 6 |
| tri-cycle `k=6` | `span{e₀+e₂, e₂+e₄, e₄+e₆, e₆+e₈, e₈+e₁₀}` | 5 | **11** | 10 |
| control: one pair-sum | | 1 | 2 | 2 |
| control: two disjoint pair-sums | | 2 | 4 | 4 |

**The mechanism.** Four pair-sums forming a cycle in the coordinate graph are linearly dependent —
`(e₀+e₂) − (e₂+e₄) + (e₄+e₆) = e₀+e₆` — so a 3-dimensional `R` can contain **four**
merge-carrying pair-sum lines. Each carries its two merges, and the classes come out `[4,2,2,2,2]`,
giving excess `3+1+1+1+1 = 7`.

**These are LINEAR systems.** Consecutive triangles in a tri-cycle share exactly one coordinate, so
this is not the non-linear escape hatch of §13. Linearity is not sufficient for `excess ≤ 2d`.

**What this kills.** The derivation `excess ≤ 2d` ⟹ `d_cb ≥ ⌈k/2⌉` is invalid as stated. The
counting bound was the first of this campaign's two obstructions and everything in §§3–7 rested on
it.

**What survives.**

- `excess ≤ 2` at `d = 1` is unaffected — it is proved (§17) and the controls above reproduce it.
- The **conclusion** still holds on every object measured: tri-cycle `k=3…7` give `d_cb = 2,2,3,3,4`,
  which is `⌈k/2⌉` throughout, and no measured object has ever fallen below the bound.
- The bound needs `excess ≤ 2d` only at `d = ⌈k/2⌉ − 1`, not at every `d`. The counterexamples
  require at least three pair-sums forming a cycle, hence `d ≥ 3`, so they do not touch the bound for
  `k ≤ 6`, where the relevant dimension is `d ≤ 2`.
- For trees the exhaustive searches at `d ≤ 3` found max excess exactly `2d` with no violation, and
  a tree has no coordinate cycle among its pair-sums, so the construction above cannot be run there.

**So the honest position** is that `excess ≤ 2d` is a *tree* phenomenon, not a linear one, and the
counting bound is proved only in the range `d ≤ 2` where the proved `d = 1` case and the verified
`d = 2` case cover it. For `k ≥ 8`, where the bound needs `d = 3`, it is now unsupported — and
tri-cycles are exactly where a counterexample would live.

**The immediate test** is tri-cycle `k = 8`: the bound claims `d_cb = 4`, and the cyclic
construction gives excess `2d+1 = 7` at `d = 3` against the `k = 8` required. That is one short, so
the bound survives arithmetic — but only just, and a cycle of pair-sums with more overlap would
close the gap.

## 20. The damage, measured: `excess ≤ 2d+1`, and the bound survives for even `k` only

The decisive test was tri-cycle `k=8`, where the bound claims `d_cb ≥ 4` and therefore needs the
lemma at `d = 3` — exactly where the counterexamples live.

| quantity | value |
|---|---|
| `\|D\|` | 24 `= r + k` |
| excess required (`\|D\| − r`) | 8 |
| cyclic `R = span{e₀+e₂, e₂+e₄, e₄+e₆}`, `dim 3` | excess **6 = 2d**, not 7 |
| pair-sum upper bound | **4** |

**Why the violation vanished here.** At `k=4` those three pair-sums *close* the hub cycle — the
hubs are `0,2,4,6` and the fourth pair-sum `e₆+e₀` is already in their span. At `k=8` the hub cycle
has eight vertices, so three pair-sums close nothing and only three lines lie in `R`, giving
`excess = 2d` exactly.

**So the violation requires a closed cycle of pair-sums.** A cycle of length `L` uses `L` pair-sums
spanning `L−1` dimensions and carrying `2L` merges with one coincidence, so

> **`excess ≤ 2d + 1`**, the `+1` occurring only when `R` contains a closed pair-sum cycle,

which matches both counterexamples exactly: `k=4` gives `excess 7 = 2·3+1`, `k=6` gives
`excess 11 = 2·5+1`. And the violating subspaces sit at `d = k−1`, far above the `d = ⌈k/2⌉−1` the
counting bound actually uses.

**What that costs.** Redoing the counting with `excess ≤ 2d+1` instead of `2d`: needing
`excess ≥ k` gives `2d+1 ≥ k`, so

| | bound obtained | previously claimed |
|---|---|---|
| **even `k`** | `d ≥ k/2` | `⌈k/2⌉` — **unchanged** |
| **odd `k`** | `d ≥ (k−1)/2` | `⌈k/2⌉` — **one short** |

For even `k` the argument survives intact, because `(k−1)/2` is not an integer and `d` must round
up to `k/2`. For odd `k` it genuinely weakens by one.

**Measured values still exceed the weakened bound**: tri-cycle `k=3,5,7` give `d_cb = 2,3,4` where
the repaired bound only proves `1,2,3`. So the conclusion `d_cb = ⌈k/2⌉` remains true everywhere
measured; it is the *proof* that now covers only even `k`.

**Status.** `excess ≤ 2d` is refuted. `excess ≤ 2d+1` is a conjecture fitted to the two
counterexamples and the cycle mechanism, not proved — and it is the weakest link, since everything
above now rests on it. The `d = 1` case (§17) is unaffected and remains proved.

## 21. `excess ≤ 2d+1` is false as well; the true shape is `2d + c`

The repair of §20 lasted one experiment. Disjoint copies of tri-cycle `k=4`, taking three pair-sums
from each block:

| blocks | `k` | `r` | `\|D\|` | `dim R` | excess | `2d` | `2d+1` | `2d+c` |
|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 8 | 12 | 3 | 7 | 6 | 7 | 7 |
| **2** | 8 | 16 | 24 | 6 | **14** | 12 | **13** | 14 |

Two blocks exceed `2d+1`. The prediction was additive and stated in advance — `d_cb` and the class
structure add over coordinate-disjoint blocks, so two copies of an excess-7 configuration at `dim 3`
must give excess 14 at `dim 6`.

**The general form.** Writing `E` for the number of merge-carrying pair-sum lines lying in `R` and
`c` for the cycle rank of the graph they form, unsigned incidence gives `d = E − c`, each such line
carries two merges, and each independent cycle costs one coincidence:

> **`excess = 2E − c = 2d + c`.**

Both counterexamples match exactly: one block `2·3+1 = 7`, two blocks `2·6+2 = 14`. `excess ≤ 2d`
and `excess ≤ 2d+1` were the `c = 0` and `c = 1` cases, and there is no reason for `c` to stop at 1.

**What this threatens.** Since `2d + c = d + E`, the counting requirement `excess ≥ k` becomes
`d + E ≥ k`. A configuration with many pair-sum lines on few coordinates makes `E` large while `d`
stays small. Counting crudely: the pairs must lie in triangles, a linear system puts at most
`V'(V'−1)/2` triangle-pairs on `V'` coordinates, and `V' ≈ d+1`, giving `E ≲ d(d+1)/2`. Then
`d + E ≥ k` is satisfiable once `d² ≳ 2k`, i.e.

> the counting argument may only give **`d_cb ≳ √(2k)`**, not `⌈k/2⌉`.

**That is an estimate, not a result.** It assumes such dense linear configurations exist, that their
pair-sums all lie in a `d`-dimensional space, and that the resulting `R` passes `valid_R` — none of
which is checked. Every object measured in this campaign still has `d_cb ≥ ⌈k/2⌉`, and the star's
`k−1` and the disjoint family's `m` are proved theorems well above `√(2k)`.

**Status of the counting bound.** It is now unsupported at every `k`, not merely at odd `k`. What
survives untouched: `excess ≤ 2` at `d = 1` (proved, §17), which is the `c = 0`, `E = d = 1` case;
the star and disjoint theorems, which never used this argument; and every measured value. The
honest reading is that `d_cb ≥ ⌈k/2⌉` is now a conjecture supported by measurement rather than a
bound with a derivation behind it.

**The test that would settle it** is a deliberately dense linear configuration — many triangles
packed onto few coordinates so that `E` is quadratic in `d` — checked for whether its excess really
reaches `k` at `d` well below `k/2`, and whether such an `R` passes `valid_R`.

## 22. The Fano plane has an empty fibre, and that may be what saves the counting bound

§21 argued that `excess = 2d + c` lets a *dense* linear system push `d` down toward `√(2k)`, since
`2d + c = d + E` and a dense configuration makes `E` large while `d` stays small. The extreme case
of a dense linear system is the **Fano plane**: 7 triples on 7 points, every pair in exactly one
triple, any two triples meeting in exactly one point. Its pair graph is the complete graph `K7` —
all 21 pairs are merge-carrying — which is as dense as a linear system on 7 points can be.

Measured:

> **`|A| = 0`.**

The Fano plane admits no valid sign vector at all. This is the classical fact that the Fano plane
is not 2-colourable — its hypergraph chromatic number is 3 — so every `±1` assignment leaves some
line monochromatic, and the fibre is empty.

**Why that matters here.** `d_cb` is not defined on an empty fibre, so the densest linear system
cannot be used against the counting bound. More generally the threat in §21 requires a linear system
that is simultaneously dense enough for `E` to be quadratic in `d` *and* 2-colourable enough to have
a spanning fibre, and those pull against each other: packing triples tightly onto few points is
exactly what forces a monochromatic line.

So the `√(2k)` estimate may be self-limiting. That is a reason to expect the counting bound to
survive, not a proof that it does — the relationship between density, 2-colourability and the
achievable `E` is not worked out here, and partial Steiner systems sparser than Fano may still have
both properties.

**What this does not change.** `excess ≤ 2d` and `excess ≤ 2d+1` remain refuted, on tri-cycles,
which have perfectly good non-empty fibres. The counting bound remains without a derivation. What
the Fano result removes is the specific route by which the damage looked unbounded.

## 23. The excess formula, derived — and it explains both the bound and its failure

`excess = 2d + c` was fitted to two counterexamples. It follows from a derivation, and the derived
form is sharper.

**The derivation.** A pair-sum line `e_x + e_y` whose pair lies in a triangle `t` contributes exactly
two merges (§17, proved): the triangle merge `f_t ∼ e_a` with `a` the third coordinate, and the
coordinate merge `e_x ∼ −e_y`. Suppose `R` contains at most one pair-sum per triangle, so the
triangle merges are distinct. Then the coordinate merges are exactly the **edges of the pair-sum
graph** `G`, and a spanning forest of `G` loses one edge per independent cycle. Writing `E` for its
edges, `V'` for the coordinates it touches, `comp` for its components and `b` for its bipartite
components:

> **`excess = E + (V' − comp)`**,  and  **`dim R = V' − b`**

the second because unsigned incidence vectors of a graph have rank `V' − b`.

**Verified: 618 of 618** pair-sum subspaces of dimension `≤ 3` across star `k=3`, chain `k=4`,
tri-cycle `k=3,4`, `(2,1)` `k=4` and disjoint `m=2`. Zero mismatches.

**Why `excess ≤ 2d` is a statement about forests.** Substituting,

  `excess ≤ 2d`  ⟺  `E + V' − comp ≤ 2V' − 2b`  ⟺  `E ≤ V' + comp − 2b`.

For a **forest**, `E = V' − comp`, and the condition becomes `V' − comp ≤ V' + comp − 2b`, i.e.
`b ≤ comp` — always true. So

> **`excess ≤ 2d` holds exactly when the pair-sum graph in `R` is a forest**, and can fail as soon
> as it carries a cycle.

That is the entire story of §§19–21 in one line. The tri-cycle counterexample is the 4-cycle
`0−2−4−6−0`: `E = 4`, `V' = 4`, `comp = 1`, so `excess = 4 + 3 = 7`, while `b = 1` gives `d = 3`.
The two-block version doubles it: `E = 8`, `V' = 8`, `comp = 2`, `excess = 14`, `d = 6`.

**Two hypotheses this needs, both found by testing rather than assumed.** First, one pair-sum per
triangle: two pair-sums of the *same* triangle share `f_t`, their merges collapse, and the count is
wrong — the check caught this at `[(0,2),(1,2)]` on star `k=3`, actual 3 against a predicted 4.
Second, `E` counts the pair-sum lines lying **in `R`**, not the ones chosen to span it — a cycle
closure pulls extra pair-sums in, which is exactly what makes the counterexample a counterexample,
and measuring the generators instead of the subspace produced the single mismatch in the first
corrected run.

**What it does not do.** It says nothing about non-pair-sum directions, which carry at most one
merge each, and nothing about whether an `R` achieving a given excess passes `valid_R`. And it does
not restore the counting bound: it explains precisely when that bound's lemma holds, and cyclic
pair-sum graphs remain outside it.

## 24. Why the density threat cannot be realised: two barriers, not one

> **Superseded in part by §30.** The two barriers are real, but the explanation below - "density
> erodes the fibre" - is wrong as stated, and the sample here (seven systems) is too small to carry
> it. §30 re-measures this on 6,124 systems plus complete enumeration for `r = 4..8`: most
> non-spanning is the arithmetic cap `|A| < 2r`, the genuine obstruction is always a single pair
> forced antipodally *inside* a triple, and the collapse is neither a parity nor a density effect.
>
> **And the central conclusion below is refuted by §33.** The claim that the `√(2k)` estimate is
> "structurally obstructed" is false. This section measured *random maximal* partial Steiner systems,
> where density does destroy the fibre; a structured construction keeps the density in the chosen
> pair-graph while hub points keep the triple system sparse and 2-colourable. `K_{5,5}` has
> `k/r = 1.67`, deep in the regime called empty here, yet `|A| = 186`, the fibre spans, and
> `d_cb ≤ 9` against `⌈k/2⌉ = 13`. The `√k` degradation is realisable.


§21 argued that `excess = 2d + c = d + E` lets a dense linear system reach `excess >= k` at `d` well
below `⌈k/2⌉`, degrading the counting bound toward `√(2k)`. §22 noted the Fano plane blocks the
extreme case by having an empty fibre. Searching the space properly - maximal partial Steiner
systems (linearity is exactly "every pair in at most one triple") built greedily from many random
orders on `r = 7, 8, 9`:

| `r` | `k` | `k/r` | `\|A\|` | spans | `d_cb` | `⌈k/2⌉` | |
|---|---|---|---|---|---|---|---|
| 7 | 7 | 1.00 | **0** | — | — | 4 | not 2-colourable (the Fano plane) |
| 9 | 12 | 1.33 | **0** | — | — | 6 | not 2-colourable |
| 9 | 10 | 1.11 | **0** | — | — | 5 | not 2-colourable |
| 8 | 8 | 1.00 | 6 | **no** | — | 4 | fibre non-spanning |
| 8 | 7 | 0.88 | 16 | **no** | — | 4 | fibre non-spanning |
| 9 | 9 | 1.00 | 10 | **no** | — | 5 | fibre non-spanning |
| 7 | 5 | 0.71 | 24 | yes | **3** | 3 | bound holds |

**No 2-colourable linear system was found with `d_cb` below `⌈k/2⌉`.** Every system dense enough to
threaten the bound failed to be an object at all.

**And it fails in two distinct ways, which matters.** The first barrier is 2-colourability: pack
triples tightly enough and some line is forced monochromatic, so `A` is empty. The second is
sparser and was not anticipated - a system can be 2-colourable (`|A| = 6, 16, 10`) and still have a
fibre that does not **span**, in which case `d_cb` is undefined because there is no coordinate basis
to draw from. Density erodes the fibre before it erodes the bound.

~~**So the `√(2k)` estimate of §21 is not merely unrealised, it is structurally obstructed.**~~ **False - see §33:** `d_cb ≤ 2√k − 1` is attained by `K_{q,q}` for odd `q`, with a spanning fibre throughout. The
count there assumed `E ≲ V'(V'−1)/2` triangle-pairs could sit on `V'` coordinates *and* the object
remain a usable fibre. Those requirements are in tension: `E` large forces the triples to cover
nearly every pair, which is exactly the regime where 2-colourability fails and, before that, where
the surviving sign vectors stop spanning.

**What this is.** Seven systems at `r = 7, 8, 9`, only one of them usable, so it is a structural
signal and not a proof - the sample of *usable* dense systems is one. What it does is remove the
specific mechanism by which the broken lemma looked like it could destroy the conclusion, and it
names the two obstructions a real proof would have to formalise.

**Standing:** `excess ≤ 2d` is still false and the counting bound still has no derivation. But the
bound's conclusion is no longer threatened by the density route, and every object measured in this
campaign continues to satisfy `d_cb >= ⌈k/2⌉`.

## 25. On usable linear systems the bound is not merely valid, it is attained

§24 showed dense linear systems are unusable. The complementary question is what happens on the
usable ones, so the sweep was widened: partial Steiner systems at every size from small to maximal,
`r = 6…10`, many random instances each, keeping those whose fibre is non-empty and spans.

Across every usable system measured so far, **`d_cb >= ⌈k/2⌉` holds with no exception**, and the
slack is almost always **zero**:

| `r` | `k` | `k/r` | `d_cb` | `⌈k/2⌉` | slack |
|---|---|---|---|---|---|
| 6 | 2, 3, 4 | 0.33–0.67 | 1, 2, 2 | 1, 2, 2 | **0** |
| 7 | 2, 3, 4, 5 | 0.29–0.71 | 1, 2, 2, 3 | 1, 2, 2, 3 | **0** |
| 8 | 3, 4, 5 | 0.38–0.62 | 2, 2, 3 | 2, 2, 3 | **0** |
| **8** | **2** | 0.25 | **2** | 1 | **+1** |

**The one row with slack is the known exception, and it arrives unprompted.** `r=8, k=2` is two
*disjoint* triples on eight points, and the proved theorem gives `d_cb = m = 2` against a floor of
1. So the random search reproduces the disjoint family's excess over the bound rather than
flattening everything onto the floor - which is the check that the sweep is measuring something
real.

**The shape this gives.** The counting bound is *attained* by typical linear systems - the ones a
random partial Steiner construction produces, which are spread out and connected - and *exceeded*
by exactly the two structured families the campaign already knows about: disjoint unions (`m`, by
theorem) and stars (`k−1`, by theorem). A random construction essentially never produces a star,
which is why every non-disjoint row sits exactly on the floor.

That is a more useful statement than "the bound holds". It says the bound is the generic answer and
the campaign's two theorems are the structured exceptions above it - and it means any proof of
`d_cb >= ⌈k/2⌉` cannot afford slack, because on most objects there is none.

**Still not a derivation.** `excess ≤ 2d` remains false and the bound remains without one. This is
evidence about where the truth sits, gathered on objects generated independently of the families
that shaped the conjecture.

## 26. The repaired counting bound, with its correction term

The derived excess formula gives back a bound - not the original one, but the original plus an
explicit correction that says exactly when it degrades.

**The derivation.** With `c = E − V' + comp` the cycle rank of the pair-sum graph inside `R`:

  `V' − comp = E − c`, so `excess = E + (V' − comp) = 2E − c`, and `d = V' − b = E − c + comp − b`.

Validity requires `excess ≥ k`, i.e. `2E − c ≥ k`, i.e. `E ≥ (k+c)/2`. Substituting,

> **`d ≥ k/2 − c/2 + nb`**,  where `nb = comp − b` counts the **non-bipartite** components.

**Verified: 0 identity mismatches over 618 subspaces, and 0 violations over 515 valid ones**, across
star `k=3`, chain `k=4`, tri-cycle `k=3,4`, `(2,1)` `k=4`, disjoint `m=2,3`. Both identities
(`excess = 2E − c` and `d = E − c + comp − b`) matched the measured values every time.

**Odd cycles help, even cycles hurt.** A non-bipartite component carries an odd cycle and
contributes to both `c` and `nb`, and the two cancel favourably - if every component has exactly one
odd cycle then `c = nb` and `d ≥ k/2 + nb/2 ≥ k/2`, so the original bound survives untouched. A
bipartite component's cycles add to `c` alone and cost `1/2` each. **That is why the counterexample
used a 4-cycle.** tri-cycle `k=4` has `E=4, V'=4, comp=1, c=1, b=1, nb=0`, giving `d = 3` and
`excess = 7` exactly as measured, with the bound reading `d ≥ 2 − 0.5 = 1.5`, hence `d ≥ 2` - which
the true `d_cb = 2` satisfies.

**So the original bound's status is now precise:**

> `d_cb ≥ ⌈k/2⌉` holds whenever `c ≤ 2·nb` — when the pair-sum graph's cycles are mostly odd.

That is a checkable structural condition rather than a hope, and it explains every measurement in
this note: forests have `c = 0` and are safe; odd-cycle structures are safe; only even cycles cost,
and they cost half a dimension each.

**A resonance worth recording.** The fibre is non-empty iff the triple system is 2-**colourable**
(§22, §24), and the bound degrades through **bipartite** - that is, 2-colourable - cycles in the
pair-sum graph. Two-colourability governs both the existence of the object and the strength of the
bound on it, in opposite directions: colourability of the triples is needed for the fibre to exist,
while colourability of the pair graph is what weakens the bound. Whether that is a coincidence of
two unrelated parity conditions or one phenomenon seen twice is not settled here, and it is the most
interesting question this section raises.

**Scope, stated plainly.** This covers `R` spanned by pair-sums with at most one per triangle. A
non-pair-sum direction carries at most one merge (§17, proved), so it cannot help reach the maximal
excess a tight bound needs - but that is an argument, not a proof, and the general statement is not
established. `excess ≤ 2d` remains false; what replaces it is this inequality, which is weaker in
general and equal to it exactly when `c ≤ 2·nb`.

## 27. The failure is a parity phenomenon, predicted in advance and confirmed exactly

The repaired bound says even cycles cost and odd cycles do not. On tri-cycles that becomes a
statement about `k` itself, because under the one-pair-sum-per-triangle hypothesis a cycle in the
pair-sum graph uses one pair from each of `L` different triples, so **cycle length = number of
triples**. The hub cycle of a tri-cycle of `k` triangles has length `k`, and unsigned incidence rank
is `V' − b`:

- **`k` even** — the hub cycle is bipartite, `b=1`, `nb=0`: `d = k−1`, `excess = 2k−1`, so
  `excess − 2d = +1`, a violation of `excess ≤ 2d`;
- **`k` odd** — the hub cycle is odd, `b=0`, `nb=1`: `d = k`, `excess = 2k−1`, so
  `excess − 2d = −1`, no violation.

Predicted before running, for all three quantities:

| `k` | parity | predicted `d` | predicted excess | measured `d` | measured excess | `2d` | violates |
|---|---|---|---|---|---|---|---|
| 4 | even | 3 | 7 | **3** | **7** | 6 | **yes** |
| 5 | odd | 5 | 9 | **5** | **9** | 10 | no |
| 6 | even | 5 | 11 | **5** | **11** | 10 | **yes** |
| 7 | odd | 7 | 13 | **7** | **13** | 14 | no |
| 8 | even | 7 | 15 | **7** | **15** | 14 | **yes** |

**Fifteen numbers predicted, fifteen correct.** Not merely the verdicts: the exact dimension and the
exact excess for every `k`, from the formula alone.

**So the counterexamples were never arbitrary.** `excess ≤ 2d` fails on tri-cycle `k=4` and `k=6`
because 4 and 6 are even, and it holds on `k=5` and `k=7` because 5 and 7 are odd. The two
counterexamples this note was built on are the first two members of a family whose membership rule
is a parity condition — and the same rule says `k=8` violates, which it does, and that `k=9` will
not.

This completes the account of the broken lemma. `excess ≤ 2d` is false; it is false exactly when the
pair-sum graph carries an even cycle; on tri-cycles that is exactly when `k` is even; and the
repaired bound `d ≥ k/2 − c/2 + nb` prices the failure at half a dimension per even cycle. What
began as a counterexample that invalidated a derivation has ended as a derivation that predicts its
own counterexamples.

## 28. The two appearances of 2-colourability are one theorem

§26 left the most interesting question open: two-colourability governs both whether the object
exists (the triples must be 2-colourable, §22/§24) and how strong the bound on it is (bipartite
cycles in the pair graph cost half a dimension each, §26/§27), in opposite directions. Those are
the same condition.

> **Theorem.** For a triple system `T`, the fibre is non-empty **iff** some choice of one pair per
> triple yields a **bipartite** pair graph.

**Proof, both directions elementary.**

*(⇐)* Suppose a one-pair-per-triple choice is bipartite, and 2-colour its vertices so every chosen
edge is bichromatic. Every triple owns a chosen pair, so every triple contains two points of
different colours and is therefore not monochromatic. Reading the colouring as `±1` gives a valid
sign vector, so `A` is non-empty.

*(⇒)* Suppose `s ∈ A`. No triple is monochromatic, so every triple contains at least one pair whose
two points differ under `s`. Choose one such pair per triple. Every chosen edge is bichromatic under
`s`, so `s` is a proper 2-colouring of the chosen graph, which is therefore bipartite. ∎

**Verified on 13 systems, all agreeing**, with the sharpest case exhaustive: the Fano plane has
`|A| = 0`, and all `3^7 = 2187` one-pair-per-triple choices were checked and **none** is bipartite.
Stars, chains, tri-cycles `k=3…6`, disjoint unions, books and wheels all have both properties.

**What it explains.** The structure that makes a triple system *exist* as an object of this theory is
the same structure that *weakens* the counting bound on it:

- no bipartite choice → no valid sign vector → no fibre → `d_cb` undefined. That is exactly why
  dense systems are unusable (§24), and why Fano is not merely awkward but absent.
- a bipartite choice exists → the fibre exists → but bipartite graphs are precisely the ones whose
  cycles are even, and even cycles are what cost `1/2` a dimension each in `d ≥ k/2 − c/2 + nb`.

So the tension is structural rather than coincidental. **Existence and tightness are governed by the
same parity condition, pulling opposite ways.** A system too far from 2-colourable has no fibre; a
system comfortably 2-colourable offers `R` the even cycles that erode the bound.

**One thing this does not say.** That a bipartite choice *exists* is not the same as `R` *using* one:
a bipartite pair graph with no cycles is a forest, `c = 0`, and costs nothing. The theorem says
bipartiteness is available whenever the object exists; whether a particular `R` realises an even
cycle is a separate question, and on tri-cycles §27 answers it by the parity of `k`.

### Machine-check of §28, including the direction that matters

The proof uses no linearity, so the theorem should hold for arbitrary triple hypergraphs — a
stronger claim than the 13 hand-picked systems supported, and stating a theorem more generally than
it was tested is how false steps have entered this campaign before. So it was checked on random
systems.

**The first attempt was worthless and it is worth saying why.** Drawing `k ∈ {4,…,7}` on `r ∈ {5,6,7}`
gave 120 systems with **zero** empty fibres. The `(⇐)` direction is only interesting when *no*
bipartite choice exists, which requires `|A| = 0`, which requires density — so the generator could
not emit the case the claim is about. That is the same generator-support failure this session
recorded hours earlier, arriving in my own test of my own theorem.

Redrawn in the dense regime (`k` from about a third of `C(r,3)` up to 14):

| | count |
|---|---|
| systems tested | 120 |
| **with `\|A\| = 0`** | **10** |
| disagreements | **0** |

Every one of the ten empty-fibre systems also has **no** bipartite one-pair-per-triple choice, and
every one of the 110 non-empty systems has one. All 120 are **non-linear**, so the theorem is
confirmed in the generality the proof claims rather than only on the linear systems the campaign
studies. With the Fano plane's exhaustive 2,187-choice check, both directions are now exercised.

## 29. What this says about the dossier's own standing hypotheses

The dossier opens its DEFINITIONS with the object everything else rests on:

> "A central deterministic object is a **nonempty** antipodal sign fibre `A ⊆ {±1}^r`, `A = −A`,
> **usually assumed spanning** and full closed."

Both properties are hypotheses there, never characterised. "Nonempty" occurs ten times in two
hundred pages and every occurrence assumes it. The document has no discussion of 2-colourability,
Property B, bipartiteness or monochromatic triples — searched, zero occurrences of any of them.

This campaign has now probed both assumptions, and they turn out to be independent.

**Nonemptiness is characterised (§28).** For a triple system the fibre is exactly the set of
not-all-equal assignments, so `|A| > 0` is hypergraph 2-colourability — classical in itself — and
the theorem gives a combinatorial criterion in the campaign's own vocabulary: **non-empty iff some
choice of one pair per triple has a bipartite pair graph.** Proved both ways, machine-checked on
120 random systems including 10 with empty fibres, and exhaustively on the Fano plane's 2,187
choices.

**Spanning fails separately, and that was not anticipated (§24).** Dense systems were found that
*are* 2-colourable — `|A| = 6, 16, 10`, so non-empty — whose fibres nevertheless do **not span**,
leaving `d_cb` undefined for want of a coordinate basis. So the dossier's two clauses are not one
condition with a weak and a strong form: a system can satisfy the first and fail the second, and
between them they cut off the dense regime twice over.

**Why this matters for the programme rather than only for the bookkeeping.** The dossier's whole
Layer II converts entropy loss into residual directions *given* a nonempty spanning fibre. The
question of which triple systems supply one is not addressed there, and this campaign's density
results say the answer is restrictive: pack the triples tightly and the object stops existing, first
by losing its span and then by losing 2-colourability. Any argument that ranges over "all sign
fibres" is quietly ranging over a set with these two obstructions built in — and §28 says the first
of them is the same parity condition that governs how tight the counting bound can be.

That is the sharpest link this campaign has to the document: not another agreement on a computed
value, but a characterisation of an assumption the document makes and does not examine.

## 30. The second barrier, measured properly: what non-spanning actually is

§24 rested on seven systems found by a greedy random search, one of them usable. That is thin for a
claim about a whole regime, and re-running it at scale changes what it says.

**The sample.** Maximal partial Steiner systems - every pair in at most one triple, grown until no
further triple fits - regenerated across `r = 7..13`, 6,124 distinct systems, plus **complete
enumeration** for `r = 4..8`. Four outcomes are separated: empty fibre; fibre non-empty but smaller
than `2r`; fibre large enough to span but not spanning; spanning.

**First correction: most of §24's "second barrier" is arithmetic, not structure.** `A` is antipodal,
so it consists of `|A|/2` antipodal pairs, and `±s` contribute one direction between them. Hence
`rank(A) ≤ |A|/2` and spanning is impossible outright once `|A| < 2r`. Two of §24's three
non-spanning rows are of that kind: `|A| = 6` at `r = 8` caps the rank at 3, `|A| = 10` at `r = 9`
caps it at 5. Those fibres did not fail to span for a structural reason - they were too small to
span anything. At scale, 346 of 605 non-spanning cases are explained by the cap alone.

**But the barrier is real.** 259 systems have `|A| ≥ 2r` and still fail, so spanning was
arithmetically available and something obstructed it. On complete enumeration at `r = 8` the figure
is 10,080 of 16,200.

**Second correction: the obstruction has exactly one shape.** Over every structural failure, all 407
independent relations satisfied by the whole fibre have **support 2**. There is no wide dependency
anywhere - the obstruction is always a coordinate identification. Moreover every forced pair `{i,j}`
lies **inside a triple**, and the identification is `s_i = −s_j`: the pair is pinned antipodally by
the rest of the system, and its triple is then not-all-equal for free, whatever the third coordinate
does. Density does not erode the fibre here, as §24 put it. It over-determines one pair inside it.

Codimension is 1 in 377 of 387 cases and **3** in the remaining 10, never 2. The codimension-3 cases
are all one object (25 of 25 in a second sweep): three coordinates forced mutually equal and a
fourth forced opposite to all three, `s_a = s_b = s_c = −s_x`, four coordinates carrying one degree
of freedom. Forced-*equal* never appears alone - only inside that quadruple - which fits the cost
argument: pinning `s_i = s_j` inside a triple `{i,j,x}` forces `s_x = −s_i` as well, so it cannot be
bought for one dimension the way forced-opposite can.

**Third, and this is the part that was not suspected.** Complete enumeration says:

| `r` | maximal systems | mean `k` | `k/r` | empty | capped | structural | **spanning** |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 1.00 | 0.25 | 0% | 0% | 0% | **100%** |
| 5 | 15 | 2.00 | 0.40 | 0% | 0% | 0% | **100%** |
| 6 | 40 | 3.50 | 0.58 | 0% | 0% | 0% | **100%** |
| 7 | 450 | 5.13 | 0.73 | 7% | 0% | 0% | **93%** |
| 8 | 16,200 | 7.05 | 0.88 | 1% | 36% | 62% | **0%** |
| 9 | sampled | 9.4 | 1.04 | 38% | 53% | 1% | **8%** |
| 10 | sampled | 11.8 | 1.18 | 47% | 53% | 0% | **rare: 22 of 23,995** |
| 11–13 | sampled | — | 1.33–1.63 | 87→100% | 13→0% | 0% | **none found** |

**Not one maximal partial Steiner system on 8 points has a spanning fibre** - all 16,200 checked,
not sampled. That row is a complete enumeration and is the only zero here entitled to be read as
impossibility; the `r ≥ 11` zeros are sampled and mean "none found". The `r = 7` row is the control for that zero and reproduces the sampler's 93%, so the
detector demonstrably finds spanning systems when they exist.

**Two readings of that zero, both refuted.** Parity looked promising, since in `K_r` each point has
degree `r−1` and each triple through a point covers two pairs there, so for even `r` every point
keeps an odd - hence nonzero - number of uncovered pairs. But `r = 4` and `r = 6` span 100%, so
"even `r` never spans" is false. Density is also not it, and fails on a direct comparison: `r = 9`
with `k = 8` is **denser** than `r = 8` with `k = 7` (`k/r` 0.889 against 0.875) yet spans 69% where
the other spans 0%. The cliff is non-monotone in both `r` and density.

**What the zero is not.** It is a statement about *maximal* systems only. Sparse linear systems on 8
points - the star, the chain, disjoint triples - all span. So nothing here says 8 coordinates are
inhospitable; it says that on 8 points, being maximal is incompatible with being usable.

**Standing.** §24's conclusion survives and is stronger: no 2-colourable linear system was found
with `d_cb` below `⌈k/2⌉`, now over 6,124 systems rather than seven, and the usable fraction
falls off a cliff at `r = 8` and never recovers past a fraction of a percent.

> **Corrected the same night.** An earlier version of this section said the usable fraction "collapses
> to zero by `r = 10` and stays there". That was a sampling artefact: a 1,200-draw sweep found no
> spanning system at `r = 10`, but a wider search over 23,995 distinct maximal systems found **22**,
> each re-verified independently (no addable triple, maximum pairwise intersection 1, `|A| = 32 ≥ 2r`,
> rank 10). At `r = 10` usable objects are rare - about one in a thousand - not absent. The `r = 8`
> zero is exhaustive and unaffected. What changes is the explanation. The density story in
§24 is wrong as stated - the obstruction is a forced antipodal pair inside a triple, and the
regime where usable objects exist is bounded by something that is neither parity nor density.
Identifying it is open.

## 31. The r = 8 zero, explained: two windows that fail to meet

§30 left the collapse unexplained after parity and density both died. The explanation is a race
between two counts that pull on the triple number `k` from opposite sides.

Define, for a fixed number of coordinates `r`,

- `U(r)` = the largest `k` such that **some** partial Steiner system on `r` points has a spanning
  fibre. Every triple is another constraint, so past `U(r)` nothing spans.
- `L(r)` = the smallest `k` such that **some maximal** partial Steiner system on `r` points exists.
  Maximality is a floor: you must keep adding triples while any pair-disjoint triple remains.

**The one-way implication.** Any spanning system has `k ≤ U(r)`; any maximal system has `k ≥ L(r)`.
So if `L(r) > U(r)`, no system can be both, and **no maximal system is usable**. The converse does
not follow - an overlap only means the two windows share a value of `k`, not that a single system
realises both - so this argument proves the zeroes and merely permits the positives.

**Measured, exactly.** `U` is computed by carrying the fibre down the search as bitmasks and pruning
at `|A| < 2r`; the pruning is exact for this purpose because the fibre only shrinks as triples are
added and `rank(A) ≤ |A|/2`, so nothing below the cut could have spanned. `L` comes from the
complete enumeration of maximal systems in §30.

| `r` | `U(r)` | `L(r)` | windows | usable maximal systems |
|---|---|---|---|---|
| 7 | 5 | 5 | meet at `k = 5` | 420 of 450 |
| 8 | 6 | 7 | **disjoint** | **0 of 16,200** |

At `r = 7` the maximal systems occur at `k = 5` and `k = 7`; the window meets the first and misses
the second, and that is exactly the split observed - all 420 of the `k = 5` systems span, and the 30
at `k = 7` are the Fano planes with empty fibres. At `r = 8` maximality forces `k ∈ {7, 8}` while
spanning dies after `k = 6`. The windows miss each other by one, and the zero follows.

**So the r = 8 collapse is not a property of 8 coordinates.** A spanning system on 8 points with
`k = 6` exists - `{012, 034, 056, 135, 146, 237}` is one - but it is not maximal, and every way of
extending it to maximality pushes `k` past the spanning ceiling. The obstruction is that on 8
points, the cheapest maximal system is already one triple too expensive.

**Where this leaves the regime.** `U(9) = 9`, computed exactly over 21,066,170 search nodes, and
maximal systems at `r = 9` start at `k = 8`, so the window is `k ∈ {8, 9}`. That is precisely where the
usable objects are: spanning maximal systems occur at `k = 8` (69%) and `k = 9` (7%) and at no other
`k` - `k = 10` and `k = 12` give none. The framework predicts the `r = 9` data exactly rather than
merely permitting it. Whether the
framework also accounts for the near-vanishing at `r ≥ 10` - rare at `r = 10`, none found beyond - is open and needs `L` there, which is the
minimum size of a maximal partial Steiner triple system - a quantity with no closed form here. The
Turán bound `3k ≥ \binom{r}{2} − ⌊r²/4⌋` (the uncovered pairs must be triangle-free) gives only
`L(8) ≥ 4` against the true 7, so it is far too weak to settle it.

**Standing.** The `⌈k/2⌉` counting bound is untouched by any of this - every object in the campaign
still satisfies it. What §30 and §31 settle is the shape of the *usable* regime the bound has to
range over, and it is narrower and stranger than §24 supposed.

## 32. `|D| = r + k` is false for linear systems, and the counting bound falls with it

§13 states the campaign's counting bound this way: for a linear system of `k` triangles on `r`
coordinates, `D` is the `r` coordinate forms plus one form per triangle, so `|D| = r + k`, the excess
that must be bought is exactly `k`, and therefore `d_cb ≥ ⌈k/2⌉` for every linear triangle system.
§16 reinforced it, recording wheel `k=3` as the only object whose dual exceeds `r + k` and noting
that it is non-linear.

Both statements are false. The dual can exceed `r + k` on linear systems, and when it does the
bound goes with it.

**The mechanism.** A linear system can *imply* not-all-equal constraints on triples that are not in
it. Each implied triple contributes a dual form, and the derivation counted only the `k` listed
triangles. Nothing about linearity prevents this: linearity constrains which pairs may be shared,
not which constraints are entailed.

**The construction.** Take any bipartite graph `H` and give each edge `{x,y}` a triple `{x,y,z}`.
Two triples may share their third point provided their `H`-edges are disjoint, so one fresh point
serves an entire matching. Decomposing `K_{p,q}` into `q` matchings gives a linear system with
`k = pq` triples on `r = p + 2q` points. The fibre is never empty - colour `H` by its bipartition and
every triple is not-all-equal whatever the third coordinate does.

| member | `k` | `r` | `\|A\|` | `\|D\|` | `r+k` | dim `R` | classes | excess | `⌈k/2⌉` | |
|---|---|---|---|---|---|---|---|---|---|---|
| `K_{2,2}` (Pasch) | 4 | 6 | 18 | **14** | 10 | 3 | 3 | 11 | 2 | bound holds |
| `K_{2,3}` | 6 | 8 | 40 | **20** | 14 | 4 | 4 | 16 | 3 | bound holds |
| `K_{3,3}` | 9 | 9 | 42 | **36** | 18 | 5 | 4 | 32 | 5 | bound holds |
| `K_{3,4}` | 12 | 11 | 82 | **47** | 23 | 6 | 5 | 42 | 6 | bound holds |
| `K_{4,4}` | 16 | 12 | 90 | **76** | 28 | **7** | 5 | 71 | **8** | **`d_cb ≤ 7 < 8`** |

Every member is linear - maximum pairwise intersection 1, checked on the printed triples - and every
member has a spanning fibre. Every member violates `|D| = r + k`, the smallest being the **Pasch
configuration** `{024, 035, 125, 134}`, four blocks on six points with each point in exactly two. It
is one of the most familiar configurations in design theory and it was simply never tested here.

At `K_{4,4}` the failure reaches the bound itself. The pair-sums of `H` span a 7-dimensional `R`
which collapses the 76 dual forms to 5 classes - well inside the `r = 12` ceiling - and those classes
admit a linearly independent transversal, so `R` is valid and `d_cb ≤ 7` while `⌈k/2⌉ = 8`.

**How this was checked.** `full_dual` reproduces `|D| = r + k` on star `k=3,4`, chain `k=4`,
tri-cycle `k=4` and disjoint `m=2`, so the enlarged duals are not an artefact of a broken routine.
`|A|` was recounted independently of the library. Validity was re-derived by a second implementation
that takes the quotient by projection onto a complement of `R` rather than by row-reduction, with an
independent transversal search; the two agree on every row. And `e₁+e₄+e₈` was evaluated over the
whole fibre of `K_{4,4}`: it takes only the values `±1`, while `{1,4,8}` is not a triple of the
system - an implied constraint, seen directly.

**What survives.** Conjecture RC is untouched, and these objects are comfortably inside it:
tightness `d_cb·β/ℓ` is 0.68, 0.58 and 0.53 for `K_{2,2}`, `K_{3,3}`, `K_{4,4}`. The refutation is
of an internal lemma, not of the programme's target. What it removes is the claim that `⌈k/2⌉` is a
theorem for linear systems - it is a theorem for linear systems **whose dual is exactly `r + k`**,
which is a hypothesis that has to be checked rather than inherited from linearity.

Nor does the natural repair work. Replacing `k` by `|D| − r` would ask for `d_cb ≥ 32` on `K_{4,4}`,
against a measured `d_cb ≤ 7`; the excess there is 71 at `d = 7`, a ratio of about ten, which is the
same wall `excess ≤ 2d` hit in §19 and §21, only far higher.

**Standing.** Every object in §§1-31 satisfies `d_cb ≥ ⌈k/2⌉` and those measurements are unaffected.
What changes is that the bound is no longer proved for the class it was claimed for, and the honest
statement of the open problem now includes: which linear systems have `|D| = r + k`?

## 33. How badly the counting bound fails, and what it does not touch

§32 exhibited one linear system below `⌈k/2⌉`. The failure is not a near miss at one size.

**The Pasch reading, and its limit.** The smallest system with extra dual forms is the Pasch
configuration `{024, 035, 125, 134}`, and its four extras are the triples `{124}, {025}, {034},
{135}` - the other Pasch on the same six points. That suggested a clean criterion: extra forms
exactly when a Pasch is present. Half of it holds. Over the objects surveyed, a Pasch always
produces extras (no counterexample), but Pasch-freeness does **not** protect: `K_{2,3}` and
`K_{3,3}` are Pasch-free with 6 and 18 extras. So "anti-Pasch" is necessary for `|D| = r + k` on
this evidence, and nowhere near sufficient.

**The extras are also more varied than §32 said.** In the `K_{p,q}` family every extra form is
`e_x+e_y+e_z` - an implied not-all-equal triple, and `e₁+e₄+e₈` was checked directly against the
whole fibre of `K_{4,4}`. In general they need not be. Random linear systems produce **signed**
extras such as `e₀−e₁+e₂`, which is a not-all-equal condition on a triple with one coordinate
negated, and extras of larger support - `e₀+e₂+e₃+e₄+e₆`, and in one case a form on all seven
coordinates. A `±1`-valued form of support 5 is a balance condition, not a triple constraint at all.
So the mechanism named in §32 is one mechanism, not the mechanism.

**Anti-Pasch does not repair the bound.** In this construction an edge `(a,y)` lies in matching
`(y−p−a) mod q`, so a Pasch rectangle needs two left points with `2(a−a') ≡ 0 (mod q)` - impossible
for odd `q`. The rule predicts Pasch-freeness exactly (9 of 9 members, both directions), and the
odd-`q` members are precisely where the bound breaks worst:

| member | `k` | `r` | Pasch | `\|D\|` | dim `R` | `⌈k/2⌉` | tightness | |
|---|---|---|---|---|---|---|---|---|
| `K_{3,3}` | 9 | 9 | free | 36 | 5 | 5 | 0.575 | holds |
| `K_{3,5}` | 15 | 13 | **free** | 58 | **7** | 8 | 0.526 | **fails** |
| `K_{4,5}` | 20 | 14 | **free** | 94 | **8** | 10 | 0.500 | **fails** |
| `K_{5,5}` | 25 | 15 | **free** | 140 | **9** | 13 | 0.501 | **fails** |

**And the failure is unbounded.** For `K_{q,q}` with `q` odd, `k = q²` and the chosen graph spans a
subspace of dimension `2q − 1`, so

> `d_cb ≤ 2√k − 1` while `⌈k/2⌉ = Θ(k)`.

The ratio runs 1.00, 0.69, 0.52, 0.42, 0.34 for `q = 3, 5, 7, 9, 11` and tends to zero. So `d_cb` for
linear systems can be of order `√k`, which is exactly the `√(2k)` degradation §21 derived from the
broken lemma and §24 declared "not merely unrealised, [but] structurally obstructed". That
conclusion is wrong. §24 measured *random maximal* partial Steiner systems and found density
destroying the fibre; this construction keeps the density in the chosen **graph** while the hub
points keep the triple system sparse and 2-colourable. `K_{5,5}` has `k/r = 1.67`, far into §24's
"empty" regime, and still has `|A| = 186` and a spanning fibre.

**What is untouched.** Conjecture RC. Tightness `d_cb·β/ℓ` across the whole family is 0.62, 0.58,
0.53, 0.50, 0.50 - flat near one half, nowhere near the ceiling of 1. The objects that destroy the
counting bound sit comfortably inside the conjecture the campaign is actually trying to prove, and
they do it while being the most extreme objects yet constructed here. That is mild evidence for RC
rather than against it.

**Verification.** Both validity implementations agree on all seven rows - the library's
row-reduction test and the independent one that quotients by projection onto a complement of `R` with
its own transversal search. Linearity is the printed maximum pairwise intersection; Pasch-freeness is
an exhaustive search over 4-subsets for a six-point union; `|A|` is recomputed directly.

**Standing.** `d_cb ≥ ⌈k/2⌉` is false for linear systems, false for anti-Pasch linear systems, and
false by an unbounded factor. It holds on every object in §§1-31 and those measurements stand. The
question it leaves is which hypothesis actually delivers it, and `|D| = r + k` remains the only one
known to work - now with no combinatorial characterisation, since the obvious candidate is refuted.

## 34. What the dossier actually needs, and why none of this touches it

Three sections of refutation invite the question of how much damage has been done to the programme.
The answer, checked against the document rather than assumed, is none.

**The dossier never uses a counting bound of this kind.** Searching the 326KB text for `k/2`,
`⌈k/2⌉`, "half the", "at least k/2" returns nothing. `⌈k/2⌉` is a campaign construct, built here
while reconstructing Layer II, and not a step the document relies on.

**And it points the wrong way.** The dossier's requirement is stated plainly:

> "A bound `dcb = O(ℓ)` therefore makes the residual cost commensurate with the entropy loss. In the
> endpoint range `k = O(n/ log n)`, it is small enough to preserve the required exponential saving.
> The unconditional theorem `dcb ≤ 9 · 4^ℓ + ℓ` already extends the summable range..."

That is an **upper** bound on `d_cb` - the whole difficulty is getting from `4^ℓ` down to `O(ℓ)`, which
is exactly Conjecture RC. `⌈k/2⌉` is a **lower** bound. Refuting it cannot weaken an upper-bound
programme, and the campaign's investment in it was effort spent on a quantity facing away from the
target. Worth recording plainly, since the same mistake is easy to repeat.

**The counterexamples are mild evidence *for* RC.** The `K_{p,q}` family has an exact fibre count.
Verified for `q = 2..13`:

> `|A| = 6(2^q − 1)` for `K_{q,q}`

giving `ℓ = 3q − log₂|A| = 2q − log₂6 + o(1)`, against `d_cb ≤ 2q − 1`. So

> `d_cb / ℓ → 1` and tightness `d_cb·β/ℓ → β = 0.415…`

from above: 1.386, 1.206, 1.138, 1.103, 1.082, 1.068 for `q = 3..13`, with tightness falling
monotonically 0.575 → 0.443. The family cannot approach the RC ceiling at any `q`. These are the
most extreme objects the campaign has built - they break the counting bound by an unbounded factor -
and they settle at `d_cb ≈ ℓ`, a factor `1/β = 2.41` inside the conjecture.

There is something suggestive in the limit being `β` itself. `β` is where the absorption threshold
sits and where the minimum congestion cost sits; a family constructed for an unrelated reason, to
make `d_cb` small relative to `k`, converges to the same constant from the other side.

**One thing the dossier does not contain.** "Pasch" does not occur in it. Since a Pasch
configuration is sufficient to produce extra dual forms - and extra dual forms are what break the
`|D| = r + k` bookkeeping that Layer II's reconstruction here leaned on - a design-theoretic
obstruction is sitting under the entropy-to-rank conversion that the document never names. Whether
the dossier's own Layer II implicitly assumes something equivalent is worth checking, and is not
answered here.

**Standing.** Conjecture RC is unrefuted and now tested on a family built to be hostile. The
counting bound is dead. The dossier's programme is untouched by both facts.

## 35. A proved necessary condition: `|D| = r + k` forces anti-Pasch

§33 left "a Pasch produces extra dual forms" as an observation with no counterexample. It has an
elementary proof, and proving it converts anti-Pasch from a pattern into a necessary condition on the
only hypothesis now known to deliver the counting bound.

Label a Pasch by its pairwise intersections. Four blocks on six points, every two blocks meeting in
exactly one point, so writing `p_ij` for the common point of `B_i` and `B_j`,

`B₁ = {p₁₂, p₁₃, p₁₄}`  `B₂ = {p₁₂, p₂₃, p₂₄}`  `B₃ = {p₁₃, p₂₃, p₃₄}`  `B₄ = {p₁₄, p₂₄, p₃₄}`

> **Theorem.** If a linear triple system contains a Pasch configuration then for every 3-subset
> `{i,j,l} ⊆ {1,2,3,4}` the triple `{p_ij, p_il, p_jl}` is not-all-equal on the whole fibre and is not
> a block of the system. Consequently `|D| ≥ r + k + 4`, and `|D| = r + k` implies the system is
> **anti-Pasch**.

*Proof.* Take `{i,j,l} = {1,2,3}`; the rest follow by relabelling. Suppose
`s(p₁₂) = s(p₁₃) = s(p₂₃) = ε`. `B₁` is not-all-equal and two of its points already read `ε`, so
`s(p₁₄) = −ε`. The same argument on `B₂` gives `s(p₂₄) = −ε`, and on `B₃` gives `s(p₃₄) = −ε`. But
`B₄ = {p₁₄, p₂₄, p₃₄}` is then monochromatic, contradicting that it is a block. So no assignment in
the fibre makes those three coordinates equal, and the form `e_{p_ij} + e_{p_il} + e_{p_jl}` takes
only the values `±1`.

For the second part, `{p₁₂, p₁₃, p₂₃}` contains the pair `{p₁₂, p₁₃}`, which lies in `B₁`. In a
linear system no pair lies in two blocks, so this triple is not a block. The four triples are
distinct - they are the conjugate Pasch on the same six points - so they contribute four dual forms
beyond the `r` coordinate forms and the `k` block forms. ∎

Checked on seven systems - the Pasch alone, `K_{2,2}`, `K_{3,4}`, `K_{4,4}`, `K_{4,6}`, and the Pasch
with a disjoint and with an attached extra triple: all four conjugate triples are `±1`-valued across
the entire fibre in every case, none is a block, and the measured excess is 4, 4, 24, 48, 72, 4, 4.
A conjugate triple taking the value `±3` anywhere would have refuted the proof.

**What this settles and what it does not.** Anti-Pasch is now *necessary* for `|D| = r + k`, hence
necessary for the counting bound's derivation. It is not sufficient: `K_{2,3}` and `K_{3,3}` are
anti-Pasch with 6 and 18 extra forms, and `K_{3,5}`, `K_{4,5}`, `K_{5,5}` are anti-Pasch and break the
bound outright. So the class that supports `⌈k/2⌉` sits strictly inside the anti-Pasch systems, and
what distinguishes it is open.

The connection is worth noting for its own sake: anti-Pasch (or quadrilateral-free) triple systems
are a studied family in design theory, so the hypothesis the campaign needs is not an ad-hoc
condition invented here but a known combinatorial class - and one the dossier never mentions, the
word "Pasch" occurring nowhere in it.

## 36. Where Conjecture RC's boundary actually sits

With the counting bound gone, RC is the live target - it is what the dossier asks for. Writing
`c = kβ − ℓ` for the **correlation excess**, positive when the constraints help each other and the
fibre is larger than independence predicts, and using the proved `d_cb ≤ k` for linear systems,

> tightness `= d_cb·β/ℓ > 1`  ⟺  `c > β(k − d_cb)`

So a counterexample needs positive correlation *large enough to pay for the gap between `d_cb` and
`k`*. That is a much narrower target than "search for a violation", and it says where to look.

**The extremal class is the disjoint unions, and they attain the bound exactly.** Measured
`d_cb` (exact) and tightness:

| object | `k` | `d_cb` | `c` | tightness |
|---|---|---|---|---|
| single triple | 1 | 1 | 0 | **1.000000** |
| disjoint `m=2` | 2 | 2 | 0 | **1.000000** |
| disjoint `m=3` | 3 | 3 | 0 | **1.000000** |
| star `k=4` | 4 | 3 | 0 | 0.750 |
| star `k=3` | 3 | 2 | 0 | 0.667 |
| chain `k=4` | 4 | 2 | 0 | 0.500 |
| tri-cycle `k=4` | 4 | 2 | +0.018 | 0.505 |
| Pasch | 4 | 2 | −0.170 | 0.454 |

The reason disjoint unions sit exactly on the line is that **both sides are additive over disjoint
blocks** - `d_cb` provably so, and `ℓ` trivially, since `|A|` multiplies and `r` adds - while a single
triple has `d_cb = 1` and `ℓ = β`. So every disjoint union has tightness `mβ/(mβ) = 1` for every `m`.
RC is exactly tight, not asymptotically tight, and it is tight on the simplest object there is.

Stars approach the line without reaching it: `d_cb = k − 1` for a star of `k` triangles, against
`ℓ = kβ`, giving `(k−1)/k`. Every tree has `c = 0` exactly - tree constraints are independent - so no
tree can ever exceed 1, whatever its `d_cb`, because `d_cb ≤ k` caps it at `kβ/(kβ)`.

**And positive correlation is rare and small — at these sizes.** Across ~74 linear systems the correlation excess is
`≤ 0` almost everywhere - the constraints of a linear system typically *fight*, making `ℓ > kβ` and
pushing tightness down. The only positive value found is `+0.018`, on tri-cycle `k=4`, where
`β(k − d_cb) = 0.83`. No object was found
with `c > 0` and `d_cb = k`, which is the shape a counterexample must have.

> **Corrected by §40.** "Rare and small" is a property of this window, not of linear systems. A sweep over
> 16,028 *connected* linear systems reaches `c = +1.132` on `K_{4,4}`, sixty times the largest value seen
> here. What does not change is the verdict: the threshold is `β(k − d_cb)`, which at `K_{4,4}` is 3.735,
> so the largest-`c` object in the corpus still sits 2.60 below a violation.

**The limitation, named rather than buried.** These `d_cb` values are exact but capped at `d_cb ≤ 4`;
objects above the cap were excluded, not scored. Since tightness `> 1` needs `d_cb > 2.41·ℓ`, a cap
of 4 means the sweep only ever examined the region `ℓ < 1.66`. A counterexample at `d_cb = 5,6,7`
would need `ℓ < 2.08, 2.49, 2.90` and was invisible to it. A deeper sweep at `dmax = 6`, with a
generator biased toward the cycle-and-overlap structures that produce `c > 0` rather than uniform
draws, is running on two boxes.

**What a proof would have to use.** The additivity argument gives RC with equality on disjoint
unions for free. Since `c = 0` forces tightness `≤ 1` outright, everything hinges on systems with
`c > 0`, and the measurements say those are exactly the ones whose overlapping structure also drives
`d_cb` far below `k`. That trade-off - the same overlap that raises `c` collapses `d_cb` - is the
mechanism a proof needs to make quantitative, and it is the same tension that appeared in §28 between
the fibre existing and the bound being tight.

## 37. The correlation excess, in closed form: why RC is safe where it is safe

§36 reduced a violation of RC to `c > β(k − d_cb)`, with `c = kβ − ℓ` the correlation excess, and said
a proof would have to make quantitative the trade-off by which the overlap that raises `c` also
collapses `d_cb`. On the standard families `c` can be computed exactly, and the trade-off is sharp.

**Trees have `c = 0` exactly.** Stars and chains at `k = 2..6`, all ten cases: `ℓ = kβ` to machine
precision. Tree constraints are independent, so no tree can violate RC whatever its `d_cb`, since
`d_cb ≤ k` caps tightness at `kβ/kβ = 1`. Stars sit closest, at `(k−1)/k`.

**Tri-cycles have an exact fibre count.** For the tri-cycle of `k` triangles on `r = 2k` coordinates,

> `|A| = 3^k + (−1)^k`

verified for `k = 3..8`, and then **predicted and confirmed out of sample** at `k = 9` (19,682) and
`k = 10` (59,050). This is a transfer-matrix count with eigenvalues `3` and `−1`: each triangle adds
two coordinates and multiplies the count by 3 rather than 4 - which is the factor `3/4` that defines
`β` - while the `−1` records the closure of the cycle. Hence, exactly,

> `c = log₂(1 + (−1)^k 3^{−k})`

matching the measurement to nine decimals at every `k` including the out-of-sample ones. The sign
alternates with parity - even `k` gives `c > 0`, odd `k` gives `c < 0` - because an even cycle closes
up under a 2-colouring and an odd one cannot, and the magnitude decays like `3^{−k}`.

That settles RC on tri-cycles with room to spare. Their `d_cb` is `⌈k/2⌉`, so a violation would need
`c > β⌊k/2⌋ ≈ 0.21k`, against an actual `|c| < 3^{−k}`. The margin is exponential in the wrong
direction for a counterexample.

**Wheels are the opposite case and make the trade-off visible.** Their correlation excess is large
and positive and grows: `+0.245, +0.468, +0.535, +0.660, +0.763` for rim `n = 3..7`. If large `c`
alone could break RC, wheels would. It cannot, because a wheel's `d_cb` is `⌈n/3⌉` - the overlap that
makes the fibre big is the same overlap that makes the residual space small. At `n = 7`,
`c = 0.763` while `β(k − d_cb) = β(7−3) = 1.66`, still short.

**So the three regimes are:** `c = 0` with `d_cb` free to reach `k` (trees, tight but never over);
`c` exponentially small with `d_cb = ⌈k/2⌉` (tri-cycles); `c` large with `d_cb` collapsed to about
`k/3` or below (wheels, and the bipartite hub family where `d_cb ~ 2√k`). In no family measured does
large `c` coexist with `d_cb` near `k`, which is the only shape that can violate RC.

The parity in `c` is the same parity that runs through the rest of the campaign - even cycles
degrade the counting bound in `d ≥ k/2 − c/2 + nb`, and §28's colourability theorem says the fibre
exists exactly when a bipartite, i.e. all-even-cycle, choice exists. Three appearances of one
mechanism rather than three coincidences: an even cycle makes the object easier to satisfy and
cheaper to span, and both effects push the same way.

## 38. The extremal characterisation, and why `1/β` cannot be improved

> **Most of this section is a re-derivation, and the credit belongs elsewhere.** WHAT_STANDS already
> records `d_cb(k-arm star) = k − 1` as **proved** for every `k ≥ 2` (P1, `star_family_proved.md`
> §§2, 6 - construction for `≤`, a leftover-structure and derangement argument for `≥`);
> `d_cb(m disjoint triples) = m` with tightness exactly 1 (P2); and `1/β` is exactly optimal, "it
> cannot be lowered and it is attained with equality along an infinite family", with
> `sup_k (k−1)/(kβ) = 1/β` approached but not attained (P3). I reached those independently from the
> exact `d_cb` values and only then found them in the ledger. Two useful things survive that:
> the independent confirmation itself, and the one genuinely new piece below - **Conjecture E**, which
> is the *only if* direction, asserting that nothing else reaches 1. The campaign had recorded
> equality "by exactly two" objects computed, not a characterisation.


Combining §§36-37 with the one surviving result of `gluing_is_a_cliff.md` - its §7 additivity lemma,
`ℓ` and `d_cb` add over coordinate-disjoint blocks, so **tightness is the `ℓ`-weighted average of the
component tightnesses** - gives a clean picture of where RC is tight.

Since an average cannot exceed its largest term, RC for all linear systems is equivalent to RC for
**connected** ones. That reduction is already in the campaign. What the exact values add is the
extremal case at both ends:

- The **single triple** is connected and sits at tightness exactly 1: `k=1`, `|A| = 6`, `ℓ = 3 − log₂6
  = β`, `d_cb = 1`. So the connected maximum is attained, and attained by the smallest object there
  is.
- Every **disjoint union of triples** is then an `ℓ`-weighted average of 1s, hence exactly 1 - which
  is why `m = 1, 2, 3` all measure 1.000000.
- Every connected object with **more than one** triangle measured here comes in strictly below:
  stars `(k−1)/k`, chains 0.500-0.667, tri-cycles 0.505-0.598, Pasch 0.454.

> **Conjecture E.** Tightness equals 1 exactly when every connected component is a single triangle,
> and is strictly less than 1 otherwise.

**And `1/β` cannot be improved.** The star family is connected with `d_cb = k − 1` against `ℓ = kβ`,
so its tightness is `(k−1)/k → 1`. So even restricted to connected multi-triangle objects the
supremum is 1, approached but not attained. Any conjecture of the form `d_cb ≤ C·ℓ` with `C < 1/β`
is false for large stars. RC is the best statement of its kind, not merely a convenient one.

**This also diagnoses a retracted number.** `gluing_is_a_cliff.md` reported a connected supremum of
0.6960 over 7,365 connected fibres, later retracted as a bounded-enumeration artefact. The window
was `r ≤ 7`, and the star with `k = 4` needs `r = 9` - it is outside the window and already reaches
0.750, with the family climbing to 1. The retraction was right and the reason is precisely that a
parametric family left the enumeration window, which is the failure mode the campaign has now hit
more than once: a maximum over what was enumerated read as a property of the objects.

**Where that leaves the target.** RC is tight, its constant is optimal, its extremal objects are the
disjoint unions of single triangles, and the approach to the constant is through stars. A proof would
need to show that gluing any two triangles together strictly loses - which is what §37's closed forms
say quantitatively on the families where they are available: gluing raises `c` only by producing
cycles, and cycles collapse `d_cb` faster than `c` grows.

## 39. `d_cb ≤ k` proved for `k ≤ 8`, and reduced to a Hall condition in general

WHAT_STANDS carries `d_cb ≤ k for every linear triangle system` as **verified on 35 objects, not
proved**, and names the gap precisely: the construction takes one pair-sum per triangle and needs the
`k` pair-sums independent, which "needs a choice of pairs whose incidence graph has no even cycle".
The RC tree leg rests on this, so the gap is load-bearing. It can be closed for small `k` and reduced
to a clean condition in general.

**Step 1 - it is a transversal problem.** Let `A_t` be the three pair-sums of triangle `t`. The
construction needs an independent transversal: one element from each `A_t`, all independent. The
elements are distinct across triangles because linearity forbids two triangles sharing a pair. By
**Rado's theorem** such a transversal exists iff

> for every subfamily `S` of triangles, `rank(⋃_{t∈S} A_t) ≥ |S|`.

**Step 2 - the rank has a closed form.** The pair-sums of a graph's edges have rank `V′ − b`, `b` the
number of bipartite components. The union of `s` triangles contains all three edges of each, so every
component of that union carries a 3-cycle, which is odd. Hence `b = 0` and

> `rank(⋃_{t∈S} A_t) = V′(S)`, the number of coordinates the `s` triangles touch.

Checked directly on 220 random subfamilies: zero mismatches between the computed rank and the count
of touched coordinates.

**Step 3 - so Rado's condition is purely combinatorial.**

> **(H)** every `s` triangles of the system touch at least `s` coordinates.

**Step 4 - linearity forces (H) for small `s`.** The `3s` pairs covered by `s` triangles are distinct,
so `3s ≤ C(V′,2)`. If `V′ ≤ s−1` this gives `6s ≤ (s−1)(s−2)`, i.e. `s² − 9s + 2 ≥ 0`, so `s ≥ 9`.
Tabulated at each `s`, the first arithmetically possible violation is exactly `s = 9` (`3s = 27`
against `C(8,2) = 28`); every `s ≤ 8` is impossible outright.

> **Theorem.** For a linear triangle system, an independent one-pair-per-triangle choice exists **iff**
> (H) holds. Since (H) is automatic for subfamilies of size at most 8, **`d_cb ≤ k` is proved for every
> linear triangle system with `k ≤ 8`.**

**(H) is exactly right, and it does fail.** Tested against direct search for an even-cycle-free choice
on ten systems: agreement 10 out of 10, including both negatives - `K_{3,4}` (12 triangles, 11
coordinates) and `K_{4,4}` (16 on 12) violate (H) and genuinely admit no such choice. So the criterion
is not vacuous and not merely necessary.

**What this does not settle.** When (H) fails the *construction* fails, but the *bound* may still hold
by other routes: `d_cb ≤ r` is free, which covers `K_{3,4}` and `K_{4,4}` since `k > r` there. A system
can be built where (H) fails while `k ≤ r` - `K_{4,4}` together with five disjoint triangles has
`k = 21`, `r = 27` - and there the bound holds by the additivity lemma plus the measured
`d_cb(K_{4,4}) = 7`, giving `7 + 5 = 12 ≤ 21`, not by this construction. So `d_cb ≤ k` in full
generality still needs an argument that covers (H)-violating systems.

**A note on how this was found.** The direct search first reported that a naive greedy fails on
`K_{3,3}` while a valid choice exists. Tracing it showed the greedy jams on the *last* triangle in the
generation order, and that 2,272 of 4,000 random orders succeed - so greedy is order-dependent rather
than wrong, and the right frame is matroid transversal, not sequential construction. That is what
pointed at Rado, which the campaign had already proved equivalent to blocking in a different context.

## 40. How large the correlation excess really gets, and why it still does not matter

§36 reported the correlation excess `c = kβ − ℓ` as "rare and small" on linear systems, with a maximum
of `+0.018`. That was a statement about a window of ~74 objects at small `r`, not about linear systems.

**Swept properly it is neither rare nor small.** Over **16,028 connected linear systems** the maximum is

> `c = +1.132` on `K_{4,4}`

sixty times the earlier figure and well past `β = 0.415`. The two runs are **not** independent
confirmations of that number: they share a hardcoded family list, and the maximum came from *that*,
not from either random search. What the sweep actually establishes is that ~16,000 random connected
linear systems failed to beat a known object - weaker than "two boxes agreed" makes it sound. The whole family runs positive and large:
`+0.128` (`K_{3,3}`), `+0.338` (`K_{3,4}`), `+0.701` (`K_{3,5}`), `+1.132` (`K_{4,4}`). Connectivity
and linearity were both enforced, so this is not a disjoint-union artefact - `c` adds over blocks while
tightness does not, so measuring `sup c` over arbitrary systems would have chased exactly that.

**And it still does not approach a violation, for a reason worth stating carefully.** A threshold of
`β` is only the right one when `k − d_cb = 1`. The sharp condition is `c > β(k − d_cb)`, equivalently

> slack `= β·d_cb − ℓ > 0`

which is just RC restated. At `K_{4,4}`, `k − d_cb = 16 − 7 = 9`, so the threshold is `3.735` against
`c = 1.132`: slack `−2.60`. Across the family the slack sits between `−1.5` and `−2.6`. The objects
with the largest correlation excess ever found here are among the *safest*, because the overlap that
inflates `c` is the overlap that collapses `d_cb` - the §37 trade-off, now visible at the top of the
`c` range rather than only at the bottom.

The extremal objects are the ones with slack exactly `0`: a single triangle (`c = 0`, `k = d_cb = 1`)
and its disjoint unions. Stars sit at `−β`, since `k − d_cb = 1` and `c = 0`.

**A note on my own reporting.** The sweep printed "c exceeds β on a connected linear system - this is a
lead on refuting RC". That verdict is wrong, and it was wrong in the script before it was run: `c > β`
is decisive only at `k − d_cb = 1`, and the sweep never checked `d_cb`. The measurement is sound and
the conclusion attached to it was not - which is the same failure as reading a maximum over a bounded
enumeration as a property of the objects, one level up.

**One structural question that fell out, and my first answer to it was wrong.** For `c` to be a
well-defined quantity the presentation must be irredundant: a redundant triangle raises `k` by 1
and `c` by `β` while leaving the fibre - hence `d_cb`, `ℓ` and tightness - untouched. Over 30
systems no triangle was implied by the others and no implied triangle was linearly addable, and I
wrote that linear systems are irredundant automatically. **That is false**, and a wider search
found the counterexample:

> `T = {(1,2,10), (1,3,5), (1,6,9), (1,7,8), (3,4,9), (3,6,10), (5,6,8), (5,9,10)}` on `r = 11`
> is linear, its fibre has `|A| = 80` and spans all ten touched coordinates, and it forces the
> triple `{2,4,8}` to be not-all-equal - while covering **none** of the pairs `{2,4}`, `{2,8}`,
> `{4,8}`. So `T ∪ {(2,4,8)}` is linear, has the same fibre, and carries a redundant triangle.

Verified in seven checks: linearity, all three pairs uncovered, all three coordinates touched by
`T`, the fibre spanning, the forcing across the whole fibre, and that adding the triangle keeps
linearity and leaves `|A|` at 80. The rate is about 1 in 1,000 spanning linear systems, which is
why 30 objects missed it. Note the earlier hits were degenerate and had to be discarded: they all
involved a coordinate touched by no triangle at all, so the "forced triple" was really a forced
antipodal *pair* plus a free coordinate - and a forced antipodal pair means the fibre does not
span, so `d_cb` is undefined and the object is inadmissible anyway.

**What this does and does not break.** It does not touch the §36 identity: adding a redundant
triangle moves `k → k+1` and `c → c+β` together, so `c > β(k − d_cb)` reads the same before and
after, and the tightness verdict is presentation-invariant as it must be. What it breaks is
treating `sup c` as a quantity in its own right - that is only meaningful once the presentation
is pinned irredundant, since redundant triangles inflate `c` for free.

## 41. Where the counterexamples sit relative to the dossier's own residual class

The dossier states its remaining gap explicitly, in a section called "Sharply formalized remaining
gap": after its Theorem 3, the unresolved deterministic statement is confined to blocks that are a
singleton-layer cyclic SCC after every admissible Gale basis exchange, with relation corank at least
five in the homogeneous boundary-closed case, failing connector absorption in the nonroot case, and
with **no sparse-cyclomatic fundamental graph, no relation-side feedback set of size `o(log n)`, no
large disjoint-support matching, no `o(log n)` ordinary star core, no sufficiently low-rank shared
form, and no multiplicative subgroup/coset fibre**.

That list is an exclusion list, so it is worth asking where the `K_{p,q}` counterexamples of §32-33
fall against it. One entry is directly computable.

**The family has a disjoint-support matching of size about `√k`.** A set of triangles with pairwise
disjoint supports needs distinct `a`, distinct `i`, and distinct `a+i (mod q)` - which is exactly a
partial transversal of the cyclic Latin square. Measured:

| `q` | parity | `k` | max disjoint-support matching |
|---|---|---|---|
| 3 | odd | 9 | **3** |
| 4 | even | 16 | 3 |
| 5 | odd | 25 | **5** |
| 6 | even | 36 | 5 |
| 7 | odd | 49 | **7** |

so the matching is `q` for odd `q` and `q − 1` for even `q`, i.e. of order `√k` and growing. Whether
that clears the dossier's threshold for "large" is not something the text settles, but it is not
bounded, and the campaign already records that every object it has built is a known non-member of the
residual class. So the refutation of the counting bound lands outside the class the dossier's proof
actually has to handle - a second reason, independent of §34's observation that `⌈k/2⌉` is a lower
bound in an upper-bound programme, that none of this damages the programme.

**And the two parities are one algebraic fact.** §33 found that a Pasch rectangle in this construction
needs two left points with `2(a − a′) ≡ 0 (mod q)`, which is possible exactly when `2` is a zero
divisor - so `q` even contains a Pasch and `q` odd is Pasch-free. The matching size is governed by the
same thing from the other side: a full transversal of the cyclic Latin square on `Z_q` is a complete
mapping, and `Z_q` has one iff `q` is odd. Hence

> for `K_{q,q}`: `q` odd gives a Pasch-free system **and** a full `q`-triangle disjoint matching;
> `q` even gives a Pasch **and** a matching one short of full.

Two combinatorial properties that arose for unrelated reasons - one from the dual bookkeeping, one
from the dossier's exclusion list - are both controlled by whether `2` is invertible in `Z_q`. That
also explains why the odd members are the ones that break the counting bound worst: they are the ones
whose structure is cleanest, not the ones that are most degenerate.

## 42. Conjecture E's content is the transversal, not the counting

Conjecture E - tightness equals 1 exactly when every component is a single triangle - reduces by the
additivity lemma to a statement about connected systems:

> **(E′)** a connected linear system with `k ≥ 2` triangles has `d_cb ≤ k − 1`.

**The counting half of that is free.** Take any `k − 1` pair-sums, one from each of `k − 1` distinct
triangles. By the verified formula of §23, `excess = E + (V′ − comp)` with `E ≥ k − 1` (the generators
lie in `R`) and `V′ − comp ≥ 1` (every edge has two endpoints, so `comp < V′`), giving
`excess ≥ k`. The span has dimension at most `k − 1` because it has `k − 1` generators. So when
`|D| = r + k` the class-count requirement `excess ≥ |D| − r = k` is met with nothing to prove.

Measured across 23 systems and about 2,700 such choices: on every system with `|D| = r + k`, **all**
choices clear the bar and **all** are valid - star `k=4`, chain `k=4,5`, tri-cycle `k=4,5` and the
random connected systems each report 108/108/108 or 300/300/300. Where the dual is larger the bar is
`|D| − r > k` and some choices fail it (Pasch: 104 of 108; three random systems at `need = 15`: 268,
265, 259 of 300). In every row the count clearing the bar **equals** the count that is valid.

**But that equality is an artefact of testing only connected systems, and the control shows it.**
Disjoint unions must break it, since their `d_cb` is `k`, not `k − 1`. Running the same construction
on them:

| system | `k` | `need` | dim | excess | excess ≥ need | `valid_R` |
|---|---|---|---|---|---|---|
| disjoint `m=2` | 2 | 2 | 1 | 2 | yes | **no** |
| disjoint `m=3` | 3 | 3 | 2 | 4 | yes | **no** |

The counting bar is cleared and validity fails anyway. So the **independent-transversal condition is
the entire content of (E′)** - the excess side never distinguishes anything. What separates a
connected system (`d_cb ≤ k − 1`) from a disjoint union (`d_cb = k`, tightness exactly 1) is Rado, not
counting.

That also fits P2's proof of the disjoint case, which is a selector argument rather than a counting
one: a basis must take three forms from each block, leaving one leftover per block, and no dependency
exists. Nothing about class counts enters.

**So the remaining statement is sharp.** (E′) is now exactly:

> for a connected linear system, some choice of `k − 1` pair-sums from `k − 1` distinct triangles
> admits an independent transversal of the resulting dual classes.

which is a Rado condition of the same shape as §39's, on a different family - and §39 showed that shape
is tractable, since there the rank of a union of triangles collapsed to a coordinate count. Whether the
same collapse is available here is the thing to try next.

## 43. (E′) has no countable criterion: the transversal is irreducible

§42 reduced Conjecture E to (E′) - a connected linear system with `k ≥ 2` has `d_cb ≤ k − 1` - and
observed that the counting half is free, so everything sits in the independent-transversal condition.
§39 had turned a transversal condition of a different shape into a plain count, so the natural hope was
that the same collapse works here. It does not, and the test that settles it is short.

For each system, every choice of `k − 1` pair-sums from `k − 1` distinct triangles was scored on two
things: the number of dual classes modulo `R`, and whether `valid_R` holds.

| object | `r` | choices | valid | class counts on valid | class counts on invalid |
|---|---|---|---|---|---|
| star `k=4` | 9 | 108 | 108 | 7 | — |
| chain `k=4` | 9 | 108 | 108 | 7 | — |
| tri-cycle `k=4` | 8 | 108 | 108 | 5, 6 | — |
| Pasch | 6 | 108 | 104 | 3, 4, 6 | 8 |
| **star3 ⊔ triple** | 10 | 108 | **81** | **8** | **8** |
| disjoint `m=2` | 6 | 6 | 0 | — | 6 |
| disjoint `m=3` | 9 | 27 | 0 | — | 8 |

**The fifth row settles it.** In `star3 ⊔ triple` the identical class count of `8` occurs among both
the 81 valid choices and the 27 invalid ones. So the class count cannot decide validity - two choices
with the same count, on the same object, come out opposite ways. The disjoint unions say the same
thing more starkly: every choice there has a class count strictly under `r` (6 of 6 at `m=2`, 27 of 27
at `m=3`) and every one fails.

The Pasch row is the only one where the count does the work - its 4 invalid choices all have count `8`
against `r = 6`, so they fail on the class bar rather than the transversal, which is the regime §32
created by enlarging the dual past `r + k`.

**So the remaining content of Conjecture E is irreducibly matroid-theoretic.** No count of classes,
components, or coordinates decides it; what decides it is whether the classes admit a system of
distinct representatives that is linearly independent. That is a sharper statement of the open problem
than "prove `d_cb ≤ k−1`", and it says where not to look - a fourth counting identity will not close
this, which is worth knowing after §§19-21 spent three of them.

It also sharpens the extremal case, though my first reading of it was wrong. I wrote that a disjoint
union fails because each block keeps its own leftover form and the leftovers cannot be exchanged
across blocks, so **connectivity** is what allows the exchange - which would make connectivity the real
hypothesis in (E′). The discriminating experiment says otherwise. Measuring the Rado slack, the minimum
of `rank(⋃S) − |S|` over subfamilies of dual classes, on the best `(k−1)` choice:

| object | connected | classes | valid | Rado slack | bottleneck size |
|---|---|---|---|---|---|
| disjoint `m=2` | no | 6 | no | **−1** | 4 |
| disjoint `m=3` | no | 8 | no | **−1** | 4 |
| **star3 ⊔ loose triple** | **no** | 8 | **yes** | 0 | 1 |
| star3 + triple at one point | yes | 7 | yes | 0 | 1 |
| two triples sharing a point | yes | 5 | yes | 0 | 1 |
| star `k=3`, chain `k=3`, tri-cycle `k=3` | yes | 5-6 | yes | 0 | 1 |

The third row is the one that matters: `star3 ⊔ loose triple` is **disconnected and valid**. So connectivity
is not the criterion, and the additivity reduction was already telling me that - a disjoint union is at
tightness 1 only when *every* component is a single triangle, since the `ℓ`-weighted average of
component tightnesses is 1 only if every term is. One multi-triangle component drags the average below 1
and the union becomes valid at `k−1`.

What the slack column does show is a clean dichotomy: **−1 with a size-4 bottleneck exactly on the unions
of single triangles, 0 with a size-1 bottleneck on everything else.** So the extremal objects are not
"disconnected" ones but *all-singleton* ones, and the quantity that separates them is the Rado slack,
which is what a proof of (E′) would have to keep non-negative.

## 44. The bottleneck identified, and Conjecture E proved for pair-sum residuals

§43 left the transversal condition irreducible and pointed at a size-4 bottleneck on unions of single
triangles. Four classes spanning three dimensions is small enough to look at directly, and it is the
same object in every case:

> classes `{e₀}`, `{e₀+e₁+e₂}`, `{−e₂}`, `{e₁}` - the four dual forms of a block that `R` never
> touches - whose union spans only that block's three coordinates.

A triangle block receiving no chosen pair-sum keeps all four of its dual forms (its three coordinate
forms and its triangle form) in separate classes inside a 3-dimensional space. Four classes, rank
three, so no independent system of distinct representatives exists. That is exactly P2's selector
argument, seen from the Rado side.

**Which gives a criterion, and it is exact.**

> A choice of `k − 1` pair-sums, one from each of `k − 1` distinct triangles, is valid **iff** every
> connected component of the system receives at least one chosen pair.

Tested on 249 admissible choices across seven systems - disjoint `m=2,3`, star `k=3`, star3 ⊔ loose
triple, chain `k=3`, tri-cycle `k=3`, and a two-block uneven system - `valid_R` and "touches every
component" agree on **every single choice**, in both directions: 0 of 6 and 0 of 27 valid on the
disjoint unions, 81 of 108 and 18 of 27 on the mixed ones, and all of them on the connected ones.

**And that proves (E′).** A choice omits exactly one triangle. It fails to touch a component only if
that component's every triangle was omitted - so the component must be the single omitted triangle,
i.e. a singleton block. Hence:

> **Theorem.** For a linear triangle system with `k ≥ 2`, a valid `(k−1)`-dimensional pair-sum residual
> space exists **unless every connected component is a single triangle**. So `d_cb ≤ k − 1` for every
> such system, and Conjecture E's "only if" direction holds for pair-sum residuals.

The connectivity hypothesis in (E′) was never the right one - §43 already showed a disconnected system
can be valid, and this says why: `star3 ⊔ loose triple` has a choice reaching both blocks, because
dropping one triangle of the star still leaves two to cover it while the loose triple keeps its own.
What matters is not that the system is connected but that no component is small enough to be erased by
the single omission.

**Scope, stated rather than glossed.** This proves the statement for residual spaces spanned by
pair-sums, which is where every `d_cb` witness in this campaign has lived, but `d_cb` minimises over
*all* subspaces. A smaller-dimensional non-pair-sum `R` would lower `d_cb` further, which only helps
the `≤` direction here - so the theorem stands as an upper bound. What it does not do is show
tightness `= 1` fails on those systems, since that needs `d_cb = k − 1` exactly rather than at most,
and the lower bound is a separate question. Conjecture E is therefore proved in one direction and open
in the other.

**Sweep completed.** The independent search finished at **2,607 connected linear systems with zero
candidates** - no system lacked a valid `(k−1)`-dimensional pair-sum residual space. Since §44 proves
that, the sweep is now a confirmation of a theorem rather than evidence for a conjecture, which is the
right order: it was launched before the proof existed and would have been the counterexample hunt if
the proof had failed. Controls passed in both directions throughout (disjoint unions must fail, stars
must pass, including star `k=5`).
