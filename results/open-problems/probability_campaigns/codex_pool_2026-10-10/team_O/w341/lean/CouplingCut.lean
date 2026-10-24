theorem coupling_scaled_cut_bound (u v c n : Nat) (hv : v ≤ n) :
    u * v - c * c ≤ u * n := by
  exact Nat.le_trans (Nat.sub_le (u * v) (c * c)) (Nat.mul_le_mul_left u hv)
