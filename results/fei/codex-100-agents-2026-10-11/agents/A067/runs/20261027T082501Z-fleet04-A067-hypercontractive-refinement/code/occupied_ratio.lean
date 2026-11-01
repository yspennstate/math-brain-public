theorem occupied_ratio (q u k : Nat) (hq : 0 < q)
    (hu : u <= 2*k*k) : u <= (2*k*k)*q := by
  have h : 1 <= q := hq
  have hmul := Nat.mul_le_mul_left (2*k*k) h
  exact Nat.le_trans hu (by simpa only [Nat.mul_one] using hmul)
