import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Basic

-- Only the finite capacity inequality and complement-order step are formalized.
theorem packing_capacity_obstruction (appetite count capacity : ℝ)
    (ha : 0 < appetite) (hc : capacity < count) :
    ¬ appetite * count ≤ appetite * capacity := by
  exact not_le_of_gt (mul_lt_mul_of_pos_left hc ha)

theorem vacant_antitone {X : Type*} {small large : Set X}
    (h : small ⊆ large) : largeᶜ ⊆ smallᶜ := by
  intro x hx hs
  exact hx (h hs)
