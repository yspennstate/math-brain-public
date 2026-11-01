# Conjecture R is false, and its death gives the first necessary condition on "admissible"

Author: main session c53c1d50, 2026-08-19 ~05:0x. **This corrects §2 of `the_ceiling_holds_and_the_greedy_lies.md`, written and committed an hour earlier (697d8a628).** The correction is the result.

## 1. What died

I had tested, and failed to falsify, **Conjecture R**: `d_cb / L_{Q|W} ≤ 1/β = 2.40942` for every NAE fibre and rooting. I also claimed the ceiling was *attained* by a family — the NAE triangle, the 3-page book (theta `m=1`), and re-rooted stars.

Exact computation kills both halves.

**The book's `d_cb` is 1, not 2.** The greedy said 2; the exhaustive search (all full-rank dual bases, all selector assignments by DFS with a rank bound, no truncation) says 1, for every `p = 2..5`. So the book does **not** attain the ceiling at `nW=1` — its ratio there is 1.475, 1.205, 1.096, 1.046, *falling* toward 1. My "attains 1/β" claim was a greedy artifact, the same failure mode I had documented one section earlier and still walked into.

**And rooted at its own shared pair the ratio is unbounded.** With `nW = 2` (boundary = the two coordinates every triple contains):

| book `p` | `r` | \|A\| | exact `d_cb` | `L_{Q|W}` | ratio |
|---|---|---|---|---|---|
| 2 | 4 | 10 | 1 | 0.40000 | **2.5000** |
| 3 | 5 | 18 | 1 | 0.33333 | **3.0000** |
| 4 | 6 | 34 | 1 | 0.23529 | **4.2500** |
| 5 | 7 | 66 | 1 | 0.15152 | **6.6000** |

`d_cb = 1` is exact and tight (`|D| > r` forces `d_cb ≥ 1`), and `L` is exact, so `ratio = 1/L` is exact. **`d_cb ≤ C·L_{Q|W}` therefore fails for every constant `C`.**

I re-derived `L` by hand for `p=3` rather than trust the code: the boundary values `(+,−)` and `(−,+)` have 8 completions each, `(+,+)` and `(−,−)` have 1 each, so `H(Q|W) = (16/18)·3 = 2.6667` and `L = 3 − 2.6667 = 1/3`. Ratio 3 exactly.

## 2. The mechanism, which is the useful part

Every triple in the book contains **both** boundary coordinates. Conditioning on them therefore **explains away the constraints**: when `s₀ ≠ s₁` every NAE triple is already satisfied and the private coordinates are completely free. That branch carries `2^{p+1}` of the `2^{p+1}+2` mass, so `H(Q|W)` approaches the full `p` bits and `L → 0` — while the dual is unchanged and still needs a selector, so the numerator stays at 1.

> **The rooted estimate fails whenever the boundary absorbs the constraints that generate the dual.** `L_{Q|W}` measures how much the private part is still constrained *given* `W`; put the constraints' shared support into `W` and that measurement goes to zero without the dual getting any simpler.

## 3. Why this matters to the campaign rather than just being a counterexample

The campaign is blocked on **"admissible Gale basis exchange"**, undefined in the 200 pages and not recoverable locally (`the_missing_tree_hunt_closed.md`). Every attempt so far has tried to *guess* the definition. This gives instead a **necessary condition it must satisfy**, derived rather than guessed:

> **No admissible rooting may place in `W` a set whose conditioning drives `L_{Q|W} → 0` while the dual is untouched.** Equivalently: admissibility must be a joint condition on the *pair* (decomposition, rooting), not a property of the decomposition alone.

This is the first constraint on that term the campaign has obtained from mathematics. It also sharpens `g2_sharpened.md`, which argued admissibility must forbid forms spanning incomparable blocks — that was a condition on the decomposition; this is a second, independent condition on the rooting.

## 4. What is NOT established, stated before anyone asks

**This does not falsify the packet's rooted target (41)/(3).** That target's left side is `dim((R+R_<)/R_<)`, a quotient by the ancestor-paid space — not `d_cb`. Since `dim((R+R_<)/R_<) ≤ dim R = d_cb`, my left side is an **over-estimate**, and with `d_cb = 1` the true left side is 0 or 1. If `R ⊆ R_<` it is 0 and there is no violation at all.

So the honest statement is a dichotomy: for the book rooted at its shared pair, **either the rooting is inadmissible, or `R ⊆ R_<` necessarily.** Both branches are informative — the first gives §3's necessary condition, the second says the ancestor-paid space must always absorb this configuration, which is itself a checkable structural claim. What is dead is the naive form `d_cb ≤ C·L`, which is what I was actually testing and what I had reported surviving.

## 5. Third correction in three hours, and they rhyme

The false SCC/cut-vertex argument, the "predictions hit" that confirmed a heuristic, and now a ceiling claim built on the same heuristic. All three were caught by the same move — **compute the thing exactly on the smallest case** — and in each the exact computation took under two minutes against prose that had taken far longer. The greedy has now produced two wrong claims in one session, in **opposite** directions: six false violations (bound too high) and one false attainment (bound too high, read as a value). One rule covers both: *`d_cb` from the greedy is an upper bound and may be used only where an upper bound is sound.* It is sound for "meets the target"; it is worthless for "attains", "exceeds", or "equals".
