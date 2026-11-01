import Std

-- Only the cleared-denominator scalar reset-credit identity is represented.
-- The basis optimization theorem and Fourier realization are not formalized.
-- Compilation was held after fresh compute admission failed.
example (i q a l : Int) : i - q - l = (i - q - a) - (l - a) := by
  omega
