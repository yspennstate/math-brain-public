# [VERDICT WITHDRAWN 2026-08-20] The unpaid-boundary-rank hypothesis is FALSE on the packet's own incoherent family

> **The verdict in this title and in the section "Verdict: mu is NOT O(L) here" is withdrawn.**
> The `mu` values below come from a multi-pass greedy that minimises `d_cb` FIRST and takes `mu`
> only afterwards, so they are **upper bounds on the `mu` of a `d_cb`-optimal certificate**. R7
> concerns the certificate one would actually choose, which may accept a larger `d_cb` to buy a
> smaller `mu`. An upper bound makes `mu <= L` safe and `mu > L` worthless, and every row here
> points in the worthless direction - so the arithmetic cannot support the verdict, independently
> of any later work.
>
> `beta_is_the_absorption_threshold.md` section 11 names this defect in the campaign's own words
> and section 12 does the exact measurement, reporting `mu_min = 0`. Section 12 does not print the
> star's rooting, so it is not certified here that the two computations are the identical
> configuration; the withdrawal does not depend on that.
>
> **What survives:** the cross-validation in "Cross-validation before any conclusion" is
> untouched - the `k = 3` row reproduces the rank lane's exhaustive branch-and-bound exactly
> (`d_cb = 2`, forced leak 1, optimum `(2,1)`), two methods agreeing on a nontrivial value. The
> `d_cb` numbers are fine. It is the `mu` verdict, and the "Close the mu route for isolated
> blocks" conclusion that follows from it, that are withdrawn.

Author: main session c53c1d50, 2026-08-19 ~02:3x. This executes the computation named as decisive in `attacks/attack_rank.md` §7.3/§12 — "whether residual-class blocks have μ = O(L)… the cheapest unexplored hypothesis on the board". Code: scratchpad `mu_dense_stars.py` (exact rational arithmetic, local, BelowNormal, seconds).

## What was computed

The k-arm NAE star: private `q`, arms `i = 1..k` each a pair `(x_i, z_i)`, rows `Y_i = x_i + z_i + q` required ±1-valued. `k = 3` is exactly the S9 counterexample (dossier pp.153–154). For each k: the fibre by enumeration, the projective full dual by solving on a spanning set and testing ±1-valuedness, then over every coordinate basis drawn from that dual and a multi-pass greedy signed-selector assignment, the minimum of `d_cb = dim R`, the leak `λ = dim(R ∩ span W)`, and `μ = dim span{boundary parts of the residual generators}` — all at `R_< = 0`.

| k | r | \|A\| | ℓ | L | \|D(A)\| | bases | d_cb | μ | λ | μ/L | d_cb/ℓ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 5 | 18 | 0.8301 | 0.5556 | 7 | 15 | 1 | 1 | 0 | 1.800 | 1.205 |
| 3 | 7 | 54 | 1.2451 | 0.7037 | 10 | 54 | **2** | **2** | **1** | **2.842** | 1.606 |
| 4 | 9 | 162 | 1.6601 | 0.8025 | 13 | 189 | 3 | 3 | 2 | 3.738 | 1.807 |

**Cross-validation before any conclusion.** The k = 3 row is the S9 star, and it reproduces the rank lane's exhaustive branch-and-bound exactly — `d_cb = 2`, forced leak `1`, optimum `(2,1)`, and `μ/L = 2.842 = 54/19` — from independent code using a different search strategy (greedy-with-restarts over every basis, versus their branch-and-bound). Two methods, same optimum. That is the check that licenses reading the other rows.

## Verdict: μ is NOT O(L) here

Closed forms, read off the table and confirmed algebraically:

- `|A| = 2·3^k`, `r = 2k+1`, so **ℓ = (2k+1) − log₂(2·3^k) = k(2 − log₂3) = k·log₂(4/3) = k·β** exactly.
- **d_cb = k − 1** and **μ = k − 1** (both matched at k = 2,3,4), while **L → 1** (0.556, 0.704, 0.803, saturating).

So `μ/L ≍ k → ∞` while `L` stays bounded. **The unpaid-boundary-rank hypothesis fails on the packet's own connector-incoherent family**, which is the rank lane's outcome (3): *"if both blow up, Target R-C is where the whole programme must be attacked."* The cheapest unexplored hypothesis is now explored, and it is not the way through.

