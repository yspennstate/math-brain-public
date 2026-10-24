/-
Grid-norming telescoping inequality.

This file formalizes the elementary core of the grid-norming lemma `lem:grid`
in `paper12/matrix_spencer_lifts.tex`.

Setting: there are `r` axes `j : Fin r`. On axis `j` the grid has size
`G j > 0` and the number of points to be normed is `N j : ℕ`. The lemma needs

  G j ≥ 8 · r · N j   (the design choice of grid size, when N j ≥ 1)

and concludes that the total normalized count is controlled:

  ∑_j (N j) / (G j) ≤ 1 / 8.

In the paper this carries a factor of `π` (each term is `(π / G j) · N j`);
we state it dimensionlessly, dropping `π`, so the constant is `1/8` rather
than `π/8`. The two are equivalent after multiplying through by `π > 0`.

The argument is a per-term bound followed by a count of terms:

* each term satisfies `N j / G j ≤ 1 / (8 r)` — for `N j ≥ 1` this is exactly
  the hypothesis `G j ≥ 8 r (N j)` divided through; for `N j = 0` the term is
  `0 ≤ 1 / (8 r)`;
* there are `r` terms, so `∑_j N j / G j ≤ ∑_j 1 / (8 r) = r · (1 / (8 r)) = 1/8`
  via `Finset.sum_le_sum` and `Finset.sum_const`.

The main statement `grid_sum_le` indexes over `Fin r` so that the number of
terms is literally `r`. A version `grid_sum_le_finset` over an arbitrary
`Finset` (with the count `r` taken to be its cardinality) is also given.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

open Finset

namespace GridNorming

/-! ### The per-term bound -/

/-- **Per-term grid bound.**
Fix `r ≥ 1`, a grid size `G > 0`, and a point count `N : ℕ`.  If the grid is
chosen large enough on axis `j`, i.e. `8 * r * N ≤ G` whenever `N ≥ 1`, then the
normalized term is bounded by `1 / (8 r)`:

  `(N : ℝ) / G ≤ 1 / (8 r)`.

For `N = 0` both this and the hypothesis are trivial (`0 ≤ 1 / (8 r)`); for
`N ≥ 1` it is the hypothesis `8 r N ≤ G` rearranged using `G > 0` and
`8 r > 0`. -/
theorem term_le
    (r : ℕ) (N : ℕ) (G : ℝ)
    (hr : 1 ≤ r) (hG : 0 < G)
    (hbig : 1 ≤ N → 8 * (r : ℝ) * (N : ℝ) ≤ G) :
    (N : ℝ) / G ≤ 1 / (8 * r) := by
  have hr0 : (0 : ℝ) < (r : ℝ) := by exact_mod_cast hr
  have h8r : (0 : ℝ) < 8 * (r : ℝ) := by positivity
  rcases Nat.eq_zero_or_pos N with hN | hN
  · -- `N = 0`: the term is `0`, and `0 ≤ 1 / (8 r)`.
    subst hN
    simp only [Nat.cast_zero, zero_div]
    positivity
  · -- `N ≥ 1`: divide the hypothesis `8 r N ≤ G` through.
    have hN1 : (1 : ℕ) ≤ N := hN
    have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
    have key : 8 * (r : ℝ) * (N : ℝ) ≤ G := hbig hN1
    -- `N / G ≤ 1 / (8 r)` iff `N * (8 r) ≤ 1 * G = G`, given `G, 8r > 0`.
    rw [div_le_div_iff₀ hG h8r, one_mul]
    -- goal: `N * (8 * r) ≤ G`; the hypothesis is `8 * r * N ≤ G`.
    calc (N : ℝ) * (8 * (r : ℝ)) = 8 * (r : ℝ) * (N : ℝ) := by ring
      _ ≤ G := key

/-! ### The telescoped sum over `Fin r` -/

/-- **Grid-norming inequality (`lem:grid`, dimensionless core).**
With `r ≥ 1` axes `j : Fin r`, grid sizes `G j > 0`, and point counts
`N j : ℕ`, suppose each axis is gridded finely enough:

  `8 * r * (N j) ≤ G j`   whenever `N j ≥ 1`.

