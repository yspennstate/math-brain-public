import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

theorem scaled_variance_loss_identity (A u v : ℝ) :
    A * (u + v) ^ 2 - ((A - 1) * u ^ 2 - A * (A - 1) * v ^ 2) =
      (u + A * v) ^ 2 := by
  ring

theorem scaled_variance_loss (A u v : ℝ) :
    (A - 1) * u ^ 2 - A * (A - 1) * v ^ 2 ≤ A * (u + v) ^ 2 := by
  apply sub_nonneg.mp
  rw [scaled_variance_loss_identity]
  exact sq_nonneg _

theorem cubic_increment (t : ℝ) :
    (t + 1) ^ 3 - t ^ 3 = 3 * t ^ 2 + 3 * t + 1 := by
  ring
