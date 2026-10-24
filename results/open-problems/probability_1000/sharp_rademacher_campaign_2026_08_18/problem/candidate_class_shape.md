# The campaign's first explicit candidate shape, and it is unique

Author: main session c53c1d50, 2026-08-19 ~14:2x.

The campaign's standing exposure has been stated the same way all along: **no explicit member of the residual class has ever been constructed**, so every number it has produced is a measurement on a known non-member. This does not close that gap — class membership cannot be verified against a definition we cannot read — but it produces the first explicit object with the right *signature*, and there turns out to be exactly one.

## 1. Where it came from

Not from guessing at the definition. The coverage sweep (`beta_is_the_absorption_threshold.md` §§15–16) found 136 configurations where **neither trivialising route applies** — neither `μ_min = 0` nor absorbability — which is precisely where the rooted target has content. Their largest group was dense: `r = 5`, four NAE triples, `|A| = 12`, `|D| = 12`.

Enumerating every 4-triple set on 5 coordinates and keeping those with an uncovered rooting: **60 triple-sets, every one with the identical signature** `|A| = 12`, `|D| = 12`, exactly 2 uncovered rootings. And up to relabelling the coordinates,

> **all 60 are the same object:**  `{(0,1,2), (0,1,3), (0,2,3), (1,2,4)}`.

## 2. Its properties

- **Dense.** `|A| = 12` of 32, density 0.375 — the four constraints kill 62.5% of the cube.
- **A large dual.** `|D| = 12 = 2.4 ×` the ambient dimension: 5 coordinates and **7 non-coordinate forms**, including the full-support `(1,1,1,1,1)` and the weighted `(2,1,1,1,0)`.
- **Two-connected.** The constraint hypergraph has **no cut vertex** — the closest computable stand-in for the class's "cyclic SCC" requirement, and exactly what the star and book fail.
- **Uncovered at exactly two rootings**, `W = (0,4)` and `W = (1,2,3)`, both at `L = 1.33333`.
- **Incoherence signature present.** Pairwise symmetric differences of the seven non-coordinate supports: min 1, mean 2.29, max 4 — mutually spread rather than aligned, which is the crosspolytope's incoherence pattern (R5: incoherence is the negation of alignment).

## 3. The alignment that makes it interesting

Its entropy defect is
  `ℓ = 5 − log₂12 = 3 − log₂3 = 1.41504`.

That is **exactly the campaign's spectral gap**. Layer III established that Erdős forces `ℓ ≥ 1` with equality only at support 2, and that the next admissible value is `1.4150` (support 3–4) — no component has `ℓ ∈ (1, 1.4150)`. So this object sits precisely at **the first admissible defect above the trivial one**, which is where the residual class must live if it lives anywhere: `ℓ = 1` is the coincident-pair regime that *is* the conjecture's constant, and everything harder starts here.

That was not designed in. The object was selected by being uncovered and dense; its defect landing on the gap is a property of the object, found afterwards.

## 4. What this is and is not

**It is:** the first explicit, canonical, fully-computable object that is simultaneously dense, two-connected, connector-incoherent by the available proxy, sitting exactly at the spectral gap, and carrying a rooted target with genuine content. Small enough that every question asked of it can be answered exhaustively.

**It is not** a verified class member. The defining term is not readable (`the_missing_tree_hunt_closed.md`), so "member of the residual class" cannot be checked, only approximated by signature. Nor is it a counterexample or a proof of anything.

**Why it is worth having anyway.** Every mechanism this campaign has proved — DRR, the arm decomposition, the boundary-multiplicity bound, and this session's absorption threshold — was calibrated on objects known *not* to be in the class, and the ledger says so. This is the first object where that objection is not immediately fatal. The natural next work is to run the campaign's existing machinery against it and see which mechanisms still bite.

**Caveat on uniqueness.** Unique *at `r = 5` among 4-triple sets*. Larger `r`, more constraints, or non-NAE constraint types were not searched, so "there is exactly one" is a statement about this window, not about the class.

## 5. Selection check: was the defect fixed by my search window? (run before publishing §3)