**Scope, stated precisely (this is the part a referee should attack).** The computation is at `R_< = 0` — an *isolated* block with nothing pre-paid by ancestors. S14 §7's lesson is exactly that such blocks can become free once ancestors have paid (the m=1 interval costs zero after payment). So this settles the isolated case and does **not** settle the in-tree case, where μ is measured modulo `R_<`. A tree-embedded version is the honest follow-up, and it is the same computation with a nonzero `R_<`. Also: this scales the star by ARM COUNT (arms of size 2), which is the regime where L saturates; the entropy lane's §5b stars scale by arm SIZE. Both are "dense stars"; only the arm-count family has bounded L, which is what makes it the sharp test.

## A second, unlooked-for result: the dense stars approach the sharp constant from below

Since `d_cb = k − 1` and `ℓ = kβ`,
  **d_cb/ℓ = (k−1)/(kβ) ↗ 1/β = 1/log₂(4/3) = 2.40942…**
The k-arm stars form a family converging to the packet's constant floor from below, never exceeding it. That floor was previously witnessed only by products of NAE three-circuits (dossier S6 tag (5)); this is a **second, structurally different family with the same limit**, and it is direct new evidence for the rank lane's **Conjecture RC** (`d_cb ≤ ℓ/β` sharp) — evidence that lane explicitly said it lacked ("small-rank evidence only… the weakest-supported claim in this memo"). It does not prove RC, and a family engineered to exceed 1/β would still most plausibly live at larger rank where neither of us has data.

## ADDENDUM (02:4x, same session): the verdict above is right but the QUESTION was posed in the wrong currency

Working the in-tree variant immediately, before it could be filed as "surviving", produced a correction to my own reading. Both statements below are exact.

**1. The star is perfectly linear — in ℓ, not in L.** From the closed forms: `d_cb = k − 1` and `ℓ = kβ`, so `d_cb = ℓ/β − 1 < ℓ/β`. **The star satisfies the unrooted target with the sharp constant.** What fails is only the *rooted-in-L* statement, because `L` counts the private entropy deficit alone (one bit of `q`, saturating at 1) while the star's cost is carried by the *boundary's* deficit (k·β of it). So `μ/L → ∞` is not evidence that the block is hard; it is evidence that **L is the wrong denominator for this block** — precisely S14 §7's m=1 lesson (`L → 0` with one direction remaining), here generalised to arbitrarily large blocks.

**2. Charged to the boundary's own defect, the star is bounded — with the same universal constant.** The boundary marginal is `A_W = {W : some q completes it}`; a W-point fails only if some pair is (+,+) *and* some pair is (−,−), so
  **|A_W| = 2·3^k − 2^k**, and `ℓ_W = 2k − log₂(2·3^k − 2^k) → kβ − 1`.
*(Cross-check: k = 3 gives |A_W| = 54 − 8 = 46 — exactly the boundary-marginal count the entropy lane and the referee computed independently for the S9 star, 27 + 27 − 8. The formula reproduces a number two other agents got by other means.)*

| k | ℓ_W | cost d_cb | d_cb / ℓ_W |
|---|---|---|---|
| 2 | 0.193 | 1 | 5.18 |
| 3 | 0.476 | 2 | 4.20 |
| 4 | 0.810 | 3 | 3.70 |
| → ∞ | kβ − 1 | k − 1 | **↘ 1/β = 2.409** |

So the ratio is bounded and *decreasing to the same constant floor*, approached from above rather than below. **The dense star is an ancestor-paid object, exactly like the m=1 interval, and its cost is linear in the defect its boundary actually owns.**

**3. What this does to the μ route.** It is not dead; it was misposed. The live question is not "is μ = O(L)?" — answered no, above — but:
> **Is μ_B = O(ℓ_{W_B}), i.e. is a block's unpaid boundary rank linear in the defect of its own boundary marginal?**
That currency is the one the telescope's chain rule apportions (T1b: `Σ_B L_B ≤ ℓ`, with the boundary deficits belonging to ancestors), and it is exactly what the amortized target (A) in `telescope_reconstruction_draft1.md` §5.6 was constructed to charge. The star family is now a *worked witness* that per-block-L charging fails while amortized charging succeeds — which is independent support for (A) from a family that was built to be an obstruction.

**4. Honest limits of this addendum.** (a) The ratios 5.18/4.20/3.70 exceed 1/β at every computed k, so any theorem in this currency needs a constant strictly above the three-circuit floor — the star is a *second* constraint on the constant, and at small k a stronger one. (b) I have not shown the boundary marginal's defect is *available* to the parent: the parent must pay for those directions out of its own budget, and whether the tree's total stays within ℓ is exactly (A)'s unproved hypothesis — this addendum makes (A) more plausible, it does not prove it. (c) Everything here is still the star, a calibration object the dossier explicitly excludes from the residual class.

