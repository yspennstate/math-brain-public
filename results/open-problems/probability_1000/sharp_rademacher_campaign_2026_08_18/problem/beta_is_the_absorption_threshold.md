# β is the absorption threshold, and that is where the constant 1/β comes from

Author: main session c53c1d50, 2026-08-19 ~06:1x. The campaign has carried `C ≥ 1/β = 1/log₂(4/3) = 2.40942` as a **floor**, obtained by exhibiting NAE three-circuit products that force it. A floor tells you the constant cannot be smaller; it does not say why that number and not another. This gives a mechanism, and the mechanism is exhaustively checked.

## 1. The right question is absorbability, not `d_cb`

The rooted target has two clauses:

  `dim((R+R_<)/R_<) ≤ C·L_{Q|W}`  and  `R ∩ span W ⊆ R_<`.

If a certificate's **entire** residual space lies inside `span W`, then `R = R ∩ span W ⊆ R_<` by the second clause, so the left side is **0** and the target holds trivially — whatever the rank of `R`, and however small `L` is. So the question that decides a configuration is not "how large is `d_cb`" but:

> **ABSORBABLE(A, W):** is there a coordinate basis `G ⊆ D(A)` and a signed selector for every form whose residuals all lie in `span W`?

This has a closed form needing no rank minimisation. Let `π` restrict a form to the coordinates **outside** `W`. Then `f − σg ∈ span W ⟺ π(f) = σ·π(g)`, so

> **ABSORBABLE ⟺ some basis `G ⊆ D` meets every ±-class of `π(D)`.**

Necessary: `π(D)` has at most `dim` classes. Sufficient on top: one representative per class can be chosen independent. Both are small checks — and both are far cheaper than the `d_cb` search that had been eating the night.

## 2. The threshold, exhaustively

Enumerating **every** set of NAE triples and **every** boundary set `W`:

| `r` | configurations | with `L < β` | non-absorbable among them |
|---|---|---|---|
| 4 | 192 | 42 | **0** |
| 5 | 16,222 | 832 | **0** |
| 6 | 393,212 (triple-sets of size ≤ 4) | 17,587 | **0** |

> **Claim B (survives exhaustive search at `r ≤ 6`): `L_{Q|W} < β` ⟹ the configuration is absorbable**, hence its target left side is 0.

And `β` is **attained**: the minimal non-absorbable configuration is two disjoint NAE triples with `W` equal to one of them, giving `L = 3 − log₂6 = 2 − log₂3 = β` exactly. Controls fire in both directions in the same pass — the book at its shared pair is absorbable at `L = 0.235`, and the two-disjoint-triples object is **not** absorbable at `L = β` — so a zero counterexample count is a finding rather than a dead detector.

## 3. Why this explains the constant

The mechanism is visible once stated. Absorption via `span W` fails exactly when the private part carries a constraint the boundary cannot see. The **cheapest** such constraint is a single fully-private NAE triple, whose conditional defect is exactly `3 − log₂6 = β`. So:

- below `β` there is no room for a private constraint, every configuration absorbs, and the left side is 0 — nothing to pay for;
- at `β` the first non-absorbable configuration appears, and it needs one dimension of residual;
- and `(1/β)·β = 1` **exactly**.

> **`1/β` is precisely the exchange rate at which the smallest non-absorbable defect pays for one dimension of residual.** Not a fitted constant, and not merely a floor — the threshold of a mechanism.

This also re-reads the campaign's floor result. NAE three-circuit products force `C ≥ 1/β` because they are built from exactly the minimal private NAE constraint; they were never a special family, they were the threshold object in disguise.

## 4. What is established and what is not — stated before anyone asks

**Established.** Absorbable ⟹ left side 0 (clause (ii) plus `R ⊆ span W`, both exact). Claim B for `r ≤ 6`, exhaustive over all triple-sets and all `W` at `r = 4, 5`, and over triple-sets of size ≤ 4 at `r = 6`. `β` attained by an explicit object. The identity `(1/β)·β = 1`.

**Not established at the time of writing** — *now closed, see §6.* That non-absorbable ⟹ left side `≥ 1`. That step needs the ancestor-paid space `R_<`, which the absorbability computation does not have — a non-absorbable configuration has `R ⊄ span W`, but `R` might still lie in `R_<` by another route.

Also not established: anything beyond `r = 6`, anything outside NAE-triple fibres, and — the campaign's standing exposure — anything about actual members of the residual class. Every object here is a known non-member.

