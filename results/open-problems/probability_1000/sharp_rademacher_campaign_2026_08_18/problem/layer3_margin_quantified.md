# The Layer-III margin, quantified — and why ℓ = 1 is the whole conjecture

Author: main session c53c1d50, 2026-08-19 ~03:4x. Executes item (5) of `ITERATION2_SYNTHESIS.md` §3: *"quantify the Layer-III margin… which replaces 'o(log n)' with a number **and** decides the strongest case against W2/W3 (if the union bound is borderline at the endpoint, description length is necessary but not sufficient and cancellation is doing real work)."* Everything below is elementary and self-contained on top of `encoding_interface_reconstruction.md` §1; the load-bearing step is Erdős's Littlewood–Offord bound.

## 1. A component's defect is exactly its dependency's anticoncentration — so ℓ ≥ 1 always

In the reconstructed framework a component is `k` rows plus the fibre `A ⊆ {±1}^k` of their column-restrictions; a dependency `Σ_a c_a x_a = 0` confines `A` to the hyperplane `c^⊥`. Then
  `|A| = 2^k · Pr_x[c·x = 0]`, so **`ℓ = k − log₂|A| = −log₂ Pr[c·x = 0]`.**
The defect is *not* an extra structural parameter: it is the negative log of the dependency's concentration probability at zero. Consequences, all immediate:

- **If `c` has exactly two nonzero entries** (necessarily `±1` against each other, i.e. two equal or opposite rows), `Pr = 1/2` and **`ℓ = 1` exactly.**
- **If `c` has support `s ≥ 3`,** Erdős's Littlewood–Offord bound gives `Pr ≤ C(s,⌊s/2⌋)/2^s < 1/2`, so **`ℓ > 1` strictly**, and for ±1 coefficients `ℓ = ½log₂s + Θ(1)`.
- Therefore **`ℓ ≥ 1` for every component, with equality exactly on the coincident-pair mechanism.**

That last line is worth pausing on: the framework's defect parameter attains its minimum precisely on the mechanism that produces the conjecture's constant (`layer3_interface_note.md` §1). Nothing was arranged to make that happen.

## 2. The budget, computed

The requirement is that the non-dominant sum be `o(n²2⁻ⁿ)`. A slice with parameters `(k, ℓ)` contributes at most `N(k,ℓ)·2^{−nℓ}` where `N` counts (row set, fibre) pairs, so the slice is affordable iff

  `log₂N(k,ℓ) < nℓ − n + 2log₂n − ω(1)`.

Splitting `N` into the row choice and the fibre naming, and using the endpoint range `k = O(n/log n)`:
  `log₂C(n,k) ≈ k·log₂(n/k) = O((n/log n)·log₂log n) = o(n)`,
so the **fibre-naming budget** is

  **`log₂N_fibre < n(ℓ − 1) + 2log₂n − o(n) − ω(1)`.**

Read off the two regimes:

| regime | budget for naming | what it means |
|---|---|---|
| **ℓ = 1** (support-2 dependency) | `2log₂n − ω(1)` bits, i.e. **at most ~n² components, and no exponential room at all** | exactly saturated by the `≈2n²` coincident row/column pairs — this slice *is* the conjecture's constant |
| **ℓ > 1** (support ≥ 3) | `n(ℓ−1)` bits — **exponential** | enormous room |
| class parameters, `ℓ ≈ ½log₂log n` | `≈ n(½log₂log n − 1)` bits | vast |

## 3. The answer to the synthesis's question: the union bound is NOT borderline where the class lives

At the residual class's own parameters the naming cost supplied by a rank certificate is `O(d_cb·k + j log r + r + n)` with `d_cb = O(ℓ)` and `k = O(n/log n)`, i.e.

  cost `≈ n·ℓ/log n + O(n)`  versus  budget `≈ n(ℓ − 1)`.

The ratio is `Θ(log n)`. **The union bound has about a log n factor of slack at the class's parameters — it is not borderline there, so no cancellation is required and description length is not merely necessary but sufficient.** W2/W3's strongest objection (that a centered-moment expansion must be doing cancellation work a counting bound cannot) is answered in the negative *for the residual class*.

**And this independently re-derives W1 with its constant explained.** The transfer lane found that any uniform coefficient `γ_n = o(log n)` closes Layer II; here the same `log n` appears as the *ratio of budget to cost* — which says W1's log-factor is not a coincidence of the dossier's bookkeeping but the actual margin between what the class costs to name and what the exponential saving affords. Two derivations, one from the packet's tags (27a)–(27b) and one from Erdős's inequality, landing on the same factor.

