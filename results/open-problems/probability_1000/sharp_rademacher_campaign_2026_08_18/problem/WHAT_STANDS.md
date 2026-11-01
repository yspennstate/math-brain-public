# What stands: the campaign's beliefs, separated by how they were earned

Assembled 2026-08-19 (late) by reading every file in `problem/`, plus `STATE.md`, `LOG.md`,
`STATE_OF_THE_PROOF.md`, `ITERATION2_SYNTHESIS.md` and the `mathbrain/` campaign layer. It is a
status document, not a result: nothing new is derived here. Where I add something of my own —
a recount, a status correction, a contradiction — it is marked as mine.

**The sharp Rademacher singularity conjecture, `Pr(det B_n = 0) = (1+o(1))·2n²·2⁻ⁿ`, is OPEN.**
Nothing in this campaign bears on it directly. Every object studied here is a known non-member of
the residual class, and the class itself has never had a member displayed — not here, and not in
the 200-page dossier.

The campaign refuted five of its own closed-form formulas, two of its own lemmas, three readings of
the rooted data, and a note it had to withdraw in full. That rate of self-refutation is the reason
this document exists: the files are chronological, most corrections live at the bottom of the file
they correct, and several sections still read as live when the section below them has killed them.

---

## 0. What the quantities are

| symbol | meaning |
|---|---|
| `A` | the sign fibre: vectors in `{±1}^r` satisfying every constraint (for triangle systems: no monochromatic triple) |
| `D(A)` | the full dual: every linear form that is `±1`-valued on all of `A` |
| `d_cb` | selector distance: choose a coordinate basis `G ⊆ D` and a signed selector for every leftover form, with all residuals in one space `R`; minimise `dim R` over basis and selectors |
| `ℓ` | unrooted defect `r − log₂\|A\|` |
| `L_{Q\|W}` | rooted (conditional) defect `q − H(Q\|W)` |
| `β` | `log₂(4/3) = 0.415037`; `1/β = 2.409420` |
| tightness | `d_cb·β/ℓ`, i.e. `d_cb/(ℓ/β)` — Conjecture RC says this is `≤ 1` |
| linear triangle system | `k` triples on `r` coordinates, no two sharing **two** coordinates |
| excess | `\|D\| − (number of ±-classes after collapsing by R)` |
| hub / `h` | a coordinate in two or more triangles; `h` counts them |
| `μ` | unpaid boundary rank; `λ` | leak `dim B̄(ker P)` |

Trees have `r = 2k+1`, tri-cycles `r = 2k`, disjoint unions `r = 3k`. Wheels, books and fans are
**not** linear — adjacent triangles there share an edge. The dossier's rooted NAE cycle is the
wheel; its rooted NAE path is the fan.

---

## 1. PROVED — unconditional, with a written argument

| # | claim | argument | where |
|---|---|---|---|
| P1 | `d_cb(k-arm NAE star) = k − 1` for every `k ≥ 2` (and 1 at `k = 1`) | construction (§2) for `≤`; leftover-structure + derangement + raw-part parallelism for `≥` (Steps 1–4) | `star_family_proved.md` §§2, 6 |
| P2 | `d_cb(m disjoint NAE triples) = m`, `ℓ = mβ`, tightness exactly 1 | basis must take 3 forms per block, leaving one leftover each; no dependency exists (fixed-point-free selector argument) | `the_constant_is_attained.md` §3 |
| P3 | `1/β` is exactly optimal for the **unrooted** bridge `d_cb ≤ C·ℓ`: it cannot be lowered and it is attained with equality along an infinite family | P2 gives equality at every `m`; P1 gives `sup_k (k−1)/(kβ) = 1/β` approached but not attained | `the_constant_is_attained.md` §4, `star_family_proved.md` §6 |
| P4 | `ℓ` and `d_cb` add over coordinate-disjoint blocks; tightness is the `ℓ`-weighted average of component tightnesses | dual of a product is a disjoint union, so per-block certificates combine and residuals on disjoint coordinates cannot cancel | `gluing_is_a_cliff.md` §7 (predicted six values to four decimals before measuring), `the_constant_is_attained.md` §2 |
| P5 | For every triangle-tree, `ℓ = kβ` exactly, independent of topology | `r = 2k+1`, `\|A\| = 6·3^{k−1}` whatever the shape | `concentrated_sharing.md` §5; measured 3.000/4.000/5.000/6.000 |
| P6 | `ker Φ = span{ρ_t}`, dimension exactly `k` | `D` contains every coordinate form so `rank D = r`; `\|D\| = r+k`; the `k` relations `ρ_t` are independent because each carries its own `δ_{f_t}` | `why_ceil_k_over_two.md` §9 |
| P7 | The transversal/Rado condition **is** a blocking condition: a transversal is independent iff the only `c` supported on the chosen triangles with `Σ_{t∋j} c_t = 0` at every missed coordinate is `c = 0` | immediate from P6 | `why_ceil_k_over_two.md` §14 |
| P8 | `E_c ≤ d` (coordinate merges) | signed incidence vectors of a forest are linearly independent | `why_ceil_k_over_two.md` §5 |
| P9 | For a **linear** system, a one-dimensional `R` produces at most **two** merges, with equality exactly when `v = e_x + e_y` for a pair inside a triangle | four-case argument on support and sign pattern | `why_ceil_k_over_two.md` §17 |
| P10 | Linearity is the right hypothesis, and P9 shows why: every failing case runs through `f_t − f_s` collapsing to support 2, which happens exactly when two triangles share an edge | same argument | `why_ceil_k_over_two.md` §17 |
| P11 | Claim Q: the largest level set of a non-coordinate linear form on `{±1}^n` is exactly `(3/4)·2^n` | `s ≤ 2` by hand, `s ≥ 3` by Erdős Littlewood–Offord. **This is the dossier's own §3.1 tag (13)** — the campaign rediscovered it | `beta_is_the_absorption_threshold.md` §13 |
| P12 | Every **minimal** Rado violation has deficiency exactly 1 | drop one class from a deeper violation and it still violates | `the_obstruction_is_four_classes_on_rank_three.md` §6 |
| P13 | ABSORBABLE ⟺ some basis `G ⊆ D` meets every `±`-class of `π(D)`, where `π` restricts outside `W` | `f − σg ∈ span W ⟺ π(f) = σπ(g)` | `beta_is_the_absorption_threshold.md` §1 |
| P14 | Absorbable ⟹ the rooted target's left side is **0** | clause (ii) plus `R ⊆ span W` | same, §1 |
| P15 | `R ∩ span W = 0` ⟺ the chosen vectors stay independent after deleting the window coordinates; and `rooted d ≤ r − \|W\|` | a combination lies in `span W` iff it vanishes off `W` | `rooted_target_in_the_pairsum_frame.md` |
| P16 | The Fano plane has `\|A\| = 0` — it is not 2-colourable, so its fibre is empty and `d_cb` is undefined on it | classical | `why_ceil_k_over_two.md` §22 |
| P17 | R1 splitting: `dim((R+R_<)/R_<) = dim((R+B)/B) + λ`; R2: `λ = dim B̄(ker P)`; R7: `dim((R+R_<)/R_<) ≤ 2ν + L + μ` with **no** absorption hypothesis | Dedekind modular law; rank–nullity | `attacks/attack_rank.md`; ledger 20/21/28 — **PROVED but UNREFEREED** |
| P18 | Clause tension: compressing private rank to `d` over `k` rows forces `k−d` dependencies, and `λ` is exactly their boundary image, so clause (i) manufactures what clause (ii) must kill | rank–nullity on R2 | `the_two_clauses_are_in_tension.md` §1 (rests on the unrefereed R2) |

