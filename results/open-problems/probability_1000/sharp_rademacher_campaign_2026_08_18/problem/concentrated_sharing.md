# Sharing concentrated at one coordinate costs exactly one dimension; spread sharing costs more

Author: main session c53c1d50, 2026-08-19 ~17:3x. Written after retracting `gluing_is_a_cliff.md` in full. That note failed because it read maxima over bounded enumerations as structure. This states the same territory using *proved family behaviour* instead, which is the form that survives.

## 1. Conjecture RC holds across every family, tested past any window

`RC: tightness = d_cb·β/ℓ ≤ 1`, equivalently `|A| ≤ 2^r(3/4)^{d_cb}`. Followed along six parametric families with exact `d_cb`:

| family | parameter range | tightness |
|---|---|---|
| disjoint triples | m = 1..3 | **1.0000** throughout |
| star | k = 1..4 | 1.0000, 0.5000, 0.6667, 0.7500 |
| wheel | k = 3..7 | 0.4150, 0.6960, 0.5388, 0.4536, 0.5813 |
| book | p = 2..6 | 0.6121, 0.5000, 0.4548, 0.4343, 0.4245 |
| chain | m = 2..4 | 0.5000, 0.6667, 0.5000 |
| fan | m = 3..5 | 0.6387, 0.5054, 0.5983 |

Nothing exceeds 1. The maximum is exactly 1, attained by disjoint unions (and by `star k=1`, which *is* a single triangle). **RC survives an adversarial test that follows families rather than filling a window** — which matters, because a window-bounded search is precisely what produced four wrong claims earlier today.

## 2. The structural fact: it is *where* the sharing is, not how much

The star and the chain have the **same number of coordinate identifications** — `k−1` and `m−1` — and behave completely differently:

| parameter | star `d_cb` | chain `d_cb` | star tightness | chain tightness |
|---|---|---|---|---|
| 2 | 1 | 1 | 0.5000 | 0.5000 |
| 3 | 2 | 2 | 0.6667 | 0.6667 |
| 4 | **3** | **2** | **0.7500** | 0.5000 |

The star's `d_cb = k−1` is **proved** for all `k`, so its tightness `(k−1)/k` climbs to 1. The chain already drops below `m−1` at `m = 4` and does not track it.

> **So the count of identifications predicts nothing. What distinguishes them is that the star's sharing is entirely concentrated at a single coordinate — the hub — while the chain spreads it across `m−1` distinct coordinates.**

This is exactly what the star's proof says structurally. Every dependency among the residuals must pass through the hub leftover `e_q`; two independent ones would differ by a dependency supported on arm leftovers alone, which the derangement argument forbids. **One shared coordinate buys exactly one dependency, hence exactly one dimension off `k`.** Spread the sharing and no single form plays that role, so no such economy exists.

## 3. Why this is stated as families and not as a supremum

`gluing_is_a_cliff.md` tried to capture this territory four times and was retracted four times. Each version maximised a ratio over an enumeration and read the maximum as a property; the enumeration's boundary moved with `r`, with `m`, and with how many disjoint blocks fit, and the movement looked like structure every time.

The statement here avoids that failure because it makes no claim about a maximum. It compares two families whose `d_cb` is known — one proved in closed form for all `k`, the other computed exactly at three points — and reports how they differ. **A family comparison cannot be an artefact of an enumeration window, because there is no window.**

## 4. Limits

The chain's behaviour rests on three exact values (`m = 2,3,4`) with no closed form, so "does not track the star" is measured, not proved; `m = 5` would strengthen or break it. Whether *any* connected family other than the star approaches 1 is open — none of the five tested does. And every object here remains a known non-member of the residual class.

## 5. [SUPERSEDED by 6, 7 and 8] Among trees of triangles it is all-or-nothing, and the star is the unique maximiser

> Superseded. The all-or-nothing reading is refuted in 6; every formula below it is refuted in 8. Read 8 before using anything in this section.

§2 compared two families. The sharpest form of the claim compares *every* topology at once, and a simplification makes that a clean test with no window at all.

**All trees of `k` triangles have the same `ℓ`.** Joining `k` triangles at `k−1` single coordinates gives `r = 3k − (k−1) = 2k+1` and `|A| = 6·3^{k−1}` — each attachment conditions on one coordinate, leaving 3 completions — whatever the shape. So

  `ℓ = (2k+1) − log₂(6·3^{k−1}) = kβ` exactly, **independent of topology**.

Therefore `tightness = d_cb/k` for every tree, and comparing topologies is comparing `d_cb` alone, with `ℓ` held fixed *by construction* rather than by an enumeration boundary.

**Enumerating every triangle-tree** (15 labelled at `k=3`, 105 at `k=4`), with exact `d_cb`. Confirmed `ℓ = 1.24511 = 3β` and `1.66015 = 4β` throughout, as predicted.

| `k` | attachment profile | `d_cb` | tightness |
|---|---|---|---|
| 3 | (2,) — star | 2 | 0.6667 |
| 3 | (1,1) — path | 2 | 0.6667 |
| 4 | **(3,) — star** | **3** | **0.7500** |
| 4 | (2,1) | 2 | 0.5000 |
| 4 | (1,1,1) — path | 2 | 0.5000 |

