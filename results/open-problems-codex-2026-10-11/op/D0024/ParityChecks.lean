import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

-- The finite moment identity responsible for the nonproduct invariant law.
theorem mixture_covariance (u v : ℚ) :
    ((1-u)^2 + (1-v)^2)/2 - (((1-u)+(1-v))/2)^2
      = (u-v)^2/4 := by
  ring

theorem chosen_covariance :
    (((1-(1/3 : ℚ))^2 + (1-(2/3 : ℚ))^2)/2
      - (((1-(1/3 : ℚ))+(1-(2/3 : ℚ)))/2)^2) = 1/36 := by
  norm_num

theorem chosen_density :
    (((1/3 : ℚ)/(1-1/3)) + ((2/3 : ℚ)/(1-2/3)))/2 = 5/4 := by
  norm_num

-- Multiplication by a positive site rate gives the empty-site obstruction.
theorem critical_empty_obstruction (a e : ℚ)
    (ha : 0 < a) (hupper : a ≤ 3/4)
    (he : a * e = a - 1/2) : e < 1/2 := by
  by_contra h
  have hl : 1/2 ≤ e := le_of_not_gt h
  have hprod : a * (1/2) ≤ a * e := mul_le_mul_of_nonneg_left hl (le_of_lt ha)
  nlinarith

theorem supercritical_density : (5 : ℚ) > 4 := by
  norm_num