**One caveat on P6 that the campaign states but does not repeat often enough.** `ker Φ = span{ρ_t}`
uses `\|D\| = r + k`. The "these forms are all dual" half is proved; the "there are no others" half is
**verified, not proved** — on trees at `k = 2,3,4,6`, disjoint `m = 1,2,3`, tri-cycles `k = 3,4,5`. **And now known false in general (§32):** the bipartite construction gives linear systems with extra dual forms, so the "no others" half holds on the objects listed and not beyond them.
The store's own object says so (`explicit_dual_of_linear_system`, status `audited-pass`, notes: "The
'no extras' half is the part carried by verification rather than proof"). So P6, and therefore P7,
are proved **modulo** an exhaustively-checked but unproved dual description. That dependency should
travel with them.

---

## 2. MEASURED EXHAUSTIVELY — finite certificates, exact rational arithmetic

These are true statements about the range enumerated. They are not theorems about the families.

| # | measurement | range | where |
|---|---|---|---|
| M1 | `excess ≤ 2d` holds, and is **tight** (max exactly `2d`) | `d = 1,2,3` on 8 triangle-trees, up to 40,629 subspaces each | `why_ceil_k_over_two.md` §4 |
| M2 | `rank(pass-1 edge vectors) = E_c`, `rank(pass-2) = E_t`; every triangle form touches at most one coordinate class | 7 trees, `d ≤ 3` | §7 |
| M3 | The rank-`k` system that would close `E_t ≤ d` holds in the range the theorem needs (`d ≤ ⌈k/2⌉−1`, `k = 2..6`, ~200,000 subspaces) and **fails at `d = 3, k = 3`** (144 cases, rank drops to `k−1`) | as stated | §11 |
| M4 | The excess-2 directions are exactly the `3k` pair-sums, zero extras | 9 objects | §15 (proved at `d=1` by P9) |
| M5 | ~~`\|D\| = r + k` on every object measured except wheel `k=3`~~ **REFUTED (§32).** The dual exceeds `r + k` on a whole family of *linear* systems, because a linear system can imply not-all-equal constraints on triples outside itself and each contributes a form. Smallest witness: the **Pasch configuration** `{024, 035, 125, 134}`, `\|D\| = 14` against `r+k = 10`. `full_dual` reproduces `r+k` on star, chain, tri-cycle and disjoint controls, so the enlarged duals are not a broken detector | linear and non-linear objects both | §16, refuted §32 |
| M6 | Blocking (P7) agrees with the rank/DFS `valid_R` implementation, zero disagreements | ~29,000 subspaces of dim ≤ 2, 8 objects | §14 |
| M7 | `rank ≤ h + d`: no subspace reaches more than `d` distinct triangles' unit constraints | ~600,000 subspaces at `d ≤ 3`, six objects | `hub_count_formula.md` |
| M8 | Claim B: `L_{Q\|W} < β` ⟹ absorbable, zero counterexamples | `r=4` 192 configs (42 sub-β), `r=5` 16,222 (832), `r=6` 393,212 (17,587); controls fire both ways | `beta_is_the_absorption_threshold.md` §2 |
| M9 | The quarter law: absorption fails exactly when a private constraint forbids ≥ 1/4 of its patterns. Perfect separation at `β` | 12 constraint types, `n = 3,4,5`; the decisive `n5k3` (defect 0.2996) predicted absorbable **in advance** and confirmed; parity4 breaks 59,312 times at the same `r=8`, so the detector was alive | §7 |
| M10 | Claim Q verified exhaustively before it was proved: extras first appear at exactly 3/4 and never above (the `n=4, \|S\|=14` row at 7/8 gives zero extras across all 8 spanning subsets) | `n = 3, 4` | §8 |
| M11 | `μ_min = 0` on **every** configuration tested except wheel `k=3` at `\|W\|=2` (`μ_min = 1` against `L = 0.811`) | exact minimisation over every full-rank dual basis and every signed-selector assignment | §12 |
| M12 | Coverage: 136 of 11,765 configurations are covered by neither trivialising route; **zero** of them have `L < β`; the uncovered `L` values are exactly `{β, 0.90532, 1.33333}` | books, stars, wheels, pair objects, exhaustive NAE-triple sets at `r=4,5` | §15 |
| M13 | The `r=5` candidate object is **unique up to relabelling**: 60 of 210 four-triple sets on 5 coordinates have an uncovered rooting, all isomorphic to `{(0,1,2),(0,1,3),(0,2,3),(1,2,4)}`; and the selection is real (`ℓ` takes two values in the population, uncoveredness picks only `1.41504`) | as stated | `candidate_class_shape.md` §§1, 5 |
| M14 | The candidate satisfies the rooted target at all 27 rootings; exact `d_cb = 2` over 6,000 optimal residual spaces; quotient 2 against budget 3.2126 at both uncovered rootings | as stated | §6 |
| M15 | The threshold object (two disjoint triples, `W` = one of them) has `d_cb = 2`, 2,304 optimal residual spaces, quotient values `{1,2}`, minimum **1** against budget `(1/β)·β = 1.000000` — equality, zero margin | as stated | `beta_is_the_absorption_threshold.md` §6 |
| M16 | Star certificates at `k = 2,3`: over **every** basis and **every** selector assignment (900/600 and 74,088/74,088), zero dependencies with the hub in the basis, min rank `k−1` with the hub as leftover | as stated | `star_family_proved.md` §5.2 |
| M17 | Rooted windows: across ~5,000 windows exhaustively enumerated by size, exactly **two** raise the dimension — fan `k=3` at `W = {0,2,3}` and chain `k=6` at `W = {4,5,6,7,8}` | objects to `r = 13`, `\|W\| ≤ 7` | `rooted_target_in_the_pairsum_frame.md` |
| M18 | Blocking windows are genuine, not a pair-sum artefact: re-run over every line of the dual, the full search finds nothing where the restricted one found nothing and reproduces every value where it did | 2 blocking windows + 1 raising + 5 controls | same file |
| M19 | Tri-cycle `k=6` blocks at `\|W\| = 7` (6 windows of 792) and not below; `r − \|W\| = 5 > 3`, so these are structural blocks, not the arithmetic ceiling | 3,223 windows | same file |
| M20 | Minimal Rado violation **size** is 4-on-rank-3 in 17 of 18 uncovered configurations; one gives 6-on-rank-5 | as stated | `the_obstruction_is_four_classes_on_rank_three.md` §6 |
| M21 | 32 random **connected** linear systems at `k = 3,4,5` and 24 random systems from a disconnection-capable generator (of which only **2** discriminated) | as stated | `hub_count_formula.md` |

