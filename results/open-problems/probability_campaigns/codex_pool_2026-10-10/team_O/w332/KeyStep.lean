import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring

theorem w332_gap (x y : ℚ) (h : x < y) : 0 < y - x := by
  exact sub_pos.mpr h

theorem w332_factor (a y D : ℚ) :
    y*y + 2*a*y - 3*a*a - D*y =
      (y-3*a)*(y+a) + (4*a-D)*y := by
  ring

theorem w332_profile_sign (a y D : ℚ) (ha : 0 ≤ a) (hy : 0 < y)
    (hcurvature : y ≤ 3*a) (hvariance : 4*a ≤ D) :
    (y-3*a)*(y+a) + (4*a-D)*y ≤ 0 := by
  exact add_nonpos
    (mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hcurvature)
      (add_nonneg (le_of_lt hy) ha))
    (mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hvariance) (le_of_lt hy))
