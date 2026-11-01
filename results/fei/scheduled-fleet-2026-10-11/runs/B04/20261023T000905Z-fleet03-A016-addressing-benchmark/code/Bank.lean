import Mathlib

-- Rational consequences only; entropy/Fourier hypotheses are not formalized.
theorem tensor_bank (r u : ℚ) (hr : 15/8 < r) (hu : u < 5/8) : 5/4 < r-u := by
  linarith

theorem padding_bank (r u : ℚ) (hr : 39/32 < r) (hu : u < 5/8) : 19/32 < r-u := by
  linarith
