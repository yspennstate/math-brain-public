import Mathlib.Tactic

namespace A059

-- This is the scalar ledger step, conditional on the universal one-query input.
theorem release_nonnegative (I p d : ℚ) (h : d ≤ (29/13 : ℚ)*I) :
    (58/13 : ℚ)*I - d - (29/13 : ℚ)*(I-p) ≥ (29/13 : ℚ)*p := by
  linarith

theorem original_source_split :
    (9/2 : ℚ) = 2*(29/13 : ℚ) + (1/26 : ℚ) := by
  norm_num

end A059
