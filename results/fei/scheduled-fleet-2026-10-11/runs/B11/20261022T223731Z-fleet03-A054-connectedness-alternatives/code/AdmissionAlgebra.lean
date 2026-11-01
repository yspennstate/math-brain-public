import Mathlib.Tactic

-- This isolates only the normalized final bank rearrangement.
-- It does not formalize entropy, component labels, or the prior transfer.
theorem admission_bank_rearrangement
    (h n b i q : ℝ) (hi : i ≤ q) (hh : h = n - i + b) :
    n - q + b ≤ h := by
  linarith

theorem fiber_threshold_requires_influence
    (p w i : ℝ) (hbound : 2 * w ≤ i) (hpaid : p ≤ 2 * w) :
    p ≤ i := by
  exact le_trans hpaid hbound

-- Not compiled in this stage: memok returned WAIT before admission.