## 5. How this sits with the rest of the campaign

It sharpens rather than contradicts. `the_rooting_must_not_explain_away_the_constraints.md` showed the naive `d_cb ≤ C·L` fails with unbounded ratio on the book; this says why that failure is harmless — the book is absorbable, so its true left side is 0, and the blow-up happens exactly where the second clause does all the work. **The two clauses are complementary here, not in tension** — which is worth setting against `the_two_clauses_are_in_tension.md`, where on horn 1 they genuinely pull against each other. Tension in one regime, complementarity in the other, and the threshold `β` is the boundary between them.

## 6. The gap closes, and the constant is exactly tight (added ~06:4x, same session)

§4 named one missing step — that non-absorbable forces a left side of at least 1 — and called closing it the most valuable next move. It closes, by an argument whose one structural input I checked rather than assumed.

**`R_< ⊆ span W`.** The ancestor-paid space is accumulated from ancestor blocks, whose residuals are built from *their* dual forms, which live on *their* coordinates — and ancestor coordinates are exactly the boundary. For the threshold object the ancestor block is the NAE triangle on `W = {0,1,4}`; its certificate has `d_cb = 1` and residual space `span(−e₀+e₁)`, and the containment in `span W` is confirmed by direct computation rather than by the argument alone.

**The inference is then immediate and covers every certificate, not just optimal ones.** Non-absorbable means *no* basis-and-selector choice puts `R` inside `span W`. Since `R_< ⊆ span W`, every certificate has `R ⊄ R_<`, hence

  `dim((R + R_<)/R_<) ≥ 1` for **every** certificate.

**Confirmed numerically, and it is tight.** The threshold object has `d_cb = 2` with **2,304** distinct optimal residual spaces; the quotient `dim((R+R_<)/R_<)` takes values `{1, 2}` across them, so the minimum is exactly **1**. The target's budget there is `(1/β)·L = (1/β)·β = 1.000000`. So

> **left side = 1 = budget. The rooted target with `C = 1/β` holds at the threshold object with EQUALITY and zero margin.**

The control behaves oppositely in the same pass: the book (`p=3`, rooted at its shared pair) has all 32 of its optimal residual spaces inside `span W`, so an absorbing choice exists and its left side is 0 — which is why its unbounded `d_cb/L` was harmless.

**What this establishes on the computable family.** For NAE-triple fibres at `r ≤ 6`, `C = 1/β` is not merely a floor and not merely a threshold — it is **the smallest constant that works, and it is attained**. Below `β` every configuration absorbs and costs nothing; at `β` the first non-absorbable object appears and costs exactly one dimension; and `1/β` is exactly the rate that pays for it.

**Carried caveats, unchanged.** The `R_< ⊆ span W` step is a reconstruction of the packet's definition — checked on this object, argued structurally in general, but not verified against a definition we cannot read. Everything is NAE-triple fibres at `r ≤ 6`, and every object remains a known non-member of the residual class.

## 7. β is universal, and it means "forbids a quarter" (added ~07:4x, same session)

§3 offered a mechanism — absorption fails when the private part carries a constraint the boundary cannot see, and the cheapest NAE triple has defect β. That story predicts something falsifiable: **change the constraint type and the threshold should move to that type's own defect.** It is wrong, and what replaces it is better.

**The test.** Constraint types are built by forbidding `k` antipodal pattern-pairs on `n` variables (keeping the fibre antipodal, which the dual machinery needs), giving defect `n − log₂(2ⁿ − 2k)`. Each type is tested identically: two disjoint constraints on `r = 2n` coordinates, `W` equal to one of them, plus a sweep over every other boundary set of that size.

| `n` | `k` | defect | vs `β` | non-absorbable? |
|---|---|---|---|---|
| 5 | 1 | 0.093109 | < | no |
| 4 | 1 | 0.192645 | < | no |
| 5 | 2 | 0.192645 | < | no |
| 5 | 3 | **0.299560** | < | **no** |
| 4 | 2 | 0.415037 | = β | **YES**, min `L` = β |
| 5 | 4 | 0.415037 | = β | **YES**, min `L` = β |
| 5 | 5 | 0.540568 | > | YES |
| 4 | 3 | 0.678072 | > | YES |

**Perfect separation at exactly `β`, across two arities and eight types.** The `n=5, k=3` row is the one that matters: its defect 0.2996 sits strictly inside the gap between the previously-tested 0.193 and `β`, so it could have broken the cutoff. It was predicted "no" in advance and came out "no".