§3's claim — that the candidate's `ℓ = 1.41504` landing on the campaign's spectral gap is a post-hoc property rather than something I built in — is hollow if *every* `r=5` four-triple set has `|A| = 12`. Then `ℓ` would be fixed by the parameters I chose and the "alignment" would be an artifact of the window. That is the one check that could empty the claim, so it was run before the claim was allowed to stand.

Over **all 210** four-triple sets on 5 coordinates:

| `\|A\|` | `ℓ = 5 − log₂\|A\|` | all sets | with an uncovered rooting |
|---|---|---|---|
| 12 | **1.41504** | 135 | **60** |
| 14 | 1.19265 | 75 | **0** |

So `ℓ` was **not** fixed by the parameters — the population carries two distinct defects — and **uncoveredness selects exactly one of them.** Every uncovered set has `|A| = 12`; not one of the 75 sets at `|A| = 14` has an uncovered rooting. The selection is real.

**But the alignment must be stated carefully, and this is where the campaign has slipped before.** The spectral gap `1.4150` is a statement about a **single dependency's** defect — `ℓ = −log₂Pr[c·x = 0]`, with Erdős forbidding `ℓ ∈ (1, 1.4150)`. The `ℓ` here is a **fibre** defect aggregating four constraints. These are different quantities in different currencies, and treating them as the same is exactly the error already logged once this campaign (the `μ` verdict, corrected first for support-vs-conditional-defect currency).

So the honest statement is: **the numerical coincidence is real and the selection behind it is real, but whether the two `ℓ`s are the same quantity is unresolved.** If they are, this says the rooted target has content exactly at the first admissible defect — a clean tie between Layer III and Layer II. If they are not, it is a coincidence at three decimal places and nothing more. **Resolving which is the single most valuable question this object raises**, and unlike most of the campaign's open questions it is a definitional matter that a careful reading of the reconstruction can settle.

## 6. The campaign's machinery run against it — the target holds, with margin

Exact computation at every rooting (all bases, all selector assignments, DFS with a rank bound; `R_<` built from the ancestor side as in `beta_is_the_absorption_threshold.md` §6):

- **exact `d_cb` = 2**, over 6,000 optimal residual spaces.
- At **both uncovered rootings** — `W = (0,4)` and `W = (1,2,3)`, `L = 1.33333` — the minimised quotient `dim((R+R_<)/R_<)` is **2**, against a budget `(1/β)·L = 3.2126`.
- **The rooted target holds at every one of the 27 rootings**, with no exceptions.

**The margin is the interesting part.** The candidate clears the target by a factor of 1.6 (`2` against `3.21`). The threshold object — two disjoint NAE triples, sparse, four coordinates fewer of structure — clears it by **nothing at all**: left side `1`, budget `1.000000`, equality.

> **So density and incoherence do not make the rooted target harder here. The dense, two-connected, connector-incoherent object has more room than the sparse one.** The binding case is the threshold object, and it binds because its `L` is small, not because its structure is rich.

That is worth stating because it runs against the shape of the campaign's difficulty narrative, which locates the problem in *dense connector-incoherent cores*. On this family, at this size, the dense incoherent object is the comfortable one. One object at `r = 5` does not overturn an asymptotic story — the class is defined asymptotically and the mechanisms that matter there may not be visible at five coordinates — but it is the first data point taken on an object with the class signature rather than on an acknowledged non-member, and it points the opposite way.

**A correction to my own framing, caught by reading these numbers.** `beta_is_the_absorption_threshold.md` §14 described routes A and B as two ways of "trivialising" the target. That overstates route A. At `W = (0,)` here, `μ_min = 0` and `R_< = 0`, and the quotient is **2**, not 0 — route A removes the *absorption requirement* and leaves R7's bound `2ν + L + μ` to be checked, whereas route B (absorbability) genuinely forces the left side to 0. The coverage sweep's "covered" therefore means *handled without absorption*, not *automatically satisfied*. The sweep's conclusions are unaffected — it was classifying which mechanism applies, not asserting triviality — but the word was wrong and the distinction matters for anything built on it.

## 7. Tightness against constraint density — the reversal survives a directed test

