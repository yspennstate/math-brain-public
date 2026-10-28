theorem a061_scaled_max (a b c : Nat) (h : b ≤ 2 * a) :
    max b (2 * c) ≤ 2 * max a c := by
  apply Nat.max_le.mpr
  constructor
  · exact Nat.le_trans h (Nat.mul_le_mul_left 2 (Nat.le_max_left a c))
  · exact Nat.mul_le_mul_left 2 (Nat.le_max_right a c)