Earlier types fit the same line: NAE4 (0.193) and NAE5 (0.093) never break absorption — across 147,575 configurations for NAE4 — while parity4 (defect 1.0) breaks it 59,312 times at the same `r = 8`, which is what proves the detector was alive for NAE4's zero.

**What `β` actually is.** Every type whose defect equals `β` allows exactly `3/4` of its patterns, since `β = log₂(4/3) = −log₂(3/4)`. Reading all twelve types tested by the *fraction forbidden* rather than by the defect:

- forbids `1/16`, `1/8`, `3/16` — NAE5, NAE4, `n5k1`, `n5k2`, `n5k3`, `n4k1` — **absorbable, every one**;
- forbids **exactly `1/4`** — NAE3, `n4k2`, `n5k4` — **non-absorbable, every one**;
- forbids `5/16`, `3/8`, `1/2` — `n5k5`, `n4k3`, parity4 — **non-absorbable, every one**.

> **Absorption fails exactly when a single private constraint forbids at least a quarter of its patterns, and `β = log₂(4/3)` is that quarter's defect. The constant `1/β` is the rate that converts one such quarter into one dimension of rank.**

This is why NAE three-circuit products were the floor family: an NAE triple forbids 2 of 8 patterns — exactly a quarter, on the smallest arity that admits one. It was the minimal quarter-forbidding constraint all along.

**Status.** A clean empirical law with perfect separation over twelve constraint types at `n = 3, 4, 5`, one registered prediction hit on the decisive case, and controls alive in both directions. **Not proved.** The obvious next question is why a quarter — what breaks in the dual when a constraint's allowed set drops to `3/4` of the cube.

## 8. Why a quarter: the largest level set of a non-coordinate form (added ~08:2x, same session)

§7 ended on "why a quarter — what breaks in the dual when the allowed set drops to 3/4 of the cube". Here is the answer, exhaustively checked.

**The idea.** A coordinate form `±eᵢ` is ±1-valued on the *whole* cube, which is why coordinates are always in the dual. A **non-coordinate** form is ±1-valued only on its level set `{x : f·x ∈ {±1}}`, a proper subset. So an *extra* dual form can appear only once the allowed set has shrunk enough to fit inside some non-coordinate form's level set. For the NAE triple that form is the homogenizer `h = e₁+e₂+e₃`: on the six not-all-equal points the signs are two-of-one and one-of-the-other, so `h·x = ±1` exactly there — 6 of 8, exactly `3/4`.

> **Claim Q: the largest level set of any non-coordinate form is exactly `(3/4)·2ⁿ`.**

**Exhaustive test** over every antipodal spanning subset of the cube, recording whether the dual exceeds the `n` coordinates:

| `n` | \|S\| | fraction of cube | spanning subsets | with an extra dual form |
|---|---|---|---|---|
| 3 | 8 | 1.000 | 1 | 0 |
| 3 | 6 | **0.750** | 4 | **4** |
| 4 | 16 | 1.000 | 1 | 0 |
| 4 | 14 | 0.875 | 8 | **0** |
| 4 | 12 | **0.750** | 28 | **16** |
| 4 | 10 | 0.625 | 56 | 48 |
| 4 | 8 | 0.500 | 58 | 58 |

The `n = 4, |S| = 14` row carries the weight: at `7/8` of the cube — above the boundary — **not one** of the eight spanning subsets admits an extra form. Extras first appear exactly at `3/4`, and never above it.

**So the chain closes.** A set larger than `3/4` of the cube admits no non-coordinate dual form, so its dual is the coordinates alone; extra dual forms are what a certificate must select against; and `β = log₂(4/3) = −log₂(3/4)` is precisely the defect of the largest allowed set that still admits one. **The quarter is not a fitted threshold — it is the maximum fraction of the cube a non-coordinate linear form can cover.**

**The one soft link, named.** "Extra dual form ⟹ absorption fails" holds on all eight product objects but is **not** a general implication: the book has `|D| = 8 > r = 5` and is nonetheless absorbable. So the two thresholds coincide at `3/4` on the objects tested, and Claim Q explains *why `3/4` is distinguished at all*, but the step from "an extra form exists" to "no certificate absorbs" is empirical rather than proved. That is the remaining gap in the explanation, and it is now a sharp question about *which* extra forms survive restriction outside `W` — not the open-ended "why this constant".

