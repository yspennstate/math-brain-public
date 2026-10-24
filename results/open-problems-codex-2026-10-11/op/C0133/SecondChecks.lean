import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- Three-step cylinder probability after integrating two opposite cookie biases.
theorem opposite_cookie_path (q a : Real) :
    (((q + a) * (q - a) + (q - a) * (q + a)) / 2) * q =
      q ^ 3 - q * a ^ 2 := by ring

-- The corresponding cylinder in a persistent, exchangeable sign mixture.
theorem persistent_cookie_path (q a : Real) :
    (((q + a) ^ 2 + (q - a) ^ 2) / 2) * q =
      q ^ 3 + q * a ^ 2 := by ring

theorem opposite_cookie_not_marginal_walk (q a : Real) (hq : 0 < q) (ha : 0 < a) :
    (((q + a) * (q - a) + (q - a) * (q + a)) / 2) * q < q ^ 3 := by
  rw [opposite_cookie_path]
  have hp : 0 < q * a ^ 2 := mul_pos hq (sq_pos_of_pos ha)
  linarith

-- Negative pair covariance cannot arise from a two-component IID mixture.
theorem mixture_pair_covariance (t a b : Real) :
    t * a ^ 2 + (1 - t) * b ^ 2 - (t * a + (1 - t) * b) ^ 2 =
      t * (1 - t) * (a - b) ^ 2 := by ring

theorem mixture_pair_covariance_nonnegative (t a b : Real)
    (ht : 0 <= t) (ht1 : t <= 1) :
    0 <= t * a ^ 2 + (1 - t) * b ^ 2 - (t * a + (1 - t) * b) ^ 2 := by
  rw [mixture_pair_covariance]
  exact mul_nonneg (mul_nonneg ht (sub_nonneg.mpr ht1)) (sq_nonneg (a - b))

#print axioms opposite_cookie_path
#print axioms persistent_cookie_path
#print axioms opposite_cookie_not_marginal_walk
#print axioms mixture_pair_covariance_nonnegative