§6's claim reverses the campaign's difficulty narrative, so the burden is on the claim. The directed test: measure

  `tightness = dim((R+R_<)/R_<) / ((1/β)·L)`

on every uncovered configuration — `1.000` is exactly tight, smaller is more room — and see whether it **rises** with constraint density, which is what the narrative predicts and what would refute me.

| object | constraints | `\|A\|` | uncovered `L` | LHS | budget | **tightness** |
|---|---|---|---|---|---|---|
| threshold pair | **2** | 36 | 0.41504 | 1 | 1.0000 | **1.0000** |
| disjoint pair | **2** | 36 | 0.41504 | 1 | 1.0000 | **1.0000** |
| book `p=4` | 4 | 34 | 0.90532 | 1 | 2.1813 | 0.4584 |
| candidate `r=5` | 4 | 12 | 1.33333 | 2 | 3.2126 | 0.6226 |

**The two-constraint objects are exactly tight. Every four-constraint object has 1.6× to 2.2× of room.** Tightness falls as constraints are added, not rises.

**A trap in my own instrumentation, worth recording.** The script tabulates `density = |A|/2ⁿ`, which is *fibre* density — the **inverse** of constraint density. Its printed legend said a positive correlation would support the campaign's narrative; with fibre density on the x-axis, positive correlation means the opposite. The table above is therefore read by **constraint count**, not by that column, and the correlation line the script prints must not be quoted without flipping its sense. A legend written before the axis was settled is exactly the kind of pre-written conclusion that reads as a finding on the next pass.

**Status.** Four objects at `r = 5, 6`; the `r = 6` five- and six-constraint rows were still computing when this was written and are not included. So this is a consistent direction across the objects available, not a law — and it remains a small-`r` observation about a class defined asymptotically. What it does support is that the tight case is characterised by **small `L`**, not by rich structure: the threshold objects bind because `L = β` is as small as a non-absorbable configuration can have, and adding constraints raises `L` faster than it raises the left side.

## 8. The strongest case that §§6–7 are wrong

Written deliberately against my own conclusion, because the conclusion reverses an established narrative and four data points are not much to reverse it with.

**1. Integer quantisation almost certainly dominates.** The left side is a *dimension* — an integer — and across every object measured it takes only the values 1 and 2. `L` is continuous. So "tightness" is a ratio whose numerator has two possible values and whose denominator varies smoothly; the apparent trend can be entirely an artefact of where the integer steps happen to fall relative to the budget. **This is the strongest objection**, and it is close to decisive at this scale: with the left side confined to `{1,2}`, almost any monotone story could be read off four points.

**2. The regimes may share no mechanism.** "Dense" at `r = 5` means four constraints on five coordinates. "Dense" in the campaign's asymptotic sense means a core of size `≍ log n · log log n`. There is no reason the same comparison holds across that gap, and the campaign's own rank lane locates its obstruction at `ν ≥ (c₀/2−o(1))·log n·log₂log n` — a quantity invisible at five coordinates.

**3. The comparison is not like-for-like.** Only *uncovered* configurations were measured. Denser objects have different numbers of uncovered rootings at different `L`, so the sets being compared are selected differently per object, not matched.

**4. `L` rises mechanically with constraints.** Each added fully-private NAE constraint adds about `β` to `L`, hence about `1` to the budget. If the left side rises more slowly than one per constraint *at small scale only*, tightness falls for arithmetic reasons that need not persist.

**The concrete check that would confirm I am wrong.** Compute tightness on objects where the left side reaches **3–5**, so quantisation no longer dominates — that needs `r ≥ 7` with enough constraints to push `d_cb` up. If tightness rises there, the campaign's narrative holds and §§6–7 are a small-number illusion. That computation is expensive but not out of reach, and it is the right next test rather than more objects at `r ≤ 6`.

**Revised status of §§6–7.** The *measurement* stands: the two-constraint objects are exactly tight and the four-constraint ones are not. The *interpretation* — that density does not drive difficulty — is **weakly supported and should not be built on**. What survives robustly is the narrower statement, which does not depend on any trend: **the binding configurations found anywhere in this campaign are those with `L = β`, the smallest `L` a non-absorbable configuration can have.**

