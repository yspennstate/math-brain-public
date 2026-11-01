import Lean
theorem lifted_scaling (t b w k : Nat) : (t^k * w) * b^k = (t*b)^k * w := by
  simp [Nat.mul_pow, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
