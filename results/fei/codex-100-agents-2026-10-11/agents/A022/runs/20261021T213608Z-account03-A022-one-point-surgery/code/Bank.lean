import Mathlib

-- This certifies only the rational last step of REPORT section 6.
theorem a022_original_bank
    (t w J s c S : ℚ) (ht : 2 ≤ t) (hw0 : 0 ≤ w)
    (hw : w ≤ 1/64) (hJ : J ≤ 2*t) (hs : -3*t ≤ s)
    (hc : c ≤ 3/2) (hS : 3*t/4 ≤ S) :
    w*(4*J+12*t+4*c-8*s)+t/64 ≤ S := by
  have hx : 4*J+12*t+4*c-8*s ≤ 44*t+6 := by linarith
  have hp : 0 ≤ 44*t+6 := by linarith
  have hmul : w*(4*J+12*t+4*c-8*s) ≤ (1/64)*(44*t+6) := by
    calc
      _ ≤ w*(44*t+6) := mul_le_mul_of_nonneg_left hx hw0
      _ ≤ (1/64)*(44*t+6) := mul_le_mul_of_nonneg_right hw hp
  linarith

#print axioms a022_original_bank
