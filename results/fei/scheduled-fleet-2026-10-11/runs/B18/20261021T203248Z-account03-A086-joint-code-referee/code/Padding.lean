import Lean
theorem A086_padding_bound (m : Nat) : 16*m+37 <= 37*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [Nat.pow_succ]
    omega
