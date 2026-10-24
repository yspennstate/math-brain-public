# Constraint interaction is a cliff, not a slope: tightness 1 exactly when the constraints are disjoint

Author: main session c53c1d50, 2026-08-19 ~14:4x. The disjoint-triples family attains `1/β` exactly. The question this answers is whether it sits at the top of a gradient — so that near-disjoint objects are near-extremal — or on a cliff.

## 1. The measurement

Define **gluing** `= 3m − r` for a fibre with `m` NAE triples on `r` coordinates: how many coordinate identifications away from the disjoint product it is. Negative means spare unconstrained coordinates.

Exact `d_cb` over every NAE-triple fibre at `r ≤ 5`, `m ≤ 4` — **401 fibres**:

| gluing | fibres | mean tightness | **max tightness** |
|---|---|---|---|
| −2 | 10 | 1.0000 | **1.0000** |
| −1 | 4 | 1.0000 | **1.0000** |
| 0 | 1 | 1.0000 | **1.0000** |
| 1 | 45 | 0.5747 | 0.6121 |
| 2 | 6 | 0.6121 | 0.6121 |
| 4 | 120 | 0.4054 | 0.5000 |
| 5 | 4 | 0.4150 | 0.4150 |
| 7 | 195 | 0.5216 | 0.6960 |

> **Tightness is exactly 1 precisely when the constraints are pairwise coordinate-disjoint, and *any* shared coordinate drops it to at most 0.70.**

Spare free coordinates do not matter — gluing `−2` and `−1` are still exactly 1, because unconstrained coordinates add nothing to `ℓ` and leave the certificate alone. What matters is only whether two constraints **share** a coordinate.

## 2. It is a cliff, and not monotone past the edge

Beyond gluing 0 the maximum does not decline steadily: 0.612, 0.612, 0.500, 0.415, **0.696**. Gluing 7 exceeds gluing 4 and 5. So "more gluing, less tight" is **false** as a trend — the structure is a single sharp drop at the first shared coordinate, and then no useful ordering. That distinction matters: it means one cannot argue about difficulty by counting interactions, only by whether interaction exists at all.

## 3. What it says about the campaign's difficulty picture

The residual class is a **single strongly connected block** — every constraint interacting, gluing maximal. On this evidence such objects sit far from extremal, with tightness bounded well below 1, so **the rooted target should hold on them with substantial room rather than tightly.**

That is the reverse of the intuition the campaign's framing carries, where the dense connector-incoherent cores are the hard case. On everything computable, **connectivity buys slack in the constant.** The difficulty in those objects, if it is real, is therefore *not* that they strain the constant — it must be something the constant does not see.

**Stated with the limits it has.** This is `r ≤ 5` and `m ≤ 4`, on NAE-triple fibres; the class is defined asymptotically and none of these objects is in it. Denser fibres at `r = 5` (`m ≥ 5`) were *not* covered: their fibres are small but still spanning, so their duals blow up toward `2^r` forms and the exhaustive basis enumeration becomes `C(32,5) ≈ 2·10⁵` per fibre. That is a real gap in coverage at exactly the dense end — which is the end the class lives at — and it should not be glossed: the cliff is established for sparse-to-moderate fibres and *assumed* to continue into the dense ones.

## 4. The dense-end gap is closed (added ~15:0x)

§3 named the coverage gap and put it exactly where it hurts: dense fibres were skipped because exact `d_cb` needs `C(|D|, r)` bases and `|D|` blows up on small spanning fibres. That gap is now closed, and it closed cheaply once the *direction* of the bound was used properly.

**The observation that made it affordable.** The claim at the dense end is that tightness is **low**. Greedy `d_cb` is an **upper** bound, so greedy tightness is an upper bound too — and an upper bound below the line settles the case. Exact computation is only needed where the *upper* bound clears 0.70. The expensive search was never required for the whole population, only for the handful that survive the cheap filter. (This is the same bound-direction reasoning that went wrong repeatedly earlier in the session, here running in my favour.)

**The measurement.** 985 dense fibres — `r=5, m=5..8` and `r=6, m=5..7`:

- `r = 5` dense: **zero** fibres with upper bound above 0.70, at any `m`.
- `r = 6` dense: **52** fibres with upper bound above 0.70, the worst at 0.9581.
- **All 52 computed exactly, none truncated.**

> **Maximum EXACT tightness anywhere at the dense end: 0.5866.** Attained by `{(0,3,5),(1,3,5),(1,4,5),(2,3,5),(2,4,5)}` at `r = 6`.