## ADDENDUM 2 (02:5x): the affordability check, run — and the star's failure is a DECOMPOSITION ARTIFACT

The addendum above left one thing open: can a parent actually afford the boundary directions? The smallest object where that is checkable is the star viewed as a two-level tree, so I ran it. It is a two-line computation with a large consequence.

**The natural tree.** Root block = the single coordinate `q` (the homogenizer). Children `B_1..B_k` = the arms: child `i` has privates `{x_i, z_i}` and incoming boundary `W_i = {q}`. Rows `Y_i = x_i + z_i + q` belong to their arms.

**Per-child arithmetic, exact.**
- Conditional defect: given `q`, the pair `(x_i,z_i)` has exactly 3 allowed values, so `H(Q_i|W_i) = log₂3` and **`L_i = 2 − log₂3 = β = 0.41504`**. Root block: `L_root = 1 − H(q) = 0`.
- Chain-rule check: `Σ_i L_i = kβ = ℓ` **exactly** — the telescope's (T1b) holds with equality on this family.
- Certificate: select the boundary coordinate `q` for the row `Y_i`. Residual `Y_i − q = x_i + z_i`, which is **purely private**. So the quotient is `dim((R_i + B)/B) = 1`, and the leak is `R_i ∩ span W_i = span{x_i+z_i} ∩ span{q} = 0` — **absorption holds trivially, for every child, with no ancestor payment at all.**
- Hence each child satisfies the **full rooted target, both clauses**, with `cost/L_i = 1/β = 2.40942…` — the sharp constant, exactly, block by block. Nothing is amortized; nothing needs the parent's budget.

**So the affordability question does not even arise on this family, and the earlier "failure" was an artifact of the decomposition.** Treating the whole star as ONE block makes `q` private and all `2k` arm coordinates boundary — which lumps `k` arms' worth of cost against a single bit of private entropy (`L → 1`). Decomposed the natural way, with `q` as the root and the arms as children, every block is individually sharp-constant compliant. **Which coordinates count as private versus boundary is a decomposition choice, and the star's pathology was choosing the pathological one.**

**Why this matters beyond the star — three consequences.**
1. **It explains the dossier's own exclusion.** S6 p.123 removes blocks with an "`o(log n)` ordinary star core" from the residual class. That exclusion has always read as a technical convenience; it is not. A star is *removable* precisely because a better decomposition of it exists, and the residual class is defined only after *every* admissible Gale basis exchange — i.e. the class consists of the blocks that fail for **every** decomposition. The star fails for one and succeeds for another, so it was never a class member. This is the structural reason, and I have not seen it stated in the dossier.
2. **It sharpens admissibility (G2 in `telescope_reconstruction_draft1.md`).** An admissible decomposition must not create a block whose private entropy is tiny relative to its cost. The star gives the minimal counterexample to the naive choice and the minimal witness that the good choice exists.
3. **It raises the bar for any future "obstruction" example**, mine included: an object only obstructs if it fails under every decomposition. Exhibiting failure under one is now known to be worth nothing — which retroactively weakens what I claimed two addenda ago, and I would rather say so than leave the stronger reading standing.

**Honest limits.** (a) This is the star, still a calibration object, still excluded from the residual class — the finding is about *why* the exclusion is legitimate, not about the class itself. (b) I have not shown that a good decomposition exists for anything harder; the class is *defined* by the non-existence of one, so this cannot generalise by itself. (c) The constant `1/β` recurring here for a third time (three-circuit products, the k-arm star's ℓ-ratio, and now the arm-decomposed per-block ratio) is suggestive for the rank lane's Conjecture RC, but three families sharing a constant is not a proof and two of the three are the same object measured differently.

## What this changes

1. **Close the μ route** for isolated blocks: recorded, with the in-tree variant as the surviving question.
2. **Target R-C stands as the campaign's central obstacle** — the factor-Θ(log n) rank compression, unchanged and now unavoidable by the cheap hypothesis.
3. **Conjecture RC gains an independent family.** If RC is true, the deterministic target is not merely `O(ℓ)` but `ℓ/β` with the constant pinned — a strictly more falsifiable statement, and the natural next thing for a counterexample hunt to aim at.
4. Honest limit: none of this touches the block-internal certificate for dense connector-incoherent cores, which remains exactly as open as before. The star is a calibration object, not a member of the residual class (the dossier excludes `o(log n)` star cores explicitly, S6 p.123).
