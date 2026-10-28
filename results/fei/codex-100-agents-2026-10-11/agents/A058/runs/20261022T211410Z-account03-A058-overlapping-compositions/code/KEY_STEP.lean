import Mathlib

-- Mass conservation used in the homogeneous collision correction.
-- This statement alone does not certify the entropy theorem.
example (a b : ℚ) : ((a + b) / 2)^2 + ((a - b) / 2)^2 = (a^2 + b^2)/2 := by ring
