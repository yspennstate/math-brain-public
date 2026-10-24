import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

theorem w334_arithmetic_checks (C : ℝ) :
    C^2 * (C+1) - 4 * (C^2-1) = (C-2)^2 * (C+1) ∧
    (61 : ℚ)/240 - 14/55 = -(1 : ℚ)/2640 ∧
    (9 : ℚ)/16 + 2/10000 - (2/3)*(77/100)^2 = 5023/30000 := by
  constructor
  · ring
  · constructor <;> norm_num
