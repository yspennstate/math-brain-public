import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- The algebraic cancellation used by the mean-field proof, without division.
theorem weighted_drift_identity (b1 b2 d1 d2 v : ℝ) :
    b1 * (b2 * v - d2) - b2 * (b1 * v - d1) =
      b2 * d1 - b1 * d2 := by
  ring

theorem weighted_drift_negative (b1 b2 d1 d2 v : ℝ)
    (h : b2 * d1 < b1 * d2) :
    b1 * (b2 * v - d2) - b2 * (b1 * v - d1) < 0 := by
  rw [weighted_drift_identity]
  linarith

-- The exact residual when the two types see different vacancy probabilities.
theorem spatial_residual_identity (b1 b2 d1 d2 q1 q2 : ℝ) :
    b1 * (b2 * q2 - d2) - b2 * (b1 * q1 - d1) =
      b1 * b2 * (q2 - q1) + b2 * d1 - b1 * d2 := by
  ring
