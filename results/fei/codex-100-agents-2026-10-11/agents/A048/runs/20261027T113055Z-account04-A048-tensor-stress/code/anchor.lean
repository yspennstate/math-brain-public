import Mathlib.Tactic

theorem A048_anchor_square (a b : ℚ) :
    ((a + b)^2 + (a - b)^2) / 2 = a^2 + b^2 := by
  ring

theorem A048_bank_drop (n a b : ℚ) (hn : 2 ≤ n) (hb : 0 ≤ b) :
    a - b ≤ (n - 1)*a - (n - 2)*(a - b) := by
  nlinarith
