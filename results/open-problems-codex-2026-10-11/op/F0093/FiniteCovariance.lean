import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- Exact finite algebra behind the conditional-iid covariance argument.
theorem conditional_two_point_covariance (w a b : ℝ) :
    w * a^2 + (1-w) * b^2 - (w*a + (1-w)*b)^2 =
      w * (1-w) * (a-b)^2 := by
  ring

theorem conditional_two_point_covariance_nonneg (w a b : ℝ)
    (hw : 0 ≤ w) (hw1 : w ≤ 1) :
    0 ≤ w * a^2 + (1-w) * b^2 - (w*a + (1-w)*b)^2 := by
  rw [conditional_two_point_covariance]
  exact mul_nonneg (mul_nonneg hw (sub_nonneg.mpr hw1)) (sq_nonneg (a-b))

-- Scalar entry identity used in the tensor total-variation bound.
theorem tensor_difference (a b p q : ℝ) :
    a*b-p*q = (a-p)*b+p*(b-q) := by
  ring