---

## 3. MEASURED PARTIALLY — real numbers, but the reading is not established

- **The dossier agreements.** Wheels `n = 3,4,5,6` measured here at 1, 2, 2, 2 match the dossier's
  proved `⌈n/3⌉` (tag 35); fans `k = 3,4,5` at 1, 2, 2 match `⌈(N−1)/3⌉` (tag 38f); rooted fans at
  1, 2, 2 match the rooted path theorem (tag 38g). STATE.md calls this ten agreements. *Mine:* the
  dossier states its cycle theorem for `n ≥ 4`, and `why_ceil_k_over_two.md` §16 says so explicitly,
  so the wheel `n=3` row is agreement with an extrapolation rather than with the theorem. Nine, not
  ten, if counted strictly. This does not weaken the validation — nine independent agreements
  against two externally proved theorems is the strongest external check the campaign has — but the
  count should be stated correctly.
- **Tightness rises with constraint count on the star family**, exact at `k ≤ 4` and now proved for
  all `k` by P1: `(k−1)/k` = 0.500, 0.667, 0.750, 0.800 → 1. The family is not monotone: `k=1` is
  exactly tight at 1, `k=2` dips to 0.5, then it climbs (`candidate_class_shape.md` §12).
  Whether tightness rises with constraints **in general** is open; two confident answers were
  published and both were withdrawn (§5 below).
- **The crosspolytope at `r = 4`** is easy at every rooting: coefficient 1.0, leak 0, `μ = O(L)`.
  The `r = 8` run was killed at the committed hour mark with no row, so the `r = 4` reading stands
  **unpromoted** (`embedded_crosspolytope_rooted.md`; STATE.md ~line 434). And the embedding had to
  be invented — the dossier never specifies which coordinates are boundary.
- **`d_cb ≤ k` for every linear triangle system**, by a construction with no search: take one
  pair-sum per triangle, missing `f_t`, which supplies the unit `e_t`; the `k` units span `Q^k`.
  Verified independent **and** `valid_R` on 35 objects (13 handpicked, 22 random from a generator
  that emits disconnected systems too; the natural choice never needed the greedy fallback). Not
  proved: the general statement needs a choice of pairs whose incidence graph has no even cycle. On
  a **tree** the note observes that the natural choice gives pairwise disjoint edges, hence a
  forest for free, so the independence half is argued there — but the note still labels the whole
  construction verified rather than proved, and that label is the one to carry.
  **Partly closed 2026-08-20 (§39).** The independence requirement is a transversal problem, so
  **Rado** applies: an independent one-pair-per-triangle choice exists iff every subfamily of `s`
  triangles touches at least `s` coordinates. The rank of a union of triangles equals the number
  of coordinates touched (every component carries a 3-cycle, so no component is bipartite;
  checked on 220 subfamilies, zero mismatches). Linearity then forces the condition for `s ≤ 8`,
  since `3s ≤ C(V',2)` with `V' ≤ s−1` needs `s ≥ 9`. **So `d_cb ≤ k` is PROVED for every linear
  system with `k ≤ 8`**, and reduced to that Hall condition in general. The condition is exactly
  right and does fail: `K_{3,4}` and `K_{4,4}` violate it and admit no such choice (10 of 10
  agreement with direct search). Where it fails the bound may still hold by `d_cb ≤ r` or by
  additivity, so the general statement is not yet proved.
- **Consequence for RC.** With `ℓ = kβ` (P5), `d_cb ≤ k` gives tightness `≤ 1` for the whole
  triangle-tree family, and P2 gives it with equality for disjoint unions. STATE.md's "RC now holds
  on three families" is right for cycles (the dossier's tag 38d, proved there) and disjoint unions
  (P2, proved here); *mine:* for **trees** it rests on the unproved construction above, so that leg
  is conditional and should be labelled so.
- **Off the tree/disjoint families `ℓ ≠ kβ` and the argument dies.** Tri-cycle `k=4` has
  `ℓ/β = 3.957`, so `d_cb ≤ k` permits tightness 1.0108 and proves nothing. The measured value is
  fine (0.5054) but that is a measurement.

---

## 4. CONJECTURED — believed, unproved, and in two cases without any derivation left

