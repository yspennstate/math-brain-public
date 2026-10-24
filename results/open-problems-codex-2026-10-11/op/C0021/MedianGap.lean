import Mathlib.Tactic.NormNum

theorem median_depth_three_gap :
    (257554309 : ℚ) / 16777216 - 15796051 / 1048576 = 4817493 / 16777216 := by
  norm_num
theorem median_depth_three_strictly_worse :
    (15796051 : ℚ) / 1048576 < 257554309 / 16777216 := by
  norm_num
theorem fixed_median_depth_two_strictly_worse : (393 : ℚ) / 64 < 199 / 32 := by
  norm_num
theorem local_median_regret :
    (3031947 : ℚ) / 262144 - 3028131 / 262144 = 477 / 32768 := by
  norm_num
theorem local_median_regret_positive : (0 : ℚ) < 477 / 32768 := by
  norm_num
#print axioms median_depth_three_gap
