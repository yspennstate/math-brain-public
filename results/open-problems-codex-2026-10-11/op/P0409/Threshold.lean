import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- The algebra responsible for nested exclusion sets on one outgoing edge.
theorem threshold_monotone (a b q r : ℝ)
    (hab : a ≤ b) (hqr : q ≤ r)
    (hq : 0 < 1 - b * q) (hr : 0 < 1 - b * r) :
    (1 - a * q) / (1 - b * q) ≤ (1 - a * r) / (1 - b * r) := by
  apply (div_le_div_iff₀ hq hr).2
  have h : 0 ≤ (b - a) * (r - q) := mul_nonneg (sub_nonneg.mpr hab) (sub_nonneg.mpr hqr)
  nlinarith

theorem threshold_above_one (a b q : ℝ)
    (hq : 0 < q) (hden : 0 < 1 - b * q) :
    1 < (1 - a * q) / (1 - b * q) ↔ a < b := by
  rw [lt_div_iff₀ hden]
  constructor
  · intro h
    nlinarith
  · intro h
    have hm : 0 < (b-a)*q := mul_pos (sub_pos.mpr h) hq
    nlinarith