## 9. §§6–7 are refuted by this session's own earlier data — the star family says the opposite

§8 named the check that would refute me and said it needed `r ≥ 7`. It did not: **the refuting evidence was already collected hours earlier in this same session**, in the very first sweep, and I did not recognise it until I stopped running new computations and re-read what I had.

The **k-arm NAE star**, measured at the start of the session with its exact closed forms:

  `L = kβ` exactly, and `d_cb = k − 1`.

So its tightness proxy is

  `d_cb·β / L = (k−1)β / (kβ) = (k−1)/k`,

which **rises monotonically toward 1 as constraints are added**: `0.500, 0.667, 0.750, 0.800, 0.833` for `k = 2..6`. More constraints, *less* room — asymptotically approaching exactly tight. That is the direction the campaign's difficulty narrative predicts and the opposite of what §§6–7 concluded from four points.

**So §6's interpretation is refuted, not merely weakened.** The four-object comparison in §7 was reading integer quantisation, exactly as §8 suspected. A family with a closed form and six data points beats four scattered objects, and it was in hand the whole time.

**Two caveats on the refutation itself, so it is not over-read in turn.** The star's `d_cb = k−1` is verified exactly only for `k ≤ 3` (§ the greedy is an upper bound), so the trend past `k=3` rests on values that could be smaller — and smaller `d_cb` would *lower* tightness, weakening the refutation. And `d_cb` is a proxy for the true left side `dim((R+R_<)/R_<)`, which is what the target actually consumes. Both caveats push the same way: the refutation is directionally right but its numbers are upper bounds.

**What stands after this.** The measurement in §7 (two-constraint objects exactly tight, four-constraint ones not) is real but does not mean what I said. The robust statement is unchanged and survives all of it: **the binding configurations are those with `L = β`.** For the star, `L = kβ` never equals `β` past `k=1` — yet tightness still approaches 1, so "small `L`" and "tight" are not the same condition, and §7's explanation of *why* the threshold objects bind was also too simple.

**The methodological point, which is the one worth keeping.** I proposed an expensive `r ≥ 7` computation to settle a question my own earlier output had already answered. The habit that would have caught it sooner is the one the brain already carries for external knowledge — *recall before grinding* — applied to **this session's own results**, which by hour twelve had become a corpus large enough to need searching rather than remembering.

## 10. The refutation in §9 is itself not established — bound-vs-value, third instance

§9 refuted §§6–7 using the star family's tightness `(k−1)/k`. That refutation has the same defect as the claim it killed.

**The star's numerator is a greedy upper bound.** `d_cb = k−1` is verified *exactly* only for `k ≤ 3`; beyond that it is what the greedy found, and the greedy has already been shown loose by up to 3× on other objects. Tightness has `d_cb` (or the true left side, which is `≤ d_cb`) in its numerator, so what the star data shows is

  `true tightness ≤ (k−1)/k`,

**an upper bound rising toward 1** — which is compatible with the true tightness rising, staying flat, or falling. It does not establish the trend it was used to assert.

**So both sides are unestablished.** §§6–7's claim (density gives room) reads integer quantisation off four points. §9's refutation (density costs room) reads a rising upper bound as a rising value. The question of how tightness moves with constraint count is **open**, and neither of my two confident answers is supported.

**What is exact, and stands.** The four-object table in §7 used the *minimised quotient over all optimal residual spaces* with `R_<` built from the ancestor side — not `d_cb` — so those numbers (threshold objects exactly 1.0000; book `p=4` 0.4584; candidate 0.6226) are real. What was never established is that they form a trend.

**The deciding computation, stated precisely so the next attempt does not repeat this.** Exact `d_cb`, or better the exact minimised quotient, for the star at `k ≥ 4`. An earlier attempt this session truncated and returned a *worse* bound (4) than the greedy's 3, so it is genuinely expensive — but it is the only thing that settles the direction. Until then the honest entry is: **tightness is exactly 1 at the threshold objects, and its behaviour as constraints are added is unknown.**