**The greedy was loose on every one of them, often badly.** Max upper bound 0.9581 against max exact 0.5866; the single worst case went from an upper bound of 0.9581 to an exact tightness of **0.3194** — the greedy reporting `d_cb ≤ 3` where the truth is **1**. That is a factor of three, on precisely the objects where a loose bound would have manufactured a false counterexample to the cliff.

**So the cliff is established across sparse, moderate and dense fibres at `r ≤ 6`:** tightness reaches 1 only for coordinate-disjoint constraints, and never exceeds 0.5866 once any coordinate is shared — with the 0.70 line comfortably clear of the true maximum rather than resting on it.

**What remains out of reach.** `r ≥ 7`, and the asymptotic regime the residual class actually lives in. The dense end is closed *at these sizes*, which is what §3 promised and no more; nothing here extends the cliff to large `r` beyond the pattern's persistence across every size tested.

## 5. r = 7 refines this: the qualitative cliff holds, the 0.70 line does not (added ~16:1x)

A faster exact algorithm (searching residual **subspaces by dimension** rather than enumerating bases — validated against all 14 known exact values with zero mismatches, and ~200x cheaper in core-seconds) put `r = 7` in reach. It was run specifically to break the claims above, and it broke one of them.

**Exhaustive over all 6,545 spanning three-triple fibres at `r = 7`:**

| shared coordinate-slots | fibres | mean tightness | max tightness |
|---|---|---|---|
| 2 (least gluing possible at `r=7, m=3`) | 945 | 0.6873 | **0.7594** |
| 3 | 3,360 | 0.4444 | 0.6387 |
| 4 | 2,100 | 0.4034 | 0.5000 |
| 5 | 140 | 0.4150 | 0.4150 |

**What survives.** **Zero** glued fibres reach tightness 1.0000, out of 6,545. Combined with the positive control (two disjoint triples at `r=7` giving exactly 1.0000), the qualitative statement stands: **tightness 1 is exclusive to pairwise coordinate-disjoint constraints.**

**What does not.** **210 glued fibres exceed 0.70**, the highest at 0.7594. So the "≤ 0.70 once glued" figure was an artefact of `r ≤ 6` — at those sizes gluing 1 was the least-glued case available, whereas `r = 7` admits three triples sharing only 2 slots, which are nearly disjoint and score accordingly. **The magnitude of the drop is `r`-dependent; only its existence is not.**

**And a correction to §2's "not monotone".** Within *fixed* `r` and `m`, tightness declines monotonically in shared slots: 0.759, 0.639, 0.500, 0.415. §2 concluded there was no ordering past the edge — that came from comparing fibres across *different* `r`, where the comparison is not like-for-like. Holding `r` and `m` fixed, the ordering is clean.

**Restated at the strength the evidence supports:**

> Tightness equals 1 exactly when the constraints are pairwise coordinate-disjoint. Any sharing strictly reduces it, monotonically in the amount shared at fixed `r` and `m`, by an amount that depends on `r` — at `r ≤ 6` the glued maximum is 0.5866, at `r = 7` it is 0.7594.

The trend across `r` is the open part: whether the glued maximum keeps climbing toward 1 as `r` grows, or settles. If it climbs, the qualitative cliff weakens into a gradient at large `r` and the disjoint family's extremality becomes a small-`r` phenomenon; if it settles below 1, the separation is real asymptotically. Two values (0.5866, 0.7594) do not distinguish those, and `r = 8` at `m = 3` is the cheap next measurement.

## 6. Fixed-sharing measurement: the glued maximum is flat in `r`, and §5's monotonicity is wrong

§5 ended on the open question — does the glued maximum climb toward 1 as `r` grows, dissolving the cliff into a gradient? The rising figures (0.5866 at `r ≤ 6`, 0.7594 at `r = 7`) were suspicious for a specific reason: with `m = 3` triples using 9 coordinate-slots, the *minimum possible* sharing is `max(0, 9−r)` — 2 at `r=7`, 1 at `r=8`, 0 at `r=9`. So a rising maximum might be nothing but "how close to disjoint the geometry allows".

The honest test holds sharing **fixed** and varies `r`:

| `r` | shared slots | fibres | mean | max |
|---|---|---|---|---|
| 7 | 2 | 900 | 0.6874 | **0.7594** |
| 8 | 2 | 900 | 0.6869 | **0.7594** |
| 8 | 1 | 840 | 0.6667 | 0.6667 |
| 7 | 3 | 900 | 0.4482 | 0.6387 |

**The glued maximum is flat.** At `shared = 2` it is 0.7594 at `r = 7` and 0.7594 again at `r = 8` — identical, not climbing. So the separation between the disjoint value (exactly 1) and everything glued does **not** dissolve as `r` grows, at least across this step. That is the answer §5 asked for, and it supports the separation being real rather than a small-`r` artefact.

