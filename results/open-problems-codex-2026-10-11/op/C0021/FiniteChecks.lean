import Mathlib.Tactic.NormNum

-- These check the algebraic consequences, not the Python DP or its optimum.
theorem depth_two_improves_greedy : (393 : ℚ) / 64 < (5 / 2 : ℚ)^2 := by
  norm_num
theorem depth_two_revealment : ((393 : ℚ) / 64) / 9 = 131 / 192 := by
  norm_num
theorem depth_three_improves_two_blocks :
    ((15796051 : ℚ) / 1048576)^2 < ((393 : ℚ) / 64)^3 := by
  norm_num
theorem cost_floor_two : (9 / 4 : ℚ)^2 ≤ 393 / 64 := by
  norm_num
theorem cost_floor_three : (9 / 4 : ℚ)^3 ≤ 15796051 / 1048576 := by
  norm_num
theorem greedy_vs_three : (15796051 : ℚ) / 1048576 < (5 / 2 : ℚ)^3 := by
  norm_num
#print axioms depth_three_improves_two_blocks