**Third instance in one session of the same error**, which is the part worth carrying: registered predictions confirming a greedy rather than the mathematics; `μ > L` rows from a `d_cb`-first search proving nothing; and now a refutation built on a rising bound. Each time the tell was identical — a quantity that is an upper bound was read as the value, and the direction of the inequality was not checked against the direction of the claim. **Before any comparative claim, state which side of the inequality the estimator sits on and whether the claim needs that side.**

## 11. Settled through k=4 on exact values: tightness rises

§10 left the direction open because both readings rested on the greedy. The deciding computation was dispatched to <box> and it answers the first open case.

**Exact `d_cb` for the star at `k = 4`: 3.** Exhaustive over all 715 bases of the 13-form dual, all selector assignments, DFS with a rank bound; positive control in the same run gave the NAE triangle exactly 1. So the greedy was tight here, and the exact sequence is now

  `d_cb = 1, 1, 2, 3` for `k = 1, 2, 3, 4`  →  `d_cb = k − 1` for `k ≥ 2`, exact through 4,

giving exact tightness `(k−1)/k` = **0.500, 0.667, 0.750** for `k = 2, 3, 4`. **Rising, on exact values.**

**So the direction is settled through `k=4`, and it settles against §§6–7.** Adding constraints costs room rather than giving it: the star family's tightness climbs toward exactly tight. §9's refutation, which §10 correctly downgraded for resting on a bound, is now established on the exact numbers for the cases computed. My original reading — that density gives room — is wrong, and the campaign's difficulty narrative is right on this family.

**What remains bounded rather than exact.** `k = 5, 6` were still running when this was written; if either breaks the `k−1` pattern the trend would need revisiting, though three exact points already rule out the flat-or-falling readings that §10 allowed. And tightness here still uses `d_cb` where the target consumes `dim((R+R_<)/R_<) ≤ d_cb`, so these are upper bounds on the true tightness — the *rise* is established for `d_cb`, and inherits to the true quantity only if the gap between them does not grow with `k`. That gap is the one thing left to check on this family.

**Worth noting about the process.** The question was open for two hours across three write-ups because each attempt to settle it locally hit the compute throttle and returned bounds. One 161-second run on a machine that was free settled it. The doctrine's *put heavy jobs on a research box* is usually framed as protecting the laptop; here it was the difference between three inconclusive documents and one exact answer.

## 12. The last caveat on the star closes: the tightness values are exact

§11 left one thing open — tightness was computed with `d_cb`, while the target consumes `dim((R+R_<)/R_<) ≤ d_cb`, so the rise would only inherit if the gap between them stayed bounded in `k`. **There is no gap.**

Rooted at the hub (`|W| = 1`), the ancestor block is a single coordinate carrying **no constraint**. Verified directly at `k = 1..4`: its fibre on `W` is the full one-dimensional cube `{(−1),(+1)}`, its dual is a **single** form, that form *is* its own basis, so **no form needs a residual and `R_< = 0`.** Hence

  `dim((R + R_<)/R_<) = rank(R) = d_cb` exactly.

So the star's tightness is exact, not an upper bound, and the caveat is discharged rather than carried.

**The numbers, now fully exact.** The budget is `(1/β)·L = (1/β)·kβ = k` — an integer — and `d_cb = k−1` for `k ≥ 2`:

| `k` | `d_cb` (exact) | budget | tightness |
|---|---|---|---|
| 1 | 1 | 1 | **1.000 — exactly tight** |
| 2 | 1 | 2 | 0.500 |
| 3 | 2 | 3 | 0.667 |
| 4 | 3 | 4 | 0.750 |

**A third exactly-tight object, which I had not noticed as one.** `k = 1` — the single NAE triangle rooted at its hub — has left side 1 against budget 1. It joins the two-disjoint-triples objects, and like them it sits at `L = β`. So every exactly-tight configuration found anywhere in this campaign has `L = β`, which is the cleanest form the threshold statement has taken.

**And the family's shape is not monotone.** Tightness is 1 at `k=1`, **dips to 0.5** at `k=2`, then climbs back: 0.667, 0.750, heading to 1. So "adding constraints costs room" is right only from `k=2` onward; the first constraint is the tight one and the second buys the most slack. That is a more specific statement than §11's, and it is exact.
