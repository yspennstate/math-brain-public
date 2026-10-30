import Mathlib

-- Auxiliary pointwise source-envelope step only. Not compiled: memory admission held.
example (a b : ℝ) : (a + b)^2 ≤ 2*a^2 + 2*b^2 := by
  nlinarith [sq_nonneg (a-b)]
