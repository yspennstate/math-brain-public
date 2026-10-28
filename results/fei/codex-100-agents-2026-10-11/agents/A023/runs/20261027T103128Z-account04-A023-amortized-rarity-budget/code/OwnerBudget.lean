theorem originalAccount (q m u root : Nat) (h : root = q + m + u) : q + m <= root := by
  rw [h]
  exact Nat.le_add_right (q + m) u
