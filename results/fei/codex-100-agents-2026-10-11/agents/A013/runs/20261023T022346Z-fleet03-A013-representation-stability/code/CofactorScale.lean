import Mathlib

-- Auxiliary Bayes scaling identity only. Compiler admission was refused.
-- This is not a formalization of conditional probabilities or of FEI.
example (u : ℚ) (a t : ℕ) :
    (u / (2:ℚ)^a) / ((2:ℚ)^t / (2:ℚ)^a) = u / (2:ℚ)^t := by
  have ha : (2:ℚ)^a ≠ 0 := pow_ne_zero a (by norm_num)
  have ht : (2:ℚ)^t ≠ 0 := pow_ne_zero t (by norm_num)
  field_simp
