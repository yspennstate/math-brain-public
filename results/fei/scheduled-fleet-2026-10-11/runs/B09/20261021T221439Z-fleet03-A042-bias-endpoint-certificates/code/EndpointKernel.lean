theorem endpoint_integer_magnitude (n : Nat) : n ≤ n * n := by
  cases n with
  | zero => exact Nat.le_refl 0
  | succ k =>
    simpa only [Nat.mul_one] using
      Nat.mul_le_mul_left (k + 1) (Nat.succ_le_succ (Nat.zero_le k))
