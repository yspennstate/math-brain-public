import Mathlib.Tactic

theorem a048_scalar (A D R : Real) : A + max (D - 4 * R) 0 = max A (A + D - 4 * R) := by
  by_cases h : D - 4 * R <= 0
  · rw [max_eq_right h, max_eq_left (by linarith : A + D - 4 * R <= A)]
    ring
  · rw [max_eq_left (by linarith : 0 <= D - 4 * R), max_eq_right (by linarith : A <= A + D - 4 * R)]
    ring
