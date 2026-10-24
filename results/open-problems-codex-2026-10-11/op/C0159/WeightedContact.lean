import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic

open scoped BigOperators

-- The finite inequality underlying the modular superlevel bound.
theorem contact_cardinality_bound {α : Type*} (s : Finset α)
    (w : α → ℝ) (ε M : ℝ)
    (hε : ∀ x ∈ s, ε ≤ w x)
    (hM : ∑ x ∈ s, w x ≤ M) :
    (s.card : ℝ) * ε ≤ M := by
  calc
    (s.card : ℝ) * ε = ∑ _x ∈ s, ε := by simp
    _ ≤ ∑ x ∈ s, w x := Finset.sum_le_sum hε
    _ ≤ M := hM

-- A closed grandparent-cone boundary has strictly positive probability.
theorem separator_probability_positive (p : ℝ) (hp : p < 1) (k : ℕ) :
    0 < (1 - p) ^ k := pow_pos (sub_pos.mpr hp) k