| # | conjecture | evidence | what is missing |
|---|---|---|---|
| C1 | **Conjecture RC**: `d_cb ≤ ℓ/β`, equivalently `\|A\| ≤ 2^r(3/4)^{d_cb}` | unrefuted on everything measured; followed along six parametric families rather than filling a window; proved with equality on disjoint unions; proved by the dossier for cycles | the general statement; and the tree leg rests on `d_cb ≤ k` |
| C2 | ~~`d_cb ≥ ⌈k/2⌉` for every linear triangle system~~ **REFUTED (§32)** | held on every object measured in §§1-31, and attained by every non-star tree at `k = 4,5,6` and by tri-cycles `k = 3..7` — those measurements stand | **counterexample**: the `K_{4,4}` member of the bipartite construction is linear with a spanning fibre, `k = 16`, `r = 12`, and a valid `R` of dimension **7** against `⌈k/2⌉ = 8`. The derivation was already gone (`excess ≤ 2d` false, R5; `excess ≤ 2d+1` false, R6); now the statement is too. It survives only under the extra hypothesis `\|D\| = r + k`, which linearity does not imply |
| C3 | **The linked-pair characterisation**: `d_cb` is the least `d` such that `d` linked pairs `(1_{S_j}, e_t)`, `j ∈ t`, span `Q^k` | 34 of 34 objects, 5 advance predictions and 5 hits; makes the discrimination no `(k,h)` formula can — `(3,1,1)` and `(2,2,1)` share `k` and `h` and come out 4 and 3 | the lower direction rested on `excess ≤ 2d`, now false in general; the upper direction (a spanning selection is always realisable as a subspace) has no argument |
| C4 | `excess = 2d + c`, `c` the cycle rank of the merge-carrying pair-sum lines in `R` | fits both counterexamples exactly (7 at `c=1`, 14 at `c=2`), predicted additively in advance | *mine:* it is derived only for `R` **spanned by pair-sum lines**. A general `R` may contain non-pair-sum directions of excess 1, so this is not yet an upper bound on excess for arbitrary `R` of dimension `d`, and no such bound is currently held |
| C5 | The counting bound is not damaged unboundedly, because dense linear systems have empty fibres | the Fano plane has `\|A\| = 0` (P16); density and 2-colourability pull against each other | the relationship is not worked out; partial Steiner systems sparser than Fano may have both properties |
| C6 | "Extra dual form ⟹ absorption fails" | holds on all eight product objects | **empirical.** Two attempts failed in opposite directions: Criterion C too strict (3,867 mismatches of 11,780), Claim R′ too permissive (111 of 492). The truth lies strictly between a cardinality count and a support condition |
| C7 | The quarter law (M9) | perfect separation, registered prediction hit | not proved |
| C8 | G2 ⟺ no full-dual form spans incomparable blocks; and this is what "admissible" must mean | holds on every computed object, with a disjoint failure mode from the defect failure | labelled RECONSTRUCTED, PLAUSIBLE — the defining tree is not on this machine |
| C9 | Whether the fibre defect `ℓ` and the single-dependency defect `ℓ = −log₂Pr[c·x=0]` are the same quantity | the candidate object's `ℓ = 1.41504` lands exactly on the campaign's spectral gap, and the selection behind that is real | unresolved, and it is definitional. `candidate_class_shape.md` §5 calls it the most valuable question the object raises |
| C10 | What distinguishes a dimension-raising window | both known raisers are unions of whole triangles | **not sufficient** — chain `k=4`'s whole-triangle window does not raise. Four mechanism guesses have died; no fifth is offered |
| C11 | Route E: the residual class may be empty | every obstruction object the campaign holds dissolves under a better decomposition; no member is displayed anywhere in 200 pages | if emptiness were easy the packet's authors would likely have said so |

---

## 5. REFUTED — by the campaign, with the witness that did it

### Its own closed forms

| # | dead claim | killed by | where |
|---|---|---|---|
| R1 | `d_cb = max(2, largest attachment group)` | chain `k=5` = 3 (profile `(1,1,1,1)`, group 1, formula says 2) | `concentrated_sharing.md` §7 |
| R2 | `d_cb = max(largest attachment group, ⌈k/2⌉)` | `(3,2)` at `k=6` = 4 against a **registered** prediction of 3 (2871s exhausting `d=3`). Eleven exact values and nine straight predictive hits did not save it | `concentrated_sharing.md` §8 |
| R3 | `d_cb = max(⌈k/2⌉, k−h)` **globally** | the proved additivity lemma: chain3 ⊔ chain3 is `2+2 = 4`, the global expression says 3. Every pair of odd chains breaks it | `hub_count_formula.md` |
| R4 | the same formula **per connected component** (the "connected conjecture") | `(3,1,1)` at `k=6` = 4 against 3 — by hand first, then by exhaustive search (5289s), then confirmed by a `d≤3` exhaustion (2962s) | `hub_count_formula.md` |
| R5 | `excess ≤ 2d` for linear systems | tri-cycle `k=4`, `R = span{e₀+e₂, e₂+e₄, e₄+e₆}`, `dim 3`, **excess 7**. Tri-cycle `k=6` reaches 11 at `d=5`. These are linear systems, so linearity is not sufficient | `why_ceil_k_over_two.md` §19 |
| R6 | `excess ≤ 2d+1` (the repair) | two disjoint tri-cycle `k=4` blocks, `dim 6`, **excess 14**, predicted additively in advance. The repair lasted one experiment | §21 |

### Its own readings of the rooted data

| # | dead claim | killed by | where |
|---|---|---|---|
| R7 | "Rooting is free or fatal, almost never expensive" | chain `k=6` at `\|W\|=5`: worst rooted 4 against unrooted 3 | `rooted_target_in_the_pairsum_frame.md` |
| R8 | "Tri-cycles never block" | tri-cycle `k=6` blocks at `\|W\| = 7`; the earlier sweep stopped at 5 | same |
| R9 | "The raising window is the hub set" | the hub set is free on chains `k = 4, 5, 6`, including the chain that does have a raiser at exactly the hub set's size | same |
| R10 | "Covering whole triangles is what raises `d`" | chain `k=4`'s whole-triangle window `{0,1,2}` does not raise | same |

### Everything else that died

| # | dead claim | killed by |
|---|---|---|
| R11 | **Conjecture R**: `d_cb ≤ (1/β)·L_{Q\|W}` for every NAE fibre and rooting | the book rooted at its shared pair: exact ratios 2.5, 3.0, 4.25, 6.6 at `p = 2..5`, growing without bound. The boundary explains away the constraints, driving `L → 0` with the dual untouched |
| R12 | "The `1/β` ceiling is attained by the book and by re-rooted stars" | greedy artefact. The book's exact `d_cb` is 1, not 2 |
| R13 | "The obstruction is four π-classes on rank three" | deficiency 1 is **forced** by minimality (P12), so half the observation was definitional; and the size is 17 of 18, not universal |
| R14 | "Density gives room" (`candidate_class_shape.md` §§6–7) | the star family, whose tightness rises. The first refutation was itself built on a bound and had to be redone on exact values |
| R15 | "Connectivity buys slack" | the star is connected and its tightness → 1 |
| R16 | every quantitative claim in `gluing_is_a_cliff.md` — the 0.70 line, the dense-end 0.5866, the `r=7` 0.7594, the flat ceiling, the monotone decline, the connected supremum 0.6960 | each was a maximum over a bounded enumeration read as a property of the objects. Only §7's additivity survives |
| R17 | "The unpaid-boundary-rank hypothesis `μ = O(L)` is FALSE" | the exact `μ_min` computation: `μ_min = 0` almost everywhere (M11). The greedy `μ` minimised `d_cb` first, so it was an upper bound and its `μ > L` rows prove nothing — the note's own §11 says exactly this about the earlier pass |
| R18 | "Strong connectivity forbids cut vertices" (a self-correction that was itself false) | the directed bowtie; 8.1% of strongly connected 5-vertex digraphs carry a cut vertex |
| R19 | "`d_cb = k−1` for the star is verified only at `k ≤ 3`" | superseded upward by P1, which proves it for all `k` |
| R20 | "The constant is ≥ 4.26 from the S9 star" | worst of 10,976 boundary-preserving certificates; honest floors are 1.42 and 2.84 |
| R21 | Route A (`μ_min = 0`) "trivialises" the target | the candidate at `W = (0,)` has `μ_min = 0`, `R_< = 0`, and quotient **2**, not 0. Route A removes the absorption requirement; only route B forces the left side to 0 |
| R22 | "Exactly one configuration is covered by neither route" | 136 of 11,765. The replacement is stronger: none of them has `L < β`, and the minimum over the uncovered set is exactly `β` |

