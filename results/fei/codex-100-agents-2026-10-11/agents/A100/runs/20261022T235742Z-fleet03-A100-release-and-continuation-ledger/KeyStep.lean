import Std.Tactic

theorem a100_padding_induction (m : Nat) : 16*m+17 <= 17*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    simp only [Nat.pow_succ]
    omega
