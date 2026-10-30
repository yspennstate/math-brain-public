import Mathlib.Tactic

-- Only the scalar comparison in the prose proof; no entropy formalization.
theorem windmill_scalar (t b : ℚ) (ht : 2 ≤ t) (hb : b ≤ 1/4)
    (hs : 0 ≤ (t - 1/2) * b^2) :
    t - 1/2 - 2*b + (t-1/2)*b^2 ≥ 1 := by
  linarith

theorem windmill_small_cases : (45:ℚ)/16 < 3 ∧ (53:ℚ)/16 < 5 := by
  norm_num
