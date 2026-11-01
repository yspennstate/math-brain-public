import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Algebraic interpolation step used between adjacent dyadic indices.
theorem average_between_dyadic_bounds (a b n m : ℝ)
    (hab : a ≤ b) (hb : 0 ≤ b) (hn : 0 < n) (hm : 0 < m)
    (hmn : m ≤ 2 * n) : a / n ≤ (2 * b) / m := by
  apply (div_le_div_iff₀ hn hm).2
  have h1 : a * m ≤ b * m := mul_le_mul_of_nonneg_right hab hm.le
  have h2 : b * m ≤ b * (2 * n) := mul_le_mul_of_nonneg_left hmn hb
  nlinarith