Refuted earlier in the campaign and carried in `ITERATION2_SYNTHESIS.md` §6: T1c per-block uniform
`γ`, Band III, the Band IV vacuity interval, the Band V shape classification, the 3-adic image bound,
"second-order differences leave the ternary class", cluster lemma part (1) (vacuous) and part (2)
(refereed-broken), and `dim span{q_a}` as the target's invariant.

---

## 6. Every exact `d_cb` value the campaign holds, by how it was measured

The distinction matters because the pair-sum search and the linked-pair model share an assumption —
that pair-sums are the directions that matter — so agreement between them is one anchor measured
twice.

### 6a. By a proved theorem

| object | `d_cb` | theorem |
|---|---|---|
| star `k = 1..7` | 1, 1, 2, 3, 4, 5, 6 | `d_cb = k−1` (P1) |
| `m` disjoint triples, `m = 1,2,3` | 1, 2, 3 | `d_cb = m` (P2) |
| single NAE triangle | 1 | both, degenerate |

### 6b. By the full `fast_dcb` search over **every** line of the dual

Independent of the pair-sum framing. These are the values that could have diverged from the model
and did not.

| object | `d_cb` | note |
|---|---|---|
| chain `k=2` | 1 | |
| path/chain `k=3` | 2 | |
| chain `k=4` | 2 | |
| chain `k=5` | 3 | 110s |
| `(2,1)` `k=4` | 2 | |
| `(1,1,1)` `k=4` | 2 | |
| `(3,1)` `k=5` | 3 | 461s |
| `(2,2)` `k=5` | 3 | 671s, registered in advance |
| `(2,1,1)` `k=5` | 3 | 219s, registered in advance |
| tri-cycle `k=3` | 2 | linear, non-tree — the separating control |
| tri-cycle `k=4` | 2 | |
| tri-cycle `k=5` | 3 | |
| **`(3,1,1)` `k=6`** | **4** | exhaustive, 5289s; and `>3` by a separate 2962s run |
| **`(4,1)` `k=6`** | **4** | exhaustive, 5851s; and `>3` by a separate 3423s run |
| star `k=4` | 3 | exhaustive over all 715 bases (161s), then 9.92s with the faster algorithm |
| chain `k=6` | 3 | 87s, `\|D\| = 19`, capped at its registered prediction so the return is exact |
| wheel `k = 3,4,5,6,7` | 1, 2, 2, 2, 3 | non-linear; matches the dossier's `⌈n/3⌉` for `n ≥ 4` |
| fan `k = 3,4,5` | 1, 2, 2 | non-linear; matches the dossier's path theorem |
| book `p = 2,3,4,5` | 1, 1, 1, 1 | non-linear; exhaustive, and it killed Conjecture R |
| candidate `r=5` | 2 | over 6,000 optimal residual spaces |
| crosspolytope `r=4` | 1 | matches the dossier's tag (31) — third independent implementation |
| dense `r=6` max-tightness object | 1 | the greedy had said 3 |

The `r ≤ 7` sweeps (401 fibres, 985 dense fibres, 6,545 three-triple fibres at `r=7`, 7,365
connected fibres) were all run with exact `d_cb` by this same path. Their *aggregate claims* are
retracted (R16); the individual values are not.

### 6c. Forced by the proved additivity lemma plus an exact component value

*Mine — a correction to the campaign's own accounting.* `linked_pair_characterisation.md` files the
disconnected constructions under "fully shared, measured by the pair-sum search alone". They are
not: P4 is proved and the components are exact, so these values are forced independently of any
pair-sum reasoning. `hub_count_formula.md` says exactly this when it uses chain3 ⊔ chain3 to kill
the global formula ("the refutation does not actually rest on the measurement").

| object | `d_cb` | forced as | in the 34-object table? |
|---|---|---|---|
| chain3 ⊔ chain3 | 4 | 2 + 2 | yes |
| chain3 ⊔ triangle | 3 | 2 + 1 | yes |
| chain3 ⊔ star3 | 4 | 2 + 2 | no — from the discriminating multi-component tests |
| chain5 ⊔ triangle | 4 | 3 + 1 | no |
| star3 ⊔ star3 | 4 | 2 + 2 | no |

*Recounting the 34-object table on this basis:* star `k=2..7` (6, theorem), disjoint `m=2,3`
(2, theorem), chain `k=2..6` (5, full search), `(2,1)` and `(1,1,1)` at `k=4` (2), `(3,1)`, `(2,2)`,
`(2,1,1)` at `k=5` (3), tri-cycles `k=3,4,5` (3), `(3,1,1)` and `(4,1)` at `k=6` (2), and the two
additivity-forced disconnected objects (2) — **25 fully independent**, with a further four (the
`k=6` squeeze rows) carrying an independent *lower* bound, and five genuinely pair-sum-only. The
campaign's own figure is "about 21"; the difference is the two disconnected objects and the
proved-theorem stars at the top of the range.

### 6d. Squeeze — exhaustive lower bound over all lines, pair-sum upper bound

Lower half independent, upper half not.

| object | `d_cb` | squeeze |
|---|---|---|
| `(3,2)` `k=6` | 4 | `d ≤ 3` exhausted over all lines (2871s) gives `≥ 4`; explicit pair-sum witness (26s) gives `≤ 4` |
| `(2,2,1)` `k=6` | 3 | |
| `(2,1,1,1)` `k=6` | 3 | |
| `(1,1,1,1,1)` `k=6` | 3 | agrees with chain `k=6`, same profile — the same-profile invariance check `k=5` could not give |
| star `k=6` | 5 | pair-sum UB 5, pinned by P1 |

### 6e. Pair-sum search only — upper bounds that match the model, and confirm only self-consistency

| object | value |
|---|---|
| star `k=7` | 6 — but pinned by P1, so not actually shared |
| tri-cycle `k=6`, `k=7` | 3, 4 (`k=6` stated in advance) |
| chain `k=7` | 4 |
| star4 + pendant chain3 | 4 |
| `(2,2,2)`, `(3,2,1)` `k=7` | 4, 4 (both stated in advance) |
| `(4,1,1)` `k=7` | 5 (stated in advance) |
| `(4,2)`, `(3,3)`, `(5,1)` `k=7` | 5, 5, 5 — the discriminating test for a formula that later died anyway |

