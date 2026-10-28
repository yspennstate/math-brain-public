theorem a015_linear_le_pow (n : Nat) : n + 1 <= 2 ^ n := by
  induction n with
  | zero => decide
  | succ n ih =>
    calc
      n + 1 + 1 <= (n + 1) + (n + 1) :=
        Nat.add_le_add_left (Nat.succ_le_succ (Nat.zero_le n)) (n + 1)
      _ <= 2 ^ n + 2 ^ n := Nat.add_le_add ih ih
      _ = 2 ^ (n + 1) := by simp [Nat.pow_succ, Nat.mul_succ]
