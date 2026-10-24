import Std.Tactic

theorem padding_bound (m : Nat) : 16*m+37 <= 37*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    simp only [Nat.pow_succ]
    omega
