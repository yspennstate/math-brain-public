-- UNCOMPILED: fresh memory-admission gate refused this stage.
-- This is only the scalar bookkeeping step.
import Mathlib.Tactic.Linarith
theorem postreset_payment (S0 S1 L B w : Real)
    (h0 : S0 >= 2) (h1 : S1 >= 2) (hL : L < 39/32)
    (hB : B <= 7/32) (hw : w <= 11/32) :
    S1 - (L+B+w+max 0 (S1-S0)) > 7/32 := by
  by_cases h : S1-S0 <= 0
  · rw [max_eq_left h]
    linarith
  · rw [max_eq_right (le_of_not_ge h)]
    linarith