**And §5's monotonicity claim is wrong.** I wrote that within fixed `r` and `m`, tightness declines monotonically in shared slots. At `r = 8` it does not: `shared = 1` gives **0.6667**, `shared = 2` gives **0.7594** — it *rises*, then falls (0.6387, 0.5000, 0.4150 at higher sharing in the `r=7` data). At `r = 7` I saw only the declining side because minimum sharing there is already 2.

The mechanism is visible in the extremal examples, which both have `d_cb = 2`:

- `shared = 1`: `{(0,1,2),(0,3,4),(5,6,7)}` — `ℓ = 1.2451`, tightness `2β/ℓ = 0.6667`
- `shared = 2`: `{(0,1,2),(0,1,3),(4,5,6)}` — `ℓ = 1.0931`, tightness `2β/ℓ = 0.7594`

Sharing shrinks `ℓ` faster than it shrinks `d_cb`, so tightness *rises* with sharing until `d_cb` finally drops, after which it falls. There is a peak, not a slope.

**Restated once more, at the strength the evidence now supports:**

> Tightness is exactly 1 precisely when the constraints are pairwise coordinate-disjoint. Any sharing drops it discontinuously — the best glued value seen anywhere is 0.7594 — and that glued ceiling is **stable across `r = 7` and `r = 8`** rather than climbing. Below the ceiling, tightness varies non-monotonically with the amount shared, peaking at two shared slots.

So "cliff" survives as the description of the gap at zero sharing, which is the part that matters for extremality; the orderly-decline picture I attached to it twice does not.

## 7. The cliff dissolves under dilution — I was measuring products, not objects (added ~16:4x)

§6 concluded the glued ceiling was flat at 0.7594 across `r = 7, 8`. That is wrong, and the reason invalidates the framing of this whole note rather than just a number.

**The extremal glued object is a product.** The `r=7` maximum came from `{(0,1,2),(0,1,3),(4,5,6)}` — a book with `p=2` *together with a disjoint triangle*. On a product of coordinate-disjoint blocks both `ℓ` and `d_cb` add, so

  `tightness(product) = (Σ dᵢ)·β / (Σ ℓᵢ)`,

which is the **`ℓ`-weighted average of the component tightnesses**. The book alone gives 0.6121, the triangle gives 1.0, and their weighted average is 0.7594 — exactly the measured maximum.

**So a glued core can be pushed arbitrarily close to 1 by adding disjoint triangles**, and it stays glued throughout. Measured, against the additivity prediction:

| core | +0 triangles | +1 | +2 |
|---|---|---|---|
| book `p=2` | 0.6121 | **0.7594** | 0.8256 |
| wheel `k=3` | 0.4150 | **0.5866** | 0.6804 |

Every value matches the prediction to four decimals. **And the two bolded numbers are the "ceilings" this note previously reported**: 0.7594 was §5's `r=7` glued maximum, and 0.5866 was §4's dense-end maximum. Both are one triangle's worth of dilution, not intrinsic quantities.

**What was wrong, precisely.** The sweeps maximised tightness over *fibres*, and a fibre may be a product of several connected blocks. The maximum then tracks how many disjoint triangles fit alongside a small glued core, which is a fact about `r` and `m`, not about gluing. §6's "flat across `r=7,8`" came from holding `m = 3` fixed, which permits at most one triangle beside a two-triple book — the flatness was the constraint budget, not the mathematics.

**The invariant that survives, and it is cleaner.** Tightness is an `ℓ`-weighted average over connected components, so:

> **The only meaningful quantity is the tightness of a CONNECTED object.** Every product is a weighted average of its blocks and can exceed none of them.

The sup over all fibres is therefore 1, attained by disjoint unions of triangles — which is exactly `the_constant_is_attained.md`'s family, and consistent with it. The substantive question is what this note should have been asking from the start:

> **What is the supremum of tightness over CONNECTED objects with at least two constraints?**

Values in hand: book `p=2` **0.6121**, book `p=3` 0.5000, star `k=2` 0.5000, the `r=5` candidate 0.5866, wheel `k=3` 0.4150. If that supremum is bounded away from 1, then the constant is attained only by disjoint triangle unions and every genuinely connected object sits strictly below — which is the statement "connectivity buys slack" *should* have been, and the one worth testing next.

**Standing correction.** §§2–6's numeric ceilings (0.70, 0.5866, 0.7594) describe dilution levels of the families that happened to be enumerated, not bounds on gluing. The qualitative claim — tightness 1 exactly for pairwise-disjoint constraints — survives, because a product hits 1 only when every component does, and the only components at 1 are triangles.

