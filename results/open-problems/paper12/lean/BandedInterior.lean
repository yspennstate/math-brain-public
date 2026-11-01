/-
Interior-row count for the finite-section bound on banded Toeplitz symbols.

This file formalizes the counting identity underlying Lemma `lem:band` in
`paper12/matrix_spencer_lifts.tex`.

In the proof of that lemma, for a degree-`w` symbol and a `d × d` Toeplitz
section `T_d(p)`, the rows `r` with `w ≤ r ≤ d - 1 - w` are exactly the rows on
which the convolution sum `(T_d(p) x)_r` "sees" the full symbol, and the lower
bound `‖T_d(p)‖² ≥ ((d - 2w)/d) ‖p‖∞²` comes from there being `d - 2w` such
interior rows when `d > 2w`.

The combinatorial content is: the set of interior rows
`{ r | w ≤ r ∧ r < d - w }` has exactly `d - 2w` elements when `2w ≤ d`.
Equivalently these are the rows `w ≤ r ≤ d - 1 - w`, since for naturals
`r ≤ d - 1 - w ↔ r < d - w` in the relevant range.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

open Finset

namespace BandedInterior

/-- The finite set of **interior rows** of a `d × d` banded section with
half-bandwidth `w`: those `r` with `w ≤ r < d - w`. -/
def interiorRows (d w : ℕ) : Finset ℕ := Finset.Ico w (d - w)

/-- **Interior-row count.** If `2w ≤ d` then there are exactly `d - 2w`
interior rows. This is the count used in the proof of `lem:band`. -/
theorem card_interiorRows {d w : ℕ} (h : 2 * w ≤ d) :
    (interiorRows d w).card = d - 2 * w := by
  unfold interiorRows
  rw [Nat.card_Ico]
  -- `(d - w) - w = d - 2 * w`
  omega

/-- A row `r` is interior iff `w ≤ r` and `r < d - w` (the membership
unfolding, recorded for downstream use). -/
theorem mem_interiorRows {d w r : ℕ} :
    r ∈ interiorRows d w ↔ w ≤ r ∧ r < d - w := by
  unfold interiorRows
  rw [Finset.mem_Ico]

/-- Reformulation of the interior condition exactly as written in the paper,
`w ≤ r ≤ d - 1 - w`, agrees with `w ≤ r < d - w` when `0 < d`. -/
theorem mem_interiorRows_iff_le {d w r : ℕ} (hd : 0 < d) :
    r ∈ interiorRows d w ↔ w ≤ r ∧ r ≤ d - 1 - w := by
  rw [mem_interiorRows]
  omega

/-- Strict positivity of the interior-row count when the bandwidth is strictly
admissible (`2w < d`), matching the hypothesis `d > 2w` of `lem:band` under
which the lower bound `(d - 2w)/d > 0` is nontrivial. -/
theorem card_interiorRows_pos {d w : ℕ} (h : 2 * w < d) :
    0 < (interiorRows d w).card := by
  rw [card_interiorRows (le_of_lt h)]
  omega

end BandedInterior
