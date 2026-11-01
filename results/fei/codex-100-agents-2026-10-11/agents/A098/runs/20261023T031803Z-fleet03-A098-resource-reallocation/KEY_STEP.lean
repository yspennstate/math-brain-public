import Mathlib

-- Only the scalar cancellation in the nonempty calibration identity.
example (a t x w : ℚ) (ha : a ≠ 0) (ht : t ≠ 0) :
    ((1-w)/(a*t))*(a*x) = ((1-w)/t)*x := by
  field_simp <;> ring