## 8. The corrected finding, measured on the right objects (added ~17:0x)

§7 established that tightness is an `ℓ`-weighted average over coordinate-disjoint blocks, so the meaningful quantity is the tightness of a **connected** object. Measured over **7,365 connected multi-constraint fibres** at `r ≤ 7` with exact `d_cb`:

> **Supremum of tightness over connected objects with `m ≥ 2`: 0.6960.**

Attained by a family of `r = 5`, `m = 4` objects with `d_cb = 2`, `ℓ = 1.19265`, `|A| = 14` — for instance `{(0,2,4),(0,3,4),(1,2,4),(1,3,4)}`: all four pairs from `{0,1}×{2,3}` sharing an apex coordinate. The wheel `k = 4` has identical invariants and ties for the maximum. It is *not* the book `p=2` (0.6121) that the smallest-connected-pair guess suggested.

**So the statement this note should have made from the beginning:**

> Tightness equals 1 exactly on disjoint unions of NAE triangles. Every **connected** object with two or more constraints measured here sits at **0.6960 or below** — a genuine separation, and the one that "connectivity buys slack" was reaching for.

**Why the earlier versions were wrong, in one line each.** §2's 0.70 line, §4's 0.5866 and §5's 0.7594 were maxima over *fibres*, and fibres can be products; each number turned out to be a dilution level — a glued core averaged against however many disjoint triangles the `(r, m)` budget allowed. §6's "flat ceiling" was the constraint budget held fixed, not an invariant. The only claim that survived every correction is the qualitative one, and it survived because a product reaches 1 only when every component does.

**Curiosity worth flagging rather than reading into.** The connected supremum 0.6960 sits very close to the 0.70 line §2 drew from products. The two come from unrelated calculations, and I have no reason to think the coincidence is meaningful — noting it so that if it recurs at larger `r` someone looks, and so it is not quietly treated as confirmation.

**Status.** Observed supremum over what was enumerated: `r ≤ 7`, with `m ≤ 4` at `r = 7` and `m ≤ 5` at `r = 6`, NAE-triple fibres only. Not a proof, and not an asymptotic statement. Whether the connected supremum stays near 0.70 or climbs toward 1 with `r` is the open question, and it is now a well-posed one — which the previous framing was not, because it was measuring products.

## 9. Retraction: the connected supremum is 1, and this entire note produced nothing about gluing

§8's supremum of 0.6960 over connected objects is wrong, by the same mechanism as everything before it.

**The star is connected** — every arm shares the hub — and this session *proved* `d_cb(star k) = k−1` with `ℓ = kβ`, so its tightness is `(k−1)/k`:

| `k` | `r` | tightness | in the `r ≤ 7` sweep? |
|---|---|---|---|
| 2 | 5 | 0.5000 | yes |
| 3 | 7 | 0.6667 | yes |
| 4 | 9 | **0.7500** | **no** |
| 5 | 11 | **0.8000** | **no** |

`(k−1)/k → 1`. **So the supremum over connected objects is 1, not 0.6960** — the sweep's window (`r ≤ 7`) simply excluded the members of a family whose values I had proved hours earlier in the same session.

**What that leaves.** Disjoint unions of triangles *attain* tightness 1; the star family *approaches* it without reaching it. That distinction — attained versus approached — is the entire surviving content of the connected/disjoint comparison. **"Connectivity buys slack" is false.** Connected objects get arbitrarily close to the constant.

**So this note produced nothing about gluing.** Every quantitative claim it made was retracted: the 0.70 line (§2), the dense-end 0.5866 (§4), the `r=7` 0.7594 (§5), the flat ceiling (§6), the monotone decline (§5–6), and now the connected supremum (§8). The one durable thing it produced is **§7's additivity** — that `ℓ` and `d_cb` add over coordinate-disjoint blocks, so tightness is an `ℓ`-weighted average — which is correct, proved, machine-checked on six values, and belongs in `the_constant_is_attained.md` rather than here.

**The single error, made four times.** Every retracted claim was a maximum taken over a bounded enumeration and then read as a property of the objects. The bound moved — with `r`, with `m`, with how many disjoint blocks fit — and each time the movement looked like structure. The check that would have caught all four is one line long and was available every time:

> **Before reporting a supremum from an enumeration, evaluate the known parametric families at parameters outside the window.**

I had the star's closed form (`(k−1)/k`, proved) in this same session and did not evaluate it against my own supremum. That is not a subtle failure; it is not looking.

**Standing status of this note:** superseded in full except §7. Conjecture RC — tightness ≤ 1 for every fibre — remains unrefuted and is the substantive statement; nothing here bears on gluing.