## 4. Where the difficulty actually is, restated

**Every bit of the conjecture's difficulty lives at `ℓ = 1`, and it is a counting problem, not a rigidity problem.** There the budget is `2log₂n` bits with no slack, so the claim reduces to: *the components with a support-2 dependency number `(1+o(1))·2n²` and nothing else has `ℓ = 1`.* The first half is the count of coincident row and column pairs; the second half is §1's Littlewood–Offord dichotomy, which is exact. Meanwhile the deterministic programme — the entire Layer-II apparatus of rigidity, congestion, absorption and the connector theorem — operates in the regime that has `n(ℓ−1)` bits of room to spare.

**The strongest case against this reading**, stated because it is the obvious objection: the sum over a slice is `Σ 2^{−nℓ}` over *all* components in it, and I have bounded slice by slice; if the number of *slices* is itself large (ℓ ranges over ~`k` values, k over ~`n/log n`), the union over slices costs another `log₂(n²/log n) = O(log n)` bits — which is absorbed by the `2log₂n` only if the `ℓ = 1` slice is treated exactly rather than through the generic bound. That is precisely how the packet's own argument is organised (the low-corank endpoints are *closed exactly*, not estimated), so the reading is consistent with the architecture — but the `ℓ = 1` slice must never be handled by the generic machinery, and any future write-up that lets it be has an error.

## 5. A spectral gap in the defect (clean, and it sharpens §2)

Erdős's bound is attained at the central binomial, so the *possible* values of ℓ are quantised at the bottom:
  `s = 2: ℓ = 1` · `s = 3 or 4: ℓ = −log₂(3/8) = 1.4150` · `s = 5 or 6: ℓ = −log₂(10/32) = 1.6781` · then `ℓ ≈ ½log₂s + ½log₂(π/2)`.
**No component has ℓ ∈ (1, 1.4150).** So the ℓ = 1 slice is not merely the minimum — it is *isolated*, with a gap of 0.415 to everything else, and every non-dominant component therefore enjoys at least `0.415n` bits of naming budget. The conjecture's `(1+o(1))` is a statement about a slice separated from its competitors by a constant gap in the exponent, which is why the answer is as clean as it is.

## 6. FALSE START, recorded because the next reader will hit it

Working §5 forward, I briefly convinced myself the conjecture *followed*: for corank-1 components the row choice costs `log₂C(n,s)` bits, the budget is `n(ℓ(s)−1) ≥ 0.415n`, and comparing the two makes every `s ≥ 3` comfortably affordable — bounded `s` costs `O(log n)` against `0.415n`, and large `s = αn` has `ℓ ≈ ½log₂(αn) → ∞` so the budget outruns the cost `nH(α) ≤ n`. Corank `≥ 2` gives `ℓ ≥ 2`, budget `≥ n`, likewise affordable. Everything except `ℓ = 1` clears, and `ℓ = 1` is the answer.

**The error: I dropped the fibre-naming term, which is the entire problem.** The count of components is *not* `C(n,k)`; it is `C(n,k) × N_fibre`, and `N_fibre` — the number of distinct fibres with the given parameters — is what the deterministic programme exists to bound. A rigidity theorem `d_cb ≤ Cℓ` is exactly what converts `N_fibre` into `2^{O(d_cb·k + …)}`. Restoring it, affordability reads `O(C·ℓ·k) < n(ℓ−1)`, i.e. `C·k < n` up to the `ℓ/(ℓ−1)` factor, i.e. with `k = O(n/log n)`: **`C < log n`** — which is W1 again, exactly.

So the crude count does not prove anything; it re-derives the interface and shows, once more, that **fibre naming is the load-bearing cost and rigidity is the only thing that bounds it.** Recorded rather than deleted because the argument is seductive, self-consistent as far as it goes, and lands on "the conjecture follows" — the exact shape of a result that should never be believed. Anyone who reconstructs it should check the same term first.

**Limits.** This is my reconstruction's framework, not the packet's verbatim one (the ambient-vs-Gale-dual parametrization question of `encoding_interface_reconstruction.md` §4 is still open, so constants do not transfer). The multiplicity concern also stands: a singular matrix has many components, and I bound a first moment. Neither affects the *ratio* computed in §3, which is what the question asked for.
