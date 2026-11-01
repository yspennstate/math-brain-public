import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

-- Arithmetic in the total variation computation. The probabilistic cycle
-- and coupling arguments are NOT formalized by these statements.
theorem uniform_except_start_tv (n : ℚ) (hn : n ≠ 0) (hn1 : n - 1 ≠ 0) :
    (1 / n + (n - 1) * (1 / (n - 1) - 1 / n)) / 2 = 1 / n := by
  field_simp [hn, hn1]
  <;> ring

theorem cycle_three_value : (1 / (3 : ℚ) + 2 * (1 / 2 - 1 / 3)) / 2 = 1 / 3 := by
  norm_num
