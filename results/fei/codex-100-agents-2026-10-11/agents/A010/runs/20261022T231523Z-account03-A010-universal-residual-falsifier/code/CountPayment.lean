import Mathlib

-- Key adjacent-ratio step in the child-count/composition payment.
theorem count_ratio (c : Nat) : (c+2)*(c+3) <= 6*(c+1)*(c+1) := by
  nlinarith [Nat.zero_le (c*c)]

#print axioms count_ratio