## 9. An attempt to close the soft link, and why it failed (added ~09:0x, same session)

§8 left one empirical step: "an extra dual form exists" ⟹ "no certificate absorbs". Working the two objects by hand suggested it was really a counting fact.

- **The book** (`W` = shared pair, `Q` = the page coordinates). Its extra forms are `e₀+e₁+eᵢ`: when `s₀ ≠ s₁` the first two cancel and it reads `sᵢ`; when `s₀ = s₁` the page is forced to `−s₀` and it reads `s₀`. Either way ±1. Restricted outside `W` it becomes `π(eᵢ)` — the **same** class as the coordinate. So the extras add no new class, and the book absorbs.
- **The threshold object** (two disjoint NAE triples, `W` one of them). Its private extra `h = e₂+e₃+e₅` lives **entirely** in `Q`, so `π(h)` is genuinely new — a fourth class on three private dimensions — while `h` is linearly dependent on `e₂,e₃,e₅`, so no basis can carry `h` and all three. It fails by counting.

That suggested **Criterion C: absorbable ⟺ #{nonzero π-classes} ≤ dim(Q)**. Tested against the direct computation over 11,780 configurations: **7,913 agree, 3,867 disagree. Criterion C is false.**

Every disagreement runs the same way — the criterion says non-absorbable, the direct computation says absorbable — and the reason is visible in the smallest of them (book `p=2`, `W = {0,2}`: 3 nonzero classes on `dim(Q) = 2`, yet absorbable). **A basis element can carry a nonzero π-class while drawing its independence from its `W`-part.** Two forms with different π-classes can be independent in the full space even when their π-parts are dependent, so the number of coverable classes is bounded by `r`, not by `dim(Q)`. My hand argument was sound for the threshold object precisely because its extra form has no `W`-part to be rescued by — and that is exactly what does not generalise.

**Where this leaves things.** §7's quarter law and §8's Claim Q are untouched; this was an attempt to upgrade the bridge between them from empirical to proved, and it failed. The bridge stays empirical. What the failure buys is a sharper target: the criterion is not about counting classes but about whether an extra form's **private part** can be separated from the coordinates it depends on — a question about the interaction of `π` with linear independence, not about cardinality. The next attempt should be phrased there.

## 10. A second attempt, refuted from the other side — and what that brackets (added ~10:0x)

§9 killed **Criterion C** (`absorbable ⟺ #nonzero π-classes ≤ dim(Q)`) as too strict. The failure pointed somewhere sharper, so the next candidate was:

> **Claim R′: absorbable ⟺ no non-coordinate dual form is supported entirely inside `Q`.**

Motivated by the two objects: a form living wholly in `Q` restricts to itself, giving a class no coordinate provides while being dependent on `Q`'s coordinates — whereas the book's extras `e₀+e₁+eᵢ` straddle `W`, so their class is already carried by `eᵢ`.

**Also false: 111 mismatches of 492 — and in the opposite direction.** Every failure is `direct = not absorbable`, `claim = absorbable`; the cleanest is the book with `W = {0}`, a single boundary coordinate. Its extras all touch coordinate 0, so R′ sees nothing wholly private and predicts absorption, but no certificate absorbs. **With too little boundary, absorption fails for reasons that have nothing to do with extra forms** — there simply is not enough room in `span W` to put the residuals.

**What the pair of failures brackets.** Criterion C was too strict (3,867 false negatives), R′ too permissive (111 false positives), so the truth lies strictly between a cardinality count and a support condition. The exact characterisation is the one absorbability already is — a **matroid transversal** problem, and therefore Rado's condition: *an independent system of distinct representatives exists iff every subfamily of π-classes spans at least its own size.* That is exact but not a closed form, and neither simplification survives.

**Status of the explanation, honestly.** §7 (the quarter law over twelve constraint types) and §8 (Claim Q, exhaustive) stand. The bridge between them — from "a quarter-forbidding private constraint" to "no certificate absorbs" — has now resisted two attempts and **remains empirical**. What the two failures buy is the shape of the answer: it must involve both the rank of the classes' union *and* how much boundary is available, since each failed criterion ignored one of those.

## 11. Connecting to the campaign's own frame (R7), and an inconclusive measurement (added ~10:4x)

Three failed attempts at the bridge is the cue to recall rather than grind, and the brain already held the frame. The rank lane's memo (`rank_lane_the_support_rank_deficit_is_theta_log_n_2026_08_19`) proves

  **R7:** `dim((R+R_<)/R_<) ≤ 2ν + L + μ`, where `μ` is the **unpaid boundary rank**,

