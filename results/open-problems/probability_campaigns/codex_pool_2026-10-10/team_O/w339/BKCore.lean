import Mathlib.Tactic

theorem w339_bk_product_bound (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    1 - a - b ≤ (1 - a) * (1 - b) := by
  nlinarith [mul_nonneg ha hb]
