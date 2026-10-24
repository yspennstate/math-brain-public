import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

-- The pointwise comparison used to pass from good Fourier bands to finite energy.
theorem energy_weight_comparison (a b k : ℝ) (hb : 0 < b)
    (h : b ≤ k * a) : 1 / b ≤ k * (a / b ^ 2) := by
  calc
    1 / b = b / b ^ 2 := by field_simp
    _ ≤ (k * a) / b ^ 2 :=
      div_le_div_of_nonneg_right h (le_of_lt (sq_pos_of_pos hb))
    _ = k * (a / b ^ 2) := by ring

-- Exact exponent margins of the construction and its good bands.
example : (3 : ℚ) / 64 < 1 / 8 := by norm_num
example : (1 : ℚ) / 8 < 1 / 4 := by norm_num
example : (4 : ℚ) * (9 / 8) < 5 := by norm_num
example : (5 : ℚ) - 4 ≤ 5 / 4 := by norm_num
example : (1 : ℚ) / 16 < 1 / 2 := by norm_num