Then the total normalized count obeys

  `∑_{j : Fin r} (N j : ℝ) / (G j) ≤ 1 / 8`.

Proof: each term is `≤ 1 / (8 r)` by `term_le`; summing the `r` constant
bounds gives `r · (1 / (8 r)) = 1 / 8`. -/
theorem grid_sum_le
    (r : ℕ) (hr : 1 ≤ r) (N : Fin r → ℕ) (G : Fin r → ℝ)
    (hG : ∀ j, 0 < G j)
    (hbig : ∀ j, 1 ≤ N j → 8 * (r : ℝ) * (N j : ℝ) ≤ G j) :
    (∑ j : Fin r, (N j : ℝ) / G j) ≤ 1 / 8 := by
  have hr0 : (0 : ℝ) < (r : ℝ) := by exact_mod_cast hr
  -- Bound each term by the constant `1 / (8 r)`.
  have hterm : ∀ j ∈ (Finset.univ : Finset (Fin r)),
      (N j : ℝ) / G j ≤ 1 / (8 * r) :=
    fun j _ => term_le r (N j) (G j) hr (hG j) (hbig j)
  calc
    (∑ j : Fin r, (N j : ℝ) / G j)
        ≤ ∑ _j : Fin r, (1 : ℝ) / (8 * r) := Finset.sum_le_sum hterm
    _ = (Finset.univ : Finset (Fin r)).card • ((1 : ℝ) / (8 * r)) :=
          Finset.sum_const _
    _ = r • ((1 : ℝ) / (8 * r)) := by rw [Finset.card_univ, Fintype.card_fin]
    _ = (r : ℝ) * ((1 : ℝ) / (8 * r)) := by rw [nsmul_eq_mul]
    _ = 1 / 8 := by
          have hrne : (r : ℝ) ≠ 0 := ne_of_gt hr0
          field_simp

/-! ### The telescoped sum over an arbitrary `Finset`

Same statement with the index set an arbitrary `Finset ι`; the "number of
axes" `r` is its cardinality. -/

/-- **Grid-norming inequality over a general index `Finset`.**
For a finite index set `s` with `r := s.card ≥ 1`, grid sizes `G j > 0`, and
point counts `N j : ℕ` satisfying `8 * r * (N j) ≤ G j` whenever `N j ≥ 1`,

  `∑_{j ∈ s} (N j : ℝ) / (G j) ≤ 1 / 8`.

The proof is identical: termwise `≤ 1 / (8 r)`, then `s.card = r` terms sum to
`r · (1 / (8 r)) = 1 / 8`. -/
theorem grid_sum_le_finset
    {ι : Type*} (s : Finset ι) (hs : 1 ≤ s.card)
    (N : ι → ℕ) (G : ι → ℝ)
    (hG : ∀ j ∈ s, 0 < G j)
    (hbig : ∀ j ∈ s, 1 ≤ N j → 8 * (s.card : ℝ) * (N j : ℝ) ≤ G j) :
    (∑ j ∈ s, (N j : ℝ) / G j) ≤ 1 / 8 := by
  set r : ℕ := s.card with hr_def
  have hr0 : (0 : ℝ) < (r : ℝ) := by exact_mod_cast hs
  have hterm : ∀ j ∈ s, (N j : ℝ) / G j ≤ 1 / (8 * r) :=
    fun j hj => term_le r (N j) (G j) hs (hG j hj) (hbig j hj)
  calc
    (∑ j ∈ s, (N j : ℝ) / G j)
        ≤ ∑ _j ∈ s, (1 : ℝ) / (8 * r) := Finset.sum_le_sum hterm
    _ = s.card • ((1 : ℝ) / (8 * r)) := Finset.sum_const _
    _ = (r : ℝ) * ((1 : ℝ) / (8 * r)) := by rw [← hr_def, nsmul_eq_mul]
    _ = 1 / 8 := by
          have hrne : (r : ℝ) ≠ 0 := ne_of_gt hr0
          field_simp

end GridNorming
