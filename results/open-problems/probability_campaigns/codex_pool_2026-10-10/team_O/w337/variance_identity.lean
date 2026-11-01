import Mathlib.Tactic

theorem w337_variance_identity (a : ℝ) (h1 : 5 - 4 * a ≠ 0)
    (h2 : 2 - a ≠ 0) :
    a ^ 2 + ((5 - 4 * a) / (2 - a)) ^ 2 *
      ((1 - a ^ 2) / (5 - 4 * a)) *
      (1 - (1 - a ^ 2) / (5 - 4 * a)) = 1 := by
  field_simp [h1, h2]
  <;> ring