and states the consequence directly: *absorption is needed only when `μ ≫ L`*, calling "do residual-class blocks have `μ = O(L)`?" the cheapest unexplored hypothesis on the board. That is the same bridge approached from the other end, in vocabulary the campaign already owns — so the right move is to use `μ`, not to invent a third notion.

Two useful cross-checks fell out of the recall. The rank lane's exhaustive computation gives the S9 NAE star `d_cb = 2` with forced leak exactly 1 over all 10,976 certificates, which **matches my independent exact `d_cb = 2` for star `k=3`** — two different code paths agreeing on a nontrivial value. And what I have been calling Conjecture R is the campaign's **Conjecture RC**, previously recorded as having "small-rank evidence only": §§7–8 upgrade it from evidence to a mechanism plus a tightness witness.

**The measurement, and why it decides nothing.** Measuring `μ` against `L` over the families gives `μ > L` in 117 configurations, worst ratios ≈ 5.7. **That does not establish R7's hypothesis fails**, for a reason named before the run: my `μ` comes from a greedy that minimises `d_cb` *first* and `μ` only as a tiebreak, so it is an **upper bound on the `μ` of a `d_cb`-optimal certificate** — while R7 concerns the certificate one would actually choose, which may accept a larger `d_cb` to buy a smaller `μ`. Upper bounds make `μ ≤ L` safe and `μ > L` worthless, which is the direction every one of those 117 rows points.

The data shows the ambiguity plainly: the threshold object at `L = 0.83007` yields `μ = 1` under some rootings and `μ = 0` under others of the same size. So zero unpaid boundary rank is achievable there, and a `μ`-minimising search would find it.

**Status: inconclusive, and the fix is specified.** A real test needs `μ` minimised directly — exactly, not greedily, and not subordinate to `d_cb`. That is the next concrete computation, and it targets a hypothesis the campaign itself nominated as cheapest.

## 12. The exact μ measurement: μ_min = 0 almost everywhere (added ~11:1x)

§11 specified the fix — minimise `μ` **directly and exactly**, not subordinate to `d_cb`. Done, over every full-rank dual basis and every signed-selector assignment, by DFS with a bound on `μ`. This verdict is safe in both directions because `μ_min` is exact.

**Result: `μ_min = 0` on every configuration tested except three.** Books `p = 2,3,4` under every rooting; the star; the wheel `k=4` under every rooting; the wheel `k=3` under all single-coordinate rootings. The exceptions are wheel `k=3` with `|W| = 2` (rootings `(0,1)`, `(0,2)`, `(0,3)`), where `μ_min = 1` against `L = 0.811` — the only place absorption is genuinely needed, and only just.

> **[FRAMING CORRECTED IN §14 — read that with this section.]** Calling the wheel case an awkward "exception" was wrong. `μ = 0` and absorbability are *opposite* conditions (residuals purely private vs purely boundary), so they are two complementary routes; the wheel `|W|=2` rootings are simply covered by the absorption route rather than the `μ` route, and nothing is amiss there. The genuinely unique configuration — where **neither** route applies — is the threshold object rooted at one whole triple, and that is exactly where `L = β` and the constant is tight.

`μ_min = 0` means there is a certificate whose residuals have **no boundary component at all** — every residual is purely private. That is far stronger than the `μ = O(L)` the rank lane hoped for, and where it holds, R7 alone delivers the rooted estimate **with no absorption hypothesis whatsoever**.

**An independent corroboration worth more than the individual results.** The book rooted at its shared pair — the configuration whose naive ratio `d_cb/L = 3.0` looked like a violation in §1 — has `μ_min = 0`. So R7 disposes of it with no absorption needed, reaching the same "harmless" verdict as the absorbability argument by a completely different route: one argues `R ⊆ span W` so the quotient vanishes, the other that a certificate exists with no boundary component at all. **These are different frames that could have disagreed, so their agreement is corroboration rather than the same anchor measured twice.**

**What this does and does not say.** It says the machinery is far less dependent on absorption than the packet's framing suggests: on everything computable here, the cheapest hypothesis the rank lane nominated does not merely hold, it holds at zero. It does **not** say anything about the residual class — the campaign still possesses no explicit class member, so this is evidence about the *machinery*, measured on known non-members. The honest reading is that absorption is not the binding constraint on these objects, and the wheel `k=3` exception is the one place to look for why it ever would be.