> **At `k = 4` the star is the unique maximiser, and the effect is all-or-nothing: `(2,1)` — two attachments concentrated, one not — scores exactly the same as the fully spread `(1,1,1)`.** Partial concentration buys nothing. It is total concentration or the floor.

At `k = 3` the star ties with the path, which is what one expects: three triangles leave too little room for the topologies to separate.

**Positive control**: the star appears in the enumeration at `d_cb = k−1 = 3`, matching the closed form proved in `star_family_proved.md`. Without that the "no other tree reaches it" would be an unverified absence.

**So the claim reaches its sharpest form.** It is not that less sharing is better, nor that concentration helps by degrees. Among objects with *identical* `ℓ` and *identical* numbers of identifications, **`d_cb = k−1` requires every attachment at a single coordinate, and any deviation whatsoever drops it to 2.** That matches the star's proof exactly — the economy comes from one form, the hub leftover, being able to carry the single permitted dependency; split the attachments and no form is in that position.

**Limits.** `k = 3, 4` only; `k = 5` (r=11, 945 labelled trees) is the natural confirmation and was not run. And this concerns trees — objects with cycles, like the wheel and fan, are outside it.

## 6. [SUPERSEDED by 7 and 8] The all-or-nothing reading was wrong: `d_cb` tracks the LARGEST attachment group

> Superseded twice. `max(2, largest group)` is refuted in 7 by chain `m=5`, and its replacement is refuted in 8 by `(3,2)` at `k=6`.

§5 read the `k=4` table as all-or-nothing — total concentration or the floor. The falsifier it named was a non-star profile reaching `k−1` at `k=5`. That did not happen, but something else did.

**`(3,1)` at `k=5` gives `d_cb = 3`** — not the floor of 2, and not the star's 4. An intermediate value, which all-or-nothing forbids. (461s; `ℓ = 2.07519 = 5β` as construction requires.)

Checking every tree value against "size of the largest attachment group":

| profile | largest group | `d_cb` | fits `max(2, largest)`? |
|---|---|---|---|
| `k=5` star `(4,)` | 4 | 4 *(proved)* | yes |
| `k=5` `(3,1)` | 3 | **3** | yes |
| `k=4` star `(3,)` | 3 | 3 | yes |
| `k=4` `(2,1)` | 2 | 2 | yes |
| `k=4` `(1,1,1)` | 1 | 2 | yes — floor |
| `k=3` star `(2,)` | 2 | 2 | yes |
| `k=3` path `(1,1)` | 1 | 2 | yes — floor |

> **`d_cb = max(2, largest attachment group)` fits all seven values at `k ≥ 3`.** So concentration is not a threshold but a *size*: `d_cb` tracks how big the biggest group of attachments-at-one-coordinate is, and everything else about the topology is invisible to it.

**What that makes of the star.** The star is the tree whose single group is as large as possible — all `k−1` attachments at one coordinate — so it is the unique tree with `d_cb` growing linearly in `k`, hence the unique tree whose tightness climbs to 1. Every other topology caps its largest group below `k−1` and its tightness with it. That is a sharper and more useful statement than either "concentration matters" or "all-or-nothing":

> **Tightness → 1 requires a single attachment group growing linearly in `k`.**

**The `k=2` exception, stated rather than smoothed.** Star `k=2` has `d_cb = 1`, while `max(2, 1) = 2`. So the formula holds for `k ≥ 3` and fails at `k = 2`, where there is only one attachment and the floor argument does not apply. I have not chased that; with one exception in seven points the honest label is a fitted pattern, not a law.

**Still pending.** `(2,2)` and `(2,1,1)` at `k=5` were queued behind `(3,1)` and had not returned; both should give 2 if the formula holds, and either giving 3 would break it. And the formula is fitted to seven points across three values of `k` — it is a description of what was measured, not a derivation. What *is* proved is the star endpoint, `d_cb = k−1`.

## 7. [SUPERSEDED by 8] The largest-group formula is refuted too; a two-term formula fits everything

> Superseded. The two-term formula stated here is **false**: `(3,2)` at `k=6` has `d_cb = 4`, not the 3 it predicts. See 8. The nine predictive hits recorded below are real and were not enough.

§6's `d_cb = max(2, largest attachment group)` is wrong. **Chain `m=5` returns `d_cb = 3`** (110s, `ℓ = 2.07519 = 5β`, tightness 0.6000). The chain's profile is `(1,1,1,1)` — largest group 1 — so that formula predicts 2.

**What the chain reveals is a second term.** Its values across `k` are `1, 2, 2, 3` at `k = 2,3,4,5`, which is `⌈k/2⌉`. Combining that with the group term fits every tree value measured:

> **`d_cb = max(largest attachment group, ⌈k/2⌉)`**

