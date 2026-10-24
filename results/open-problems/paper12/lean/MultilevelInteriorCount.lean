/-
Multilevel interior-index count for boxes ∏_j [0, d_j).

This file formalizes the counting identity underlying Lemma `lem:bandml` (the
multilevel / tensor-product version of `lem:band`) in
`paper12/matrix_spencer_lifts.tex`.

Setting: a box `∏_{j} [0, d_j)` of multi-indices, where each axis `j` carries a
per-axis half-bandwidth `w_j` with `d_j > 2 w_j`. A multi-index `m` is
**fully interior** when it is interior in *every* coordinate, i.e.

  `w_j ≤ m_j ≤ d_j - 1 - w_j`   for all `j`,

equivalently `w_j ≤ m_j < d_j - w_j` for all `j`. The multilevel finite-section
lower bound rests on the count of such multi-indices being

  `∏_j (d_j - 2 w_j)`,

the product over axes of the one-dimensional interior-row counts.

The proof reduces the product count to the one-dimensional case: the set of
fully-interior multi-indices is the dependent product (`Fintype.piFinset`) of
the per-axis interior-row sets `BandedInterior.interiorRows (d j) (w j)`, so
`Fintype.card_piFinset` turns its cardinality into the product of the per-axis
cardinalities, each of which is `d_j - 2 w_j` by
`BandedInterior.card_interiorRows`.

Reuses `BandedInterior.lean` (the 1-D count) verbatim.

Compiles against `mathlib` (see `README.md`).
-/

import Mathlib.Data.Fintype.BigOperators
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import BandedInterior

open Finset

namespace MultilevelInteriorCount

variable {ι : Type*} [DecidableEq ι] [Fintype ι]

/-- The finite set of **fully-interior multi-indices** of the box
`∏_j [0, d_j)` with per-axis half-bandwidths `w`: the dependent product over
the axes of the one-dimensional interior-row sets
`BandedInterior.interiorRows (d j) (w j)`.

A multi-index `m : ι → ℕ` lies in this set iff, in every coordinate `j`, it is
an interior row of the `d j × d j` section with half-bandwidth `w j`, i.e.
`w j ≤ m j < d j - w j`. -/
def interiorIndices (d w : ι → ℕ) : Finset (ι → ℕ) :=
  Fintype.piFinset (fun j => BandedInterior.interiorRows (d j) (w j))

/-- A multi-index is fully interior iff it is interior in every coordinate:
`w j ≤ m j` and `m j < d j - w j` for all axes `j`. -/
theorem mem_interiorIndices {d w : ι → ℕ} {m : ι → ℕ} :
    m ∈ interiorIndices d w ↔ ∀ j, w j ≤ m j ∧ m j < d j - w j := by
  unfold interiorIndices
  rw [Fintype.mem_piFinset]
  -- Each per-axis membership is `BandedInterior.mem_interiorRows`.
  exact forall_congr' fun j => BandedInterior.mem_interiorRows

/-- Reformulation of the fully-interior condition exactly as written in the
paper, `w j ≤ m j ≤ d j - 1 - w j` in every coordinate, valid when every axis
length is positive (`0 < d j`). -/
theorem mem_interiorIndices_iff_le {d w : ι → ℕ} {m : ι → ℕ}
    (hd : ∀ j, 0 < d j) :
    m ∈ interiorIndices d w ↔ ∀ j, w j ≤ m j ∧ m j ≤ d j - 1 - w j := by
  rw [mem_interiorIndices]
  exact forall_congr' fun j => by have := hd j; omega

/-- **Multilevel interior-index count.** If `2 w_j ≤ d_j` on every axis, then
the number of fully-interior multi-indices of the box `∏_j [0, d_j)` is

  `∏_j (d_j - 2 w_j)`.

This is the count used in the proof of `lem:bandml`. The proof reduces to the
one-dimensional `BandedInterior.card_interiorRows` via `Fintype.card_piFinset`. -/
theorem card_interiorIndices {d w : ι → ℕ} (h : ∀ j, 2 * w j ≤ d j) :
    (interiorIndices d w).card = ∏ j, (d j - 2 * w j) := by
  unfold interiorIndices
  rw [Fintype.card_piFinset]
  -- Replace each per-axis factor by the 1-D count `d j - 2 * w j`.
  exact Finset.prod_congr rfl fun j _ => BandedInterior.card_interiorRows (h j)

/-- Strict positivity of the multilevel interior-index count when every axis is
strictly admissible (`2 w_j < d_j`, i.e. the lemma's hypothesis `d_j > 2 w_j`).
Each factor `d_j - 2 w_j` is then positive, so their product is positive. -/
theorem card_interiorIndices_pos {d w : ι → ℕ} (h : ∀ j, 2 * w j < d j) :
    0 < (interiorIndices d w).card := by
  rw [card_interiorIndices (fun j => le_of_lt (h j))]
  -- A finite product of positive naturals is positive.
  apply Finset.prod_pos
  intro j _
  have := h j
  omega

/-! ### `Fin r` specialization

The paper indexes the `r` levels by `j = 1, …, r`; the statements above with
`ι := Fin r` give exactly the box `∏_{j} [0, d_j)` over `r` axes. We record the
two main results in this form for direct use. -/

/-- The multilevel count for an `r`-fold box `∏_{j : Fin r} [0, d_j)`:
the number of fully-interior multi-indices is `∏_{j : Fin r} (d_j - 2 w_j)`
when `2 w_j ≤ d_j` on every axis. -/
theorem card_interiorIndices_fin {r : ℕ} {d w : Fin r → ℕ}
    (h : ∀ j, 2 * w j ≤ d j) :
    (interiorIndices d w).card = ∏ j, (d j - 2 * w j) :=
  card_interiorIndices h

/-- Positivity of the `r`-fold count under the lemma's hypothesis `d_j > 2 w_j`
on every axis. -/
theorem card_interiorIndices_fin_pos {r : ℕ} {d w : Fin r → ℕ}
    (h : ∀ j, 2 * w j < d j) :
    0 < (interiorIndices d w).card :=
  card_interiorIndices_pos h

end MultilevelInteriorCount