## 13. Claim Q is the dossier's own 3/4 bound — I rediscovered it (added ~11:3x, corrected on searching properly)

§8 verified Claim Q exhaustively at `n = 3, 4`, and I then derived it from Erdős's Littlewood–Offord bound, believing the derivation was the new part. **It is not. The dossier proves this exact bound in its §3.1, tag (13), by exactly the argument below.** My first search for it failed — I grepped for `psi` and `3/4` in plain text while the document is LaTeX (`\psi`, `\frac34`) — and a second search with different phrasing found it immediately. Recording that, because a failed search is a fact about the search.

So the proof below is an independent **rediscovery**, which validates the reasoning and nothing more. What is genuinely new is §13.5: that this same `3/4` is the *absorption threshold*.

**Claim Q.** For a linear form `f` on `{±1}ⁿ` that is not `±eᵢ`, `Pr[f·x ∈ {±1}] ≤ 3/4`.

*Proof.* Let `s` be the size of `f`'s support; all coefficients on it are nonzero.

- `s = 1`: `f = f₁e₁`, and `f·x = f₁x₁ ∈ {±1}` requires `|f₁| = 1`, i.e. `f = ±e₁`, excluded. Probability 0.
- `s = 2`: the four values are `±(f₁+f₂)` and `±(f₁−f₂)`. Both pairs lie in `{±1}` only if `(f₁+f₂)² = (f₁−f₂)²`, i.e. `f₁f₂ = 0` — a coordinate, excluded. So at most one pair qualifies: probability `≤ 1/2`.
- `s ≥ 3`: by Erdős's theorem, `sup_t Pr[f·x = t] ≤ C(s,⌊s/2⌋)/2ˢ`. Taking the union over the two values `t = ±1`,
    `Pr[f·x ∈ {±1}] ≤ 2·C(s,⌊s/2⌋)/2ˢ = 2^{1−s}C(s,⌊s/2⌋)`,
  which equals `3/4` at `s = 3` and `s = 4`, and then decreases: `5/8, 5/8, 35/64, …` ∎

**The equality cases are exactly the objects that attain `β`.** The bound is met at `s = 3` and `s = 4` and nowhere else — and the constraint types measured at defect exactly `β` in §7 were NAE3 (the homogenizer `e₁+e₂+e₃`, support 3) and `n4k2` / `n5k4` (support 4). The extremal forms and the extremal fibres are the same objects, which is why the quarter is attained rather than merely approached.

**Where this already lives in the dossier.** `ψ(u) = min{3/4, 2^{1−u}C(u,⌊u/2⌋)}` appears at line 1944 of the extraction; the `3/4` half is §3.1 tag (13) — proved there by the same two-active-coordinates argument, noted as target-uniform and valid in every odd characteristic — and the binomial half is §3.2 tag (14), classical Littlewood–Offord. The `min` does exactly the job of my `s = 1, 2` cases, where the raw binomial expression exceeds `3/4`. My derivation reproduces the dossier's, independently; it does not extend it.

## 13.5 What is actually new: `β` is the minimum cost in the dossier's own bookkeeping

The dossier sets `c_s = −log₂ ψ(a_s+1)` (tags (15), (24a)) and uses `ψ` for entropy/congestion accounting. It does **not**, anywhere I have found, connect `ψ`'s cap to absorption. That connection is this session's:

> `max ψ = 3/4` is the largest fraction of the cube on which a non-coordinate dual form can be `±1`-valued. A private constraint must push its allowed set **below** that before an extra dual form — and hence any obstruction at all — can exist. So the absorption threshold is `−log₂(max ψ) = log₂(4/3) = β`, and the rooted target's constant is `1/β`.

Read in the dossier's own units this says something sharper: since `c_s = −log₂ψ(a_s+1)`, **`β = min_s c_s`** — the smallest per-batch cost the dossier's congestion bookkeeping can ever charge. The rooted constant `1/β` is therefore the reciprocal of the minimum congestion cost, which is why the same number keeps surfacing in both the entropy lane and the rigidity lane. Two lanes, one constant, and now one reason.

That completes the analytic account of the constant:

> `1/β` is `1/(−log₂ max ψ)`. The rooted target's constant is the reciprocal log of the campaign's own anticoncentration cap, because `max ψ = 3/4` is the largest fraction of the cube on which a non-coordinate dual form can be `±1`-valued — and a private constraint must push the allowed set below that before an extra dual form, and hence any obstruction, can exist at all.