| object | largest group | `⌈k/2⌉` | formula | measured |
|---|---|---|---|---|
| star `k=2` | 1 | 1 | 1 | **1** |
| star `k=3` | 2 | 2 | 2 | **2** |
| path `k=3` | 1 | 2 | 2 | **2** |
| star `k=4` | 3 | 2 | 3 | **3** |
| `(2,1)` `k=4` | 2 | 2 | 2 | **2** |
| `(1,1,1)` `k=4` | 1 | 2 | 2 | **2** |
| star `k=5` | 4 | 3 | 4 | **4** *(proved)* |
| `(3,1)` `k=5` | 3 | 3 | 3 | **3** |
| chain `k=5` | 1 | 3 | 3 | **3** |

Nine for nine, and it **repairs the `k=2` exception** that §6 had to state as a failure: `max(1, 1) = 1`, matching star `k=2`. A formula that fixes an anomaly it was not built to fix is worth more than one fitted to the same points.

**What the second term means.** `⌈k/2⌉` is a floor that grows with the number of triangles regardless of topology — so even maximally spread attachments cannot hold `d_cb` down as `k` grows. That kills a reading §6 invited: it is not that spread topologies stay cheap, they simply grow at half the rate. The star's `k−1` beats `⌈k/2⌉` for `k ≥ 3`, which is exactly when the star separates from everything else — and at `k = 3` the two terms coincide at 2, which is why the star and path tie there. The tie was not a small-`k` accident; the formula predicts it.

**A registered prediction, from the formula rather than fitted to the answer.** `(2,2)` and `(2,1,1)` at `k = 5` have largest group 2 and `⌈5/2⌉ = 3`, so both should give **3**. §6's formula said 2 for both. Those two cases were already queued and running when this was written, so the discrimination is genuine rather than retrospective.

**Status.** Nine exact values, one proved endpoint (`star = k−1`), and a two-term fit with no exceptions. Still a fit: no derivation of the `⌈k/2⌉` term, and nothing here covers trees at `k ≥ 6` or objects with cycles.

### 7.1 The prediction landed

Both queued cases returned, and both match the two-term formula against the one it replaced:

| profile `k=5` | largest group | `⌈k/2⌉` | new formula | §6 formula | **measured** |
|---|---|---|---|---|---|
| `(2,2)` | 2 | 3 | **3** | 2 | **3** (671s) |
| `(2,1,1)` | 2 | 3 | **3** | 2 | **3** (219s) |

Both at `ℓ = 2.07519 = 5β` as construction requires, tightness 0.6000.

The two formulas disagreed on these cases, the predictions were written while the runs were already in flight, and the new one is right. **`d_cb = max(largest attachment group, ⌈k/2⌉)` now stands at eleven exact values with no exceptions**, one of them (`star = k−1`) proved rather than measured.

That is a different epistemic status from the three readings this note went through earlier. Those were descriptions fitted to whatever had been enumerated, and each died when the enumeration moved. This one was stated in advance of two measurements that discriminated it from its predecessor, and survived. It is still a fit — no derivation of `⌈k/2⌉`, trees only, `k ≤ 5` — but it is a fit that has been given a chance to fail and did not take it.

## 8. The two-term formula is refuted at k=6

`(3,2)` at `k=6` returns **`d_cb > 3`** (2871s, exhausting the `d=3` search; `|D| = 19`,
`ℓ = 6β`). Largest group 3, `⌈6/2⌉ = 3`, so `max(3,3) = 3` was the registered prediction.

> **`d_cb = max(largest attachment group, ⌈k/2⌉)` is false.**

Eleven exact values and nine straight predictive hits did not save it. The tenth registered
prediction killed it — which is what registering them is for, and it is the first pattern in this
note to die on a stated prediction rather than on a re-enumeration that moved under it.

**What survives.** The lower bound `d_cb ≥ ⌈k/2⌉` is untouched: 3 is a lower bound and the
measured value exceeds it. That bound was derived from the explicit dual rather than fitted
(`why_ceil_k_over_two.md`), and the refutation of the fit is not evidence against the derivation.
The star theorem `d_cb(star k) = k−1` is likewise untouched.

**What dies** is the claim that counting and the largest group are the *only* obstructions. `(3,2)`
sits strictly above both, so there is a third mechanism, and the disjoint family in
`why_ceil_k_over_two.md` §10 already said the transversal term was a tree-specific proxy for
something the group does not measure. That warning was recorded before this run and this is it
arriving.

**A guess worth testing rather than asserting.** `(3,2)` has two attachment coordinates, hosting
local stars of 4 and 3 triangles (counting the base triangle each shares), whose star obstructions
are 3 and 2. Naively adding and discounting the shared base gives `3 + 2 − 1 = 4`. Disjoint triples
add the same way — `m` blocks of 1 giving `m` — and a single star does not add at all, giving
`k−1`. So the mechanism may be additivity of local star obstructions over attachment coordinates,
with the sharing discounted. Stated as a guess; the exact value of `d_cb((3,2))` is not yet known,
only that it exceeds 3.

**Immediate next step.** Get the exact value. The run capped at its prediction, so it proves
`d_cb ≥ 4` and nothing more.
