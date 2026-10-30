import Mathlib

-- Only the final scalar deduction. The Fourier/entropy argument is not formalized.
example (C gap E D : ℚ) (hC : C < 7 / 2)
    (hg : 443 / 128 < gap) (hE : 0 ≤ E) (hD : 0 ≤ D) :
    C - gap - 1 - E - D < -(123 / 128) := by
  linarith