The check the current evidence cannot supply, named by the campaign itself: run the full `fast_dcb`
search on one `k=7` shape where only the pair-sum search has spoken. Expensive at `r=15`, and it is
the honest test of the shared half.

---

## 7. Sections that still assert refuted claims

Every entry below is a section whose text reads as live and is contradicted by later work. I have
not padded the list and I have not skipped anything I found. Ordered by how likely a reader is to be
misled.

1. **`problem/mu_on_dense_stars.md` — the title and the section headed "Verdict: μ is NOT O(L) here".**
   The file's title is "The unpaid-boundary-rank hypothesis is FALSE on the packet's own incoherent
   family". Its `μ = k−1` values were read off a multi-pass greedy that minimises `d_cb` and then
   reports `μ`, so they are **upper bounds on the `μ` of a `d_cb`-optimal certificate** — precisely
   the defect `beta_is_the_absorption_threshold.md` §11 names ("upper bounds make `μ ≤ L` safe and
   `μ > L` worthless") and §12 fixes by minimising `μ` directly and exactly. §12 reports `μ_min = 0`
   for "the star". *Stated carefully:* §12 does not print the star's rooting, so I cannot certify
   the two computations are the identical configuration; what is certain is that the μ verdict's
   numbers sit on the wrong side of the inequality its own claim needs, which is enough to void the
   verdict without appeal to §12 at all. The file's three addenda reframe the *currency* of the
   question but never record that. Its closing "What this changes" item 1 — "Close the μ route for
   isolated blocks" — is dead either way. This is the most misleading document in the campaign,
   because the unsupported verdict is stated as a title.

2. **`STATE.md`, the block at "THE RANK LANE'S DECISIVE COMPUTATION, EXECUTED … the cheapest
   unexplored hypothesis is FALSE".** Carries the same dead verdict in its heading. The `β` block
   above it does record `μ_min = 0`, and one line there says "This corrects the mu block's framing" —
   but that sentence is about the wheel exception inside the `μ_min` block, not about this block's
   FALSE verdict. No marker points from the μ block to §12.

3. **`problem/why_ceil_k_over_two.md` §§1–14, and the file's opening sentence.**
   Line 3 asserts `d_cb = max(largest attachment group, ⌈k/2⌉)` "fits eleven exact values … and
   predicted two of them in advance" — that formula is R2, dead. §3's derivation of `d_cb ≥ ⌈k/2⌉`
   from `excess ≤ 2d`, §5's status table (including the row "`d_cb =` max of the two"), §7's chain
   ending "therefore `excess ≤ 2d`, therefore `d_cb ≥ ⌈k/2⌉`", §12's status table row
   "`excess ≤ 2d`, hence `d_cb ≥ ⌈k/2⌉` | follows from the above", and §13's boxed
   "`d_cb ≥ ⌈k/2⌉` for every linear triangle system" are all invalidated by §§19–21, which are 400
   lines further down. §19 does say "everything in §§3–7 rested on it" — that is the only
   backward-pointer in the file, and there is no forward marker anywhere above it.

4. **`problem/hub_count_formula.md` — the title and roughly the first 350 lines.**
   Title: "`d_cb = max(⌈k/2⌉, k − h)`: the hub count, not the group size". Refuted in the same file
   (R3, R4), about 490 lines in. In between: "Every exact value in hand … No exceptions"; "And the
   formula is now derived, not fitted", which derives `rank ≤ min(2d, d+h)` from `\|M\| = excess ≤ 2d`,
   a premise now known false; "The `d ≥ 2` composition holds", concluding "together they give
   `d_cb ≥ max(⌈k/2⌉, k − h)`"; the existence sketch; and the 32-random-system sweep. None carries a
   marker. The last section does flag itself ("The refuted formula is still right on all four").

5. **`problem/rooted_target_in_the_pairsum_frame.md` — four passages.**
   - The section head "The full cost profile: rooting is free or fatal, almost never expensive" and
     its boxed conclusion (R7).
   - "**Tri-cycles never block.**" (R8) — refuted 34 lines later.
   - "**'Free or fatal' survives the extension.**" — refuted 16 lines later.
   - "**Two mechanisms, both readable**" — its *first* mechanism (the window swallows a needed
     pair-sum's two hub coordinates) is disowned later in the file as a general account: "the
     mechanism I guessed for them is wrong", since the hub set is harmless on every chain. Its
     second mechanism, the counting ceiling `rooted d ≤ r − |W|`, is proved and stands (P15). So
     this entry is half-dead, and the half that died is not marked.
   None has a marker at its head.

6. **`problem/gluing_is_a_cliff.md` — the title and §§1–6 and §8.**
   The file is retracted in full except §7, but only at the very end. The title still reads
   "Constraint interaction is a cliff, not a slope: tightness 1 exactly when the constraints are
   disjoint", §1's boxed claim still says any shared coordinate drops tightness "to at most 0.70",
   and §8 still states "Supremum of tightness over connected objects with `m ≥ 2`: 0.6960". A reader
   who stops before §9 gets six retracted numbers.

7. **`problem/k6_predictions.md` — the whole file.**
   Built on R2 (`max(largest attachment group, ⌈k/2⌉)`), whose failure the file never records. Its
   prediction table says `(3,2)` → 3 and `(3,1,1)` → 3; both measured **4**. Its results section
   still closes "Nine registered predictions so far, nine hits", which was true when written and is
   not now. No marker.

8. **`problem/the_ceiling_holds_and_the_greedy_lies.md` §3.**
   The file has a correction banner, and the banner is good — but it does not cover §3's boxed
   "`d_cb = k−1` for the star is verified exactly only at `k ≤ 3`. Beyond that it is an upper bound",
   which P1 supersedes.

9. **`problem/candidate_class_shape.md` §§9–10, and §11's closing caveat.**
   §9 and §10 rest on "the star's `d_cb = k−1` is verified exactly only for `k ≤ 3`" and treat the
   star's tightness as a rising **upper bound**; §11 adds "`k = 5, 6` were still running; if either
   breaks the `k−1` pattern the trend would need revisiting". P1 closes all of it. §12 partially
   repairs the caveat (the tightness values are exact at the hub rooting) but stops its table at
   `k = 4`.

10. **`problem/linked_pair_characterisation.md` — three places that call `excess ≤ 2d` "unproved".**
    Lines describing the remaining gap say the lower direction rests on "`excess ≤ 2d`, resting on
    the unproved `E_t ≤ d`", and the scope-test section says "it needs `excess ≤ 2d`, which book
    `p=3` already breaks". As of §§19–21 of `why_ceil_k_over_two.md`, written afterwards,
    `excess ≤ 2d` is not unproved — it is **false**, on linear systems, at `d = 3`. This
    understates the status of the characterisation's own foundation.

11. **`mathbrain/campaign_objects.jsonl` and `mathbrain/README.md` — four of the thirteen campaign
    objects carry statuses the session has since overturned.**
    - `excess_at_most_two_per_dimension`, status `audited-pass`, statement "a subspace `R` of
      dimension `d` collapses `D` by an excess of at most `2d`" — **refuted** (R5). Its notes even
      argue the search was "COMPLETE rather than a sample", which is true of the 8-tree enumeration
      and false as a statement about linear systems.
    - `counting_bound_dcb_ceil_k_over_two`, status `conditional` on `E_t ≤ d` — the condition is no
      longer the issue; the derivation is gone.
    - `hub_count_lower_bound`, status `conditional` — its `rank ≤ 2d` half is refuted.
    - `hub_count_formula`, status `heuristic` — **refuted**, twice (R3, R4).
    The README's summary lines repeat all four. Also absent from the store: P1, P2, P4, the
    linked-pair characterisation, `excess = 2d + c`, the `(3,1,1)`/`(4,1)` exact values, the rooted
    window results and the Fano observation — so the store currently records the dead formulas and
    not the proved theorems.

12. **`LOG.md` ends at 20:3x with "a new formula, read off the obstructions rather than fitted",**
    presenting `max(⌈k/2⌉, k−h)` as the campaign's live position. Everything after 20:3x — the
    refutation at `(3,1,1)`, the linked-pair characterisation, the excess refutations, the rooted
    window work — is unlogged. A chronological log is allowed to stop, but this one stops one entry
    before the entry that kills its last one.

---

## 8. Contradictions between campaign documents

1. **`μ = O(L)` is simultaneously FALSE and true at zero.** `mu_on_dense_stars.md` (and its
   `STATE.md` block) says the hypothesis is false; `beta_is_the_absorption_threshold.md` §12 says
   `μ_min = 0` almost everywhere, which is far stronger than `O(L)`. §11 explains the discrepancy
   precisely — the first measurement optimised the wrong quantity, so its `μ > L` rows are the
   worthless direction of an upper bound — but the first document was never amended and the second
   never names it. **Resolution: the exact `μ_min` computation wins, and the FALSE verdict is void
   on its own terms regardless of whether the two runs used the same rooting.**
   `attacks/attack_rank.md` and `ITERATION2_SYNTHESIS.md` row 29 both still record the question as
   UNKNOWN, which is correct for the residual class and stale for everything computable.

2. **The precedence rule points at a stale ledger.** `STATE_OF_THE_PROOF.md` line 3 says
   "`ITERATION2_SYNTHESIS.md` remains the adjudicated claim ledger, and where the two differ the
   ledger's labels win". The ledger's row 35 labels Conjecture RC "the weakest claim in the campaign
   — ℚ only, `r ≤ 5`, no data at `r ≥ 8` … do not build on"; RC has since been proved with equality
   on an infinite family (P2), matched against the dossier's own proved cycle bound, and followed
   along six families to `k = 7`. Under the stated rule the stale label wins. The rule needs
   retiring or the row needs updating.

3. **`STATE_OF_THE_PROOF.md` §9 closes with "`d_cb ≥ k−1` (the lower bound, hence saturation) is not
   proved".** `star_family_proved.md` §6 proves it, and that file is the later of the two on disk.
   The same document's §9 opening correctly reports the star construction as proved, so the file
   contradicts itself within one section.

4. **Whether the disconnected values are independent evidence.**
   `linked_pair_characterisation.md` files them as "fully shared … measured by the pair-sum search
   alone"; `hub_count_formula.md` says of the same objects that "the refutation does not actually
   rest on the measurement: additivity is proved and chain `k=3` is exact, so 4 is forced". The
   second is right (see 6c), and the first under-counts the campaign's own independent evidence.

5. **The one surviving result of a fully retracted note lives inside that note.** `gluing_is_a_cliff.md`
   §9 says the file is "superseded in full except §7" and that §7's additivity lemma "belongs in
   `the_constant_is_attained.md` rather than here". It was never moved. The proved additivity lemma —
   which forces five exact `d_cb` values and underwrites the component-wise reading — currently sits
   in the middle of a document whose closing instruction is to disregard it.

6. **The dossier-agreement count.** STATE.md says ten agreements; `why_ceil_k_over_two.md` §16 notes
   the dossier states its cycle theorem only for `n ≥ 4`, which makes the wheel `n=3` row an
   agreement with an extrapolation. Nine is the defensible number.

7. **`|D| = r + k` and wheel `k=3`.** §13 recorded wheel `k=3` as evidence that non-linearity
   enlarges the dual; §16 corrects that — every other non-linear object also satisfies `|D| = r+k`,
   and wheel `k=3` is a degenerate 3-cycle outside the dossier's own stated range. §13's table row
   remains in place without a marker. Minor, but it is the same shape as the others.

---

## 9. Where the campaign stands on the conjecture

It has not moved the conjecture, and it is important to say that in the same breath as anything else.
What this campaign has is a small, sharp theory of a finite object — the selector distance `d_cb` of
linear triangle systems — with two genuine theorems in it (the star at `k−1`, disjoint triples at
`m`), a proved additivity lemma, a proved reformulation of the Rado condition as a blocking
condition, a proved account of why linearity rather than treeness is the hypothesis, and an
explanation of where the constant `1/β` comes from that ties the rooted target's constant to the
dossier's own anticoncentration cap `max ψ = 3/4`. It also has nine independent agreements with two
theorems the dossier proves by other means, which is the only external calibration the machinery has
ever had, and it is a real one. Against that: the campaign's principal quantitative conjecture,
`d_cb ≥ ⌈k/2⌉`, currently has **no derivation at all** — the lemma it rested on is false at `d = 3`
on tri-cycles, its repair is false as well, and what survives is a fitted shape `excess = 2d + c`
that has been checked against two counterexamples and no general upper bound on excess is held. The
linked-pair characterisation matches every object measured and is the best description the campaign
has, but it is a description; its lower half inherits the broken lemma and its upper half was never
argued. Above all, the object the whole programme is about — a member of the dense, connector-
incoherent residual class — has still never been exhibited by anyone, here or in the 200 pages, so
every number in this document is a measurement on something known not to be in the class, and the
block-internal certificate that Layer II actually needs has not moved in the entire campaign. The
honest position is that the campaign has built a working laboratory and calibrated it against
external theorems, and has not yet used it on the case that matters.

---

## ADDENDUM 2026-09-01 (30h loop, session 2b7f8005): the night's results, by grade

Full trail: ASSEMBLY_no_R2_20260901.md (status box first), then
exists_choice_conjecture_20260901.md (the flagship),
conjA_body3_cutinflation_20260901.md and outside_gap_20260901.md (working
chronologies with the refutations in place).

REFEREED THEOREMS (fresh-context adversarial passes, reports on disk):
- K(p,q) coverage theorem (kpq_coverage_draft_20260901.md): every +-1-valued
  form on those fibres reduces mod R to +-u or +-e_h. CONFIRMED-WITH-
  CORRECTIONS, C1 applied.
- 2-SHARED PURITY (purity_referee_20260901.md): every triangle <= 2-shared
  => D = coordinates u triangle forms exactly (proved regime). CONFIRMED-
  WITH-CORRECTIONS (557 exact runs, 0 breaks; step-c repaired by referee;
  spanning hypothesis redundant - <= 2-shared forces spanning).

REFUTED TONIGHT (falsifier-first; each corrected in place same-tick):
- "Outside regime => c <= 0": FALSE. K(3,3)-matching (S32's own family) is
  linear, spanning, outside, c = +0.1277. The 442-random-system base was
  sampling bias. outside_gap_20260901.md carries the full story.
- The L1a blob program (W9 break, referee-constructed) - repaired into the
  R1/R3 pieces; R1's chain BROKEN-AS-PROVED at the same missing inequality
  everything else needs (assembly_referee_R1_R3_20260901.md); R3 largely
  confirmed. Also refuted: max-dim and min-dim canonical choice forms,
  A-prime, the correlation floor, the collapsed closure bound, my own
  too-strict checker's no-winner claim (scar filed).

THE FLAGSHIP OPEN STATEMENT (implies RC for all linear NAE triangle
systems): the TWO-SIDED EXISTS-CHOICE - every spanning linear system has a
pair choice with c <= beta(k - dim R) and valid_R. Proved on |D| = r+k
(M1-M3); verified exhaustively on Pasch/witness/W9/K33-matching and by
search on 285+ random outside systems and the K-matching family through
K(4,5); the K_{q,q} family's c-side closed EXACTLY via S34's fibre count
(automatic-dependency margin 1.82q - 6.2). Structure: a WINDOW statement
(class-merge floor vs c-side ceiling) with a measured merging CLIFF
(21 -> 3 -> 2 classes). Sub-conjecture FR (full-rank => admissible,
55k/0) under prover-referee as of this writing.

MECHANISM RESULTS (measured, unrefereed): implied-triple taxonomy
(divisibility/GF(2)-even-subfamilies - quorum >= 4 DERIVED, Pasch minimal;
UP-forcing chains 99.0%; 22 deep), CONJECTURE CERT (minimal UP-certificate
subsystems subcritical, Pasch extremal Z <= 8/9, 269 certificates, survives
inside c > 0 hosts).


### 2026-09-01 addendum update (hour 10)

The FR prover-referee cycle completed after the entry above: FR (full-rank
=> admissible) CONFIRMED at 10,284/10,284 but unproved; FR-c refuted and
REPLACED BY A PROVED THEOREM - the Rado criterion: a full-rank one-pair-per-
triangle choice exists iff every subset S of triangles touches at least |S|
coordinates (verified against exhaustive enumeration). Realizability proved
for bipartite choice graphs; the general case reduced to an explicit
dodge-CSP (open, 0 failures measured). The k > r regime reduces to the pure
counting inequality c <= beta (k - r) (263/263 dense spanning systems, min
slack +0.48). The one-step case reduced to a scalar-spread statement; both
open pieces under a second prover-referee. Reports:
FR_prover_referee_20260901.md, scalar_spread_referee_20260901.md (pending).

Second referee cycle (hour 11): maxrank of pair-sum choices is the
Rado-deficiency quantity min_S (|coords(S)| + k - |S|), NOT min(k, r)
(broken premise, witnesses on record); Theorems A1, B1, B2-cases PROVED
(scalar_spread_referee_20260901.md) - the realizability dodge-CSP is
superseded by interior absorption, with the Fano plane as the boundary
object. The window program's opens: extras value bound, rigidity Q, and
|A| <= (3/2)^r for k > r.

Third referee cycle (hour 11-12): the dense inequality |A| <= (3/2)^r for
spanning k > r is REFUTED - compound witness S33 (two K33-matching blocks +
a Z5-torus + one bridge triple; spanning certified exactly; ratio 1.0140,
family unbounded), verified by three independent code paths including a
2^27 brute-force gold standard. K33-matching itself spans, making the k > r
form equivalent to the k = r bound it already violated. The 263-system
supporting scan was generator-scope bias (compounds absent from random
connected-ish sampling) - the same mechanism that had killed the outside
gap, now claiming one of this session's own conjectures. Survivors: the
connected-repair form (referee frontier 0.978), the 42^{r/9} base
candidate, exact reduction lemmas. A fourth referee is testing whether the
flagship exists-choice reduces to connected systems and whether S33 itself
carries a witness. Report: dense_inequality_referee_20260901.md.

Fourth referee cycle (hour 12): the flagship exists-choice HOLDS on S33
(witness at the exact dim ceiling, verified on the full fibre) and is
PROVED to reduce to connected systems - disjoint-union composition and the
single-bridge 3-block theorem both proved and brute-verified
(compound_flagship_referee_20260901.md). The compound machinery that
refuted two conjectures tonight is disarmed against the flagship up to
multi-bridge composition (open).

Fifth referee cycle (hour 12): multi-bridge composition essentially closed
- dual law proved for bridge forests (h-family characterized for 2-in-1),
c-neutrality proved with exact factors, tree composition proved, cycle
composition via closing choices (sharp 9/729), S36 witnesses end-to-end at
r = 36. The flagship's one remaining attack surface: the extras value
bound (many-extras hosts vs the r-class budget). Report:
multibridge_referee_20260901.md.

Seventh referee cycle (hour 12-13): the extras-overflow route is CLOSED at
the top layer - hub-forcing lemma (K(q,q) dual = 3q + q^3 for all q),
unconditional 2-class collapse lemma at dim r-1, overflow frontier reduced
to a triple-simultaneous corner (nearest measured margin 0.0595 bits). A
+-1-extras universality claim was corrected (coefficient-2 certificate on a
dense system). The flagship is unbroken on all seven cycles' evidence.
Report: extras_bound_referee_20260901.md.