**Status.** Claim Q is now **proved**, not merely exhaustively checked, and it rests on Erdős — the same classical input the campaign already uses for `ℓ ≥ 1` and the spectral gap. What remains empirical is the bridge of §§9–10 (extra form ⟹ absorption fails), which two attempts failed to close and which §12's `μ` measurement suggests may be the wrong thing to want: on everything computable, `μ_min = 0` and absorption is not binding at all.

## 14. Two complementary routes, and the single configuration where neither applies (added ~12:3x)

Reading the wheel's dual directly — rather than only measuring it — corrected a framing error in §12 and produced the sharpest statement this session has.

**`μ = 0` and absorbability are opposite conditions, not the same one.** Absorbable means `R ⊆ span W`: the residuals *are* their boundary parts, so `μ = dim R > 0`. `μ = 0` means the residuals have no boundary part at all, i.e. `R ⊆ span Q`. So there are two routes, and they trivialise the target from opposite ends:

- **Route A (`μ_min = 0`)** — residuals purely **private**. R7's `dim ≤ 2ν + L + μ` then gives the estimate with **no absorption hypothesis**.
- **Route B (absorbable)** — residuals purely **boundary**. Clause (ii) then gives left side **0** outright.

> **[PRECISION FIX, from `candidate_class_shape.md` §6.]** Calling both routes "trivialising" overstates route A. Route B genuinely forces the left side to 0; route A only removes the *absorption requirement* and leaves R7's bound `2ν + L + μ` still to be checked. Measured instance: the candidate object at `W = (0,)` has `μ_min = 0` and `R_< = 0`, and its quotient is **2, not 0**. So "covered" throughout §§14–16 means **handled without absorption**, not automatically satisfied. The classifications are unaffected — they record which mechanism applies — but nothing should be built on reading route A as triviality.

§12 called the wheel `k=3` at `|W|=2` "the only place absorption is genuinely needed" and framed it as an awkward exception. That was wrong: it is simply a configuration where route B does the work and route A does not. Nothing is amiss there.

**The real finding is the coverage pattern.** Computing exact `μ_min` and absorbability at *every* rooting of both objects:

- **Wheel `k=3`:** all 14 rootings covered. Single coordinates and rim pairs go by route A (`μ_min = 0`); hub-plus-rim and the triples go by route B.
- **Threshold object:** all 62 rootings covered — **except exactly one.**

> **`W = (0,1,4)` — the defining rooting, `W` equal to one whole NAE triple — is the unique configuration where `μ_min = 1` and the fibre is non-absorbable, so *neither route applies*.**

> **[CORRECTED IN §15 — do not read this section without it.]** "Unique" was an artifact of testing two objects. A sweep over 11,765 configurations finds **136** covered by neither route, not one. What survives, and is stronger: **none of them has `L < β`**, and the minimum `L` over all uncovered configurations is exactly `β`.

And that is precisely where `L = β` exactly, and where §6 showed the left side is `1` against a budget of `(1/β)·β = 1.000000` — equality, zero margin.

**What this reframes.** The rooted target's two clauses are not two independent requirements to be established separately. They are **two trivialising routes**, and everything computable falls to one or the other — except at a single configuration, which is exactly the object that fixes the constant. So `1/β` is not a constant chosen to cover a family of hard cases; it is the constant required by **the one configuration where both easy routes close simultaneously**.

That also explains, in retrospect, why the bridge of §§9–10 resisted two attempts. I was trying to prove "extra form ⟹ absorption fails" as though absorption were the only mechanism in play. It is not: on most configurations absorption is not needed at all, because route A already applies. The right question was never "when does absorption fail" but **"when do both routes fail at once"** — and the answer, on everything computed, is: at one object, at `L = β`.

**Caveats unchanged.** Two objects, NAE-triple fibres, small `r`; the `R_< ⊆ span W` step remains a reconstruction; and every object is a known non-member of the residual class.

## 15. §14's coverage claim was over-specific — the corrected version is stronger (added ~13:2x)

§14 concluded, from **two objects**, that every configuration falls to route A or route B "except exactly one". That is wrong, and testing it was the point: a claim that strong resting on two objects is a claim waiting to break.

**Swept over 11,765 configurations** — books, stars, wheels, the pair objects, and exhaustive NAE-triple sets at `r = 4, 5` — every rooting of each, with exact absorbability and an exact test for `μ_min = 0`:

- **136 configurations are covered by neither route**, not one.
- **Zero of them have `L < β`.**
- The uncovered `L` values are exactly three: `β = 0.41504` (4 configurations), `0.90532` (12), `1.33333` (120).

So the "single configuration" claim dies and a better one replaces it:

> **The two trivialising routes cover every configuration with `L < β`. Where neither route applies, `L ≥ β` always — and the minimum over all such configurations is exactly `β`, attained at the two-disjoint-NAE-triples objects.**

This is the same conclusion the session has been circling, now stated where it is actually true and supported by 11,765 configurations rather than 2. It also sits exactly on top of Claim B (§2): everything below `β` absorbs, so nothing below `β` can be uncovered — and the sweep confirms that independently, by a different computation, over a different family set.

**Why the over-claim happened, since it is the same shape as three earlier ones tonight.** Two objects agreed, the agreement was striking, and I wrote the striking version rather than the supported one. The fix each time has been the same: run it on more things before believing the shape. Here it cost one sweep and bought a stronger theorem — the minimum of `L` over uncovered configurations being *exactly* `β` is a sharper statement than "one object is special", and it is the direct form of "β is the threshold".

**Caveats.** NAE-triple fibres, `r ≤ 6`; exhaustive only at `r = 4,5` and for triple-sets of size ≤ 4 at `r = 5`; and every object remains a known non-member of the residual class.

## 16. The uncovered set has TWO mechanisms, and only one sets the constant (added ~14:0x)

The uncovered configurations — where neither trivialising route applies, and therefore the only place the rooted target has content — are worth characterising rather than just counting. Of the 136 found across 11,765, their `L` values take exactly three values, and the three groups are structurally different:

| `L` | count | shape | triples wholly inside `Q` |
|---|---|---|---|
| **`β` = 0.41504** | 4 | `r=6`, 2 triples, `|W|=3` | **1** (4 of 4 configurations) |
| 0.90532 | 12 | `r=6`, 4 triples (book `p=4`), `|W|=3` | **0** (0 of 12) |
| 1.33333 | 120 | `r=5`, 4 triples, `|W|=2,3` | **0** (0 of 120) |

**So there are two distinct ways to be uncovered.**

- **Mechanism A** — a constraint lies **wholly inside the private part**. This is the mechanism §§3, 7 and 8 characterise: the private constraint the boundary cannot see, forbidding a quarter, contributing an extra dual form. It occurs at `L = β` exactly.
- **Mechanism B** — **no** constraint is wholly private; every one straddles `W`. Yet the configuration is still uncovered. This is 132 of the 136, and **my mechanism story does not explain it at all.**

> **[SUPERSEDED — see `the_obstruction_is_four_classes_on_rank_three.md`.]** A and B are the **same** mechanism. The minimal Rado violation in both is **four π-classes spanning rank three**; the difference is only whether the four forms are all private (A) or include two straddling forms that share a boundary part, so their difference is purely private and already spanned (B). Mechanism B is a dual restatement of the campaign's own "boundary parts constant on private-sharing clusters" condition.

**Why the constant survives anyway.** Mechanism B's configurations sit at `L = 0.905` and `L = 1.333`, both well above `β`. They have more budget, not less, so they never bind. The minimum over the uncovered set remains exactly `β`, attained only by mechanism A. **The constant is set by mechanism A alone**, which is why §§7–8 could explain it correctly while describing only a quarter of the phenomenon.

That is a real limit on the explanation, stated plainly: the account of *why the constant is `1/β`* stands, and the account of *when the target has content* does not — mechanism B is uncharacterised.

**A concrete lead on the campaign's standing gap.** The campaign has never constructed an explicit member of the residual class, and the class is *dense* and connector-incoherent. Mechanism B's largest group is the densest thing this sweep produced: `r = 5` with **4** NAE triples, `|A| = 12`, `|D| = 12` — a dual twice the ambient dimension. Those objects are uncovered, dense, and small enough to compute on exhaustively. **If a class member is to be constructed, this is the shape to try**, and it is reachable in a way nothing else the campaign has looked at has been.

**Caveats.** `r ≤ 6`, NAE-triple fibres, and exhaustive only at `r = 4,5` with triple-sets of size ≤ 4 at `r=5` — so mechanism B's three observed `L` values are three values *in this range*, not a classification. And every object remains a known non-member.
