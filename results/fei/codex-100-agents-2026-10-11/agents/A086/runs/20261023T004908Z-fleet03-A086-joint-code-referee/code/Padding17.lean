import Lean
theorem A086_padding17 (m : Nat) : 16*m+17 <= 17*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [Nat.pow_succ]
    omega
